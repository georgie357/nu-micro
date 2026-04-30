# BIO203 Ch.7 Multiple Choice Questions - Version 4
# V4: Lecture-slide-only. REMOVED: Q15 (hopanoids), Q16 (ergosterol), Q20 (PHB granules)
# 37 questions total (was 40). Renumbered.

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
import os

os.makedirs('C:/Users/User/Dropbox/Nu micro/Ch 7', exist_ok=True)

OUTPUT = 'C:/Users/User/Dropbox/Nu micro/Ch 7/BIO203_Ch7_MC_Questions_v4.pdf'

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.75*inch, bottomMargin=0.75*inch)

h1  = ParagraphStyle('h1', fontSize=13, fontName='Helvetica-Bold', spaceAfter=4, spaceBefore=6,
                     alignment=TA_CENTER, borderPad=4, borderWidth=1, borderColor=colors.black,
                     backColor=colors.Color(0.92, 0.92, 0.92))
h2  = ParagraphStyle('h2', fontSize=10, fontName='Helvetica-Bold', spaceAfter=3, spaceBefore=10,
                     textColor=colors.Color(0.15, 0.15, 0.15))
q   = ParagraphStyle('q',  fontSize=9, fontName='Helvetica-Bold', spaceAfter=2, spaceBefore=5, leading=13)
opt = ParagraphStyle('opt',fontSize=9, fontName='Helvetica', spaceAfter=1, leftIndent=16, leading=12)
ans = ParagraphStyle('ans',fontSize=8, fontName='Helvetica-Bold', spaceAfter=1, leftIndent=16,
                     leading=11, textColor=colors.HexColor('#0000aa'))
cit = ParagraphStyle('cit',fontSize=7.5, fontName='Helvetica-Oblique', spaceAfter=5, leftIndent=16,
                     leading=11, textColor=colors.Color(0.4, 0.4, 0.4))

cell_body = ParagraphStyle('cb', fontName='Helvetica',      fontSize=8, leading=11, spaceAfter=0)
cell_bold = ParagraphStyle('cB', fontName='Helvetica-Bold', fontSize=8, leading=11, spaceAfter=0)

def _cell(val, hdr=False):
    if isinstance(val, str):
        return Paragraph(val.replace('\n', '<br/>'), cell_bold if hdr else cell_body)
    return val

def tbl(data, widths):
    wrapped = [[_cell(c, hdr=(i == 0)) for c in row] for i, row in enumerate(data)]
    t = Table(wrapped, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('GRID',           (0,0), (-1,-1), 0.5, colors.black),
        ('BACKGROUND',     (0,0), (-1, 0), colors.Color(0.82, 0.82, 0.82)),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.Color(0.95, 0.95, 0.95)]),
        ('TOPPADDING',     (0,0), (-1,-1), 4),
        ('BOTTOMPADDING',  (0,0), (-1,-1), 4),
        ('LEFTPADDING',    (0,0), (-1,-1), 4),
        ('RIGHTPADDING',   (0,0), (-1,-1), 4),
        ('VALIGN',         (0,0), (-1,-1), 'TOP'),
    ]))
    return t

def sp(n=1): return Spacer(1, n * 0.1 * inch)

story = []

story.append(Paragraph('BIO203 — Chapter 7 — 37 Multiple Choice Questions — Version 4', h1))
story.append(Paragraph('Microbial Biochemistry | Lecture Slides Only | Answer key included',
    ParagraphStyle('sub', fontSize=9, fontName='Helvetica-Oblique', spaceAfter=4, alignment=TA_CENTER)))
story.append(HRFlowable(width='100%', thickness=1.5, color=colors.Color(0.1, 0.1, 0.5), spaceAfter=6))
story.append(sp(1))

# Format: (num, question_text, [A, B, C, D], answer, citation)
questions = [
    # 7.1 Organic Molecules
    (1,
     "Which of the following statements about lipids is CORRECT?",
     ["A. Lipids are assembled from glycerol monomers into glycerol polymers",
      "B. Lipids have no true monomers and no true polymers",
      "C. Lipids always contain nitrogen in their structure",
      "D. Lipids are hydrophilic and dissolve readily in water"],
     "B", "Popa Ch.7 slide 19"),

    (2,
     "Glucose, galactose, and fructose are examples of:",
     ["A. Disaccharides with different glycosidic bonds",
      "B. Structural isomers — same molecular formula (C6H12O6) but different arrangement of atoms",
      "C. Stereoisomers that are mirror images of each other",
      "D. Polymers formed by dehydration synthesis"],
     "B", "Popa Ch.7 slide 7"),

    (3,
     "D-aspartame is tasteless while L-aspartame is sweet. These two molecules are best described as:",
     ["A. Structural isomers",
      "B. Constitutional isomers",
      "C. Enantiomers — non-superimposable mirror images",
      "D. Epimers"],
     "C", "Popa Ch.7 slide 8"),

    (4,
     "In dehydration synthesis, two monomers join to form a polymer. What is released in this reaction?",
     ["A. Carbon dioxide (CO2)",
      "B. Hydrogen gas (H2)",
      "C. A water molecule (H2O)",
      "D. A phosphate group"],
     "C", "Popa Ch.7 slide 11"),

    (5,
     "Which functional group is responsible for the acidic properties of amino acids and fatty acids?",
     ["A. Amino group (-NH2)",
      "B. Hydroxyl group (-OH)",
      "C. Carboxyl group (-COOH)",
      "D. Phosphate group (-PO4-)"],
     "C", "Popa Ch.7 slide 10"),

    (6,
     "The methyl group (-CH3) added to DNA is associated with:",
     ["A. Energy storage in ATP",
      "B. Epigenetic regulation — silencing gene expression",
      "C. Forming disulfide bridges in protein structure",
      "D. Creating the hydrophilic head of phospholipids"],
     "B", "Popa Ch.7 slide 10"),

    # 7.2 Carbohydrates
    (7,
     "Which polysaccharide is found EXCLUSIVELY in bacterial cell walls?",
     ["A. Cellulose",
      "B. Chitin",
      "C. Peptidoglycan (contains NAM — N-acetyl muramic acid)",
      "D. Glycogen"],
     "C", "Popa Ch.7 slide 17 — NAM is bacteria-only"),

    (8,
     "N-acetyl muramic acid (NAM) is significant because:",
     ["A. It is found in fungal cell walls and arthropod exoskeletons",
      "B. It is found ONLY in prokaryotic (bacterial) peptidoglycan — not in any eukaryote",
      "C. It is the monomer of chitin in fungi",
      "D. It is found in plant cellulose cell walls"],
     "B", "Popa Ch.7 slide 17"),

    (9,
     "Chitin is a polymer of:",
     ["A. N-acetyl muramic acid (NAM)",
      "B. N-acetyl glucosamine (NAG) only",
      "C. Alternating NAG and NAM",
      "D. Glucose only"],
     "B", "Popa Ch.7 slide 17"),

    (10,
     "Penicillin kills bacteria by targeting:",
     ["A. The ribosome — preventing protein synthesis",
      "B. DNA replication — causing strand breaks",
      "C. Peptidoglycan synthesis — blocking cross-linking of the cell wall",
      "D. The cytoplasmic membrane — disrupting ion gradients"],
     "C", "Popa Ch.7 slide 17"),

    (11,
     "Which of the following correctly distinguishes storage polysaccharides?",
     ["A. Starch is the animal storage form; glycogen is the plant storage form",
      "B. Starch is the plant storage form; glycogen is the animal (and bacterial) storage form",
      "C. Chitin is used for storage in insects; cellulose is used for storage in plants",
      "D. Glycogen is used for storage in fungi; starch is used in bacteria"],
     "B", "Popa Ch.7 slide 16"),

    (12,
     "Ribose and deoxyribose are both pentose sugars (5 carbons). Their difference is:",
     ["A. Ribose has a ketone group; deoxyribose has an aldehyde group",
      "B. Deoxyribose is missing one oxygen atom (the -OH at C2 is replaced by -H)",
      "C. Ribose is found in DNA; deoxyribose is found in RNA",
      "D. They are enantiomers that rotate polarized light in opposite directions"],
     "B", "Popa Ch.7 slide 14"),

    # 7.3 Lipids
    (13,
     "Which lipid type forms the basis of ALL cell membranes?",
     ["A. Triglycerides — because they provide the most energy per gram",
      "B. Steroids — because cholesterol stabilizes all membranes",
      "C. Phospholipids — because they are amphipathic and spontaneously form bilayers in water",
      "D. Waxes — because they are waterproof and rigid"],
     "C", "Popa Ch.7 slide 22"),

    (14,
     "Amphipathic means a molecule:",
     ["A. Contains both saturated and unsaturated fatty acids",
      "B. Has both hydrophilic (polar) and hydrophobic (nonpolar) regions",
      "C. Can function as both an acid and a base",
      "D. Contains both carbon and nitrogen in its structure"],
     "B", "Popa Ch.7 slide 22"),

    (15,
     "Mycolic acid is a waxy lipid found in the cell wall of Mycobacterium tuberculosis. Its clinical significance is:",
     ["A. It forms the outer membrane of Gram-negative bacteria containing LPS",
      "B. It causes Mycobacterium to stain PINK in the acid-fast stain by resisting acid-alcohol decolorization",
      "C. It is the target of penicillin, explaining why TB is treated with penicillin",
      "D. It makes the cell wall similar to chitin, classifying Mycobacterium as a fungus"],
     "B", "Popa Ch.7 slide 25"),

    (16,
     "A saturated fatty acid differs from an unsaturated fatty acid in that saturated fatty acids:",
     ["A. Contain only double bonds between carbon atoms",
      "B. Contain only single bonds — no double bonds — allowing tighter packing → solid at room temperature",
      "C. Have a shorter carbon chain length",
      "D. Contain a phosphate group in addition to the hydrocarbon chain"],
     "B", "Popa Ch.7 slide 20"),

    (17,
     "Triglycerides provide more than twice the calories per gram compared to carbohydrates or proteins because:",
     ["A. They contain nitrogen, which releases more energy during catabolism",
      "B. Their hydrocarbon chains are highly reduced (more C-H bonds) and release more energy when oxidized",
      "C. They are polymers while carbohydrates are monomers",
      "D. They contain phosphate groups that store energy like ATP"],
     "B", "Popa Ch.7 slide 21"),

    # 7.4 Proteins
    (18,
     "The primary structure of a protein is:",
     ["A. The alpha helices and beta pleated sheets formed by hydrogen bonding",
      "B. The overall 3D shape formed by disulfide bridges and hydrophobic interactions",
      "C. The sequence of amino acids in the polypeptide chain, held together by peptide bonds",
      "D. The assembly of multiple polypeptide subunits into a functional complex"],
     "C", "Popa Ch.7 slide 31"),

    (19,
     "Secondary protein structure (alpha helices and beta sheets) is maintained by:",
     ["A. Disulfide bridges between cysteine residues",
      "B. Hydrogen bonds between backbone carbonyl (C=O) and amino (-NH) groups — NOT the R side chains",
      "C. Ionic bonds between charged R side chains",
      "D. Hydrophobic interactions between nonpolar R groups"],
     "B", "Popa Ch.7 slide 32"),

    (20,
     "Tertiary protein structure is stabilized by all of the following EXCEPT:",
     ["A. Disulfide bridges between cysteine residues",
      "B. Peptide bonds between adjacent amino acids in the sequence",
      "C. Hydrophobic interactions between nonpolar R side chains",
      "D. Ionic bonds between charged R side chains"],
     "B", "Popa Ch.7 slide 33 — peptide bonds stabilize PRIMARY structure"),

    (21,
     "Quaternary protein structure refers to:",
     ["A. The sequence of amino acids coded by the gene",
      "B. The local folding into alpha helices and beta sheets",
      "C. The overall 3D shape of a single polypeptide",
      "D. The assembly of two or more polypeptide subunits into a functional complex"],
     "D", "Popa Ch.7 slide 34"),

    (22,
     "Hemoglobin is an example of a protein with quaternary structure. It consists of:",
     ["A. A single polypeptide chain with extensive disulfide bridges",
      "B. 2 alpha subunits + 2 beta subunits + 4 heme groups",
      "C. A protein backbone covalently attached to cellulose",
      "D. Only beta-pleated sheets held together by ionic bonds"],
     "B", "Popa Ch.7 slide 34"),

    (23,
     "Denaturation of a protein means:",
     ["A. The primary (amino acid) sequence is destroyed",
      "B. The 2°, 3°, and 4° structure is disrupted while the 1° (amino acid sequence) remains intact",
      "C. All four levels of protein structure are irreversibly destroyed",
      "D. The protein is broken down into individual amino acids by hydrolysis"],
     "B", "Popa Ch.7 slide 35"),

    (24,
     "Autoclave sterilization at 121°C works on microorganisms primarily because:",
     ["A. High temperature breaks all peptide bonds, destroying the primary structure of all proteins",
      "B. High temperature denatures (unfolds) proteins — destroying their functional 3D structure",
      "C. High pressure at 121°C dissolves cell membranes by breaking lipid bonds",
      "D. Steam oxidizes all nucleic acids, destroying genetic information"],
     "B", "Popa Ch.7 slide 35"),

    (25,
     "Which amino acid is specifically involved in forming disulfide bridges that stabilize tertiary protein structure?",
     ["A. Glycine", "B. Alanine", "C. Cysteine", "D. Lysine"],
     "C", "Popa Ch.7 slide 33"),

    (26,
     "All 20 amino acids share the same core structure EXCEPT for one variable component. That variable component is:",
     ["A. The amino group (-NH2)",
      "B. The carboxyl group (-COOH)",
      "C. The alpha carbon",
      "D. The R side chain (R group)"],
     "D", "Popa Ch.7 slide 28"),

    # 7.5 ID Methods
    (27,
     "MALDI-TOF mass spectrometry is now considered STANDARD in clinical microbiology because:",
     ["A. It uses radioactive isotopes to label bacteria, making them visible under fluorescence microscopy",
      "B. It generates a unique mass spectrum (protein/chemical fingerprint) that is compared to a database for rapid ID",
      "C. It sequences the 16S rRNA gene to determine species identity",
      "D. It detects antibiotic resistance genes in bacterial DNA extracts"],
     "B", "Popa Ch.7 slides 44-46"),

    (28,
     "FAME analysis identifies microorganisms by analyzing:",
     ["A. Flagella antigen patterns using agglutination antibodies",
      "B. Fatty acid methyl esters from cell membrane lipids, separated by gas chromatography",
      "C. Protein mass spectra compared to a reference database",
      "D. Polysaccharide antigens on the bacterial cell surface"],
     "B", "Popa Ch.7 slide 47"),

    (29,
     "Serological tests identify organisms by:",
     ["A. Fatty acid profiles determined by gas chromatography",
      "B. Protein mass spectra from MALDI-TOF analysis",
      "C. Antibody-antigen reactions — antibodies bind specific surface molecules",
      "D. 16S rRNA gene sequencing"],
     "C", "Popa Ch.7 slide 48"),

    (30,
     "In MALDI-TOF analysis, the UV laser pulse generates:",
     ["A. Kills the microorganism and releases DNA for PCR amplification",
      "B. Gaseous ions from proteins and chemicals; ions are separated by mass-to-charge ratio",
      "C. Excited fluorochrome dyes attached to antibodies",
      "D. Breaks glycosidic bonds in polysaccharides to release monosaccharides"],
     "B", "Popa Ch.7 slides 44-46"),

    # Mixed / Highest yield traps
    (31,
     "TRAP: Which of the following has NO true monomer and NO true polymer?",
     ["A. Carbohydrates (polysaccharides)",
      "B. Proteins (polypeptides)",
      "C. Lipids",
      "D. Nucleic acids (DNA/RNA)"],
     "C", "Popa Ch.7 slide 19 — most tested trap in Ch.7"),

    (32,
     "TRAP: The cell walls of Archaea differ from bacteria in that Archaea:",
     ["A. Have chitin cell walls like fungi",
      "B. Have thick peptidoglycan like Gram-positive bacteria",
      "C. Have NO peptidoglycan — unique ether-linked lipid walls instead",
      "D. Have LPS (lipopolysaccharide) in an outer membrane like Gram-negative bacteria"],
     "C", "Popa Ch.7 slide 17 + Ch.1 slide 21"),

    (33,
     "TRAP: After denaturation by autoclave (121°C), which level of protein structure remains intact?",
     ["A. Quaternary (subunit assembly)",
      "B. Tertiary (3D fold)",
      "C. Secondary (alpha helices and beta sheets)",
      "D. Primary (amino acid sequence)"],
     "D", "Popa Ch.7 slide 35"),

    (34,
     "TRAP: The Gram stain does NOT work reliably on which of the following?",
     ["A. Staphylococcus aureus (Gram-positive coccus)",
      "B. Mycobacterium tuberculosis (acid-fast; waxy mycolic acid wall resists crystal violet)",
      "C. Escherichia coli (Gram-negative rod)",
      "D. Bacillus anthracis (Gram-positive rod)"],
     "B", "Popa Ch.2 slide 28; Ch.7 slide 25"),

    (35,
     "Which biomolecule has the highest caloric density per gram?",
     ["A. Carbohydrates (~4 kcal/g)",
      "B. Proteins (~4 kcal/g)",
      "C. Lipids (~9 kcal/g — more than double carbs/proteins)",
      "D. Nucleic acids (~4 kcal/g)"],
     "C", "Popa Ch.7 slide 21"),

    (36,
     "TRAP: Which of the following correctly pairs an organism with its cell wall composition?",
     ["A. Fungi — peptidoglycan",
      "B. Gram-positive bacteria — chitin",
      "C. Algae — cellulose",
      "D. Archaea — thick peptidoglycan"],
     "C", "Popa Ch.7 slides 16-17; Ch.1 slides 21-25 — Algae (Protist) = cellulose"),

    (37,
     "TRAP: Which functional group makes a molecule acidic?",
     ["A. Amino group (-NH2)",
      "B. Hydroxyl group (-OH)",
      "C. Carboxyl group (-COOH)",
      "D. Methyl group (-CH3)"],
     "C", "Popa Ch.7 slide 10 — carboxyl = acidic; amino = basic"),
]

# Print questions
story.append(Paragraph("Chapter 7 — 37 Questions (Microbial Biochemistry)", h2))
story.append(HRFlowable(width='100%', thickness=0.75, color=colors.Color(0.1, 0.1, 0.5), spaceAfter=6))

for (num, qtext, opts, correct, citation) in questions:
    story.append(Paragraph(f"{num}. {qtext}", q))
    for o in opts:
        story.append(Paragraph(o, opt))
    story.append(Paragraph(f"Answer: {correct}", ans))
    story.append(Paragraph(f"Source: {citation}", cit))

# Answer Key
story.append(PageBreak())
story.append(Paragraph('ANSWER KEY — Ch.7 Version 4', h1))
story.append(HRFlowable(width='100%', thickness=1, color=colors.Color(0.1, 0.1, 0.5), spaceAfter=8))

rows = [["Q#", "Ans", "Q#", "Ans", "Q#", "Ans", "Q#", "Ans"]]
per_col = 10
for i in range(per_col):
    row = []
    for j in range(4):
        idx = j * per_col + i
        if idx < len(questions):
            row += [str(questions[idx][0]), questions[idx][3]]
        else:
            row += ["", ""]
    rows.append(row)

col_w = [0.55*inch, 0.45*inch] * 4
story.append(tbl(rows, col_w))
story.append(sp(2))
story.append(Paragraph(
    'Sources: Popa BIO203 Ch.7 lecture slides (49 slides). '
    'Version 4 — 37 questions, lecture-slide content only. Textbook-only topics excluded.',
    ParagraphStyle('note', fontSize=7.5, fontName='Helvetica-Oblique', textColor=colors.Color(0.4, 0.4, 0.4))))

doc.build(story)
print("Done -> " + OUTPUT)

