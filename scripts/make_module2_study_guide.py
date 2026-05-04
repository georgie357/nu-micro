# BIO203 Module 2 Study Guide — Ch.3 Cell Structure, Ch.4 Prokaryotes,
# Ch.5 Eukaryotes, Ch.6 Acellular Pathogens
# Built from actual Popa lecture slides (BIO203.ch3-6.pptx) + Lab reports L3/L4/L5

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, HRFlowable)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\chapter 3 to 6\BIO203_Module2_Study_Guide.pdf"

h1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=16, spaceAfter=6,
                    textColor=colors.HexColor('#1a1a6e'))
h2 = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=13, spaceAfter=4,
                    spaceBefore=10, textColor=colors.HexColor('#1a1a6e'))
h3 = ParagraphStyle('H3', fontName='Helvetica-Bold', fontSize=10, spaceAfter=3,
                    spaceBefore=6)
bod = ParagraphStyle('BD', fontName='Helvetica', fontSize=9, spaceAfter=3, leading=13)
bul = ParagraphStyle('BL', fontName='Helvetica', fontSize=9, spaceAfter=2,
                     leading=13, leftIndent=14, firstLineIndent=-10)
tip = ParagraphStyle('TP', fontName='Helvetica-Bold', fontSize=8.5, spaceAfter=4,
                     leading=12, backColor=colors.HexColor('#fff3cd'),
                     borderPad=4, borderWidth=0.5, borderColor=colors.HexColor('#cc8800'))
lab_style = ParagraphStyle('LAB', fontName='Helvetica-Bold', fontSize=8.5, spaceAfter=4,
                     leading=12, backColor=colors.HexColor('#e8f4e8'),
                     borderPad=4, borderWidth=0.5, borderColor=colors.HexColor('#2d7a2d'))

cell_body = ParagraphStyle('cb', fontName='Helvetica', fontSize=8, leading=11, spaceAfter=0)
cell_bold = ParagraphStyle('cB', fontName='Helvetica-Bold', fontSize=8, leading=11, spaceAfter=0)


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
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t


def B(text): return f'<b>{text}</b>'
def sp(n=6): return Spacer(1, n)
def HY(text): return Paragraph(f'HIGHEST YIELD: {text}', tip)
def LAB(text): return Paragraph(f'LAB CONNECTION: {text}', lab_style)


doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
                        topMargin=0.75 * inch, bottomMargin=0.75 * inch)
W = 7.0 * inch
story = []

# ─── TITLE ───────────────────────────────────────────────────────────────────
story += [
    Paragraph("BIO203 Microbiology — National University",
              ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=20,
                             alignment=TA_CENTER, textColor=colors.HexColor('#1a1a6e'))),
    Spacer(1, 4),
    Paragraph("Module 2 Study Guide — Chapters 3, 4, 5, 6",
              ParagraphStyle('TS', fontName='Helvetica-Bold', fontSize=14, alignment=TA_CENTER)),
    Spacer(1, 3),
    Paragraph("Cell Structure | Prokaryotic Diversity | Eukaryotes | Acellular Pathogens",
              ParagraphStyle('TS2', fontName='Helvetica', fontSize=11, alignment=TA_CENTER,
                             textColor=colors.grey)),
    Spacer(1, 3),
    Paragraph("Source: Popa BIO203 lecture slides (ch3–ch6) + Lab 3/4/5 reports",
              ParagraphStyle('TC', fontName='Helvetica-Oblique', fontSize=9,
                             alignment=TA_CENTER, textColor=colors.grey)),
    HRFlowable(width=W, thickness=2, color=colors.HexColor('#1a1a6e')),
    sp(8),
]

# ═══════════════════════════════════════════════════════════════════════════════
# CHAPTER 3 — THE CELL
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("CHAPTER 3: THE CELL", h1))

story.append(Paragraph("3.1 History: Spontaneous Generation → Cell Theory", h2))
story.append(Paragraph(
    f"{B('Spontaneous generation')} (Aristotle): life arises from non-living matter (\"pneuma\"). "
    f"Challenged by Redi (1668) — maggots only from fly eggs, not spontaneously. "
    f"Needham's covered broth seemed to support it. "
    f"Definitively disproved by {B('Pasteur')} (swan-neck flask): boiled broth stayed sterile "
    f"until neck broken. Coined {B('\"Omne vivum ex vivo\"')} — life only from life.", bod))
story.append(Paragraph(
    f"{B('Cell theory:')} Schwann (animal cells) + Schleiden (plant cells) established cells "
    f"as basic unit. Robert Remak: cells arise by division. "
    f"{B('Virchow: omnis cellula a cellula')} (all cells from cells).", bod))
story.append(Paragraph(
    f"{B('Endosymbiotic theory:')} Mitochondria and chloroplasts have own DNA and divide "
    f"independently → originally free-living bacteria that became symbionts with eukaryotic cells.", bod))
story.append(Paragraph(
    f"{B('Germ theory of disease (Koch):')} Semmelweis (handwashing → puerperal fever), "
    f"John Snow (cholera → contaminated water), Lister (surgical antisepsis), "
    f"Koch's postulates (identify which microbe causes which disease).", bod))

story.append(Paragraph("3.2 Prokaryote vs Eukaryote Comparison", h2))
story.append(HY("This comparison is the most-tested concept in Module 2. Know every row."))
story.append(tbl([
    ['Feature', 'Prokaryotes', 'Eukaryotes'],
    ['Nucleus', 'NO — nucleoid region (no membrane)', 'YES — membrane-bound nuclear envelope'],
    ['DNA', 'One circular chromosome; no histones; NAPs organize DNA', 'Paired linear chromosomes; histones → nucleosomes'],
    ['Organelles', 'NONE (no membrane-bound)', 'YES: ER, Golgi, mitochondria, lysosomes, etc.'],
    ['Ribosomes', '70S (30S + 50S) — antibiotic target', '80S (40S + 60S); 70S inside mitochondria/chloroplasts'],
    ['Cell wall', 'Peptidoglycan (bacteria); pseudomurein (Archaea)', 'Cellulose (plants), chitin (fungi), none (animals)'],
    ['Cell division', 'Binary fission', 'Mitosis; budding (some fungi)'],
    ['Size', '~0.2–2.0 µm diam; 2–8 µm length', 'Typically 10–100 µm'],
    ['Higher surface-to-volume', 'YES → grow faster than eukaryotes', 'NO'],
], [1.5 * inch, 2.7 * inch, 2.6 * inch]))
story.append(sp(4))

story.append(Paragraph("3.3 Prokaryotic Cell Structures — from Slide", h2))

story.append(Paragraph(B("Internal structures:"), h3))
story.append(Paragraph(
    f"• {B('Nucleoid:')} region (not membrane-bound) with one circular chromosome. Organized by "
    f"{B('NAPs')} (nucleoid-associated proteins) in bacteria; Archaea use NAPs or histone-like proteins.", bul))
story.append(Paragraph(
    f"• {B('Plasmids:')} small, extrachromosomal, circular dsDNA. Usually 5–100 genes. "
    f"Replicate independently. Can be transferred cell-to-cell (carry antibiotic resistance genes).", bul))
story.append(Paragraph(
    f"• {B('Ribosomes (70S):')} sites of protein synthesis; composed of protein + rRNA. "
    f"Smaller than eukaryotic (80S) → antibiotics selectively target them (e.g. streptomycin, tetracycline).", bul))
story.append(Paragraph(
    f"• {B('Inclusions:')} cytoplasmic storage granules — glycogen, starches, volutin "
    f"(metachromatic = inorganic phosphate), lipids, sulfur. "
    f"Special inclusions: gas vacuoles (buoyancy), magnetosomes, carboxysomes (carbon fixation).", bul))

story.append(Paragraph(B("Endospores (EXAM FAVORITE):"), h3))
story.append(Paragraph(
    f"Resting structures formed by {B('Bacillus')} and {B('Clostridium')} (Gram-positive) when "
    f"key nutrients (carbon, nitrogen) become scarce. Highly durable: dehydrated, thick walls, "
    f"additional protective layers. Formed inside the vegetative cell; when done, vegetative cell "
    f"disintegrates and endospore is free. Can be at the center or end of cell.", bod))
story.append(Paragraph(
    f"{B('Germination:')} endospore returns to vegetative cell when triggered by physical/chemical "
    f"damage to spore coat → forms a single cell. "
    f"{B('NOT a reproduction method — a survival system.')}", bod))
story.append(HY("Endospores survive boiling, UV, bleach. Only autoclaving (121°C, 15 min) reliably destroys them. "
                "Stain with Schaeffer-Fulton (malachite green heat stain)."))

story.append(Paragraph(B("Plasma membrane:"), h3))
story.append(Paragraph(
    f"Phospholipid bilayer with peripheral and integral (transmembrane) proteins. "
    f"Photosynthetic bacteria have infoldings called {B('chromatophores')} containing pigments.", bod))

story.append(Paragraph(B("Membrane transport (slide-specific):"), h3))
story.append(tbl([
    ['Mechanism', 'Energy?', 'Notes'],
    ['Simple diffusion', 'No', 'Down concentration gradient'],
    ['Osmosis', 'No', 'Diffusion of water'],
    ['Facilitated diffusion', 'No', 'Requires carrier proteins'],
    ['Active transport', 'Yes (ATP)', 'Against gradient'],
    ['Group translocation', 'Yes', 'BACTERIA ONLY — sugars phosphorylated as they cross'],
    ['Endocytosis / Engulfment', 'Yes', 'EUKARYOTES ONLY — pinocytosis, phagocytosis'],
], [2.0 * inch, 0.8 * inch, 4.0 * inch]))
story.append(sp(4))

story.append(Paragraph("3.4 Cell Wall", h2))
story.append(Paragraph(
    f"Semi-rigid structure; gives shape, protects from osmotic lysis; anchor for flagella; "
    f"target of antibiotics (e.g. penicillin blocks peptidoglycan synthesis). "
    f"Made of {B('peptidoglycan')} = repeating disaccharide of {B('NAG')} (N-acetylglucosamine) "
    f"+ {B('NAM')} (N-acetylmuramic acid), cross-linked by polypeptides.", bod))

story.append(Paragraph(B("Gram stain steps (memorize in order):"), h3))
story.append(tbl([
    ['Step', 'Reagent', 'Gram+', 'Gram−'],
    ['1. Primary stain', 'Crystal violet', 'Purple', 'Purple'],
    ['2. Mordant', "Gram's iodine", 'Crystal violet-iodine complex (CV-I) too large to escape thick PG', 'CV-I too large to escape (yet)'],
    ['3. Destain', 'Alcohol', 'Dehydrates PG → CV-I stays IN → purple', 'Dissolves outer membrane → CV-I leaks OUT → colorless'],
    ['4. Counterstain', 'Safranin', 'Still purple (safranin masked)', 'Stains pink/red'],
], [1.0 * inch, 1.2 * inch, 2.5 * inch, 2.1 * inch]))
story.append(sp(4))

story.append(tbl([
    ['Feature', 'Gram-positive', 'Gram-negative'],
    ['Peptidoglycan', 'THICK (multiple layers)', 'THIN (single layer in periplasm)'],
    ['Teichoic acids', 'YES', 'NO'],
    ['Outer membrane', 'NO', 'YES — contains LPS'],
    ['LPS / Endotoxin', 'NO', 'YES — lipid A = endotoxin → septic shock'],
    ['Periplasmic space', 'Small', 'Large (between outer memb + plasma memb)'],
    ['Gram stain result', 'Purple', 'Pink/Red'],
    ['Antibiotic resistance', 'More susceptible to penicillin', 'Often resistant — LPS is barrier'],
], [1.5 * inch, 2.5 * inch, 2.8 * inch]))
story.append(sp(4))

story.append(Paragraph(B("Atypical cell walls:"), h3))
story.append(Paragraph(
    f"• {B('Acid-fast (Mycobacterium, Nocardia):')} waxy mycolic acid bound to peptidoglycan. "
    f"Usually Gram-variable. Very resistant to antibiotics; slow-growing. "
    f"Detected by Ziehl-Neelsen (acid-fast) stain. Causes TB, leprosy.", bul))
story.append(Paragraph(
    f"• {B('Mycoplasma:')} NO cell wall; sterols in plasma membrane. "
    f"Causes walking pneumonia (M. pneumoniae).", bul))
story.append(Paragraph(
    f"• {B('Archaea:')} wall-less OR pseudomurein — lacks NAM and D-amino acids "
    f"(not affected by penicillin).", bul))

story.append(Paragraph("3.5 External Structures", h2))
story.append(Paragraph(
    f"• {B('Glycocalyx:')} sugar coat = 2 types: {B('capsule')} (organized, thick) and "
    f"{B('slime layer')} (unorganized, loose). Functions: adhesion, biofilm, protection from "
    f"desiccation and phagocytosis. S-layer = proteins/glycoproteins (protection, immune interaction).", bul))
story.append(Paragraph(
    f"• {B('Fimbriae:')} short hairlike appendages of pilin protein; allow attachment to surfaces "
    f"(e.g. E. coli O157 attaches to small intestine). Distributed over surface or at poles.", bul))
story.append(Paragraph(
    f"• {B('Pili (sex pili):')} 1–2 per cell; longer than fimbriae. Join two cells for "
    f"{B('conjugation')} (DNA transfer).", bul))
story.append(Paragraph(
    f"• {B('Flagella:')} motility; filament (flagellin protein) + hook + basal body. "
    f"Arrangements from slide:", bul))
story.append(tbl([
    ['Arrangement', 'Description'],
    ['Atrichous', 'No flagella'],
    ['Monotrichous', 'Single polar flagellum'],
    ['Amphitrichous', 'Tuft of flagella at EACH end of cell'],
    ['Peritrichous', 'Flagella distributed over ENTIRE cell surface'],
], [1.8 * inch, 5.0 * inch]))
story.append(sp(4))
story.append(Paragraph(
    f"• {B('Axial filaments (endoflagella):')} in spirochetes (Treponema, Borrelia). "
    f"Anchored at one end; rotation causes cell to corkscrew through tissue.", bul))

story.append(Paragraph("3.6 Eukaryotic Cell Features", h2))
story.append(Paragraph(
    f"Eukaryotes have {B('cilia')} (shorter, unique to eukaryotes) and {B('flagella')} "
    f"(flexible whip of microtubules — different from prokaryotic flagellin). "
    f"Cytoplasmic membrane contains {B('sterols')} (unlike most bacteria). "
    f"Cell walls: fungi (chitin), plants (cellulose), algae (various polysaccharides), "
    f"most protists and animals have none.", bod))

story.append(Paragraph(B("Endomembrane system:"), h3))
story.append(Paragraph(
    f"• {B('Rough ER:')} ribosomes on surface → protein synthesis. "
    f"• {B('Smooth ER:')} phospholipid synthesis. "
    f"• {B('Golgi apparatus:')} packaging and distribution → makes glycolipids and glycoproteins "
    f"(commonly inserted in plasma membrane). "
    f"• {B('Lysosomes:')} digestive enzymes → break down particles, microorganisms, damaged organelles. "
    f"• {B('Peroxisomes:')} NOT part of endomembrane; lipid biosynthesis + molecule breakdown.", bod))

story.append(Paragraph(B("Cytoskeleton:"), h3))
story.append(Paragraph(
    f"• {B('Microfilaments')} (thinnest): actin pairs → ameboid movement, cytokinesis, muscle contraction. "
    f"• {B('Intermediate filaments')} (strongest): various proteins → nuclear lamina, desmosomes. "
    f"• {B('Microtubules')} (hollow, largest): tubulin dimers → form cilia/flagella + mitotic spindle.", bod))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 — PROKARYOTIC DIVERSITY
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("CHAPTER 4: PROKARYOTIC DIVERSITY", h1))

story.append(Paragraph("4.1 Overview & Classification", h2))
story.append(Paragraph(
    f"Prokaryotes = unicellular; no nucleus; includes Bacteria and Archaea. Found in virtually "
    f"all environments. Classified by: {B('Bergey' + chr(39) + 's Manual')} (morphology, physiology, biochemistry), "
    f"Gram staining, GC content of DNA, sequence similarities.", bod))
story.append(Paragraph(
    f"{B('Human microbiome:')} all prokaryotes (mostly bacteria) living in/on the human body. "
    f"Changes among body regions; affected by diet, lifestyle, environment.", bod))

story.append(Paragraph("4.2 Proteobacteria — Gram-negative, chemoheterotrophs (5 Classes)", h2))
story.append(HY("Proteobacteria is the largest, most diverse phylum. Know each class + at least 2 pathogens per class."))
story.append(tbl([
    ['Class', 'Key Genera', 'Diseases / Importance (from slides)'],
    ['Alpha', 'Rickettsia (obligate intracellular), Brucella, Bartonella, Ehrlichia, Nitrobacter, Rhizobium, Azospirillum',
     'Rocky Mountain spotted fever, cat-scratch disease, brucellosis, ehrlichiosis; nitrogen fixation (Rhizobium in plant roots)'],
    ['Beta', 'Neisseria (G− cocci), Bordetella, Burkholderia',
     'N. meningitidis (meningitis), N. gonorrhoeae (gonorrhea), B. pertussis (whooping cough), nosocomial infections'],
    ['Gamma', 'E. coli, Salmonella, Vibrio, Pseudomonas, Haemophilus, Legionella, Francisella',
     'Largest/most diverse; V. cholerae (cholera); P. aeruginosa (cystic fibrosis, burn patients — very resistant); Acinetobacter (extremely resistant)'],
    ['Delta', 'Desulfovibrio, Bdellovibrio, Myxococcus',
     'Use sulfur instead of O₂ as final electron acceptor; Bdellovibrio preys on other bacteria; myxobacteria form myxospores'],
    ['Epsilon', 'Helicobacter, Campylobacter',
     'H. pylori (peptic ulcers, stomach cancer); C. jejuni (gastroenteritis, microaerophilic, one polar flagellum)'],
], [1.0 * inch, 2.3 * inch, 3.5 * inch]))
story.append(sp(4))

story.append(Paragraph("4.3 Gram-negative Non-Proteobacteria", h2))
story.append(Paragraph(
    f"• {B('Spirochetes:')} axial filament inside (endoflagella) → corkscrew motility. "
    f"Borrelia burgdorferi (Lyme disease), Treponema pallidum (syphilis), Leptospira (leptospirosis).", bul))
story.append(Paragraph(
    f"• {B('Cyanobacteria:')} oxygenic photosynthesis; critical O₂ producers; nitrogen fixation. "
    f"Photosynthetic bacteria (purple/green sulfur) do anoxygenic photosynthesis (use S²⁻ instead of H₂O).", bul))
story.append(Paragraph(
    f"• {B('Bacteroidetes:')} Bacteroides (large intestine, degrade complex carbs), "
    f"Prevotella (mouth), Cytophaga (soil, cellulose-degrading).", bul))
story.append(Paragraph(
    f"• {B('Fusobacterium:')} found in mouth; cause dental abscesses.", bul))

story.append(Paragraph("4.4 Gram-positive Bacteria", h2))
story.append(Paragraph(
    f"Classified by {B('GC content')} (guanine + cytosine percent in DNA):", bod))
story.append(tbl([
    ['Group', 'GC content', 'Key genera + diseases (from slides)'],
    ['Actinobacteria', 'HIGH GC',
     'Mycobacterium (TB = M. tuberculosis; leprosy = M. leprae), Corynebacterium (diphtheria), '
     'Streptomyces (antibiotics!), Propionibacterium acnes (acne), Gardnerella (vaginitis), '
     'Bifidobacteria (gut probiotics), Nocardia, Frankia'],
    ['Firmicutes — Clostridia', 'LOW GC',
     'Clostridium: endospore-forming obligate anaerobes — C. tetani (tetanus), C. botulinum (botulism), '
     'C. perfringens (gas gangrene), C. difficile (colitis)'],
    ['Firmicutes — Lactobacillales', 'LOW GC',
     'Lactobacillus (lactic acid, gut/vagina), Streptococcus (many pathogens, classified by hemolysis: alpha/beta), '
     'Enterococcus (GI tract, hospital contaminants), Listeria (grows at refrigeration temp, survives inside phagocytes)'],
    ['Firmicutes — Bacilli order', 'LOW GC',
     'Bacillus (endospore rods, soil): B. anthracis (anthrax), B. cereus (food poisoning), B. thuringiensis (Bt toxin); '
     'Staphylococcus (cocci, salt-resistant): S. aureus → MRSA; Mycoplasma: no cell wall, M. pneumoniae (walking pneumonia)'],
], [1.4 * inch, 0.7 * inch, 4.7 * inch]))
story.append(sp(4))

story.append(Paragraph("4.5 Deeply Branching Bacteria & Archaea", h2))
story.append(Paragraph(
    f"• {B('Deeply branching bacteria:')} ancient, close to LUCA (last universal common ancestor). "
    f"Many are extremophiles. "
    f"{B('Deinococcus radiodurans')} = \"Conan the bacterium\" — extremely radiation-resistant. "
    f"Thermotoga (hyperthermophile).", bul))
story.append(Paragraph(
    f"• {B('Archaea:')} distinct domain. NO known human pathogens. "
    f"Cell wall = pseudomurein (lacks NAM, D-amino acids) or no wall. "
    f"Ether-linked membrane lipids (vs ester-linked in bacteria).", bul))
story.append(tbl([
    ['Archaea Group', 'Habitat / Key feature'],
    ['Hyperthermophiles', 'Hot springs, hydrothermal vents — Pyrodictium, Sulfolobus'],
    ['Methanogens', 'Strictly anaerobic; produce methane (gut, swamps, sewage) — Methanobacterium; industrial use'],
    ['Extreme halophiles', 'High salt — Halobacterium, Halococcus'],
], [1.8 * inch, 5.0 * inch]))
story.append(sp(4))
story.append(HY("Archaea key differences from bacteria: (1) no peptidoglycan — pseudomurein instead, "
                "(2) ether-linked lipids in membrane, (3) no human pathogens known, "
                "(4) use histone-like proteins (like eukaryotes)."))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 — EUKARYOTES OF MICROBIOLOGY
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("CHAPTER 5: THE EUKARYOTES OF MICROBIOLOGY", h1))

story.append(Paragraph("5.1 Protists & Protozoa", h2))
story.append(Paragraph(
    f"{B('Protists')} = not a formal taxonomic group; polyphyletic. Three types: "
    f"animal-like (protozoa), plant-like (algae), fungus-like (water molds). "
    f"Most protozoa placed across {B('6 supergroups')} based on evolutionary history. "
    f"Eukaryotic supergroups containing most protozoa: Amoebozoa, Excavata, Chromalveolata.", bod))
story.append(tbl([
    ['Supergroup', 'Movement', 'Important examples (from slides)', 'Disease'],
    ['Amoebozoa', 'Pseudopods', 'Entamoeba histolytica, slime molds', 'Dysentery (amebic)'],
    ['Chromalveolata\n(Apicomplexa)', 'Non-motile; apical complex for host invasion', 'Plasmodium, Toxoplasma, Cryptosporidium', 'Malaria, toxoplasmosis'],
    ['Chromalveolata\n(Ciliates)', 'Cilia; cytostome + cytoproct', 'Paramecium', 'Model organism'],
    ['Excavata', 'Flagella', 'Giardia lamblia, Trypanosoma', 'Giardiasis, sleeping sickness/Chagas'],
], [1.3 * inch, 1.5 * inch, 2.2 * inch, 1.8 * inch]))
story.append(sp(4))
story.append(Paragraph(
    f"Note: Amoeba has pseudopods + distinct cytoplasm layers; Euglena has flagellum; "
    f"Paramecium has cytostome (ingestion) + cytoproct (excretion); "
    f"many protozoa have contractile vacuole (water regulation).", bod))
story.append(LAB("Lab 1: You observed Trypanosoma trypomastigotes in a blood smear — the kinetoplast "
                 "(near flagellum base) distinguishes it from host RBCs."))

story.append(Paragraph("5.2 Helminths (Parasitic Worms)", h2))
story.append(Paragraph("Multicellular animals studied in microbiology because eggs/larvae are microscopic:", bod))
story.append(tbl([
    ['Group', 'Features', 'Key species'],
    ['Nematoda\n(roundworms)', '>15,000 species; unsegmented, full digestive system; egg or larvae infective',
     'Ascaris lumbricoides (small intestine), Trichuris trichiura (whipworm), '
     'Enterobius (pinworm), hookworms, Trichinella spiralis, heartworm'],
    ['Trematoda\n(flukes)', 'Flat, leaf-shaped; suckers; complicated life cycle',
     'Schistosoma (schistosomiasis)'],
    ['Cestoda\n(tapeworms)', 'Segmented ribbon; scolex with suckers/hooks; NO digestive system — absorbs nutrients',
     'Taenia (beef/pork tapeworm)'],
], [1.2 * inch, 2.5 * inch, 3.1 * inch]))
story.append(sp(4))

story.append(Paragraph("5.3 Fungi", h2))
story.append(Paragraph(
    f"Eukaryotic heterotrophs. Cell wall = {B('chitin')}. Decomposers, mutualists, pathogens. "
    f"Important for antibiotics (penicillin from Penicillium).", bod))
story.append(tbl([
    ['Form', 'Structure', 'Examples'],
    ['Yeasts', 'Unicellular; reproduce by budding or fission; aerobic or anaerobic (fermentation)', 'Saccharomyces (bread, alcohol), Candida (thrush)'],
    ['Molds + fleshy fungi', 'Filamentous hyphae (with or without septa) → thallus (body); vegetative or reproductive/aerial hyphae; visible mycelium', 'Rhizopus (black bread mold), Penicillium, Aspergillus'],
    ['Dimorphic', 'Mold at 25°C (environmental) / yeast at 37°C (in host body)', 'Histoplasma, Coccidioides, Blastomyces'],
], [1.0 * inch, 3.2 * inch, 2.6 * inch]))
story.append(sp(4))
story.append(Paragraph(B("Medically important groups (from slides):"), h3))
story.append(Paragraph(
    f"• {B('Zygomycota:')} conjugation fungi. Rhizopus (black bread mold), Mucor. "
    f"• {B('Ascomycota:')} sac fungi (includes most yeasts). Trichophyton, Microsporum (athlete's foot, ringworm). "
    f"• {B('Anamorphs:')} asexual fungi. Candida, Pneumocystis. "
    f"• {B('Basidiomycota:')} Cryptococcus.", bod))

story.append(Paragraph("5.4 Algae", h2))
story.append(Paragraph(
    f"Photosynthetic eukaryotes. Unicellular or multicellular. Important O₂ producers and "
    f"organic matter source. Types: diatoms, dinoflagellates (microscopic); kelp, seaweed (macroscopic).", bod))
story.append(Paragraph(
    f"• {B('Diatoms:')} produce {B('domoic acid')} (toxin — amnesic shellfish poisoning).", bul))
story.append(Paragraph(
    f"• {B('Dinoflagellates:')} produce neurotoxins → {B('paralytic shellfish poisoning')} and ciguatera.", bul))
story.append(Paragraph(
    f"• {B('Agar:')} used in laboratory media → produced from seaweed.", bul))

story.append(Paragraph("5.5 Lichens", h2))
story.append(Paragraph(
    f"Symbiosis of green algae (or cyanobacteria) + a fungus. Slow-growing, live for centuries. "
    f"Important in environment as pioneer species and air quality indicators.", bod))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 — ACELLULAR PATHOGENS
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("CHAPTER 6: ACELLULAR PATHOGENS", h1))

story.append(Paragraph("6.1 General Characteristics of Viruses", h2))
story.append(Paragraph(
    f"Viruses = {B('acellular')} (not cells), 20–900 nm. Also called {B('virions')} when infectious. "
    f"Obligate intracellular parasites — use host metabolic machinery. "
    f"All contain {B('DNA or RNA')} (never both) + a {B('protein coat (capsid)')}. "
    f"Some enclosed by an {B('envelope')} (lipid bilayer from host). "
    f"Host range determined by specific attachment sites on host cell.", bod))
story.append(Paragraph(
    f"Capsid shapes: {B('helical')}, {B('polyhedral')} (icosahedral), or {B('complex')} (bacteriophages). "
    f"Bacteriophages infect bacteria.", bod))

story.append(Paragraph("6.2 Viral Life Cycles", h2))
story.append(Paragraph(B("Lytic cycle (virulent phages — host cell dies):"), h3))
story.append(Paragraph(
    f"Steps: {B('Attachment → Penetration → Biosynthesis → Maturation → Release (lysis)')}", bod))
story.append(Paragraph(B("Lysogenic cycle (temperate phages — dormant):"), h3))
story.append(Paragraph(
    f"Viral DNA integrates into host chromosome as {B('prophage')}. Replicates passively with host "
    f"(no harm). If induced (UV, stress), switches to lytic cycle.", bod))
story.append(Paragraph(B("Animal virus life cycle (differences from phages):"), h3))
story.append(Paragraph(
    f"• Entry = {B('endocytosis')} (not injection). "
    f"• Extra step: {B('uncoating')} (release from capsid). "
    f"• Release = {B('budding')} (acquires envelope from host membrane).", bod))

story.append(Paragraph("6.3 Viral Nucleic Acid Processing", h2))
story.append(tbl([
    ['Genome type', 'Replication strategy'],
    ['dsDNA (double-stranded)', 'Transcribed by cellular or viral enzymes (normal)'],
    ['ssDNA (single-stranded)', 'Strand copied first to make dsDNA'],
    ['ss (+) RNA', 'Acts directly as mRNA; makes RNA-dependent RNA polymerase; uses (−) strand as template'],
    ['ss (−) RNA', 'Copied to make mRNA using own polymerase'],
    ['Retroviruses (ssRNA-RT)', 'Carry reverse transcriptase → RNA → DNA → inserted into host DNA. Target of anti-HIV drugs.'],
], [2.0 * inch, 4.8 * inch]))
story.append(sp(4))
story.append(HY("Retroviruses (HIV): reverse transcriptase makes DNA from viral RNA, which integrates into host genome. "
                "Reverse transcriptase = major antiviral drug target."))

story.append(Paragraph("6.4 Types of Viral Infections", h2))
story.append(tbl([
    ['Type', 'Description', 'Example'],
    ['Acute', 'Short-term, resolved by immune system', 'Flu, common cold'],
    ['Latent', 'Virus stays in asymptomatic host; can reactivate', 'Herpes (cold sores), chickenpox/shingles (VZV)'],
    ['Chronic', 'Long-term disease process, often fatal', 'HIV/AIDS, subacute sclerosing panencephalitis (measles virus)'],
], [1.0 * inch, 3.3 * inch, 2.5 * inch]))
story.append(sp(4))
story.append(Paragraph(
    f"VZV example: dsDNA genome incorporates into host DNA. After latency, reactivates as "
    f"{B('shingles')} (painful localized rash, one side of body).", bod))
story.append(Paragraph(
    f"HIV example: remains hidden in tissues; as immune damage mounts → AIDS develops.", bod))

story.append(Paragraph("6.5 Viral Growth Curve & Detection", h2))
story.append(Paragraph(B("Growth curve phases:"), h3))
story.append(Paragraph(
    f"1. {B('Inoculation')} — attachment to host cells. "
    f"2. {B('Eclipse')} — virions inside cells (can't detect any outside). "
    f"3. {B('Burst')} — virions released.", bod))
story.append(Paragraph(B("Culturing methods:"), h3))
story.append(Paragraph(
    f"• Bacteriophages: added to {B('bacterial lawns')}; counted by {B('plaques')} (clear zones = lysis). "
    f"• Animal viruses: embryo cells (often eggs) or live animals. "
    f"Separated from cells by filtration/centrifugation (viruses too small to filter out).", bod))
story.append(Paragraph(B("Detection methods:"), h3))
story.append(Paragraph(
    f"• {B('Cytopathic effects (CPE)')} — visible cell damage. "
    f"• Molecular: PCR, RT-PCR. "
    f"• Enzyme immunoassays. "
    f"• Hemagglutination / hemagglutination inhibition assay.", bod))

story.append(Paragraph(B("Transduction:"), h3))
story.append(Paragraph(
    f"Genetic exchange in bacteria using viruses as 'messengers.' "
    f"Can be {B('generalized')} (any bacterial DNA) or {B('specialized')} (specific genes only).", bod))

story.append(Paragraph("6.6 Viroids, Virusoids, and Prions", h2))
story.append(tbl([
    ['Agent', 'Structure', 'Replication', 'Disease'],
    ['Viroid', 'Small circular ssRNA — no protein coat', 'Self-replicating', 'Plant diseases only (e.g. potato spindle tuber viroid)'],
    ['Virusoid', 'Non-self-replicating ssRNA', 'Needs "helper virus"', 'Plant diseases'],
    ['Prion', 'Misfolded protein (PrPSc) — NO nucleic acid', 'Converts normal PrPC → abnormal PrPSc; accumulates in brain', 'Spongiform encephalopathies: CJD (humans), mad cow (BSE), scrapie (sheep)'],
], [0.9 * inch, 1.7 * inch, 1.7 * inch, 2.5 * inch]))
story.append(sp(4))
story.append(HY("Prions: no DNA or RNA. Transmitted by ingestion, transplant, surgical instruments. "
                "Resistant to standard autoclaving. Cause fatal neurodegenerative 'spongiform' brain damage."))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# MODULE 2 LABS (L3, L4, L5)
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("MODULE 2 LABS — L3, L4, L5 (Week 2)", h1))

story.append(Paragraph("Lab 3: Pick and Patch of Solid Colonies", h2))
story.append(Paragraph(
    f"{B('Objective:')} aseptically transfer bacterial colonies from soil plates to make a library plate. "
    f"Directly supports the {B('Antibiotic Discovery project')} (Tiny Earth).", bod))
story.append(Paragraph(B("Key concepts:"), h3))
story.append(Paragraph(
    f"• {B('Pick and patch:')} touch colony with sterile toothpick (picks up thousands of bacteria) → "
    f"patch (zigzag) onto fresh TSA or PDA plate grid square.", bul))
story.append(Paragraph(
    f"• Select promising colonies: {B('haloes')} (may indicate antibiotic production) and "
    f"{B('pigmented colonies')}. Aim for 10–12+ unique colonies.", bul))
story.append(Paragraph(
    f"• {B('Library plate')} = bacterial catalog of all unique isolates for antibiotic testing.", bul))
story.append(Paragraph(
    f"• {B('Timing + sterile technique')} are critical — colonies overgrow, migrate, contaminate.", bul))
story.append(Paragraph(
    f"• Label each patch with a number/letter. Take pictures of the original soil plate "
    f"to trace colony origins.", bul))
story.append(Paragraph(
    f"• Report must include: colony list, diagram/photo of soil plate, description of library plate.", bul))

story.append(Paragraph("Lab 4: Aseptic Technique", h2))
story.append(Paragraph(
    f"{B('Objective:')} transfer bacteria without introducing contaminants. "
    f"All culture media sterilized by {B('autoclave')} before use.", bod))
story.append(Paragraph(B("Culture media types:"), h3))
story.append(tbl([
    ['Medium', 'Form', 'Use'],
    ['Broth', 'Liquid', 'Large numbers of bacteria in small space; easy transport'],
    ['Agar slant', 'Solid (angled tube)', 'Solid growth surface; easier storage/transport than Petri plates'],
    ['Agar deep', 'Solid (bottom of tube)', 'Anaerobic growth; 0.5–0.7% agar (semisolid) = motility test (inverted pine tree pattern)'],
], [0.9 * inch, 0.9 * inch, 5.0 * inch]))
story.append(sp(4))
story.append(Paragraph(B("Inoculation tools and rules:"), h3))
story.append(Paragraph(f"• {B('Inoculating loop')} = broth and slant transfers (zigzag)", bul))
story.append(Paragraph(f"• {B('Inoculating needle')} = deep transfers (stab)", bul))
story.append(Paragraph(f"• Flame loop {B('red hot')}, cool ≥30 sec before touching culture", bul))
story.append(Paragraph(f"• Hold cap with {B('little finger')} of dominant hand; never set down open tubes", bul))
story.append(Paragraph(f"• Flame mouth of tube before and after inoculation", bul))
story.append(Paragraph(f"• {B('LOOSELY screw caps')} after inoculation — most cultures need O₂ (only anaerobes get tight caps)", bul))
story.append(Paragraph(B("Organisms used: Bacillus subtilis (broth) + Escherichia coli (slant)"), bod))
story.append(Paragraph(B("Growth pattern observation (agar slants):"), h3))
story.append(Paragraph(
    f"Patterns: arborescent, beaded, echinulate, filiform, rhizoid, spreading. "
    f"Broth patterns: turbid, pellicle, sediment, flocculent.", bod))

story.append(Paragraph("Lab 5: Smears and Simple Staining", h2))
story.append(Paragraph(
    f"{B('Objectives:')} prepare smear, heat-fix, perform simple stain, identify bacterial morphology.", bod))
story.append(Paragraph(B("Why stain?"), h3))
story.append(Paragraph(
    f"(1) Lasting preparation for comparison. (2) Increases contrast → better detail and resolution.", bod))
story.append(Paragraph(B("Smear preparation:"), h3))
story.append(Paragraph(f"• Broth culture: 2–3 loopfuls directly on slide; spread thin", bul))
story.append(Paragraph(f"• Solid culture: 1–2 loopfuls of water first, then add small amount of solid culture; avoid scraping agar", bul))
story.append(Paragraph(f"• Let air dry completely", bul))
story.append(Paragraph(
    f"• {B('Heat fixation:')} pass through outer blue flame 2–3 times. "
    f"Kills bacteria, prevents wash-off, preserves morphology, helps stain uptake. "
    f"(Too hot → distorted cells or black, no stain uptake)", bul))
story.append(Paragraph(B("Stain chemistry:"), h3))
story.append(Paragraph(
    f"Stains are dyes derived from benzene. "
    f"{B('Chromogen')} = colored component. "
    f"{B('Chromophore')} = region giving color. "
    f"{B('Auxochrome')} = charged part of the chromogen.", bod))
story.append(Paragraph(
    f"• {B('Basic stains:')} positively charged chromophore → attaches to OUTSIDE of bacterial cell (negatively charged). "
    f"Direct stain → stains bacteria. Examples: crystal violet, methylene blue, safranin, malachite green.", bul))
story.append(Paragraph(
    f"• {B('Acidic stains:')} negatively charged → stains background (negative stain).", bul))
story.append(Paragraph(B("Simple stain procedure:"), h3))
story.append(Paragraph(
    f"Cover smear with dye → 1 minute → wash with water → blot dry → observe under microscope. "
    f"Use 40× first → oil immersion (100×) for final observation. "
    f"Move away from edges/clumps; look for separated cells.", bod))
story.append(Paragraph(B("Morphology recording:"), h3))
story.append(Paragraph(
    f"• {B('Shape:')} coccus (perfectly round) vs bacillus (rod). "
    f"If not round → rod (rods can be very long or very short).", bul))
story.append(Paragraph(f"• {B('Arrangement:')} singles, pairs, chains, clusters, etc. (most common two arrangements)", bul))
story.append(Paragraph(B("Organisms used: Staphylococcus epidermidis (slant) + Bacillus megaterium (broth)"), bod))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# QUICK REFERENCE / CHEAT SHEET
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("MODULE 2 — QUICK REFERENCE / EXAM CHEAT SHEET", h1))

story.append(Paragraph("Must-Know Facts (from Popa Slides)", h2))
must_know = [
    ("Prokaryote ribosomes", "70S (30S + 50S) — antibiotic target"),
    ("Eukaryote ribosomes", "80S (40S + 60S); 70S in mitochondria/chloroplasts"),
    ("Bacterial cell wall", "Peptidoglycan (NAG + NAM)"),
    ("Archaea cell wall", "Pseudomurein or none — lacks NAM + D-amino acids; NOT affected by penicillin"),
    ("Fungi cell wall", "Chitin"),
    ("Gram+ color", "Purple — thick PG retains crystal violet-iodine complex"),
    ("Gram− color", "Pink/Red — alcohol dissolves outer membrane, CV-I escapes; safranin counterstain"),
    ("Gram stain steps (4)", "Crystal violet → Iodine (mordant) → Alcohol (destain) → Safranin (counterstain)"),
    ("Endotoxin", "Lipid A of LPS — Gram-NEGATIVE only → septic shock"),
    ("Endospore producers", "Bacillus, Clostridium (Gram-positive)"),
    ("Endospore = reproduction?", "NO — survival structure only"),
    ("Acid-fast organism", "Mycobacterium (TB, leprosy) — mycolic acid in cell wall"),
    ("Source of most antibiotics", "Streptomyces (Actinobacteria, high GC)"),
    ("Group translocation", "Bacteria ONLY — sugars phosphorylated as they cross membrane"),
    ("Engulfment", "Eukaryotes ONLY — endocytosis/phagocytosis"),
    ("Flagella types", "Atrichous, monotrichous, amphitrichous, peritrichous"),
    ("Axial filaments", "Spirochetes (endoflagella inside cell)"),
    ("Malaria pathogen", "Plasmodium (Apicomplexa, Chromalveolata); Anopheles mosquito vector"),
    ("Sleeping sickness", "Trypanosoma (Excavata); tsetse fly; kinetoplast near flagellum base"),
    ("Lytic cycle steps (5)", "Attachment → Penetration → Biosynthesis → Maturation → Release"),
    ("Lysogenic cycle", "Prophage integrates into host chromosome; dormant until induced"),
    ("Retroviruses", "Carry reverse transcriptase (RNA → DNA); HIV; major antiviral target"),
    ("Viral growth curve", "Inoculation → Eclipse → Burst"),
    ("Viroids", "ssRNA, no protein coat; self-replicating; plants only"),
    ("Prions", "Misfolded proteins (PrPSc), NO nucleic acid; CJD, mad cow, scrapie"),
    ("Agar source", "Seaweed (algae)"),
    ("Dimorphic fungi", "Mold at 25°C / yeast at 37°C (Histoplasma, Coccidioides)"),
    ("Diatom toxin", "Domoic acid (amnesic shellfish poisoning)"),
    ("Dinoflagellate toxin", "Neurotoxins → paralytic shellfish poisoning, ciguatera"),
    ("Deeply branching: Conan the bacterium", "Deinococcus radiodurans — extreme radiation resistance"),
]
story.append(tbl([['Topic', 'Answer']] + must_know, [2.3 * inch, 4.5 * inch]))
story.append(sp(8))

story.append(Paragraph("Common Trap Questions", h2))
story.append(Paragraph(
    f"• {B('Viruses are NOT cells')} — no organelles, no metabolism, no ribosomes (use host's)", bul))
story.append(Paragraph(
    f"• {B('Archaea ≠ Bacteria')} — separate domain; ether-linked lipids, no peptidoglycan, no human pathogens", bul))
story.append(Paragraph(
    f"• {B('Endospore ≠ reproduction')} — survival structure only; not a method of making more cells", bul))
story.append(Paragraph(
    f"• {B('Endotoxin ≠ Exotoxin:')} Endotoxin = LPS/Lipid A (Gram−, structural, heat-stable, causes fever/shock). "
    f"Exotoxin = secreted protein (Gram+ and Gram−, heat-labile, more potent, specific targets)", bul))
story.append(Paragraph(
    f"• {B('Lysogenic ≠ Lytic:')} Lysogenic = integrated/dormant prophage. Lytic = active replication + cell death", bul))
story.append(Paragraph(
    f"• {B('Yeast vs mold:')} yeasts = single-celled + budding. Molds = filamentous hyphae. "
    f"Dimorphic = both (depends on temperature)", bul))
story.append(Paragraph(
    f"• {B('Capsule vs cell wall:')} capsule is OUTSIDE the cell wall; polysaccharide; virulence factor (anti-phagocytic)", bul))
story.append(Paragraph(
    f"• {B('Mitochondria/chloroplast ribosomes = 70S')} (like bacteria) — endosymbiotic origin", bul))
story.append(Paragraph(
    f"• {B('Aseptic technique — loose caps:')} most bacteria need O₂; only tighten caps for strict anaerobes", bul))

story.append(sp(8))
story.append(Paragraph("Sources: Popa BIO203 lecture slides ch3–ch6; Lab reports L3 (Pick & Patch), "
                       "L4 (Aseptic Technique), L5 (Smears & Simple Staining)",
                       ParagraphStyle('FT', fontName='Helvetica-Oblique', fontSize=8,
                                      alignment=TA_CENTER, textColor=colors.grey)))

doc.build(story)
print(f"Done -> {OUTPUT}")
