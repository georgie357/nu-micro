# BIO203 Ch.1 & Ch.2 Study Guide - Version 2
# Built from actual source material: Popa slides + OpenStax textbook

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, HRFlowable)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\chapter 1 and 2\BIO203_Ch1_Ch2_Study_Guide_v2.pdf"

# ── styles ──────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()
h1  = ParagraphStyle('H1', fontName='Helvetica-Bold',   fontSize=16, spaceAfter=6,  textColor=colors.HexColor('#1a1a6e'))
h2  = ParagraphStyle('H2', fontName='Helvetica-Bold',   fontSize=13, spaceAfter=4,  spaceBefore=10, textColor=colors.HexColor('#1a1a6e'))
h3  = ParagraphStyle('H3', fontName='Helvetica-Bold',   fontSize=10, spaceAfter=3,  spaceBefore=6)
bod = ParagraphStyle('BD', fontName='Helvetica',         fontSize=9,  spaceAfter=3,  leading=13)
bul = ParagraphStyle('BL', fontName='Helvetica',         fontSize=9,  spaceAfter=2,  leading=13, leftIndent=14, firstLineIndent=-10)
sml = ParagraphStyle('SM', fontName='Helvetica',         fontSize=8,  spaceAfter=2,  leading=11)
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
def I(text): return f'<i>{text}</i>'
def sp(n=6): return Spacer(1, n)

# ── document ─────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                        leftMargin=0.75*inch, rightMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)
W = 7.0 * inch
story = []

# ══════════════════════════════════════════════════════════════════════════════
# TITLE
# ══════════════════════════════════════════════════════════════════════════════
story += [
    Paragraph("BIO203 Microbiology — National University", ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=20, alignment=TA_CENTER, textColor=colors.HexColor('#1a1a6e'))),
    Spacer(1, 4),
    Paragraph("Chapters 1 &amp; 2 Study Guide — Version 2", ParagraphStyle('TS', fontName='Helvetica-Bold', fontSize=14, alignment=TA_CENTER)),
    Spacer(1, 3),
    Paragraph("Source: Popa lecture slides + OpenStax Microbiology (2016)", ParagraphStyle('TC', fontName='Helvetica-Oblique', fontSize=9, alignment=TA_CENTER, textColor=colors.grey)),
    HRFlowable(width=W, thickness=2, color=colors.HexColor('#1a1a6e')),
    sp(8),
]

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — AN INVISIBLE WORLD
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("CHAPTER 1: AN INVISIBLE WORLD", h1))
story.append(HRFlowable(width=W, thickness=1, color=colors.HexColor('#1a1a6e')))
story.append(sp(4))

# Learning Outcomes
story.append(Paragraph("1.1  Learning Outcomes (Popa slide 2)", h2))
for item in [
    "Define microbiology and explain what a microorganism is",
    "List the key milestones in the history of microbiology",
    "Explain the basis of classification of microbes (three-domain system, binomial nomenclature)",
]:
    story.append(Paragraph(f"• {item}", bul))
story.append(sp())

# Definition
story.append(Paragraph("1.2  Defining Microbiology (Popa slide 3; OpenStax 1.1)", h2))
story.append(Paragraph(
    "Microbiology is the science that studies <b>microorganisms</b> — organisms too small to see "
    "with the unaided eye. Sub-disciplines are organized <b>by application</b> (medical, industrial, "
    "agricultural, environmental) or <b>by organism type</b> (bacteriology, virology, mycology, etc.).",
    bod))
story.append(sp(4))

# Size scale
story.append(Paragraph("1.3  Size Scale (Popa slide 3; OpenStax 1.1)", h2))
story.append(tbl([
    ["Object", "Approximate Size", "Visible without microscope?"],
    ["Virus",              "~100 nm",       "No"],
    ["Bacterium",          "~1 µm",         "No"],
    ["Plant / animal cell","~10–100 µm",    "Borderline (~100 µm threshold)"],
    ["Sand grain",         "~90 µm–2 mm",   "Yes"],
], [2.0*inch, 2.0*inch, 3.0*inch]))
story.append(sp())

# History
story.append(Paragraph("1.4  History of Microbiology (Popa slides 4–13; OpenStax 1.1–1.2)", h2))

story.append(Paragraph(B("Ancient world — disease concepts before microscopes:"), h3))
story.append(tbl([
    ["Person / Event", "Date", "What they did", "Why it matters for the test"],
    ["Fermented foods\n(Neolithic China)", "~7000 BC",
     "Rice, honey, fruit fermented in pottery jars",
     "Humans used microbes thousands of years before knowing they existed"],
    ["Otzi the Iceman", "~3300 BC\n(found 1991)",
     "Frozen mummy infected with Trichuris parasite eggs and Borrelia burgdorferi (Lyme disease); carried a fungus (Fomitopsis) with antibiotic properties",
     "Evidence that prehistoric humans attempted to treat infections"],
    ["Quarantine\n(Bible — Leviticus)", "Ancient",
     "Isolation of people with leprosy and other diseases",
     "Early recognition that disease could spread person to person"],
    ["Hippocrates\n(460–370 BC)", "Ancient Greece",
     "Father of Western medicine. Dismissed supernatural causes of disease. Said diseases have NATURAL causes from within patients or their environments. Wrote Hippocratic Corpus. Associated with Hippocratic Oath.",
     "First to argue disease = natural, not divine punishment. This is the foundation of medicine."],
    ["Thucydides\n(460–395 BC)", "Ancient Greece",
     "Survived Athenian plague (430–410 BC, killed 1/3 of Athens). Observed that survivors did NOT get re-infected even when caring for sick people.",
     "First recorded observation of IMMUNITY — the body remembers a disease"],
    ["Marcus Terentius Varro\n(116–27 BC)", "Ancient Rome",
     "In Res Rusticae (36 BC): 'certain minute creatures [animalia minuta] grow there which cannot be seen by the eye, which float in the air and enter the body through the mouth and nose and there cause serious diseases'",
     "First to propose invisible creatures cause disease — 1,700 years before germ theory was proven"],
    ["al-Razi (Rhazes)\n(854–925 AD)", "Islamic / Persia",
     "First to distinguish measles from smallpox. Selected hospital locations by hanging raw meat and choosing where it rotted slowest.",
     "Early experimental medicine; differential diagnosis"],
    ["Ibn Sina (Avicenna)\n(980–1037 AD)", "Islamic / Persia",
     "Canon of Medicine (1025): described contagion, organisms infected by foreign substances, illness transmitted by breath. Advanced quarantine practice.",
     "Canon used as medical textbook worldwide through the Renaissance"],
], [1.4*inch, 0.8*inch, 2.8*inch, 2.0*inch]))
story.append(sp())

story.append(Paragraph(B("Birth of microbiology — invention of the microscope:"), h3))
story.append(tbl([
    ["Person", "Date", "Microscope type", "Key contribution", "Critical distinction"],
    ["Zacharias Janssen\n(+ father Hans)", "Late 1500s–\nearly 1600s",
     "Compound\n(two lenses)",
     "Dutch spectacle-makers. May have invented the compound microscope, simple microscope, AND telescope.",
     "IMPORTANT: evidence is INCONCLUSIVE. They were secretive, never published, records lost. Neighbor Hans Lippershey also built same instruments. Cannot be confirmed as inventor."],
    ["Galileo Galilei\n(1564–1642)", "~1609",
     "Compound\n(two lenses)",
     "Used compound microscope to examine INSECT PARTS (compound eyes).",
     "NOT the discoverer of microorganisms. More famous for the telescope. Contribution = applying compound design to small objects."],
    ["Robert Hooke\n(1635–1703)", "1665",
     "Compound",
     "Published Micrographia (1665) — became a bestseller across Europe. Viewed thin slice of CORK. Saw box-like structures he called CELLS (Latin: cella = small room). Described them as resembling a honeycomb.",
     "Hooke saw DEAD PLANT CELL WALLS only — cells appeared hollow because cork cells are dead. He did NOT see living microorganisms."],
    ["Anton van Leeuwenhoek\n(1632–1723)", "1674–1675",
     "Simple\n(one lens — more powerful than compound of his era)",
     "Cloth merchant from Delft who became a lens-maker. First to see LIVING microorganisms. Called them animalcules ('wee little beasties'). Observed pond water, rain water, dental scrapings. Sent letters to Royal Society of London from 1673. Initially met with skepticism — Society sent delegation to verify. Became a celebrity (visited by Czar of Russia).",
     "KEY DISTINCTION from Hooke: Leeuwenhoek saw LIVING organisms. His drawings = bacteria and protists. Called 'father of microbiology.'"],
    ["Girolamo Fracastoro\n(Italian scholar)", "1546",
     "None\n(pre-microscope)",
     "De Contagione (1546): proposed disease spread by tiny invisible seminaria ('seeds of contagion') that attach to objects (fomes = cloth) and transfer person to person.",
     "Purely theoretical — no microscope to prove it. Conceptual precursor to germ theory."],
], [1.3*inch, 0.7*inch, 0.8*inch, 2.3*inch, 1.9*inch]))
story.append(sp())

story.append(Paragraph(B("Golden Age of Microbiology (1857–1914):"), h3))
story.append(tbl([
    ["Scientist", "Dates / Country", "Key Contributions", "What Popa emphasizes"],
    ["Louis Pasteur", "1822–1895\nFrance",
     "Disproved spontaneous generation (swan-neck flask — boiled broth stayed sterile until neck broken)\nProved microbes cause FERMENTATION\nInvented PASTEURIZATION (high heat, short time — kills spoilage organisms)\nDeveloped vaccines: chicken cholera, anthrax, RABIES\nCo-developed germ theory of disease",
     "Popa gave him a full slide (slide 8). Fermentation + pasteurization + vaccines + germ theory. All four testable."],
    ["Robert Koch", "1843–1910\nGermany",
     "Proved Bacillus anthracis causes ANTHRAX (1876) — first proof a single microbe causes a specific disease\nDeveloped KOCH'S POSTULATES: 4-step experimental proof that a microbe causes a disease\nMajor advances in pure culture technique (isolating single species)\nSolid agar medium = FANNY HESSE's idea — she was not credited",
     "Popa slide 9. Koch's postulates are tested repeatedly. Fanny Hesse always comes up — know her name."],
    ["Edward Jenner", "1749–1823\nEngland",
     "Observed: dairymaids who got mild COWPOX were protected from SMALLPOX\nHypothesis: cowpox provides protection\nExperiment: inoculated boy with cowpox fluid, later challenged with smallpox fluid\nResult: boy did not get smallpox\nDeveloped FIRST VACCINE (smallpox)",
     "Popa slide 7. Know the experiment structure (observation → hypothesis → experiment → result). Cowpox = vaccinia virus, smallpox = variola virus — related viruses."],
    ["Paul Ehrlich", "1854–1915\nGermany",
     "Concept of 'MAGIC BULLET' — a drug with SELECTIVE TOXICITY: kills the pathogen but not the host\nDeveloped SALVARSAN (arsenic compound, 1910) for syphilis — first modern chemotherapy drug\nFounded the field of chemotherapy",
     "Popa slide 11. Magic bullet = selective toxicity. Salvarsan = syphilis. These two facts are always tested."],
    ["Alexander Fleming", "1881–1955\nScotland",
     "Left a Staphylococcus plate open → contaminated with Penicillium mold → saw clear zone of NO bacterial growth around mold\nDiscovered PENICILLIN (1928)\nMass production in time for WW2 — saved countless soldiers' lives\nDr. Sarah Voureka (Greece) — colleague and later spouse — contributed significantly but received less credit",
     "Popa slides 12–13. The accidental discovery story is testable. Voureka mentioned by Popa specifically — know her name."],
], [1.1*inch, 0.9*inch, 3.2*inch, 1.8*inch]))
story.append(sp())

# Taxonomy and Classification
story.append(Paragraph("1.5  Taxonomy and Classification (Popa slides 10, 17–19; OpenStax 1.2–1.3)", h2))
story.append(Paragraph(B("History of classification:"), h3))
for item in [
    "Carolus Linnaeus (1758): established binomial nomenclature — genus + specific epithet; taxonomy hierarchy: Domain → Kingdom → Phylum → Class → Order → Family → Genus → Species",
    "Ernst Haeckel (1866): added Protista as third kingdom alongside Plants and Animals",
    "Robert Whittaker (1969): proposed 5 kingdoms (Animalia, Plantae, Fungi, Protista, Monera) + empire level",
    "Carl Woese & George Fox (1970s): used 16S rRNA sequences to establish three-domain system (Bacteria, Archaea, Eukarya) — replaced 5-kingdom system",
    "Bergey's Manual of Systematic Bacteriology (1923–present): standard reference for bacteria classification based on genetic, biochemical, and immunological characteristics; Gram-staining is a key differential",
]:
    story.append(Paragraph(f"• {item}", bul))
story.append(sp(4))

story.append(Paragraph(B("Binomial nomenclature rules (Popa slide 19):"), h3))
for item in [
    "Always two parts: Genus (capitalized) + specific epithet (lowercase)",
    "Always italicized: e.g., Escherichia coli, Staphylococcus aureus",
    "After first mention, genus may be abbreviated: E. coli, S. aureus",
]:
    story.append(Paragraph(f"• {item}", bul))
story.append(sp())

# Three-domain system
story.append(Paragraph("1.6  The Three-Domain System (Popa slides 17–18; OpenStax 1.3)", h2))
story.append(tbl([
    ["Domain", "Cell Type", "Key Features"],
    ["Bacteria", "Prokaryote", "Peptidoglycan cell walls; binary fission (no mitosis); diverse energy sources (organic/inorganic chemicals or photosynthesis); shapes: coccus, bacillus, spirillum/spirochete; CAN be pathogenic"],
    ["Archaea", "Prokaryote", "NO peptidoglycan cell walls (unique lipids); live in extreme environments; NOT known pathogens of humans; includes methanogens (landfills, gut), extreme halophiles (salt lakes), extreme thermophiles (hot springs like Yellowstone)"],
    ["Eukarya", "Eukaryote", "Membrane-bound nucleus; includes Protists (algae + protozoa), Fungi, Plants, Animals"],
], [1.2*inch, 1.2*inch, 4.6*inch]))
story.append(sp())

# The 8 groups
story.append(Paragraph("1.7  Major Groups of Microorganisms (Popa slides 20–28; OpenStax 1.3)", h2))
story.append(tbl([
    ["Group", "Domain", "Cell Type", "Cell Wall", "Energy", "Motility", "Pathogenic?", "Key Examples"],
    ["Bacteria", "Bacteria", "Prokaryote", "Peptidoglycan", "Varied (organic, inorganic, photosynthesis)", "Yes (flagella)", "Many are", "E. coli, Staphylococcus, Mycobacterium"],
    ["Archaea", "Archaea", "Prokaryote", "No peptidoglycan", "Varied", "Some", "NOT known human pathogens", "Methanobacterium, Halobacterium"],
    ["Algae (Protists)", "Eukarya", "Eukaryote", "Cellulose", "Photosynthesis", "Some", "Not pathogenic", "Diatoms, Chlamydomonas; agar from red algae"],
    ["Protozoa (Protists)", "Eukarya", "Eukaryote", "None (most)", "Absorb/ingest organics", "Pseudopods, cilia, or flagella", "Many are", "Giardia lamblia, Plasmodium, Trichomonas"],
    ["Fungi", "Eukarya", "Eukaryote", "Chitin", "Absorb organics", "No (mostly)", "Some are", "Candida (unicellular yeast), molds (multicellular), mushrooms"],
    ["Helminths", "Eukarya", "Eukaryote (multicellular)", "None", "Absorb organics (parasitic)", "Yes (adult)", "Yes (parasitic)", "Taenia saginata (beef tapeworm), Dracunculus medinensis (guinea worm)"],
    ["Viruses", "Acellular", "Acellular", "Protein coat (capsid)", "N/A — use host", "No", "Yes", "Coronavirus, Ebolavirus, HIV"],
    ["Prions", "Acellular", "Acellular (protein only)", "None", "N/A", "No", "Yes", "CJD, 'mad cow' disease (BSE)"],
], [0.85*inch, 0.75*inch, 0.75*inch, 0.85*inch, 0.95*inch, 0.6*inch, 0.7*inch, 1.55*inch]))
story.append(sp())

# Helminths detail
story.append(Paragraph(B("Helminths (Popa slide 26; OpenStax 1.3):"), h3))
for item in [
    "Technically multicellular animals — not microorganisms — but studied in microbiology because eggs and larval stages are microscopic",
    "Parasitic flatworms (Platyhelminthes: flukes, tapeworms) and roundworms (Nematoda)",
    "Example: Taenia saginata (beef tapeworm); Dracunculus medinensis (guinea worm)",
]:
    story.append(Paragraph(f"• {item}", bul))
story.append(sp(4))

# Viruses detail
story.append(Paragraph(B("Viruses (Popa slide 27; OpenStax 1.3):"), h3))
for item in [
    "Acellular — not made of cells",
    "Contain DNA OR RNA — never both",
    "Core surrounded by a protein coat (capsid)",
    "Capsid may be enclosed in a lipid envelope (from host cell membrane)",
    "Replicate ONLY when inside a living host cell",
    "Example: Coronavirus family (respiratory), Ebolavirus (hemorrhagic fever)",
]:
    story.append(Paragraph(f"• {item}", bul))
story.append(sp(4))

# Prions detail
story.append(Paragraph(B("Prions (Popa slide 28; OpenStax 1.3):"), h3))
for item in [
    "Contain NO nucleic acid — only protein",
    "Normal prion protein (PrPc) present in all mammal brain cells",
    "Misfolded prion protein (PrPsc) causes normal molecules to misfold",
    "Misfolded prions accumulate → form fibrils → cause cell death",
    "Result: degenerative CNS diseases (untreatable, fatal)",
    "Examples: Creutzfeldt-Jakob disease (CJD) in humans; bovine spongiform encephalopathy (BSE = 'mad cow' disease) in cattle",
    "Stanley Prusiner won Nobel Prize in Physiology or Medicine, 1998",
]:
    story.append(Paragraph(f"• {item}", bul))
story.append(sp(4))

# Modern microbiology
story.append(Paragraph("1.8  Modern Microbiology & Biotechnology (Popa slides 14–16; OpenStax 1.1–1.2)", h2))
story.append(tbl([
    ["Topic", "Description"],
    ["Human microbiome", "Microbes naturally inhabiting the human body (gut, skin, etc.); contribute to health and immunity; disruption linked to disease"],
    ["Genetic engineering", "Bacteria/fungi used to produce human proteins (insulin, vaccines, enzymes); gene therapy replaces missing or defective genes"],
    ["CRISPR", "Gene-editing technology based on normal bacterial immune processes; enables precise DNA changes"],
    ["Bioremediation", "Bacteria degrade environmental pollutants (oil spills: Deepwater Horizon 2010, Gulf of Mexico)"],
    ["Epidemiology", "Studies how diseases are transmitted in populations; tracks outbreaks and emerging diseases (COVID-19), recurring epidemics (flu)"],
    ["Bioterrorism agents", "CDC Category A agents (anthrax, smallpox, plague) require special preparedness"],
], [2.0*inch, 5.0*inch]))
story.append(sp())

# ── Chapter 1 Quick Summary ──────────────────────────────────────────────────
story.append(Paragraph("Chapter 1 — Key Facts to Memorize", h2))
story.append(tbl([
    ["Fact", "Detail"],
    ["Leeuwenhoek", "1675, described animalcules with simple microscope → first to observe microorganisms"],
    ["Pasteur", "Disproved spontaneous generation; fermentation = microbial; pasteurization; germ theory"],
    ["Koch", "Anthrax (1876); Koch's postulates; agar = Fanny Hesse's idea"],
    ["Jenner", "Cowpox vaccination prevents smallpox; first vaccine"],
    ["Woese & Fox", "1970s rRNA sequences → three-domain system (Bacteria / Archaea / Eukarya)"],
    ["Prions", "Protein only, no nucleic acid; misfolding cascade; CJD, BSE; Prusiner Nobel 1998"],
    ["Viruses", "Acellular; DNA OR RNA (never both); replicate only in host"],
    ["Archaea", "Prokaryote; NO peptidoglycan; NOT human pathogens; extremophiles"],
    ["Binomial nomenclature", "Genus + specific epithet; italicized; Genus capitalized; Linnaeus 1758"],
    ["Fungi cell wall", "Chitin (NOT peptidoglycan, NOT cellulose)"],
    ["Algae cell wall", "Cellulose; photosynthetic; NOT pathogenic; source of agar"],
], [2.5*inch, 4.5*inch]))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 2 — HOW WE SEE THE INVISIBLE WORLD
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("CHAPTER 2: HOW WE SEE THE INVISIBLE WORLD", h1))
story.append(HRFlowable(width=W, thickness=1, color=colors.HexColor('#1a1a6e')))
story.append(sp(4))

# 2.1 Properties of light
story.append(Paragraph("2.1  Properties of Waves and Light (Popa slides 4–5; OpenStax 2.1)", h2))
story.append(tbl([
    ["Property", "Definition"],
    ["Wavelength", "Distance between one peak of a wave and the next peak"],
    ["Amplitude", "Height of each peak (or depth of each trough)"],
    ["Frequency", "Rate of vibration of the wave; number of wavelengths per unit time"],
    ["Reflection", "Wave bounces off of a material"],
    ["Absorbance", "Material captures the energy of a light wave"],
    ["Transmission", "Wave travels through a material"],
    ["Transparency", "Material allows light to pass through (transmissive)"],
    ["Opacity", "Material blocks light (absorbs or reflects all)"],
], [2.0*inch, 5.0*inch]))
story.append(sp())

# 2.2 Refraction
story.append(Paragraph("2.2  Refraction and Immersion Oil (Popa slide 6; OpenStax 2.1)", h2))
for item in [
    "Refraction: bending of light as it passes from one medium into another with a different refractive index (RI)",
    "High-magnification lenses are very small; refracted light may miss the lens entirely",
    "Immersion oil fills the space between the 100× objective and the coverslip",
    "RI of immersion oil (~1.515) ≈ RI of glass — light passes through without bending",
    "Result: more light enters the objective → better resolution and brighter image",
]:
    story.append(Paragraph(f"• {item}", bul))
story.append(sp())

# 2.3 EM spectrum
story.append(Paragraph("2.3  Electromagnetic Spectrum (Popa slide 7; OpenStax 2.1)", h2))
story.append(Paragraph(
    "Visible light is a <b>narrow band</b> of the EM spectrum (roughly 400–700 nm), between UV and infrared. "
    "<b>Shorter wavelength = higher energy</b>; longer wavelength = less energy. "
    "Electron microscopes exploit this: electrons have far shorter wavelengths than visible light, "
    "giving much greater resolving power.",
    bod))
story.append(sp())

# 2.4 Magnification, Resolution, Contrast
story.append(Paragraph("2.4  Magnification, Resolution, and Contrast (Popa slide 8; OpenStax 2.1)", h2))
story.append(tbl([
    ["Term", "Definition", "Key Point"],
    ["Magnification", "Ability of a lens to enlarge the image compared to the real object", "Total magnification = ocular lens × objective lens (e.g., 10× × 100× = 1000×)"],
    ["Resolution\n(resolving power)", "Ability of the lens system to distinguish two adjacent points as separate", "Smaller resolvable distance = better resolution. Affected by wavelength (shorter = better) and numerical aperture (higher NA = better). Human eye ≈ 200 µm; light microscope ≈ 200 nm; TEM ≈ 2.5 nm"],
    ["Contrast", "Visible difference between the specimen and its background", "Staining and special illumination techniques (darkfield, phase-contrast) increase contrast"],
    ["Numerical Aperture (NA)", "Measure of a lens's ability to gather light", "Higher NA → better resolution; NA depends on RI of medium and half-angle of light cone"],
], [1.5*inch, 2.5*inch, 3.0*inch]))
story.append(sp())

# 2.5 History of microscopy
story.append(Paragraph("2.5  History of Microscopy (OpenStax 2.2)", h2))
story.append(tbl([
    ["Year / Person", "Contribution"],
    ["Late 1500s — Zacharias Janssen", "Credited with first compound microscope (two lenses)"],
    ["~1609 — Galileo Galilei", "Adapted compound microscope to study insects"],
    ["1665 — Robert Hooke", "Micrographia: described cells in cork; coined term 'cell'; used compound microscope"],
    ["1674–1675 — Anton van Leeuwenhoek", "Simple (single-lens) microscope; described animalcules from pond water, dental scrapings; reported to Royal Society of London"],
    ["1830 — Joseph Lister", "Achromatic lenses corrected chromatic aberration → modern light microscope"],
    ["1884 — Hans Christian Gram", "Developed Gram staining — most important differential stain"],
    ["1931 — Ernst Ruska", "First electron microscope (TEM); Nobel Prize 1986"],
    ["1981 — Gerd Binnig & Heinrich Rohrer", "Scanning tunneling microscope; Nobel Prize 1986"],
], [2.2*inch, 4.8*inch]))
story.append(sp())

# 2.6 Light Microscope Types
story.append(Paragraph("2.6  Types of Light Microscopes (Popa slides 9–14; OpenStax 2.2)", h2))
story.append(tbl([
    ["Type", "Mechanism", "Image Appearance", "Best Uses"],
    ["Brightfield\n(compound)", "Transmitted white light through specimen; specimen absorbs light", "Dark specimen on bright background", "Stained specimens; most common; up to 1000× (oil immersion); coarse focus 4×/10× only, fine focus 40×/100×"],
    ["Darkfield", "Opaque disk blocks direct light; only scattered/diffracted light enters objective", "Bright specimen on dark background", "Unstained live organisms; thin spirochetes (Treponema pallidum — syphilis); difficult to stain organisms"],
    ["Phase-contrast", "Annular stop + phase ring create destructive interference for direct light", "High-contrast grayscale; unstained", "Live unstained cells; internal organelles; endospores; Giemsa-stained cells"],
    ["DIC (Nomarski)", "Two polarized beams; interference creates 3D-like appearance", "3D shadow-cast look, full color", "Live unstained cells; thick specimens; research"],
    ["Fluorescence", "UV light excites fluorochromes → emit visible light (longer wavelength)", "Bright colored glow on dark background", "Immunofluorescence (DFA/IFA); MRSA testing; pathogens; antibody-tagged cells"],
    ["Confocal\n(laser scanning)", "Single laser focal plane; computer reconstructs 3D from z-slices", "Sharp 3D reconstructions", "Biofilms; thick specimens; live cell 3D imaging; 'CT scan of cells'"],
    ["Two-photon", "Infrared laser; two photons needed; only excites at focal point", "Deep tissue imaging", "Live tissue imaging; least phototoxicity; research"],
], [1.1*inch, 1.8*inch, 1.5*inch, 2.6*inch]))
story.append(sp())

# Fluorescence detail
story.append(Paragraph(B("Fluorescence microscopy details (Popa slide 13; OpenStax 2.2):"), h3))
for item in [
    "Fluorescent substances absorb UV light and emit visible light (Stokes shift — emission at longer wavelength than excitation)",
    "Cells may be stained with fluorescent dyes (fluorochromes: DAPI, FITC, rhodamine)",
    "Direct fluorescent antibody (DFA): fluorochrome attached directly to antibody",
    "Indirect fluorescent antibody (IFA): unlabeled primary antibody + fluorochrome-labeled secondary antibody (more sensitive)",
    "Applications: detection of Legionella, Chlamydia, Bordetella, rabies virus, MRSA typing",
]:
    story.append(Paragraph(f"• {item}", bul))
story.append(sp())

# 2.7 Electron Microscopy
story.append(Paragraph("2.7  Electron Microscopy (Popa slides 15–18; OpenStax 2.3)", h2))
story.append(Paragraph(
    "Electron microscopes use <b>electrons instead of light</b>. Electrons have much shorter wavelengths "
    "than visible light → <b>far greater resolution</b>. Cannot be used on living material (high vacuum required). "
    "Electromagnetic lenses focus electron beam.",
    bod))
story.append(sp(4))

story.append(tbl([
    ["Feature", "TEM\n(Transmission EM)", "SEM\n(Scanning EM)"],
    ["Principle", "Electrons pass THROUGH ultrathin specimen sections", "Electron beam SCANS the SURFACE of a whole specimen; secondary electrons detected"],
    ["Specimen prep", "Dehydration series (ethanol), embed in resin, ultramicrotome (20–100 nm sections), heavy metal staining (uranyl acetate, osmium tetroxide)", "Dehydration, critical-point drying (liquid CO₂), sputter-coat with gold/palladium (~10 nm layer)"],
    ["Image", "2D internal cross-section", "3D surface topography"],
    ["Magnification", "10,000–100,000×", "1,000–10,000×"],
    ["Resolution", "~2.5 nm", "~20 nm"],
    ["What you see", "Internal structures (ribosomes, membranes, inclusions)", "Surface features, attachment structures, 3D morphology"],
    ["Examples", "Internal virus structure, intracellular bacteria", "Biofilms, surface pili/flagella, spores"],
], [1.8*inch, 2.6*inch, 2.6*inch]))
story.append(sp())

# Scanning probe
story.append(Paragraph(B("Scanning probe microscopy (Popa slide 19; OpenStax 2.3):"), h3))
for item in [
    "Scanning tunneling microscope (STM): measures electron tunneling current; images individual atoms on conductive surfaces; up to 100,000,000×",
    "Atomic force microscope (AFM): mechanical probe feels surface contours; works on non-conductive materials (e.g., nanocellulose); research use only",
]:
    story.append(Paragraph(f"• {item}", bul))
story.append(sp())

# 2.8 Specimen preparation
story.append(Paragraph("2.8  Preparing Specimens for Light Microscopy (Popa slides 20–21; OpenStax 2.4)", h2))
story.append(tbl([
    ["Method", "Description", "When Used"],
    ["Wet mount", "Specimen in a drop of liquid under a coverslip; no fixation", "Quick look at live/motile organisms; fresh specimens"],
    ["Smear", "Thin film of liquid culture spread on slide and air-dried", "Preparation for fixation and staining"],
    ["Heat fixation", "Smear passed quickly through flame 2–3×; denatures proteins, kills organisms, adheres cells to slide", "Most common for bacteria"],
    ["Chemical fixation", "Immerse in acetic acid, ethanol, methanol, formalin, or glutaraldehyde", "Preserves fine structures; required for some stains and EM"],
], [1.4*inch, 3.3*inch, 2.3*inch]))
story.append(sp())

# 2.9 Staining overview
story.append(Paragraph("2.9  Staining Principles (Popa slide 22; OpenStax 2.4)", h2))
for item in [
    "Stains are salts composed of a positive ion and a negative ion — one of which is a chromophore (the colored part)",
    "Basic dyes: color is in the POSITIVE ion → attracted to negatively charged bacterial surfaces → positive staining (cells appear colored)",
    "Acidic dyes: color is in the NEGATIVE ion → repelled by negatively charged surfaces → negative staining (background stained, cells appear as halos)",
    "Common basic dyes: crystal violet, methylene blue, malachite green, safranin",
]:
    story.append(Paragraph(f"• {item}", bul))
story.append(sp())

# 2.10 Staining types
story.append(Paragraph("2.10  Types of Stains (Popa slides 22–32; OpenStax 2.4)", h2))
story.append(tbl([
    ["Stain Type", "Steps", "Results", "Purpose / Organisms"],
    ["Simple stain", "Fix smear → apply single basic dye (crystal violet, methylene blue, or safranin) 30–60 sec → water rinse → blot dry", "All cells same color", "Determine cell shape (coccus/bacillus/spirillum), arrangement (singles/pairs/chains/tetrads), and relative size"],
    ["Gram stain\n(differential)", "1. Crystal violet (primary) — all cells purple\n2. Gram's iodine (mordant) — CV-I complex formed\n3. Alcohol/acetone (decolorizer) — G+ thick peptidoglycan retains CV-I; G− thin peptidoglycan loses color\n4. Safranin (counterstain) — G− cells stain pink", "Gram+: PURPLE\nGram−: PINK/RED", "Most widely used differential stain; distinguishes two major bacterial groups based on cell wall structure; guides antibiotic selection (G+ generally more sensitive to penicillin)"],
    ["Acid-fast stain\n(Ziehl-Neelsen)", "1. Carbolfuchsin (hot, primary) — all cells pink\n2. Acid-alcohol (decolorizer) — waxy mycolic acid wall resists decolorization\n3. Methylene blue (counterstain) — non-AFB stain blue", "AFB: PINK/RED\nNon-AFB: BLUE", "Mycobacterium tuberculosis, M. leprae, Nocardia; waxy mycolic acid in cell wall resists most stains"],
    ["Capsule stain\n(negative)", "India ink or nigrosin stains background; cells remain unstained", "Cells appear as clear halos against dark background", "Visualizes polysaccharide capsules (protect against phagocytosis); Cryptococcus neoformans, Klebsiella pneumoniae"],
    ["Endospore stain\n(Schaeffer-Fulton)", "1. Malachite green + steam (primary) — drives stain into resistant spores\n2. Water wash — removes stain from vegetative cells\n3. Safranin (counterstain) — vegetative cells stain pink", "Endospores: GREEN\nVegetative cells: PINK", "Bacillus, Clostridium, Clostridioides (C. difficile); endospores survive boiling, disinfectants, desiccation"],
    ["Flagella stain", "Mordant (tannic acid or potassium alum) precipitates on flagella → thickens → visible with basic fuchsin/pararosaniline", "Flagella visible as dark lines", "Determine flagella number and arrangement; Bacillus cereus example; flagella too thin (~20 nm) to see without mordant"],
], [1.1*inch, 2.2*inch, 1.3*inch, 2.4*inch]))
story.append(sp())

# Gram stain summary box
story.append(Paragraph(B("Gram Stain — Why G+ stays purple (Popa slide 26; OpenStax 2.4):"), h3))
for item in [
    "G+ bacteria have THICK peptidoglycan cell wall (20–80 nm) — alcohol dehydrates and contracts it → pores close → CV-I complex trapped → PURPLE",
    "G− bacteria have THIN peptidoglycan (2–7 nm) + outer membrane — alcohol dissolves outer membrane lipids → CV-I washes out → colorless → safranin → PINK",
    "Hans Christian Gram developed the technique in 1884 while trying to stain bacteria in lung tissue",
    "Gram stain result guides antibiotic treatment — critical clinical test",
]:
    story.append(Paragraph(f"• {item}", bul))
story.append(sp())

# 2.11 Quick reference
story.append(Paragraph("Chapter 2 — Comparison Quick Reference", h2))
story.append(tbl([
    ["Microscope/Stain", "Key Number / Fact"],
    ["Human eye resolution", "~200 µm (need ~100 µm object to see without microscope)"],
    ["Brightfield (oil, 100×)", "Total magnification 1000×; resolution ~200 nm"],
    ["TEM magnification", "10,000–100,000×; resolution 2.5 nm; 2D internal sections"],
    ["SEM magnification", "1,000–10,000×; resolution 20 nm; 3D surface"],
    ["STM/AFM", "Up to 100,000,000×; individual atoms; research only"],
    ["Immersion oil RI", "~1.515 ≈ glass RI; prevents light scattering at 100× objective"],
    ["Gram stain: G+ result", "PURPLE (thick peptidoglycan retains crystal violet–iodine complex)"],
    ["Gram stain: G− result", "PINK (thin peptidoglycan + outer membrane; loses CV; counterstained with safranin)"],
    ["Acid-fast result", "AFB = PINK/RED (mycolic acid wall); non-AFB = BLUE (methylene blue counterstain)"],
    ["Endospore stain result", "Spores = GREEN (malachite green); vegetative cells = PINK (safranin)"],
    ["Capsule stain method", "Negative stain — background stained, capsule appears as clear halo"],
    ["Flagella stain requirement", "Mordant (tannic acid) needed — thickens flagella so they can be visualized"],
    ["Phase-contrast best use", "Live unstained specimens; visualizes internal structures without killing cells"],
    ["Confocal best use", "3D images of thick specimens; biofilms; z-plane optical sectioning"],
    ["Darkfield best use", "Treponema pallidum (syphilis); thin organisms difficult to stain"],
], [3.0*inch, 4.0*inch]))
story.append(sp())

story.append(Paragraph(
    "Sources: Popa BIO203 lecture slides (Ch.1: 29 slides; Ch.2: 33 slides) + "
    "OpenStax Microbiology (2016), Chapters 1–2. Version 2 — rebuilt from source material.",
    cit))

# ── build ─────────────────────────────────────────────────────────────────────
doc.build(story)
print("Done →", OUTPUT)
