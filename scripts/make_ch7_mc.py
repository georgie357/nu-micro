from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
import os

os.makedirs('C:/Users/User/Dropbox/Nu micro/Ch 7', exist_ok=True)

doc = SimpleDocTemplate(
    'C:/Users/User/Dropbox/Nu micro/Ch 7/BIO203_Ch7_MC_Questions.pdf',
    pagesize=letter,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.75*inch, bottomMargin=0.75*inch
)

h1  = ParagraphStyle('h1',  fontSize=13, fontName='Helvetica-Bold', spaceAfter=4, spaceBefore=6,
                     alignment=TA_CENTER, borderPad=4, borderWidth=1, borderColor=colors.black,
                     backColor=colors.Color(0.92,0.92,0.92))
h2  = ParagraphStyle('h2',  fontSize=10, fontName='Helvetica-Bold', spaceAfter=3, spaceBefore=10,
                     textColor=colors.Color(0.15,0.15,0.15))
q   = ParagraphStyle('q',   fontSize=9,  fontName='Helvetica-Bold', spaceAfter=2, spaceBefore=5, leading=13)
opt = ParagraphStyle('opt', fontSize=9,  fontName='Helvetica',      spaceAfter=1, leftIndent=16, leading=12)
ans = ParagraphStyle('ans', fontSize=8,  fontName='Helvetica-Oblique', spaceAfter=2, leftIndent=16,
                     leading=11, textColor=colors.Color(0.2,0.2,0.2),
                     borderPad=3, borderWidth=0.5, borderColor=colors.Color(0.6,0.6,0.6),
                     backColor=colors.Color(0.96,0.96,0.96))

story = []
story.append(Paragraph('BIO203 — Chapter 7 Practice Questions', h1))
story.append(Paragraph('50 Multiple Choice  |  Answers + Explanations Below Each Question', h2))
story.append(Paragraph('Sources: OpenStax Microbiology Ch.7 + Popa Lecture Slides',
    ParagraphStyle('src', fontSize=8, fontName='Helvetica-Oblique', spaceAfter=6,
                   textColor=colors.Color(0.3,0.3,0.3), alignment=TA_CENTER)))
story.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceAfter=6))

questions = [

    # ── 7.1 ORGANIC MOLECULES (Q1-15) ──────────────────────────────
    {'section': '7.1 — Organic Molecules & Carbon Chemistry  (Q1–15)'},

    {'q':  '1.  Which element forms the backbone of ALL organic molecules in living cells?',
     'opts':['A. Nitrogen',
             'B. Oxygen',
             'C. Carbon',
             'D. Hydrogen'],
     'ans': 'C',
     'exp': 'Carbon is the basis of life. It forms 4 covalent bonds, allowing it to build the large, diverse molecules required by all living organisms. (Popa slide 3; OpenStax 7.1)'},

    {'q':  '2.  According to Dr. Popa\'s lecture, what are the 4 most common elements in living matter?',
     'opts':['A. C, N, O, P',
             'B. C, N, O, H',
             'C. H, O, Na, Cl',
             'D. C, S, P, K'],
     'ans': 'B',
     'exp': 'Popa slide 3 states directly: "4 most common elements in living matter: C, N, O, and H." These form nearly all biomolecules.'},

    {'q':  '3.  A carbon atom forming a SINGLE bond with four other atoms produces what geometry?',
     'opts':['A. Planar (flat)',
             'B. Linear',
             'C. Tetrahedral',
             'D. Spherical'],
     'ans': 'C',
     'exp': 'Single bonds = tetrahedral arrangement. Double bonds = planar. (Popa slide 6; OpenStax 7.1). Both shapes allow carbon to build diverse structures.'},

    {'q':  '4.  Glucose and fructose share the formula C₆H₁₂O₆ but differ in bonding arrangement. They are called:',
     'opts':['A. Enantiomers',
             'B. Stereoisomers',
             'C. Structural isomers',
             'D. Polymers'],
     'ans': 'C',
     'exp': 'Structural isomers = same molecular formula, different bonding sequence. Enantiomers are a type of stereoisomer (mirror images, same bonding). (Popa slide 7; OpenStax 7.1)'},

    {'q':  '5.  Enantiomers are a type of stereoisomer. What makes them unique?',
     'opts':['A. They have different molecular formulas',
             'B. They are non-superimposable mirror images of each other',
             'C. They differ only in the number of double bonds',
             'D. They are always biologically interchangeable'],
     'ans': 'B',
     'exp': 'Enantiomers (optical isomers) are mirror images with the same bonding sequence but different spatial arrangement. Discovered by Pasteur from wine fermentation crystals in 1848. Many microbes can only use ONE enantiomeric form. (OpenStax 7.1)'},

    {'q':  '6.  Which functional group makes organic acids ACIDIC by donating a proton (H⁺)?',
     'opts':['A. Amino group (-NH₂)',
             'B. Carboxyl group (-COOH)',
             'C. Hydroxyl group (-OH)',
             'D. Methyl group (-CH₃)'],
     'ans': 'B',
     'exp': 'The carboxyl group (-COOH) donates a proton, making the molecule acidic. Found in fatty acids and amino acids. (Popa slide 12; OpenStax 7.1)'},

    {'q':  '7.  Which functional group gives molecules a BASIC (alkaline) character?',
     'opts':['A. Phosphate (-PO₄⁻)',
             'B. Carbonyl (C=O)',
             'C. Amino (-NH₂)',
             'D. Sulfhydryl (-SH)'],
     'ans': 'C',
     'exp': 'The amino group (-NH₂) accepts protons, making the molecule basic. Every amino acid carries one. (Popa slide 13; OpenStax 7.1)'},

    {'q':  '8.  ATP, DNA, RNA, and phospholipids all contain which functional group?',
     'opts':['A. Amino (-NH₂)',
             'B. Hydroxyl (-OH)',
             'C. Carboxyl (-COOH)',
             'D. Phosphate (-PO₄⁻)'],
     'ans': 'D',
     'exp': 'The phosphate group (-PO₄⁻) carries a negative charge and is found in all nucleotides, nucleic acids, ATP, and phospholipids. (Popa slide 15; OpenStax 7.1)'},

    {'q':  '9.  Adding methyl groups (-CH₃) to DNA has what effect, according to Popa\'s slides?',
     'opts':['A. Increases DNA replication speed',
             'B. Makes the DNA less accessible — silences gene expression',
             'C. Causes DNA strand breaks',
             'D. Has no effect on gene expression'],
     'ans': 'B',
     'exp': 'Popa slide 16: "adding methyl groups to DNA makes it less accessible (silences it)." This is epigenetic regulation. (-CH₃ is nonpolar.) (OpenStax 7.1)'},

    {'q':  '10. Disulfide bonds that stabilize protein structure form from which functional group?',
     'opts':['A. Carboxyl (-COOH)',
             'B. Sulfhydryl (-SH)',
             'C. Amino (-NH₂)',
             'D. Phosphate (-PO₄⁻)'],
     'ans': 'B',
     'exp': 'Two sulfhydryl groups (-SH) on cysteine residues oxidize to form a disulfide bond (-S-S-). Critical for tertiary protein structure. (Popa slide 14; OpenStax 7.1)'},

    {'q':  '11. A carbonyl group (C=O) located in the MIDDLE of a carbon chain is called a:',
     'opts':['A. Aldehyde',
             'B. Ester',
             'C. Ketone',
             'D. Amine'],
     'ans': 'C',
     'exp': 'Carbonyl at the END of a chain = aldehyde (aldose sugars). In the MIDDLE = ketone (ketose sugars). (Popa slide 11; OpenStax 7.1)'},

    {'q':  '12. Monomers are joined to make polymers by which type of reaction?',
     'opts':['A. Hydrolysis',
             'B. Oxidation',
             'C. Phosphorylation',
             'D. Dehydration synthesis (condensation)'],
     'ans': 'D',
     'exp': 'Dehydration synthesis removes a water molecule to form a bond between monomers. Hydrolysis is the reverse — adds water to break the bond. (Popa slide 17; OpenStax 7.1)'},

    {'q':  '13. Which reaction breaks polymers back into monomers during digestion?',
     'opts':['A. Dehydration synthesis',
             'B. Hydrolysis',
             'C. Condensation',
             'D. Reduction'],
     'ans': 'B',
     'exp': 'Hydrolysis (adding water) breaks polymer bonds into monomers. Every digestive enzyme (amylase, protease, lipase) catalyzes hydrolysis. (Popa slide 17; OpenStax 7.1)'},

    {'q':  '14. The four groups of carbon-containing macromolecules (biomolecules) in cells are:',
     'opts':['A. Glucose, fatty acids, amino acids, nucleotides',
             'B. Carbohydrates, lipids, proteins, nucleic acids',
             'C. Starch, triglycerides, enzymes, DNA',
             'D. Sugars, waxes, antibodies, ribosomes'],
     'ans': 'B',
     'exp': 'The 4 macromolecule classes from Popa slide 19 and OpenStax Table 7.1: carbohydrates, lipids, proteins, nucleic acids. Ch.7 covers the first three; nucleic acids are in Ch.10.'},

    {'q':  '15. Which statement correctly distinguishes organic from inorganic molecules?',
     'opts':['A. Organic molecules are always large; inorganic are always small',
             'B. Organic molecules contain carbon (plus H); inorganic do not contain both',
             'C. Inorganic molecules always contain carbon',
             'D. Organic molecules dissolve in water; inorganic do not'],
     'ans': 'B',
     'exp': 'Organic = contains carbon AND hydrogen. Carbon oxides (CO₂) and carbonates contain C but not H — considered inorganic. (OpenStax 7.1)'},

    # ── 7.2 CARBOHYDRATES (Q16-25) ─────────────────────────────────
    {'section': '7.2 — Carbohydrates  (Q16–25)'},

    {'q':  '16. What elements make up carbohydrates?',
     'opts':['A. C, H, N, O',
             'B. C, H, O',
             'C. C, N, S, P',
             'D. H, O, N only'],
     'ans': 'B',
     'exp': 'Carbohydrates contain Carbon, Hydrogen, and Oxygen only — empirical formula (CH₂O)n. No nitrogen, unlike proteins and nucleic acids. (Popa slide 20; OpenStax 7.2)'},

    {'q':  '17. Glucose is a 6-carbon monosaccharide. This classifies it as a:',
     'opts':['A. Pentose',
             'B. Triose',
             'C. Hexose',
             'D. Tetrose'],
     'ans': 'C',
     'exp': 'Hexose = 6 carbons (hex = 6). Pentose = 5C (ribose, deoxyribose). Triose = 3C. Glucose is the most abundant monosaccharide in nature. (Popa slide 21; OpenStax 7.2)'},

    {'q':  '18. Which 5-carbon (pentose) sugar is the backbone of DNA?',
     'opts':['A. Glucose',
             'B. Ribose',
             'C. Fructose',
             'D. Deoxyribose'],
     'ans': 'D',
     'exp': 'Deoxyribose is the pentose in DNA (missing one -OH compared to ribose). Ribose is the pentose in RNA. (Popa slide 21; OpenStax 7.2)'},

    {'q':  '19. Two monosaccharides are joined by what type of covalent bond?',
     'opts':['A. Peptide bond',
             'B. Phosphodiester bond',
             'C. Glycosidic bond',
             'D. Hydrogen bond'],
     'ans': 'C',
     'exp': 'A glycosidic bond (formed by dehydration) links monosaccharides together to make disaccharides and polysaccharides. (OpenStax 7.2)'},

    {'q':  '20. Table sugar (sucrose) is a disaccharide consisting of:',
     'opts':['A. Glucose + glucose',
             'B. Glucose + galactose',
             'C. Fructose + galactose',
             'D. Glucose + fructose'],
     'ans': 'D',
     'exp': 'Sucrose = glucose + fructose. Lactose (milk sugar) = glucose + galactose. Maltose (grain sugar) = glucose + glucose. (Popa slide 22; OpenStax 7.2)'},

    {'q':  '21. Which polysaccharide is the primary energy-storage molecule in ANIMALS and also in bacteria?',
     'opts':['A. Starch',
             'B. Cellulose',
             'C. Chitin',
             'D. Glycogen'],
     'ans': 'D',
     'exp': 'Glycogen = energy storage in animals and bacteria. Starch = energy storage in plants. Both are branched polysaccharides of glucose. (Popa slide 23; OpenStax 7.2)'},

    {'q':  '22. Which polysaccharide forms the structural component of plant cell walls?',
     'opts':['A. Glycogen',
             'B. Cellulose',
             'C. Chitin',
             'D. Starch'],
     'ans': 'B',
     'exp': 'Cellulose (linear glucose polymer with beta-1,4 bonds) is the main structural component of plant cell walls — indigestible by most organisms. (Popa slide 23; OpenStax 7.2)'},

    {'q':  '23. The two modified sugar building blocks of bacterial cell wall PEPTIDOGLYCAN are:',
     'opts':['A. Glucose + fructose',
             'B. Ribose + deoxyribose',
             'C. NAG (N-acetyl glucosamine) + NAM (N-acetyl muramic acid)',
             'D. Starch + chitin'],
     'ans': 'C',
     'exp': 'NAG and NAM are modified glucose molecules that alternate in the peptidoglycan backbone. Short peptide chains cross-link the NAM units. Target of penicillin. (Popa slide 25; OpenStax 7.2)'},

    {'q':  '24. Chitin is a polymer of NAG. Where is chitin found? (select ALL correct — choose the best answer)',
     'opts':['A. Bacterial cell walls and plant cell walls',
             'B. Animal muscle tissue',
             'C. Fungal cell walls and arthropod exoskeletons',
             'D. Gram-positive cell walls only'],
     'ans': 'C',
     'exp': 'Chitin (polymer of NAG) is the structural carbohydrate of fungal cell walls and arthropod (insect, crustacean) exoskeletons. NOT found in bacteria (which use peptidoglycan). (Popa slide 25; OpenStax 7.2)'},

    {'q':  '25. Polysaccharides are generally NOT sweet and NOT soluble in water. They are held together by:',
     'opts':['A. Peptide bonds',
             'B. Glycosidic bonds',
             'C. Phosphodiester bonds',
             'D. Hydrogen bonds only'],
     'ans': 'B',
     'exp': 'All polysaccharides use glycosidic bonds (same as disaccharides, just many more of them). The orientation of these bonds (alpha vs beta) determines structure and digestibility. (OpenStax 7.2)'},

    # ── 7.3 LIPIDS (Q26-34) ────────────────────────────────────────
    {'section': '7.3 — Lipids  (Q26–34)'},

    {'q':  '26. Which of the following statements about lipids is TRUE?',
     'opts':['A. Lipids are polymers made of fatty acid monomers',
             'B. Lipids contain only C and H',
             'C. Lipids are hydrophobic and have no true monomers',
             'D. Lipids are water-soluble'],
     'ans': 'C',
     'exp': 'Lipids are hydrophobic, NOT true polymers (no repeating monomer), and can contain C, H, O, and also N, S, P. (Popa slide 26; OpenStax 7.3)'},

    {'q':  '27. A saturated fatty acid has which structural feature?',
     'opts':['A. At least one C=C double bond, making it liquid at room temperature',
             'B. Only C-C single bonds, making it solid at room temperature',
             'C. A ring structure like cholesterol',
             'D. A phosphate head group'],
     'ans': 'B',
     'exp': 'Saturated = all single bonds, maximum H atoms, straight chain → solid at room temp (butter). Unsaturated = double bond(s) → "kinks" in chain → liquid (oil). (Popa slide 29; OpenStax 7.3)'},

    {'q':  '28. A triglyceride (triacylglycerol) is composed of:',
     'opts':['A. Three amino acids + glycerol',
             'B. Glycerol + three fatty acids (ester bonds)',
             'C. Two fatty acids + a phosphate group + glycerol',
             'D. Three monosaccharides + glycerol'],
     'ans': 'B',
     'exp': 'Triglycerides = glycerol backbone + 3 fatty acids joined by ester bonds via dehydration synthesis. Primary form of long-term energy storage; provide >2× calories vs carbs/proteins. (Popa slide 27; OpenStax 7.3)'},

    {'q':  '29. What makes phospholipids AMPHIPATHIC?',
     'opts':['A. They contain three fatty acid chains',
             'B. They have a hydrophilic phosphate head AND hydrophobic fatty acid tails',
             'C. They are found only in eukaryotic membranes',
             'D. They are positively charged'],
     'ans': 'B',
     'exp': 'Amphipathic = has both water-loving (polar phosphate head) and water-fearing (nonpolar fatty acid tails) regions. This drives spontaneous bilayer formation in water. (Popa slide 30; OpenStax 7.3)'},

    {'q':  '30. In a phospholipid BILAYER (cell membrane), how are the fatty acid tails oriented?',
     'opts':['A. Facing outward into the aqueous environment',
             'B. Facing inward, sandwiched between the two layers, away from water',
             'C. Randomly distributed throughout the bilayer',
             'D. Attached directly to membrane proteins'],
     'ans': 'B',
     'exp': 'In the lipid bilayer, hydrophobic tails face INWARD (toward each other), shielded from water. Hydrophilic heads face OUTWARD into the aqueous environments on both sides. (Popa slide 31; OpenStax 7.3)'},

    {'q':  '31. Prokaryotes generally do NOT produce cholesterol. Instead, they use _____ to stabilize their membranes.',
     'opts':['A. Triglycerides',
             'B. Waxes',
             'C. Ergosterol',
             'D. Hopanoids'],
     'ans': 'D',
     'exp': 'Hopanoids are multiringed structures in bacteria that function like cholesterol — they strengthen bacterial membranes. Ergosterol is the equivalent in fungi and some protozoa. (OpenStax 7.3)'},

    {'q':  '32. Ergosterol is found in fungal cell membranes. Why is this clinically significant?',
     'opts':['A. It makes fungi Gram-positive',
             'B. It is the target of antifungal drugs (e.g., fluconazole)',
             'C. It makes fungi acid-fast',
             'D. It is identical to human cholesterol'],
     'ans': 'B',
     'exp': 'Because ergosterol is unique to fungi (not in human cells), antifungal drugs like azoles target ergosterol biosynthesis — selectively killing fungi without harming human cells. (OpenStax 7.3)'},

    {'q':  '33. Mycobacterium tuberculosis resists decolorization in the acid-fast stain because of which lipid?',
     'opts':['A. Cholesterol in its plasma membrane',
             'B. Mycolic acid — a waxy lipid in its cell wall',
             'C. Phospholipid bilayer with extra outer membrane',
             'D. High glycogen content'],
     'ans': 'B',
     'exp': 'Mycolic acid is a long-chain waxy lipid in the Mycobacterium cell wall. It forms a waxy coat that resists decolorization — the basis of acid-fast staining. (OpenStax 7.3)'},

    {'q':  '34. Isoprenoids are lipids derived from isoprene. According to Popa\'s lecture, they are used as:',
     'opts':['A. Energy storage only',
             'B. Pigments, fragrances, and pharmaceuticals',
             'C. Building blocks of DNA',
             'D. Structural components of peptidoglycan'],
     'ans': 'B',
     'exp': 'Popa slide 32: isoprenoids can be used as pigments (e.g., beta-carotene), fragrances (menthol, camphor, limonene, pinene), and pharmaceuticals (capsaicin). (OpenStax 7.3)'},

    # ── 7.4 PROTEINS (Q35-45) ──────────────────────────────────────
    {'section': '7.4 — Proteins  (Q35–45)'},

    {'q':  '35. Which elements are always present in proteins?',
     'opts':['A. C, H, O only',
             'B. C, H, N, O (some also contain S and P)',
             'C. C, N, P, S only',
             'D. C, H, O, P always'],
     'ans': 'B',
     'exp': 'Proteins always contain C, H, N, O. The N (from amino groups) distinguishes them from carbs and lipids. Some also contain S (cysteine, methionine) and P. (Popa slide 34; OpenStax 7.4)'},

    {'q':  '36. All 20 amino acids share the same core structure bonded to an alpha carbon. What is the variable part?',
     'opts':['A. The amino group',
             'B. The carboxyl group',
             'C. The R group (side chain)',
             'D. The central carbon itself'],
     'ans': 'C',
     'exp': 'All amino acids share: amino group + carboxyl group + H + alpha carbon. The R group (side chain) is what differs — determining polarity, charge, size, and reactivity. (Popa slide 35; OpenStax 7.4)'},

    {'q':  '37. A peptide bond forms by a dehydration reaction between the _____ of one amino acid and the _____ of the next.',
     'opts':['A. R group … R group',
             'B. Carboxyl (-COOH) … amino (-NH₂)',
             'C. Amino (-NH₂) … amino (-NH₂)',
             'D. Carboxyl (-COOH) … carboxyl (-COOH)'],
     'ans': 'B',
     'exp': '-COOH of one amino acid + -NH₂ of the next → peptide bond + H₂O released. This is the backbone bond of every polypeptide. (Popa slide 36; OpenStax 7.4)'},

    {'q':  '38. According to Popa\'s slide 37, ALL four levels of protein structure together determine:',
     'opts':['A. The amino acid sequence only',
             'B. The number of subunits in the protein',
             'C. The structure of the protein, which is NECESSARY for its function',
             'D. Only the 3D shape, not the function'],
     'ans': 'C',
     'exp': 'Popa slide 37: "ALL together determine the structure of the protein, which is NECESSARY for its function." Structure = function is the central concept of protein biology.'},

    {'q':  '39. Alpha (α) helices and beta (β) pleated sheets are stabilized by which type of bond?',
     'opts':['A. Peptide bonds',
             'B. Disulfide bonds',
             'C. Ionic bonds',
             'D. Hydrogen bonds between backbone carbonyl and amino groups'],
     'ans': 'D',
     'exp': 'Secondary structure (α-helix, β-sheet) is formed by hydrogen bonds between backbone C=O and N-H groups — NOT the R side chains. (OpenStax 7.4)'},

    {'q':  '40. Tertiary structure (overall 3D shape) of a polypeptide is stabilized by all of the following EXCEPT:',
     'opts':['A. Disulfide bridges (-S-S-)',
             'B. Hydrophobic interactions between nonpolar side chains',
             'C. Peptide bonds between every amino acid',
             'D. Hydrogen bonds and van der Waals forces'],
     'ans': 'C',
     'exp': 'Peptide bonds are part of PRIMARY structure — they form the backbone. Tertiary structure is held by weaker interactions: H-bonds, disulfide bridges, hydrophobic interactions, van der Waals. (OpenStax 7.4)'},

    {'q':  '41. Hemoglobin has two α-subunits and two β-subunits. This assembly is an example of:',
     'opts':['A. Primary structure',
             'B. Secondary structure',
             'C. Tertiary structure',
             'D. Quaternary structure'],
     'ans': 'D',
     'exp': 'Quaternary structure = multiple polypeptide chains (subunits) assembled together. Hemoglobin (4 subunits) is the textbook example. (Popa slide 37; OpenStax 7.4)'},

    {'q':  '42. A protein loses its 3D shape but its amino acid sequence is unchanged. This is called:',
     'opts':['A. Mutation',
             'B. Denaturation',
             'C. Hydrolysis',
             'D. Translation'],
     'ans': 'B',
     'exp': 'Denaturation = loss of 2°, 3°, and 4° structure without breaking peptide bonds (primary structure intact). Caused by heat or pH changes. Function is lost. (Popa slide 44; OpenStax 7.4)'},

    {'q':  '43. Cystic fibrosis is caused by the loss of a single amino acid (phenylalanine) in the CFTR protein. This directly alters which level of protein structure?',
     'opts':['A. Quaternary structure',
             'B. Tertiary structure',
             'C. Primary structure',
             'D. Secondary structure'],
     'ans': 'C',
     'exp': 'A gene mutation changes the primary structure (amino acid sequence). This cascades to alter folding and function. CF results from one missing AA out of ~1480. (OpenStax 7.4 — Micro Connections box)'},

    {'q':  '44. Autoclaving sterilizes equipment by exposing it to 121°C steam. Why does this kill microbes?',
     'opts':['A. High pressure ruptures cell membranes',
             'B. Heat denatures proteins — enzymes and structural proteins stop functioning',
             'C. Steam oxidizes DNA',
             'D. Heat dissolves peptidoglycan'],
     'ans': 'B',
     'exp': 'High heat denatures proteins (reversible at mild temps, irreversible at extreme temps). This inactivates all microbial enzymes, destroying function and killing the organism. (Popa slide 44; OpenStax 7.4)'},

    {'q':  '45. A glycoprotein is a conjugated protein that has what attached to it?',
     'opts':['A. A lipid molecule',
             'B. A carbohydrate moiety',
             'C. A nucleic acid sequence',
             'D. A phosphate group'],
     'ans': 'B',
     'exp': 'Glycoproteins = protein + carbohydrate. Lipoproteins = protein + lipid. Both are important membrane components. Glycoproteins on cell surfaces are used in serological ID tests. (OpenStax 7.4)'},

    # ── 7.5 IDENTIFICATION (Q46-50) ────────────────────────────────
    {'section': '7.5 — Using Biochemistry to Identify Microorganisms  (Q46–50)'},

    {'q':  '46. MALDI-TOF mass spectrometry identifies microbes by:',
     'opts':['A. Detecting antigen-antibody reactions on the cell surface',
             'B. Firing a UV laser at the microbe, generating ions that are separated by mass and compared to a reference database',
             'C. Analyzing fatty acid methyl esters by gas chromatography',
             'D. Sequencing 16S rRNA genes'],
     'ans': 'B',
     'exp': 'MALDI-TOF: pulsed UV laser ionizes microbial chemicals. Ions travel to detector — heavier ones arrive later (time-of-flight). Unique mass spectrum is compared to a database. Now STANDARD in clinical microbiology labs. (Popa slide 46; OpenStax 7.5)'},

    {'q':  '47. In FAME analysis, what are the bacterial fatty acids converted into before analysis?',
     'opts':['A. Amino acid derivatives',
             'B. Volatile methyl esters analyzed by gas chromatography',
             'C. Phospholipid bilayer fragments',
             'D. Nucleotide sequences'],
     'ans': 'B',
     'exp': 'FAME = Fatty Acid Methyl Ester. Fatty acids are extracted, chemically converted to methyl esters (making them volatile), then separated by GC. The chromatogram peak pattern is species-unique. (Popa slide 47; OpenStax 7.5)'},

    {'q':  '48. Lancefield group tests identify Streptococcus species by detecting:',
     'opts':['A. Unique lipid profiles using FAME',
             'B. Specific carbohydrate antigens on the cell surface using antibodies',
             'C. Mass spectrum of bacterial proteins by MALDI-TOF',
             'D. DNA sequences of virulence genes'],
     'ans': 'B',
     'exp': 'Lancefield tests are serological: antibodies bind specific carbohydrates on the Streptococcus surface, causing agglutination. Group A (S. pyogenes) causes strep throat. (Popa slide 48; OpenStax 7.5)'},

    {'q':  '49. Proteomic analysis identifies microorganisms by:',
     'opts':['A. Detecting storage granules like poly-β-hydroxybutyrate (PHB)',
             'B. Separating proteins by HPLC, digesting them, and analyzing by MALDI-TOF',
             'C. Using antibodies to detect surface carbohydrates',
             'D. Growing colonies on selective media'],
     'ans': 'B',
     'exp': 'Proteomic analysis: proteins separated by high-pressure liquid chromatography (HPLC), digested into peptides, analyzed by MALDI-TOF, and matched to a database. (Popa slide 48; OpenStax 7.5)'},

    {'q':  '50. Some Pseudomonas species can be identified by the ABSENCE of which storage compound, while P. aeruginosa lacks it?',
     'opts':['A. Glycogen',
             'B. Chitin',
             'C. Poly-β-hydroxybutyrate (PHB)',
             'D. Starch'],
     'ans': 'C',
     'exp': 'PHB (poly-β-hydroxybutyrate) is a carbon/energy storage granule. Non-fluorescent Pseudomonas accumulate PHB; fluorescent species like P. aeruginosa (human pathogen) do NOT. Presence/absence helps differentiate species. (OpenStax 7.5)'},
]

for item in questions:
    if 'section' in item:
        story.append(Spacer(1, 0.08*inch))
        story.append(Paragraph(item['section'], h2))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.Color(0.5,0.5,0.5), spaceAfter=3))
        continue
    story.append(Paragraph(item['q'], q))
    for o in item['opts']:
        story.append(Paragraph(o, opt))
    story.append(Paragraph(f"✓ Answer: {item['ans']} — {item['exp']}", ans))
    story.append(Spacer(1, 0.03*inch))

doc.build(story)
print('Ch7 MC questions PDF saved successfully.')
