# BIO203A Lab 6: Gram Staining — Traditional Lab Report (Popa STRICT v2)
# Author: George Vela
# References cite ONLY OpenStax Microbiology (Parker et al. 2016). CSE Name-Year style.
# NOTE: Image paths are placeholders. Save photos to:
#   C:\Users\User\Dropbox\Nu micro\lab reports\lab 6 gram bacillus.jpg
#   C:\Users\User\Dropbox\Nu micro\lab reports\lab 6 gram ecoli.jpg
# Then re-run this script.

import os
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\lab reports\BIO203A_Lab6_Traditional_Report.docx"

BACILLUS_IMG_PATHS = [
    r"C:\Users\User\Dropbox\Nu micro\lab reports\lab 6 gram bacillus.jpg",
    r"C:\Users\User\Dropbox\Nu micro\lab reports\lab 6 gram bacillus.JPG",
    r"C:\Users\User\Dropbox\Nu micro\lab reports\lab 6 gram bacillus.png",
    r"C:\Users\User\Dropbox\Nu micro\lab reports\lab 6 gram subtilis.jpg",
    r"C:\Users\User\Dropbox\Nu micro\lab reports\lab 6 gram subtilis.JPG",
]
ECOLI_IMG_PATHS = [
    r"C:\Users\User\Dropbox\Nu micro\lab reports\lab 6 gram ecoli.jpg",
    r"C:\Users\User\Dropbox\Nu micro\lab reports\lab 6 gram ecoli.JPG",
    r"C:\Users\User\Dropbox\Nu micro\lab reports\lab 6 gram ecoli.png",
    r"C:\Users\User\Dropbox\Nu micro\lab reports\lab 6 gram e.coli.jpg",
]
BACILLUS_IMG = next((p for p in BACILLUS_IMG_PATHS if os.path.exists(p)), None)
ECOLI_IMG = next((p for p in ECOLI_IMG_PATHS if os.path.exists(p)), None)

doc = Document()
style = doc.styles['Normal']
style.font.name = 'Times New Roman'
style.font.size = Pt(12)
style.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
style.paragraph_format.space_after = Pt(0)

for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)


def add_page_number(footer_para):
    footer_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = footer_para.add_run()
    fldChar1 = OxmlElement('w:fldChar'); fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText'); instrText.set(qn('xml:space'), 'preserve'); instrText.text = 'PAGE'
    fldChar2 = OxmlElement('w:fldChar'); fldChar2.set(qn('w:fldCharType'), 'end')
    run._r.append(fldChar1); run._r.append(instrText); run._r.append(fldChar2)


for section in doc.sections:
    add_page_number(section.footer.paragraphs[0])


def add_paragraph(text_runs, alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
                  first_indent=Inches(0.5), space_after=Pt(0)):
    p = doc.add_paragraph()
    p.alignment = alignment
    p.paragraph_format.first_line_indent = first_indent
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    p.paragraph_format.space_after = space_after
    for text, fmt in text_runs:
        run = p.add_run(text)
        run.font.name = 'Times New Roman'; run.font.size = Pt(fmt.get('size', 12))
        if fmt.get('bold'): run.bold = True
        if fmt.get('italic'): run.italic = True


def section_heading(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    p.paragraph_format.space_before = Pt(12); p.paragraph_format.space_after = Pt(0)
    run = p.add_run(text); run.bold = True
    run.font.name = 'Times New Roman'; run.font.size = Pt(12)


def subhead(text):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    p.paragraph_format.space_before = Pt(6)
    run = p.add_run(text); run.bold = True; run.italic = True
    run.font.name = 'Times New Roman'; run.font.size = Pt(12)


def add_caption(text_runs):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(12)
    for text, fmt in text_runs:
        run = p.add_run(text)
        run.font.name = 'Times New Roman'; run.font.size = Pt(11)
        if fmt.get('bold'): run.bold = True
        if fmt.get('italic', True): run.italic = True


def add_image(path, width_inches=4.5):
    if path and os.path.exists(path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(0)
        run = p.add_run()
        run.add_picture(path, width=Inches(width_inches))
    else:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        run = p.add_run("[Photo placeholder — save image to expected path and re-run script]")
        run.font.name = 'Times New Roman'; run.font.size = Pt(11); run.italic = True


# ════════════════════════════════════════════════════════════════════════════
# TITLE PAGE
# ════════════════════════════════════════════════════════════════════════════
for _ in range(4):
    doc.add_paragraph()

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
run = p_title.add_run("Lab 6: Gram Staining")
run.bold = True; run.font.name = 'Times New Roman'; run.font.size = Pt(16)

p_subtitle = doc.add_paragraph()
p_subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_subtitle.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
run = p_subtitle.add_run("Differential Gram Staining of Bacillus subtilis and Escherichia coli")
run.italic = True; run.font.name = 'Times New Roman'; run.font.size = Pt(13)

for _ in range(3):
    doc.add_paragraph()

for line in [
    "George Vela",
    "BIO203A — Microbiology Laboratory",
    "Spring 2026",
    "Instructor: Dr. Radu Popa",
    "National University, Los Angeles Campus",
    "",
    "Staining Sessions: May 7 and May 9, 2026",
    "Report Submitted: May 2026",
]:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    run = p.add_run(line)
    run.font.name = 'Times New Roman'; run.font.size = Pt(12)

doc.add_page_break()

# ════════════════════════════════════════════════════════════════════════════
# SCOPE
# ════════════════════════════════════════════════════════════════════════════
section_heading("Scope")
add_paragraph([
    ("This laboratory exercise performed the Gram stain — the most widely used "
     "differential staining procedure in clinical microbiology — on two bacterial "
     "species with known but opposite cell-wall types: ", {}),
    ("Bacillus subtilis", {'italic': True}),
    (" (expected gram-positive) and ", {}),
    ("Escherichia coli", {'italic': True}),
    (" (expected gram-negative). The objective was to apply the four-step Gram "
     "stain procedure correctly, to observe the resulting differential staining at "
     "oil-immersion magnification, and to confirm the Gram classification of each "
     "organism by direct visualization.", {}),
])

# ════════════════════════════════════════════════════════════════════════════
# INTRODUCTION
# ════════════════════════════════════════════════════════════════════════════
section_heading("Introduction")

add_paragraph([
    ("The Gram stain is a differential staining procedure developed by the Danish "
     "microbiologist Hans Christian Gram in 1884 to distinguish between bacteria "
     "with different types of cell walls. It remains one of the most frequently "
     "used staining techniques in microbiology (Parker et al. 2016, §2.4). Unlike "
     "simple stains, which use a single basic dye to reveal cell shape and "
     "arrangement, differential stains use multiple reagents to give different "
     "groups of bacteria different colors so that they can be distinguished within "
     "the same preparation (Parker et al. 2016, §2.4).", {}),
])

add_paragraph([
    ("The Gram stain procedure consists of four reagents applied in sequence "
     "(Parker et al. 2016, §2.4). First, crystal violet, a primary stain, is "
     "applied to a heat-fixed smear, giving all of the cells a purple color. "
     "Second, Gram's iodine, a mordant, is added; the iodine acts as a trapping "
     "agent that complexes with crystal violet, forming a crystal-violet–iodine "
     "complex that clumps and stays contained in thick layers of peptidoglycan in "
     "the cell wall. Third, a decolorizing agent (ethanol or an acetone/ethanol "
     "solution) is added: cells with thick peptidoglycan retain the crystal "
     "violet–iodine complex and remain purple, whereas cells with thinner "
     "peptidoglycan are decolorized and become colorless. Fourth, a secondary "
     "counterstain — usually safranin — stains the decolorized cells pink while "
     "remaining less noticeable on cells that still contain the crystal violet "
     "dye (Parker et al. 2016, §2.4).", {}),
])

add_paragraph([
    ("The purple, crystal-violet–stained cells are referred to as gram-positive "
     "cells, while the red or pink, safranin-stained cells are gram-negative "
     "(Parker et al. 2016, §2.4). The difference reflects the underlying cell-wall "
     "architecture: gram-positive cell walls have a thick peptidoglycan layer "
     "external to the plasma membrane that retains the crystal-violet–iodine "
     "complex during decolorization, while gram-negative cells have a much thinner "
     "peptidoglycan layer covered by an outer membrane and lose the complex "
     "during the alcohol wash. The two organisms used in this exercise are known "
     "examples of each type: ", {}),
    ("Bacillus", {'italic': True}),
    (" species are gram-positive bacilli (Parker et al. 2016, §4.4), and ", {}),
    ("Escherichia coli", {'italic': True}),
    (" is a gram-negative member of the family Enterobacteriaceae within the "
     "Gammaproteobacteria (Parker et al. 2016, §4.4).", {}),
])

# ════════════════════════════════════════════════════════════════════════════
# MATERIALS AND METHODS
# ════════════════════════════════════════════════════════════════════════════
section_heading("Materials and Methods")

subhead("Materials")
for item in [
    "Bacterial cultures: Bacillus subtilis and Escherichia coli (from previous laboratory exercise)",
    "Clean glass microscope slides",
    "Distilled water in a dropper",
    "Sterile inoculating loops",
    "Bunsen burner with striker",
    "Clothespin (to hold slide during heat fixation)",
    "Crystal violet (primary stain)",
    "Gram's iodine (mordant)",
    "95% ethanol or acetone/ethanol (decolorizing agent)",
    "Safranin (counterstain)",
    "Staining tray, wash bottle of water, and waste beaker",
    "Bibulous paper or paper towel for blotting",
    "Compound brightfield microscope with 100× oil immersion objective",
    "Type-A immersion oil",
    "Lens paper",
]:
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.25)
    run = p.add_run(f"• {item}")
    run.font.name = 'Times New Roman'; run.font.size = Pt(12)

subhead("Methods")

add_paragraph([
    ("On May 7, 2026, separate smears were prepared on labeled glass slides for ", {}),
    ("B. subtilis", {'italic': True}),
    (" and ", {}),
    ("E. coli", {'italic': True}),
    (". For each smear, a loopful of culture (with one drop of distilled water "
     "added for slants) was spread evenly across a marked area of the slide, "
     "allowed to air-dry, and then heat-fixed by passing the slide through the "
     "outer cone of the Bunsen flame two to three times with the smear side up.", {}),
])

add_paragraph([
    ("Each heat-fixed smear was placed on the staining tray and the four-step "
     "Gram stain procedure was applied. Crystal violet was added to cover the "
     "smear and left for one minute, then rinsed gently with distilled water. "
     "Gram's iodine was added next and left for one minute, then rinsed with "
     "distilled water. The slide was tilted and 95% ethanol was applied "
     "drop-by-drop until the solvent ran clear from the smear (typically "
     "10–20 seconds), and the slide was immediately rinsed with water to halt "
     "decolorization. Safranin was added as a counterstain and left for one "
     "minute, then rinsed and blotted dry with bibulous paper.", {}),
])

add_paragraph([
    ("Additional smears were prepared and stained during the second laboratory "
     "session on May 9, 2026, to allow time for re-staining if the first set of "
     "slides did not produce clean results. Stained slides were observed using "
     "the compound brightfield microscope. Each slide was first located at 4× "
     "and then brought into focus at 10× and 40× using the parfocal objective "
     "progression. A drop of immersion oil was applied directly to the smear and "
     "the 100× oil immersion objective was rotated into the oil for final "
     "observation. Representative fields were photographed through the ocular.", {}),
])

# ════════════════════════════════════════════════════════════════════════════
# RESULTS AND DISCUSSION
# ════════════════════════════════════════════════════════════════════════════
doc.add_page_break()
section_heading("Results and Discussion")

add_paragraph([
    ("Both stained slides produced clear differential staining at 1000× total "
     "magnification (Figures 1 and 2). The two organisms gave the opposite Gram "
     "reactions expected from their published cell-wall classifications: ", {}),
    ("B. subtilis", {'italic': True}),
    (" retained the crystal-violet stain and appeared purple, while ", {}),
    ("E. coli", {'italic': True}),
    (" was decolorized by the alcohol step and was counterstained pink by the "
     "safranin. Observation details are summarized in Table 1.", {}),
])

subhead("Bacillus subtilis")
add_image(BACILLUS_IMG, width_inches=4.5)
add_caption([
    ("Figure 1. ", {'bold': True, 'italic': True}),
    ("Gram stain of ", {'italic': True}),
    ("Bacillus subtilis", {'italic': True}),
    (" at 1000× total magnification (100× oil immersion × 10× ocular). The cells "
     "appear purple, indicating retention of the crystal-violet–iodine complex "
     "after alcohol decolorization, and confirming the gram-positive "
     "classification expected for this organism (Parker et al. 2016, §2.4 and §4.4).",
     {'italic': True}),
])

subhead("Escherichia coli")
add_image(ECOLI_IMG, width_inches=4.5)
add_caption([
    ("Figure 2. ", {'bold': True, 'italic': True}),
    ("Gram stain of ", {'italic': True}),
    ("Escherichia coli", {'italic': True}),
    (" at 1000× total magnification. The cells appear pink, indicating loss of "
     "the crystal-violet–iodine complex during alcohol decolorization and uptake "
     "of the safranin counterstain, confirming the gram-negative classification "
     "expected for this organism (Parker et al. 2016, §2.4 and §4.4).", {'italic': True}),
])

subhead("Summary of Gram Reactions")

table = doc.add_table(rows=3, cols=5)
table.style = 'Table Grid'
table.alignment = WD_ALIGN_PARAGRAPH.CENTER

headers = ['Organism', 'Final Color', 'Gram Reaction', 'Cell Shape', 'Arrangement']
for i, h in enumerate(headers):
    cell = table.rows[0].cells[i]; cell.text = ''
    p = cell.paragraphs[0]; p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    run = p.add_run(h); run.bold = True; run.font.name = 'Times New Roman'; run.font.size = Pt(11)

rows_data = [
    ['Bacillus subtilis', 'Purple', 'Gram-positive (+)', 'Bacillus (rod)', 'Singles and short chains'],
    ['Escherichia coli', 'Pink', 'Gram-negative (−)', 'Bacillus (rod)', 'Singles, scattered'],
]
for i, row in enumerate(rows_data, start=1):
    for j, val in enumerate(row):
        cell = table.rows[i].cells[j]; cell.text = ''
        p = cell.paragraphs[0]; p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        run = p.add_run(val); run.font.name = 'Times New Roman'; run.font.size = Pt(11)
        if j == 0:
            run.italic = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(12)
run = p.add_run("Table 1. ")
run.bold = True; run.italic = True; run.font.name = 'Times New Roman'; run.font.size = Pt(11)
run = p.add_run("Summary of Gram stain observations.")
run.italic = True; run.font.name = 'Times New Roman'; run.font.size = Pt(11)

subhead("Interpretation")
add_paragraph([
    ("The purple final color of ", {}),
    ("B. subtilis", {'italic': True}),
    (" is consistent with the thick peptidoglycan cell wall characteristic of "
     "gram-positive bacteria: the thick peptidoglycan layer retains the "
     "crystal-violet–iodine complex during the alcohol decolorization step, so "
     "the cells remain purple at the end of the procedure (Parker et al. 2016, "
     "§2.4). Members of the genus ", {}),
    ("Bacillus", {'italic': True}),
    (" are described in OpenStax as large gram-positive bacilli that include "
     "aerobes or facultative anaerobes and form endospores (Parker et al. 2016, "
     "§4.4), and the result of this Gram stain is consistent with that "
     "description.", {}),
])

add_paragraph([
    ("The pink final color of ", {}),
    ("E. coli", {'italic': True}),
    (" is consistent with the thin peptidoglycan cell wall and outer membrane "
     "characteristic of gram-negative bacteria. During alcohol decolorization, "
     "the crystal-violet–iodine complex is more easily washed out of cells with "
     "thinner peptidoglycan, so they become colorless and then take up the "
     "safranin counterstain to appear pink at the end of the procedure (Parker "
     "et al. 2016, §2.4). ", {}),
    ("E. coli", {'italic': True}),
    (" is a member of the family Enterobacteriaceae within the "
     "Gammaproteobacteria, a class of gram-negative bacteria (Parker et al. 2016, "
     "§4.4), and the observed Gram reaction confirms that classification.", {}),
])

add_paragraph([
    ("The successful production of contrasting Gram reactions on the two slides "
     "indicates that the four-step procedure — primary stain, mordant, "
     "decolorizer, counterstain — was applied within appropriate time windows. "
     "Over-decolorization (excess alcohol exposure) can cause gram-positive cells "
     "to lose the crystal-violet complex and incorrectly appear pink, and "
     "under-decolorization can cause gram-negative cells to remain purple; "
     "neither error occurred in the slides photographed here.", {}),
])

# ════════════════════════════════════════════════════════════════════════════
# CONCLUSION
# ════════════════════════════════════════════════════════════════════════════
section_heading("Conclusion")

add_paragraph([
    ("Differential Gram staining of ", {}),
    ("Bacillus subtilis", {'italic': True}),
    (" and ", {}),
    ("Escherichia coli", {'italic': True}),
    (" produced the expected contrasting Gram reactions: ", {}),
    ("B. subtilis", {'italic': True}),
    (" cells stained purple (gram-positive), and ", {}),
    ("E. coli", {'italic': True}),
    (" cells stained pink (gram-negative). The results are consistent with the "
     "cell-wall classifications of each organism in OpenStax §4.4 and confirm "
     "that the four-step Gram stain procedure described in §2.4 was carried out "
     "correctly.", {}),
])

add_paragraph([
    ("The Gram stain is a foundational tool for the rapid differential "
     "classification of bacterial isolates and underlies subsequent diagnostic "
     "and identification work in clinical microbiology. The same procedure will "
     "be applied to the library-plate isolates from the soil sample in later "
     "exercises of the Antibiotic Discovery Project to begin characterizing the "
     "cell-wall type of each candidate antimicrobial producer.", {}),
])

# ════════════════════════════════════════════════════════════════════════════
# REFERENCES
# ════════════════════════════════════════════════════════════════════════════
section_heading("References")


def add_reference(text_runs):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.5)
    p.paragraph_format.space_after = Pt(0)
    for text, fmt in text_runs:
        run = p.add_run(text)
        run.font.name = 'Times New Roman'; run.font.size = Pt(12)


add_reference([
    ("Parker N, Schneegurt M, Tu A-HT, Lister P, Forster BM. 2016. Microbiology. "
     "Houston (TX): OpenStax. Available from: "
     "https://openstax.org/details/books/microbiology", {}),
])

doc.save(OUTPUT)
print(f"Done -> {OUTPUT}")
print(f"Bacillus photo: {'EMBEDDED' if BACILLUS_IMG else 'MISSING (placeholder)'}")
if BACILLUS_IMG: print(f"  {BACILLUS_IMG}")
print(f"E. coli photo:  {'EMBEDDED' if ECOLI_IMG else 'MISSING (placeholder)'}")
if ECOLI_IMG: print(f"  {ECOLI_IMG}")
