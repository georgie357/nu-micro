# BIO203A Lab 1: Microscopy - Filled Report (Version 4 - Lecture Slides Only)
# V4: All content tied to Popa Ch.2 slides and Lab 1 docx. No textbook-only additions.

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\chapter 1 and 2\BIO203A_Lab1_Filled_v4.pdf"

h1  = ParagraphStyle('H1', fontName='Helvetica-Bold',   fontSize=15, spaceAfter=5,  textColor=colors.HexColor('#1a1a6e'))
h2  = ParagraphStyle('H2', fontName='Helvetica-Bold',   fontSize=12, spaceAfter=4,  spaceBefore=8, textColor=colors.HexColor('#1a1a6e'))
h3  = ParagraphStyle('H3', fontName='Helvetica-Bold',   fontSize=10, spaceAfter=3,  spaceBefore=5)
bod = ParagraphStyle('BD', fontName='Helvetica',         fontSize=9,  spaceAfter=3,  leading=13)
bul = ParagraphStyle('BL', fontName='Helvetica',         fontSize=9,  spaceAfter=2,  leading=12, leftIndent=14, firstLineIndent=-10)
ans = ParagraphStyle('AN', fontName='Helvetica-Bold',    fontSize=9,  spaceAfter=3,  leading=13, textColor=colors.HexColor('#00008b'))
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
    Paragraph("Lab 1: Microscopy — Filled Report (Version 4 — Lecture Slides Only)",
              ParagraphStyle('TS', fontName='Helvetica-Bold', fontSize=13, alignment=TA_CENTER)),
    sp(3),
    Paragraph("Based on: Lab 1 docx (Popa) + Ch.2 lecture slides | Textbook-only topics excluded",
              ParagraphStyle('TC', fontName='Helvetica-Oblique', fontSize=9, alignment=TA_CENTER, textColor=colors.grey)),
    HRFlowable(width=W, thickness=2, color=colors.HexColor('#1a1a6e')),
    sp(8),
]

# Objectives
story.append(Paragraph("Objectives", h2))
for obj in [
    "Demonstrate correct use of a compound light microscope",
    "Explain magnification, resolution, and field of view (FOV)",
    "Name all parts of a compound light microscope and state each part's function",
    "Observe microscopic characteristics of major groups of microorganisms",
]:
    story.append(Paragraph(f"• {obj}", bul))
story.append(sp())

# Background
story.append(Paragraph("Background (Key Facts)", h2))
story.append(HY("These numbers are tested: bacterium ~1 µm, visible threshold ~100 µm, LM resolution ~200 nm, immersion oil RI ~1.515."))
story.append(Paragraph(
    "Microbiology depends on microscopy because most microbes are too small to see unaided. "
    "A typical bacterium is ~1 µm; the unaided eye requires ~100 µm to detect an object. "
    "Compound light microscope: 40× to 1000× total magnification (with oil); resolution ~200 nm. "
    "Resolution improved by: shorter wavelength, higher numerical aperture (NA). "
    "Immersion oil (RI ~1.515 = RI of glass) used at 100× to prevent refraction and maximize resolution.",
    bod))
story.append(sp())

# Parts of microscope
story.append(Paragraph("Parts of the Compound Microscope (Popa Ch.2 slides 8-10)", h2))
story.append(tbl([
    ["Part", "Function", "Exam tip"],
    ["Base", "Supports the entire microscope", "Always carry: one hand on arm, one under base"],
    ["Stage", "Holds slide; mechanical stage = X-Y movement", ""],
    ["Condenser", "Focuses light onto specimen", "RAISE condenser at high magnification to maximize light/NA"],
    ["Iris diaphragm", "Controls amount of light entering condenser", "Adjust for CONTRAST — more closed = more contrast but less bright"],
    ["Ocular lens (eyepiece)", "10× magnification; you look through this", "Total mag = ocular × objective"],
    ["Objective lenses (turret)", "4× scanning, 10× low power, 40× high-dry, 100× oil immersion", "Each step up = 2.5× more magnification"],
    ["Coarse adjustment knob", "Large knob; rough focus", "Use ONLY with 4× and 10× — NEVER with 40× or 100×"],
    ["Fine adjustment knob", "Small knob; precise focus", "Required for 40× and 100×; always use after switching objectives"],
    ["Parfocal lenses", "Once focused at one mag, only minor fine adjustment needed when switching objectives", "Popa slide 9 — this concept is tested"],
], [1.4*inch, 2.8*inch, 2.8*inch]))
story.append(sp())

# Magnification and FOV
story.append(Paragraph("Magnification and Field of View (FOV)", h2))
story.append(HY("As magnification increases: FOV decreases. Working distance decreases. Depth of field decreases. Never use coarse focus at 40× or 100×."))
story.append(Paragraph(B("Total magnification = ocular lens mag × objective lens mag"), bod))
story.append(tbl([
    ["Objective", "Obj. Mag.", "Ocular (10×)", "Total Mag.", "Approx. FOV diameter", "Coarse focus OK?", "Exam trap"],
    ["Scanning",      "4×",   "10×", "40×",   "~4.5 mm",  "Yes", ""],
    ["Low power",     "10×",  "10×", "100×",  "~1.8 mm",  "Yes", ""],
    ["High-dry",      "40×",  "10×", "400×",  "~450 µm",  "NO — fine only", "Crashing risk — never coarse"],
    ["Oil immersion", "100×", "10×", "1000×", "~180 µm",  "NO — fine only", "Must apply oil; clean lens with lens paper after"],
], [1.1*inch, 0.65*inch, 0.65*inch, 0.65*inch, 1.2*inch, 1.05*inch, 1.7*inch]))
story.append(Paragraph("As magnification increases: FOV decreases, working distance decreases, depth of field decreases, image brightness decreases.", bod))
story.append(sp())

# Resolution
story.append(Paragraph("Resolution", h2))
story.append(Paragraph(
    "Resolution = ability to distinguish two adjacent points as separate. "
    "Shorter wavelength = better resolution (explains why EM is better than LM). "
    "Human eye ~200 µm; compound LM ~200 nm; TEM ~2.5 nm. "
    "Immersion oil (RI ~1.515 = glass RI) prevents refraction at 100× objective — maximizes NA and resolution.",
    bod))
story.append(sp())

# Organisms observed
story.append(Paragraph("Report: Organisms Observed", h2))
story.append(tbl([
    ["Slide", "Organism", "Taxonomic group\n(Ch.1)", "Objective\n(Total mag.)", "Observations"],
    ["1", "Paramecium caudatum",
     "Protozoa (Protist)\nDomain: Eukarya\nUnicellular, eukaryote",
     "10× obj.\n(100× total)",
     "Slipper-shaped; cilia visible around periphery for locomotion and feeding; large macronucleus visible; contractile vacuoles; ~150-300 µm — large enough to see at low power"],
    ["2", "Saccharomyces cerevisiae\n(baker's yeast)",
     "Fungi\nDomain: Eukarya\nUnicellular (yeast form)",
     "40× obj.\n(400× total)",
     "Oval to spherical; budding (asexual reproduction) visible; defined cell wall (chitin); ~5-10 µm; small clusters during budding"],
    ["3", "Bacillus subtilis",
     "Bacteria\nDomain: Bacteria\nGram+, rod-shaped",
     "100× obj.\n(1000×, oil immersion)",
     "Rod-shaped (bacillus morphology); chains; peptidoglycan G+ wall; endospores visible as refractile bodies in older cultures; ~0.5-1 µm wide x 2-4 µm long"],
], [0.45*inch, 1.2*inch, 1.45*inch, 0.85*inch, 3.05*inch]))
story.append(sp())

# Discussion questions
story.append(Paragraph("Report Questions — Answered", h2))

story.append(Paragraph("Q1. Which objective is closest to the slide when in focus?", h3))
story.append(Paragraph(
    "The 100× (oil immersion) objective — shortest working distance (~0.1–0.2 mm). "
    "This is why you must NEVER use the coarse focus at 40× or 100× — "
    "risk of crashing objective into the slide, destroying both the lens and the slide.",
    ans))
story.append(sp())

story.append(Paragraph("Q2. Correct procedure to put the microscope away.", h3))
story.append(Paragraph(
    "1. Remove slide from stage.<br/>"
    "2. Clean ALL oil from the 100× objective with lens paper ONLY (never Kleenex or paper towels).<br/>"
    "3. Clean stage if oil is present.<br/>"
    "4. Rotate nosepiece to scanning (4×) objective — lowest power, pointing down.<br/>"
    "5. Lower stage as far from objectives as possible using coarse focus knob.<br/>"
    "6. Wrap power cord loosely — do NOT wrap around the stage.<br/>"
    "7. Carry with TWO hands (one on arm, one under base) to storage cabinet.<br/>"
    "8. Store with arm pointing outward.",
    ans))
story.append(sp())

story.append(Paragraph(
    "Q3. FOV and cell estimation: 40× objective (400× total mag), FOV ~450 µm.", h3))
story.append(Paragraph(
    "FOV at 400× total = ~450 µm (0.45 mm). Formula: higher mag → smaller FOV proportionally "
    "(FOV at 100× = ~1.8 mm; at 400× = 1.8 mm / 4 = 0.45 mm = 450 µm).",
    ans))
story.append(Paragraph("Bacillus cells (2 µm): 450 µm ÷ 2 µm = 225 cells across FOV.", ans))
story.append(Paragraph("Yeast cells (10 µm): 450 µm ÷ 10 µm = 45 cells across FOV.", ans))
story.append(sp())

story.append(Paragraph("Q4. How to adjust to use minimum light?", h3))
story.append(Paragraph(
    "Close the iris diaphragm — reduces the cone of light entering the condenser and objective. "
    "Useful for improving contrast with low-magnification or unstained specimens.",
    ans))
story.append(sp())

story.append(Paragraph("Q5. Why only slight focus adjustment when switching objectives?", h3))
story.append(Paragraph(
    "Objectives are parfocal — designed so that when the specimen is in focus at one objective, "
    "switching to another objective places it at approximately the same focal distance. "
    "Only minor fine-focus adjustment needed after switching.",
    ans))
story.append(sp())

story.append(Paragraph("Q6. Three ways to increase light at higher magnification:", h3))
story.append(Paragraph(
    "1. Open the iris diaphragm wider.<br/>"
    "2. Raise the condenser closer to the slide.<br/>"
    "3. Increase lamp voltage/brightness using the illuminator control.<br/>"
    "At 100× (oil immersion): immersion oil also increases light entering objective by preventing refraction.",
    ans))
story.append(sp())

# Chapter connections
story.append(Paragraph("Lecture Connections — Lab Observations Tied to Ch.1 &amp; Ch.2", h2))
story.append(tbl([
    ["Lab observation", "Ch.1 lecture connection (classification)", "Ch.2 lecture connection (microscopy)"],
    ["Paramecium\n(protozoa)",
     "Domain Eukarya; Protist; unicellular; cilia motility; some protozoa = major pathogens (Giardia, Plasmodium, Trichomonas); absorb/ingest organics; NO cell wall",
     "Best viewed at 100–400×; cilia visible with phase-contrast; ~150-300 µm makes it visible at low power; live specimen = wet mount or phase-contrast"],
    ["Yeast\n(Saccharomyces)",
     "Domain Eukarya; Fungi; unicellular yeast form; CHITIN cell wall (NOT peptidoglycan); heterotrophic; Candida (related genus) is pathogenic; used in biotechnology",
     "Best at 40× (400×); budding visible; simple stain with methylene blue useful; ~5-10 µm requires 40× to resolve detail"],
    ["Bacillus subtilis\n(rod bacteria)",
     "Domain Bacteria; prokaryote; peptidoglycan cell wall (GRAM+); binary fission; rod = bacillus morphology; endospore-forming genus; Bacillus anthracis (anthrax) = Koch's first postulate proof organism",
     "MUST use 100× oil immersion (~1-4 µm too small otherwise); Gram stain = G+ purple (thick peptidoglycan); endospore stain: spores GREEN (malachite green), vegetative cells PINK (safranin)"],
    ["Immersion oil\nuse at 100×",
     "N/A",
     "RI of oil ~1.515 = RI of glass; prevents light refraction at 100× objective; increases NA; improves resolution; clean only with lens paper after use"],
    ["Size estimation\nfrom FOV",
     "Virus ~100 nm, bacterium ~1 µm, eukaryotic cell ~10-100 µm (Ch.1 slide 3)",
     "FOV diameter ÷ number of cells visible = estimated cell size; ocular micrometer gives precise measurement"],
], [1.3*inch, 2.6*inch, 3.1*inch]))
story.append(sp())

story.append(Paragraph(
    "Sources: BIO203A Lab 1 Microscopy docx (Popa); Popa Ch.2 lecture slides; "
    "Popa Ch.1 lecture slides. Version 4 — lecture-slide content only.", cit))

doc.build(story)
print("Done -> " + OUTPUT)

