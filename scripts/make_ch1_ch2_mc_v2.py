# BIO203 Ch.1 & Ch.2 - 50 Multiple Choice Questions - Version 2
# Built from actual source material: Popa slides + OpenStax textbook

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\chapter 1 and 2\BIO203_Ch1_Ch2_MC_Questions_v2.pdf"

styles = getSampleStyleSheet()
h1  = ParagraphStyle('H1', fontName='Helvetica-Bold',   fontSize=16, spaceAfter=6,  textColor=colors.HexColor('#1a1a6e'))
h2  = ParagraphStyle('H2', fontName='Helvetica-Bold',   fontSize=12, spaceAfter=4,  spaceBefore=10, textColor=colors.HexColor('#1a1a6e'))
qst = ParagraphStyle('QS', fontName='Helvetica-Bold',   fontSize=9,  spaceAfter=2,  leading=13)
opt = ParagraphStyle('OP', fontName='Helvetica',         fontSize=9,  spaceAfter=1,  leading=12, leftIndent=18)
ans = ParagraphStyle('AN', fontName='Helvetica-Bold',   fontSize=8,  spaceAfter=1,  textColor=colors.HexColor('#0000aa'))
cit = ParagraphStyle('CT', fontName='Helvetica-Oblique', fontSize=7.5,spaceAfter=6,  textColor=colors.HexColor('#555555'), leftIndent=18)

def sp(n=6): return Spacer(1, n)

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                        leftMargin=0.75*inch, rightMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)
W = 7.0 * inch
story = []

# Title
story += [
    Paragraph("BIO203 Microbiology — National University", ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=18, alignment=TA_CENTER, textColor=colors.HexColor('#1a1a6e'))),
    sp(4),
    Paragraph("Chapters 1 &amp; 2 — 50 Multiple Choice Questions — Version 2", ParagraphStyle('TS', fontName='Helvetica-Bold', fontSize=13, alignment=TA_CENTER)),
    sp(3),
    Paragraph("Source: Popa lecture slides + OpenStax Microbiology (2016) | Answer key included", ParagraphStyle('TC', fontName='Helvetica-Oblique', fontSize=9, alignment=TA_CENTER, textColor=colors.grey)),
    HRFlowable(width=W, thickness=2, color=colors.HexColor('#1a1a6e')),
    sp(8),
]

# ─── Question data ────────────────────────────────────────────────────────────
# Format: (number, question, [A,B,C,D], correct_letter, "citation")
questions = [
    # ── CHAPTER 1: Definitions & Microbiology overview (Q1–5) ──────────────
    (1,
     "Which of the following BEST defines microbiology?",
     ["A. The study of viruses only",
      "B. The science that studies organisms too small to be seen with the unaided eye",
      "C. The study of chemistry within living cells",
      "D. The branch of biology focused on genetics"],
     "B",
     "Popa slide 3; OpenStax 1.1"),

    (2,
     "Approximately what size must an object be to be visible without a microscope?",
     ["A. 1 µm",
      "B. 10 µm",
      "C. 100 µm",
      "D. 1 mm"],
     "C",
     "Popa slide 3; OpenStax 1.1"),

    (3,
     "A typical bacterium measures approximately:",
     ["A. 100 nm",
      "B. 1 µm",
      "C. 10 µm",
      "D. 100 µm"],
     "B",
     "Popa slide 3; OpenStax 1.1"),

    (4,
     "Which sub-discipline of microbiology studies bacteria specifically?",
     ["A. Mycology",
      "B. Virology",
      "C. Bacteriology",
      "D. Epidemiology"],
     "C",
     "Popa slide 3; OpenStax 1.1"),

    (5,
     "Marcus Terentius Varro (116–27 BC) is notable in microbiology history because he:",
     ["A. First described live microorganisms under a microscope",
      "B. Proposed that 'things we cannot see' can cause disease",
      "C. Developed the first vaccine",
      "D. Established Koch's postulates"],
     "B",
     "Popa slide 5; OpenStax 1.2"),

    # ── History (Q6–15) ─────────────────────────────────────────────────────
    (6,
     "Anton van Leeuwenhoek described live 'animalcules' from pond water and dental scrapings in:",
     ["A. 1543",
      "B. 1665",
      "C. 1675",
      "D. 1796"],
     "C",
     "Popa slide 6; OpenStax 1.2"),

    (7,
     "Robert Hooke's 1665 book Micrographia is significant because it:",
     ["A. First described bacteria in soil",
      "B. Introduced the term 'cell' and described cells in cork",
      "C. Proved that microbes cause fermentation",
      "D. Established the germ theory of disease"],
     "B",
     "OpenStax 1.2; Popa slide 6"),

    (8,
     "Louis Pasteur's swan-neck flask experiment definitively disproved:",
     ["A. Germ theory of disease",
      "B. Koch's postulates",
      "C. Spontaneous generation",
      "D. The concept of immunity"],
     "C",
     "Popa slide 8; OpenStax 1.2"),

    (9,
     "Pasteurization involves:",
     ["A. Sterilizing food by boiling for 30 minutes",
      "B. Application of a high heat for a short time to reduce microbial load",
      "C. Adding preservative chemicals to food",
      "D. Freezing food to kill pathogens"],
     "B",
     "Popa slide 8; OpenStax 1.2"),

    (10,
     "Robert Koch proved that Bacillus anthracis causes anthrax in:",
     ["A. 1857",
      "B. 1876",
      "C. 1884",
      "D. 1928"],
     "B",
     "Popa slide 9; OpenStax 1.2"),

    (11,
     "Koch's postulates are a set of experimental criteria used to:",
     ["A. Classify bacteria by Gram staining",
      "B. Prove that a specific microorganism causes a specific disease",
      "C. Determine antibiotic susceptibility",
      "D. Establish the three-domain classification system"],
     "B",
     "Popa slide 9; OpenStax 1.2"),

    (12,
     "Solid agar as a culture medium was the idea of:",
     ["A. Robert Koch",
      "B. Louis Pasteur",
      "C. Fanny Hesse",
      "D. Alexander Fleming"],
     "C",
     "Popa slide 9; OpenStax 1.2"),

    (13,
     "Edward Jenner's vaccine discovery was based on the observation that:",
     ["A. Smallpox fluid directly protected against cowpox",
      "B. Dairymaids who had mild cowpox infections were protected from smallpox",
      "C. Children vaccinated with cowpox also became immune to measles",
      "D. Smallpox survivors could not be reinfected with cowpox"],
     "B",
     "Popa slide 7; OpenStax 1.2"),

    (14,
     "Paul Ehrlich's 'magic bullet' concept refers to:",
     ["A. A targeted missile delivery system for vaccines",
      "B. A drug with selective toxicity — harmful to the pathogen but not the host",
      "C. The use of radiation to kill bacteria",
      "D. An antibiotic derived from Penicillium mold"],
     "B",
     "Popa slide 11; OpenStax 1.2"),

    (15,
     "Alexander Fleming discovered penicillin when he noticed:",
     ["A. A clear zone around Penicillium mold on a Staphylococcus plate left open accidentally",
      "B. Mold growing in a patient's wound prevented infection",
      "C. Bread mold killed bacteria in broth cultures",
      "D. Sulfa drugs inhibited mold growth"],
     "A",
     "Popa slide 12; OpenStax 1.2"),

    # ── Taxonomy & Classification (Q16–25) ──────────────────────────────────
    (16,
     "Carolus Linnaeus established the system of binomial nomenclature in:",
     ["A. 1543",
      "B. 1665",
      "C. 1758",
      "D. 1866"],
     "C",
     "Popa slide 10; OpenStax 1.3"),

    (17,
     "In binomial nomenclature, which part of the name is ALWAYS capitalized?",
     ["A. Specific epithet",
      "B. Genus",
      "C. Both genus and specific epithet",
      "D. Neither — both are lowercase when written by hand"],
     "B",
     "Popa slide 19; OpenStax 1.3"),

    (18,
     "Carl Woese and George Fox established the three-domain system based on sequences of:",
     ["A. DNA polymerase",
      "B. 16S/18S ribosomal RNA",
      "C. ATP synthase",
      "D. Cell wall peptidoglycan"],
     "B",
     "Popa slide 17; OpenStax 1.3"),

    (19,
     "Which of the following is the CORRECT order from most inclusive to least inclusive in biological classification?",
     ["A. Species → Genus → Family → Order → Class → Phylum → Kingdom → Domain",
      "B. Domain → Kingdom → Phylum → Class → Order → Family → Genus → Species",
      "C. Domain → Phylum → Kingdom → Class → Order → Family → Genus → Species",
      "D. Kingdom → Domain → Phylum → Class → Order → Family → Genus → Species"],
     "B",
     "Popa slide 10; OpenStax 1.3"),

    (20,
     "Archaea differ from Bacteria in that Archaea:",
     ["A. Are eukaryotic",
      "B. Have peptidoglycan cell walls",
      "C. Do not have peptidoglycan cell walls",
      "D. Always cause human disease"],
     "C",
     "Popa slide 21; OpenStax 1.3"),

    (21,
     "Which group of organisms includes methanogens, extreme halophiles, and extreme thermophiles?",
     ["A. Bacteria",
      "B. Fungi",
      "C. Archaea",
      "D. Protozoa"],
     "C",
     "Popa slide 21; OpenStax 1.3"),

    (22,
     "The cell walls of fungi are composed of:",
     ["A. Peptidoglycan",
      "B. Cellulose",
      "C. Chitin",
      "D. Murein"],
     "C",
     "Popa slide 25; OpenStax 1.3"),

    (23,
     "Algae are classified as protists and are characterized by:",
     ["A. Chitin cell walls and heterotrophic nutrition",
      "B. Cellulose cell walls and photosynthetic nutrition; NOT pathogenic",
      "C. No cell walls and motility via pseudopods",
      "D. Peptidoglycan cell walls and binary fission"],
     "B",
     "Popa slide 23; OpenStax 1.3"),

    (24,
     "Viruses differ from all other microorganisms in that they:",
     ["A. Contain both DNA and RNA",
      "B. Have a peptidoglycan protein coat",
      "C. Are acellular and can only replicate inside a living host cell",
      "D. Reproduce by binary fission"],
     "C",
     "Popa slide 27; OpenStax 1.3"),

    (25,
     "Prions are infectious agents that consist of:",
     ["A. Single-stranded RNA only",
      "B. Double-stranded DNA enclosed in a lipid envelope",
      "C. Misfolded proteins with no nucleic acid",
      "D. Small circular DNA plasmids"],
     "C",
     "Popa slide 28; OpenStax 1.3"),

    # ── The 6 groups continued (Q26–30) ─────────────────────────────────────
    (26,
     "Helminths are studied in microbiology primarily because:",
     ["A. They are acellular pathogens smaller than bacteria",
      "B. Their eggs and larval stages are microscopic",
      "C. They lack a nucleus and are prokaryotic",
      "D. They reproduce inside host cells like viruses"],
     "B",
     "Popa slide 26; OpenStax 1.3"),

    (27,
     "Protozoa are motile by which of the following structures?",
     ["A. Peptidoglycan projections",
      "B. Cellulose flagella",
      "C. Pseudopods, cilia, or flagella",
      "D. Pili only"],
     "C",
     "Popa slide 24; OpenStax 1.3"),

    (28,
     "Which organism is a yeast (unicellular fungus) and can cause human infection?",
     ["A. Giardia lamblia",
      "B. Candida albicans",
      "C. Mycobacterium tuberculosis",
      "D. Taenia saginata"],
     "B",
     "Popa slide 25; OpenStax 1.3"),

    (29,
     "Stanley Prusiner received the 1998 Nobel Prize for his work on:",
     ["A. Discovery of penicillin",
      "B. Ribosomal RNA sequencing and the three-domain system",
      "C. Prions as proteinaceous infectious particles",
      "D. CRISPR gene editing"],
     "C",
     "Popa slide 28; OpenStax 1.3"),

    (30,
     "In the three-domain system, which organisms belong to domain Eukarya?",
     ["A. Bacteria, Archaea, and Viruses",
      "B. Only animals and plants",
      "C. Protists (algae and protozoa), Fungi, Plants, and Animals",
      "D. All prokaryotes"],
     "C",
     "Popa slide 18; OpenStax 1.3"),

    # ══ CHAPTER 2 (Q31–50) ══════════════════════════════════════════════════
    # Properties of waves/light (Q31–34)
    (31,
     "The distance between one peak of a wave and the next peak is defined as the:",
     ["A. Amplitude",
      "B. Frequency",
      "C. Wavelength",
      "D. Refractive index"],
     "C",
     "Popa slide 4; OpenStax 2.1"),

    (32,
     "Regarding electromagnetic radiation, which statement is CORRECT?",
     ["A. Longer wavelength = higher energy",
      "B. Shorter wavelength = higher energy",
      "C. All wavelengths have equal energy",
      "D. Wavelength has no relationship to energy"],
     "B",
     "Popa slide 7; OpenStax 2.1"),

    (33,
     "Immersion oil is used with the 100× objective lens primarily to:",
     ["A. Increase the magnification above 1000×",
      "B. Prevent refraction by matching the refractive index of glass, improving resolution",
      "C. Stain the specimen so cells are more visible",
      "D. Cool the objective lens during extended use"],
     "B",
     "Popa slides 6 & 10; OpenStax 2.2"),

    (34,
     "Resolution is defined as:",
     ["A. The ability of a lens to enlarge the image of an object",
      "B. The ability of the lens system to distinguish two adjacent points as separate",
      "C. The difference in light intensity between specimen and background",
      "D. The speed at which light passes through a medium"],
     "B",
     "Popa slide 8; OpenStax 2.1"),

    # Microscope types (Q35–42)
    (35,
     "In a brightfield microscope using a 10× ocular and 40× objective, total magnification is:",
     ["A. 40×",
      "B. 50×",
      "C. 400×",
      "D. 4000×"],
     "C",
     "Popa slide 9; OpenStax 2.2"),

    (36,
     "A darkfield microscope is particularly useful for visualizing:",
     ["A. Stained bacteria on a light background",
      "B. Treponema pallidum (syphilis spirochetes), which are very thin and difficult to stain",
      "C. Endospores inside Bacillus cells",
      "D. Acid-fast Mycobacterium tuberculosis"],
     "B",
     "Popa slide 11; OpenStax 2.2"),

    (37,
     "Phase-contrast microscopy works by:",
     ["A. Staining cells with fluorescent dyes that emit visible light",
      "B. Using an annular stop and phase ring to create destructive interference and enhance contrast",
      "C. Scanning the surface of specimens with an electron beam",
      "D. Firing two infrared photons simultaneously at the specimen"],
     "B",
     "Popa slide 12; OpenStax 2.2"),

    (38,
     "Fluorescence microscopy uses UV light because:",
     ["A. UV light passes through cells without causing any damage",
      "B. Fluorochromes absorb UV light and emit visible light, which is detected",
      "C. UV light has a longer wavelength than visible light, improving resolution",
      "D. UV light is reflected by all biological membranes"],
     "B",
     "Popa slide 13; OpenStax 2.2"),

    (39,
     "Confocal microscopy is described as similar to a CT scan because it:",
     ["A. Uses X-rays to penetrate thick specimens",
      "B. Uses a laser to image a single focal plane (z-slice), allowing 3D reconstruction",
      "C. Scans the surface of specimens like SEM",
      "D. Uses multiple fluorescent antibodies simultaneously"],
     "B",
     "Popa slide 14; OpenStax 2.2"),

    (40,
     "Transmission electron microscopy (TEM) differs from scanning electron microscopy (SEM) in that TEM:",
     ["A. Uses electrons that scan the surface of a whole specimen",
      "B. Produces 3D surface images by detecting secondary electrons",
      "C. Passes electrons through ultrathin sections to reveal INTERNAL structures",
      "D. Has lower resolution (20 nm) than SEM"],
     "C",
     "Popa slides 16–18; OpenStax 2.3"),

    (41,
     "The maximum magnification of TEM is approximately:",
     ["A. 1,000×",
      "B. 10,000×",
      "C. 100,000×",
      "D. 1,000,000×"],
     "C",
     "Popa slide 16; OpenStax 2.3"),

    (42,
     "Before viewing a specimen under SEM, specimens are typically coated with a thin layer of:",
     ["A. Immersion oil",
      "B. India ink",
      "C. Heavy metal salts (uranyl acetate)",
      "D. Gold or gold-palladium alloy"],
     "D",
     "Popa slide 17; OpenStax 2.3"),

    # Staining (Q43–50)
    (43,
     "In the Gram staining procedure, the mordant used to 'set' the primary stain is:",
     ["A. Safranin",
      "B. Methylene blue",
      "C. Gram's iodine",
      "D. Acid-alcohol"],
     "C",
     "Popa slide 26; OpenStax 2.4"),

    (44,
     "After the decolorization step in Gram staining, Gram-positive cells appear:",
     ["A. Pink, because they absorbed safranin",
      "B. Colorless, because the thin peptidoglycan layer cannot retain crystal violet",
      "C. Purple, because thick peptidoglycan retains the crystal violet–iodine complex",
      "D. Green, because malachite green is used as the primary dye"],
     "C",
     "Popa slide 26; OpenStax 2.4"),

    (45,
     "The acid-fast stain is used primarily to identify organisms in the genus:",
     ["A. Bacillus and Clostridium",
      "B. Mycobacterium and Nocardia",
      "C. Cryptococcus and Klebsiella",
      "D. Treponema and Borrelia"],
     "B",
     "Popa slide 28; OpenStax 2.4"),

    (46,
     "In the acid-fast stain, what property of Mycobacterium allows it to resist decolorization with acid-alcohol?",
     ["A. Thick peptidoglycan cell wall",
      "B. Waxy mycolic acid in the cell wall",
      "C. Outer membrane lipopolysaccharide (LPS)",
      "D. Chitin capsule surrounding the cell"],
     "B",
     "Popa slide 28; OpenStax 2.4"),

    (47,
     "In the endospore stain (Schaeffer-Fulton method), the PRIMARY stain used (requires steam) is:",
     ["A. Crystal violet",
      "B. Safranin",
      "C. Malachite green",
      "D. Carbolfuchsin"],
     "C",
     "Popa slide 31; OpenStax 2.4"),

    (48,
     "Capsule staining uses a negative stain (India ink or nigrosin) because:",
     ["A. The capsule absorbs basic dyes strongly",
      "B. The capsule is positively charged and repels the acidic dye",
      "C. The capsule resists all staining, so the background is stained instead to visualize it",
      "D. Capsules only fluoresce under UV light"],
     "C",
     "Popa slide 30; OpenStax 2.4"),

    (49,
     "Flagella staining requires a mordant because:",
     ["A. Flagella are negatively charged and repel all basic dyes without treatment",
      "B. Flagella (~20 nm diameter) are too thin to see without the mordant thickening them",
      "C. Flagella are encased in a waxy capsule that resists staining",
      "D. The mordant dissolves the cell wall to expose the flagella attachment points"],
     "B",
     "Popa slide 32; OpenStax 2.4"),

    (50,
     "A simple stain using a single basic dye (e.g., crystal violet) allows you to determine all of the following EXCEPT:",
     ["A. Cell shape (coccus, bacillus, spirillum)",
      "B. Cell arrangement (singles, pairs, chains, tetrads)",
      "C. Whether an organism is Gram-positive or Gram-negative",
      "D. Approximate cell size"],
     "C",
     "Popa slides 23–24; OpenStax 2.4"),
]

# ── Print questions ───────────────────────────────────────────────────────────
ch1_header_done = False
ch2_header_done = False

for (num, qtext, opts, correct, citation) in questions:
    if num == 1 and not ch1_header_done:
        story.append(Paragraph("CHAPTER 1 QUESTIONS (Q1–Q30)", h2))
        story.append(HRFlowable(width=W, thickness=0.75, color=colors.HexColor('#1a1a6e')))
        story.append(sp(4))
        ch1_header_done = True
    if num == 31 and not ch2_header_done:
        story.append(Paragraph("CHAPTER 2 QUESTIONS (Q31–Q50)", h2))
        story.append(HRFlowable(width=W, thickness=0.75, color=colors.HexColor('#1a1a6e')))
        story.append(sp(4))
        ch2_header_done = True

    story.append(Paragraph(f"{num}. {qtext}", qst))
    for o in opts:
        story.append(Paragraph(o, opt))
    story.append(Paragraph(f"Answer: {correct}", ans))
    story.append(Paragraph(f"Source: {citation}", cit))

# ── Answer Key Summary ────────────────────────────────────────────────────────
story.append(PageBreak())
story.append(Paragraph("ANSWER KEY SUMMARY", h1))
story.append(HRFlowable(width=W, thickness=1, color=colors.HexColor('#1a1a6e')))
story.append(sp(6))

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

# Build answer table: 5 columns of 10
rows = [["Q#", "Ans", "Q#", "Ans", "Q#", "Ans", "Q#", "Ans", "Q#", "Ans"]]
nums = [q[0] for q in questions]
ans_list = [q[3] for q in questions]
for i in range(0, 10):
    row = []
    for j in range(5):
        idx = j * 10 + i
        if idx < len(questions):
            row += [str(nums[idx]), ans_list[idx]]
        else:
            row += ["", ""]
    rows.append(row)

col_w = [0.55*inch, 0.45*inch] * 5
story.append(tbl(rows, col_w))

story.append(sp(8))
story.append(Paragraph(
    "Sources: Popa BIO203 lecture slides (Ch.1: 29 slides; Ch.2: 33 slides) + "
    "OpenStax Microbiology (2016), Chapters 1–2. Version 2 — built from actual source material.",
    ParagraphStyle('CT', fontName='Helvetica-Oblique', fontSize=7.5, textColor=colors.grey)))

doc.build(story)
print("Done →", OUTPUT)
