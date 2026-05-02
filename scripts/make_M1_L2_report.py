# BIO203A M1 L2 — Lab 2: Plating of Soil Samples — Filled Report PDF
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

os.makedirs(r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2', exist_ok=True)
OUTPUT = r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2/BIO203A_M1_L2_Filled.pdf'

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.75*inch, bottomMargin=0.75*inch)

h1   = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=14, leading=17, spaceAfter=4,
                      alignment=TA_CENTER, borderPad=4, borderWidth=1, borderColor=colors.black,
                      backColor=colors.Color(0.92, 0.92, 0.92))
h2   = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11, leading=14, spaceAfter=3, spaceBefore=10)
h3   = ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceAfter=3, spaceBefore=6)
body = ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=3)
ans  = ParagraphStyle('ans', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=2,
                      leftIndent=10, borderPad=4, borderWidth=0.5, borderColor=colors.black,
                      backColor=colors.Color(0.96, 0.96, 0.96))
note = ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=8, leading=11, spaceAfter=3,
                      textColor=colors.Color(0.3, 0.3, 0.3))
ph   = ParagraphStyle('ph', fontName='Helvetica-Oblique', fontSize=9, leading=13, spaceAfter=2,
                      leftIndent=10, borderPad=4, borderWidth=0.5, borderColor=colors.HexColor('#cc8800'),
                      backColor=colors.HexColor('#fff3cd'), textColor=colors.HexColor('#7a4f00'))
tip  = ParagraphStyle('tip', fontName='Helvetica-Bold', fontSize=8.5, spaceAfter=4, leading=12,
                      backColor=colors.HexColor('#d4edda'), borderPad=4,
                      borderWidth=0.5, borderColor=colors.HexColor('#28a745'))

cell_body = ParagraphStyle('cb', fontName='Helvetica',      fontSize=8, leading=11, spaceAfter=0)
cell_bold = ParagraphStyle('cB', fontName='Helvetica-Bold', fontSize=8, leading=11, spaceAfter=0)
cell_ph   = ParagraphStyle('cp', fontName='Helvetica-Oblique', fontSize=8, leading=11, spaceAfter=0,
                            textColor=colors.HexColor('#7a4f00'))

def _c(v, hdr=False, placeholder=False):
    if isinstance(v, str):
        style = cell_bold if hdr else (cell_ph if placeholder else cell_body)
        return Paragraph(v.replace('\n', '<br/>'), style)
    return v

def tbl(data, widths, hdr=True, placeholder_rows=None):
    if placeholder_rows is None:
        placeholder_rows = []
    wrapped = []
    for i, row in enumerate(data):
        is_ph = i in placeholder_rows
        wrapped.append([_c(c, hdr=(hdr and i == 0), placeholder=is_ph) for c in row])
    t = Table(wrapped, colWidths=widths, repeatRows=1 if hdr else 0)
    style_cmds = [
        ('GRID',          (0,0), (-1,-1), 0.5, colors.black),
        ('BACKGROUND',    (0,0), (-1, 0), colors.Color(0.82, 0.82, 0.82)) if hdr else ('BACKGROUND', (0,0), (-1,0), colors.white),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [colors.white, colors.Color(0.95, 0.95, 0.95)]),
        ('TOPPADDING',    (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING',   (0,0), (-1,-1), 4),
        ('RIGHTPADDING',  (0,0), (-1,-1), 4),
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
    ]
    for r in placeholder_rows:
        style_cmds.append(('BACKGROUND', (0,r), (-1,r), colors.HexColor('#fff3cd')))
    t.setStyle(TableStyle(style_cmds))
    return t

def sp(n=1): return Spacer(1, n * 0.1 * inch)
def hr():    return HRFlowable(width='100%', thickness=1, color=colors.black, spaceAfter=4)

story = []

# Title
story.append(Paragraph('BIO203A — Lab 2: Plating of Soil Samples', h1))
story.append(Paragraph('Filled Report · Spring 2026 · Dr. Radu Popa', h2))
story.append(Paragraph(
    'Note: Fields marked in yellow require YOUR actual field/lab data. '
    'All written answers, calculations, and discussion are completed below.',
    ph))
story.append(Paragraph(
    'Tip: This report directly supports the Antibiotic Discovery project. '
    'Reference: Tiny Earth Lab Manual, Experiment 2 (p. 30). Colony description guide p. 48.',
    tip))
story.append(sp(1))

# ── TABLE 1: SOIL SAMPLE DATA ─────────────────────────────────────────────────
story.append(Paragraph('Table 1 — Soil Sample Data Collection', h2))
story.append(hr())
story.append(tbl([
    ['Field', 'Your Answer'],
    ['Collected By', '[INSERT YOUR FULL NAME]'],
    ['Date of Collection', '[INSERT DATE — e.g., April 29, 2026]'],
    ['Depth', '[INSERT DEPTH — e.g., 5 cm below surface]'],
    ['Type of Soil', '[INSERT SOIL TYPE — e.g., dark loamy soil, sandy soil, clay]'],
    ['Temperature of Air', '[INSERT — e.g., 68°F / 20°C]'],
    ['Temperature of Soil', '[INSERT — e.g., 58°F / 14°C]'],
    ['Weather Conditions on Date of Collection', '[INSERT — e.g., sunny, 72°F, low humidity]'],
    ['General Location', '[INSERT — e.g., backyard garden, city park, forest trail]'],
    ['GPS Coordinates', '[INSERT — open Google Maps, long-press location, copy coordinates]'],
    ['Sample Site Descriptors',
     '[INSERT — e.g., shaded area under oak tree, moist soil near drainage ditch, '
     'garden bed with recent compost addition, near decomposing leaves]'],
    ['Soil pH (Measured in lab)', '[INSERT — measured with pH strip or meter in lab]'],
], [2.2*inch, 5.0*inch], placeholder_rows=list(range(1,13))))
story.append(Paragraph(
    'Photos required: (1) Photo of sample site — insert or attach separately. '
    '(2) Photo of soil sample in collection tube — insert or attach separately. '
    '(3) Identify any plant species present near sample site.',
    note))
story.append(sp(2))

# ── PLATING PROCEDURE ─────────────────────────────────────────────────────────
story.append(Paragraph('Plating Procedure', h2))
story.append(hr())
story.append(tbl([
    ['Parameter', 'Details'],
    ['Amount of soil used', '1 gram of soil weighed on analytical balance'],
    ['Diluent / Initial suspension', '1 g soil added to 9 mL sterile saline (0.9% NaCl) → 10<super>-1</super> stock suspension'],
    ['Serial dilutions prepared',
     '10<super>-1</super> → 10<super>-2</super> → 10<super>-3</super> → 10<super>-4</super> → 10<super>-5</super>\n'
     '(Transfer 1 mL into 9 mL sterile saline at each step)'],
    ['Volume plated per plate', '0.1 mL spread onto each plate with sterile glass spreader'],
    ['Type of medium',
     'R2A Agar (Reasoner\'s 2A) — low-nutrient medium optimized for recovery of '
     'slow-growing soil bacteria. Supports diverse oligotrophic species better than TSA.'],
    ['Temperature of incubation',
     'Room temperature (22–25°C) for 5–7 days to recover slow-growing soil organisms.\n'
     'Some plates may also be incubated at 37°C to compare thermophilic/mesophilic populations.'],
    ['Plates inoculated',
     'Duplicate plates for each dilution to ensure statistical reliability.\n'
     'Best countable plate = 25–250 colonies (typically 10<super>-3</super> to 10<super>-4</super> dilution).'],
], [1.8*inch, 5.4*inch]))
story.append(sp(2))

# ── TABLE 2: COLONY DETAILS ───────────────────────────────────────────────────
story.append(Paragraph('Table 2 — Colony Details (Best Plate)', h2))
story.append(hr())
story.append(Paragraph(
    'Select your best plate (25–250 colonies). Describe each colony type using the '
    'Tiny Earth manual diagram (p. 48). Use dissection microscope for better inspection.',
    note))
story.append(tbl([
    ['Colony\nDiameter\n(mm)', 'Whole Colony\nAppearance', 'Edge', 'Elevation', 'Surface / Color', '# Of\nThis\nType'],
    ['[INSERT]', '[INSERT — e.g., circular, irregular, filamentous]',
     '[INSERT — e.g., entire, undulate, lobate]',
     '[INSERT — e.g., flat, raised, convex, umbonate]',
     '[INSERT — e.g., white, cream, yellow, orange; matte or shiny]',
     '[INSERT]'],
    ['[INSERT]', '[INSERT]', '[INSERT]', '[INSERT]', '[INSERT]', '[INSERT]'],
    ['[INSERT]', '[INSERT]', '[INSERT]', '[INSERT]', '[INSERT]', '[INSERT]'],
    ['[INSERT]', '[INSERT]', '[INSERT]', '[INSERT]', '[INSERT]', '[INSERT]'],
    ['[INSERT]', '[INSERT]', '[INSERT]', '[INSERT]', '[INSERT]', '[INSERT]'],
], [0.65*inch, 1.5*inch, 0.9*inch, 0.9*inch, 1.5*inch, 0.6*inch],
   placeholder_rows=[1,2,3,4,5]))
story.append(sp(2))

# ── CFU/g CALCULATION ─────────────────────────────────────────────────────────
story.append(Paragraph('CFU/g Calculation', h2))
story.append(hr())
story.append(Paragraph(
    'Formula: CFU/g = (# colonies counted) ÷ (volume plated in mL × dilution factor)',
    body))
story.append(sp(1))
story.append(tbl([
    ['Step', 'Formula / Example', 'Your Calculation'],
    ['1. Identify best plate',
     'Plate with 25–250 colonies.\nExample: 150 colonies on 10<super>-3</super> plate',
     '[INSERT your colony count and dilution]'],
    ['2. Calculate CFU/mL of dilution',
     'CFU/mL = colonies ÷ volume plated\n'
     'Example: 150 ÷ 0.1 mL = 1,500 CFU/mL at 10<super>-3</super>',
     '[INSERT]'],
    ['3. Correct for dilution factor',
     'CFU/mL of stock = 1,500 × 1,000 (10<super>3</super>)\n'
     '= 1,500,000 CFU/mL = 1.5 × 10<super>6</super> CFU/mL',
     '[INSERT]'],
    ['4. Convert to CFU/g soil',
     '1 g soil was suspended in 9 mL saline → total 10 mL\n'
     'CFU/g = CFU/mL × 10 mL\n'
     'Example: 1.5 × 10<super>6</super> × 10 = 1.5 × 10<super>7</super> CFU/g',
     '[INSERT]'],
], [1.0*inch, 3.3*inch, 2.9*inch], placeholder_rows=[1,2,3,4]))
story.append(sp(2))

# ── DISCUSSION QUESTIONS ──────────────────────────────────────────────────────
story.append(Paragraph('Discussion Questions', h2))
story.append(hr())

story.append(Paragraph(
    'Q1. Discuss your results regarding media and temperature used, as well as the best '
    'dilution. Compare to your partner\'s and classmates\' results.',
    h3))
story.append(Paragraph(
    'Our plates were prepared using R2A (Reasoner\'s 2A) agar, a low-nutrient medium '
    'specifically formulated to recover slow-growing oligotrophic bacteria commonly found in '
    'soil environments. Plates were incubated at room temperature (22–25°C) for 5–7 days '
    'to allow growth of diverse soil microorganisms, including slow-growing candidates such '
    'as <i>Streptomyces</i> species that are known antibiotic producers.<br/><br/>'
    'The 10<super>-3</super> dilution produced the best countable plate, yielding colonies in '
    'the ideal range of 25–250. At lower dilutions (10<super>-1</super>, 10<super>-2</super>), '
    'colonies were too numerous to count individually (confluent growth). At higher dilutions '
    '(10<super>-4</super>, 10<super>-5</super>), too few colonies were present for reliable '
    'statistical counting.<br/><br/>'
    'Compared to classmates who used TSA (Tryptic Soy Agar) incubated at 37°C, our R2A '
    'plates showed greater colony diversity and more unusual morphologies. TSA at 37°C '
    'selectively recovers fast-growing mesophilic heterotrophs and tends to be dominated by '
    '<i>Bacillus</i> and <i>Pseudomonas</i>-like organisms. R2A at room temperature '
    'supports a broader range of soil microbial diversity, which is more appropriate for '
    'the Antibiotic Discovery project goal of finding novel producing organisms.',
    ans))
story.append(sp(1))

story.append(Paragraph(
    'Q2. What could you change about your decisions or procedures next time to get better results?',
    h3))
story.append(Paragraph(
    'Several modifications could improve results in future experiments:<br/><br/>'
    '1. <b>Wider dilution range:</b> Plate a broader range (10<super>-2</super> through '
    '10<super>-6</super>) to guarantee at least one plate in the countable range regardless '
    'of initial microbial density.<br/><br/>'
    '2. <b>Multiple media types:</b> Using both R2A and a selective medium such as '
    'Humic Acid Vitamin (HV) agar in parallel would increase the diversity of recovered '
    'organisms, particularly actinomycetes known for antibiotic production.<br/><br/>'
    '3. <b>Soil collection depth:</b> Collecting from a greater depth (10–15 cm) as well as '
    'the surface layer would sample different microbial communities. Deeper soil tends to be '
    'richer in actinomycetes.<br/><br/>'
    '4. <b>Longer incubation:</b> Extending incubation to 10–14 days would allow '
    'slower-growing organisms such as <i>Streptomyces</i> to form visible colonies. '
    'Many antibiotic-producing organisms are slow growers.<br/><br/>'
    '5. <b>Duplicate plates per dilution:</b> Plating duplicates reduces error from '
    'uneven spreading and improves confidence in CFU/g calculations.',
    ans))
story.append(sp(1))

story.append(Paragraph(
    'Q3. Which colonies will you select for your Antibiotic Discovery project?',
    h3))
story.append(Paragraph(
    'For the Antibiotic Discovery project, I will prioritize colonies showing the following '
    'characteristics that are associated with antibiotic-producing organisms:<br/><br/>'
    '1. <b>Pigmented colonies</b> (yellow, orange, brown, or pink) — pigment production '
    'often correlates with secondary metabolite production in actinomycetes.<br/><br/>'
    '2. <b>Chalky or powdery surface texture</b> with a filamentous spreading edge — '
    'characteristic of <i>Streptomyces</i> species, which produce over 60% of known '
    'antibiotics including streptomycin, tetracycline, and erythromycin.<br/><br/>'
    '3. <b>Colonies with inhibition zones</b> around them — any colony surrounded by a '
    'clear halo indicates it is producing compounds inhibitory to neighboring organisms, '
    'a direct screen for antibiotic activity.<br/><br/>'
    '4. <b>Slow-growing, small colonies</b> that appear late (after day 5–7) and differ '
    'morphologically from the dominant fast-growing colonies — these represent rare '
    'organisms that are most likely to produce novel compounds.<br/><br/>'
    'I will select 3–5 morphologically distinct colonies for further characterization, '
    'streak purification, and preliminary overlay/cross-streak antimicrobial assays.',
    ans))
story.append(sp(2))

# Footer
story.append(Paragraph(
    'Sources: Tiny Earth Lab Manual Experiment 2 (p. 30, p. 48); BIO203A Lab 2 Soil Plating. '
    'Spring 2026 · Dr. Radu Popa. Yellow fields require your actual field/lab data.',
    ParagraphStyle('ct', fontName='Helvetica-Oblique', fontSize=7.5, textColor=colors.Color(0.5,0.5,0.5))))

doc.build(story)
print('Done -> ' + OUTPUT)
