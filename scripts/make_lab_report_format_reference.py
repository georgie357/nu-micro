# BIO203 Lab Report Format Reference — Popa requirement (May 2026)
# Quick-reference printable PDF showing the 8-section traditional format
# and the citation rules.

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\BIO203_Lab_Report_Format_Reference.pdf"

h1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=16, spaceAfter=6,
                    textColor=colors.HexColor('#1a1a6e'))
h2 = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=12, spaceAfter=4,
                    spaceBefore=10, textColor=colors.HexColor('#1a1a6e'))
h3 = ParagraphStyle('H3', fontName='Helvetica-Bold', fontSize=10, spaceAfter=3,
                    spaceBefore=6)
bod = ParagraphStyle('BD', fontName='Helvetica', fontSize=9.5, spaceAfter=3, leading=13)
bul = ParagraphStyle('BL', fontName='Helvetica', fontSize=9.5, spaceAfter=2,
                     leading=13, leftIndent=14, firstLineIndent=-10)
warn = ParagraphStyle('WN', fontName='Helvetica-Bold', fontSize=10, spaceAfter=4,
                      leading=13, backColor=colors.HexColor('#ffe5e5'),
                      borderPad=6, borderWidth=1, borderColor=colors.HexColor('#cc0000'))
ok = ParagraphStyle('OK', fontName='Helvetica-Bold', fontSize=10, spaceAfter=4,
                    leading=13, backColor=colors.HexColor('#e5ffe5'),
                    borderPad=6, borderWidth=1, borderColor=colors.HexColor('#2d7a2d'))

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
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t


def B(text): return f'<b>{text}</b>'
def sp(n=6): return Spacer(1, n)


doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
                        topMargin=0.6 * inch, bottomMargin=0.6 * inch)
W = 7.0 * inch
story = []

story += [
    Paragraph("BIO203 — Traditional Lab Report Format",
              ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=20,
                             alignment=TA_CENTER, textColor=colors.HexColor('#1a1a6e'))),
    sp(4),
    Paragraph("Professor Popa Requirement — National University, Spring 2026",
              ParagraphStyle('TS', fontName='Helvetica', fontSize=11, alignment=TA_CENTER,
                             textColor=colors.grey)),
    HRFlowable(width=W, thickness=2, color=colors.HexColor('#1a1a6e')),
    sp(8),
]

# ─── REQUIRED FORMAT ──────────────────────────────────────────────────────────
story.append(Paragraph("⛔⛔⛔ HARD RULE: NO Handout Q&A Format in Traditional Reports", h1))
story.append(Paragraph(
    f"The traditional lab report is a science paper, NOT a fill-in-the-handout document. "
    f"NEVER include numbered \"Q1: ...\", \"Q2: ...\" question-and-answer blocks in the traditional report. "
    f"Those belong only in the D2L docx quiz form. In the traditional report, information from "
    f"handout questions is integrated as flowing prose into the appropriate section "
    f"(procedural details → Materials and Methods; observations → Results and Discussion; "
    f"calculations → Results and Discussion; interpretation → Discussion).", warn))
story.append(Paragraph(
    f"Test: would this sentence appear in a published microbiology paper, or only on a "
    f"homework worksheet? If worksheet, leave it out of the traditional report.", bod))
story.append(sp(6))

story.append(Paragraph("⛔⛔⛔ HARD RULE: Textbook PDF is Read-Only", h1))
story.append(Paragraph(
    f"The OpenStax Microbiology textbook at "
    f"{B('C:\\Users\\User\\Dropbox\\Nu micro\\microbiology_-_WEB.pdf')} "
    f"must never be deleted, moved, renamed, or overwritten by any script or AI assistant. "
    f"It is the only source against which lab report citations are verified. "
    f"If it is missing, lab report writing must STOP until the file is restored from "
    f"openstax.org/details/books/microbiology.", warn))
story.append(sp(8))

story.append(Paragraph("Required Sections (in order)", h1))
story.append(Paragraph(
    f"Every lab — Lab 1 through Lab 17 — must include the following 8 sections in this exact order. "
    f"This is a separate deliverable from the D2L docx quiz form (the quiz form is data submission; "
    f"this report is the graded analysis).", bod))
story.append(sp(4))

story.append(tbl([
    ['#', 'Section', 'What goes here'],
    ['1', 'Title', 'Lab number + lab name (e.g. "Lab 3: Pick and Patch of Solid Colonies")'],
    ['2', 'Name', 'Your full name, date, course, professor (BIO203A — Spring 2026 — Dr. Popa)'],
    ['3', 'Scope', '1–2 sentences stating what this lab investigated and why'],
    ['4', 'Introduction', 'Background on the technique + why it matters. 1–2 paragraphs. Cite OpenStax for factual claims.'],
    ['5', 'Materials and Methods', 'Exact materials used + step-by-step procedure followed. Past-tense narrative prose (not a copy of the manual, not a numbered list of questions).'],
    ['6', 'Results and Discussion', 'Observations, data tables, photos, calculations + interpretation. Flowing prose, NOT a Q&A block.'],
    ['7', 'Conclusion', 'What was learned + connection to course concepts and the Antibiotic Discovery project.'],
    ['8', 'References', 'OpenStax textbook only — one entry total.'],
], [0.3 * inch, 1.7 * inch, 5.0 * inch]))
sp(8)

story.append(Paragraph("What NOT to put in a traditional lab report", h2))
story.append(Paragraph("• ❌ Numbered handout questions (\"Q1...\", \"Question 2:...\")", bul))
story.append(Paragraph("• ❌ \"Procedure Question Responses\" section headers or Q&A blocks", bul))
story.append(Paragraph("• ❌ Copy-pasted lab handout text", bul))
story.append(Paragraph("• ❌ Bullet-list answers to handout prompts", bul))
story.append(Paragraph("• ✅ Instead — integrate that information as flowing prose into the relevant section", bul))
sp(8)

# ─── REFERENCE RULE ───────────────────────────────────────────────────────────
story.append(Paragraph("Reference Rule (the unique requirement)", h1))

story.append(Paragraph("✅ ALLOWED — ONE source only:", ok))
story.append(Paragraph(
    f"• {B('OpenStax Microbiology')} (the assigned textbook).", bul))

story.append(sp(4))
story.append(Paragraph(B("Citation style: CSE (Council of Science Editors) Name-Year"), h3))
story.append(Paragraph(
    f"CSE is the gold standard for biology, microbiology, chemistry, and medical lab reports. "
    f"APA is acceptable at some schools but CSE is the field standard for the life sciences. "
    f"Use CSE Name-Year unless your professor specifies otherwise.", bod))

story.append(sp(4))
story.append(Paragraph(B("OpenStax Microbiology — authoritative author info:"), h3))
story.append(Paragraph("• Authors: Parker N, Schneegurt M, Tu A-HT, Lister P, Forster BM", bul))
story.append(Paragraph("• Year: 2016", bul))
story.append(Paragraph("• Publisher: OpenStax (Houston, TX)", bul))
story.append(Paragraph("• URL: https://openstax.org/details/books/microbiology", bul))

story.append(sp(4))
story.append(Paragraph(B("In-text citation format (CSE Name-Year):"), h3))
story.append(Paragraph("• General fact: (Parker et al. 2016)", bul))
story.append(Paragraph("• Specific section: (Parker et al. 2016, §2.3)", bul))
story.append(Paragraph("• \"et al.\" is used for 3+ authors (only first author named)", bul))

story.append(sp(4))
story.append(Paragraph(B("Reference list entry (CSE Name-Year):"), h3))
story.append(Paragraph(
    "Parker N, Schneegurt M, Tu A-HT, Lister P, Forster BM. 2016. Microbiology. "
    "Houston (TX): OpenStax. Available from: https://openstax.org/details/books/microbiology", bod))
story.append(Paragraph(
    f"{B('Only ONE entry is needed')} for the entire textbook, even if multiple sections are cited "
    f"in-text. Different sections are distinguished by the §X.Y callout in the in-text cite.", bod))

story.append(sp(4))
story.append(Paragraph("⛔ NEVER cite — these are NOT allowed in lab reports:", warn))
story.append(Paragraph("• Popa lecture slides (used for studying, NOT for lab report citations)", bul))
story.append(Paragraph("• Tiny Earth Lab Manual (used as procedure reference, NOT for citations)", bul))
story.append(Paragraph("• BIO203A lab handouts / docx quiz forms", bul))
story.append(Paragraph("• Wikipedia, Google, web pages", bul))
story.append(Paragraph("• Journal articles (PubMed, ScienceDirect, etc.)", bul))
story.append(Paragraph("• AI sources (ChatGPT, Claude, Gemini)", bul))
story.append(Paragraph("• YouTube, blogs, social media, anything else not OpenStax", bul))

story.append(sp(6))
story.append(Paragraph(
    f"{B('If a fact in your report cannot be traced to a specific OpenStax section — '
       'rewrite the claim or remove it.')}", warn))

story.append(sp(6))
story.append(Paragraph("⛔ NO EDITORIAL PARAPHRASING:", warn))
story.append(Paragraph(
    "Every factual sentence in Introduction / Discussion / Conclusion must trace directly to "
    "specific OpenStax content. Do not write decorative descriptors not in the textbook "
    "(\"foundational instrument,\" \"primary tool,\" \"essential method\"). Do not write "
    "connector phrases that imply causation not in the source (\"therefore,\" \"consequently,\" "
    "\"thus the microscope is...\"). Procedure description (Materials and Methods) and own "
    "observations (Results) do NOT need citations — those are factual narration.", bod))

# ─── EXAMPLE REFERENCE BLOCK ──────────────────────────────────────────────────
story.append(Paragraph("Example References Section", h2))
story.append(Paragraph(
    f"At the end of your lab report, list ONE OpenStax entry only — even if you cite multiple "
    f"sections in-text. Section identification is handled by the (§X.Y) marker in the in-text cite.", bod))
story.append(sp(4))
story.append(tbl([
    ['References'],
    ['Parker N, Schneegurt M, Tu A-HT, Lister P, Forster BM. 2016. Microbiology. '
     'Houston (TX): OpenStax. Available from: https://openstax.org/details/books/microbiology'],
], [W]))
sp(8)

# ─── DELIVERABLES ─────────────────────────────────────────────────────────────
story.append(Paragraph("What to Submit", h1))
story.append(tbl([
    ['Deliverable', 'Format', 'Where', 'Purpose'],
    ['D2L Lab Quiz form', 'Filled-in .docx → upload', 'D2L Brightspace quiz', 'Bare data submission'],
    ['Traditional Lab Report', 'PDF in 8-section format above', 'D2L assignment dropbox', 'Graded report Popa wants'],
    ['Plate / culture photos', 'JPG or PNG', 'Embed in both', 'Required visual evidence'],
], [1.7 * inch, 1.6 * inch, 1.7 * inch, 2.0 * inch]))
sp(8)

# ─── QUICK CHECKLIST ──────────────────────────────────────────────────────────
story.append(Paragraph("Pre-Submission Checklist", h1))
story.append(Paragraph("Before submitting any lab report .docx, confirm:", bod))
story.append(Paragraph("☐ Title and Name on first page", bul))
story.append(Paragraph("☐ Scope statement (1–2 sentences) before Introduction", bul))
story.append(Paragraph("☐ Every factual claim in Introduction / Discussion / Conclusion has an OpenStax section cite", bul))
story.append(Paragraph("☐ NO Popa slide cites anywhere (slides are study aids, not citations)", bul))
story.append(Paragraph("☐ NO Tiny Earth manual cites anywhere", bul))
story.append(Paragraph("☐ NO lab handout / D2L docx cites anywhere", bul))
story.append(Paragraph("☐ Materials and Methods written in past tense, factual narration (no citations needed)", bul))
story.append(Paragraph("☐ Results section contains your own observations, calculations, photos (no citations needed for own data)", bul))
story.append(Paragraph("☐ Discussion ties results back to OpenStax content with explicit section cites", bul))
story.append(Paragraph("☐ References section contains ONLY OpenStax entries — nothing else", bul))
story.append(Paragraph("☐ No editorial connectors (\"therefore,\" \"consequently,\" \"thus...\") that aren't in the textbook", bul))
story.append(Paragraph("☐ No invented adjectives (\"foundational,\" \"primary tool,\" \"essential\") not in the textbook", bul))
story.append(Paragraph("☐ Every cite has been verified against source_text/chN_textbook_raw.txt", bul))

story.append(sp(10))
story.append(Paragraph(
    f"Source: NU Micro production rules — see NU_Micro_Study_Method.md and CLAUDE.md "
    f"(both in Dropbox\\Nu micro\\)",
    ParagraphStyle('FT', fontName='Helvetica-Oblique', fontSize=8,
                   alignment=TA_CENTER, textColor=colors.grey)))

doc.build(story)
print(f"Done -> {OUTPUT}")
