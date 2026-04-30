# BIO203 Ch.7 Study Guide - Version 4
# V4: Lecture-slide-only. REMOVED: hopanoids, ergosterol, PLFA analysis, PHB granules
# (none of these appear in Popa's Ch.7 lecture slides)
# Cholesterol and isoprenoids remain (both in slides). Mycolic acid remains (slides 25+47).

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
import os

os.makedirs('C:/Users/User/Dropbox/Nu micro/Ch 7', exist_ok=True)

OUTPUT = 'C:/Users/User/Dropbox/Nu micro/Ch 7/BIO203_Ch7_Study_Guide_v4.pdf'

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.75*inch, bottomMargin=0.75*inch)

h1 = ParagraphStyle('h1', fontSize=13, fontName='Helvetica-Bold', spaceAfter=5, spaceBefore=10,
                    alignment=TA_CENTER,
                    borderPad=4, borderWidth=1, borderColor=colors.black,
                    backColor=colors.Color(0.92, 0.92, 0.92))
h2 = ParagraphStyle('h2', fontSize=11, fontName='Helvetica-Bold', spaceAfter=4, spaceBefore=10)
h3 = ParagraphStyle('h3', fontSize=10, fontName='Helvetica-Bold', spaceAfter=3, spaceBefore=6)
body = ParagraphStyle('body', fontSize=9, fontName='Helvetica', spaceAfter=3, leading=13)
bld  = ParagraphStyle('bld', fontSize=9, fontName='Helvetica-Bold', spaceAfter=3, leading=13)
note = ParagraphStyle('note', fontSize=8, fontName='Helvetica-Oblique', spaceAfter=3, leftIndent=10,
                      textColor=colors.Color(0.3, 0.3, 0.3))
tip  = ParagraphStyle('tip', fontSize=8.5, fontName='Helvetica-Bold', spaceAfter=4, leading=12,
                      backColor=colors.HexColor('#fff3cd'), borderPad=4,
                      borderWidth=0.5, borderColor=colors.HexColor('#cc8800'))

cell_body = ParagraphStyle('cell_body', fontSize=8, fontName='Helvetica', leading=11, spaceAfter=0)
cell_bold = ParagraphStyle('cell_bold', fontSize=8, fontName='Helvetica-Bold', leading=11, spaceAfter=0)

def _cell(val, is_header=False):
    if isinstance(val, str):
        return Paragraph(val.replace('\n', '<br/>'), cell_bold if is_header else cell_body)
    return val

def tbl(data, col_widths=None):
    wrapped = [[_cell(c, is_header=(i == 0)) for c in row] for i, row in enumerate(data)]
    t = Table(wrapped, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('GRID',          (0,0), (-1,-1), 0.5, colors.black),
        ('BACKGROUND',    (0,0), (-1,0),  colors.Color(0.82, 0.82, 0.82)),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [colors.white, colors.Color(0.95, 0.95, 0.95)]),
        ('TOPPADDING',    (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING',   (0,0), (-1,-1), 4),
        ('RIGHTPADDING',  (0,0), (-1,-1), 4),
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
    ]))
    return t

def sp(n=1): return Spacer(1, n * 0.1 * inch)
def hr():    return HRFlowable(width="100%", thickness=1, color=colors.black, spaceAfter=4)
def HY(text): return Paragraph(f'HIGHEST YIELD: {text}', tip)

story = []

# ── TITLE ──────────────────────────────────────────────────────────
story.append(Paragraph('BIO203 — Chapter 7 Study Guide — Version 4 (Lecture Slides Only)', h1))
story.append(Paragraph('Microbial Biochemistry | Source: Popa lecture slides only | Textbook-only topics excluded', note))
story.append(sp(1))

# ═══════════════════════════════════════════════════════════════════
# 7.1 ORGANIC MOLECULES
# ═══════════════════════════════════════════════════════════════════
story.append(Paragraph('7.1 — Organic Molecules (Popa slides 3–12)', h1))

story.append(Paragraph('Elements in Living Cells', h2))
story.append(hr())
story.append(tbl([
    ['Category', 'Elements', 'Exam tip'],
    ['Most abundant (macronutrients)', 'H, C, O, N, P, S',
     '~99% of dry cell weight.'],
    ['The "Big 4" (Popa emphasis)', 'C, N, O, H',
     'Low atomic number. Form strong covalent bonds. Build all organic molecules.'],
    ['Trace elements (micronutrients)', 'Na, K, Mg, Zn, Fe, Ca, Mo, Cu, Co, Mn, V',
     'Required in tiny amounts. Essential to enzymes and biochemical reactions.'],
], [1.6*inch, 1.8*inch, 3.8*inch]))
story.append(sp(2))

story.append(Paragraph('Isomers — Same Formula, Different Structure', h2))
story.append(hr())
story.append(HY("Structural isomers: glucose, galactose, fructose all = C6H12O6 — different structure, different properties."))
story.append(tbl([
    ['Type', 'Definition', 'Example', 'Exam trap'],
    ['Structural isomers',
     'Same molecular formula; different bonding sequence',
     'Glucose, galactose, fructose all = C6H12O6',
     'They are NOT the same molecule despite identical formula.'],
    ['Stereoisomers',
     'Same bonding; different spatial arrangement',
     'D-glucose vs L-glucose',
     ''],
    ['Enantiomers',
     'Non-superimposable mirror images; rotate polarized light.\nD form = clockwise (+); L form = counterclockwise (-)',
     'D-aspartame = tasteless; L-aspartame = sweet.',
     'Many microbes metabolize ONLY one enantiomeric form — important for drug design.'],
], [1.1*inch, 1.7*inch, 2.0*inch, 2.4*inch]))
story.append(sp(2))

story.append(Paragraph('Functional Groups — Know All 7', h2))
story.append(hr())
story.append(tbl([
    ['Group', 'Formula', 'Property', 'Found in', 'Exam tip'],
    ['Hydroxyl',   '-OH',     'Polar, hydrophilic',           'Alcohols, sugars',                   'Ethanol: CH3-CH2-OH'],
    ['Carbonyl',   'C=O',     'Polar',                         'Sugars (aldoses/ketoses)',             'Aldehyde = end of chain; Ketone = middle'],
    ['Carboxyl',   '-COOH',   'Acidic',                        'Fatty acids, amino acids',            'Acetic acid (vinegar): CH3-COOH'],
    ['Amino',      '-NH2',    'Basic (alkaline)',               'Amino acids, nucleotides',            'All 20 amino acids have -NH2 on alpha carbon'],
    ['Sulfhydryl', '-SH',     'Reactive; forms disulfide bonds (-S-S-)',  'Cysteine (amino acid)', 'Stabilizes protein tertiary structure'],
    ['Phosphate',  '-PO4-',   'Negatively charged',            'ATP, DNA, RNA, phospholipids',       'ATP = energy transfer; backbone of nucleic acids'],
    ['Methyl',     '-CH3',    'Nonpolar; silences DNA when added',  'DNA methylation',            'Epigenetic regulation of gene expression'],
], [0.85*inch, 0.65*inch, 1.4*inch, 1.4*inch, 2.9*inch]))
story.append(sp(2))

story.append(Paragraph('Monomers, Polymers, Reactions', h2))
story.append(hr())
story.append(HY("Lipids have NO true monomer and NO true polymer — this is the most common exam trap in 7.1."))
story.append(tbl([
    ['Reaction', 'Direction', 'Equation', 'Products'],
    ['Dehydration synthesis\n(condensation)',
     'Monomers JOIN → polymer',
     'Monomer + Monomer → Polymer + H2O',
     'Water released for every bond formed'],
    ['Hydrolysis',
     'Polymer BREAKS → monomers',
     'Polymer + H2O → Monomers',
     'Water consumed for every bond broken'],
], [1.5*inch, 1.1*inch, 2.2*inch, 2.4*inch]))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════
# 7.2 CARBOHYDRATES
# ═══════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph('7.2 — Carbohydrates (Popa slides 13–18)', h1))
story.append(Paragraph(
    'Elements: C, H, O. Empirical formula: (CH2O)n. Most abundant biomolecules on earth. '
    'Major function: energy source. Also structural (cell walls, exoskeletons).',
    body))
story.append(sp(1))

story.append(tbl([
    ['Type', 'Key examples', 'Function', 'Exam tip'],
    ['Monosaccharides\n(simple sugars)',
     'Hexoses (6C): glucose, galactose, fructose (all = C6H12O6)\nPentoses (5C): ribose (RNA), deoxyribose (DNA)',
     'Energy source. Backbone of nucleic acids.',
     'Glucose, galactose, fructose are structural isomers — same formula, different structure.'],
    ['Disaccharides',
     'Sucrose = glucose + fructose (table sugar)\nLactose = glucose + galactose (milk sugar)\nMaltose = glucose + glucose',
     'Transport form of sugar in plants.',
     'Formed by glycosidic bond (dehydration synthesis).'],
    ['Polysaccharides\n(glycans)',
     'Starch (plants), Glycogen (animals + bacteria),\nCellulose (plants), Chitin (fungi + arthropods)',
     'Storage: starch, glycogen.\nStructural: cellulose, chitin.',
     'NOT sweet. Generally NOT soluble. Starch = plant storage; glycogen = animal/bacterial storage.'],
], [1.1*inch, 2.1*inch, 1.6*inch, 2.4*inch]))
story.append(sp(1))

story.append(Paragraph('Modified Glucose — Critical for Microbiology (Popa slide 17)', h3))
story.append(HY("NAM is found ONLY in bacteria — this fact is always tested. Chitin is NOT in bacteria. Peptidoglycan = target of penicillin."))
story.append(tbl([
    ['Compound', 'Full name', 'Where found', 'Why it matters', 'Exam trap'],
    ['NAG', 'N-acetyl glucosamine',
     'Bacterial cell wall; fungal cell walls (as chitin)',
     'Building block of both peptidoglycan AND chitin',
     'Present in fungi too — not bacteria-exclusive'],
    ['NAM', 'N-acetyl muramic acid',
     'Bacterial cell wall ONLY — NOT in fungi, animals, or plants',
     'Bacteria-exclusive marker; presence = bacterial cell wall',
     'NAM is UNIQUE TO BACTERIA — if you see NAM, it is bacteria'],
    ['Peptidoglycan', 'Alternating NAG–NAM polymer with peptide cross-links',
     'Bacterial cell walls (G+ thick, G- thin)',
     'Rigid structure. Target of penicillin (blocks cross-linking step).',
     'G+ = thick layer; G- = thin layer + outer membrane. Archaea have NO peptidoglycan.'],
    ['Chitin', 'Polymer of NAG only',
     'Fungal cell walls; arthropod exoskeletons (insects, crabs)',
     'Distinguishes fungi from bacteria',
     'NOT found in bacteria. Common trap: mix up chitin (fungi) with peptidoglycan (bacteria).'],
], [0.7*inch, 1.4*inch, 1.4*inch, 1.6*inch, 2.1*inch]))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════
# 7.3 LIPIDS
# ═══════════════════════════════════════════════════════════════════
story.append(Paragraph('7.3 — Lipids (Popa slides 19–27)', h1))
story.append(Paragraph(
    'Elements: C, H, O (also N, S, P in some). Hydrophobic (nonpolar). '
    '<b>NO true monomer. NO true polymer.</b> '
    'Functions: energy storage, membranes, hormones, pigments, waterproofing.',
    body))
story.append(sp(1))

story.append(tbl([
    ['Type', 'Structure', 'Key property', 'Microbiology connection', 'Exam trap'],
    ['Fatty acids',
     'Long hydrocarbon chain + carboxyl group (-COOH) at end',
     'Saturated = single bonds → solid. Unsaturated = double bonds → liquid (oil, "kinks").',
     'Building blocks of triglycerides and phospholipids.',
     'Saturated = solid fat; unsaturated = liquid oil. Double bond causes kink = less packing.'],
    ['Triglycerides\n(triacylglycerol)',
     'Glycerol + 3 fatty acids. Simple lipid.',
     'Primary energy storage. Provide >2× calories of carbs or proteins.',
     'Major energy reserve in cells.',
     'Simple lipid = only glycerol + fatty acids. NOT amphipathic.'],
    ['Phospholipids',
     'Glycerol + 2 fatty acids + phosphate group. Complex lipid.',
     'AMPHIPATHIC: hydrophilic phosphate head (polar) + hydrophobic fatty acid tails (nonpolar).',
     'Form lipid bilayer of ALL cell membranes. Gram- bacteria have outer membrane containing LPS.',
     'Amphipathic = interacts with BOTH water and lipids. Basis of all membranes.'],
    ['Isoprenoids\n(terpenoids)',
     'Branched lipids from isoprene units',
     'Multiple physiological roles',
     'Pigments (beta-carotene), fragrances (menthol, camphor, limonene), pharmaceuticals.',
     ''],
    ['Steroids / Sterols',
     '4 interlocking hydrocarbon rings. Main example: cholesterol.',
     'Mostly hydrophobic; sterols have some hydrophilic character',
     'Cholesterol found in eukaryotes and Mycoplasma (wall-less bacteria). Stabilizes membranes.',
     'Most bacteria do NOT have cholesterol — they have functionally similar but structurally different membrane lipids.'],
    ['Waxes\n(incl. mycolic acid)',
     'Long-chain fatty acids. Water-resistant.',
     'Waterproofing',
     'Mycolic acid in Mycobacterium tuberculosis cell wall → waxy → acid-fast staining.',
     'Mycolic acid = waxy lipid = ACID-FAST = Mycobacterium. This connection is always tested.'],
], [0.95*inch, 1.5*inch, 1.3*inch, 1.85*inch, 1.6*inch]))
story.append(sp(1))

story.append(Paragraph('Phospholipid Bilayer', h3))
story.append(tbl([
    ['Structure', 'Description', 'Significance'],
    ['Micelle', 'Spherical; hydrophobic tails inside, polar heads outside', 'Simple assembly in water'],
    ['Lipid bilayer', 'Two layers; tails face each other inward, heads face outward', 'Basis of ALL cell membranes'],
    ['Vesicle / Liposome', 'Lipid bilayer forms a sphere', 'Subcellular compartments; drug delivery vehicles'],
], [1.3*inch, 2.6*inch, 3.3*inch]))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════
# 7.4 PROTEINS
# ═══════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph('7.4 — Proteins (Popa slides 28–38)', h1))
story.append(Paragraph(
    'Elements: C, H, N, O (some also S, P). Monomer = amino acid (20 standard types). '
    'Functions: enzymes, transport, structure, defense (antibodies), communication (receptors/hormones).',
    body))
story.append(sp(1))

story.append(Paragraph('Amino Acid Structure', h2))
story.append(hr())
story.append(Paragraph(
    'Every amino acid has the SAME core on the alpha (α) carbon: '
    'amino group (-NH2) + carboxyl group (-COOH) + hydrogen + <b>R side chain</b> '
    '(the R group is what differs among the 20 amino acids).',
    body))
story.append(sp(1))

story.append(Paragraph('4 Levels of Protein Structure — All 4 Are Tested', h2))
story.append(hr())
story.append(HY("Know the bonds at each level. Primary = peptide bonds. Secondary = H-bonds (backbone). Tertiary = disulfide bridges + H-bonds + ionic + hydrophobic. Quaternary = multiple subunits."))
story.append(tbl([
    ['Level', 'Description', 'Bonds / Forces', 'Exam tip'],
    ['1° Primary',
     'Sequence of amino acids in the chain',
     'Peptide bonds',
     'Directly coded by genes. Change ONE amino acid → can destroy function.'],
    ['2° Secondary',
     'Local folding: alpha (α) helix OR beta (β) pleated sheet',
     'Hydrogen bonds between BACKBONE carbonyl (C=O) and amino (-NH) groups — NOT the R side chains',
     'α-helix: coiled spring.\nβ-sheet: pleated structure.\nKey: H-bonds between backbone atoms, not R groups.'],
    ['3° Tertiary',
     'Overall 3D shape — large-scale folding of all secondary structures',
     'Disulfide bridges (-S-S- between cysteine R groups), H-bonds, ionic bonds, hydrophobic interactions between nonpolar R groups',
     'The functional shape. Active site shape determined here.\nDisulfide bridges = cysteine residues. Only bond involving R side chains.'],
    ['4° Quaternary',
     'Multiple polypeptide subunits assembled together',
     'Same as tertiary (relatively weak non-covalent interactions)',
     'Only in proteins with 2+ subunits.\nHemoglobin = 2α + 2β subunits + 4 heme groups (conjugated protein).'],
], [0.85*inch, 1.5*inch, 1.75*inch, 3.1*inch]))
story.append(sp(1))

story.append(Paragraph('Denaturation', h3))
story.append(tbl([
    ['Concept', 'What changes', 'What stays', 'Causes', 'Clinical relevance'],
    ['Denaturation',
     '2°, 3°, and 4° structure unfolds',
     '1° structure (amino acid sequence) intact',
     'Heat or pH change',
     'Autoclave (121°C) denatures proteins → sterilization.\nAntiseptics denature microbial proteins.\nCooking egg = irreversible denaturation.'],
    ['Reversible', '2°/3°/4° unfolds', '1° intact; can refold', 'Mild heat / pH shift', 'Cell may recover protein function'],
    ['Irreversible', '2°/3°/4° unfolds permanently', '1° intact; cannot refold', 'Extreme heat, strong acid/base', 'Permanent loss of function'],
], [1.0*inch, 1.3*inch, 1.1*inch, 1.1*inch, 2.7*inch]))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════
# 7.5 ID METHODS
# ═══════════════════════════════════════════════════════════════════
story.append(Paragraph('7.5 — Biochemical Identification Methods (Popa slides 39–49)', h1))
story.append(HY("MALDI-TOF is now standard in clinical labs. FAME = fatty acid methyl ester profiling. Serological tests = antibody-antigen. Know what each method analyzes."))
story.append(sp(1))

story.append(tbl([
    ['Method', 'What it analyzes', 'How it works', 'Exam tip'],
    ['MALDI-TOF\nMass Spectrometry',
     'Proteins and chemicals from the microbe',
     '1. Microbe + matrix reagent on plate.\n2. UV laser → gaseous ions ejected.\n3. Ions separated by mass-to-charge ratio (m/z) → unique mass spectrum.\n4. Spectrum matched to database.',
     'NOW STANDARD in clinical labs. Fast, accurate. Popa emphasized this heavily.'],
    ['FAME analysis',
     'Fatty acids in cell membranes',
     '1. Fatty acids extracted.\n2. Converted to methyl esters.\n3. Gas chromatography (GC).\n4. Chromatogram matched to reference database.',
     'Each species has unique fatty acid profile (like fingerprint). FAME = Fatty Acid Methyl Ester.'],
    ['Serological tests',
     'Carbohydrates / antigens on cell surface',
     'Antibodies bind specific surface antigens → agglutination (clumping) or other reaction',
     'Antibody-antigen specificity used for ID. Rapid clinical tests use this principle.'],
    ['Proteomic analysis',
     'Proteins expressed under growth conditions',
     '1. Proteins separated.\n2. Digested into peptides.\n3. Peptides analyzed by MALDI-TOF.\n4. Compared to database.',
     'Identifies proteins expressed during infection. Powerful for clinical diagnostics.'],
], [1.0*inch, 1.1*inch, 2.2*inch, 2.9*inch]))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════
# QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph('QUICK REFERENCE — Chapter 7 Highest Yield', h1))
story.append(sp(1))

story.append(Paragraph('The 4 Biomolecules — Must Know Cold', h2))
story.append(hr())
story.append(tbl([
    ['Biomolecule', 'Elements', 'Monomer', 'Polymer', 'Key function', 'Exam trap'],
    ['Carbohydrates', 'C, H, O', 'Monosaccharide', 'Polysaccharide', 'Energy; structural (cell walls)', 'Most abundant biomolecule on earth'],
    ['Lipids', 'C, H, O\n(N, S, P in some)', 'NO true monomer', 'NO true polymer', 'Membranes, energy storage, hormones', 'TRAP: lipids have no monomer/polymer — most tested fact'],
    ['Proteins', 'C, H, N, O\n(some S, P)', 'Amino acid', 'Polypeptide / protein', 'Enzymes, transport, structure, defense', '20 amino acids; sequence coded by genes'],
    ['Nucleic acids', 'C, H, N, O, P', 'Nucleotide', 'DNA / RNA', 'Genetic information; protein synthesis', 'Covered in Ch.10'],
], [1.0*inch, 0.85*inch, 0.85*inch, 0.95*inch, 1.6*inch, 1.95*inch]))
story.append(sp(1))

story.append(Paragraph('Must-Know Microbiology Connections', h2))
story.append(hr())
story.append(tbl([
    ['Concept', 'Connection to exam questions'],
    ['Peptidoglycan',
     'NAG + NAM alternating. G+ = thick, G- = thin + outer membrane.\nTarget of PENICILLIN (blocks cross-linking).\nNAM = bacteria ONLY (Archaea, fungi, animals have NO NAM).'],
    ['Chitin',
     'Polymer of NAG only. Fungal cell walls + arthropod exoskeletons.\nNOT in bacteria. Test Q: "What is the fungal cell wall made of?" = CHITIN.'],
    ['Mycolic acid',
     'Waxy lipid in Mycobacterium tuberculosis and M. leprae cell wall.\nCauses ACID-FAST result: resists acid-alcohol decolorization → stains PINK.\nAlso confers antibiotic resistance.'],
    ['Phospholipid bilayer',
     'ALL cell membranes = phospholipid bilayer.\nAmphipathic: tails inward (hydrophobic), heads outward (hydrophilic).\nG- bacteria have SECOND outer membrane containing LPS (lipopolysaccharide).'],
    ['Protein denaturation',
     'Autoclave (121°C, 15 min) = denatures proteins → sterilization.\nAntiseptics = denature microbial proteins → kill microbes.\nDenaturation: 2°/3°/4° structure destroyed; 1° (AA sequence) intact.'],
    ['MALDI-TOF',
     'Now STANDARD clinical lab ID method. Faster and more accurate than culture-based phenotypic tests for many organisms.'],
    ['Cholesterol',
     'Sterol found in eukaryote membranes. Mycoplasma (bacteria with no cell wall) also have cholesterol. Most other bacteria do not.'],
    ['Enantiomers — D vs L',
     'Many microbes metabolize only ONE enantiomeric form.\nSome antibiotics are enantiomer-specific.'],
], [1.6*inch, 5.6*inch]))
story.append(sp(1))

story.append(Paragraph('Common Exam Traps — Chapter 7', h2))
story.append(hr())
story.append(tbl([
    ['Wrong answer students pick', 'Correct answer'],
    ['"Lipids have monomers and polymers"', 'Lipids do NOT have true monomers or polymers — they are assembled differently'],
    ['"Chitin is found in bacteria"', 'Chitin is in FUNGI and arthropods — bacteria have PEPTIDOGLYCAN'],
    ['"Archaea have peptidoglycan cell walls"', 'Archaea have NO peptidoglycan — unique ether-linked lipid walls instead'],
    ['"Denaturation destroys the amino acid sequence"', 'Denaturation destroys 2°/3°/4° structure ONLY — primary (AA sequence) remains intact'],
    ['"MALDI-TOF is only a research tool"', 'MALDI-TOF is now STANDARD in clinical microbiology labs for ID'],
    ['"Mycobacterium stains normally with Gram stain"', 'Mycobacterium is Gram-variable/poor staining — use ACID-FAST stain instead'],
], [2.8*inch, 4.2*inch]))

doc.build(story)
print("Done -> " + OUTPUT)

