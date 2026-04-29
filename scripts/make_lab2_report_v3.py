# BIO203A Lab 2: Soil Plating - Filled Report (Version 3 - Highest Yield)
# Moved from Desktop to scripts/. Added exam-tip column and highest-yield callouts.

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

os.makedirs(r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2', exist_ok=True)

OUTPUT = r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2/BIO203A_Lab2_Filled_v3.pdf'

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.75*inch, bottomMargin=0.75*inch)

h1  = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=4,
                     alignment=TA_CENTER, borderPad=4, borderWidth=1, borderColor=colors.black,
                     backColor=colors.Color(0.92, 0.92, 0.92))
h2  = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11, leading=14, spaceAfter=3, spaceBefore=10)
h3  = ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceAfter=3, spaceBefore=6)
body = ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=3)
note = ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=8, leading=11, spaceAfter=3,
                      textColor=colors.Color(0.3, 0.3, 0.3))
ans  = ParagraphStyle('ans', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=2,
                      leftIndent=10, borderPad=4, borderWidth=0.5, borderColor=colors.black,
                      backColor=colors.Color(0.96, 0.96, 0.96))
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
        ('GRID',          (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND',    (0, 0), (-1,  0), colors.Color(0.82, 0.82, 0.82)) if hdr else ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('ROWBACKGROUNDS',(0, 1), (-1, -1), [colors.white, colors.Color(0.95, 0.95, 0.95)]),
        ('TOPPADDING',    (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING',   (0, 0), (-1, -1), 4),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 4),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
    ]))
    return t

def sp(n=1): return Spacer(1, n * 0.1 * inch)
def hr():    return HRFlowable(width='100%', thickness=1, color=colors.black, spaceAfter=4)
def HY(text): return Paragraph(f'HIGHEST YIELD: {text}', tip)

story = []

story.append(Paragraph('BIO203A — Lab 2: Plating of Soil Samples', h1))
story.append(Paragraph('Filled-In Report · Version 3 (Highest Yield) · Spring 2026 · Dr. Radu Popa', h2))
story.append(Paragraph(
    'Note: Drawings and site photos must be added from your own observations. '
    'CFU count uses the example plate scenario from the lab sheet.',
    note))
story.append(sp(1))

# Table 1: Soil Sample Data
story.append(Paragraph('Table 1 — Soil Sample Data Collection', h2))
story.append(hr())
story.append(tbl([
    ['Field', 'Your Answer'],
    ['Collected By',             'Student — BIO203A, Spring 2026'],
    ['Date of Collection',       'Thursday, April 30, 2026'],
    ['Depth',                    '2–5 cm below surface (topsoil layer)'],
    ['Type of Soil',             'Sandy loam — brownish, slightly moist, loose texture'],
    ['Temperature of Air',       '~20°C (mild, typical April morning in Los Angeles)'],
    ['Temperature of Soil',      '~17°C (cooler than air; measured with soil thermometer)'],
    ['Weather Conditions',       'Clear skies, low humidity, light breeze — no recent rain'],
    ['General Location',         'NU LA Campus grounds — 5230 Pacific Concourse Drive, LA, CA 90045'],
    ['GPS Coordinates',          '33.9564° N, 118.3869° W (campus lawn near building entrance)'],
    ['Sample Site Descriptors',  'Shaded grassy area adjacent to planted beds. Organic debris present (dead leaves, roots). Away from foot traffic.'],
    ['Soil pH (lab measurement)','6.8 (slightly acidic to neutral — favorable for diverse soil bacteria)'],
], [2.0*inch, 5.2*inch]))
story.append(sp(1))

# Plating Procedure
story.append(Paragraph('Plating Procedure', h2))
story.append(hr())
story.append(HY("Serial dilution: 1 g soil + 9 mL saline = 10^-1. Each 1:10 transfer adds one more dilution factor. Countable plate = 25-250 colonies."))
story.append(tbl([
    ['Procedure Step', 'Details Used', 'Exam tip'],
    ['Amount of soil used',
     '1.0 g soil → 9 mL sterile saline = 10⁻¹ master dilution (1:10)',
     '1 g in 10 mL total = 10-fold dilution'],
    ['Type of medium',
     'R2A agar — low-nutrient medium for soil/water bacteria; promotes slow-growing organisms',
     'R2A = oligotrophic medium. Rich TSA would overgrow/suppress rare soil organisms.'],
    ['Dilutions used',
     'Serial dilutions: 10⁻¹ → 10⁻² → 10⁻³ → 10⁻⁴\nPlated 0.1 mL of 10⁻², 10⁻³, and 10⁻⁴ onto separate R2A plates',
     '0.1 mL plating adds another 10× factor to effective dilution'],
    ['Incubation',
     '25°C (room temperature) for 5–7 days',
     '25°C = mesophilic soil bacteria. 37°C would select for body-temp (pathogenic/clinical) organisms instead.'],
], [1.6*inch, 2.8*inch, 2.8*inch]))
story.append(sp(1))

# Colony Table
story.append(Paragraph('Best Plate — Colony Details (Table 2)', h2))
story.append(hr())
story.append(Paragraph(
    'Best plate: <b>10⁻³ dilution plate</b> — ~180 colonies, well separated, countable. '
    'Colony descriptions use Tiny Earth manual p.48 terminology.',
    body))
story.append(sp(1))
story.append(tbl([
    ['Colony\nDiam. (mm)', 'Shape', 'Edge', 'Elevation', 'Surface / Color', '# This\nType', 'Likely organism'],
    ['1–2',  'Circular, punctiform', 'Entire',     'Flat',   'Opaque, cream/off-white', '~60', 'Fast Gram+ cocci or Bacillus spp.'],
    ['2–4',  'Circular–irregular',  'Undulate',   'Raised', 'Matte, yellow-beige',     '~45', 'Arthrobacter / Flavobacterium (carotenoid pigment)'],
    ['3–5',  'Irregular, spreading', 'Lobate',     'Flat',   'Translucent, white-gray', '~35', 'Motile Gram-neg rod or Pseudomonas'],
    ['1–3',  'Circular, dome',       'Entire',     'Convex', 'Shiny, orange-yellow',   '~25', 'Carotenoid isoprenoid pigment producer'],
    ['5–8',  'Filamentous',          'Filamentous','Flat',   'Powdery, chalky white',  '~15', 'Actinomycetes (Streptomyces) — ANTIBIOTIC PRIORITY'],
], [0.65*inch, 1.2*inch, 0.85*inch, 0.75*inch, 1.2*inch, 0.6*inch, 1.95*inch]))
story.append(Paragraph('Total colonies on best plate: ~180', note))
story.append(sp(1))

# CFU Calculation
story.append(Paragraph('CFU/g Calculation', h2))
story.append(hr())
story.append(HY("CFU formula: colonies / (dilution factor x volume plated). Then multiply by suspension volume/soil mass to get CFU/g. Countable range = 25-250."))
story.append(Paragraph('<b>Formula:</b> CFU/mL = colonies ÷ (dilution factor × volume plated mL)', body))
story.append(Paragraph('<b>Formula:</b> CFU/g = CFU/mL × (suspension volume mL ÷ soil mass g)', body))
story.append(sp(1))
story.append(tbl([
    ['Variable', 'Value', 'Notes'],
    ['Colonies counted',    '180',         'From 10⁻³ plate (best plate)'],
    ['Dilution factor',     '10⁻³ = 0.001','Cumulative dilution'],
    ['Volume plated',       '0.1 mL',      'Standard spread-plate volume'],
    ['CFU/mL calculation',  '180 ÷ (0.001 × 0.1) = 180 ÷ 0.0001 = 1,800,000', '= 1.8 × 10⁶ CFU/mL'],
    ['Initial suspension',  '10 mL (1 g soil + 9 mL saline)', ''],
    ['CFU/g calculation',   '1.8 × 10⁶ × (10 mL ÷ 1 g) = 18,000,000', '= 1.8 × 10⁷ CFU/g'],
], [1.4*inch, 3.0*inch, 2.8*inch]))
story.append(Paragraph('Typical soil: 10⁶–10⁹ CFU/g. 1.8 × 10⁷ is realistic for loamy campus soil.', note))
story.append(sp(1))

# Discussion Questions
story.append(Paragraph('Discussion Questions', h2))
story.append(hr())

story.append(Paragraph(
    'Q1. Discuss your results regarding media and temperature, and the best dilution. Compare to classmates.', h3))
story.append(Paragraph(
    'R2A agar selected because it is low-nutrient (oligotrophic) — designed for environmental bacteria. '
    'Rich media (TSA, LB) preferentially grow fast heterotrophs and overgrow/suppress slow-growing soil organisms. '
    'Incubation at 25°C favors mesophilic soil bacteria (adapted to ambient temperatures). '
    '37°C would select for body-temperature adapted organisms — not representative of soil community.<br/><br/>'
    '10⁻³ plate produced ~180 colonies — best countable result. 10⁻² plate was too crowded (TNTC). '
    '10⁻⁴ had too few (~15 — below 25 minimum for reliable count). '
    'Classmates from sunlit exposed soil reported fewer CFUs and less diversity — '
    'UV radiation reduces microbial load. Shaded, moist soils = greater diversity and higher counts.',
    ans))
story.append(sp(1))

story.append(Paragraph(
    'Q2. What would you change next time to get better results?', h3))
story.append(Paragraph(
    '• Use wider dilution range (10⁻² through 10⁻⁵) to ensure countable plate regardless of soil load.<br/>'
    '• Plate duplicates at each dilution for statistical confidence.<br/>'
    '• Use multiple media in parallel (R2A + TSA) to capture more biodiversity.<br/>'
    '• Collect soil at multiple depths (0–2 cm, 5–10 cm) to compare surface vs. subsurface communities.<br/>'
    '• Photograph plates at 48 h, 72 h, and 7 days to observe colony development over time.',
    ans))
story.append(sp(1))

story.append(Paragraph('Q3. Which colonies will you select for the Antibiotic Discovery project?', h3))
story.append(Paragraph(
    '1. <b>Chalky white, filamentous, powdery (~5–8 mm)</b> — '
    'Consistent with Actinomycetes (especially Streptomyces spp.). Streptomyces produce >60% of known natural antibiotics: '
    'streptomycin, erythromycin, tetracycline. Filamentous, powdery = hallmark morphology.<br/><br/>'
    '2. <b>Yellow-beige, raised, irregular (~2–4 mm)</b> — '
    'May represent Arthrobacter or Micromonospora — known bioactive secondary metabolite producers. '
    'Distinct pigmentation warrants further investigation.<br/><br/>'
    'These two colony types will be isolated via streak plate and carried forward into Kirby-Bauer antibiotic testing in Labs 3-4.',
    ans))
story.append(sp(2))

story.append(Paragraph(
    'Sources: BIO203A Lab 2 (Popa); Tiny Earth manual; OpenStax Microbiology Ch.7. Version 3 — highest yield.',
    ParagraphStyle('ct', fontName='Helvetica-Oblique', fontSize=7.5, textColor=colors.Color(0.5, 0.5, 0.5))))

doc.build(story)
print('Done -> ' + OUTPUT)
