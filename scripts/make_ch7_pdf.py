from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
import os

os.makedirs('C:/Users/User/Dropbox/Nu micro/Ch 7', exist_ok=True)

doc = SimpleDocTemplate(
    'C:/Users/User/Dropbox/Nu micro/Ch 7/BIO203_Ch7_Study_Guide.pdf',
    pagesize=letter,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.75*inch, bottomMargin=0.75*inch
)

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

cell_body = ParagraphStyle('cell_body', fontSize=8, fontName='Helvetica', leading=11, spaceAfter=0)
cell_bold = ParagraphStyle('cell_bold', fontSize=8, fontName='Helvetica-Bold', leading=11, spaceAfter=0)

def _cell(val, is_header=False):
    if isinstance(val, str):
        text = val.replace('\n', '<br/>')
        return Paragraph(text, cell_bold if is_header else cell_body)
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

def sp(n=1):
    return Spacer(1, n * 0.1 * inch)

def hr():
    return HRFlowable(width="100%", thickness=1, color=colors.black, spaceAfter=4)

story = []

# ── TITLE ────────────────────────────────────────────────────────────
story.append(Paragraph('BIO203 — Chapter 7 Study Guide', h1))
story.append(Paragraph('Microbial Biochemistry | Thu Apr 30', h2))
story.append(Paragraph('Sources: OpenStax Microbiology Ch.7 + Popa lecture slides', note))
story.append(sp(1))

# ── LEARNING OUTCOMES (from slide 2) ─────────────────────────────────
story.append(Paragraph('Learning Outcomes (from lecture)', h2))
story.append(hr())
story.append(Paragraph('Define the building blocks of life — the four biomolecules:', body))
story.append(Paragraph('1. Carbohydrates  &nbsp; 2. Lipids  &nbsp; 3. Proteins  &nbsp; 4. Nucleic acids', bld))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════
# 7.1 ORGANIC MOLECULES
# ═══════════════════════════════════════════════════════════════════
story.append(Paragraph('7.1 — Organic Molecules', h1))

# Elements in cells
story.append(Paragraph('Elements in Living Cells', h2))
story.append(hr())
story.append(tbl([
    ['Category', 'Elements', 'Notes'],
    ['Most abundant (macronutrients)', 'H, C, O, N, P, S', 'Account for ~99% of dry cell weight. H is the single most abundant.'],
    ['The "Big 4" (Popa emphasis)', 'C, N, O, H', 'Low atomic number — form strong covalent bonds, build diverse molecules.'],
    ['Trace elements (micronutrients)', 'Na, K, Mg, Zn, Fe, Ca, Mo, Cu, Co, Mn, V', 'Required in tiny amounts; essential to many biochemical reactions.'],
], [1.4*inch, 1.8*inch, 4*inch]))
story.append(sp(2))

# Carbon chemistry
story.append(Paragraph('Carbon — The Basis of Life', h2))
story.append(hr())
story.append(Paragraph('<b>Carbon forms 4 covalent bonds.</b> This is why life is carbon-based — no other element builds such diverse, large molecules.', body))
story.append(tbl([
    ['Bond type', 'Shape', 'Carbon skeleton forms'],
    ['Single bonds only', 'Tetrahedral', 'Long straight chains, branched chains'],
    ['Double bonds', 'Planar', 'Rings, chains with both single and double bonds'],
], [1.4*inch, 1.2*inch, 4.6*inch]))
story.append(sp(1))
story.append(Paragraph('Organic molecules contain carbon + hydrogen. Inorganic compounds do NOT contain carbon '
    '(exception: carbon oxides and carbonates contain C but no H — still considered inorganic).', note))
story.append(sp(2))

# Isomers
story.append(Paragraph('Isomers — Same Formula, Different Structure', h2))
story.append(hr())
story.append(tbl([
    ['Type', 'Definition', 'Example'],
    ['Structural isomers',
     'Same molecular formula; different bonding sequence of atoms',
     'Glucose, galactose, and fructose all = C6H12O6 but bonded differently'],
    ['Stereoisomers',
     'Same bonding sequence; different spatial arrangement of atoms',
     'Enantiomers — mirror images of each other (e.g., D-glucose vs L-glucose)'],
    ['Enantiomers (detail)',
     'Stereoisomers that are non-superimposable mirror images; called optical isomers because they rotate polarized light.\n'
     'D form rotates light clockwise (+); L form rotates counterclockwise (−).',
     'Discovered by Pasteur (1848) from wine fermentation crystals.\n'
     'D-aspartame = tasteless; L-aspartame (aspartame) = sweet.\n'
     'Many microbes can only metabolize ONE enantiomeric form.'],
], [1.3*inch, 2.4*inch, 3.5*inch]))
story.append(sp(2))

# Functional groups
story.append(Paragraph('Functional Groups — Know These 7', h2))
story.append(hr())
story.append(Paragraph(
    'Functional groups give organic molecules their chemical properties (polarity, acidity, etc.). '
    'They determine how a molecule behaves and reacts.',
    body))
story.append(sp(1))
story.append(tbl([
    ['Group', 'Formula', 'Property', 'Found in', 'Example (from lecture)'],
    ['Hydroxyl',   '-OH',     'Polar, hydrophilic',        'Alcohols, sugars',               'Ethanol: CH3-CH2-OH'],
    ['Carbonyl',   'C=O',     'Polar',                      'Sugars (aldoses/ketoses)',        'Aldehyde = end of chain; Ketone = middle of chain'],
    ['Carboxyl',   '-COOH',   'Acidic',                     'Fatty acids, amino acids',       'Acetic acid (vinegar): CH3-COOH'],
    ['Amino',      '-NH2',    'Basic (alkaline)',            'Amino acids, nucleotides',       'All amino acids have -NH2 on alpha carbon'],
    ['Sulfhydryl', '-SH',     'Reactive; forms disulfide bonds (-S-S-)',  'Amino acids',      'Cysteine — important for protein tertiary structure'],
    ['Phosphate',  '-PO4-',   'Negatively charged',         'Nucleic acids, ATP, phospholipids', 'ATP — energy transfer'],
    ['Methyl',     '-CH3',    'Nonpolar; adding to DNA silences it (less accessible)', 'DNA methylation', 'Epigenetic regulation of gene expression'],
], [0.8*inch, 0.65*inch, 1.5*inch, 1.5*inch, 2.75*inch]))
story.append(sp(2))

# Monomers / Polymers
story.append(Paragraph('Monomers, Polymers, and Reactions', h2))
story.append(hr())
story.append(tbl([
    ['Concept', 'Definition', 'Reaction', 'Result'],
    ['Monomer', 'Small subunit building block', '—', '—'],
    ['Polymer',  'Many monomers linked together', '—', '—'],
    ['Dehydration synthesis\n(condensation)',
     'Monomers JOIN to form a polymer',
     'Monomer + Monomer → Polymer + H2O',
     'Water molecule released for every bond formed'],
    ['Hydrolysis',
     'Polymer BREAKS into monomers',
     'Polymer + H2O → Monomers',
     'Water molecule consumed for every bond broken'],
], [1.3*inch, 1.8*inch, 2.3*inch, 1.8*inch]))
story.append(Paragraph(
    'The four macromolecule groups: polysaccharides, proteins, lipids, nucleic acids. '
    'The first three are covered in Ch.7. Nucleic acids are covered in Ch.10.',
    note))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════
# 7.2 CARBOHYDRATES
# ═══════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph('7.2 — Carbohydrates', h1))
story.append(Paragraph(
    'Elements: C, H, O. Empirical formula: (CH2O)n. '
    '<b>Most abundant biomolecules on earth.</b> Major function: cellular energy source. Also structural roles.',
    body))
story.append(sp(1))

story.append(Paragraph('Monosaccharides, Disaccharides, Polysaccharides', h2))
story.append(hr())
story.append(tbl([
    ['Type', 'Structure', 'Key Examples', 'Function'],
    ['Monosaccharides\n(simple sugars)',
     'Single sugar — monomer unit.\nClassified by C count:\n3C = triose, 4C = tetrose, 5C = pentose, 6C = hexose.\nContain carbonyl (C=O) and hydroxyl (-OH) groups.',
     'Hexoses (6C): glucose (most abundant in nature), galactose, fructose\nPentoses (5C): ribose (in RNA), deoxyribose (in DNA)',
     'Energy source.\nRibose/deoxyribose = backbone of nucleic acids.\nFour+ carbons form cyclic (ring) structures.'],
    ['Disaccharides',
     '2 monosaccharides joined by a glycosidic bond\n(dehydration synthesis reaction)',
     'Sucrose (table sugar) = glucose + fructose\nLactose (milk sugar) = glucose + galactose\nMaltose (grain sugar) = glucose + glucose',
     'Transport form of sugar in plants.'],
    ['Polysaccharides\n(glycans)',
     'Hundreds of monosaccharides linked by glycosidic bonds.\nNOT sweet. Generally NOT soluble in water.\nCan be straight, helical, or branched.',
     'Starch (plants), Glycogen (animals + bacteria),\nCellulose (plants), Chitin (fungi + arthropods)',
     'Storage: starch (plants), glycogen (animals/bacteria).\nStructural: cellulose (plant cell walls), chitin (fungal walls + insect exoskeletons).'],
], [1.1*inch, 2.1*inch, 2.3*inch, 1.7*inch]))
story.append(sp(1))

story.append(Paragraph('Modified Glucose — Microbiology Critical (Popa slide 25)', h3))
story.append(tbl([
    ['Compound', 'Full name', 'Where it is', 'What it does'],
    ['NAG', 'N-acetyl glucosamine', 'Bacterial cell wall; fungal cell walls (as chitin)', 'Modified glucose — building block of peptidoglycan and chitin'],
    ['NAM', 'N-acetyl muramic acid', 'Bacterial cell wall ONLY', 'Modified glucose — found ONLY in prokaryotic peptidoglycan'],
    ['Peptidoglycan', 'NAG + NAM alternating polymer', 'Bacterial cell wall', 'Gives bacteria their rigid structure. Target of penicillin.'],
    ['Chitin', 'Polymer of NAG', 'Fungal cell walls; arthropod exoskeletons', 'NOT found in bacteria. Distinguishes fungi from bacteria.'],
], [0.7*inch, 1.6*inch, 1.8*inch, 3.1*inch]))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════
# 7.3 LIPIDS
# ═══════════════════════════════════════════════════════════════════
story.append(Paragraph('7.3 — Lipids', h1))
story.append(Paragraph(
    'Elements: C, H, O (also N, S, P in some). <b>Hydrophobic</b> (nonpolar). '
    'No true monomers — NOT polymers. '
    'Functions: energy storage, membrane structure, hormones, pigments, pharmaceuticals.',
    body))
story.append(sp(1))

story.append(Paragraph('Types of Lipids', h2))
story.append(hr())
story.append(tbl([
    ['Type', 'Structure', 'Key Property', 'Microbiology Relevance'],
    ['Fatty acids',
     'Long hydrocarbon chain + carboxyl group (-COOH) at end',
     'Hydrophobic/nonpolar.\nSaturated = single bonds only → solid at room temp.\nUnsaturated = one or more double bonds → liquid (oils); causes "kinks" in chain',
     'Building blocks of triglycerides and phospholipids.'],
    ['Triglycerides\n(triacylglycerol)',
     'Glycerol + 3 fatty acids joined by dehydration synthesis.\nClassified as SIMPLE lipids (only two component types).',
     'Primary energy-storage molecules. Provide >2× the calories of carbs or proteins.',
     'Found in adipose tissue and sebum (skin oil). Cutibacterium acnes feeds on skin lipids → acne.'],
    ['Phospholipids',
     'Glycerol + 2 fatty acids + phosphate group.\nComplex lipid (3+ component types).',
     'AMPHIPATHIC:\nHydrophilic phosphate "head" (polar) +\nHydrophobic fatty acid "tails" (nonpolar)',
     'Form lipid bilayer of ALL cell membranes.\nBilayer: tails face inward, heads face outward into water.'],
    ['Isoprenoids\n(terpenoids)',
     'Branched lipids derived from isoprene molecule',
     'Multiple physiological roles',
     'Used as pigments (beta-carotene), fragrances (menthol, camphor, limonene), pharmaceuticals (capsaicin).'],
    ['Steroids / Sterols',
     '4 interlocking hydrocarbon rings.\nSterols = steroids with -OH group.',
     'Mostly hydrophobic; sterols have some hydrophilic character',
     'Cholesterol: strengthens membranes in eukaryotes + bacteria lacking cell walls (Mycoplasma).\nHopanoids: bacteria produce these (NOT cholesterol) to strengthen their membranes.\nErgosterol: fungi and some protozoa — target of antifungal drugs.'],
    ['Waxes',
     'Long-chain isoprenoids — water resistant, hard at room temp',
     'Waterproofing',
     'Mycolic acid: waxy lipid in Mycobacterium tuberculosis cell wall → acid-fast staining result.\nSebum = wax esters + triacylglycerol in skin.'],
], [1*inch, 1.9*inch, 1.7*inch, 2.6*inch]))
story.append(sp(1))

story.append(Paragraph('Phospholipid Bilayer — Critical Concept', h3))
story.append(Paragraph(
    'Phospholipids are AMPHIPATHIC — they interact with BOTH water and fats. '
    'In aqueous environments they spontaneously arrange into structures:',
    body))
story.append(tbl([
    ['Structure', 'Description', 'Significance'],
    ['Micelle', 'Spherical; hydrophobic tails inside, polar heads outside', 'Simple assembly in water'],
    ['Lipid bilayer sheet', 'Two-dimensional layer, tails face each other inward', 'Basis of ALL cell membranes'],
    ['Vesicle / Liposome', 'Lipid bilayer forms a sphere', 'Subcellular components; drug delivery in medicine'],
], [1.2*inch, 2.8*inch, 3.2*inch]))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════
# 7.4 PROTEINS
# ═══════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph('7.4 — Proteins (Polypeptides)', h1))
story.append(Paragraph(
    'Elements: C, H, N, O — some also have S and P. Monomers = amino acids (20 standard).',
    body))
story.append(Paragraph(
    'Functions: enzymes (catalysis), transport, structure, communication (receptors, hormones), '
    'defense (antibodies, clotting factors). '
    '<b>The amino acid sequence is the information coded in the genes.</b>',
    body))
story.append(sp(1))

story.append(Paragraph('Amino Acids', h2))
story.append(hr())
story.append(Paragraph(
    'Every amino acid has the SAME core structure bonded to an alpha (α) carbon: '
    'amino group (-NH2) + carboxyl group (-COOH) + hydrogen atom + <b>R side chain</b> (variable — this is what differs between the 20 amino acids).',
    body))
story.append(tbl([
    ['Size range', 'Name', 'Notes'],
    ['~2–50 AA', 'Peptide (oligopeptide)', '2 AA = dipeptide; 3 AA = tripeptide; up to ~20 = oligopeptide; up to ~50 = polypeptide'],
    ['Very large (many AA)\nor multiple polypeptides', 'Protein', 'Essentially unlimited diversity from combinations of 20 amino acids'],
], [1.5*inch, 1.5*inch, 4.2*inch]))
story.append(Paragraph(
    'Peptide bond: formed when -NH2 of one amino acid reacts with -COOH of another → peptide bond + H2O released (dehydration synthesis).',
    note))
story.append(sp(2))

story.append(Paragraph('4 Levels of Protein Structure', h2))
story.append(hr())
story.append(tbl([
    ['Level', 'Description', 'Forces/Bonds', 'Key Point'],
    ['1° Primary',
     'Sequence of amino acids in the polypeptide chain',
     'Peptide bonds',
     'Directly coded by genes. Change ONE amino acid → can change or destroy function.\nEx: Cystic fibrosis = loss of ONE amino acid (phenylalanine) in CFTR protein.'],
    ['2° Secondary',
     'Local folding into alpha (α) helices OR beta (β) pleated sheets',
     'Hydrogen bonds between backbone carbonyl (C=O) and amino (-NH) groups — NOT the R side chains',
     'α-helix: coiled spring held by H-bonds every 4 AA.\nβ-pleated sheet: pleated structure from H-bonds between adjacent chain segments.'],
    ['3° Tertiary',
     'Overall 3D shape — large-scale folding of all secondary structures into one shape',
     'Disulfide bridges (-S-S- between cysteine R groups), H-bonds, ionic bonds, hydrophobic interactions between nonpolar side chains',
     'Final functional 3D shape. Determines what protein can do (active site shape).'],
    ['4° Quaternary',
     'Multiple polypeptide subunits assembled together',
     'Same as tertiary (relatively weak interactions)',
     'Only in proteins with 2+ subunits.\nEx: Hemoglobin = 2α + 2β subunits + 4 heme groups.\nConjugated proteins: glycoproteins (+ carbohydrate) or lipoproteins (+ lipid) — membrane components.'],
], [0.8*inch, 1.5*inch, 1.9*inch, 3.0*inch]))
story.append(sp(1))

story.append(Paragraph('Denaturation', h3))
story.append(tbl([
    ['Concept', 'Definition', 'Causes', 'Clinical relevance'],
    ['Denaturation',
     'Unfolding/loss of 2°, 3°, and 4° structure WITHOUT loss of 1° (amino acid sequence stays intact)',
     'Heat (increased temp) or pH changes (drops in pH)',
     'Autoclave (121°C) denatures proteins → sterilization.\nAntiseptics/disinfectants work partly by denaturing microbial proteins.\nCooking an egg = irreversible denaturation of albumin.'],
    ['Reversible', 'Mild conditions — protein can refold', 'Mild heat or pH shift', 'Cell can sometimes recover protein function'],
    ['Irreversible', 'Extreme conditions — protein cannot refold', 'Extreme heat, strong acid/base', 'Permanent loss of function'],
], [0.9*inch, 1.8*inch, 1.4*inch, 3.1*inch]))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════
# 7.5 ID METHODS
# ═══════════════════════════════════════════════════════════════════
story.append(Paragraph('7.5 — Using Biochemistry to Identify Microorganisms', h1))
story.append(Paragraph(
    'Accurate identification of bacterial isolates is essential in clinical microbiology '
    '— informs treatment decisions. Many methods rely on unique biochemical/molecular profiles.',
    body))
story.append(sp(1))

story.append(Paragraph('Identification Methods', h2))
story.append(hr())
story.append(tbl([
    ['Method', 'What it analyzes', 'How it works', 'Example / Notes'],
    ['Biochemical tests\n(phenotypic)',
     'Metabolic reactions, carbon utilization, enzyme activity',
     'Test tubes or automated panels (e.g., Biolog system) detect specific reactions',
     'Biolog: hundreds of biochemical reactions run simultaneously; software analyzes pH, chemical sensitivity, metabolic profiles.'],
    ['PHB granules\n(storage compound)',
     'Poly-β-hydroxybutyrate (carbon/energy storage)',
     'Presence or absence distinguishes species',
     'Found in some Pseudomonas species. P. aeruginosa (human pathogen) does NOT accumulate PHB.'],
    ['MALDI-TOF\nMass Spectrometry',
     'Proteins and chemicals released from the microbe',
     '1. Microbe mixed with matrix reagent on MALDI plate.\n2. Pulsed UV laser irradiates sample → gaseous ions ejected.\n3. Ions accelerated through spectrometer; separated by mass-to-charge ratio (m/z) → unique mass spectrum.\n4. Spectrum compared to database of thousands of known organisms.',
     'Now STANDARD in clinical microbiology labs. Rapidly IDs organisms that are hard to identify by traditional methods.'],
    ['FAME analysis\n(lipid profile)',
     'Fatty acids in cell membranes',
     '1. Fatty acids extracted from membranes.\n2. Chemically converted to volatile methyl esters.\n3. Analyzed by gas chromatography (GC).\n4. Chromatogram compared to reference database.',
     'Each peak = a specific fatty acid methyl ester. Profile is species-unique.'],
    ['PLFA analysis\n(phospholipid-derived)',
     'Phospholipids from membranes',
     'Membranes hydrolyzed (saponified) to release fatty acids → same as FAME analysis',
     'Similar to FAME but specifically from phospholipid fraction.'],
    ['Proteomic analysis',
     'Proteins produced under specific growth conditions',
     '1. Proteins separated by HPLC.\n2. Fractions digested into smaller peptides.\n3. Peptides analyzed by MALDI-TOF.\n4. Compared to known organism database.',
     'Identifies proteins expressed during infection — powerful for clinical diagnostics.'],
    ['Serological tests\n(glycoproteins)',
     'Carbohydrates on cell surface glycoproteins or cell wall',
     'Antibodies bind to specific surface carbohydrate antigens → cells clump (agglutination)',
     'Lancefield group tests: identify Streptococcus species by surface carbohydrate type.\nRapid strep test uses this principle.'],
], [1*inch, 1.1*inch, 2.3*inch, 2.8*inch]))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════
# QUICK REFERENCE SUMMARY
# ═══════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph('QUICK REFERENCE — Chapter 7', h1))
story.append(sp(1))

story.append(Paragraph('The 4 Biomolecules', h2))
story.append(hr())
story.append(tbl([
    ['Biomolecule', 'Elements', 'Monomer', 'Polymer', 'Key Functions'],
    ['Carbohydrates', 'C, H, O', 'Monosaccharide', 'Polysaccharide', 'Energy, structural (cell walls, exoskeletons)'],
    ['Lipids', 'C, H, O\n(also N, S, P)', 'No true monomer', 'No true polymer', 'Membranes, energy storage, hormones, waterproofing'],
    ['Proteins', 'C, H, N, O\n(some S, P)', 'Amino acid', 'Polypeptide / protein', 'Enzymes, transport, structure, defense (antibodies)'],
    ['Nucleic acids', 'C, H, N, O, P', 'Nucleotide', 'DNA / RNA', 'Genetic information, protein synthesis (Ch.10)'],
], [1.1*inch, 0.9*inch, 1*inch, 1.1*inch, 3.1*inch]))
story.append(sp(1))

story.append(Paragraph('Must-Know Microbiology Connections', h2))
story.append(hr())
story.append(tbl([
    ['Concept', 'Connection to Microbiology'],
    ['Peptidoglycan',
     'Made of alternating NAG + NAM (modified sugars). Gram+ = thick layer, Gram− = thin layer + outer membrane.\nTarget of penicillin (blocks peptidoglycan synthesis).'],
    ['Chitin',
     'Polymer of NAG. Fungal cell walls + arthropod exoskeletons. NOT in bacteria.\nDistinguishes fungi from bacteria.'],
    ['Phospholipid bilayer',
     'All cell membranes. Amphipathic: hydrophobic tails inward, hydrophilic heads outward.\nGram− bacteria have a second (outer) membrane containing LPS.'],
    ['Hopanoids vs cholesterol',
     'Cholesterol (eukaryotes + wall-less bacteria like Mycoplasma) strengthens membranes.\nHopanoids (bacteria) = functional equivalent of cholesterol in prokaryotes.\nErgosterol (fungi, some protozoa) = fungal membrane sterol; target of antifungal drugs (e.g., fluconazole).'],
    ['Mycolic acid (wax)',
     'Waxy lipid in Mycobacterium (TB, leprosy) cell wall. Makes it acid-fast — resists decolorization in acid-fast stain.\nConfers antibiotic resistance.'],
    ['Protein denaturation',
     'Autoclave (121°C) denatures proteins → sterilization of equipment.\nAntiseptics denature microbial proteins → disinfection.'],
    ['Primary structure → function',
     'One AA change = possible complete loss of function (cystic fibrosis: loss of phenylalanine in CFTR).\nAlso explains antibiotic resistance mutations.'],
    ['MALDI-TOF',
     'Now standard in clinical labs for rapid ID. Faster and more accurate than traditional culture-based methods for many organisms.'],
    ['Enantiomers in microbiology',
     'Many microbes metabolize ONLY one enantiomeric form of a nutrient or building block.\nSome antibiotics are enantiomer-specific in their activity.'],
], [1.5*inch, 5.7*inch]))
story.append(sp(1))

story.append(Paragraph('Functional Groups Cheat Sheet', h2))
story.append(hr())
story.append(tbl([
    ['Group', 'Formula', 'Property', 'Key Location', 'Popa Note'],
    ['Hydroxyl',   '-OH',   'Polar/hydrophilic',            'Sugars, alcohols',                'Ethanol (CH3-CH2-OH)'],
    ['Carbonyl',   'C=O',   'Polar',                         'Sugars (aldoses/ketoses)',         'Aldehyde = end of chain; Ketone = middle'],
    ['Carboxyl',   '-COOH', 'Acidic',                        'Fatty acids, amino acids',        'Acetic acid (vinegar)'],
    ['Amino',      '-NH2',  'Basic (alkaline)',               'Amino acids, nucleotides',        'All 20 amino acids carry this'],
    ['Sulfhydryl', '-SH',   'Reactive; disulfide bonds',     'Cysteine (amino acid)',           'Stabilizes protein 3° structure'],
    ['Phosphate',  '-PO4-', 'Negative charge',               'ATP, DNA, RNA, phospholipids',    'ATP; backbone of nucleic acids'],
    ['Methyl',     '-CH3',  'Nonpolar; silences genes in DNA','DNA methylation',                'Epigenetic regulation'],
], [0.85*inch, 0.7*inch, 1.45*inch, 1.5*inch, 2.7*inch]))

doc.build(story)
print('Ch7 study guide PDF saved successfully.')
