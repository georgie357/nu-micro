# -*- coding: utf-8 -*-
"""Apply the same compaction to labs 3-6 that we did to Lab 2:
- Collapse title block padding -> 2 paragraphs
- Materials bullets -> 1 paragraph
- Tables -> 1 paragraph
- Shrink images to ~3.2" wide
- Single-space all paragraphs
"""
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import xml.etree.ElementTree as ET

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ET.register_namespace('w', W_NS)
EXTRA = {
    'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006',
    'o': 'urn:schemas-microsoft-com:office:office',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
    'v': 'urn:schemas-microsoft-com:vml',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'w10': 'urn:schemas-microsoft-com:office:word',
    'wne': 'http://schemas.microsoft.com/office/word/2006/wordml',
    'sl': 'http://schemas.openxmlformats.org/schemaLibrary/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
    'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
    'lc': 'http://schemas.openxmlformats.org/drawingml/2006/lockedCanvas',
    'dgm': 'http://schemas.openxmlformats.org/drawingml/2006/diagram',
    'wps': 'http://schemas.microsoft.com/office/word/2010/wordprocessingShape',
    'wpg': 'http://schemas.microsoft.com/office/word/2010/wordprocessingGroup',
    'w14': 'http://schemas.microsoft.com/office/word/2010/wordml',
    'w15': 'http://schemas.microsoft.com/office/word/2012/wordml',
    'w16': 'http://schemas.microsoft.com/office/word/2018/wordml',
    'w16cex': 'http://schemas.microsoft.com/office/word/2018/wordml/cex',
    'w16cid': 'http://schemas.microsoft.com/office/word/2016/wordml/cid',
    'cr': 'http://schemas.microsoft.com/office/comments/2020/reactions',
}
for k, v in EXTRA.items(): ET.register_namespace(k, v)
W = lambda tag: f'{{{W_NS}}}{tag}'

def para_text(p):
    return ''.join((t.text or '') for t in p.iter(W('t')))

def replace_para_text(p, new_text, bold=False, center=False):
    runs = list(p.findall(W('r')))
    first_rpr_xml = None
    if bold:
        # build a bold rPr
        first_rpr_xml = f'<w:rPr xmlns:w="{W_NS}"><w:b w:val="1"/><w:bCs w:val="1"/><w:rFonts w:ascii="Times New Roman" w:cs="Times New Roman" w:eastAsia="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="28"/><w:szCs w:val="28"/><w:rtl w:val="0"/></w:rPr>'
    else:
        for r in runs:
            if not any(c.tag in (W('drawing'), W('pict')) for c in r):
                rpr = r.find(W('rPr'))
                if rpr is not None:
                    first_rpr_xml = ET.tostring(rpr, encoding='unicode')
                    break
    keep_runs = []
    for r in runs:
        if any(c.tag in (W('drawing'), W('pict')) for c in r):
            keep_runs.append(r)
        p.remove(r)
    new_r = ET.SubElement(p, W('r'))
    if first_rpr_xml:
        new_r.append(ET.fromstring(first_rpr_xml))
    else:
        rpr = ET.SubElement(new_r, W('rPr'))
        ET.SubElement(rpr, W('rtl')).set(W('val'), '0')
    t = ET.SubElement(new_r, W('t'))
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    t.text = new_text
    for r in keep_runs:
        p.append(r)
    # set centering and single spacing
    pPr = p.find(W('pPr'))
    if pPr is None:
        pPr = ET.Element(W('pPr')); p.insert(0, pPr)
    if center:
        jc = pPr.find(W('jc'))
        if jc is None: jc = ET.SubElement(pPr, W('jc'))
        jc.set(W('val'), 'center')
    sp = pPr.find(W('spacing'))
    if sp is None: sp = ET.SubElement(pPr, W('spacing'))
    sp.set(W('line'), '240'); sp.set(W('lineRule'), 'auto')
    # remove numPr (bullet) if present
    np = pPr.find(W('numPr'))
    if np is not None: pPr.remove(np)


LAB_CONFIG = {
    3: {
        'title_strings': [
            "Lab 3: Pick and Patch Colonies",
            "Library Plate from Backyard Soil for Antibiotic Screening",
            "George Vela",
            "BIO203A — Microbiology Laboratory",
            "Spring 2026",
            "Instructor: Dr. Radu Popa",
            "Source Plate Date: April 30, 2026",
            "Pick and Patch Date: May 5, 2026",
            "Report Submitted: May 2026",
        ],
        'title_combined': "Lab 3: Pick and Patch Colonies — Library Plate from Backyard Soil for Antibiotic Screening",
        'byline': "George Vela | BIO203A — Microbiology Laboratory | Instructor: Dr. Radu Popa | Source plate 4/30/26; pick & patch 5/5/26; report submitted May 2026.",
        'materials_combined': "TSA plate of 10⁻³ dilution of soil; Tryptic Soy Agar library plate; sterile wooden toothpicks; permanent marker; Bunsen burner; incubator.",
        'table_intro': "The seven patches on the library plate (Table 1 in paragraph form):",
        'table_paragraph': "Patch 1 — yellow/cream, smooth, raised, circular (from another student's source plate). Patch 2 — yellow/cream, cluster, slightly rough (own 10⁻³ plate). Patch 3 — white, cluster, rough surface. Patch 4 — white, cluster, rough surface. Patch 5 — white, small, circular units. Patch 6 — white, small, two circles. Patch 7 — white, medium, smooth. (Patches 2–7 from own 10⁻³ plate.)",
    },
    4: {
        'title_strings': [
            "Lab 4: Aseptic Technique",
            "Inoculation of Bacillus subtilis and Escherichia coli on TSA Slant and Deep Culture Tubes",
            "George Vela",
            "BIO203A — Microbiology Laboratory",
            "Spring 2026",
            "Instructor: Dr. Radu Popa",
            "Inoculation Date: May 5, 2026",
            "Report Submitted: May 2026",
        ],
        'title_combined': "Lab 4: Aseptic Technique — Inoculation of Bacillus subtilis and Escherichia coli on TSA Slant and Deep Culture Tubes",
        'byline': "George Vela | BIO203A — Microbiology Laboratory | Instructor: Dr. Radu Popa | Inoculated 5/5/26; report submitted May 2026.",
        'materials_combined': "Bacillus subtilis; Escherichia coli; Tryptic Soy Agar (TSA) slant tubes; TSA deep tubes; inoculating loop; inoculating needle; Bunsen burner and flint/steel; test-tube rack; marker; incubator.",
        'table_intro': None,
        'table_paragraph': None,
    },
    5: {
        'title_strings': [
            "Lab 5: Smears and Simple Staining",
            "Heat-Fixation, and Methylene Blue Staining of a Bacterial Smear",
            "George Vela",
            "BIO203A — Microbiology Laboratory",
            "Spring 2026",
            "Instructor: Dr. Radu Popa",
            "Staining Date: May 7, 2026",
            "Report Submitted: May 2026",
        ],
        'title_combined': "Lab 5: Smears and Simple Staining — Heat-Fixation and Methylene Blue Staining of a Bacterial Smear",
        'byline': "George Vela | BIO203A — Microbiology Laboratory | Instructor: Dr. Radu Popa | Stained 5/7/26; report submitted May 2026.",
        'materials_combined': "Bacterial culture; glass slide; distilled water; inoculating loop; Bunsen burner; marker; methylene blue; staining tray, wash bottle of water, and beaker for waste; bibulous paper; light microscope; Type-A immersion oil; lens paper.",
        'table_intro': None,
        'table_paragraph': None,
    },
    6: {
        'title_strings': [
            "Lab 6: Gram Staining",
            "Differential Gram Staining of a Mixed Smear Containing Escherichia coli and Staphylococcus epidermidis",
            "George Vela",
            "BIO203A — Microbiology Laboratory",
            "Spring 2026",
            "Instructor: Dr. Radu Popa",
            "Staining Sessions: May 7 and May 9, 2026",
            "Report Submitted: May 2026",
        ],
        'title_combined': "Lab 6: Gram Staining — Differential Gram Staining of a Mixed Smear Containing Escherichia coli and Staphylococcus epidermidis",
        'byline': "George Vela | BIO203A — Microbiology Laboratory | Instructor: Dr. Radu Popa | Staining sessions 5/7/26 and 5/9/26; report submitted May 2026.",
        'materials_combined': "Bacterial cultures: Escherichia coli and Staphylococcus epidermidis; glass slides; distilled water; inoculation loop; Bunsen burner and striker; clothespin; crystal violet; Gram's iodine; ethanol; safranin; staining tray; bibulous paper; light microscope; immersion oil.",
        'table_intro': "Gram-stain observations (Table 1 in paragraph form):",
        'table_paragraph': "Escherichia coli — final color pink, Gram-negative (−), bacillus (rod), singles/scattered. Staphylococcus epidermidis — final color purple/darker, Gram-positive (+), coccus (sphere), clusters.",
    },
}


def process_lab(lab):
    path = f'unpacked_lab{lab}/word/document.xml'
    tree = ET.parse(path)
    root = tree.getroot()
    body = root.find(W('body'))
    cfg = LAB_CONFIG[lab]

    # --- 1. Title block collapse ---
    paragraphs = list(body.iter(W('p')))
    title_set = set(cfg['title_strings'])
    first_idx = last_idx = None
    for i, p in enumerate(paragraphs):
        if para_text(p).strip() in title_set:
            if first_idx is None: first_idx = i
            last_idx = i
    if first_idx is not None:
        # Delete empty paragraphs before first_idx
        for p in paragraphs[:first_idx]:
            if not para_text(p).strip():
                try: body.remove(p)
                except ValueError: pass
        # Replace first_idx with bold combined title
        replace_para_text(paragraphs[first_idx], cfg['title_combined'], bold=True, center=True)
        # Find or create byline holder
        inner = paragraphs[first_idx+1:last_idx+1]
        byline_holder = None
        for p in inner:
            if para_text(p).strip():
                byline_holder = p
                break
        for p in inner:
            if p is byline_holder: continue
            try: body.remove(p)
            except ValueError: pass
        if byline_holder is not None:
            replace_para_text(byline_holder, cfg['byline'], center=True)
        # Collapse empties before next non-empty (Scope)
        paragraphs = list(body.iter(W('p')))
        scope_idx = None
        for i, p in enumerate(paragraphs):
            if para_text(p).strip().startswith('Scope'):
                scope_idx = i; break
        if scope_idx is not None and scope_idx > 0:
            empties = []
            for i in range(scope_idx-1, 0, -1):
                if not para_text(paragraphs[i]).strip(): empties.append(paragraphs[i])
                else: break
            for p in empties[1:]:
                try: body.remove(p)
                except ValueError: pass

    # --- 2. Materials -> paragraph ---
    paragraphs = list(body.iter(W('p')))
    first_bullet_idx = None
    bullet_paras = []
    for i, p in enumerate(paragraphs):
        txt = para_text(p).strip()
        if txt.startswith('•'):
            if first_bullet_idx is None: first_bullet_idx = i
            bullet_paras.append(p)
    if first_bullet_idx is not None and bullet_paras:
        replace_para_text(bullet_paras[0], cfg['materials_combined'])
        for p in bullet_paras[1:]:
            try: body.remove(p)
            except ValueError: pass

    # --- 3. Tables -> paragraph ---
    if cfg['table_paragraph']:
        tables = list(body.iter(W('tbl')))
        for tbl in tables:
            # find parent
            parent = None
            for par in body.iter():
                for child in list(par):
                    if child is tbl:
                        parent = par; break
                if parent is not None: break
            if parent is None: continue
            new_p = ET.Element(W('p'))
            pPr = ET.SubElement(new_p, W('pPr'))
            sp = ET.SubElement(pPr, W('spacing'))
            sp.set(W('line'), '240'); sp.set(W('lineRule'), 'auto')
            new_r = ET.SubElement(new_p, W('r'))
            rpr = ET.SubElement(new_r, W('rPr'))
            ET.SubElement(rpr, W('rtl')).set(W('val'), '0')
            t = ET.SubElement(new_r, W('t'))
            t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
            t.text = cfg['table_paragraph']
            idx = list(parent).index(tbl)
            parent.insert(idx, new_p)
            parent.remove(tbl)

    # Write
    tree.write(path, encoding='utf-8', xml_declaration=True)

    # --- 4. Shrink images via regex on raw xml ---
    with open(path, 'r', encoding='utf-8') as f: raw = f.read()
    target_w = 2926080  # 3.2"
    def repl_extent(m):
        cx = int(m.group('cx')); cy = int(m.group('cy'))
        if cx <= target_w: return m.group(0)
        new_cy = int(cy * (target_w / cx))
        return m.group(0).replace(f'cx="{cx}"', f'cx="{target_w}"').replace(f'cy="{cy}"', f'cy="{new_cy}"')
    raw = re.sub(r'<wp:extent[^/>]*cx="(?P<cx>\d+)"[^/>]*cy="(?P<cy>\d+)"[^/]*/?>', repl_extent, raw)
    raw = re.sub(r'<a:ext[^/>]*cx="(?P<cx>\d+)"[^/>]*cy="(?P<cy>\d+)"[^/]*/?>', repl_extent, raw)
    with open(path, 'w', encoding='utf-8') as f: f.write(raw)

    # word + para count
    tree2 = ET.parse(path)
    total = ''
    for t in tree2.iter(W('t')):
        if t.text: total += t.text + ' '
    print(f'Lab {lab}: {len(total.split())} words, {len(list(tree2.iter(W("p"))))} paragraphs')


for lab in [3,4,5,6]:
    process_lab(lab)
