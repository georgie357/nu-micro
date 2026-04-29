# BIO203 Lab 1: Microscopy - Study Guide (Version 2)
# Built from actual Lab 1 docx + Ch.2 Popa slides + OpenStax
# Output: C:\Users\User\Dropbox\Nu micro\chapter 1 and 2\BIO203A_Lab1_Study_Guide_v2.pdf

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\chapter 1 and 2\BIO203A_Lab1_Study_Guide_v2.pdf"

h1  = ParagraphStyle('H1', fontName='Helvetica-Bold',   fontSize=15, spaceAfter=5,  textColor=colors.HexColor('#1a1a6e'))
h2  = ParagraphStyle('H2', fontName='Helvetica-Bold',   fontSize=12, spaceAfter=4,  spaceBefore=8, textColor=colors.HexColor('#1a1a6e'))
h3  = ParagraphStyle('H3', fontName='Helvetica-Bold',   fontSize=10, spaceAfter=3,  spaceBefore=5)
bod = ParagraphStyle('BD', fontName='Helvetica',         fontSize=9,  spaceAfter=3,  leading=13)
bul = ParagraphStyle('BL', fontName='Helvetica',         fontSize=9,  spaceAfter=2,  leading=12, leftIndent=14, firstLineIndent=-10)
cit = ParagraphStyle('CT', fontName='Helvetica-Oblique', fontSize=7.5,spaceAfter=2,  textColor=colors.HexColor('#555555'))

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

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                        leftMargin=0.75*inch, rightMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)
W = 7.0 * inch
story = []

story += [
    Paragraph("BIO203A Microbiology Lab — National University", ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=16, alignment=TA_CENTER, textColor=colors.HexColor('#1a1a6e'))),
    sp(3),
    Paragraph("Lab 1: Microscopy — Study Guide (Version 2)", ParagraphStyle('TS', fontName='Helvetica-Bold', fontSize=13, alignment=TA_CENTER)),
    sp(3),
    Paragraph("Source: Lab 1 docx (Popa) + Ch.2 lecture slides (33 slides) + Ch.1 slides (29 slides) + OpenStax Ch.1-2",
              ParagraphStyle('TC', fontName='Helvetica-Oblique', fontSize=9, alignment=TA_CENTER, textColor=colors.grey)),
    HRFlowable(width=W, thickness=2, color=colors.HexColor('#1a1a6e')),
    sp(8),
]

# Section 1
story.append(Paragraph("1. Lab 1 Objectives and Concepts", h2))
story.append(tbl([
    ["Lab Objective", "Lecture Connection", "Source"],
    ["Demonstrate correct use of compound light microscope",
     "Ch.2: brightfield microscope parts, handling rules, parfocal lenses, coarse/fine focus rules",
     "Popa Ch.2 slides 9-10; Lab 1 docx"],
    ["Explain magnification",
     "Ch.2: total magnification = ocular x objective; FOV decreases as magnification increases",
     "Popa Ch.2 slide 8; OpenStax 2.1"],
    ["Name main parts of microscope",
     "Ch.2: base, arm, stage, condenser, iris diaphragm, ocular (10x), objectives (4x/10x/40x/100x), coarse/fine knobs",
     "Lab 1 docx; OpenStax 2.2"],
    ["Observe microscopic characteristics of microorganism groups",
     "Ch.1: bacteria (prokaryotes, ~1 um), protozoa (eukaryotes, cilia/flagella), fungi (eukaryotes, chitin); size scale",
     "Popa Ch.1 slides 20-25; OpenStax 1.3"],
], [2.0*inch, 3.0*inch, 2.0*inch]))
story.append(sp())

# Section 2
story.append(Paragraph("2. Compound Microscope — Parts and Functions", h2))
story.append(Paragraph(B("Handling rules (Lab 1 docx — must know for lab practical):"), h3))
for item in [
    "Always carry with TWO hands: one on the arm, one under the base",
    "Store with scanning (4x) objective pointing down, stage lowered as far as possible",
    "Clean lenses ONLY with lens paper — never Kleenex, paper towels, or cloth",
    "Clean all oil from 100x lens and stage before storage",
    "Do NOT twist the power cord around the stage",
]:
    story.append(Paragraph(f"• {item}", bul))
story.append(sp())

story.append(tbl([
    ["Part", "Function", "Critical Rule"],
    ["Coarse focus knob", "Large knob; brings specimen into rough focus",
     "USE ONLY with 4x and 10x objectives. NEVER with 40x or 100x — will crash into slide"],
    ["Fine focus knob", "Small knob; final focus adjustment",
     "Always use for 40x and 100x; use after coarse for 4x and 10x"],
    ["Condenser", "Focuses light onto specimen; located below stage",
     "Raise condenser to maximize light at high magnification; lower to reduce light"],
    ["Iris diaphragm", "Controls light cone entering condenser",
     "Close to reduce light/increase contrast; open to increase light at high mag"],
    ["Parfocal", "Property of lens set: focused at one mag stays near-focused when switching",
     "Only minor fine-focus adjustment needed after switching objectives"],
    ["Oil immersion (100x)", "Highest magnification; requires immersion oil",
     "Place one drop of oil on slide before placing 100x objective; NEVER use 40x in oil; clean lens after use"],
    ["Ocular micrometer", "Calibrated scale in the eyepiece (if present)",
     "Used to measure cell size directly in um"],
], [1.4*inch, 2.5*inch, 3.1*inch]))
story.append(sp())

# Section 3
story.append(Paragraph("3. Magnification, Field of View, and Calculations", h2))
story.append(tbl([
    ["Objective", "Total Mag.\n(x10 ocular)", "Approx. FOV\nDiameter", "Working\nDistance", "Coarse\nFocus?", "Best for..."],
    ["4x (scanning)",       "40x",   "~4.5 mm",  "~30 mm",    "Yes", "Finding specimen on slide; orientation"],
    ["10x (low power)",     "100x",  "~1.8 mm",  "~10 mm",    "Yes", "Protozoa, algae, fungi (larger cells)"],
    ["40x (high-dry)",      "400x",  "~0.45 mm", "~0.5 mm",   "No",  "Yeast, large bacteria, fungal structures"],
    ["100x (oil immersion)","1000x", "~0.18 mm", "~0.1 mm",   "No",  "Bacteria (MUST use oil); Gram stain; endospores"],
], [1.3*inch, 0.8*inch, 0.9*inch, 0.9*inch, 0.8*inch, 2.3*inch]))
story.append(sp(4))

story.append(Paragraph(B("FOV calculation method:"), h3))
story.append(Paragraph(
    "When you know FOV at one magnification, you can calculate FOV at another: "
    "FOV2 = FOV1 x (Mag1 / Mag2). Example: if FOV at 100x = 1.8 mm, then at 400x: "
    "FOV = 1.8 mm x (100/400) = 0.45 mm = 450 um.",
    bod))
story.append(sp(4))

story.append(Paragraph(B("Cell count across FOV:"), h3))
story.append(Paragraph(
    "Number of cells across FOV = FOV diameter / cell size. "
    "Example: FOV = 450 um; Bacillus = 2 um long -- 450/2 = 225 cells; "
    "Yeast = 10 um -- 450/10 = 45 cells.",
    bod))
story.append(sp())

# Section 4
story.append(Paragraph("4. Resolution and Immersion Oil (Ch.2 lecture key concepts)", h2))
story.append(tbl([
    ["Concept", "Definition / Rule", "Source"],
    ["Resolution", "Ability to distinguish two adjacent points as separate; smaller distance = better resolution", "Popa Ch.2 slide 8; OpenStax 2.1"],
    ["Wavelength effect", "Shorter wavelength = better resolution (electrons far better than visible light)", "Popa Ch.2 slide 7"],
    ["Numerical Aperture (NA)", "Measure of lens's light-gathering ability; higher NA = better resolution", "Popa Ch.2 slide 8"],
    ["Refraction problem", "Light bends when passing from glass slide into air; may miss small 100x lens", "Popa Ch.2 slide 6"],
    ["Immersion oil solution", "RI of oil (~1.515) = RI of glass; light passes without bending; more light enters objective", "Popa Ch.2 slides 6 & 10; Lab 1 docx"],
    ["Resolution comparison", "Human eye ~200 um; compound light microscope ~200 nm; TEM ~2.5 nm; SEM ~20 nm", "Popa Ch.2 slide 8; OpenStax 2.1"],
], [1.5*inch, 3.5*inch, 2.0*inch]))
story.append(sp())

# Section 5
story.append(Paragraph("5. Organisms Observed in Lab 1 — Ch.1 Classification Connections", h2))
story.append(tbl([
    ["Organism", "Domain/Group\n(Ch.1 classification)", "Size &\nBest Objective", "Key Morphology to Observe", "Pathogenic?"],
    ["Paramecium caudatum",
     "Eukarya\nProtozoa (Protist)\nUnicellular",
     "150-300 um\n10x (100x)",
     "Slipper-shaped; cilia around periphery (locomotion); macronucleus; contractile vacuoles",
     "Not pathogenic (similar pathogenic example: Giardia lamblia)"],
    ["Saccharomyces cerevisiae\n(baker's yeast)",
     "Eukarya\nFungi\nUnicellular (yeast form)",
     "5-10 um\n40x (400x)",
     "Oval/spherical cells; budding (asexual reproduction); chitin cell wall; clusters during budding",
     "Not pathogenic (similar pathogenic example: Candida albicans)"],
    ["Bacillus subtilis",
     "Bacteria\nDomain: Bacteria\nGram-positive",
     "0.5x2-4 um\n100x oil (1000x)",
     "Rod-shaped (bacillus); chains; endospores as refractile bodies in older cultures; Gram+ = purple",
     "Generally non-pathogenic; related B. anthracis = anthrax (Koch 1876)"],
    ["Algae (e.g., Spirogyra)",
     "Eukarya\nAlgae (Protist)",
     "10-100 um+\n10x or 40x",
     "Green chloroplasts (spiral in Spirogyra); rigid cellulose cell wall; no centrioles",
     "Not pathogenic"],
    ["Fungi (mold, e.g., Aspergillus)",
     "Eukarya\nFungi\nMulticellular (mold form)",
     "Hyphae 5-10 um\n10x-40x",
     "Filamentous hyphae (branching threads); conidia (asexual spores); chitin cell wall",
     "Some are (Aspergillus fumigatus in immunocompromised)"],
], [1.3*inch, 1.3*inch, 0.9*inch, 2.2*inch, 1.3*inch]))
story.append(sp())

# Section 6
story.append(Paragraph("6. Staining Methods Used with These Organisms (Ch.2 lecture)", h2))
story.append(tbl([
    ["Stain", "Steps Summary", "What you see", "Relevant for Lab 1 organisms"],
    ["Simple stain\n(crystal violet or\nmethylene blue)",
     "Fix smear -> apply dye 30-60 sec -> water rinse",
     "All cells same color against white background",
     "Bacillus: confirms rod shape and arrangement; yeast: shows oval cells and budding"],
    ["Gram stain\n(4 steps)",
     "1. Crystal violet (all purple)\n2. Gram's iodine (mordant)\n3. Alcohol decolorize\n4. Safranin counterstain",
     "G+: PURPLE\nG-: PINK",
     "Bacillus subtilis = Gram+ (PURPLE thick peptidoglycan); Gram staining does not apply to fungi or protozoa in same way"],
    ["Wet mount\n(no stain)",
     "Place drop of culture on slide + coverslip; observe immediately",
     "Live, motile organisms visible; phase-contrast shows internal structures best",
     "Paramecium: observe live cilia movement; yeast: observe budding in real time"],
    ["Endospore stain\n(Schaeffer-Fulton)",
     "Malachite green + steam -> water wash -> safranin counterstain",
     "Endospores: GREEN\nVegetative cells: PINK",
     "Bacillus subtilis: distinguishes endospores from vegetative cells in older cultures"],
], [1.2*inch, 2.0*inch, 1.3*inch, 2.5*inch]))
story.append(sp())

# Section 7: Key numbers
story.append(Paragraph("7. Key Numbers — Lab 1 + Ch.1 & Ch.2", h2))
story.append(tbl([
    ["Item", "Value", "Source"],
    ["Minimum size visible to naked eye", "~100 um", "Popa Ch.2 slide 3"],
    ["Typical virus size", "~100 nm", "Popa Ch.1 slide 3"],
    ["Typical bacterium size", "~1 um (0.5-5 um)", "Popa Ch.1 slide 3"],
    ["Typical eukaryotic cell", "~10-100 um", "Popa Ch.1 slide 3"],
    ["Light microscope resolution", "~200 nm", "Popa Ch.2 slide 8"],
    ["TEM resolution / max magnification", "2.5 nm / 100,000x", "Popa Ch.2 slide 16"],
    ["SEM resolution / max magnification", "20 nm / 10,000x", "Popa Ch.2 slide 17"],
    ["Immersion oil refractive index", "~1.515 (same as glass)", "Popa Ch.2 slide 10"],
    ["Total magnification with 100x oil", "1000x (10x ocular x 100x objective)", "Lab 1 docx; Popa Ch.2 slide 9"],
    ["FOV at 400x (approx.)", "~450 um (0.45 mm)", "Lab 1 docx calculations"],
    ["FOV at 1000x (approx.)", "~180 um (0.18 mm)", "Lab 1 docx calculations"],
    ["Gram stain developer (1884)", "Hans Christian Gram", "Popa Ch.2 slide 26"],
    ["Leeuwenhoek first described animalcules", "1675", "Popa Ch.1 slide 6; Ch.2 history"],
], [3.0*inch, 2.0*inch, 2.0*inch]))
story.append(sp())

# Section 8: Practice Qs
story.append(Paragraph("8. Practice Questions for Lab 1", h2))
qs = [
    ("Why must you NEVER use the coarse focus knob at 40x or 100x?",
     "The working distance at 40x (~0.5 mm) and 100x (~0.1 mm) is extremely small. "
     "Using the coarse knob can drive the objective into the slide, cracking the slide and potentially scratching the objective lens."),
    ("Why is immersion oil required for the 100x objective?",
     "Without oil, light refracts (bends) as it passes from the glass slide into air, "
     "missing the small 100x objective lens. Immersion oil has the same refractive index (~1.515) as glass, "
     "so light passes straight through without bending, maximizing light entering the lens and improving resolution."),
    ("What is parfocality and why is it useful?",
     "Parfocal means that when the specimen is in focus at one magnification, "
     "switching to another objective leaves it at approximately the same focal plane. "
     "Only minor fine-focus adjustment is needed, preventing the need to re-focus from scratch at each magnification."),
    ("You observe Paramecium at 100x total magnification. The FOV is 1.8 mm. "
     "Paramecium are 200 um long. How many fit across the FOV?",
     "FOV = 1.8 mm = 1800 um. Number of cells = 1800 / 200 = 9 Paramecium across the FOV."),
    ("You switch from 10x to 40x objective. What happens to the FOV and brightness?",
     "FOV decreases by factor of 4 (from ~1.8 mm to ~0.45 mm). "
     "Brightness also decreases (less light per unit area at higher magnification). "
     "You need to open the iris diaphragm and/or increase lamp brightness."),
    ("What are the four steps of the Gram stain in order?",
     "1. Crystal violet (primary stain) - all cells purple. "
     "2. Gram's iodine (mordant) - CV-iodine complex forms. "
     "3. Alcohol/acetone (decolorizer) - G+ keeps purple; G- loses color. "
     "4. Safranin (counterstain) - G- stains pink. "
     "Result: G+ = purple; G- = pink."),
    ("Which microscope type would be BEST for observing live, unstained Paramecium in water?",
     "Phase-contrast microscopy. It uses destructive interference to create high contrast "
     "without staining or killing the cells. Also acceptable: darkfield (good for motility) "
     "or DIC (Nomarski). Brightfield shows live cells with poor contrast."),
    ("Name the three domains of life and give one example organism for each.",
     "Bacteria: Escherichia coli (Gram-negative rod). "
     "Archaea: Methanobacterium (methanogen). "
     "Eukarya: Saccharomyces cerevisiae (baker's yeast - fungi)."),
]

for i, (q, a) in enumerate(qs, 1):
    story.append(Paragraph(f"Q{i}. {q}", ParagraphStyle('QQ', fontName='Helvetica-Bold', fontSize=9, spaceAfter=2, leading=13)))
    story.append(Paragraph(f"Answer: {a}", ParagraphStyle('AA', fontName='Helvetica', fontSize=9, spaceAfter=6, leading=13, leftIndent=14, textColor=colors.HexColor('#00008b'))))

story.append(sp(4))
story.append(Paragraph(
    "Sources: BIO203A Lab 1 Microscopy docx (Popa); Popa Ch.2 lecture slides (33 slides); "
    "Popa Ch.1 lecture slides (29 slides); OpenStax Microbiology (2016) Ch.1-2. Version 2.",
    cit))

doc.build(story)
print("Done ->", OUTPUT)
