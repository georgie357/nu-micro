# BIO203 Ch.1 & Ch.2 Study Guide - Version 3
# HIGHEST YIELD: Every table has Exam Trap / Popa emphasis column.
# Key distinctions called out explicitly. No background fluff.

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, HRFlowable)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\chapter 1 and 2\BIO203_Ch1_Ch2_Study_Guide_v3.pdf"

styles = getSampleStyleSheet()
h1  = ParagraphStyle('H1', fontName='Helvetica-Bold',   fontSize=16, spaceAfter=6,  textColor=colors.HexColor('#1a1a6e'))
h2  = ParagraphStyle('H2', fontName='Helvetica-Bold',   fontSize=13, spaceAfter=4,  spaceBefore=10, textColor=colors.HexColor('#1a1a6e'))
h3  = ParagraphStyle('H3', fontName='Helvetica-Bold',   fontSize=10, spaceAfter=3,  spaceBefore=6)
bod = ParagraphStyle('BD', fontName='Helvetica',         fontSize=9,  spaceAfter=3,  leading=13)
bul = ParagraphStyle('BL', fontName='Helvetica',         fontSize=9,  spaceAfter=2,  leading=13, leftIndent=14, firstLineIndent=-10)
tip = ParagraphStyle('TP', fontName='Helvetica-Bold',    fontSize=8.5,spaceAfter=4,  leading=12,
                     backColor=colors.HexColor('#fff3cd'), borderPad=4,
                     borderWidth=0.5, borderColor=colors.HexColor('#cc8800'))
cit = ParagraphStyle('CT', fontName='Helvetica-Oblique', fontSize=7.5,spaceAfter=2,  textColor=colors.HexColor('#555555'))

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

def B(text): return f'<b>{text}</b>'
def sp(n=6): return Spacer(1, n)
def HY(text): return Paragraph(f'HIGHEST YIELD: {text}', tip)

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                        leftMargin=0.75*inch, rightMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)
W = 7.0 * inch
story = []

# ── TITLE ─────────────────────────────────────────────────────────────────────
story += [
    Paragraph("BIO203 Microbiology — National University",
              ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=20,
                             alignment=TA_CENTER, textColor=colors.HexColor('#1a1a6e'))),
    Spacer(1, 4),
    Paragraph("Chapters 1 &amp; 2 Study Guide — Version 3 (Highest Yield)",
              ParagraphStyle('TS', fontName='Helvetica-Bold', fontSize=14, alignment=TA_CENTER)),
    Spacer(1, 3),
    Paragraph("Source: Popa lecture slides + OpenStax Microbiology (2016)",
              ParagraphStyle('TC', fontName='Helvetica-Oblique', fontSize=9,
                             alignment=TA_CENTER, textColor=colors.grey)),
    HRFlowable(width=W, thickness=2, color=colors.HexColor('#1a1a6e')),
    sp(8),
]

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 1
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("CHAPTER 1: AN INVISIBLE WORLD", h1))
story.append(HRFlowable(width=W, thickness=1, color=colors.HexColor('#1a1a6e')))
story.append(sp(4))

# 1.2 Definition
story.append(Paragraph("1.1  Microbiology Definition &amp; Size Scale (Popa slides 2–3; OpenStax 1.1)", h2))
story.append(tbl([
    ["Object", "Approx. Size", "Visible without scope?", "Exam trap"],
    ["Virus",               "~100 nm",      "No",  "Viruses are acellular — NOT cells"],
    ["Bacterium",           "~1 µm",        "No",  "1 µm = 1,000 nm; bacteria smallest cells"],
    ["Plant/animal cell",   "~10–100 µm",   "~100 µm threshold", ""],
    ["Sand grain",          "~90 µm–2 mm",  "Yes", ""],
], [1.8*inch, 1.1*inch, 1.3*inch, 2.8*inch]))
story.append(sp())

# 1.3 History — Ancient
story.append(Paragraph("1.2  History — Ancient World (Popa slides 4–6; OpenStax 1.2)", h2))
story.append(HY("Thucydides = first IMMUNITY observation. Varro = first germ theory proposal. These names appear on tests."))
story.append(tbl([
    ["Person / Event", "Date", "What they did / said", "Exam tip"],
    ["Hippocrates\n(460–370 BC)", "Ancient Greece",
     "Father of Western medicine. Diseases have NATURAL causes, not divine punishment. Wrote Hippocratic Corpus.",
     "Foundation of all medicine. Know: natural vs supernatural explanation."],
    ["Thucydides\n(460–395 BC)", "430 BC plague",
     "Survived Athenian plague; observed survivors did NOT get re-infected even when nursing sick.",
     "FIRST recorded observation of IMMUNITY. Trick Q: 'who first described immunity?' = Thucydides, not a scientist."],
    ["Marcus Terentius Varro\n(116–27 BC)", "36 BC",
     "Proposed invisible animalia minuta (minute creatures) cause disease — 1,700 years before germ theory proven.",
     "Germ theory CONCEPT, but NO proof. Common trap: confuse with Koch who PROVED it."],
    ["al-Razi (Rhazes)\n(854–925 AD)", "Islamic Persia",
     "First to distinguish MEASLES from SMALLPOX. Chose hospital site by rotting meat test.",
     "First differential diagnosis. Know the measles/smallpox distinction."],
    ["Ibn Sina (Avicenna)\n(980–1037 AD)", "1025 AD",
     "Canon of Medicine: contagion through contaminated breath; advanced quarantine. Used as textbook through Renaissance.",
     "Canon = major text through Renaissance. Know the quarantine connection."],
], [1.4*inch, 0.85*inch, 2.75*inch, 2.0*inch]))
story.append(sp())

# 1.4 History — Microscope Pioneers
story.append(Paragraph("1.3  Microscope Pioneers (Popa slides 6–7; OpenStax 1.2)", h2))
story.append(HY("Hooke = DEAD cell walls only. Leeuwenhoek = LIVING organisms. This distinction is tested every time."))
story.append(tbl([
    ["Person", "Date", "Key contribution", "Critical exam distinction"],
    ["Zacharias Janssen\n(+ Hans)", "Late 1500s–early 1600s",
     "Credited with compound microscope (two lenses). Dutch spectacle-maker.",
     "Evidence is INCONCLUSIVE — records lost, never published, neighbor Lippershey built same. Cannot confirm as inventor."],
    ["Galileo Galilei\n(1564–1642)", "~1609",
     "Applied compound microscope to insect parts (compound eyes).",
     "NOT discoverer of microorganisms. Used it on insects, not microbes. More famous for telescope."],
    ["Robert Hooke\n(1635–1703)", "1665",
     "Micrographia (1665) — bestseller. Viewed cork slice; saw box-like walls; coined term CELL (cella = small room).",
     "Saw DEAD PLANT CELL WALLS only — cork cells are dead, appeared hollow. Did NOT see living organisms."],
    ["Anton van Leeuwenhoek\n(1632–1723)", "1674–1675",
     "Cloth merchant/lens-maker from Delft. Simple (1 lens) microscope, more powerful than compound. First to see LIVING organisms (animalcules). Pond water, rain water, dental scrapings. Letters to Royal Society of London.",
     "KEY: living organisms = first time. Simple scope > compound scope of his era. 'Father of microbiology.' Called animalcules = 'wee little beasties.'"],
    ["Girolamo Fracastoro", "1546",
     "De Contagione: proposed seminaria ('seeds of contagion') spread disease via objects (fomes).",
     "THEORETICAL only — no microscope. Conceptual germ theory predecessor. Fomes = infected object (e.g., cloth)."],
], [1.3*inch, 0.75*inch, 2.2*inch, 2.75*inch]))
story.append(sp())

# 1.5 History — Golden Age
story.append(Paragraph("1.4  Golden Age of Microbiology 1857–1914 (Popa slides 7–13; OpenStax 1.2)", h2))
story.append(HY("Know Fanny Hesse (agar idea, uncredited). Know magic bullet = selective toxicity. Know Fleming's accident + Voureka's name."))
story.append(tbl([
    ["Scientist", "Country / Dates", "Key contributions — testable facts", "Popa emphasis / Exam trap"],
    ["Edward Jenner", "England\n1749–1823",
     "Observed dairymaids with COWPOX protected from SMALLPOX. Experiment: inoculated boy with cowpox → challenged with smallpox → boy did not get smallpox. Developed FIRST VACCINE.",
     "Popa slide 7. Know the logic: observation → hypothesis → experiment → result. Cowpox = vaccinia virus; smallpox = variola virus — related viruses. Jenner = first vaccine, NOT first immunity observation (Thucydides)."],
    ["Louis Pasteur", "France\n1822–1895",
     "1. Disproved spontaneous generation: swan-neck flask — boiled broth stayed sterile until neck broken\n2. Proved microbes cause FERMENTATION\n3. Invented PASTEURIZATION (high heat, short time)\n4. Vaccines: chicken cholera, anthrax, RABIES\n5. Co-developed germ theory of disease",
     "Popa slide 8 — full slide. All 5 contributions testable. Trap: pasteurization does NOT sterilize — it kills most spoilage organisms but not ALL."],
    ["Robert Koch", "Germany\n1843–1910",
     "1. Proved Bacillus anthracis causes ANTHRAX (1876) — first proof ONE microbe causes ONE disease\n2. Developed KOCH'S POSTULATES (4 steps)\n3. Pure culture technique\n4. Agar plates — Fanny Hesse's idea (she was his assistant's wife — NOT credited)",
     "Popa slide 9. Koch's postulates are the most-tested concept. Fanny Hesse ALWAYS comes up — know her name and that she was NOT credited. Trap: Pasteur = germ theory idea, Koch = experimental PROOF."],
    ["Paul Ehrlich", "Germany\n1854–1915",
     "Concept of 'magic bullet' = drug with SELECTIVE TOXICITY (kills pathogen, not host). Developed SALVARSAN (arsenic compound, 1910) for syphilis — first modern chemotherapy drug.",
     "Popa slide 11. Magic bullet = selective toxicity (these two phrases are the same thing). Salvarsan = syphilis. Founded the field of chemotherapy."],
    ["Alexander Fleming", "Scotland\n1881–1955",
     "Staphylococcus plate contaminated with Penicillium mold → clear zone of NO growth around mold → discovered PENICILLIN (1928). Mass-produced in time for WW2. Dr. Sarah Voureka (Greece) — colleague and later spouse — contributed significantly.",
     "Popa slides 12–13. Accidental discovery story is testable. Voureka is specifically named by Popa — know her name. Mass production context = WW2 battlefield use."],
], [1.1*inch, 0.85*inch, 3.0*inch, 2.05*inch]))
story.append(sp())

# Koch's Postulates
story.append(Paragraph(B("Koch's Postulates — 4 Steps (Popa slide 9; OpenStax 1.2):"), h3))
story.append(tbl([
    ["Step", "What must be shown", "Exam trap"],
    ["1", "The microorganism is found in ALL animals with the disease (not in healthy animals)", "Must be present in EVERY diseased animal — not just some"],
    ["2", "The microorganism is isolated from the diseased animal and grown in PURE CULTURE", "Must be pure culture — one species only"],
    ["3", "Pure culture inoculated into healthy animal causes the SAME disease", "Must cause the SAME disease — not a different one"],
    ["4", "The microorganism is re-isolated from the experimentally infected animal and shown to be the SAME as step 2", "Completing the loop — confirms causation"],
], [0.4*inch, 3.5*inch, 3.1*inch]))
story.append(Paragraph("Note: Koch's postulates cannot always be applied — some pathogens cannot be cultured (e.g., Treponema pallidum), and some only cause disease in humans.", cit))
story.append(sp())

# 1.6 Taxonomy
story.append(Paragraph("1.5  Taxonomy &amp; Classification (Popa slides 10, 17–19; OpenStax 1.2–1.3)", h2))
story.append(tbl([
    ["Person", "Year", "Contribution", "What they added / changed"],
    ["Carolus Linnaeus", "1758",
     "Binomial nomenclature; taxonomy hierarchy",
     "Genus + specific epithet, italicized. Hierarchy: Domain → Kingdom → Phylum → Class → Order → Family → Genus → Species"],
    ["Ernst Haeckel", "1866",
     "Added Protista",
     "Third kingdom alongside Plants and Animals"],
    ["Robert Whittaker", "1969",
     "5 kingdoms + empire",
     "Animalia, Plantae, Fungi, Protista, Monera"],
    ["Carl Woese &amp; George Fox", "1970s",
     "3-domain system via 16S rRNA sequences",
     "Bacteria, Archaea, Eukarya — replaced 5-kingdom system. Molecular phylogeny."],
], [1.3*inch, 0.55*inch, 1.8*inch, 3.35*inch]))
story.append(Paragraph("Binomial nomenclature rules: Genus capitalized + specific epithet lowercase, always italicized (E. coli, S. aureus). After first mention, genus can be abbreviated.", bod))
story.append(sp())

# 1.7 Three-Domain System
story.append(Paragraph("1.6  Three-Domain System (Popa slides 17–18; OpenStax 1.3)", h2))
story.append(HY("Archaea: prokaryote but NO peptidoglycan and NOT human pathogens — two separate testable facts."))
story.append(tbl([
    ["Domain", "Cell Type", "Cell wall", "Pathogens?", "Examples / Key facts"],
    ["Bacteria", "Prokaryote", "Peptidoglycan (thick in G+, thin in G-)",
     "Many are", "E. coli, Staph, Mycobacterium; binary fission; diverse energy sources"],
    ["Archaea", "Prokaryote", "NO peptidoglycan (unique ether-linked lipids)",
     "NOT known human pathogens",
     "Extremophiles: methanogens (gut, landfills), halophiles (salt lakes), thermophiles (hot springs, Yellowstone)"],
    ["Eukarya", "Eukaryote", "Varies (chitin in fungi, cellulose in algae, none in protozoa)",
     "Some are", "Protists (algae + protozoa), Fungi, Plants, Animals; membrane-bound nucleus"],
], [0.85*inch, 0.85*inch, 1.55*inch, 0.95*inch, 2.8*inch]))
story.append(sp())

# 1.8 Major Groups
story.append(Paragraph("1.7  Major Groups of Microorganisms (Popa slides 20–28; OpenStax 1.3)", h2))
story.append(tbl([
    ["Group", "Domain", "Cell wall", "Pathogenic?", "Exam trap / Key distinction"],
    ["Bacteria", "Bacteria", "Peptidoglycan", "Many", "Cell wall = peptidoglycan. Gram stain works here."],
    ["Archaea", "Archaea", "No peptidoglycan", "NOT human pathogens", "Gram stain does NOT work on Archaea. Not pathogens."],
    ["Algae\n(Protists)", "Eukarya", "Cellulose", "Not pathogenic", "Photosynthetic. Source of agar (red algae). NOT pathogens."],
    ["Protozoa\n(Protists)", "Eukarya", "None (most)", "Many are", "Giardia, Plasmodium, Trichomonas. No cell wall."],
    ["Fungi", "Eukarya", "Chitin", "Some are", "Chitin — NOT peptidoglycan, NOT cellulose. Yeast (unicellular) vs mold (multicellular)."],
    ["Helminths", "Eukarya\n(multicellular)", "None", "Yes (parasitic)", "NOT microorganisms — multicellular animals. Studied in micro because eggs/larvae are microscopic."],
    ["Viruses", "Acellular", "Protein capsid\n(+/- lipid envelope)", "Yes", "DNA OR RNA — NEVER both. Acellular. Replicate ONLY inside a host cell."],
    ["Prions", "Acellular", "None", "Yes", "Protein ONLY — no nucleic acid at all. Misfolding cascade. CJD (human), BSE (mad cow). Prusiner Nobel 1998."],
], [0.85*inch, 0.75*inch, 1.0*inch, 0.7*inch, 3.7*inch]))
story.append(sp())

# 1.9 Modern Microbiology
story.append(Paragraph("1.8  Modern Microbiology (Popa slides 14–16; OpenStax 1.1–1.2)", h2))
story.append(tbl([
    ["Topic", "What it is", "Testable fact"],
    ["Human microbiome", "Microbes naturally inhabiting body (gut, skin, etc.)", "Contribute to health; disruption linked to disease"],
    ["Genetic engineering", "Bacteria/fungi produce human proteins (insulin, vaccines, enzymes)", "Recombinant DNA; bacteria used as factories"],
    ["CRISPR", "Gene-editing based on bacterial immune mechanisms", "Derived from normal bacterial immune process"],
    ["Bioremediation", "Bacteria degrade environmental pollutants", "Oil spills — Deepwater Horizon 2010, Gulf of Mexico"],
    ["Bioterrorism", "CDC Category A agents require special preparedness", "Category A = anthrax, smallpox, plague — highest concern"],
], [1.4*inch, 2.5*inch, 3.1*inch]))
story.append(sp())

# Ch1 summary
story.append(Paragraph("Chapter 1 — Must Memorize", h2))
story.append(tbl([
    ["Fact", "The answer"],
    ["Who first saw living organisms?", "Leeuwenhoek, 1675 — animalcules, simple microscope — 'father of microbiology'"],
    ["Who first saw cells?", "Hooke, 1665 — but DEAD cork cell walls only, coined 'cell'"],
    ["Who disproved spontaneous generation?", "Pasteur — swan-neck flask"],
    ["Who proved ONE microbe causes ONE disease?", "Koch — anthrax 1876 — Koch's postulates"],
    ["Whose idea was agar?", "Fanny Hesse — Koch's assistant's wife, never credited"],
    ["First vaccine?", "Jenner — cowpox → smallpox protection"],
    ["Magic bullet?", "Ehrlich — selective toxicity — Salvarsan for syphilis"],
    ["Penicillin discovered by?", "Fleming (accidental) — colleague Voureka contributed"],
    ["3-domain system via?", "Woese &amp; Fox, 1970s, using 16S rRNA sequences"],
    ["Prions?", "Protein only, no nucleic acid. CJD/BSE. Prusiner Nobel 1998."],
    ["Viruses?", "Acellular. DNA OR RNA — never both. Host cell required for replication."],
    ["Archaea?", "Prokaryote, NO peptidoglycan, NOT human pathogens, extremophiles"],
    ["Fungi cell wall?", "Chitin (NOT peptidoglycan, NOT cellulose)"],
    ["Algae cell wall?", "Cellulose. Photosynthetic. NOT pathogenic. Source of agar."],
], [2.8*inch, 4.2*inch]))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 2
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("CHAPTER 2: HOW WE SEE THE INVISIBLE WORLD", h1))
story.append(HRFlowable(width=W, thickness=1, color=colors.HexColor('#1a1a6e')))
story.append(sp(4))

# 2.1 Properties of light
story.append(Paragraph("2.1  Properties of Waves and Light (Popa slides 4–5; OpenStax 2.1)", h2))
story.append(tbl([
    ["Property", "Definition", "Exam tip"],
    ["Wavelength", "Distance between consecutive wave peaks", "Shorter wavelength = higher energy; electron microscopes exploit this"],
    ["Amplitude", "Height of wave peak / depth of trough", "Amplitude = brightness (not color)"],
    ["Frequency", "Number of wavelengths per unit time", "Higher frequency = shorter wavelength = higher energy"],
    ["Reflection", "Wave bounces off material", "Basis of SEM — secondary electrons reflected off surface"],
    ["Absorbance", "Material captures wave energy", "Stains work by absorbing specific wavelengths"],
    ["Transmission", "Wave passes through material", "Light microscope = transmission through specimen"],
], [1.3*inch, 2.3*inch, 3.4*inch]))
story.append(sp())

# 2.2 Magnification / Resolution / Contrast
story.append(Paragraph("2.2  Magnification, Resolution, and Contrast (Popa slide 8; OpenStax 2.1)", h2))
story.append(HY("Resolution numbers are tested: human eye 200 µm, light scope 200 nm, TEM 2.5 nm. Shorter wavelength = better resolution."))
story.append(tbl([
    ["Term", "Definition", "Key number / Exam trap"],
    ["Magnification", "Enlarges image; Total = ocular × objective", "10× ocular × 100× objective = 1,000× total"],
    ["Resolution\n(resolving power)", "Ability to distinguish two adjacent points as separate; smaller resolvable distance = better resolution",
     "Human eye: ~200 µm\nLight microscope: ~200 nm\nTEM: ~2.5 nm\nTrap: more magnification without better resolution = blurry image ('empty magnification')"],
    ["Contrast", "Visible difference between specimen and background", "Staining and special illumination (darkfield, phase-contrast) increase contrast"],
    ["Numerical Aperture\n(NA)", "Measure of lens's ability to gather light; higher NA = better resolution",
     "NA depends on RI of medium and half-angle of light cone. Oil immersion raises NA."],
], [1.3*inch, 2.5*inch, 3.2*inch]))
story.append(sp())

# 2.3 Immersion Oil
story.append(Paragraph("2.3  Refraction and Immersion Oil (Popa slide 6; OpenStax 2.1)", h2))
story.append(tbl([
    ["Concept", "What it means", "Exam trap"],
    ["Refraction", "Light bends when passing from one medium to another with different refractive index (RI)", "High-magnification lenses are tiny — refracted light misses the lens"],
    ["Immersion oil", "Fills gap between 100× objective and coverslip. RI ~1.515 = same as glass.", "Light passes straight through without bending → more light enters objective → better resolution AND brightness"],
    ["When to use", "Required ONLY at 100× (oil immersion objective)", "Never use oil on 40× or lower objectives — will damage them"],
], [1.2*inch, 2.8*inch, 3.0*inch]))
story.append(sp())

# 2.4 Types of Light Microscopes
story.append(Paragraph("2.4  Types of Light Microscopes (Popa slides 9–14; OpenStax 2.2)", h2))
story.append(HY("Darkfield = Treponema pallidum (syphilis). Phase-contrast = live unstained cells. Fluorescence = immunofluorescence / MRSA. These associations are tested."))
story.append(tbl([
    ["Type", "How it works", "Image look", "Best use / Organisms"],
    ["Brightfield\n(compound)", "Transmitted white light; specimen absorbs light",
     "Dark on bright background",
     "Stained specimens. Most common lab scope. 1000× max with oil. Coarse focus: 4×/10× only; fine focus: 40×/100×."],
    ["Darkfield", "Opaque disk blocks direct light; only scattered light enters objective",
     "Bright on dark background",
     "Unstained LIVE organisms. Treponema pallidum (syphilis) — too thin to stain. Spirochetes."],
    ["Phase-contrast", "Annular stop + phase ring create destructive interference for direct light",
     "High-contrast grayscale; no stain",
     "Live unstained cells; internal organelles; endospores. Useful for fragile organisms that would be killed by staining."],
    ["DIC (Nomarski)", "Two polarized beams; interference creates 3D appearance",
     "3D shadow-cast, full color",
     "Live cells; thick specimens; research labs."],
    ["Fluorescence", "UV excites fluorochrome dyes → emit visible light (Stokes shift)",
     "Bright colored glow on dark background",
     "Immunofluorescence: DFA (direct) or IFA (indirect, more sensitive). MRSA typing. Legionella, Chlamydia, rabies virus."],
    ["Confocal\n(laser scanning)", "Single laser focal plane; computer reconstructs 3D from z-slices",
     "Sharp 3D reconstructions",
     "Biofilms. Thick specimens. 'CT scan of cells.' Research."],
], [1.0*inch, 1.7*inch, 1.3*inch, 3.0*inch]))
story.append(sp())

# 2.5 Electron Microscopy
story.append(Paragraph("2.5  Electron Microscopy (Popa slides 15–18; OpenStax 2.3)", h2))
story.append(HY("TEM = 2D internal cross-sections. SEM = 3D surface. CANNOT use on living material. This TEM vs SEM distinction is always tested."))
story.append(tbl([
    ["Feature", "TEM — Transmission EM", "SEM — Scanning EM"],
    ["Principle", "Electrons pass THROUGH ultrathin sections", "Electron beam SCANS SURFACE; secondary electrons detected"],
    ["Specimen prep", "Dehydrate → embed in resin → ultramicrotome (20–100 nm sections) → heavy metal stain (uranyl acetate, osmium tetroxide)",
     "Dehydrate → critical-point dry (liquid CO2) → sputter-coat with gold/palladium (~10 nm)"],
    ["Image type", "2D internal cross-section", "3D surface topography"],
    ["Magnification", "10,000–100,000×", "1,000–10,000×"],
    ["Resolution", "~2.5 nm", "~20 nm"],
    ["What you see", "Ribosomes, membranes, inclusions, intracellular details",
     "Surface features, pili, flagella, spores, biofilms, 3D morphology"],
    ["Exam trap", "Cannot use for living material (requires vacuum)", "Cannot see internal structures"],
], [1.5*inch, 2.75*inch, 2.75*inch]))
story.append(sp())

# 2.6 Specimen Prep
story.append(Paragraph("2.6  Specimen Preparation (Popa slides 20–21; OpenStax 2.4)", h2))
story.append(tbl([
    ["Method", "Description", "When used / Exam trap"],
    ["Wet mount", "Specimen in liquid drop under coverslip; no fixation", "Live/motile organisms. Quick look. Cannot stain."],
    ["Smear", "Thin film spread on slide, air-dried", "Preparation step before fixation and staining — not a finished prep by itself"],
    ["Heat fixation", "Smear passed through flame 2–3×", "Most common for bacteria. Kills cells, adheres to slide, denatures proteins. Faster than chemical."],
    ["Chemical fixation", "Acetic acid, ethanol, methanol, formalin, or glutaraldehyde", "Preserves fine structures. Required for EM and some special stains."],
], [1.3*inch, 2.2*inch, 3.5*inch]))
story.append(sp())

# 2.7 Staining — Principles
story.append(Paragraph("2.7  Staining Principles (Popa slide 22; OpenStax 2.4)", h2))
story.append(tbl([
    ["Stain type", "Ion charged", "What stains", "Examples"],
    ["Basic dye (positive)", "Chromophore is the POSITIVE ion", "Negatively charged bacterial surfaces → cells appear colored (positive staining)",
     "Crystal violet, methylene blue, malachite green, safranin"],
    ["Acidic dye (negative)", "Chromophore is the NEGATIVE ion", "Repelled by bacterial surfaces → background stains, cells appear as HALOS",
     "India ink, nigrosin — used for capsule staining"],
], [1.1*inch, 1.5*inch, 2.4*inch, 2.0*inch]))
story.append(sp())

# 2.8 Staining Types
story.append(Paragraph("2.8  Differential and Special Stains (Popa slides 22–32; OpenStax 2.4)", h2))
story.append(HY("Gram stain steps must be in order. Gram+ = PURPLE. Gram- = PINK. Acid-fast = PINK (AFB) or BLUE (non-AFB). Endospore: spores GREEN, cells PINK."))
story.append(tbl([
    ["Stain", "Steps in order", "Results", "Purpose / Organisms / Exam trap"],
    ["Simple stain", "Fix smear → one basic dye (crystal violet, methylene blue, OR safranin) 30–60 sec → water rinse → blot",
     "All cells same color",
     "Determine shape (coccus/bacillus/spirillum), arrangement (singles/pairs/chains/tetrads/clusters). Cannot distinguish G+ from G-."],
    ["Gram stain\n(differential)", "1. Crystal violet (primary) — ALL cells purple\n2. Iodine (mordant) — CV-I complex forms\n3. Alcohol/acetone (decolorizer) — G+ thick wall retains CV-I; G- thin wall loses it\n4. Safranin (counterstain) — G- cells stain pink",
     "G+ = PURPLE\nG- = PINK/RED",
     "Most important differential stain. Developed by Hans Christian Gram, 1884.\nTrap: the DECOLORIZER step is critical — over-decolorize → G+ looks G-; under-decolorize → G- looks G+.\nGuides antibiotic choice: penicillin works better on G+."],
    ["Acid-fast stain\n(Ziehl-Neelsen)", "1. Carbolfuchsin + heat — ALL cells pink\n2. Acid-alcohol (decolorizer) — waxy mycolic acid resists\n3. Methylene blue (counterstain) — non-AFB stain blue",
     "AFB = PINK/RED\nNon-AFB = BLUE",
     "Mycobacterium tuberculosis, M. leprae, Nocardia.\nMycolic acid in cell wall = waxy → resists decolorization.\nTrap: only some bacteria are acid-fast — most bacteria are NOT."],
    ["Capsule stain\n(negative)", "India ink or nigrosin stains background; cells unstained",
     "Cells = clear halos on dark background",
     "Visualizes polysaccharide capsules. Capsules protect against phagocytosis.\nCryptococcus neoformans, Klebsiella pneumoniae.\nNegative stain = background stained, NOT the cells."],
    ["Endospore stain\n(Schaeffer-Fulton)", "1. Malachite green + steam — drives stain into spores\n2. Water wash — removes stain from vegetative cells\n3. Safranin — vegetative cells stain pink",
     "Spores = GREEN\nVegetative cells = PINK",
     "Bacillus, Clostridium, Clostridioides difficile (C. diff).\nEndospores survive boiling, disinfectants, desiccation.\nTrap: not all bacteria form spores — only Bacillus and Clostridium genera tested here."],
    ["Flagella stain", "Mordant (tannic acid or alum) thickens flagella first → then basic fuchsin",
     "Flagella visible as dark lines",
     "Determine flagella number and arrangement.\nTrap: flagella are ~20 nm — WAY too thin to see without the mordant thickening step.\nExample organism: Bacillus cereus."],
], [1.0*inch, 2.0*inch, 1.2*inch, 2.8*inch]))
story.append(sp())

# Gram stain mechanism
story.append(Paragraph(B("Gram Stain Mechanism — Why G+ stays purple (Popa slide 26; OpenStax 2.4):"), h3))
story.append(tbl([
    ["Cell type", "Cell wall", "What happens during decolorization", "Final color"],
    ["Gram-positive", "THICK peptidoglycan (20–80 nm)", "Alcohol dehydrates + contracts thick wall → pores close → CV-I complex TRAPPED inside", "PURPLE"],
    ["Gram-negative", "THIN peptidoglycan (2–7 nm) + outer membrane with LPS", "Alcohol dissolves outer membrane lipids → CV-I washes out → colorless → safranin counterstain binds", "PINK/RED"],
], [1.2*inch, 2.2*inch, 2.5*inch, 1.1*inch]))
story.append(sp())

# Ch2 Quick Reference
story.append(Paragraph("Chapter 2 — Numbers to Memorize", h2))
story.append(tbl([
    ["Fact", "The number / answer"],
    ["Human eye resolution", "~200 µm"],
    ["Light microscope resolution (oil immersion)", "~200 nm"],
    ["TEM resolution", "~2.5 nm — internal 2D sections"],
    ["SEM resolution", "~20 nm — 3D surface"],
    ["STM/AFM magnification", "Up to 100,000,000× — individual atoms"],
    ["Immersion oil refractive index", "~1.515 = same as glass — prevents light scatter at 100×"],
    ["G+ peptidoglycan thickness", "20–80 nm (thick) → retains crystal violet–iodine → PURPLE"],
    ["G- peptidoglycan thickness", "2–7 nm (thin) + outer membrane → loses CV-I → PINK after safranin"],
    ["Acid-fast result (AFB)", "PINK/RED — mycolic acid wall resists acid-alcohol decolorizer"],
    ["Acid-fast result (non-AFB)", "BLUE — methylene blue counterstain"],
    ["Endospore stain results", "Spores = GREEN (malachite green); vegetative cells = PINK (safranin)"],
    ["Capsule stain method", "Negative stain — background dark, capsule = clear halo"],
    ["When to use darkfield", "Treponema pallidum (syphilis) — live, unstained, too thin for standard staining"],
    ["When to use phase-contrast", "Live unstained cells — internal structures visible without killing organism"],
    ["When to use fluorescence", "Immunofluorescence, MRSA, Legionella, Chlamydia — antibody-tagged detection"],
], [3.5*inch, 3.5*inch]))
story.append(sp())

story.append(Paragraph(
    "Sources: Popa BIO203 lecture slides (Ch.1: 29 slides; Ch.2: 33 slides) + "
    "OpenStax Microbiology (2016), Chapters 1–2. Version 3 — highest yield, exam-focused.", cit))

doc.build(story)
print("Done -> " + OUTPUT)
