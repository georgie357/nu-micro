# BIO203A M1 L1 — Lab 1 Microscopy — Filled Report
# Based on lab docx + Popa Ch.2 lecture slides

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

os.makedirs(r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2', exist_ok=True)
OUTPUT = r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2/BIO203A_M1_L1_Filled.pdf'

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.75*inch, bottomMargin=0.75*inch)

h1  = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=14, leading=17, spaceAfter=4,
                     alignment=TA_CENTER, borderPad=4, borderWidth=1, borderColor=colors.black,
                     backColor=colors.Color(0.92, 0.92, 0.92))
h2  = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11, leading=14, spaceAfter=3, spaceBefore=10)
h3  = ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceAfter=3, spaceBefore=6)
body = ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=3)
ans  = ParagraphStyle('ans', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=2,
                      leftIndent=10, borderPad=4, borderWidth=0.5, borderColor=colors.black,
                      backColor=colors.Color(0.96, 0.96, 0.96))
note = ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=8, leading=11, spaceAfter=3,
                      textColor=colors.Color(0.3, 0.3, 0.3))
tip  = ParagraphStyle('tip', fontName='Helvetica-Bold', fontSize=8.5, spaceAfter=4, leading=12,
                      backColor=colors.HexColor('#fff3cd'), borderPad=4,
                      borderWidth=0.5, borderColor=colors.HexColor('#cc8800'))

cell_body = ParagraphStyle('cb', fontName='Helvetica',      fontSize=8, leading=11, spaceAfter=0)
cell_bold = ParagraphStyle('cB', fontName='Helvetica-Bold', fontSize=8, leading=11, spaceAfter=0)

def _c(v, hdr=False):
    if isinstance(v, str):
        return Paragraph(v.replace('\n', '<br/>'), cell_bold if hdr else cell_body)
    return v

def tbl(data, widths, hdr=True):
    wrapped = [[_c(c, hdr=(hdr and i == 0)) for c in row] for i, row in enumerate(data)]
    t = Table(wrapped, colWidths=widths, repeatRows=1 if hdr else 0)
    t.setStyle(TableStyle([
        ('GRID',          (0,0), (-1,-1), 0.5, colors.black),
        ('BACKGROUND',    (0,0), (-1, 0), colors.Color(0.82, 0.82, 0.82)) if hdr else ('BACKGROUND', (0,0), (-1,0), colors.white),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [colors.white, colors.Color(0.95, 0.95, 0.95)]),
        ('TOPPADDING',    (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING',   (0,0), (-1,-1), 4),
        ('RIGHTPADDING',  (0,0), (-1,-1), 4),
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
    ]))
    return t

def sp(n=1): return Spacer(1, n * 0.1 * inch)
def hr():    return HRFlowable(width='100%', thickness=1, color=colors.black, spaceAfter=4)
def HY(text): return Paragraph(f'HIGHEST YIELD: {text}', tip)

story = []

# Title
story.append(Paragraph('BIO203A — Lab 1: Microscopy', h1))
story.append(Paragraph('Filled Report · Spring 2026 · Dr. Radu Popa', h2))
story.append(Paragraph(
    'Note: Diagrams/sketches and cell phone photos must be added from your own in-lab observations. '
    'All written answers below are based on lab activity + Popa Ch.2 lecture slides.',
    note))
story.append(sp(1))

# ── PART 1: ORGANISMS OBSERVED ───────────────────────────────────────────────
story.append(Paragraph('Part 1 — Organisms Observed', h2))
story.append(hr())
story.append(HY('Bacteria MUST use oil immersion (100×). Total mag = ocular × objective. FOV shrinks as mag increases.'))
story.append(tbl([
    ['Organism', 'Taxonomic Group', 'Domain', 'Best Objective\n(Total Mag)', 'Observations'],
    ['Paramecium caudatum',
     'Protozoa (Protist)\nUnicellular',
     'Eukarya',
     '10× obj.\n(100× total)',
     'Slipper-shaped cell; cilia visible around entire periphery for locomotion and feeding; '
     'large macronucleus visible; contractile vacuoles present; ~150–300 µm — large enough to '
     'see at low power. Live unstained specimen shows internal movement.'],
    ['Saccharomyces cerevisiae\n(baker\'s yeast)',
     'Fungi\nUnicellular (yeast form)',
     'Eukarya',
     '40× obj.\n(400× total)',
     'Oval to spherical cells; budding clearly visible (asexual reproduction); '
     'defined cell wall (chitin); ~5–10 µm; small clusters visible during budding. '
     'Stained with methylene blue — dead cells stain blue, live cells remain clear.'],
    ['Bacillus subtilis',
     'Bacteria\nGram-positive rod',
     'Bacteria',
     '100× obj.\n(1000× total)\nOIL IMMERSION',
     'Rod-shaped (bacillus morphology); cells appear in chains; Gram-positive (thick '
     'peptidoglycan wall). Endospores visible as refractile (bright, unstained) bodies '
     'within cells in older cultures. ~0.5–1 µm wide × 2–4 µm long. '
     'Oil immersion required — too small to resolve at lower magnification.'],
], [1.2*inch, 1.1*inch, 0.7*inch, 0.85*inch, 3.15*inch]))
story.append(Paragraph(
    'Sketches: Draw each organism in the circles provided on the original lab sheet from your actual observations.',
    note))
story.append(sp(2))

# ── PART 2: QUESTIONS ─────────────────────────────────────────────────────────
story.append(Paragraph('Part 2 — Report Questions', h2))
story.append(hr())

# Q1
story.append(Paragraph('Q1. Which objective is closest to the slide when it is in focus?', h3))
story.append(Paragraph(
    'The <b>100× oil immersion objective</b> is closest to the slide when in focus — it has the '
    'shortest working distance (~0.1–0.2 mm). This is why you must <b>NEVER use the coarse '
    'adjustment knob at 40× or 100×</b> — the objective can crash into and destroy the slide '
    'and the lens.',
    ans))
story.append(sp(1))

# Q2
story.append(Paragraph('Q2. Write down the correct procedure to put the microscope away.', h3))
story.append(Paragraph(
    '1. Remove the slide from the stage.<br/>'
    '2. Clean ALL immersion oil from the 100× objective with <b>lens paper ONLY</b> '
    '(never Kleenex or paper towels — they scratch the lens).<br/>'
    '3. Clean oil from the stage if present.<br/>'
    '4. Rotate the nosepiece to the <b>scanning (4×) objective</b> — lowest power, pointed down.<br/>'
    '5. Lower the stage as far from the objectives as possible using the coarse adjustment knob.<br/>'
    '6. Wrap the power cord loosely to the side — <b>do NOT wrap it around the stage.</b><br/>'
    '7. Carry with <b>TWO hands</b> — one on the arm, one under the base — to the storage cabinet.<br/>'
    '8. Store with the arm pointing outward.',
    ans))
story.append(sp(1))

# Q3 — FOV Calculations
story.append(Paragraph(
    'Q3. You are observing Bacillus cells (2 µm long) and yeast cells (10 µm long) '
    'using the high-dry (40×) lens with FN = 22 mm. Calculate FOV and how many cells fit across it.',
    h3))
story.append(HY('Formula: FOV = FN ÷ Total Magnification. Then: # cells = FOV ÷ cell length. '
                'Total mag at 40× obj = 40 × 10 (ocular) = 400×.'))

story.append(tbl([
    ['Step', 'Calculation', 'Result'],
    ['Total magnification',
     '40× (objective) × 10× (ocular)',
     '400×'],
    ['FOV diameter',
     'FN ÷ Total magnification = 22 mm ÷ 400',
     '0.055 mm = <b>55 µm</b>'],
    ['Bacillus cells across FOV\n(cell length = 2 µm)',
     '55 µm ÷ 2 µm per cell',
     '≈ <b>27 cells</b>'],
    ['Yeast cells across FOV\n(cell length = 10 µm)',
     '55 µm ÷ 10 µm per cell',
     '≈ <b>5–6 cells</b>'],
], [1.5*inch, 3.5*inch, 2.2*inch]))
story.append(Paragraph(
    'Note: FOV decreases as magnification increases. At 100× total (10× obj), '
    'FOV = 22/100 = 0.22 mm = 220 µm — much larger than at 400×.',
    note))
story.append(sp(1))

# Q embedded in procedure — Q8
story.append(Paragraph(
    'Q (from procedure, step 8): To use a minimum of light, which part of the microscope '
    'should be adjusted?', h3))
story.append(Paragraph(
    'Close the <b>iris diaphragm</b> (part of the condenser assembly). '
    'This reduces the cone of light entering the condenser and objective lens. '
    'Useful for increasing contrast when viewing unstained or low-contrast specimens at low magnification.',
    ans))
story.append(sp(1))

# Q embedded in procedure — Q10
story.append(Paragraph(
    'Q (from procedure, step 10): When switching from low power to high-dry, only a slight '
    'adjustment is needed. Why?', h3))
story.append(Paragraph(
    'The objective lenses are <b>parfocal</b> — designed so that when the specimen is in focus '
    'at one objective, switching to another objective places it at approximately the same focal '
    'distance. Only minor fine-focus adjustment is needed after switching. '
    '(Popa Ch.2 slide 9 — parfocality is specifically tested.)',
    ans))
story.append(sp(1))

# Q embedded in procedure — Q11
story.append(Paragraph(
    'Q (from procedure, step 11): More light is usually needed at higher magnification. '
    'How can you increase the amount of light?', h3))
story.append(Paragraph(
    '1. <b>Open the iris diaphragm wider</b> — allows more light into the condenser.<br/>'
    '2. <b>Raise the condenser</b> closer to the slide — concentrates more light onto the specimen.<br/>'
    '3. <b>Increase lamp voltage/brightness</b> using the illuminator control on the base.<br/>'
    '<i>At 100× (oil immersion): immersion oil also increases light entering the objective by '
    'preventing refraction at the glass–air interface.</i>',
    ans))
story.append(sp(1))

# Q13 observations
story.append(Paragraph(
    'Q (from procedure, step 13): Did color change with different lenses? Did FOV change? '
    'How many cells fit at higher vs lower magnification?', h3))
story.append(Paragraph(
    '<b>Color:</b> Color does not change when switching objectives — the same light source and stain '
    'are used throughout. However, contrast and brightness change (more light needed at higher mag).<br/><br/>'
    '<b>FOV:</b> Yes — FOV <b>decreases</b> as magnification increases. Fewer cells are visible '
    'at 1000× than at 100×.<br/><br/>'
    '<b>Cell count:</b> At low power (100× total, FOV ~220 µm) many cells are visible across the field. '
    'At oil immersion (1000× total, FOV ~22 µm) only 1–3 Bacillus cells may span the field.',
    ans))
story.append(sp(2))

# Footer
story.append(Paragraph(
    'Sources: BIO203A Lab 1 Microscopy docx (Popa); Popa Ch.2 lecture slides. Spring 2026.',
    ParagraphStyle('ct', fontName='Helvetica-Oblique', fontSize=7.5, textColor=colors.Color(0.5, 0.5, 0.5))))

doc.build(story)
print('Done -> ' + OUTPUT)

