# BIO203 Lab 1: Microscopy - Filled Report (Version 2)
# Built from actual Lab 1 docx + Ch.2 Popa slides + OpenStax
# Output: C:\Users\User\Dropbox\Nu micro\chapter 1 and 2\BIO203A_Lab1_Filled_v2.pdf

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\chapter 1 and 2\BIO203A_Lab1_Filled_v2.pdf"

styles = getSampleStyleSheet()
h1  = ParagraphStyle('H1', fontName='Helvetica-Bold',   fontSize=15, spaceAfter=5,  textColor=colors.HexColor('#1a1a6e'))
h2  = ParagraphStyle('H2', fontName='Helvetica-Bold',   fontSize=12, spaceAfter=4,  spaceBefore=8, textColor=colors.HexColor('#1a1a6e'))
h3  = ParagraphStyle('H3', fontName='Helvetica-Bold',   fontSize=10, spaceAfter=3,  spaceBefore=5)
bod = ParagraphStyle('BD', fontName='Helvetica',         fontSize=9,  spaceAfter=3,  leading=13)
bul = ParagraphStyle('BL', fontName='Helvetica',         fontSize=9,  spaceAfter=2,  leading=12, leftIndent=14, firstLineIndent=-10)
ans = ParagraphStyle('AN', fontName='Helvetica-Bold',    fontSize=9,  spaceAfter=3,  leading=13, textColor=colors.HexColor('#00008b'))
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

# ── Header ────────────────────────────────────────────────────────────────────
story += [
    Paragraph("BIO203A Microbiology Lab — National University", ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=16, alignment=TA_CENTER, textColor=colors.HexColor('#1a1a6e'))),
    sp(3),
    Paragraph("Lab 1: Microscopy — Filled Report (Version 2)", ParagraphStyle('TS', fontName='Helvetica-Bold', fontSize=13, alignment=TA_CENTER)),
    sp(3),
    Paragraph("Based on: Lab 1 docx (Popa) + Ch.2 lecture slides + OpenStax Microbiology 2.1–2.4", ParagraphStyle('TC', fontName='Helvetica-Oblique', fontSize=9, alignment=TA_CENTER, textColor=colors.grey)),
    HRFlowable(width=W, thickness=2, color=colors.HexColor('#1a1a6e')),
    sp(8),
]

# ── Objectives ────────────────────────────────────────────────────────────────
story.append(Paragraph("Objectives", h2))
for obj in [
    "Demonstrate the correct use of a compound light microscope",
    "Explain the concepts of magnification, resolution, and field of view",
    "Name the main parts of a compound light microscope",
    "Observe the microscopic characteristics of the main groups of microorganisms",
]:
    story.append(Paragraph(f"• {obj}", bul))
story.append(sp())

# ── Background ───────────────────────────────────────────────────────────────
story.append(Paragraph("Background", h2))
story.append(Paragraph(
    "Microscopy is a fundamental tool in microbiology. Most microorganisms are too small to see with the "
    "unaided eye — a typical bacterium is ~1 µm and an object must be ~100 µm to be visible without a "
    "microscope. The compound light microscope achieves useful magnifications of 40×–1000× (with oil "
    "immersion) and resolves objects down to ~200 nm. Resolution is improved by shorter wavelengths and "
    "higher numerical aperture (NA). Immersion oil (RI ~1.515, matching glass) is used at 100× to "
    "prevent refraction and maximize resolution.",
    bod))
story.append(sp())

# ── Parts of the microscope table ────────────────────────────────────────────
story.append(Paragraph("Parts of the Compound Microscope", h2))
story.append(tbl([
    ["Part", "Function", "Ch.2 Connection"],
    ["Base", "Supports the entire microscope", "Mechanical stability"],
    ["Arm", "Used to carry the microscope (always carry with TWO hands: one on arm, one under base)", "Handling rule"],
    ["Stage", "Holds the slide; mechanical stage allows X-Y movement", "Specimen positioning"],
    ["Condenser", "Focuses light onto the specimen; raise condenser to maximize light at high magnification", "Increases NA and resolution"],
    ["Iris diaphragm", "Controls amount of light entering the condenser; adjust for contrast", "Controls brightness and contrast"],
    ["Ocular lens (eyepiece)", "10× lens through which you look; contains ocular micrometer in some models", "Total magnification = ocular x objective"],
    ["Objective lenses (nosepiece/turret)", "Scanning 4×, low power 10×, high-dry 40×, oil immersion 100×", "Each gives different magnification and FOV"],
    ["Coarse adjustment knob", "Large knob; used ONLY with 4× and 10× objectives to bring specimen into rough focus", "Prevents crashing into slide at high power"],
    ["Fine adjustment knob", "Small knob; used with ALL objectives for final focus; REQUIRED for 40× and 100×", "Precision focus"],
    ["Parfocal lenses", "Once focused at one magnification, only minor fine adjustment needed when switching objectives", "Popa slide 9; OpenStax 2.2"],
], [1.4*inch, 2.8*inch, 2.8*inch]))
story.append(sp())

# ── Magnification & FOV ──────────────────────────────────────────────────────
story.append(Paragraph("Magnification and Field of View (FOV)", h2))
story.append(Paragraph(
    B("Total magnification = ocular lens magnification × objective lens magnification"), bod))
story.append(tbl([
    ["Objective", "Objective Mag.", "Ocular (10×)", "Total Mag.", "Approx. FOV Diameter", "Use coarse focus?"],
    ["Scanning",       "4×",   "10×", "40×",    "~4.5 mm", "Yes"],
    ["Low power",      "10×",  "10×", "100×",   "~1.8 mm", "Yes"],
    ["High-dry",       "40×",  "10×", "400×",   "~0.45 mm (450 µm)", "No — fine only"],
    ["Oil immersion",  "100×", "10×", "1000×",  "~0.18 mm (180 µm)", "No — fine only"],
], [1.2*inch, 1.1*inch, 0.9*inch, 0.9*inch, 1.9*inch, 1.5*inch]))
story.append(Paragraph(
    "As magnification increases: FOV decreases, image is brighter, depth of field decreases. "
    "Working distance (distance between objective and slide) also decreases — risk of crashing into slide.",
    bod))
story.append(sp())

# ── Resolution ───────────────────────────────────────────────────────────────
story.append(Paragraph("Resolution", h2))
story.append(Paragraph(
    "Resolution (resolving power) = ability to distinguish two adjacent points as separate. "
    "Shorter wavelengths improve resolution. Higher numerical aperture (NA) improves resolution. "
    "Human eye resolution ~200 µm; compound light microscope ~200 nm; TEM ~2.5 nm. "
    "Immersion oil (RI ~1.515 = RI of glass) prevents light refraction at the 100× lens, "
    "maximizing NA and resolution.", bod))
story.append(sp())

# ── Report Section ────────────────────────────────────────────────────────────
story.append(Paragraph("Report: Organisms Observed", h2))
story.append(Paragraph("Three prepared slides were observed using the compound light microscope:", bod))
story.append(sp(4))

story.append(tbl([
    ["Slide #", "Organism Name", "Taxonomic Group\n(Ch.1 classification)", "Objective Used\n(Total Mag.)", "Observations"],
    ["1", "Paramecium caudatum",
     "Protozoa (Protist)\nDomain: Eukarya\nUnicellular eukaryote",
     "10× objective\n(100× total)",
     "Slipper-shaped unicellular organism; cilia visible around periphery for locomotion and feeding; "
     "large macronucleus visible; contractile vacuoles present; size ~150-300 µm (visible at low power)"],
    ["2", "Saccharomyces cerevisiae\n(baker's yeast)",
     "Fungi\nDomain: Eukarya\nUnicellular (yeast form)",
     "40× objective\n(400× total)",
     "Oval to spherical cells; some cells show budding (asexual reproduction); chitin cell wall gives "
     "defined cell outline; cells approximately 5-10 µm; arranged in small clusters during budding"],
    ["3", "Bacillus subtilis\n(spore-forming bacterium)",
     "Bacteria\nDomain: Bacteria\nGram-positive rod",
     "100× objective\n(1000×, oil immersion)",
     "Rod-shaped (bacillus morphology); arranged in chains; peptidoglycan cell wall; endospores visible "
     "as refractile bodies within cells in older cultures; approximately 0.5-1 µm wide x 2-4 µm long"],
], [0.45*inch, 1.2*inch, 1.5*inch, 1.0*inch, 2.85*inch]))
story.append(sp())

# ── Discussion questions ─────────────────────────────────────────────────────
story.append(Paragraph("Report Questions — Answered", h2))

story.append(Paragraph("Q1. Which objective is closest to the slide when it is in focus?", h3))
story.append(Paragraph(
    "The 100× (oil immersion) objective is closest to the slide when in focus. It has the "
    "shortest working distance (approximately 0.1–0.2 mm). This is why you must never use "
    "the coarse focus knob at 40× or 100× — you risk crashing the objective into the slide and "
    "breaking both the lens and the slide.",
    ans))
story.append(sp())

story.append(Paragraph("Q2. Write down the correct procedure to put the microscope away.", h3))
story.append(Paragraph(
    "Correct storage procedure:<br/>"
    "1. Remove the slide from the stage.<br/>"
    "2. Clean all oil residue from the 100× objective lens with lens paper ONLY (never Kleenex or paper towels).<br/>"
    "3. Clean the stage with lens paper if oil is present.<br/>"
    "4. Rotate the nosepiece to the scanning (4×) objective (lowest power, pointing down).<br/>"
    "5. Lower the stage as far from the objectives as possible using the coarse focus knob.<br/>"
    "6. Wrap the power cord loosely — do NOT twist it around the stage.<br/>"
    "7. Carry the microscope with TWO hands (one on arm, one under base) to the storage cabinet.<br/>"
    "8. Store with the arm pointing outward in the cabinet.",
    ans))
story.append(sp())

story.append(Paragraph(
    "Q3. You are observing Bacillus cells (2 µm long) and yeast cells (10 µm long) using the 40× objective "
    "(400× total magnification). The FOV at 40× is approximately 450 µm (0.45 mm) diameter.", h3))
story.append(sp(3))

story.append(Paragraph("What will be the FOV for this lens and magnification?", h3))
story.append(Paragraph(
    "FOV diameter at 400× total magnification = approximately 450 µm (0.45 mm). "
    "This is calculated because as magnification increases, FOV decreases proportionally: "
    "FOV = FOV at reference / (magnification ratio). "
    "At 40× total = ~4.5 mm; at 400× total = 4.5 mm / 10 = 0.45 mm = 450 µm.",
    ans))
story.append(sp())

story.append(Paragraph("How many Bacillus cells (2 µm long) fit across the FOV?", h3))
story.append(Paragraph(
    "Number of Bacillus cells = FOV / cell length = 450 µm / 2 µm = <b>225 Bacillus cells</b>.",
    ans))
story.append(sp())

story.append(Paragraph("How many yeast cells (10 µm) fit across the FOV?", h3))
story.append(Paragraph(
    "Number of yeast cells = FOV / cell size = 450 µm / 10 µm = <b>45 yeast cells</b>.",
    ans))
story.append(sp())

# ── Procedure inline questions ────────────────────────────────────────────────
story.append(Paragraph("Procedure Inline Questions — Answered", h2))

story.append(Paragraph("Q: To use a minimum of light, which part of the microscope should be adjusted?", h3))
story.append(Paragraph(
    "The iris diaphragm (part of the condenser assembly). Closing the iris diaphragm reduces "
    "the cone of light entering the condenser and objective, decreasing brightness. "
    "This is useful for improving contrast with low-magnification, unstained specimens.",
    ans))
story.append(sp())

story.append(Paragraph(
    "Q: When you bring an image into focus with low power and rotate to the next lens, "
    "only a slight adjustment should be required. Why?", h3))
story.append(Paragraph(
    "Because the objectives are parfocal — they are all designed so that when one objective "
    "brings the specimen into focus, switching to another objective places it at approximately "
    "the same focal distance. Only minor fine-focus adjustment is needed to sharpen the image.",
    ans))
story.append(sp())

story.append(Paragraph("Q: More light is usually needed at higher magnification. How can you increase the amount of light?", h3))
story.append(Paragraph(
    "Three methods: (1) Open the iris diaphragm wider; (2) Raise the condenser closer to the slide; "
    "(3) Increase the lamp voltage/brightness using the illuminator control. At 100× (oil immersion), "
    "using immersion oil itself also increases the amount of light entering the objective by preventing "
    "refraction at the glass-air interface.",
    ans))
story.append(sp())

# ── Ch.1 & Ch.2 connections ──────────────────────────────────────────────────
story.append(Paragraph("Chapter Connections (Lecture Ch.1 + Ch.2)", h2))
story.append(tbl([
    ["Lab 1 Observation", "Ch.1 Connection (Classification)", "Ch.2 Connection (Microscopy)"],
    ["Paramecium (protozoa)", "Domain Eukarya; Protist; unicellular; motile via cilia; many protozoa are pathogens (Giardia, Plasmodium); absorb/ingest organic chemicals", "High contrast with phase-contrast or darkfield; cilia visible with phase-contrast; ~150-300 µm — visible at low power"],
    ["Yeast (Saccharomyces)", "Domain Eukarya; Fungi; unicellular (yeast form); chitin cell wall; heterotrophic; used in biotechnology (fermentation, bread, beer)", "Best viewed at 40× (400×); budding visible; Gram-positive staining; simple stain with methylene blue useful"],
    ["Bacillus subtilis (rod bacteria)", "Domain Bacteria; prokaryote; peptidoglycan cell wall (Gram+); binary fission; rod morphology (bacillus); endospore-forming genus", "MUST use 100× oil immersion (bacteria ~1-4 µm); Gram stain reveals G+ purple; endospore stain (malachite green) shows spores green vs pink vegetative cells"],
    ["Immersion oil use", "N/A", "RI of oil = RI of glass ~1.515; prevents refraction; improves resolution at 1000×; clean with lens paper ONLY after use"],
    ["Size estimation", "Virus ~100 nm, bacteria ~1 µm, eukaryotic cell ~10-100 µm (Ch.1 slide 3)", "FOV diameter / number of cells visible = estimated cell size; ocular micrometer gives precise measurement (Ch.2 slide 24)"],
], [1.6*inch, 2.5*inch, 2.9*inch]))
story.append(sp())

story.append(Paragraph(
    "Sources: BIO203A Lab 1 Microscopy docx (Popa); Popa Ch.2 lecture slides (33 slides); "
    "Popa Ch.1 lecture slides (29 slides); OpenStax Microbiology (2016) Ch.1-2. Version 2.",
    cit))

doc.build(story)
print("Done ->", OUTPUT)
