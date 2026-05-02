# BIO203 Chemistry Pre-Quiz Study Sheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
import os

os.makedirs(r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2', exist_ok=True)
OUTPUT = r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2/BIO203_Chem_PreQuiz_Study.pdf'

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.75*inch, bottomMargin=0.75*inch)

h1  = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=14, leading=17, spaceAfter=4,
                     alignment=TA_CENTER, borderPad=4, borderWidth=1, borderColor=colors.black,
                     backColor=colors.Color(0.92, 0.92, 0.92))
h2  = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11, leading=14, spaceAfter=3, spaceBefore=10)
h3  = ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceAfter=3, spaceBefore=6)
body = ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=3)
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
        ('GRID',          (0,0), (-1,-1), 0.5, colors.black),
        ('BACKGROUND',    (0,0), (-1, 0), colors.Color(0.82, 0.82, 0.82)),
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
def HY(t):   return Paragraph(f'HIGHEST YIELD: {t}', tip)

story = []

story.append(Paragraph('BIO203 — Chemistry Pre-Quiz Study Sheet', h1))
story.append(Paragraph('Topics: Atomic Structure · Valence · Chemical Bonds · Acid-Base · OpenStax Appendix A', h2))
story.append(Paragraph('Due Sun May 3 · 15 questions · 30 min · 3 attempts · 10 pt bonus', note))
story.append(sp(1))

# 1. Atomic Structure
story.append(Paragraph('1. Atomic Structure', h2))
story.append(hr())
story.append(HY('Atomic number = protons. Mass number = protons + neutrons. Isotopes = same protons, different neutrons.'))
story.append(tbl([
    ['Particle', 'Location', 'Charge', 'Mass', 'Key fact'],
    ['Proton',   'Nucleus',  '+1',     '~1 amu', 'Defines the element (atomic number)'],
    ['Neutron',  'Nucleus',  '0',      '~1 amu', 'Varies in isotopes — does NOT change element identity'],
    ['Electron', 'Electron shells (orbitals)', '-1', '~0 (negligible)', 'Determines bonding and reactivity'],
], [0.9*inch, 1.3*inch, 0.6*inch, 0.7*inch, 3.7*inch]))
story.append(sp(1))
story.append(tbl([
    ['Shell (energy level)', 'Max electrons', 'Example'],
    ['Shell 1 (innermost)', '2',  'H (1), He (2)'],
    ['Shell 2',             '8',  'C (2,4), N (2,5), O (2,6)'],
    ['Shell 3',             '8',  'Na (2,8,1), Cl (2,8,7)'],
], [1.8*inch, 1.5*inch, 3.9*inch]))
story.append(sp(2))

# 2. Valence Electrons
story.append(Paragraph('2. Valence Electrons', h2))
story.append(hr())
story.append(HY('Valence electrons = outermost shell electrons. Octet rule = atoms want 8. H wants 2.'))
story.append(Paragraph(
    'Valence electrons are in the outermost shell. They determine how many bonds an atom forms. '
    'The <b>octet rule</b>: atoms bond to achieve 8 valence electrons (full outer shell). '
    'Hydrogen is the exception — it needs only 2.',
    body))
story.append(sp(1))
story.append(tbl([
    ['Element', 'Symbol', 'Atomic #', 'Electron config', 'Valence e-', 'Bonds formed'],
    ['Hydrogen',  'H', '1',  '1',       '1', '1'],
    ['Carbon',    'C', '6',  '2, 4',    '4', '4 (backbone of organic molecules)'],
    ['Nitrogen',  'N', '7',  '2, 5',    '5', '3'],
    ['Oxygen',    'O', '8',  '2, 6',    '6', '2'],
    ['Sodium',    'Na','11', '2, 8, 1', '1', '1 (loses 1 e- to form Na+)'],
    ['Chlorine',  'Cl','17', '2, 8, 7', '7', '1 (gains 1 e- to form Cl-)'],
], [0.85*inch, 0.55*inch, 0.65*inch, 0.9*inch, 0.7*inch, 3.6*inch]))
story.append(sp(2))

# 3. Chemical Bonds
story.append(Paragraph('3. Chemical Bonds', h2))
story.append(hr())
story.append(HY('Covalent = sharing. Ionic = transfer. Hydrogen = weak attraction. Polar covalent = unequal sharing (water!).'))
story.append(tbl([
    ['Bond type', 'How it forms', 'Strength', 'Biological example', 'Exam trap'],
    ['Nonpolar covalent',
     'Equal sharing of electrons between atoms of same/similar electronegativity',
     'Strong', 'O=O, C-H bonds in organic molecules',
     'Nonpolar = hydrophobic — does NOT dissolve in water'],
    ['Polar covalent',
     'Unequal sharing — more electronegative atom pulls e- closer, creating partial charges (delta+ / delta-)',
     'Strong', 'H2O — O pulls electrons, leaving H slightly positive',
     'Polar = hydrophilic. Water is polar covalent, NOT ionic.'],
    ['Ionic',
     'Complete transfer of e- from one atom to another; opposite charges attract',
     'Strong\n(in solid)', 'NaCl — Na loses 1 e- (Na+), Cl gains 1 e- (Cl-)',
     'Ionic compounds dissociate in water into ions'],
    ['Hydrogen',
     'Attraction between H (bonded to O or N) and a nearby O or N on another molecule',
     'Weak\n(individually)', 'Water cohesion; DNA base pairing; protein folding',
     'Individually weak, but MANY hydrogen bonds = very strong collectively'],
], [1.1*inch, 1.8*inch, 0.7*inch, 1.6*inch, 2.0*inch]))
story.append(sp(1))
story.append(Paragraph(
    '<b>Electronegativity tip:</b> F > O > N > C > H. The more electronegative atom pulls electrons toward itself. '
    'When two atoms of very different electronegativity bond, the result is polar covalent or ionic.',
    body))
story.append(sp(2))

# 4. Acid-Base
story.append(Paragraph('4. Acid-Base Chemistry', h2))
story.append(hr())
story.append(HY('pH = -log[H+]. Each unit = 10x difference. Acid = H+ donor. Base = H+ acceptor. Buffer resists pH change.'))
story.append(tbl([
    ['Concept', 'Definition', 'Example'],
    ['Acid',   'Proton (H+) donor — releases H+ in solution',        'HCl --> H+ + Cl-\nH2CO3 --> H+ + HCO3-'],
    ['Base',   'Proton (H+) acceptor — releases OH- or accepts H+',  'NaOH --> Na+ + OH-\nNH3 + H+ --> NH4+'],
    ['pH',     'pH = -log[H+]. Scale 0-14. Lower = more acidic.',    'pH 3 = [H+] = 10-3 M\npH 10 = [H+] = 10-10 M'],
    ['Neutral','[H+] = [OH-] = 10-7 M',                              'Pure water at 25C = pH 7'],
    ['Buffer', 'Resists pH change by absorbing excess H+ or OH-',    'Bicarbonate buffer in blood (pH ~7.4)'],
], [1.0*inch, 2.8*inch, 3.4*inch]))
story.append(sp(1))
story.append(tbl([
    ['pH value', 'Classification', 'Example'],
    ['0-3',   'Strongly acidic',  'Stomach acid (pH ~2), lemon juice (pH ~2)'],
    ['4-6',   'Weakly acidic',    'Coffee (pH ~5), urine (pH ~6)'],
    ['7',     'Neutral',          'Pure water'],
    ['8-10',  'Weakly basic',     'Seawater (pH ~8), baking soda (pH ~9)'],
    ['11-14', 'Strongly basic',   'Bleach (pH ~12), drain cleaner (pH ~14)'],
], [0.9*inch, 1.5*inch, 4.8*inch]))
story.append(sp(1))

# Quick calc box
story.append(Paragraph('pH Calculation — Quick Reference', h3))
story.append(tbl([
    ['Given', 'Find', 'Formula', 'Example'],
    ['[H+] concentration', 'pH', 'pH = -log[H+]',
     '[H+] = 0.001 M = 10-3 M --> pH = 3'],
    ['pH', '[H+]', '[H+] = 10-pH',
     'pH = 5 --> [H+] = 10-5 M = 0.00001 M'],
    ['pH', 'Acid or base?', 'pH < 7 = acid; pH > 7 = base',
     'pH 4.5 = acidic; pH 9 = basic'],
], [1.3*inch, 1.0*inch, 1.8*inch, 3.1*inch]))
story.append(sp(2))

# Quick Reference Summary
story.append(Paragraph('Quick Reference — Must Know for Quiz', h2))
story.append(hr())
story.append(tbl([
    ['Fact', 'Answer'],
    ['What does atomic number tell you?', 'Number of protons = identity of element'],
    ['What are isotopes?', 'Same element (same protons), different number of neutrons'],
    ['How many valence electrons does carbon have?', '4 — forms 4 bonds (backbone of all organic molecules)'],
    ['What is the octet rule?', 'Atoms bond to achieve 8 valence electrons in outer shell'],
    ['What makes a bond ionic vs covalent?', 'Ionic = electron TRANSFER; Covalent = electron SHARING'],
    ['Why is water polar?', 'O is more electronegative than H — pulls shared electrons closer, creating partial charges'],
    ['What is a hydrogen bond?', 'Weak attraction between H (bonded to O/N) and a nearby O/N'],
    ['pH of pure water?', '7 (neutral) — [H+] = [OH-] = 10-7 M'],
    ['What does a buffer do?', 'Resists changes in pH by neutralizing added acid or base'],
    ['pH 2 vs pH 4 — which is more acidic?', 'pH 2 — lower pH = more H+ = more acidic. pH 2 is 100x more acidic than pH 4.'],
], [2.5*inch, 4.7*inch]))

story.append(sp(1))
story.append(Paragraph(
    'Source: OpenStax Microbiology Appendix A. BIO203 Chemistry Pre-Quiz prep — Spring 2026.',
    ParagraphStyle('ct', fontName='Helvetica-Oblique', fontSize=7.5, textColor=colors.Color(0.5,0.5,0.5))))

doc.build(story)
print('Done -> ' + OUTPUT)
