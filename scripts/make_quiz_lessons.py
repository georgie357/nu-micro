# BIO203 — Quiz Lessons & Review Log PDF
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

os.makedirs(r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2', exist_ok=True)
OUTPUT = r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2/BIO203_Quiz_Lessons.pdf'

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.75*inch, bottomMargin=0.75*inch)

h1   = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=14, leading=17, spaceAfter=4,
                      alignment=TA_CENTER, borderPad=4, borderWidth=1, borderColor=colors.black,
                      backColor=colors.Color(0.92, 0.92, 0.92))
h2   = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11, leading=14, spaceAfter=3, spaceBefore=10)
h3   = ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceAfter=3, spaceBefore=6)
body = ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=3)
note = ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=8, leading=11, spaceAfter=3,
                      textColor=colors.Color(0.3, 0.3, 0.3))
hook = ParagraphStyle('hook', fontName='Helvetica-Bold', fontSize=9, leading=13, spaceAfter=4,
                      backColor=colors.HexColor('#d4edda'), borderPad=6,
                      borderWidth=1, borderColor=colors.HexColor('#28a745'))
wrong = ParagraphStyle('wrong', fontName='Helvetica-Bold', fontSize=9, leading=13, spaceAfter=4,
                       backColor=colors.HexColor('#f8d7da'), borderPad=6,
                       borderWidth=1, borderColor=colors.HexColor('#dc3545'))
partial = ParagraphStyle('partial', fontName='Helvetica-Bold', fontSize=9, leading=13, spaceAfter=4,
                         backColor=colors.HexColor('#fff3cd'), borderPad=6,
                         borderWidth=1, borderColor=colors.HexColor('#cc8800'))
ans  = ParagraphStyle('ans', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=2,
                      leftIndent=10, borderPad=4, borderWidth=0.5, borderColor=colors.black,
                      backColor=colors.Color(0.96, 0.96, 0.96))

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

story = []

# Title
story.append(Paragraph('BIO203 — Quiz Lessons &amp; Review Log', h1))
story.append(Paragraph('Read this file BEFORE every quiz and exam', h2))
story.append(Paragraph(
    'HOOK: Open this file. Go through every WRONG and PARTIAL entry. '
    'Ask: do I know the correct answer NOW and WHY? '
    'If not — re-read the relevant study sheet section before starting the quiz.',
    hook))
story.append(sp(2))

# ── QUIZ 1 ───────────────────────────────────────────────────────────────────
story.append(Paragraph('Quiz 1 — Chemistry Pre-Quiz', h2))
story.append(hr())
story.append(Paragraph('Date: May 1, 2026 &nbsp;&nbsp; Score: 13.8 / 15 — 92% &nbsp;&nbsp; Points lost: Q3 (−0.2 partial) · Q10 (−1.0 wrong)', body))
story.append(sp(1))

# Correct answers table
story.append(Paragraph('Correct Answers', h3))
story.append(tbl([
    ['Q', 'Topic', 'Question (short)', 'My Answer'],
    ['1',  'Atomic structure',   'Which particle determines element identity?',
     'Protons (atomic number)'],
    ['2',  'Electron shells',    'Max electrons in shell 2?',
     '8'],
    ['4',  'Valence electrons',  'How many valence electrons does carbon have?',
     '4 (forms 4 bonds — backbone of organic molecules)'],
    ['5',  'Octet rule',         'Atoms bond to achieve how many valence e-?',
     '8 (H needs only 2)'],
    ['6',  'Chemical bonds',     'Covalent vs ionic — key difference?',
     'Covalent = sharing; ionic = electron transfer'],
    ['7',  'Electronegativity',  'Which atom pulls electrons harder in H2O?',
     'Oxygen — more electronegative than H'],
    ['8',  'Bond polarity',      'Water is what type of bond?',
     'Polar covalent (NOT ionic)'],
    ['9',  'Hydrogen bonds',     'What makes a hydrogen bond form?',
     'H bonded to O or N attracts nearby O or N on another molecule'],
    ['11', 'Hydrogen bond',      'H of one molecule attracted to N of another = ?',
     'Hydrogen bond'],
    ['12', 'Hydrogen bonds',     'When water evaporates, which bonds break?',
     'H-bonds BETWEEN molecules break; polar covalent bonds WITHIN stay intact'],
    ['13', 'Enzyme / energy',    'What is the SAME with and without enzyme?',
     'd — overall free energy change (Delta-G); enzymes only lower activation energy'],
    ['14', 'Molecular weight',   'Molecular weight of ethanol C2H5OH?',
     '46 g/mol (2x12 + 6x1 + 1x16 = 24+6+16)'],
    ['15', 'Isotopes',           'Difference between carbon-12 and carbon-14?',
     'Two more neutrons — same protons = same element; different neutrons = isotope'],
], [0.25*inch, 1.1*inch, 2.1*inch, 3.75*inch]))
story.append(sp(2))

# Q3 Partial
story.append(Paragraph('Q3 — PARTIAL CREDIT (0.8 / 1)   pH fill-in-the-blank', partial))
story.append(Paragraph(
    '<b>Question:</b> If pH increases from 4 to 7, H<super>+</super> will be ___ times ___ '
    'and OH<super>-</super> will be ___ times ___ than at pH 4. Solution will be more ___ than before.',
    body))
story.append(Paragraph(
    '<b>Correct answers:</b> 1/1000 · lower · 1000 · higher · basic',
    ans))
story.append(Paragraph(
    '<b>What went wrong:</b> For the blank after "H<super>+</super> will be 1/1000 times ___" '
    'I likely put <b>1000</b> instead of <b>lower</b>. '
    'The word bank had both numbers AND direction words — both must be used correctly.',
    body))
story.append(tbl([
    ['Rule', 'Detail'],
    ['pH up = H+ down',      'pH 4 to 7 = 3 units = 10^3 = 1000x change. H+ is 1/1000 times LOWER.'],
    ['pH up = OH- up',       'OH- is 1000 times HIGHER. Solution becomes more basic.'],
    ['Fill-in-the-blank tip','Scan the FULL word bank first. Check: does this blank need a number or a direction word?'],
], [1.5*inch, 5.7*inch]))
story.append(sp(2))

# Q10 Wrong
story.append(Paragraph('Q10 — WRONG (0 / 1)   Bond identification from figure', wrong))
story.append(Paragraph(
    '<b>Question:</b> Figure shows two water molecules. Bond "B" = solid line O–H within same molecule. '
    'Bond "A" = dashed lines between two molecules. What type of bond is "B"?',
    body))
story.append(Paragraph(
    '<b>My answer:</b> Hydrogen   <b>Correct answer:</b> Polar covalent',
    ans))
story.append(Paragraph(
    '<b>What went wrong:</b> I confused which label was which. '
    'Bond B (solid line, within molecule) = polar covalent. '
    'Bond A (dashed lines, between molecules) = hydrogen bond.',
    body))
story.append(tbl([
    ['Bond type', 'Visual cue', 'Location', 'Example'],
    ['Polar covalent', 'SOLID line',  'Within same molecule (O–H)',          'O–H in water'],
    ['Hydrogen bond',  'DASHED line', 'Between two molecules (H...O or H...N)', 'Water cohesion; DNA base pairing'],
], [1.2*inch, 1.1*inch, 2.2*inch, 2.7*inch]))
story.append(Paragraph(
    '<b>Rule: In ANY bond diagram — identify WITHIN vs BETWEEN molecules FIRST, then name the bond.</b>',
    body))
story.append(sp(2))

# Lessons Summary
story.append(Paragraph('Lessons Summary — Apply to Every Future Quiz', h2))
story.append(hr())
story.append(tbl([
    ['#', 'Rule', 'Source'],
    ['1', 'Fill-in-the-blank: check if blank needs a number OR a direction word — never reuse same word for both', 'Q3'],
    ['2', 'pH up: H+ goes DOWN (1/1000x per 3 units), OH- goes UP (1000x per 3 units)', 'Q3'],
    ['3', 'Bond diagrams: solid line = covalent (within molecule); dashed line = hydrogen bond (between molecules)', 'Q10'],
    ['4', 'Isotopes = same protons (same element), different neutrons (different mass number)', 'Q15'],
    ['5', 'Enzymes lower activation energy ONLY — Delta-G (overall free energy change) is unchanged', 'Q13'],
    ['6', 'Molecular weight: count every atom; C=12, H=1, O=16, N=14', 'Q14'],
], [0.25*inch, 5.5*inch, 1.45*inch]))
story.append(sp(2))

# Pre-Quiz Checklist
story.append(Paragraph('Pre-Quiz / Pre-Exam Checklist', h2))
story.append(hr())
story.append(tbl([
    ['Step', 'Action'],
    ['1', 'Read every WRONG and PARTIAL entry in this file'],
    ['2', 'For each: can you explain WHY the correct answer is correct — without looking?'],
    ['3', 'Any lesson that feels shaky: re-read the relevant study sheet section'],
    ['4', 'For bond diagrams: look for solid vs dashed lines FIRST before answering'],
    ['5', 'For fill-in-the-blank: scan the ENTIRE word bank before filling any blank'],
    ['6', 'For molecular weight: write out every atom and count carefully'],
], [0.4*inch, 6.8*inch]))

story.append(sp(1))
story.append(Paragraph(
    'BIO203 Quiz Lessons Log — Spring 2026. Update after every graded quiz.',
    ParagraphStyle('ct', fontName='Helvetica-Oblique', fontSize=7.5, textColor=colors.Color(0.5,0.5,0.5))))

doc.build(story)
print('Done -> ' + OUTPUT)
