# BIO203A Lab 1: Microscopy - Study Guide (Version 4 - Lecture Slides Only)
# V4: Removed DIC (Nomarski) microscope reference from practice Q7 — not in lecture slides.
# All other content directly tied to Popa Ch.2 slides and Lab 1 docx.

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\chapter 1 and 2\BIO203A_Lab1_Study_Guide_v4.pdf"

h1  = ParagraphStyle('H1', fontName='Helvetica-Bold',   fontSize=15, spaceAfter=5,  textColor=colors.HexColor('#1a1a6e'))
h2  = ParagraphStyle('H2', fontName='Helvetica-Bold',   fontSize=12, spaceAfter=4,  spaceBefore=8, textColor=colors.HexColor('#1a1a6e'))
h3  = ParagraphStyle('H3', fontName='Helvetica-Bold',   fontSize=10, spaceAfter=3,  spaceBefore=5)
bod = ParagraphStyle('BD', fontName='Helvetica',         fontSize=9,  spaceAfter=3,  leading=13)
bul = ParagraphStyle('BL', fontName='Helvetica',         fontSize=9,  spaceAfter=2,  leading=12, leftIndent=14, firstLineIndent=-10)
cit = ParagraphStyle('CT', fontName='Helvetica-Oblique', fontSize=7.5,spaceAfter=2,  textColor=colors.HexColor('#555555'))
tip = ParagraphStyle('TP', fontName='Helvetica-Bold',    fontSize=8.5,spaceAfter=4,  leading=12,
                     backColor=colors.HexColor('#fff3cd'), borderPad=4,
                     borderWidth=0.5, borderColor=colors.HexColor('#cc8800'))

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

def sp(n=6): return Spacer(1, n)
def B(t): return f'<b>{t}</b>'
def HY(text): return Paragraph(f'HIGHEST YIELD: {text}', tip)

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                        leftMargin=0.75*inch, rightMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)
W = 7.0 * inch
story = []

story += [
    Paragraph("BIO203A Microbiology Lab — National University",
              ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=16, alignment=TA_CENTER, textColor=colors.HexColor('#1a1a6e'))),
    sp(3),
    Paragraph("Lab 1: Microscopy — Study Guide (Version 4 — Lecture Slides Only)",
              ParagraphStyle('TS', fontName='Helvetica-Bold', fontSize=13, alignment=TA_CENTER)),
    sp(3),
    Paragraph("Source: Lab 1 docx (Popa) + Ch.2 slides (33) + Ch.1 slides (29) | Textbook-only topics excluded",
              ParagraphStyle('TC', fontName='Helvetica-Oblique', fontSize=9, alignment=TA_CENTER, textColor=colors.grey)),
    HRFlowable(width=W, thickness=2, color=colors.HexColor('#1a1a6e')),
    sp(8),
]

# Section 1: Objectives
story.append(Paragraph("1. Lab 1 Objectives and Lecture Connections", h2))
story.append(tbl([
    ["Lab objective", "Lecture connection", "Source"],
    ["Correct use of compound light microscope",
     "Ch.2: parts, handling, parfocal lenses, coarse/fine focus rules",
     "Popa Ch.2 slides 9-10; Lab 1 docx"],
    ["Explain magnification",
     "Ch.2: total mag = ocular x objective; FOV decreases as mag increases",
     "Popa Ch.2 slide 8"],
    ["Name parts of microscope",
     "Ch.2: base, arm, stage, condenser, iris diaphragm, ocular (10x), objectives (4x/10x/40x/100x), coarse/fine knobs",
     "Lab 1 docx"],
    ["Observe microscopic characteristics of microorganism groups",
     "Ch.1: bacteria (~1 um, prokaryote), protozoa (eukaryote, cilia/flagella), fungi (eukaryote, chitin wall); size scale",
     "Popa Ch.1 slides 20-25"],
], [2.0*inch, 3.0*inch, 2.0*inch]))
story.append(sp())

# Section 2: Parts
story.append(Paragraph("2. Microscope Parts — Functions and Rules", h2))
story.append(HY("Coarse focus = ONLY 4x and 10x. Never 40x or 100x. This rule appears in every lab practical."))
story.append(tbl([
    ["Part", "Function", "Critical rule / Exam trap"],
    ["Coarse focus knob", "Large knob; rough focus",
     "USE ONLY with 4x and 10x. NEVER with 40x or 100x — crashes into slide"],
    ["Fine focus knob", "Small knob; precise focus",
     "Required for 40x and 100x; use after coarse for 4x and 10x"],
    ["Condenser", "Focuses light onto specimen (below stage)",
     "RAISE condenser at high magnification to maximize NA and light"],
    ["Iris diaphragm", "Controls light cone entering condenser",
     "Close to INCREASE contrast; open to INCREASE brightness"],
    ["Parfocal lenses", "Focused at one mag = near-focused when switching",
     "Only minor fine-focus after switching objectives — tested concept"],
    ["Oil immersion (100x)", "Highest magnification; requires immersion oil",
     "One drop of oil on slide; NEVER use 40x in oil; clean lens with lens paper after use"],
    ["Ocular micrometer", "Calibrated scale in eyepiece (if present)",
     "Used to measure cell size directly in micrometers"],
], [1.4*inch, 2.3*inch, 3.3*inch]))
story.append(sp())

# Section 3: Magnification/FOV
story.append(Paragraph("3. Magnification, FOV, and Calculations", h2))
story.append(HY("As magnification increases: FOV decreases, working distance decreases, brightness decreases, depth of field decreases."))
story.append(tbl([
    ["Objective", "Total mag.", "Approx. FOV", "Working dist.", "Coarse?", "Best for"],
    ["4x (scanning)",       "40x",   "~4.5 mm",  "~30 mm",   "Yes", "Finding specimen; orientation"],
    ["10x (low power)",     "100x",  "~1.8 mm",  "~10 mm",   "Yes", "Protozoa, algae, larger cells"],
    ["40x (high-dry)",      "400x",  "~450 µm",  "~0.5 mm",  "NO",  "Yeast, large bacteria, fungal structures"],
    ["100x (oil immersion)","1000x", "~180 µm",  "~0.1 mm",  "NO",  "Bacteria (must use oil); Gram stain; endospores"],
], [1.3*inch, 0.7*inch, 0.85*inch, 0.85*inch, 0.65*inch, 2.65*inch]))
story.append(sp(4))

story.append(Paragraph(B("FOV calculation:"), h3))
story.append(Paragraph(
    "FOV2 = FOV1 x (Mag1 / Mag2). Example: FOV at 100x = 1.8 mm. At 400x: 1.8 mm x (100/400) = 0.45 mm = 450 µm.",
    bod))
story.append(Paragraph(B("Cell count across FOV:"), h3))
story.append(Paragraph(
    "Number of cells = FOV diameter / cell size. "
    "FOV = 450 µm; Bacillus = 2 µm: 450/2 = 225 cells. Yeast = 10 µm: 450/10 = 45 cells.",
    bod))
story.append(sp())

# Section 4: Resolution
story.append(Paragraph("4. Resolution and Immersion Oil", h2))
story.append(tbl([
    ["Concept", "Definition / Rule", "Exam tip"],
    ["Resolution", "Ability to distinguish two adjacent points as separate; smaller resolvable distance = BETTER resolution", "More magnification without better resolution = 'empty magnification'"],
    ["Wavelength effect", "Shorter wavelength = better resolution", "Electrons have far shorter wavelengths than light → TEM resolves 2.5 nm vs LM 200 nm"],
    ["Numerical Aperture (NA)", "Measure of lens's ability to gather light; higher NA = better resolution", "Immersion oil raises NA by preventing refraction"],
    ["Immersion oil", "RI of oil (~1.515) = RI of glass; prevents light bending at 100x lens; more light enters objective",
     "Required ONLY at 100x. Never use with 40x or lower."],
    ["Resolution values", "Human eye ~200 µm; LM ~200 nm; SEM ~20 nm; TEM ~2.5 nm", "TEM is best resolution; SEM gives 3D surface — different uses"],
], [1.3*inch, 2.7*inch, 3.0*inch]))
story.append(sp())

# Section 5: Organisms
story.append(Paragraph("5. Organisms in Lab 1 — Classification and Microscopy", h2))
story.append(tbl([
    ["Organism", "Domain/Group", "Size &amp; Objective", "Key features", "Pathogenic example"],
    ["Paramecium caudatum",
     "Eukarya\nProtozoa (Protist)\nUnicellular",
     "150-300 µm\n10x (100x)",
     "Slipper-shaped; cilia (locomotion + feeding); macronucleus; contractile vacuoles; NO cell wall",
     "Not pathogenic itself. Related: Giardia lamblia (protozoa) = pathogenic"],
    ["Saccharomyces cerevisiae\n(baker's yeast)",
     "Eukarya\nFungi\nUnicellular",
     "5-10 µm\n40x (400x)",
     "Oval/spherical; budding (asexual reproduction); CHITIN cell wall; clusters during budding",
     "Not pathogenic. Related: Candida albicans = pathogenic yeast"],
    ["Bacillus subtilis",
     "Bacteria\nDomain: Bacteria\nGram-positive",
     "0.5 x 2-4 µm\n100x oil (1000x)",
     "Rod-shaped (bacillus); chains; PEPTIDOGLYCAN G+ wall; endospores in older cultures",
     "Generally non-pathogenic. Related: B. anthracis = anthrax (Koch 1876 proof)"],
    ["Algae\n(e.g., Spirogyra)",
     "Eukarya\nAlgae (Protist)",
     "10-100 µm+\n10x or 40x",
     "Green chloroplasts; CELLULOSE cell wall; not pathogenic; source of agar (red algae)",
     "Not pathogenic"],
    ["Mold\n(e.g., Aspergillus)",
     "Eukarya\nFungi\nMulticellular",
     "Hyphae 5-10 µm\n10x-40x",
     "Filamentous hyphae; conidia (asexual spores); CHITIN cell wall",
     "Some are: A. fumigatus in immunocompromised"],
], [1.3*inch, 1.1*inch, 0.95*inch, 2.1*inch, 1.55*inch]))
story.append(sp())

# Section 6: Staining
story.append(Paragraph("6. Staining Methods Relevant to Lab 1 Organisms (Ch.2)", h2))
story.append(HY("Gram stain steps in ORDER are tested. G+ = purple. G- = pink. Endospore: spores GREEN, vegetative cells PINK."))
story.append(tbl([
    ["Stain", "Steps", "Results", "Lab 1 organism"],
    ["Simple stain\n(crystal violet or methylene blue)",
     "Fix smear → apply single dye 30-60 sec → water rinse",
     "All cells same color",
     "Bacillus: rod shape + arrangement; yeast: oval cells + budding"],
    ["Gram stain (4 steps)",
     "1. Crystal violet (all purple)\n2. Gram's iodine (mordant)\n3. Alcohol (decolorize)\n4. Safranin (counterstain)",
     "G+: PURPLE\nG-: PINK",
     "Bacillus subtilis = G+ PURPLE. Trap: over-decolorize → G+ looks G-"],
    ["Wet mount\n(no stain)",
     "Drop of culture on slide + coverslip; no fixation",
     "Live, motile organisms",
     "Paramecium: cilia movement visible; yeast: budding in real time"],
    ["Endospore stain\n(Schaeffer-Fulton)",
     "1. Malachite green + steam\n2. Water wash\n3. Safranin counterstain",
     "Spores: GREEN\nVeg. cells: PINK",
     "Bacillus subtilis: endospores vs vegetative cells in older cultures"],
], [1.2*inch, 2.1*inch, 1.1*inch, 2.6*inch]))
story.append(sp())

# Section 7: Key numbers
story.append(Paragraph("7. Key Numbers — Must Memorize", h2))
story.append(tbl([
    ["Item", "Value", "Source / Exam context"],
    ["Minimum visible to naked eye", "~100 µm", "Popa Ch.2 slide 3 — bacterium is 100x too small"],
    ["Typical virus size", "~100 nm", "Popa Ch.1 slide 3 — acellular"],
    ["Typical bacterium size", "~1 µm (0.5-5 µm)", "Popa Ch.1 slide 3 — need 1000x oil"],
    ["Typical eukaryotic cell", "~10-100 µm", "Popa Ch.1 slide 3"],
    ["Light microscope resolution", "~200 nm", "Popa Ch.2 slide 8"],
    ["TEM resolution / max mag", "2.5 nm / 100,000x", "Popa Ch.2 slide 16 — 2D internal sections"],
    ["SEM resolution / max mag", "20 nm / 10,000x", "Popa Ch.2 slide 17 — 3D surface"],
    ["Immersion oil RI", "~1.515 (same as glass)", "Popa Ch.2 slide 10"],
    ["Total mag at 100x obj.", "1000x (10x ocular x 100x)", "Lab 1 docx"],
    ["FOV at 400x total", "~450 µm", "Calculated from 1.8 mm at 100x"],
    ["FOV at 1000x total", "~180 µm", "Calculated — needed for Bacillus estimation"],
    ["Gram stain developer", "Hans Christian Gram, 1884", "Popa Ch.2 slide 26"],
], [2.5*inch, 1.8*inch, 2.7*inch]))
story.append(sp())

# Section 8: Practice questions
story.append(Paragraph("8. Practice Questions — Highest Yield", h2))
qs = [
    ("Why must you NEVER use the coarse focus at 40x or 100x?",
     "Working distance at 40x (~0.5 mm) and 100x (~0.1 mm) is extremely small. Coarse focus knob moves stage too fast — will drive objective into slide, cracking slide and scratching objective lens."),
    ("Why is immersion oil required for the 100x objective?",
     "Without oil, light refracts (bends) as it passes from glass into air, missing the tiny 100x lens. Immersion oil (RI ~1.515 = glass RI) allows light to pass straight through without bending — more light enters objective = better resolution."),
    ("What is parfocality?",
     "Parfocal = when specimen is in focus at one objective, switching to another objective leaves it at approximately the same focal plane. Only minor fine-focus adjustment needed after switching — no starting from scratch."),
    ("FOV at 100x total = 1.8 mm. Paramecium is 200 µm long. How many fit across FOV?",
     "FOV = 1.8 mm = 1800 µm. Number of cells = 1800 µm / 200 µm = 9 Paramecium."),
    ("You switch from 10x to 40x objective. What changes?",
     "FOV decreases by 4x (1.8 mm → 0.45 mm). Brightness decreases. Depth of field decreases. Working distance decreases. Open iris diaphragm and raise condenser to compensate."),
    ("What are the four steps of the Gram stain in order?",
     "1. Crystal violet (primary — all cells purple). 2. Gram's iodine (mordant — CV-I complex forms). 3. Alcohol/acetone (decolorizer — G+ retains; G- loses). 4. Safranin (counterstain — G- turns pink). Result: G+ = purple; G- = pink."),
    ("Which microscope is best for live unstained Paramecium?",
     "Phase-contrast — creates high contrast without staining or killing cells. Darkfield also acceptable (good for motility). Brightfield shows poor contrast on live unstained organisms."),
    ("What is the cell wall composition of each: bacteria, fungi, algae?",
     "Bacteria = peptidoglycan (Gram+ thick; Gram- thin). Fungi = chitin. Algae = cellulose. Archaea = no peptidoglycan (unique lipid walls). Protozoa = no cell wall (most)."),
]

for i, (q, a) in enumerate(qs, 1):
    story.append(Paragraph(f"Q{i}. {q}", ParagraphStyle('QQ', fontName='Helvetica-Bold', fontSize=9, spaceAfter=2, leading=13)))
    story.append(Paragraph(f"A: {a}", ParagraphStyle('AA', fontName='Helvetica', fontSize=9, spaceAfter=6, leading=13, leftIndent=14, textColor=colors.HexColor('#00008b'))))

story.append(sp(4))
story.append(Paragraph(
    "Sources: BIO203A Lab 1 Microscopy docx (Popa); Popa Ch.2 lecture slides (33 slides); "
    "Popa Ch.1 lecture slides (29 slides). Version 4 — lecture-slide content only.", cit))

doc.build(story)
print("Done -> " + OUTPUT)
