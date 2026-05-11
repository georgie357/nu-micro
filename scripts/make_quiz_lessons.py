# BIO203 — Quiz Lessons & Review Log PDF
# Updated after every graded quiz. Read BEFORE every quiz/exam.

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

os.makedirs(r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2', exist_ok=True)
OUTPUT = r'C:/Users/User/Dropbox/Nu micro/chapter 1 and 2/BIO203_Quiz_Lessons.pdf'

doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
    leftMargin=0.6*inch, rightMargin=0.6*inch,
    topMargin=0.6*inch, bottomMargin=0.6*inch)

h1   = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=14, leading=17, spaceAfter=4,
                      alignment=TA_CENTER, borderPad=4, borderWidth=1, borderColor=colors.black,
                      backColor=colors.Color(0.92, 0.92, 0.92))
h2   = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11, leading=14, spaceAfter=3, spaceBefore=8)
h3   = ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceAfter=3, spaceBefore=5)
body = ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=12, spaceAfter=3)
hook = ParagraphStyle('hook', fontName='Helvetica-Bold', fontSize=9, leading=13, spaceAfter=4,
                      backColor=colors.HexColor('#d4edda'), borderPad=6,
                      borderWidth=1, borderColor=colors.HexColor('#28a745'))
wrong = ParagraphStyle('wrong', fontName='Helvetica-Bold', fontSize=9, leading=13, spaceAfter=4,
                       backColor=colors.HexColor('#f8d7da'), borderPad=6,
                       borderWidth=1, borderColor=colors.HexColor('#dc3545'))
partial = ParagraphStyle('partial', fontName='Helvetica-Bold', fontSize=9, leading=13, spaceAfter=4,
                         backColor=colors.HexColor('#fff3cd'), borderPad=6,
                         borderWidth=1, borderColor=colors.HexColor('#cc8800'))
perfect = ParagraphStyle('perfect', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceAfter=4,
                         backColor=colors.HexColor('#cce5ff'), borderPad=6,
                         borderWidth=1, borderColor=colors.HexColor('#004085'),
                         alignment=TA_CENTER)
prep = ParagraphStyle('prep', fontName='Helvetica-Bold', fontSize=9, leading=13, spaceAfter=4,
                      backColor=colors.HexColor('#fce4ec'), borderPad=6,
                      borderWidth=1, borderColor=colors.HexColor('#c2185b'))

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

# ═══════════════════════════════════════════════════════════════════════════════
# TITLE + HOOK
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph('BIO203 — Quiz Lessons &amp; Review Log', h1))
story.append(sp(1))
story.append(Paragraph(
    '🔔 HOOK — READ THIS BEFORE EVERY QUIZ OR EXAM. '
    'Open this file. Go through every WRONG and PARTIAL entry. '
    'For each: do I know the correct answer NOW and WHY? '
    'If no → re-read the relevant study sheet before starting.',
    hook))

# ═══════════════════════════════════════════════════════════════════════════════
# SCORE PROGRESSION SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph('Score Progression — All Quizzes To Date', h2))
story.append(hr())
story.append(tbl([
    ['Quiz', 'Best Score', 'Date', 'Notes'],
    ['Chemistry Pre-Quiz', '15/15 (100%) ⭐', 'May 3', 'Attempt 3 — perfect after 92% / 90.67%'],
    ['Quiz M1 (Intro + Biomolecules)', '15/15 (100%) ⭐', 'May 3', 'Attempt 2 — perfect after 92.03%'],
    ['Post Lab Quiz 1 (Safety + Microscopy)', '10/10 (100%) ⭐', 'May 3', 'Attempt 2 — perfect after 9/10'],
    ['Post Lab Quiz 2 (Aseptic + Stainings)', '10/10 (100%) ⭐', 'May 10', 'First attempt, no retake needed'],
], [2.5*inch, 1.2*inch, 0.7*inch, 2.9*inch]))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════════════════
# MASTER LESSONS — apply to every future quiz
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph('🎯 MASTER LESSONS — apply to every future quiz', h2))
story.append(hr())

story.append(Paragraph('Strategy & Mechanics', h3))
story.append(tbl([
    ['#', 'Rule', 'Source'],
    ['1', 'BEFORE starting quiz: read this lessons file end-to-end + study sheet relevant to topic', 'all'],
    ['2', 'For drag-and-drop fill-in: ALWAYS drag word-bank items, never type. Capitalization must match.', 'Chem Q3, M1 Q3'],
    ['3', 'D2L allows reusing the same word-bank item in multiple slots (e.g. "amino acids" twice)', 'M1 A2 Q14, Q15'],
    ['4', 'For fill-in-the-blank: scan FULL word bank first — check if each blank needs a number OR a direction word', 'Chem Q3'],
    ['5', 'For calculation answers: check the UNITS of the answer choices first. Convert your answer to match (55 µm, not 0.055 mm)', 'Lab 1 Q4'],
    ['6', 'When 2+ answers seem correct: pick the simpler / more obvious wrong one', 'M1 Q5'],
    ['7', 'For bond diagrams: identify WITHIN vs BETWEEN molecules first. Solid line = covalent, dashed = hydrogen', 'Chem Q10'],
    ['8', 'For numbered-molecule diagrams: identify structure TYPE first (carb/lipid/protein) before assigning #', 'M1 Q15'],
    ['9', 'Cation +1 ≠ Inert atom. Cation +1 = 1 outer-shell electron. Inert = 8 outer-shell electrons (octet).', 'Chem Pre A3 Q1'],
], [0.25*inch, 5.5*inch, 1.5*inch]))
story.append(sp(1))

story.append(Paragraph('Chemistry & Biochemistry Facts', h3))
story.append(tbl([
    ['#', 'Rule', 'Source'],
    ['10', 'pH ↑ = H+ ↓ (1/1000× per 3 units); OH- ↑ (1000× per 3 units). 100× per 2 units. 10× per 1 unit.', 'Chem Q3'],
    ['11', 'Isotopes = same protons (same element), different neutrons (different mass)', 'Chem Q15'],
    ['12', 'Enzymes lower activation energy ONLY — overall ΔG is unchanged', 'Chem Q13'],
    ['13', 'Molecular weight: count every atom; C=12, H=1, O=16, N=14, P=31, S=32', 'Chem Q14'],
    ['14', '1 mm = 1000 µm = 10⁶ nm. 100 µm = 0.1 mm. 100 nm = 0.1 µm.', 'M1 Q5, Q6'],
    ['15', 'Tertiary protein structure = H-bonds + ionic + hydrophobic + disulfide (NOT covalent only)', 'M1 Q11'],
    ['16', 'Triglycerides contain NO phosphate. ATP, phospholipids, nucleic acids do.', 'M1 A2 Q9'],
    ['17', 'Phospholipids and triglycerides both contain glycerol; proteins, DNA, carbohydrates do not.', 'M1 A2 Q13'],
], [0.25*inch, 5.5*inch, 1.5*inch]))
story.append(sp(1))

story.append(Paragraph('Microbiology Facts', h3))
story.append(tbl([
    ['#', 'Rule', 'Source'],
    ['18', 'Koch: anthrax 1876 (first), tuberculosis 1882 (second). Pasteur ≠ Koch (different scientist).', 'M1 Q1'],
    ['19', 'Microscopy pioneers: van Leeuwenhoek (first to see microbes) → Jenner (vaccines) → Pasteur (germ theory) → Koch (postulates) → Fleming (penicillin)', 'M1 A2 Q3'],
    ['20', 'Electron microscope = NO direct lens viewing (image on screen). Light microscopes use ocular.', 'M1 A2 Q5'],
    ['21', 'Gram stain mordant = iodine. Function: prevents crystal violet from leaving cells.', 'M1 A2 Q4'],
    ['22', 'Gram+ = purple (CV-I retained by thick PG after destain). Gram- = pink (CV-I leaks out during destain, safranin counterstains).', 'M1 Q7'],
    ['23', 'Endospore stain (Schaeffer-Fulton): malachite green + heat → green endospores; safranin → pink vegetative cells. Bacillus, Clostridium produce endospores.', 'M1 A2 Q7'],
    ['24', 'Crystal violet DOES penetrate Gram-neg cells initially — it leaks out during alcohol destain. NOT because CV "cannot enter."', 'PLQ2 Q5'],
    ['25', 'In Gram-NEG: peptidoglycan is in periplasm BENEATH outer membrane (NOT exposed). In Gram-POS: PG is the outer layer (IS exposed).', 'PLQ2 Q6'],
], [0.25*inch, 5.5*inch, 1.5*inch]))
story.append(sp(1))

story.append(Paragraph('Lab Technique Facts', h3))
story.append(tbl([
    ['#', 'Rule', 'Source'],
    ['26', 'Smear order: Smear → AIR DRY → Heat-fix → Stain. NEVER fix wet smear.', 'PLQ2 Q8'],
    ['27', 'Heat fixation OR methanol fixation are ALTERNATIVES — never done in sequence.', 'PLQ2 Q4'],
    ['28', 'Fixation primary purpose: AFFIX cells to slide (prevents wash-off). Also kills, preserves shape, lets stain bind.', 'PLQ2 Q9'],
    ['29', 'Simple stain dyes (any basic): crystal violet, methylene blue, safranin, malachite green. All work.', 'PLQ2 Q10'],
    ['30', 'Inoculating loop must be flamed at START (begin clean) AND END (kill bacteria before setting down on bench)', 'PLQ2 Q7'],
    ['31', 'Loop for broth & slant; needle for deep (stab)', 'Lab 4'],
    ['32', 'Tube caps: LOOSE after inoculation for aerobic growth; tight only for anaerobes', 'Lab 4'],
    ['33', 'Coccobacilli = very short rods that look almost like cocci. Individual (not chains).', 'PLQ2 Q2'],
    ['34', 'Library plate: pick PIGMENTED, well-ISOLATED, HALO-producing colonies. REJECT spreading/lace-like (contaminates neighbors).', 'PLQ2 Q1'],
], [0.25*inch, 5.5*inch, 1.5*inch]))
story.append(sp(1))

story.append(Paragraph('Disposal & Safety Facts', h3))
story.append(tbl([
    ['#', 'Rule', 'Source'],
    ['35', 'Live cultures (Petri dishes, broth tubes) → biohazard red bin / decontamination', 'PLQ1 Q8'],
    ['36', 'Microscope slides → sharps (glass)', 'PLQ1 Q8'],
    ['37', 'Paper towels with disinfectant → regular waste (already disinfected)', 'PLQ1 Q8'],
    ['38', 'Broth cultures in glass tubes → decontamination (bleach soak), NOT sharps', 'PLQ1 Q8'],
    ['39', 'Lens cleaning: ONLY lens paper. Never Kleenex, tissue, or paper towel (they scratch).', 'PLQ1 Q6'],
    ['40', 'Coarse focus knob: ONLY for 4× and 10× objectives. Fine focus only for 40× and 100×.', 'PLQ1 Q9'],
], [0.25*inch, 5.5*inch, 1.5*inch]))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# PRE-QUIZ CHECKLIST
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph('📋 Pre-Quiz / Pre-Exam Checklist', h2))
story.append(hr())
story.append(tbl([
    ['Step', 'Action'],
    ['1', 'Read every WRONG and PARTIAL entry in this file'],
    ['2', 'Read the relevant chapter study sheet (Ch.X) AND the Module study guide'],
    ['3', 'For each lesson: can you explain WHY the correct answer is correct — without looking?'],
    ['4', 'Any lesson that feels shaky: re-read the relevant study sheet section'],
    ['5', 'For bond / diagram questions: look for solid vs dashed lines, identify structure type FIRST'],
    ['6', 'For fill-in-the-blank: scan the ENTIRE word bank, plan all blanks before filling any'],
    ['7', 'For calculation answers: check answer-choice UNITS first, convert your result to match'],
    ['8', 'Pre-load mental cheat sheet of key facts for this quiz topic'],
    ['9', 'Time check: how many questions, how many minutes per question?'],
    ['10', 'Submit only after reviewing every answer'],
], [0.4*inch, 6.8*inch]))
story.append(sp(2))

# ═══════════════════════════════════════════════════════════════════════════════
# UPCOMING — Module 2 prep (Ch.3, 4, 5, 6)
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph('🔮 Next Quiz Prep — Quiz M2 (Module 2: Ch.3, 4, 5, 6)', h2))
story.append(hr())
story.append(Paragraph(
    'Likely upcoming: Quiz M2 covers Cell Structure (Ch.3), Prokaryotic Diversity (Ch.4), '
    'Eukaryotes (Ch.5), Acellular Pathogens (Ch.6). Also possible: Post Lab Quiz 3 covering Labs 3-5. '
    'Pre-load these high-yield facts:', prep))

story.append(Paragraph('Ch.3 — The Cell', h3))
story.append(tbl([
    ['Topic', 'Key fact'],
    ['Prokaryote vs Eukaryote', 'Prok = no nucleus, no organelles, 70S ribosomes, circular DNA, peptidoglycan wall. Euk = nucleus, organelles, 80S ribosomes, linear DNA.'],
    ['Endosymbiotic theory', 'Mitochondria + chloroplasts have own DNA, divide independently → originated as free-living bacteria'],
    ['Endospores', 'Bacillus + Clostridium (Gram+). Survival, NOT reproduction. Form under nutrient stress.'],
    ['Gram stain order', 'Crystal violet → Gram\'s iodine (mordant) → alcohol (destain) → safranin (counterstain)'],
    ['Acid-fast', 'Mycobacterium, Nocardia. Mycolic acid in wall. Ziehl-Neelsen stain.'],
    ['Flagella arrangements', 'Atrichous (none), monotrichous (one polar), amphitrichous (tuft each end), peritrichous (all over)'],
    ['Plasmids', 'Small circular extrachromosomal dsDNA. 5–100 genes. Transferable. Carry antibiotic resistance.'],
    ['Group translocation', 'Bacteria ONLY membrane transport. Endocytosis = Eukaryotes ONLY.'],
], [1.7*inch, 5.3*inch]))
story.append(sp(1))

story.append(Paragraph('Ch.4 — Prokaryotic Diversity', h3))
story.append(tbl([
    ['Topic', 'Key fact'],
    ['Proteobacteria 5 classes', 'Alpha (Rickettsia, Rhizobium), Beta (Neisseria, Bordetella), Gamma (E. coli, Vibrio, Pseudomonas), Delta (Bdellovibrio, Myxococcus), Epsilon (Helicobacter, Campylobacter)'],
    ['Spirochetes', 'Borrelia (Lyme), Treponema pallidum (syphilis), Leptospira. Axial filament motility.'],
    ['Firmicutes (Low GC, Gram+)', 'Clostridium (endospore, anaerobic; tetanus/botulism/gas gangrene/C.diff), Bacillus (endospore; anthrax/cereus/Bt), Staphylococcus (cocci, MRSA), Streptococcus, Listeria, Lactobacillus'],
    ['Actinobacteria (High GC, Gram+)', 'Mycobacterium (TB, leprosy), Streptomyces (antibiotics!), Corynebacterium (diphtheria)'],
    ['Deinococcus radiodurans', '"Conan the bacterium" — extreme radiation resistance'],
    ['Archaea', 'NO known human pathogens. Pseudomurein wall (no peptidoglycan). Ether-linked lipids. Methanogens, halophiles, thermophiles.'],
], [1.7*inch, 5.3*inch]))
story.append(sp(1))

story.append(Paragraph('Ch.5 — Eukaryotes of Microbiology', h3))
story.append(tbl([
    ['Topic', 'Key fact'],
    ['Protozoa supergroups', 'Amoebozoa (Entamoeba — dysentery), Chromalveolata (Apicomplexa: Plasmodium/malaria, Toxoplasma, Cryptosporidium), Excavata (Giardia, Trypanosoma)'],
    ['Apicomplexa', 'Non-motile, obligate intracellular parasites, apical complex for invasion. Complex life cycles.'],
    ['Trypanosoma', 'Excavata (Euglenozoa). T. brucei = African sleeping sickness (tsetse fly). T. cruzi = Chagas disease.'],
    ['Helminths', 'Nematodes (Ascaris, hookworm, pinworm), Trematodes (flukes — Schistosoma), Cestodes (tapeworms — Taenia, no digestive system, scolex with suckers)'],
    ['Fungi forms', 'Yeasts (unicellular, budding); Molds (filamentous, hyphae, mycelium); Dimorphic (yeast 37°C / mold 25°C — Histoplasma, Coccidioides, Blastomyces)'],
    ['Fungal cell wall', 'Chitin (NOT cellulose, NOT peptidoglycan)'],
    ['Algae', 'Diatoms → domoic acid. Dinoflagellates → paralytic shellfish poisoning (neurotoxin). Agar from seaweed.'],
    ['Lichens', 'Fungus + green algae (or cyanobacterium) symbiosis. Slow-growing.'],
], [1.7*inch, 5.3*inch]))
story.append(sp(1))

story.append(Paragraph('Ch.6 — Acellular Pathogens', h3))
story.append(tbl([
    ['Topic', 'Key fact'],
    ['Virus composition', 'Nucleic acid (DNA OR RNA, never both) + capsid (protein coat) ± envelope (lipid bilayer from host membrane)'],
    ['Virus shapes', 'Helical, polyhedral (icosahedral), enveloped, complex (bacteriophages)'],
    ['Lytic cycle (5 steps)', 'Attachment → Penetration → Biosynthesis → Maturation → Release (cell dies)'],
    ['Lysogenic cycle', 'Prophage integrates into host chromosome. Dormant. Can switch to lytic when triggered.'],
    ['Animal virus entry', 'Endocytosis + uncoating (extra step). Release by budding (acquires envelope).'],
    ['Retroviruses', 'Carry reverse transcriptase. RNA → DNA → integrates into host genome. HIV. Major drug target.'],
    ['Viral growth curve', 'Inoculation → Eclipse → Burst (3 phases)'],
    ['Detection', 'Cytopathic effects (CPE), PCR/RT-PCR, hemagglutination, enzyme immunoassay'],
    ['Latent vs Chronic', 'Latent = dormant, can reactivate (herpes, VZV-shingles). Chronic = ongoing disease (HIV/AIDS).'],
    ['Viroids', 'ssRNA, NO protein coat, self-replicating, plant pathogens only (e.g. potato spindle tuber)'],
    ['Prions', 'Misfolded proteins, NO nucleic acid. PrPC → PrPSc conversion. Mad cow (BSE), CJD, scrapie, kuru. Resistant to autoclaving.'],
], [1.7*inch, 5.3*inch]))

doc.build(story)
print('Done -> ' + OUTPUT)
