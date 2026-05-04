# BIO203 Module 2 MC Practice Questions — Ch. 3, 4, 5, 6
# 50 multiple-choice questions built from Popa lecture slides (ch3–ch6) + Labs L3/L4/L5

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\Users\User\Dropbox\Nu micro\chapter 3 to 6\BIO203_Module2_MC_Questions.pdf"

h1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=15, spaceAfter=6,
                    textColor=colors.HexColor('#1a1a6e'))
h2 = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=12, spaceAfter=4,
                    spaceBefore=10, textColor=colors.HexColor('#1a1a6e'))
qst = ParagraphStyle('Q', fontName='Helvetica-Bold', fontSize=10, spaceAfter=4, leading=13)
opt = ParagraphStyle('O', fontName='Helvetica', fontSize=9.5, spaceAfter=2, leading=12,
                     leftIndent=20)
ans = ParagraphStyle('A', fontName='Helvetica-Bold', fontSize=9, spaceAfter=4, leading=12,
                     textColor=colors.HexColor('#0a6b0a'), leftIndent=10)
exp = ParagraphStyle('E', fontName='Helvetica-Oblique', fontSize=8.5, spaceAfter=10,
                     leading=11, leftIndent=10, textColor=colors.HexColor('#555555'))


def Q(num, question, options, answer, explanation):
    story.append(Paragraph(f"<b>{num}.</b> {question}", qst))
    for letter_, text in options:
        story.append(Paragraph(f"({letter_}) {text}", opt))
    story.append(Paragraph(f"Answer: {answer}", ans))
    story.append(Paragraph(f"Why: {explanation}", exp))


doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                        leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                        topMargin=0.6 * inch, bottomMargin=0.6 * inch)
W = 7.3 * inch
story = []

story += [
    Paragraph("BIO203 Microbiology — Module 2 MC Practice Questions",
              ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=18,
                             alignment=TA_CENTER, textColor=colors.HexColor('#1a1a6e'))),
    Spacer(1, 4),
    Paragraph("50 questions from Popa slides (Ch.3–6) + Labs L3/L4/L5",
              ParagraphStyle('TS', fontName='Helvetica', fontSize=10, alignment=TA_CENTER,
                             textColor=colors.grey)),
    HRFlowable(width=W, thickness=2, color=colors.HexColor('#1a1a6e')),
    Spacer(1, 8),
]

# ═══ CHAPTER 3 — THE CELL (Q1–14) ═══════════════════════════════════════════
story.append(Paragraph("CHAPTER 3: THE CELL (Q1–14)", h2))

Q(1,
  "Pasteur's swan-neck flask experiment demonstrated which of the following?",
  [('a','Cells arise by spontaneous generation from nutrient-rich broth'),
   ('b','Life only comes from pre-existing life (Omne vivum ex vivo)'),
   ('c','Boiling cannot kill all microorganisms'),
   ('d','Airborne microbes can only be blocked by a solid plug'),
   ('e','The germ theory of disease')],
  "b",
  "Pasteur boiled broth and left it in swan-neck flasks. It remained sterile until the neck was broken, "
  "disproving spontaneous generation and showing that life comes only from life.")

Q(2,
  "According to the slide, which cell biologist stated 'omnis cellula a cellula' (all cells arise from cells)?",
  [('a','Schleiden'),('b','Schwann'),('c','Robert Brown'),('d','Rudolf Virchow'),('e','Robert Remak')],
  "d",
  "Virchow coined 'omnis cellula a cellula' as a basic tenet of cell theory. "
  "Robert Remak earlier described that cells arise from other cells via cell division, but the Latin phrase belongs to Virchow.")

Q(3,
  "What is the primary evidence cited in the lecture slides that supports the endosymbiotic theory?",
  [('a','Mitochondria have ribosomes identical to eukaryotic cytoplasmic ribosomes'),
   ('b','Mitochondria and chloroplasts have their own DNA and divide independently'),
   ('c','Chloroplasts are found in all eukaryotic cells'),
   ('d','Both organelles lack an outer membrane'),
   ('e','They are derived from the Golgi apparatus')],
  "b",
  "Slides state: mitochondria and chloroplasts have their own DNA and divide independently — "
  "originally independent bacteria that became symbionts with eukaryotic cells.")

Q(4,
  "Which of the following is a key difference between prokaryotes and eukaryotes per the Ch.3 comparison slide?",
  [('a','Prokaryotes have membrane-bound organelles'),
   ('b','Eukaryotes divide by binary fission'),
   ('c','Prokaryotes have no histones; their DNA is organized by NAPs'),
   ('d','Eukaryotes have 70S ribosomes'),
   ('e','Prokaryotes have linear chromosomes')],
  "c",
  "Slide: prokaryotes have no histones; DNA is organized by NAPs (nucleoid-associated proteins). "
  "Eukaryotes have histones forming nucleosomes → chromosomes.")

Q(5,
  "A prokaryotic ribosome has a sedimentation value of:",
  [('a','80S'),('b','40S'),('c','60S'),('d','70S'),('e','50S only')],
  "d",
  "Prokaryotic ribosomes are 70S (30S small + 50S large subunits). "
  "Eukaryotic cytoplasmic ribosomes are 80S. The difference makes prokaryotic ribosomes targets for many antibiotics.")

Q(6,
  "Which statement about plasmids is correct per the Ch.3 slide?",
  [('a','Plasmids are part of the main circular chromosome'),
   ('b','Plasmids are membrane-bound organelles'),
   ('c','Plasmids are small extrachromosomal circular dsDNA that replicate independently and can be transferred between cells'),
   ('d','Plasmids contain only structural genes, never antibiotic resistance genes'),
   ('e','Plasmids are unique to Archaea')],
  "c",
  "Slide: plasmids are small, extrachromosomal, circular pieces of dsDNA; usually 5–100 genes; "
  "replicate independently; can be transferred cell-to-cell.")

Q(7,
  "Endospores are formed by bacteria primarily in response to:",
  [('a','Exposure to antibiotics'),
   ('b','Phagocytosis by immune cells'),
   ('c','Nutrient scarcity — when key nutrients like carbon or nitrogen become unavailable'),
   ('d','Temperature exceeding 100°C'),
   ('e','Viral infection')],
  "c",
  "Slide: sporulation generally occurs when a key nutrient such as carbon or nitrogen becomes scarce or unavailable. "
  "It is a survival system, NOT a reproduction method.")

Q(8,
  "Which membrane transport mechanism is found ONLY in bacteria (not eukaryotes)?",
  [('a','Simple diffusion'),('b','Facilitated diffusion'),('c','Osmosis'),
   ('d','Group translocation'),('e','Active transport')],
  "d",
  "Slide specifically states: group translocation is only in bacteria — mainly for sugars, "
  "which become phosphorylated as they cross the membrane. Engulfment is the eukaryote-only mechanism.")

Q(9,
  "In the Gram stain, alcohol (the destaining step) affects Gram-positive and Gram-negative cells differently. "
  "What happens to Gram-negative cells during the alcohol step?",
  [('a','Alcohol dehydrates the thick peptidoglycan, trapping crystal violet inside'),
   ('b','Alcohol dissolves the outer membrane, leaving holes in the thin peptidoglycan so crystal violet can diffuse out'),
   ('c','Alcohol causes safranin to bind to the outer membrane'),
   ('d','Alcohol causes the CV-iodine complex to crystallize permanently'),
   ('e','Alcohol has no effect on Gram-negative cells')],
  "b",
  "Slide: in Gram-negative cells, alcohol dissolves the outer membrane and leaves small holes in the thin "
  "peptidoglycan layer so CV-I can diffuse out, leaving the cell colorless until safranin (counterstain) turns it pink/red.")

Q(10,
  "Which bacteria produce waxy mycolic acid in their cell walls, making them resistant to standard Gram staining and most antibiotics?",
  [('a','Staphylococcus aureus'),('b','Mycoplasma pneumoniae'),('c','Mycobacterium tuberculosis'),
   ('d','Neisseria meningitidis'),('e','Clostridium botulinum')],
  "c",
  "Slide: acid-fast bacteria (Mycobacterium, Nocardia) have waxy mycolic acid bound to peptidoglycan. "
  "Hard to penetrate, very resistant to antibiotics; slow-growing. Usually yield Gram-variable results.")

Q(11,
  "The glycocalyx includes which two structures?",
  [('a','Flagellum and pilus'),
   ('b','Capsule (organized) and slime layer (unorganized/loose)'),
   ('c','Fimbriae and capsule'),
   ('d','S-layer and flagellum'),
   ('e','Teichoic acid and LPS')],
  "b",
  "Slide: glycocalyx = sugar coat, 2 types: capsule (organized) and slime layer (unorganized and loose). "
  "Both help with adhesion and biofilm formation.")

Q(12,
  "Which flagellar arrangement describes flagella distributed over the ENTIRE cell surface?",
  [('a','Monotrichous'),('b','Amphitrichous'),('c','Atrichous'),('d','Lophotrichous'),('e','Peritrichous')],
  "e",
  "Slide: peritrichous = flagella distributed over entire cell surface. "
  "Monotrichous = single polar. Amphitrichous = tuft at each end. Atrichous = no flagella.")

Q(13,
  "Axial filaments (endoflagella) are characteristic of which bacterial group?",
  [('a','Cyanobacteria'),('b','Spirochetes'),('c','Firmicutes'),('d','Actinobacteria'),('e','Gammaproteobacteria')],
  "b",
  "Slide: axial filaments are also called endoflagella; found in spirochetes (Treponema, Borrelia). "
  "Anchored at one end; rotation causes corkscrew motion through tissue.")

Q(14,
  "According to the Ch.3 slide, which cytoskeletal component is involved in ameboid movement, "
  "cytoplasmic streaming, and muscle contraction in animals?",
  [('a','Microtubules'),('b','Intermediate filaments'),('c','Microfilaments'),('d','Nuclear lamina'),('e','Flagellin')],
  "c",
  "Slide: microfilaments are composed of actin filaments. Their dynamic polymerization/depolymerization "
  "and association with myosin allows them to participate in ameboid movement, cytoplasmic streaming, "
  "contractile ring formation during cell division, and muscle contraction.")

story.append(PageBreak())

# ═══ CHAPTER 4 — PROKARYOTIC DIVERSITY (Q15–28) ══════════════════════════════
story.append(Paragraph("CHAPTER 4: PROKARYOTIC DIVERSITY (Q15–28)", h2))

Q(15,
  "Which phylum contains Gram-negative chemoheterotrophs classified into 5 classes (Alpha through Epsilon)?",
  [('a','Firmicutes'),('b','Actinobacteria'),('c','Spirochetes'),('d','Proteobacteria'),('e','Cyanobacteria')],
  "d",
  "Slide: Proteobacteria are Gram-negatives, chemoheterotrophs, with 5 classes: Alpha, Beta, Gamma, Delta, Epsilon.")

Q(16,
  "Rocky Mountain spotted fever is caused by which organism, and what class of Proteobacteria does it belong to?",
  [('a','Neisseria meningitidis — Betaproteobacteria'),
   ('b','Rickettsia rickettsii — Alphaproteobacteria'),
   ('c','Helicobacter pylori — Epsilonproteobacteria'),
   ('d','Vibrio cholerae — Gammaproteobacteria'),
   ('e','Campylobacter jejuni — Epsilonproteobacteria')],
  "b",
  "Slide: Rickettsia (obligate intracellular parasites) are Alphaproteobacteria. "
  "R. rickettsii causes Rocky Mountain spotted fever. Transmitted by arthropods.")

Q(17,
  "Nitrogen-fixing bacteria that grow in soil using nutrients excreted by plants, "
  "or that fix nitrogen in plant roots, are found in which class of Proteobacteria?",
  [('a','Epsilonproteobacteria'),('b','Gammaproteobacteria'),('c','Deltaproteobacteria'),
   ('d','Alphaproteobacteria'),('e','Betaproteobacteria')],
  "d",
  "Slide: Alphaproteobacteria include Azospirillum (nitrogen-fixing in soil) and Rhizobium (nitrogen-fixing in plant roots). "
  "Also includes Nitrobacter and Nitrosomonas (nitrification).")

Q(18,
  "Which Gammaproteobacteria pathogen is described in the slides as 'very antibiotic resistant' "
  "and causes infections in cystic fibrosis and burn patients?",
  [('a','Vibrio cholerae'),('b','Haemophilus influenzae'),('c','Pseudomonas aeruginosa'),
   ('d','E. coli O157'),('e','Francisella tularensis')],
  "c",
  "Slide: P. aeruginosa (order Pseudomonadales) is metabolically diverse; grows on unusual nutrients even in disinfectants. "
  "Opportunistic pathogen — very antibiotic resistant. Infects cystic fibrosis and burn patients.")

Q(19,
  "What unique feature distinguishes Deltaproteobacteria like Bdellovibrio from other bacteria?",
  [('a','They fix nitrogen in legume roots'),
   ('b','They use sulfur instead of oxygen in cellular respiration and some prey on other bacteria'),
   ('c','They are obligate intracellular parasites transmitted by ticks'),
   ('d','They produce acid-fast cell walls'),
   ('e','They have no cell wall')],
  "b",
  "Slide: Desulfovibrionales use sulfur instead of O₂ as final electron acceptor. Bdellovibrio preys on other bacteria. "
  "Myxococcales form myxospores by aggregation (gliding motility).")

Q(20,
  "Helicobacter pylori is associated with which diseases and belongs to which Proteobacteria class?",
  [('a','Cholera and dysentery — Gammaproteobacteria'),
   ('b','Peptic ulcers and stomach cancer — Epsilonproteobacteria'),
   ('c','Whooping cough — Betaproteobacteria'),
   ('d','Lyme disease — Alphaproteobacteria'),
   ('e','Tetanus — Firmicutes')],
  "b",
  "Slide: Helicobacter is Epsilonproteobacteria; multiple flagella; causes peptic ulcers (H. pylori) and stomach cancer. "
  "Campylobacter jejuni (same class) causes gastroenteritis.")

Q(21,
  "Which bacterial phylum includes Borrelia burgdorferi (Lyme disease), Treponema pallidum (syphilis), "
  "and uses axial filaments for motility?",
  [('a','Cyanobacteria'),('b','Actinobacteria'),('c','Spirochetes'),('d','Firmicutes'),('e','Bacteroidetes')],
  "c",
  "Slide: Spirochetes have axial filaments (inside flagella) — Borrelia = Lyme disease, "
  "Leptospira = leptospirosis, Treponema pallidum = syphilis.")

Q(22,
  "Gram-positive bacteria are classified into two groups based on GC content. "
  "Which group includes Streptomyces (major antibiotic source) and Mycobacterium?",
  [('a','Firmicutes (Low GC)'),('b','Actinobacteria (High GC)'),('c','Proteobacteria'),
   ('d','Bacteroidetes'),('e','Cyanobacteria')],
  "b",
  "Slide: High GC Actinobacteria include Streptomyces (antibiotics), Mycobacterium (TB, leprosy), "
  "Corynebacterium (diphtheria), Propionibacterium acnes (acne), Bifidobacteria (gut probiotics).")

Q(23,
  "Clostridium species (tetanus, botulism, gas gangrene, C. diff) share which two characteristics?",
  [('a','Gram-negative and aerobic'),
   ('b','Endospore-forming and obligate anaerobes'),
   ('c','Non-endospore forming and microaerophilic'),
   ('d','Gram-positive high GC and acid-fast'),
   ('e','Cell wall-less and motile by axial filaments')],
  "b",
  "Slide: Clostridium are Firmicutes (low GC), endospore-producing obligate anaerobes. "
  "Species cause tetanus, botulism, gas gangrene, and C. difficile colitis.")

Q(24,
  "Listeria monocytogenes is notable for which two survival abilities mentioned in the slides?",
  [('a','Forms endospores and tolerates extreme heat'),
   ('b','Grows at refrigeration temperature and survives inside phagocytes'),
   ('c','Grows only in strictly anaerobic conditions and produces mycolic acid'),
   ('d','Produces Bt toxin and causes skin anthrax'),
   ('e','Causes walking pneumonia and has no cell wall')],
  "b",
  "Slide: Listeria (Firmicutes, Lactobacillales) can grow at refrigeration temperatures and "
  "survives inside phagocytes — making it a dangerous food-borne pathogen.")

Q(25,
  "Which bacteria is known as 'Conan the bacterium' due to extreme radiation resistance?",
  [('a','Thermus aquaticus'),('b','Thermotoga'),('c','Deinococcus radiodurans'),
   ('d','Sulfolobus'),('e','Methanobacterium')],
  "c",
  "Slide: Deinococcus radiodurans = 'Conan the bacterium' — very resistant. "
  "Classified as a deeply branching bacterium, ancient, close to LUCA.")

Q(26,
  "Which of the following correctly describes Archaea per the Ch.4 slide?",
  [('a','They are Gram-negative with LPS in their outer membrane'),
   ('b','They have peptidoglycan cell walls like bacteria'),
   ('c','No known human pathogens; many are extremophiles; cell wall is pseudomurein or none'),
   ('d','They infect only bacteria as bacteriophages'),
   ('e','They are obligate intracellular parasites')],
  "c",
  "Slide: Archaea have no known human pathogens; many are extremophiles. "
  "Cell wall is pseudomurein (lacks NAM and D-amino acids) or wall-less.")

Q(27,
  "Methanogens are found in which environments and what do they produce?",
  [('a','Hot springs — produce sulfur compounds'),
   ('b','Strictly anaerobic environments (gut, swamps, sewage) — produce methane'),
   ('c','High-salt environments — produce halorhodopsin'),
   ('d','Plant roots — fix nitrogen'),
   ('e','Hospital environments — produce biofilms')],
  "b",
  "Slide: methanogens are strictly anaerobic; produce methane; industrial use; also present in the gut. "
  "Example: Methanobacterium. They are Archaea.")

Q(28,
  "Which of the following is used to classify prokaryotes according to the Ch.4 slide?",
  [('a','Cell shape only'),
   ('b','Only Gram staining'),
   ('c','Bergey\'s Manual (morphology/physiology/biochemistry), Gram staining, GC content, and sequence similarities'),
   ('d','Endospore formation only'),
   ('e','Colony color on agar plates')],
  "c",
  "Slide: classification uses Bergey's Manual (morphology, physiological and biochemical characteristics), "
  "Gram staining, GC content, and sequence similarities.")

story.append(PageBreak())

# ═══ CHAPTER 5 — EUKARYOTES (Q29–38) ════════════════════════════════════════
story.append(Paragraph("CHAPTER 5: THE EUKARYOTES OF MICROBIOLOGY (Q29–38)", h2))

Q(29,
  "According to the Ch.5 slide, which three eukaryotic supergroups contain most of the protozoa?",
  [('a','Opisthokonta, Archaeplastida, Rhizaria'),
   ('b','Amoebozoa, Excavata, and Chromalveolata'),
   ('c','Chromalveolata, Opisthokonta, and Amoebozoa'),
   ('d','Excavata, Rhizaria, and Archaeplastida'),
   ('e','Fungi, Protozoa, and Helminths are not classified under supergroups')],
  "b",
  "Slide: 6 supergroups of eukaryotes exist; Amoebozoa, Excavata, and Chromalveolata contain most of the protozoa.")

Q(30,
  "Apicomplexa (Plasmodium, Toxoplasma, Cryptosporidium) are characterized by which features?",
  [('a','They use pseudopods and form slime molds'),
   ('b','They are ciliated and have a cytostome'),
   ('c','They are non-motile obligate intracellular parasites with apical complexes and complex life cycles'),
   ('d','They are free-living flagellates with a kinetoplast'),
   ('e','They produce neurotoxins during red tide events')],
  "c",
  "Slide: Apicomplexa (Chromalveolata) are not motile, obligate intracellular parasites with apical complexes "
  "used for host invasion. They have complex life cycles.")

Q(31,
  "In Lab 1 (Module 1), you observed Trypanosoma trypomastigotes in a blood smear. "
  "Trypanosoma is classified under which protozoan supergroup?",
  [('a','Amoebozoa'),('b','Chromalveolata (Apicomplexa)'),('c','Excavata'),
   ('d','Opisthokonta'),('e','Archaeplastida')],
  "c",
  "Slide: Trypanosoma is in Excavata (flagellates). The kinetoplast near the flagellum base "
  "is a diagnostic feature seen in the Lab 1 blood smear.")

Q(32,
  "Which helminth group (per Ch.5 slides) has NO digestive system and absorbs nutrients directly, "
  "with a head (scolex) bearing suckers and hooks?",
  [('a','Nematoda (roundworms)'),('b','Trematoda (flukes)'),('c','Cestoda (tapeworms)'),
   ('d','Apicomplexa'),('e','Amoebozoa')],
  "c",
  "Slide: Cestodes (tapeworms) have segmented, ribbon-shaped bodies; the scolex has suckers and hooks for attachment; "
  "NO digestive system — absorbs nutrients directly. Example: Taenia.")

Q(33,
  "Which roundworm species specifically infects the small intestines of humans per the Ch.5 slide?",
  [('a','Trichinella spiralis'),('b','Enterobius vermicularis (pinworm)'),
   ('c','Trichuris trichiura (whipworm)'),('d','Ascaris lumbricoides'),('e','Heartworm')],
  "d",
  "Slide: Ascaris lumbricoides infects the small intestines of humans. Egg is infective (like Trichuris). "
  "Enterobius (pinworm), Trichuris (whipworm), and hookworms are also listed.")

Q(34,
  "What is the key difference between yeasts and molds as described in the Ch.5 slide?",
  [('a','Yeasts have chitin walls; molds have cellulose walls'),
   ('b','Yeasts are unicellular and often reproduce by budding; molds form filamentous hyphae creating a thallus'),
   ('c','Yeasts can only do aerobic respiration; molds are strictly anaerobic'),
   ('d','Molds are dimorphic; yeasts are always unicellular'),
   ('e','Yeasts are Ascomycota only; molds are Basidiomycota only')],
  "b",
  "Slide: Yeasts are unicellular, divide by budding or fission, can do aerobic or anaerobic growth. "
  "Molds/fleshy fungi form filamentous hyphae (with or without septa) → thallus. "
  "Dimorphic fungi can be either form depending on temperature.")

Q(35,
  "Dimorphic fungi grow as molds at room temperature and as yeasts at body temperature. "
  "What temperature switch triggers each form per the slides?",
  [('a','Mold at 37°C (body), yeast at 25°C (environment)'),
   ('b','Yeast at 37°C (body/host), mold at 25°C (environment/lower temperature)'),
   ('c','Mold at 4°C, yeast above 100°C'),
   ('d','Both forms can occur at any temperature depending on nutrients'),
   ('e','Mold in acidic pH, yeast in alkaline pH')],
  "b",
  "Slide: dimorphic fungi grow as mold or as yeast depending on temperature — "
  "yeast form at 37°C (inside host), mold at 25°C (environmental/culture). "
  "Examples: Histoplasma, Coccidioides, Blastomyces.")

Q(36,
  "According to the slides, which asexual fungi group includes Candida and Pneumocystis?",
  [('a','Zygomycota'),('b','Ascomycota'),('c','Basidiomycota'),('d','Anamorphs'),('e','Oomycota')],
  "d",
  "Slide: Anamorphs are asexual fungi. Examples: Candida and Pneumocystis. "
  "Ascomycota (sac fungi) includes Trichophyton/Microsporum (athlete's foot, ringworm). "
  "Basidiomycota includes Cryptococcus.")

Q(37,
  "Which algal group produces domoic acid (a toxin) per the Ch.5 lecture slides?",
  [('a','Dinoflagellates'),('b','Kelp'),('c','Diatoms'),('d','Cyanobacteria'),('e','Green algae')],
  "c",
  "Slide: diatoms produce domoic acid, a toxin. Dinoflagellates produce neurotoxins causing "
  "paralytic shellfish poisoning and ciguatera. Agar is produced by seaweed.")

Q(38,
  "Lichens are described in the slides as a combination of which two organisms?",
  [('a','Two species of bacteria living in symbiosis'),
   ('b','Green algae (or cyanobacteria) and a fungus in symbiosis'),
   ('c','A protozoan and a fungus'),
   ('d','A virus and a bacterium'),
   ('e','Two species of fungi')],
  "b",
  "Slide: lichens = combination of green algae (or cyanobacteria) and a fungus in symbiosis. "
  "Slow-growing, can live for centuries; environmentally important.")

story.append(PageBreak())

# ═══ CHAPTER 6 — ACELLULAR PATHOGENS (Q39–50) ════════════════════════════════
story.append(Paragraph("CHAPTER 6: ACELLULAR PATHOGENS (Q39–50)", h2))

Q(39,
  "According to the Ch.6 slide, what determines the host range of a virus?",
  [('a','The size of the virus (nm diameter)'),
   ('b','Specific host attachment sites and cellular factors'),
   ('c','Whether the virus has a lipid envelope'),
   ('d','Whether the virus contains DNA or RNA'),
   ('e','The GC content of the viral genome')],
  "b",
  "Slide: host range is determined by specific host attachment sites and cellular factors. "
  "Most viruses infect only specific types of cells.")

Q(40,
  "What are the 5 steps of the lytic cycle in the correct order per the Ch.6 slide?",
  [('a','Attachment → Biosynthesis → Penetration → Release → Maturation'),
   ('b','Penetration → Attachment → Biosynthesis → Maturation → Release'),
   ('c','Attachment → Penetration → Biosynthesis → Maturation → Release'),
   ('d','Attachment → Penetration → Maturation → Biosynthesis → Release'),
   ('e','Biosynthesis → Attachment → Penetration → Maturation → Release')],
  "c",
  "Slide: virulent phages use lytic cycle: Attachment → Penetration → Biosynthesis → Maturation → Release. "
  "Host cell dies (lysis).")

Q(41,
  "In the lysogenic cycle, what happens to the viral DNA?",
  [('a','It replicates independently in the cytoplasm'),
   ('b','It is immediately destroyed by host restriction enzymes'),
   ('c','It integrates into the host chromosome as a prophage and replicates passively with the host'),
   ('d','It is translated directly into viral proteins without replication'),
   ('e','It exits the cell by budding each time the host replicates')],
  "c",
  "Slide: temperate phages can become part of the host genome (lysogenic cycle) = dormant. "
  "If induced (e.g. UV), they switch to the lytic cycle.")

Q(42,
  "How does penetration differ between bacteriophages and animal viruses per the Ch.6 slides?",
  [('a','Phages use endocytosis; animal viruses inject nucleic acid directly'),
   ('b','Animal virus entry = endocytosis + requires an extra uncoating step; phages inject nucleic acid'),
   ('c','Both use identical endocytosis mechanisms'),
   ('d','Animal viruses insert their genome into the host chromosome; phages do not'),
   ('e','Phages require receptor binding; animal viruses do not')],
  "b",
  "Slide: animal virus life cycle differs from phages — penetration by endocytosis, "
  "extra step of uncoating (release from capsid), and release by budding (acquires envelope).")

Q(43,
  "What enzyme do retroviruses carry, and why is it important clinically?",
  [('a','RNA polymerase — allows them to replicate in the nucleus'),
   ('b','Reverse transcriptase — makes DNA using RNA as template; inserted into host DNA; major anti-HIV drug target'),
   ('c','Lysozyme — destroys host cell wall'),
   ('d','Integrase only — this is the only retrovirus target'),
   ('e','DNA gyrase — unwinds host chromosome for viral integration')],
  "b",
  "Slide: retroviruses carry reverse transcriptase which makes DNA using RNA as template. "
  "The DNA is inserted into host DNA. Reverse transcriptase is an effective antiviral target — "
  "many anti-HIV medications target it.")

Q(44,
  "Varicella zoster virus causes chickenpox and can reactivate as shingles. "
  "What type of viral infection is this, and where does the viral genome reside during dormancy?",
  [('a','Chronic infection; virus stays in the bloodstream permanently'),
   ('b','Latent infection; dsDNA genome incorporates into host DNA'),
   ('c','Acute infection; virus is completely cleared from the body'),
   ('d','Subacute infection; virus remains in peripheral lymph nodes'),
   ('e','Productive infection; continuous low-level virus shedding')],
  "b",
  "Slide: Varicella zoster causes a latent infection. Its dsDNA genome becomes incorporated in host DNA. "
  "After latency, reactivates as shingles — painful localized rash on one side of the body.")

Q(45,
  "The three phases of the viral growth curve are (in order):",
  [('a','Eclipse → Inoculation → Burst'),
   ('b','Burst → Eclipse → Inoculation'),
   ('c','Inoculation → Burst → Eclipse'),
   ('d','Inoculation → Eclipse → Burst'),
   ('e','Attachment → Eclipse → Release')],
  "d",
  "Slide: viral growth curve phases: Inoculation (attachment to host cells) → Eclipse (inside the cells) → Burst (virions released). "
  "During eclipse, no free virions are detectable outside cells.")

Q(46,
  "How are bacteriophage particles estimated in the laboratory per the Ch.6 slide?",
  [('a','By measuring optical density of the culture'),
   ('b','By counting plaques (clear zones) on bacterial lawns'),
   ('c','By PCR amplification of viral DNA'),
   ('d','By centrifugation and weighing the viral pellet'),
   ('e','By hemagglutination of red blood cells')],
  "b",
  "Slide: bacteriophages are added to bacterial lawns; viral particles can be estimated by counting plaques "
  "(clear zones where phage killed bacteria). Animal viruses require cell cultures or embryo (egg) systems.")

Q(47,
  "Which of the following correctly describes viroids?",
  [('a','Small infectious RNA molecules with a protein coat; infect animals'),
   ('b','Misfolded proteins with no nucleic acid; cause spongiform encephalopathies'),
   ('c','Small circular ssRNA with NO protein coat; self-replicating; infect plants only'),
   ('d','Double-stranded RNA viruses requiring a helper virus'),
   ('e','DNA fragments from degraded bacteriophages that cause disease')],
  "c",
  "Slide: viroids are small circular ssRNA molecules that can self-replicate (no protein coat). "
  "Mainly plant infections. Virusoids are non-self-replicating ssRNAs that need a helper virus.")

Q(48,
  "Prions cause disease by which mechanism per the Ch.6 slide?",
  [('a','Integrating viral DNA into host neurons'),
   ('b','PrPSc (misfolded protein) accumulates in brain cells forming plaques by converting normal PrPC'),
   ('c','Producing exotoxins that destroy myelin sheaths'),
   ('d','Inserting RNA into host ribosomes and hijacking protein synthesis'),
   ('e','Activating an inflammatory response that destroys brain tissue directly')],
  "b",
  "Slide: PrPC = normal cellular prion protein on cell surface. PrPSc = misfolded form; "
  "accumulates in brain cells forming plaques. Inherited and transmissible by ingestion, transplant, surgical instruments.")

Q(49,
  "Transduction (Ch.6 slide) refers to which process?",
  [('a','Transfer of DNA between bacteria via direct cell contact and sex pilus'),
   ('b','Uptake of naked DNA from the environment by a competent bacterium'),
   ('c','Genetic exchange in bacteria using viruses as messengers (can be generalized or specialized)'),
   ('d','Viral integration of DNA into the host chromosome'),
   ('e','Transfer of plasmids between bacteria by electroporation')],
  "c",
  "Slide: transduction = genetic exchange in bacteria using viruses as messengers. "
  "Can be generalized (any bacterial DNA) or specialized (specific genes near phage integration site).")

Q(50,
  "In Lab 5 (Simple Staining), basic stains attach to bacteria because:",
  [('a','The bacterial cell wall is positively charged, attracting the negatively charged stain'),
   ('b','Basic stains have a positively charged chromophore that attaches to the negatively charged outside of the bacterial cell'),
   ('c','Basic stains have a negatively charged chromophore that stains the background'),
   ('d','The stain is covalently bonded to peptidoglycan'),
   ('e','Basic stains are activated by heat fixation to bind bacterial DNA')],
  "b",
  "Lab 5 background: basic stains have a positively charged chromophore (auxochrome). "
  "The outside of the bacterial cell is negatively charged → electrostatic attraction. "
  "This is a direct stain (stains bacteria). Acidic stains (negative stains) stain the background.")

story.append(Spacer(1, 12))
story.append(Paragraph("Sources: Popa BIO203 lecture slides ch3–ch6; Lab reports L3 (Pick & Patch), "
                       "L4 (Aseptic Technique), L5 (Smears & Simple Staining)",
                       ParagraphStyle('FT', fontName='Helvetica-Oblique', fontSize=8,
                                      alignment=TA_CENTER, textColor=colors.grey)))

doc.build(story)
print(f"Done -> {OUTPUT}")
