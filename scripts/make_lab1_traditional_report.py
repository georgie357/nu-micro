# BIO203A Lab 1: Microscopy — Traditional 8-Section Lab Report (Popa format, May 2026)
# Author: George Vela
# References cite ONLY OpenStax Microbiology + Tiny Earth manual + Popa lecture slides
# (Per the Popa requirement — no outside web/AI sources.)

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, HRFlowable, Image)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\lab reports\BIO203A_Lab1_Traditional_Report.pdf"
DRAWING_PATH = r"C:\Users\User\Dropbox\Nu micro\lab1_drawing.png"
FIELD_SKETCH_PATH = r"C:\Users\User\Dropbox\Nu micro\lab reports\lab 1 image.png"

# Styles
title_style = ParagraphStyle('Title', fontName='Helvetica-Bold', fontSize=18,
                              alignment=TA_CENTER, textColor=colors.HexColor('#1a1a6e'),
                              spaceAfter=6)
subtitle = ParagraphStyle('Sub', fontName='Helvetica', fontSize=11, alignment=TA_CENTER,
                           textColor=colors.grey, spaceAfter=4)
section = ParagraphStyle('Sec', fontName='Helvetica-Bold', fontSize=14,
                          textColor=colors.HexColor('#1a1a6e'),
                          spaceBefore=14, spaceAfter=6)
sub = ParagraphStyle('Sub2', fontName='Helvetica-Bold', fontSize=11,
                      spaceBefore=8, spaceAfter=4)
body = ParagraphStyle('Body', fontName='Helvetica', fontSize=10, leading=14,
                       alignment=TA_JUSTIFY, spaceAfter=6)
bullet = ParagraphStyle('Bullet', fontName='Helvetica', fontSize=10, leading=14,
                         leftIndent=14, firstLineIndent=-10, spaceAfter=3)
caption = ParagraphStyle('Cap', fontName='Helvetica-Oblique', fontSize=9,
                          alignment=TA_CENTER, textColor=colors.grey, spaceAfter=8)

cell_body = ParagraphStyle('cb', fontName='Helvetica', fontSize=9, leading=12, spaceAfter=0)
cell_bold = ParagraphStyle('cB', fontName='Helvetica-Bold', fontSize=9, leading=12, spaceAfter=0)


def _cell(val, hdr=False):
    if isinstance(val, str):
        return Paragraph(val.replace('\n', '<br/>'), cell_bold if hdr else cell_body)
    return val


def tbl(data, widths):
    wrapped = [[_cell(c, hdr=(i == 0)) for c in row] for i, row in enumerate(data)]
    t = Table(wrapped, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.82, 0.82, 0.82)),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.Color(0.95, 0.95, 0.95)]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t


def B(t): return f"<b>{t}</b>"
def I(t): return f"<i>{t}</i>"
def sp(n=6): return Spacer(1, n)


doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                        leftMargin=0.85 * inch, rightMargin=0.85 * inch,
                        topMargin=0.75 * inch, bottomMargin=0.75 * inch)
W = 6.8 * inch
story = []

# ════════════════════════════════════════════════════════════════════════════
# 1. TITLE
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Lab 1: Microscopy", title_style))
story.append(HRFlowable(width=W, thickness=1.5, color=colors.HexColor('#1a1a6e')))
story.append(sp(8))

# ════════════════════════════════════════════════════════════════════════════
# 2. NAME
# ════════════════════════════════════════════════════════════════════════════
story.append(tbl([
    ['Student', 'George Vela'],
    ['Course', 'BIO203A Microbiology Laboratory'],
    ['Term', 'Spring 2026 (April 27 – June 20, 2026)'],
    ['Instructor', 'Dr. Radu Popa'],
    ['Institution', 'National University, Los Angeles Campus'],
    ['Lab Date', 'Tuesday, April 28, 2026'],
    ['Report Submitted', 'May 2026'],
], [1.7 * inch, 5.1 * inch]))
story.append(sp(10))

# ════════════════════════════════════════════════════════════════════════════
# 3. SCOPE
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Scope", section))
story.append(Paragraph(
    f"This laboratory exercise introduced the use of the compound brightfield light microscope "
    f"and applied it to the observation of a prepared blood-smear slide containing "
    f"{I('Trypanosoma')} trypomastigotes alongside host red blood cells. The investigation focused on "
    f"the operation of the microscope at increasing magnifications, the relationships between "
    f"magnification, field of view, and resolution, and the recognition of distinguishing "
    f"morphological features of a flagellated protozoan parasite.", body))

# ════════════════════════════════════════════════════════════════════════════
# 4. INTRODUCTION
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Introduction", section))
story.append(Paragraph(
    f"Microbiology is the study of organisms too small to be seen with the unaided eye, and the "
    f"compound light microscope is its foundational instrument (Popa BIO203 Lecture, Ch.2, slides 1–3). "
    f"The compound microscope uses two lens systems — an ocular eyepiece (typically 10×) and a "
    f"rotating set of objective lenses (4×, 10×, 40×, and 100× oil immersion) — to magnify a "
    f"specimen through a calculated combination of the two values. Total magnification equals "
    f"the ocular magnification multiplied by the objective magnification (OpenStax Microbiology, §2.3).", body))
story.append(Paragraph(
    f"Two further optical concepts govern useful microscopy. {B('Resolution')}, or resolving power, "
    f"is the ability to distinguish two adjacent points as separate objects; it improves with shorter "
    f"wavelengths of light and higher numerical aperture, which is why immersion oil is used at the "
    f"100× objective to prevent refraction at the glass-air interface (OpenStax Microbiology, §2.1). "
    f"{B('Parfocality')} is the property by which a specimen remains in approximate focus when the "
    f"objective is changed, requiring only fine-adjustment correction (Popa BIO203 Lecture, Ch.2, slide 9). "
    f"{B('Field of view (FOV)')} is the visible diameter at the specimen plane and is calculated as "
    f"the field number of the ocular divided by the total magnification.", body))
story.append(Paragraph(
    f"The specimen examined in this lab — {I('Trypanosoma')} sp. — is a unicellular flagellated "
    f"protozoan and a representative member of the supergroup Excavata "
    f"(Popa BIO203 Lecture, Ch.5, slide 6). Members of this genus are obligate parasites of "
    f"vertebrate blood and tissue and are responsible for African sleeping sickness "
    f"({I('T. brucei')}) and Chagas disease ({I('T. cruzi')}). The diagnostic morphology of the "
    f"trypomastigote stage is its slender, curved cell body bearing a single nucleus, a "
    f"prominent {B('kinetoplast')} (a DNA-containing region adjacent to the basal body of the "
    f"flagellum), and an undulating membrane formed where the flagellum runs along the length of "
    f"the cell before extending freely from the anterior end (OpenStax Microbiology, §1.3 and §5.1).", body))

# ════════════════════════════════════════════════════════════════════════════
# 5. MATERIALS AND METHODS
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Materials and Methods", section))
story.append(Paragraph(B("Materials:"), sub))
story.append(Paragraph("• Compound binocular brightfield microscope (4×, 10×, 40×, 100× oil objectives; 10× oculars; field number 22 mm)", bullet))
story.append(Paragraph("• Pre-prepared, fixed and stained microscope slides (including a stained blood smear containing Trypanosoma sp. and red blood cells)", bullet))
story.append(Paragraph("• Type-A immersion oil", bullet))
story.append(Paragraph("• Lens paper", bullet))
story.append(Paragraph("• Permanent marker for slide identification", bullet))

story.append(Paragraph(B("Procedure:"), sub))
story.append(Paragraph(
    f"The microscope was carried to the bench using both hands — one supporting the base, one "
    f"grasping the arm — and the power cord was placed to the side rather than wrapped around "
    f"the stage. The 4× scanning objective was rotated into position and the stage was raised "
    f"to its lowest setting using the coarse-adjustment knob. The illuminator was switched on "
    f"and the iris diaphragm of the condenser was partially closed to increase contrast at low "
    f"magnification.", body))
story.append(Paragraph(
    f"The prepared slide was secured on the stage. Initial focus was achieved at 4×, and the "
    f"specimen was then centered in the field of view. The nosepiece was rotated to the 10× "
    f"objective, which required only minor refocusing using the fine-adjustment knob, "
    f"confirming the parfocal property of the lens system. The 40× high-dry objective was "
    f"engaged next and the iris diaphragm was opened wider to compensate for the smaller field "
    f"of view and reduced light. A general sketch of cell size and shape was recorded at this "
    f"magnification.", body))
story.append(Paragraph(
    f"For the highest-resolution observation, the 40× objective was rotated out of the optical "
    f"path. A single drop of immersion oil was placed directly on the area of the slide being "
    f"observed, and the 100× oil immersion objective was rotated into the oil. Fine focus was "
    f"adjusted carefully to bring the specimen into sharp resolution. Cell shape, internal "
    f"organelles, and identifying features were recorded by hand sketch.", body))
story.append(Paragraph(
    f"Upon completion, the slide was removed without rotating the stage downward against the "
    f"oil objective. The 100× lens was wiped clean with lens paper, the stage was cleaned of "
    f"residual oil, the nosepiece was returned to the 4× objective, the stage was lowered to "
    f"its furthest position from the lenses, and the microscope was returned to the storage "
    f"cabinet with the arm pointing outward.", body))

# ════════════════════════════════════════════════════════════════════════════
# 6. RESULTS AND DISCUSSION
# ════════════════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph("Results and Discussion", section))

story.append(Paragraph(B("Organism Observed:"), sub))
story.append(Paragraph(
    f"The blood smear contained two distinct cell types, both observed at the same field. "
    f"The dominant cells were biconcave, anucleate discs approximately 7–8 µm in diameter, "
    f"identified as host {B('red blood cells (erythrocytes)')}. Among the erythrocytes, slender "
    f"elongated cells with a clear central nucleus, a smaller darker stained granule (kinetoplast) "
    f"located adjacent to the nucleus, and a single long flagellum trailing from the anterior end "
    f"were identified as {B(I('Trypanosoma') + ' sp. trypomastigotes')} — flagellated protozoa "
    f"of the supergroup Excavata.", body))

story.append(Paragraph(B("Sketch of Specimens at Total Magnification 400× (40× objective × 10× ocular):"), sub))
if os.path.exists(DRAWING_PATH):
    img = Image(DRAWING_PATH, width=5.5 * inch, height=3.4 * inch)
    img.hAlign = 'CENTER'
    story.append(img)
    story.append(Paragraph(
        "Figure 1. Hand sketch of the prepared blood smear at 400× total magnification. "
        "Left: anucleate biconcave red blood cell. Right: <i>Trypanosoma</i> sp. trypomastigote "
        "with labeled nucleus (N) and kinetoplast (K) and a single anterior flagellum.", caption))
else:
    story.append(Paragraph("[lab1_drawing.png — clean labeled sketch of the observed smear]", caption))

if os.path.exists(FIELD_SKETCH_PATH):
    img2 = Image(FIELD_SKETCH_PATH, width=5.0 * inch, height=2.8 * inch)
    img2.hAlign = 'CENTER'
    story.append(sp(6))
    story.append(img2)
    story.append(Paragraph(
        "Figure 2. Field-notebook sketch made during the lab session. Center: a host cell containing "
        "a rosette of intracellular forms. Right: two free trypomastigote-shaped organisms with anterior "
        "flagella outside the host cell, consistent with the trypanosome life cycle.", caption))

story.append(Paragraph(B("Field of View (FOV) and Cell-Count Calculations:"), sub))
story.append(Paragraph(
    f"At the 40× objective with a field number (FN) of 22 mm and a 10× ocular, the field of "
    f"view is calculated as FN ÷ total magnification = 22 mm ÷ 400 = {B('0.055 mm')} = "
    f"{B('55 µm')}. Using this FOV:", body))
story.append(tbl([
    ['Cell type', 'Length (µm)', 'Cells across 55 µm FOV'],
    ['Bacillus (rod-shaped bacterium)', '2 µm', '55 ÷ 2 ≈ 27 cells'],
    ['Yeast (Saccharomyces)', '10 µm', '55 ÷ 10 ≈ 5.5 cells'],
], [2.4 * inch, 1.6 * inch, 2.6 * inch]))
story.append(sp(4))
story.append(Paragraph(
    f"This calculation illustrates the inverse relationship between magnification and field "
    f"of view: as magnification increases, the visible field shrinks and fewer cells fit "
    f"across it. The same relationship explains why locating a specimen begins at low power "
    f"(4× scanning, where the field is widest) before progressing to higher objectives.", body))

story.append(Paragraph(B("Procedure Question Responses:"), sub))
story.append(Paragraph(
    f"{B('Q1. Which objective is closest to the slide when in focus?')} The 100× oil immersion "
    f"objective has the shortest working distance (approximately 0.1–0.2 mm) and is therefore "
    f"closest to the slide when the specimen is in focus. For this reason the coarse adjustment "
    f"knob must never be used at 40× or 100× — the lens can crush into and damage both the "
    f"slide and the objective itself (OpenStax Microbiology, §2.3).", body))
story.append(Paragraph(
    f"{B('Q2. Correct procedure to put the microscope away:')} (1) remove the slide from the "
    f"stage; (2) clean all immersion oil from the 100× objective using lens paper only — "
    f"never tissue or paper towels, which scratch the lens; (3) clean any oil from the stage; "
    f"(4) rotate the nosepiece to the 4× scanning objective; (5) lower the stage to its "
    f"farthest position from the objectives using the coarse-adjustment knob; (6) leave the "
    f"power cord beside the microscope rather than wrapping it around the stage; (7) carry "
    f"the microscope with both hands — one under the base, one on the arm — to the storage "
    f"cabinet; (8) store with the arm pointing outward.", body))
story.append(Paragraph(
    f"{B('Q3. Step 7 — minimum light setting:')} the iris diaphragm of the condenser is "
    f"closed. This narrows the cone of light entering the condenser and increases contrast "
    f"on unstained or low-contrast specimens at low magnification.", body))
story.append(Paragraph(
    f"{B('Q4. Step 8a — only slight focus adjustment between objectives:')} the lens system "
    f"is parfocal — designed so that a specimen in focus at one objective remains in approximate "
    f"focus at the next, requiring only small fine-focus correction (Popa BIO203 Lecture, "
    f"Ch.2, slide 9).", body))
story.append(Paragraph(
    f"{B('Q5. Step 8b — increasing light at higher magnification:')} (1) open the iris "
    f"diaphragm wider to admit more light; (2) raise the condenser closer to the slide to "
    f"concentrate light onto the specimen; (3) increase lamp brightness on the illuminator. "
    f"At 100× immersion oil itself increases light delivery by eliminating refraction at the "
    f"glass-air interface (OpenStax Microbiology, §2.1).", body))
story.append(Paragraph(
    f"{B('Q6. Step 10 — color, FOV, and cell density across magnifications:')} cell color did "
    f"not change with magnification because color is a property of the stain bound to the "
    f"specimen, not of the optical system. Field of view decreased substantially at each step "
    f"up in magnification, with proportionally fewer cells visible per field — the inverse "
    f"relationship described in the FOV calculation above.", body))

# ════════════════════════════════════════════════════════════════════════════
# 7. CONCLUSION
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Conclusion", section))
story.append(Paragraph(
    f"The objectives of Lab 1 were met. Correct handling and operation of the compound brightfield "
    f"microscope was demonstrated through the systematic progression from 4× scanning through "
    f"100× oil immersion observation. The mathematical relationships between ocular and objective "
    f"magnification, between magnification and field of view, and between resolution and "
    f"numerical aperture were applied to a practical cell-counting problem. The diagnostic "
    f"morphology of {I('Trypanosoma')} sp. trypomastigotes was identified directly under "
    f"the microscope, anchoring the lecture material on protozoa (Popa BIO203 Lecture, Ch.5) "
    f"to a real specimen.", body))
story.append(Paragraph(
    f"The skills practiced in this laboratory — slide handling, parfocal objective progression, "
    f"oil immersion technique, and recognition of microbial morphology — are directly applied "
    f"in subsequent labs of the {B('Antibiotic Discovery Project')}, where soil-isolated "
    f"colonies will be examined by Gram stain and simple stain (Lab 5) for morphological "
    f"identification before functional screening for antimicrobial activity "
    f"(Tiny Earth Lab Manual, Experiment 5).", body))

# ════════════════════════════════════════════════════════════════════════════
# 8. REFERENCES
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("References", section))
story.append(Paragraph(
    "1. OpenStax Microbiology. Chapter 1: An Invisible World. §1.3 — Types of Microorganisms. "
    "OpenStax College, 2024. (Free textbook, openstax.org/details/books/microbiology)", body))
story.append(Paragraph(
    "2. OpenStax Microbiology. Chapter 2: How We See the Invisible World. §2.1 — The Properties of Light; "
    "§2.3 — Instruments of Microscopy. OpenStax College, 2024.", body))
story.append(Paragraph(
    "3. OpenStax Microbiology. Chapter 5: The Eukaryotes of Microbiology. §5.1 — Unicellular Eukaryotic "
    "Parasites. OpenStax College, 2024.", body))
story.append(Paragraph(
    "4. Popa, R. BIO203 Microbiology Lecture, National University, Spring 2026. Chapter 2: Microscopy "
    "and Staining, slides 1–9 (parts of the microscope, magnification, parfocality).", body))
story.append(Paragraph(
    "5. Popa, R. BIO203 Microbiology Lecture, National University, Spring 2026. Chapter 5: The Eukaryotes "
    "of Microbiology, slide 6 (protozoa supergroups, Excavata, <i>Trypanosoma</i>).", body))
story.append(Paragraph(
    "6. Tiny Earth Lab Manual. Experiment 5: Isolate Unique Colonies to Test for Antibiotic Production. "
    "Tiny Earth Network, 2024.", body))

doc.build(story)
print(f"Done -> {OUTPUT}")
