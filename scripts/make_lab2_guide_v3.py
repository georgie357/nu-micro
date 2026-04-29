# BIO203A Lab 2: Soil Plating - Study Guide (Version 3 - Highest Yield)
# Moved from Desktop to scripts/. Added exam-tip columns and highest-yield callouts.

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
import os

os.makedirs(r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2', exist_ok=True)

OUTPUT = r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2/BIO203A_Lab2_Study_Guide_v3.pdf'

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.75*inch, bottomMargin=0.75*inch)

h1  = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=4,
                     alignment=TA_CENTER, borderPad=4, borderWidth=1, borderColor=colors.black,
                     backColor=colors.Color(0.92, 0.92, 0.92))
h2  = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11, leading=14, spaceAfter=3, spaceBefore=10)
h3  = ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceAfter=3, spaceBefore=6)
body = ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=3)
bld  = ParagraphStyle('bld', fontName='Helvetica-Bold', fontSize=9, leading=13, spaceAfter=3)
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

def tbl(data, widths):
    wrapped = [[_c(c, hdr=(i == 0)) for c in row] for i, row in enumerate(data)]
    t = Table(wrapped, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('GRID',          (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND',    (0, 0), (-1,  0), colors.Color(0.82, 0.82, 0.82)),
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

story.append(Paragraph('BIO203A — Lab 2 Study Guide: Soil Plating — Version 3 (Highest Yield)', h1))
story.append(Paragraph(
    'Serial Dilutions · CFU Calculations · Colony Morphology · Aseptic Technique · Antibiotic Discovery',
    h2))
story.append(Paragraph('Connections to Ch.7 Biochemistry noted throughout', note))
story.append(sp(1))

# 1. Why plate soil
story.append(Paragraph('1. Purpose — Why Plate Soil?', h2))
story.append(hr())
story.append(tbl([
    ['Goal', 'How plating achieves it', 'Exam tip'],
    ['Isolate individual organisms',
     'Diluting separates cells so each grows into a distinct, countable colony',
     '1 colony = descended from 1 original living cell = 1 CFU'],
    ['Quantify microbial load (CFU/g)',
     'Count colonies × correct for dilution = estimate of living bacteria in original soil',
     'CFU = Colony Forming Unit — living cells only'],
    ['Screen for antibiotic producers',
     'Tiny Earth: look for colonies that inhibit neighbors — potential drug leads',
     'Chalky/powdery = Actinomycetes = highest antibiotic priority'],
    ['Study biodiversity',
     'Different colony types = different species. Morphology gives identity clues.',
     'Colony morphology reflects cell wall, pigment, motility — all biochemistry'],
], [1.6*inch, 2.6*inch, 3.0*inch]))
story.append(sp(2))

# 2. Serial dilution
story.append(Paragraph('2. Serial Dilution', h2))
story.append(hr())
story.append(HY("Countable plate = 25-250 colonies. Below 25 = statistically unreliable. Above 250 = TNTC. Plating 0.1 mL from a 10^-3 tube gives EFFECTIVE dilution of 10^-4."))
story.append(Paragraph(
    'Soil contains too many bacteria to count directly. Serial dilution reduces concentration in controlled steps. '
    'Countable plate range = <b>25–250 colonies</b>.',
    body))
story.append(sp(1))
story.append(tbl([
    ['Step', 'What you do', 'Dilution factor', 'Meaning', 'Exam trap'],
    ['Master suspension',
     '1 g soil + 9 mL saline; vortex',
     '10⁻¹', '1 part soil in 10 total',
     '10 mL total = 1 g in 10 mL'],
    ['1st dilution',
     '1 mL from master → 9 mL saline',
     '10⁻²', '1/100 of original',
     'Transfer exactly 1 mL each time'],
    ['2nd dilution',
     '1 mL from 10⁻² → 9 mL saline',
     '10⁻³', '1/1,000 of original', ''],
    ['3rd dilution',
     '1 mL from 10⁻³ → 9 mL saline',
     '10⁻⁴', '1/10,000 of original', ''],
    ['Plating 0.1 mL',
     '0.1 mL from chosen tube → spread on agar',
     'Adds 10× more (×0.1)',
     '0.1 mL from 10⁻³ tube = effective 10⁻⁴',
     'Common error: forgetting the 0.1 mL factor in the formula'],
], [0.85*inch, 1.7*inch, 0.85*inch, 1.1*inch, 2.7*inch]))
story.append(Paragraph('Use a NEW sterile pipette/spreader at every transfer — carryover contaminates the entire series.', note))
story.append(sp(2))

# 3. CFU Calculation
story.append(Paragraph('3. CFU/g Calculation', h2))
story.append(hr())
story.append(HY("CFU/mL = colonies / (dilution factor x volume plated). CFU/g = CFU/mL x (suspension volume / soil mass). Forgetting the 0.1 mL or the x10 conversion are the two most common mistakes."))
story.append(Paragraph('CFU = Colony Forming Unit — one colony = one original living cell.', body))
story.append(Paragraph('Formula 1 — CFU/mL of original suspension:', h3))
story.append(Paragraph('CFU/mL = colonies counted ÷ (dilution factor × volume plated in mL)', bld))
story.append(Paragraph('Formula 2 — CFU/g of soil:', h3))
story.append(Paragraph('CFU/g = CFU/mL × (total volume of initial suspension ÷ grams of soil)', bld))
story.append(sp(1))
story.append(tbl([
    ['Calculation step', 'Work shown', 'Result'],
    ['Step 1: CFU/mL',
     '180 colonies ÷ (10⁻³ × 0.1 mL) = 180 ÷ 0.0001',
     '1.8 × 10⁶ CFU/mL'],
    ['Step 2: CFU/g',
     '1.8 × 10⁶ × (10 mL ÷ 1 g)',
     '1.8 × 10⁷ CFU/g of soil'],
], [1.8*inch, 2.8*inch, 2.6*inch]))
story.append(Paragraph('Typical range: healthy soil = 10⁶–10⁹ CFU/g. Sandy/dry = lower; rich organic = higher.', note))
story.append(sp(1))
story.append(tbl([
    ['Common mistake', 'Correct approach'],
    ['Using dilution factor without accounting for 0.1 mL volume plated',
     'Plating 0.1 mL from 10⁻³ tube = effective dilution 10⁻⁴. Use BOTH in denominator.'],
    ['Forgetting to convert CFU/mL to CFU/g',
     'Multiply CFU/mL × (10 mL suspension ÷ 1 g soil) to get CFU per gram.'],
    ['Counting plates with <25 or >250 colonies',
     '<25 = statistically unreliable. >250 = TNTC (too numerous to count). Use ONLY countable plates.'],
], [2.3*inch, 4.9*inch]))
story.append(sp(2))

# 4. Culture media
story.append(PageBreak())
story.append(Paragraph('4. Culture Media — What We Use and Why', h2))
story.append(hr())
story.append(tbl([
    ['Medium', 'Nutrient level', 'Why used in soil plating', 'Exam tip'],
    ['R2A agar', 'Low-nutrient (oligotrophic)',
     'Designed for environmental bacteria. Slow-growing soil organisms cannot compete on rich media.',
     'R2A = standard for Tiny Earth. Rich TSA would overgrow rare soil organisms.'],
    ['TSA (Tryptic Soy Agar)', 'Rich / complex',
     'Good for fast-growing heterotrophs. Would mask rare soil organisms.',
     'Tryptone + soy = rich amino acid/N source — not what we want for soil diversity.'],
    ['Selective media', 'Varies',
     'Select specific groups (e.g., add antibacterials to select fungi)',
     'Exploits specific biochemical properties — organisms lacking required pathway cannot grow.'],
], [1.1*inch, 1.0*inch, 2.5*inch, 2.6*inch]))
story.append(sp(2))

# 5. Colony morphology
story.append(Paragraph('5. Colony Morphology', h2))
story.append(hr())
story.append(tbl([
    ['Descriptor', 'Options', 'What it tells you', 'Exam tip'],
    ['Whole colony shape', 'Circular, irregular, rhizoid, filamentous, spindle',
     'Growth pattern — tight vs. spreading',
     'Filamentous/spreading = motile organisms or Actinomycetes'],
    ['Size', 'Punctiform (<1 mm), small (1–2 mm), medium (3–5 mm), large (>5 mm)',
     'Growth rate and cell density', ''],
    ['Edge', 'Entire (smooth), undulate (wavy), lobate (lobed), serrate, filamentous',
     'Cell arrangement at colony perimeter', ''],
    ['Elevation', 'Flat, raised, convex, umbonate (raised center), crateriform',
     'Growth habit', ''],
    ['Surface texture', 'Smooth/shiny, matte, wrinkled, mucoid (slimy), dry, powdery/chalky',
     'Capsule = mucoid; endospore formers = dry; Actinomycetes = powdery/chalky',
     'Powdery/chalky = ACTINOMYCETES (antibiotic priority)'],
    ['Color/opacity', 'White, cream, yellow, orange, pink, tan, transparent, opaque',
     'Pigment production is species-specific; orange/yellow = carotenoids (isoprenoids)',
     'Chalky white + powdery = Streptomyces'],
], [1.0*inch, 1.7*inch, 1.9*inch, 2.6*inch]))
story.append(sp(1))

story.append(Paragraph('Colony types for Antibiotic Discovery — priority order:', h3))
story.append(tbl([
    ['Colony appearance', 'Likely organism', 'Antibiotic relevance', 'Priority'],
    ['Powdery/chalky, white-gray, filamentous, 5–8 mm',
     'Actinomycetes (Streptomyces spp.)',
     '>60% of known antibiotics come from Streptomyces. Streptomycin, erythromycin, tetracycline.',
     'HIGHEST'],
    ['Small, circular, cream, fast-growing',
     'Gram+ cocci or Bacillus',
     'Some Bacillus produce bacteriocins; bacitracin from B. subtilis.',
     'Medium'],
    ['Bright yellow/orange, convex, circular',
     'Flavobacterium / Arthrobacter',
     'Carotenoid pigment producers — moderate antibiotic interest.',
     'Medium'],
    ['Spreading, flat, irregular, thin',
     'Pseudomonas or motile Gram⁻ rods',
     'Lower priority — Gram⁻ pathogens themselves.',
     'Low'],
], [1.7*inch, 1.4*inch, 2.6*inch, 0.65*inch]))
story.append(sp(2))

# 6. Aseptic technique
story.append(Paragraph('6. Aseptic Technique', h2))
story.append(hr())
story.append(tbl([
    ['Rule', 'Why it matters', 'Exam tip'],
    ['Work near a flame or biosafety cabinet',
     'Updraft creates sterile zone — airborne contaminants burned or blown away',
     ''],
    ['Flame loop/spreader between each use',
     'Kills cells on tool — prevents carryover to next plate or tube',
     ''],
    ['Open tubes briefly, at an angle',
     'Minimizes time open air can fall into tube',
     ''],
    ['Label plates on BOTTOM (base)',
     'Lid is removed for inspection — base stays with plate; label always visible when stacked',
     'Tested in lab practical: WHERE to label'],
    ['Invert plates for incubation',
     'Prevents condensation dripping onto colonies — prevents spreading and merging',
     'Invert = upside down = agar on TOP'],
    ['Refrigerate at 4°C after counting',
     'Stops further growth — preserves count at time of reading',
     ''],
], [1.7*inch, 2.8*inch, 2.7*inch]))
story.append(sp(2))

# 7. Ch.7 Biochemistry connections
story.append(Paragraph('7. Ch.7 Biochemistry Connections (Exam tie-ins)', h2))
story.append(hr())
story.append(tbl([
    ['Lab observation', 'Ch.7 Biochemistry explanation'],
    ['Why R2A supports soil bacteria better than rich media',
     'Oligotrophic soil bacteria have enzyme systems adapted to low carbohydrate concentrations (Ch.7 §7.2). Rich media overwhelm them with fast-growing competitors.'],
    ['Why incubate at 25°C not 37°C',
     'Enzyme function depends on protein tertiary structure (Ch.7 §7.4). Soil organisms have proteins optimized for ~20-25°C. 37°C risks partial denaturation.'],
    ['Why Actinomycetes colony is chalky/powdery',
     'Aerial hyphae tipped with conidiospores — spore wall contains modified carbohydrates + waxy lipids (similar to mycolic acid concept, §7.3).'],
    ['Why mucoid colonies look slimy',
     'Slimy = polysaccharide capsule (Ch.7 §7.2 — exopolysaccharide secreted outside cell wall). Protects against drying.'],
    ['Why saline (NaCl) is used as diluent, not water',
     'Pure water = hypotonic → osmotic shock can lyse cells before plating. Saline maintains osmotic balance. Phospholipid bilayer integrity (Ch.7 §7.3) requires isotonic conditions.'],
    ['Why some colonies are yellow/orange',
     'Carotenoids = isoprenoid lipids (Ch.7 §7.3). Function as pigments and antioxidants — protect against UV in exposed soil.'],
], [2.0*inch, 5.2*inch]))
story.append(sp(2))

# Quick reference
story.append(Paragraph('Quick Reference', h2))
story.append(hr())
story.append(tbl([
    ['Formula / Fact', 'Value / Rule'],
    ['CFU/mL formula', 'colonies ÷ (dilution factor × volume plated mL)'],
    ['CFU/g formula', 'CFU/mL × (suspension volume mL ÷ soil mass g)'],
    ['Countable plate range', '25–250 colonies (below = unreliable; above = TNTC)'],
    ['Standard volume plated', '0.1 mL per plate (spread plate method)'],
    ['Master suspension dilution', '1 g soil + 9 mL saline = 10⁻¹ (1:10)'],
    ['Typical soil CFU/g', '10⁶–10⁹ CFU/g depending on soil type'],
    ['Incubation: R2A soil plates', '25°C room temp, 5–7 days'],
    ['Best antibiotic producer morphology', 'Chalky/powdery, white-gray, filamentous = Actinomycetes (Streptomyces)'],
    ['Why saline diluent?', 'Isotonic — prevents osmotic lysis of bacteria during dilution'],
    ['Why invert plates?', 'Prevents condensation drips from spreading/merging colonies'],
    ['Effective dilution: 0.1 mL from 10⁻³', '10⁻³ × 0.1 mL = effective 10⁻⁴ — use this in formula'],
], [2.7*inch, 4.5*inch]))

doc.build(story)
print('Done -> ' + OUTPUT)
