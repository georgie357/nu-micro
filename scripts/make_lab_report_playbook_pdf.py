# -*- coding: utf-8 -*-
"""Generate lab_report_playbook.pdf from lab_report_playbook.md using reportlab."""
import re
from pathlib import Path
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                 Table, TableStyle, ListFlowable, ListItem,
                                 PageBreak, KeepTogether)

MD  = Path(r"C:\Users\User\Dropbox\Nu micro\lab_report_playbook.md")
PDF = Path(r"C:\Users\User\Dropbox\Nu micro\lab_report_playbook.pdf")

styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=18, spaceAfter=10, textColor=colors.HexColor("#1a1a1a"))
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, spaceBefore=12, spaceAfter=6, textColor=colors.HexColor("#0b3d91"))
H3 = ParagraphStyle('H3', parent=styles['Heading3'], fontSize=12, spaceBefore=8, spaceAfter=4, textColor=colors.HexColor("#222222"))
BODY = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, leading=14, spaceAfter=4, alignment=TA_LEFT)
CODE = ParagraphStyle('Code', parent=styles['Code'], fontSize=9, leading=11, backColor=colors.HexColor("#f4f4f4"),
                       borderColor=colors.HexColor("#cccccc"), borderWidth=0.5, borderPadding=4, leftIndent=6, rightIndent=6)
RULE = ParagraphStyle('Rule', parent=BODY, textColor=colors.HexColor("#a00000"), fontName='Helvetica-Bold')

def md_inline(s):
    # Bold **text**
    s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
    # Italic *text* (after bold so ** doesn't conflict)
    s = re.sub(r'(?<![\*])\*([^*\n]+)\*(?![\*])', r'<i>\1</i>', s)
    # Inline code `code`
    s = re.sub(r'`([^`]+)`', r'<font face="Courier" backColor="#f4f4f4">\1</font>', s)
    return s

def parse_md_to_flowables(md_text):
    flow = []
    lines = md_text.split('\n')
    i = 0
    in_code = False
    code_buf = []
    in_table = False
    table_buf = []

    def flush_code():
        if code_buf:
            flow.append(Paragraph('<br/>'.join(code_buf), CODE))
            flow.append(Spacer(1, 6))
            code_buf.clear()

    def flush_table():
        if table_buf and len(table_buf) >= 2:
            rows = [[c.strip() for c in r.strip('|').split('|')] for r in table_buf if '|' in r and not re.match(r'^[\s\-\|:]+$', r)]
            if rows:
                tbl = Table(rows, hAlign='LEFT')
                tbl.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0b3d91")),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0,0), (-1,-1), 9),
                    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                    ('LEFTPADDING', (0,0), (-1,-1), 4),
                    ('RIGHTPADDING', (0,0), (-1,-1), 4),
                    ('TOPPADDING', (0,0), (-1,-1), 3),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
                ]))
                flow.append(tbl)
                flow.append(Spacer(1, 8))
        table_buf.clear()

    while i < len(lines):
        line = lines[i]

        if line.strip().startswith('```'):
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            i += 1; continue

        if in_code:
            code_buf.append(line.replace('<','&lt;').replace('>','&gt;').replace(' ','&nbsp;'))
            i += 1; continue

        if line.strip().startswith('|'):
            in_table = True
            table_buf.append(line)
            i += 1; continue
        elif in_table:
            flush_table()
            in_table = False

        if line.startswith('# '):
            flow.append(Paragraph(md_inline(line[2:].strip()), H1))
        elif line.startswith('## '):
            flow.append(Paragraph(md_inline(line[3:].strip()), H2))
        elif line.startswith('### '):
            flow.append(Paragraph(md_inline(line[4:].strip()), H3))
        elif line.startswith('---'):
            flow.append(Spacer(1, 4))
        elif line.startswith('- [ ] '):
            flow.append(Paragraph('☐ ' + md_inline(line[6:]), BODY))
        elif line.startswith('- ') or line.startswith('* '):
            flow.append(Paragraph('• ' + md_inline(line[2:]), BODY))
        elif re.match(r'^\d+\.\s', line):
            flow.append(Paragraph(md_inline(line), BODY))
        elif line.strip().startswith('🛑') or line.strip().startswith('⚠'):
            flow.append(Paragraph(md_inline(line.strip()), RULE))
        elif line.strip() == '':
            flow.append(Spacer(1, 4))
        else:
            flow.append(Paragraph(md_inline(line), BODY))
        i += 1

    flush_code()
    flush_table()
    return flow

def main():
    md_text = MD.read_text(encoding='utf-8')
    flowables = parse_md_to_flowables(md_text)
    doc = SimpleDocTemplate(str(PDF), pagesize=LETTER,
                            leftMargin=0.7*inch, rightMargin=0.7*inch,
                            topMargin=0.6*inch, bottomMargin=0.6*inch,
                            title="BIO203A Lab Report Playbook")
    doc.build(flowables)
    print(f"PDF written: {PDF}")

if __name__ == '__main__':
    main()
