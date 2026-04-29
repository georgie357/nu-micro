# BIO203 Ch.1 & Ch.2 - Multiple Choice Questions - Version 3 (Highest Yield)
# 55 questions. New trap-focused questions added. All cited to Popa slides + OpenStax.

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\chapter 1 and 2\BIO203_Ch1_Ch2_MC_Questions_v3.pdf"

h1  = ParagraphStyle('H1', fontName='Helvetica-Bold',   fontSize=16, spaceAfter=6,  textColor=colors.HexColor('#1a1a6e'))
h2  = ParagraphStyle('H2', fontName='Helvetica-Bold',   fontSize=12, spaceAfter=4,  spaceBefore=10, textColor=colors.HexColor('#1a1a6e'))
qst = ParagraphStyle('QS', fontName='Helvetica-Bold',   fontSize=9,  spaceAfter=2,  leading=13)
opt = ParagraphStyle('OP', fontName='Helvetica',         fontSize=9,  spaceAfter=1,  leading=12, leftIndent=18)
ans = ParagraphStyle('AN', fontName='Helvetica-Bold',   fontSize=8,  spaceAfter=1,  textColor=colors.HexColor('#0000aa'))
cit = ParagraphStyle('CT', fontName='Helvetica-Oblique', fontSize=7.5,spaceAfter=6,  textColor=colors.HexColor('#555555'), leftIndent=18)

cell_body = ParagraphStyle('cb', fontName='Helvetica',      fontSize=8, leading=11, spaceAfter=0)
cell_bold = ParagraphStyle('cB', fontName='Helvetica-Bold', fontSize=8, leading=11, spaceAfter=0)

def _cell(val, hdr=False):
    if isinstance(val, str):
        return Paragraph(val.replace('\n', '<br/>'), cell_bold if hdr else cell_body)
    return val

def tbl(data, widths):
    wrapped = [[_cell(c, hdr=(i == 0)) for c in row] for i, row in enumerate(data)]
    t = Table(wrapped, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('GRID',           (0,0), (-1,-1), 0.5, colors.black),
        ('BACKGROUND',     (0,0), (-1, 0), colors.Color(0.82, 0.82, 0.82)),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.Color(0.95, 0.95, 0.95)]),
        ('TOPPADDING',     (0,0), (-1,-1), 4),
        ('BOTTOMPADDING',  (0,0), (-1,-1), 4),
        ('LEFTPADDING',    (0,0), (-1,-1), 4),
        ('RIGHTPADDING',   (0,0), (-1,-1), 4),
        ('VALIGN',         (0,0), (-1,-1), 'TOP'),
    ]))
    return t

def sp(n=6): return Spacer(1, n)

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                        leftMargin=0.75*inch, rightMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)
W = 7.0 * inch
story = []

story += [
    Paragraph("BIO203 Microbiology — National University",
              ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=18, alignment=TA_CENTER, textColor=colors.HexColor('#1a1a6e'))),
    sp(4),
    Paragraph("Chapters 1 &amp; 2 — 55 Multiple Choice Questions — Version 3 (Highest Yield)",
              ParagraphStyle('TS', fontName='Helvetica-Bold', fontSize=13, alignment=TA_CENTER)),
    sp(3),
    Paragraph("Source: Popa lecture slides + OpenStax Microbiology (2016) | Answer key included | Trap questions flagged",
              ParagraphStyle('TC', fontName='Helvetica-Oblique', fontSize=9, alignment=TA_CENTER, textColor=colors.grey)),
    HRFlowable(width=W, thickness=2, color=colors.HexColor('#1a1a6e')),
    sp(8),
]

# Format: (number, question_text, [A,B,C,D], correct_letter, "citation")
questions = [
    # ── CHAPTER 1 (Q1–35) ───────────────────────────────────────────────────
    (1,
     "Which statement BEST defines microbiology?",
     ["A. The study of viruses only",
      "B. The science studying organisms too small to see with the unaided eye",
      "C. The study of chemistry within living cells",
      "D. The branch of biology focused on genetics"],
     "B", "Popa slide 3; OpenStax 1.1"),

    (2,
     "Approximately what minimum size must an object be to be visible to the naked eye?",
     ["A. 1 µm", "B. 10 µm", "C. 100 µm", "D. 1 mm"],
     "C", "Popa slide 3; OpenStax 1.1"),

    (3,
     "A typical bacterium measures approximately:",
     ["A. 100 nm", "B. 1 µm", "C. 10 µm", "D. 100 µm"],
     "B", "Popa slide 3; OpenStax 1.1"),

    (4,
     "Marcus Terentius Varro (116–27 BC) is notable in microbiology history because he:",
     ["A. First described live microorganisms under a microscope",
      "B. Proposed that invisible 'minute creatures' cause disease — 1,700 years before germ theory was proven",
      "C. Developed the first vaccine",
      "D. Established Koch's postulates"],
     "B", "Popa slide 5; OpenStax 1.2"),

    (5,
     "Thucydides (460–395 BC) is significant in medical history because he made the first recorded observation of:",
     ["A. Spontaneous generation of microorganisms",
      "B. Germ theory of disease",
      "C. Immunity — survivors of the Athenian plague did not get re-infected",
      "D. Differential diagnosis between measles and smallpox"],
     "C", "Popa slide 5; OpenStax 1.2"),

    (6,
     "Anton van Leeuwenhoek described live 'animalcules' from pond water and dental scrapings approximately in:",
     ["A. 1543", "B. 1665", "C. 1675", "D. 1796"],
     "C", "Popa slide 6; OpenStax 1.2"),

    (7,
     "Robert Hooke's 1665 publication Micrographia is significant because it:",
     ["A. First described bacteria in soil",
      "B. Introduced the term 'cell' and described cells in cork using a compound microscope",
      "C. Proved that microbes cause fermentation",
      "D. Established germ theory of disease"],
     "B", "OpenStax 1.2; Popa slide 6"),

    (8,
     "What was the KEY difference between Hooke's and Leeuwenhoek's microscopic observations?",
     ["A. Hooke used a simple microscope; Leeuwenhoek used a compound microscope",
      "B. Hooke observed DEAD cell walls in cork; Leeuwenhoek observed LIVING microorganisms",
      "C. Hooke observed bacteria; Leeuwenhoek observed plant cells",
      "D. Hooke worked in Germany; Leeuwenhoek worked in France"],
     "B", "Popa slides 6–7; OpenStax 1.2"),

    (9,
     "Regarding Zacharias Janssen and the compound microscope, which statement is most accurate?",
     ["A. Janssen definitively invented the compound microscope in 1590",
      "B. Janssen's contribution is widely credited with no competing claims",
      "C. Evidence is inconclusive — he was secretive, never published, and neighbor Lippershey built similar instruments",
      "D. Janssen built the first electron microscope"],
     "C", "Popa slide 6; OpenStax 1.2"),

    (10,
     "Louis Pasteur's swan-neck flask experiment definitively disproved:",
     ["A. Germ theory of disease", "B. Koch's postulates",
      "C. Spontaneous generation", "D. The concept of immunity"],
     "C", "Popa slide 8; OpenStax 1.2"),

    (11,
     "Pasteurization involves:",
     ["A. Sterilizing food by boiling for 30 minutes",
      "B. Application of high heat for a short time to reduce microbial load",
      "C. Adding preservative chemicals to food",
      "D. Freezing food to kill pathogens"],
     "B", "Popa slide 8; OpenStax 1.2"),

    (12,
     "Which of the following is NOT one of Pasteur's contributions to microbiology?",
     ["A. Disproved spontaneous generation",
      "B. Proved microbes cause fermentation",
      "C. First experimental proof that ONE specific microbe causes ONE specific disease",
      "D. Invented pasteurization"],
     "C", "Popa slide 8; OpenStax 1.2 — C is Koch's contribution (anthrax 1876)"),

    (13,
     "Robert Koch proved that Bacillus anthracis causes anthrax in:",
     ["A. 1857", "B. 1876", "C. 1884", "D. 1928"],
     "B", "Popa slide 9; OpenStax 1.2"),

    (14,
     "Koch's postulates are a set of experimental criteria used to:",
     ["A. Classify bacteria by Gram staining",
      "B. Prove that a specific microorganism causes a specific disease",
      "C. Determine antibiotic susceptibility",
      "D. Establish the three-domain classification system"],
     "B", "Popa slide 9; OpenStax 1.2"),

    (15,
     "Solid agar as a culture medium was the idea of:",
     ["A. Robert Koch", "B. Louis Pasteur",
      "C. Fanny Hesse", "D. Alexander Fleming"],
     "C", "Popa slide 9; OpenStax 1.2"),

    (16,
     "Edward Jenner's vaccine discovery was based on the observation that:",
     ["A. Smallpox fluid directly protected against cowpox",
      "B. Dairymaids who had mild cowpox infections were protected from smallpox",
      "C. Children vaccinated with cowpox also became immune to measles",
      "D. Smallpox survivors could not be reinfected with cowpox"],
     "B", "Popa slide 7; OpenStax 1.2"),

    (17,
     "Paul Ehrlich's 'magic bullet' concept refers to:",
     ["A. A targeted missile delivery system for vaccines",
      "B. A drug with selective toxicity — harmful to the pathogen but not the host",
      "C. The use of radiation to kill bacteria",
      "D. An antibiotic derived from Penicillium mold"],
     "B", "Popa slide 11; OpenStax 1.2"),

    (18,
     "Ehrlich's drug Salvarsan (1910) was used to treat:",
     ["A. Anthrax", "B. Tuberculosis", "C. Syphilis", "D. Smallpox"],
     "C", "Popa slide 11; OpenStax 1.2"),

    (19,
     "Alexander Fleming discovered penicillin when he noticed:",
     ["A. A clear zone around Penicillium mold on a Staphylococcus plate left open accidentally",
      "B. Mold growing in a patient's wound prevented infection",
      "C. Bread mold killed bacteria in broth cultures",
      "D. Sulfa drugs inhibited mold growth"],
     "A", "Popa slide 12; OpenStax 1.2"),

    (20,
     "Dr. Sarah Voureka is mentioned specifically by Popa in connection with:",
     ["A. Fanny Hesse and the invention of agar plates",
      "B. The discovery of penicillin alongside Alexander Fleming",
      "C. Edward Jenner's smallpox vaccine trials",
      "D. The development of Koch's postulates"],
     "B", "Popa slides 12–13"),

    (21,
     "Carolus Linnaeus established the system of binomial nomenclature in:",
     ["A. 1543", "B. 1665", "C. 1758", "D. 1866"],
     "C", "Popa slide 10; OpenStax 1.3"),

    (22,
     "In binomial nomenclature, which rule is correct?",
     ["A. Both genus and specific epithet are capitalized",
      "B. Genus is capitalized; specific epithet is lowercase; both are italicized",
      "C. Only the specific epithet is italicized",
      "D. The genus may be written in any font when handwritten"],
     "B", "Popa slide 19; OpenStax 1.3"),

    (23,
     "Carl Woese and George Fox established the three-domain system based on sequences of:",
     ["A. DNA polymerase", "B. 16S/18S ribosomal RNA",
      "C. ATP synthase", "D. Cell wall peptidoglycan"],
     "B", "Popa slide 17; OpenStax 1.3"),

    (24,
     "Which is the CORRECT order from most to least inclusive in biological classification?",
     ["A. Species → Genus → Family → Order → Class → Phylum → Kingdom → Domain",
      "B. Domain → Kingdom → Phylum → Class → Order → Family → Genus → Species",
      "C. Domain → Phylum → Kingdom → Class → Order → Family → Genus → Species",
      "D. Kingdom → Domain → Phylum → Class → Order → Family → Genus → Species"],
     "B", "Popa slide 10; OpenStax 1.3"),

    (25,
     "Archaea differ from Bacteria in that Archaea:",
     ["A. Are eukaryotic",
      "B. Have peptidoglycan cell walls",
      "C. Do NOT have peptidoglycan cell walls",
      "D. Always cause human disease"],
     "C", "Popa slide 21; OpenStax 1.3"),

    (26,
     "Which group includes methanogens, extreme halophiles, and extreme thermophiles?",
     ["A. Bacteria", "B. Fungi", "C. Archaea", "D. Protozoa"],
     "C", "Popa slide 21; OpenStax 1.3"),

    (27,
     "The cell walls of FUNGI are composed of:",
     ["A. Peptidoglycan", "B. Cellulose", "C. Chitin", "D. Murein"],
     "C", "Popa slide 25; OpenStax 1.3"),

    (28,
     "Algae are BEST characterized as:",
     ["A. Chitin cell walls and heterotrophic nutrition",
      "B. Cellulose cell walls, photosynthetic, and NOT pathogenic",
      "C. No cell walls, motile by pseudopods",
      "D. Peptidoglycan cell walls, binary fission"],
     "B", "Popa slide 23; OpenStax 1.3"),

    (29,
     "Viruses differ from all other microorganisms in that they:",
     ["A. Contain both DNA and RNA",
      "B. Have a peptidoglycan protein coat",
      "C. Are acellular and can only replicate inside a living host cell",
      "D. Reproduce by binary fission"],
     "C", "Popa slide 27; OpenStax 1.3"),

    (30,
     "Prions are infectious agents consisting of:",
     ["A. Single-stranded RNA only",
      "B. Double-stranded DNA in a lipid envelope",
      "C. Misfolded proteins with NO nucleic acid",
      "D. Small circular DNA plasmids"],
     "C", "Popa slide 28; OpenStax 1.3"),

    (31,
     "Helminths are studied in microbiology primarily because:",
     ["A. They are acellular pathogens smaller than bacteria",
      "B. Their eggs and larval stages are microscopic",
      "C. They lack a nucleus and are prokaryotic",
      "D. They reproduce inside host cells like viruses"],
     "B", "Popa slide 26; OpenStax 1.3"),

    (32,
     "Stanley Prusiner received the 1998 Nobel Prize for his work on:",
     ["A. Discovery of penicillin",
      "B. Ribosomal RNA sequencing and the three-domain system",
      "C. Prions as proteinaceous infectious particles",
      "D. CRISPR gene editing"],
     "C", "Popa slide 28; OpenStax 1.3"),

    (33,
     "Which domain contains organisms that are prokaryotic but do NOT have peptidoglycan cell walls and are NOT known human pathogens?",
     ["A. Bacteria", "B. Archaea", "C. Eukarya", "D. Protista"],
     "B", "Popa slides 17–18; OpenStax 1.3"),

    (34,
     "CRISPR gene editing technology is based on:",
     ["A. Artificial synthetic chemistry developed in the 1980s",
      "B. Normal bacterial immune processes",
      "C. Protein denaturation mechanisms",
      "D. Viral replication pathways"],
     "B", "Popa slide 16; OpenStax 1.1"),

    (35,
     "Which scientist first clinically distinguished measles from smallpox?",
     ["A. Ibn Sina (Avicenna)", "B. Hippocrates",
      "C. al-Razi (Rhazes)", "D. Thucydides"],
     "C", "Popa slide 5; OpenStax 1.2"),

    # ══ CHAPTER 2 (Q36–55) ══════════════════════════════════════════════════
    (36,
     "The distance between one wave peak and the next is defined as the:",
     ["A. Amplitude", "B. Frequency", "C. Wavelength", "D. Refractive index"],
     "C", "Popa slide 4; OpenStax 2.1"),

    (37,
     "Regarding electromagnetic radiation, which statement is CORRECT?",
     ["A. Longer wavelength = higher energy",
      "B. Shorter wavelength = higher energy",
      "C. All wavelengths have equal energy",
      "D. Wavelength has no relationship to energy"],
     "B", "Popa slide 7; OpenStax 2.1"),

    (38,
     "Immersion oil is used with the 100× objective primarily to:",
     ["A. Increase magnification above 1000×",
      "B. Prevent refraction by matching the refractive index of glass, improving resolution",
      "C. Stain the specimen to make cells more visible",
      "D. Cool the objective during extended use"],
     "B", "Popa slide 6; OpenStax 2.2"),

    (39,
     "Resolution is defined as:",
     ["A. The ability of a lens to enlarge an image",
      "B. The ability of a lens system to distinguish two adjacent points as separate",
      "C. Difference in light intensity between specimen and background",
      "D. Speed at which light passes through a medium"],
     "B", "Popa slide 8; OpenStax 2.1"),

    (40,
     "Which gives the correct resolution limits from WORST to BEST?",
     ["A. Human eye → Light microscope → TEM",
      "B. TEM → Light microscope → Human eye",
      "C. Light microscope → TEM → Human eye",
      "D. Human eye → TEM → Light microscope"],
     "A", "Popa slides 16–18; OpenStax 2.1 — Human eye ~200 µm; LM ~200 nm; TEM ~2.5 nm"),

    (41,
     "In a brightfield microscope using a 10× ocular and 40× objective, total magnification is:",
     ["A. 40×", "B. 50×", "C. 400×", "D. 4000×"],
     "C", "Popa slide 9; OpenStax 2.2"),

    (42,
     "A darkfield microscope is particularly useful for visualizing:",
     ["A. Stained bacteria on a light background",
      "B. Treponema pallidum (syphilis spirochetes) — very thin and difficult to stain",
      "C. Endospores inside Bacillus cells",
      "D. Acid-fast Mycobacterium tuberculosis"],
     "B", "Popa slide 11; OpenStax 2.2"),

    (43,
     "Phase-contrast microscopy is most useful for:",
     ["A. Staining intracellular pathogens with fluorescent antibodies",
      "B. Imaging live unstained cells and visualizing internal structures without killing the organism",
      "C. Imaging the surface of bacteria at high magnification",
      "D. Detecting surface antigens on bacterial cells"],
     "B", "Popa slide 12; OpenStax 2.2"),

    (44,
     "Fluorescence microscopy is used to detect MRSA and Legionella because:",
     ["A. These organisms are autofluorescent without any staining",
      "B. Fluorochrome-labeled antibodies (DFA or IFA) bind specifically to the organism",
      "C. UV light kills non-target bacteria, leaving only the pathogen visible",
      "D. These organisms emit UV light when alive"],
     "B", "Popa slide 13; OpenStax 2.2"),

    (45,
     "Transmission electron microscopy (TEM) differs from SEM in that TEM:",
     ["A. Scans the surface of specimens with secondary electrons",
      "B. Produces 3D surface images",
      "C. Passes electrons through ultrathin sections to reveal INTERNAL structures",
      "D. Has lower resolution (20 nm) than SEM"],
     "C", "Popa slides 16–18; OpenStax 2.3"),

    (46,
     "Before viewing under SEM, specimens are typically coated with a thin layer of:",
     ["A. Immersion oil", "B. India ink",
      "C. Uranyl acetate", "D. Gold or gold-palladium alloy"],
     "D", "Popa slide 17; OpenStax 2.3"),

    (47,
     "In Gram staining, the mordant (Gram's iodine) functions to:",
     ["A. Kill all bacteria to prevent cross-contamination",
      "B. Form a Crystal violet-iodine complex that is large enough to be trapped in thick peptidoglycan",
      "C. Decolorize Gram-negative bacteria",
      "D. Counterstain Gram-negative cells pink"],
     "B", "Popa slide 26; OpenStax 2.4"),

    (48,
     "After the alcohol/acetone decolorization step in Gram staining, Gram-positive cells appear:",
     ["A. Pink, because safranin has been applied",
      "B. Colorless, because the thin wall cannot retain crystal violet",
      "C. Purple, because thick peptidoglycan RETAINS the crystal violet-iodine complex",
      "D. Green, because malachite green was the primary stain"],
     "C", "Popa slide 26; OpenStax 2.4"),

    (49,
     "The acid-fast stain is used primarily to identify organisms of the genus:",
     ["A. Bacillus and Clostridium",
      "B. Mycobacterium and Nocardia",
      "C. Cryptococcus and Klebsiella",
      "D. Treponema and Borrelia"],
     "B", "Popa slide 28; OpenStax 2.4"),

    (50,
     "In the endospore stain (Schaeffer-Fulton), the PRIMARY stain applied with steam is:",
     ["A. Crystal violet", "B. Safranin",
      "C. Malachite green", "D. Carbolfuchsin"],
     "C", "Popa slide 31; OpenStax 2.4"),

    (51,
     "Capsule staining uses a negative stain (India ink) because:",
     ["A. The capsule absorbs basic dyes strongly",
      "B. The capsule is positively charged and repels acidic dye",
      "C. The capsule resists staining, so the background is stained instead",
      "D. Capsules only fluoresce under UV light"],
     "C", "Popa slide 30; OpenStax 2.4"),

    (52,
     "Flagella staining requires a mordant because:",
     ["A. Flagella are negatively charged and repel all basic dyes",
      "B. Flagella (~20 nm) are too thin to see without the mordant thickening them",
      "C. Flagella are encased in a waxy capsule that resists staining",
      "D. The mordant dissolves the cell wall to expose flagella attachment points"],
     "B", "Popa slide 32; OpenStax 2.4"),

    (53,
     "A simple stain using a single basic dye allows you to determine all of the following EXCEPT:",
     ["A. Cell shape (coccus, bacillus, spirillum)",
      "B. Cell arrangement (singles, pairs, chains, tetrads)",
      "C. Whether an organism is Gram-positive or Gram-negative",
      "D. Approximate cell size"],
     "C", "Popa slides 23–24; OpenStax 2.4"),

    (54,
     "TRAP QUESTION: Over-decolorization during Gram staining would cause which error?",
     ["A. Gram-negative bacteria appear purple",
      "B. Gram-positive bacteria appear pink (falsely Gram-negative result)",
      "C. All bacteria lose all staining and appear colorless",
      "D. The endospores stain red instead of green"],
     "B", "Popa slide 26 — common lab error"),

    (55,
     "Which microscope type is described as similar to a 'CT scan of cells' because it optically sections thick specimens?",
     ["A. Phase-contrast", "B. DIC (Nomarski)",
      "C. Confocal laser scanning", "D. Two-photon"],
     "C", "Popa slide 14; OpenStax 2.2"),
]

# ── Print questions ─────────────────────────────────────────────────────────
ch1_done = False
ch2_done = False

for (num, qtext, opts, correct, citation) in questions:
    if num == 1 and not ch1_done:
        story.append(Paragraph("CHAPTER 1 QUESTIONS (Q1–Q35)", h2))
        story.append(HRFlowable(width=W, thickness=0.75, color=colors.HexColor('#1a1a6e')))
        story.append(sp(4))
        ch1_done = True
    if num == 36 and not ch2_done:
        story.append(Paragraph("CHAPTER 2 QUESTIONS (Q36–Q55)", h2))
        story.append(HRFlowable(width=W, thickness=0.75, color=colors.HexColor('#1a1a6e')))
        story.append(sp(4))
        ch2_done = True

    story.append(Paragraph(f"{num}. {qtext}", qst))
    for o in opts:
        story.append(Paragraph(o, opt))
    story.append(Paragraph(f"Answer: {correct}", ans))
    story.append(Paragraph(f"Source: {citation}", cit))

# ── Answer Key ──────────────────────────────────────────────────────────────
story.append(PageBreak())
story.append(Paragraph("ANSWER KEY — Version 3", h1))
story.append(HRFlowable(width=W, thickness=1, color=colors.HexColor('#1a1a6e')))
story.append(sp(6))

rows = [["Q#", "Ans", "Q#", "Ans", "Q#", "Ans", "Q#", "Ans", "Q#", "Ans", "Q#", "Ans"]]
per_col = 10
for i in range(per_col):
    row = []
    for j in range(6):
        idx = j * per_col + i
        if idx < len(questions):
            row += [str(questions[idx][0]), questions[idx][3]]
        else:
            row += ["", ""]
    rows.append(row)
# remaining rows 50-55
for i in range(50, len(questions)):
    pass  # already handled above

col_w = [0.48*inch, 0.38*inch] * 6
story.append(tbl(rows, col_w))
story.append(sp(8))
story.append(Paragraph(
    "Sources: Popa BIO203 lecture slides (Ch.1: 29 slides; Ch.2: 33 slides) + "
    "OpenStax Microbiology (2016), Chapters 1–2. Version 3 — 55 questions, highest yield.",
    ParagraphStyle('CT', fontName='Helvetica-Oblique', fontSize=7.5, textColor=colors.grey)))

doc.build(story)
print("Done -> " + OUTPUT)
