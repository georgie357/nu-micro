# -*- coding: utf-8 -*-
"""
Smarter edit script: matches by paragraph extracted text, then rewrites the
paragraph's runs to a single run with new text. Preserves the paragraph's
properties (w:pPr) and the first run's properties (w:rPr).
"""
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import xml.etree.ElementTree as ET

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ns = {'w': W_NS}
ET.register_namespace('w', W_NS)
# also register other namespaces from document so they don't get prefixed weirdly
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
for k, v in EXTRA.items():
    ET.register_namespace(k, v)

W = lambda tag: f'{{{W_NS}}}{tag}'

def para_text(p):
    out = ''
    for t in p.iter(W('t')):
        if t.text: out += t.text
    return out

def norm(s):
    return re.sub(r'\s+', ' ', s).strip()

def replace_para_text(p, new_text):
    """Replace all text in a paragraph with new_text. Drops existing runs
    that contained only text (no drawings/etc.), keeps the first run's rPr,
    and preserves any runs that have non-text children like w:drawing.
    """
    pPr = p.find(W('pPr'))
    runs = list(p.findall(W('r')))

    # find first text-only run to grab its rPr
    first_rpr = None
    for r in runs:
        children_tags = [c.tag for c in r]
        if not any(c == W('drawing') or c == W('pict') for c in children_tags):
            rpr = r.find(W('rPr'))
            if rpr is not None:
                first_rpr = ET.tostring(rpr, encoding='unicode')
                break

    # Remove all old runs that don't have drawings
    keep_runs = []
    for r in runs:
        children_tags = [c.tag for c in r]
        if any(c == W('drawing') or c == W('pict') for c in children_tags):
            keep_runs.append(r)
        p.remove(r)

    # Build a new single text run
    new_r = ET.SubElement(p, W('r'))
    if first_rpr:
        new_rpr_el = ET.fromstring(first_rpr)
        new_r.append(new_rpr_el)
    else:
        rpr = ET.SubElement(new_r, W('rPr'))
        ET.SubElement(rpr, W('rtl')).set(W('val'), '0')
    t = ET.SubElement(new_r, W('t'))
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    t.text = new_text

    # Re-append any drawing runs back at end
    for r in keep_runs:
        p.append(r)

def delete_para(body, p):
    body.remove(p)

# (lab_num, action, find_text, replace_text)
# action: 'replace' or 'delete'
edits = []

# ===== LAB 2 =====
edits.append((2, 'replace',
    "We used a serial dilution plating method to further isolate a soil sample. The sample was collected from my backyard in North Hollywood, California. There were  two  main objectives: the first was to give a density measurement of the bacterial colonies in the soil. The second objective was to record the diversity of the colonies. diversity of colonies. This will eventually help us progress into the semester-long Antibiotic Discovery Project.",
    "We used a serial dilution plating method to isolate a soil sample collected from my backyard in North Hollywood, California. The two main objectives were to give a density measurement of the bacterial colonies in the soil and to record the diversity of the colonies. This will help us progress into the semester-long Antibiotic Discovery Project."
))
edits.append((2, 'replace',
    "People think negatively of bacteria, surprisingly, not all but a lot of antibiotics were isolated from soil bacteria. For example, Streptomyces is a  Gram-positive, aerobic, spore bacteria. It is found in soil and pharmaceutical companies derived a huge portion of the antibiotics we use today (Parker et al. 2016, §4.4). Looking at soil for anti microbial makes perfect sense.",
    "Surprisingly, many antibiotics were isolated from soil bacteria. For example, Streptomyces is a Gram-positive, aerobic, spore bacteria found in soil from which pharmaceutical companies have derived a huge portion of the antibiotics we use today (Parker et al. 2016, §4.4). Looking at soil for antimicrobials makes sense."
))
edits.append((2, 'replace',
    "Bacteria are very small and naturally found in soil under high density, very difficult to study in natural density (Parker et al. 2016, §1.3). This is where serial dilution comes into use, to have more manageable densities. Serial dilution operates under the idea of viable plate count. This is a count of live cells that replicate and give rise to colonies when incubated (CFU/mL). We use colony forming units because more than one cell may land on the spot that gives rise to a single colony (Parker et al. 2016, §9.1). In serial dilution we are aiming to get plates with CFU counts from 30–300 (Parker et al. 2016, §9.1). The standard is the ten-fold serial dilution method. This is where 1ml of the original culture is added to a tube containing 9.0 mL of sterile diluent. This is a 1:10 dilution. After we draw 1.0 mL and it is once again mixed 9.0 mL of diluent. This continues until we reach the desired concentration (Parker et al. 2016, §9.1). Next we either plate by spread plate or pour plate (Parker et al. 2016, §9.1).",
    "Bacteria are very small and naturally found in soil under high density, making them difficult to study at natural density (Parker et al. 2016, §1.3). Serial dilution gives us more manageable densities. It operates under the idea of viable plate count — a count of live cells that replicate and give rise to colonies when incubated (CFU/mL). We use colony forming units because more than one cell may land on the spot that gives rise to a single colony. The aim is to get plates with CFU counts from 30–300 (Parker et al. 2016, §9.1). The standard ten-fold method adds 1 mL of culture to 9 mL of sterile diluent (1:10) and is repeated until the desired concentration is reached. The dilution is plated by spread plate or pour plate (Parker et al. 2016, §9.1)."
))
edits.append((2, 'replace',
    "After incubation, the 10^-3 plate was looked at and used to  count Colonies. What we counted we could see colonies had unique size, color, surface texture, and edge characteristics. With these measurements we were finally able to do our calculations to obtain measurements needed.",
    "After incubation the 10⁻³ plate was used to count colonies, each with unique size, color, surface texture, and edge characteristics. These measurements enabled the calculations below."
))
edits.append((2, 'replace',
    "Density 2.7 × 10⁶ CFU per gram was our calculation. This is close to what was expected however it is on the lower end. What is the published range for one gram of soil is close to what we got (Parker et al. 2016, §4.1). Unfortunately we only had 22 colonies, which is below the reliable range of  30–300 CFU in plates (Parker et al. 2016, §9.1); We would have had better results if we would have used a less dilute suspension (such as 10⁻² in addition to 10⁻³). Also there is much diversity, not all grow on tsa, incubation setting, so we do not see full spectrum that exists §4.1.",
    "Our calculated density of 2.7 × 10⁶ CFU per gram is on the lower end of the published range for one gram of soil (Parker et al. 2016, §4.1). Only 22 colonies grew, below the reliable 30–300 range (Parker et al. 2016, §9.1); a less dilute suspension (10⁻² alongside 10⁻³) would have given better results. Also, not all soil bacteria grow on TSA at our incubation setting, so we do not see the full spectrum that exists (Parker et al. 2016, §4.1)."
))
edits.append((2, 'replace',
    "Serial dilution plating of the soil sample gave density of about 2.7 × 10⁶ colony forming units per gram of soil. This is within the published range (Parker et al. 2016, §4.1). Six colonies on the 10⁻³ plate. These were good enough for the antibiotic-producing isolates in the following labs.",
    "Serial dilution plating of the soil sample gave a density of about 2.7 × 10⁶ colony forming units per gram of soil, within the published range (Parker et al. 2016, §4.1). The six colonies on the 10⁻³ plate were good enough for the antibiotic-producing isolates in the following labs. These methods and techniques are key for the discovery of novel antimicrobial compounds."
))
edits.append((2, 'delete',
    "I can see these methods, techniques are key for the discovery of novel antimicrobial compounds.",
    None
))

# ===== LAB 3 =====
edits.append((3, 'replace',
    "In our history of anti microbial, soil bacteria, has been a great source of clinically useful antimicrobials. A Rutger University professor, Selman Waksman, is a soil microbiologist that discovered actinomycin, streptomycin, and neomycin. These soil bacteria are from Streptomyces (Parker et al. 2016, §14.1). Soil continues to be a great area for the  discovery of antimicrobial agents (Parker et al. 2016, §14.7).",
    "Soil bacteria have been a great source of clinically useful antimicrobials. Rutgers professor Selman Waksman, a soil microbiologist, discovered actinomycin, streptomycin, and neomycin — all from Streptomyces (Parker et al. 2016, §14.1). Soil continues to be a great area for antimicrobial discovery (Parker et al. 2016, §14.7)."
))
edits.append((3, 'replace',
    "However, what should have been done better would have been the total number of patches 7, which is less than the  10–12 recommended for a library plate. Conclusion",
    "Only 7 patches were made, less than the 10–12 recommended for a library plate."
))
edits.append((3, 'replace',
    "A library plate of 7 was successfully constructed by the pick-and-patch technique from the 10⁻³ TSA source plate. Patch pigmented yellow, white colonies as well as fuzzy textured colony of the kind morphologically suggestive of Streptomyces (Parker et al. 2016, §4.4).",
    "A library plate of 7 patches was successfully constructed by pick-and-patch from the 10⁻³ TSA source plate, including pigmented yellow and white colonies as well as a fuzzy textured colony morphologically suggestive of Streptomyces (Parker et al. 2016, §4.4). The library plate is a catalog of candidates for the Antibiotic Discovery Project."
))
edits.append((3, 'delete',
    "The library plate is a catalog of candidates for the Antibiotic Discovery Project.",
    None
))

# ===== LAB 4 =====
edits.append((4, 'replace',
    "We transferred bacterial cultures from stock to agar slants and agar deeps. and Then we recorded growth patterns after incubation. The organism grown have different oxygen requirements, which made them interesting to observe them grow. We grew Bacillus subtilis and Escherichia coli.",
    "We transferred Bacillus subtilis and Escherichia coli from stock to TSA agar slants and deeps, then recorded growth patterns after incubation. These two organisms have different oxygen requirements, which made them interesting to observe."
))
edits.append((4, 'replace',
    "One organism was Bacillus, which are gram-positive, aerobes or facultative anaerobes, that may or may not have endospores (Parker et al. 2016, §4.4). Escherichia coli has the most variety as a bacteria class. We are used to seeing it in the gut and gi processes. Classically seen in pink eye, but also aids with vitamin K (Parker et al. 2016, §4.4). It is know that this bacteria group are facultative anaerobes (Parker et al. 2016, §9.2).",
    "Bacillus species are gram-positive aerobes or facultative anaerobes that may have endospores (Parker et al. 2016, §4.4). Escherichia coli is the most varied bacterial class — commonly seen in the gut, in pink eye, and aiding with vitamin K production; it is a facultative anaerobe (Parker et al. 2016, §4.4, §9.2)."
))
edits.append((4, 'replace',
    "Through our experiment we are able to verify oxygen qualities of our bacteria. We made tube cultures, which allow growth of bacteria, but  oxygen concentration decreases with depth of the tubes. The area with the most oxygen is the surface of agar so this is where obligate aerobes grow. Thos bacteria that are facultative anaerobes are able to grow anywhere in the tube, however even with those that dont require oxygen, they still grow more where aerobic respiration is possible (Parker et al. 2016, §9.2). Hence these tubes allow to quickly identify bacteria  oxygen requirements. Materials and Methods",
    "Tube cultures allow growth of bacteria, but oxygen concentration decreases with depth. Obligate aerobes grow at the agar surface where oxygen is most abundant; facultative anaerobes grow throughout, though more heavily where aerobic respiration is possible (Parker et al. 2016, §9.2). These tubes quickly identify bacterial oxygen requirements."
))
edits.append((4, 'replace',
    "We used the Bunsen burner to sterilize the inoculating loop by holding it in the inner flame until it glowed red. Before sampling the bacteria we allowed the loop to cool near the flame. Next the cap of the B. subtilis stock tube was removed with pinky and ring finger. We flamed the mouth of the stock tube. Finally we were ready to get a loop of culture. After taking a sample we re-flamed the tube at the mouth and recapped. We re racked the B. Subtitles. Followed by removing the cap of the slant tube. We flamed the mouth of the slant tube. Next we used the loop to streak the inoculum in a zigzag pattern across the agar surface of the slant. All the way from the bottom of the slant to the top of the slant. We flamed the mouth of the slant tube ,recapped, re racked. Finished this portion by flaming the inoculating loop.",
    "The inoculating loop was sterilized in the Bunsen flame until red, then cooled briefly. The cap of the B. subtilis stock tube was removed with the pinky and ring finger and the tube mouth was flamed before sampling a loopful. The tube mouth was reflamed, recapped, and racked. The slant tube cap was then removed, the mouth flamed, and the loop used to streak the inoculum in a zigzag across the agar surface from bottom to top. The slant was flamed, recapped, racked, and the loop reflamed."
))
edits.append((4, 'replace',
    "Next we worked on the deep tube of B. subtilis. We inoculated it using the needle instrument. We followed the same aseptic flame protocol described previously.  The needle with sample was inserted into the center of the agar deep. We went almost to the bottom of the tube. This entire process was repeated for the E. coli. We produced one TSA slant and one TSA deep with E. coli. Finally we capped loosely for gas exchange, incubated, and waited for growth.",
    "The B. subtilis deep tube was inoculated using a needle following the same aseptic flame protocol; the needle was inserted into the center of the agar almost to the bottom. This entire process was repeated for E. coli, producing one TSA slant and one TSA deep per organism. Tubes were capped loosely for gas exchange and incubated."
))
edits.append((4, 'replace',
    "In the E. coli deep growth was seen from the surface to the bottom of the tube. This growth is expected of facultative anaerobes, organisms that can grow with or without oxygen, and ecoli has member in these categories (Parker et al. 2016, §9.2, 4.4). Conclusion",
    "In the E. coli deep, growth was seen from surface to bottom — expected of facultative anaerobes, which can grow with or without oxygen (Parker et al. 2016, §9.2, §4.4)."
))
edits.append((4, 'replace',
    "Bacillus subtilis and Escherichia coli on the TSA slant and deep tubes was performed successfully. After incubation, all four tubes showed growth without contamination, confirming aseptic technique (Parker et al. 2016, §13.1 and §13.2).",
    "Inoculation of B. subtilis and E. coli on TSA slant and deep tubes was performed successfully. All four tubes showed growth without contamination, confirming aseptic technique (Parker et al. 2016, §13.1, §13.2)."
))
edits.append((4, 'replace',
    "The deep-tube growth demonstrated textbook oxygen requirements: B. subtilis growth woxygen-rich (aerobic pattern);  E. coli showed growth along stab line (facultative anaerobe pattern)( Parker et al. 2016, §4.4 and §9.2).",
    "The deep-tube growth demonstrated textbook oxygen requirements: B. subtilis growth in the oxygen-rich surface (aerobic pattern); E. coli growth along the entire stab line (facultative anaerobe pattern) (Parker et al. 2016, §4.4, §9.2)."
))

# ===== LAB 5 =====
edits.append((5, 'replace',
    "We heat-fixed, stained a bacterial smear using a single basic dye (methylene blue). Then we observed the slide under a light microscope. The purpose was to learn simple-staining.Introduction",
    "We heat-fixed and stained a bacterial smear using a single basic dye (methylene blue), then observed the slide under a light microscope. The purpose was to learn simple-staining."
))
edits.append((5, 'replace',
    "The cells were small, straight, rod-shaped bacilli. This was expected of gram-negative enteric bacterium Escherichia coli  (Parker et al. 2016, §4.4). However, identification need more than a simple stain.  To be more accurate we would need to look at cell-wall type and more for that definitive identification.",
    "The cells were small, straight, rod-shaped bacilli — consistent with the gram-negative enteric bacterium Escherichia coli (Parker et al. 2016, §4.4). However, definitive identification would require more than a simple stain (e.g., cell-wall type)."
))
edits.append((5, 'replace',
    "We made a bacterial smear, heat-fixed, and stained with methylene blue.  We looked at the light microscope through the 1000× total magnification under oil immersion. The methylene blue simple stain, basic dye, positively charged chromophore binds to the negatively charged bacterial cell wall (Parker et al. 2016, §2.4). The cells rod-shape was compatible, but not diagnostic for Escherichia coli (Parker et al. 2016, §4.4). Ahtough not diagnostic the simple stain did show shape.  To properly distinguish among bacterial groups we would need to perform gram stains.",
    "We made a bacterial smear, heat-fixed it, and stained with methylene blue, then observed at 1000× total magnification under oil immersion. The positively charged methylene blue chromophore bound to the negatively charged bacterial cell wall (Parker et al. 2016, §2.4). The rod shape was compatible with — but not diagnostic for — Escherichia coli (Parker et al. 2016, §4.4). To distinguish among bacterial groups, a Gram stain is needed."
))

# ===== LAB 6 =====
edits.append((6, 'replace',
    "The Gram stain is the most popular  differential staining procedure. We performed a mixed smear containing: Escherichia coli (gram-negative) and Staphylococcus epidermidis (gram-positive). Our objective  was to perform a Gram stain procedure correctly to a mixed preparation.",
    "The Gram stain is the most popular differential staining procedure. We performed a mixed smear containing Escherichia coli (gram-negative) and Staphylococcus epidermidis (gram-positive). Our objective was to correctly perform the Gram stain procedure on a mixed preparation."
))
edits.append((6, 'replace',
    "The purple, crystal violet, cells are gram-positive cells;  The pink, safranin cells are gram-negative (Parker et al. 2016, §2.4). Gram-positive cell walls have a thick peptidoglycan external to the plasma membrane. The thick peptidoglycan keeps the crystal-violet–iodine complex through all the steps. Gram-negative cells have a thinner peptidoglycan layer that loses the purple during the alcohol wash. Escherichia coli is a gram-negative, Staphylococcus epidermidis is a gram-positive coccus. Staphylococcus name is derived from the word bunches of grapes, which is descriptive of its classics cells in clusters.  Staphylococcus Epidermedis are facultative anaerobes and are part of the normal microbiota of human skin (Parker et al. 2016, §4.4). Thus we should be able to view gram positive and gram negative in a single slide and observe differences.",
    "Purple cells are gram-positive; pink cells are gram-negative (Parker et al. 2016, §2.4). E. coli is gram-negative; S. epidermidis is a gram-positive coccus whose name comes from \"bunches of grapes,\" descriptive of its classic clusters. S. epidermidis is a facultative anaerobe and part of the normal microbiota of human skin (Parker et al. 2016, §4.4). Thus we should be able to view both Gram reactions on a single slide and observe the differences."
))
edits.append((6, 'replace',
    "We have the pink, rod-shaped cells, thin peptidoglycan, gram-negative bacteria.This resulted because during alcohol decolorization, the crystal-violet–iodine washed out due to thinner peptidoglycan. Cells are colorless, keep safranin, and become pink (Parker et al. 2016, §2.4). The rod shape, pink color are  Gram reaction of E. coli (Parker et al. 2016, §4.4).",
    "The pink, rod-shaped cells are gram-negative with thin peptidoglycan. During alcohol decolorization the crystal-violet–iodine washed out, leaving cells colorless to take up safranin and turn pink (Parker et al. 2016, §2.4). The rod shape and pink color are the Gram reaction of E. coli (Parker et al. 2016, §4.4)."
))
edits.append((6, 'replace',
    "We also have the purple gram-positive part of the mixed smear. This is expected of S. epidermidis. Due to the thick peptidoglycan layer, that retains crystal-violet–iodine complex even after alcohol decolorization (Parker et al. 2016, §2.4). Staphylococcus, gram-positive cocci in characteristic clusters (grapes) (Parker et al. 2016, §4.4).",
    "The purple gram-positive portion is expected of S. epidermidis, whose thick peptidoglycan retains the crystal-violet–iodine complex even after alcohol decolorization (Parker et al. 2016, §2.4). Staphylococcus cells appear as gram-positive cocci in characteristic grape-like clusters (Parker et al. 2016, §4.4)."
))

# ===== Apply =====
for lab in [2,3,4,5,6]:
    path = f'unpacked_lab{lab}/word/document.xml'
    tree = ET.parse(path)
    root = tree.getroot()
    body = root.find(W('body'))

    paragraphs = list(body.iter(W('p')))
    n_applied = 0
    n_missed = 0
    for L, action, find, repl in edits:
        if L != lab: continue
        target = norm(find)
        matched = False
        for p in paragraphs:
            if norm(para_text(p)) == target:
                if action == 'replace':
                    replace_para_text(p, repl)
                elif action == 'delete':
                    body.remove(p)
                    paragraphs.remove(p)
                matched = True
                n_applied += 1
                break
        if not matched:
            n_missed += 1
            print(f'  Lab {lab} MISS: {find[:80]}...')

    # Write back
    tree.write(path, encoding='utf-8', xml_declaration=True)
    print(f'Lab {lab}: applied {n_applied}, missed {n_missed}')
