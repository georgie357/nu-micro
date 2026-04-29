# NU Microbiology — Chapter Study Method

---

## 🛑 READ THIS DOCUMENT BEFORE MAKING ANYTHING FOR BIO203 — AND BEFORE ANSWERING QUESTIONS

**This file is the production system for all BIO203 National University Microbiology study materials.**

Before writing any script, any PDF, any study guide, any MC questions, or any lab report for this course — **read this document first.** Not the summary. The whole thing.

Why this rule exists:
- Ch.1&2 study guide was originally written from memory → wrong emphasis, wrong terminology, missed Popa's actual tested content
- Ch.7 study guide was written without reading the textbook → same problem
- Lab 1 and Lab 2 files were built without reading the lecture slides → no lecture-to-lab connections
- Every single rebuild came from skipping this step

**The correct order, every time, no exceptions:**
1. Read this file
2. Extract source material (slides + textbook) — see Step 0 below
3. Read the extracted material
4. Then write the script

If you skip steps 1–3, the output will be wrong and will need to be rebuilt.

---

## How to Answer Questions in Chat

When the student asks a question about course material, answer in this order:

### 1. Popa slide answer first
Lead with exactly what the professor put on the slide — the specific wording, the specific fact, the specific example. Cite the slide number. This is what gets tested.

### 2. Expand with textbook detail
After giving the slide answer, expand using the OpenStax chapter to add depth, mechanism, or context that helps it make sense. Cite the section (e.g., OpenStax 2.4).

### 3. Flag what Popa emphasizes
If Popa dedicated a full slide to something, or repeated it across multiple slides, call that out explicitly — it signals exam priority.

### 4. Give a concrete example
Anchor every concept to a real organism, disease, or lab observation from the course materials. Abstract facts without examples are hard to retain.

### 5. Connect to the lab when relevant
If the concept appeared in Lab 1 or Lab 2, tie it back — "you saw this when..." or "this is why the protocol says...". Lab practicals test the same content.

**The goal:** The student learns what the professor finds most important, not a generic textbook answer. Popa's slides define the emphasis. The textbook provides the mechanism. Examples make it stick.

---

## Core Principle
Go chapter by chapter, concept by concept. Never jump ahead. Always anchor to **what that specific chapter wants you to know** — not the full deep dive across all chapters.

---

## Step 1 — Identify What the Chapter Covers
Before studying, list the chapter's concepts at a high level.
Example — Ch.1 Intro to Microbiology:
- What is Microbiology?
- The 6 groups of microorganisms
- History of Microbiology
- Why microbes matter

---

## Step 2 — Go Concept by Concept
For each concept, cover it in this order:
1. **What is it** — one sentence definition
2. **Key facts** — bullet points only, no fluff
3. **Examples** — real organisms or diseases to anchor the memory
4. **Why it matters** — clinical or ecological relevance
5. **Size/scale** if applicable

---

## Step 3 — The 6 Groups Formula (Ch.1 Model)
When a chapter introduces a group of microorganisms, cover each group with:
- Prokaryote or Eukaryote?
- Single-celled or multicellular?
- How they feed / survive
- Disease relevance (if any)
- Key examples
- Size

### Ch.1 — The 6 Groups Quick Reference
| Group | Pro/Euk | Disease? | Key Example |
|---|---|---|---|
| Bacteria | Prokaryote | Yes | E. coli, Streptococcus |
| Archaea | Prokaryote | No | Methanogens, Halophiles |
| Fungi | Eukaryote | Some | Candida, Aspergillus |
| Protozoa | Eukaryote | Yes | Plasmodium (malaria), Giardia |
| Algae | Eukaryote | No | Diatoms, green algae |
| Viruses | Neither (not alive) | Yes | Influenza, HIV |

---

## Step 4 — Stay in the Chapter
If a concept appears in Ch.1 but the deep detail is in Ch.3 or Ch.4 — **note it, don't teach it yet.**
Example: Gram staining is introduced visually in Ch.2, deep detail in Ch.3/Ch.4. Don't mix them.

---

## Step 5 — Size Scale (Always Know This)
| Microbe | Size |
|---|---|
| Protozoa | 10–100 µm |
| Fungi (yeast) | 3–10 µm |
| Bacteria | 1–10 µm |
| Viruses | 20–300 nm |

**Conversion:** 1 mm = 1,000 µm = 1,000,000 nm

---

## Progress Log

### Ch.1 — Intro to Microbiology ✓ COMPLETE
- [x] 1.3 — Types of Microorganisms (The 6 Groups)
- [x] 1.1 — What Our Ancestors Knew (History, key scientists, spontaneous generation, Koch's Postulates)
- [x] 1.2 — A Systematic Approach (Scientific method, nomenclature, taxonomy, 3 domains, culture basics)

### Ch.2 — Microscopy & Staining ✓ COMPLETE
- [x] 2.1 — Properties of Light (wavelength, resolution, refraction, magnification vs resolution, immersion oil)
- [x] 2.2 — Peering Into the Invisible World (Leeuwenhoek, Hooke, simple vs compound, magnification formula)
- [x] 2.3 — Instruments of Microscopy (brightfield, darkfield, phase-contrast, fluorescence, TEM, SEM)
- [x] 2.4 — Staining Microscopic Specimens (Gram stain steps, acid-fast, endospore, capsule, flagella)

---

## Dropbox Folder Structure
`C:\Users\User\Dropbox\Nu micro\`

| Folder | Contents |
|---|---|
| `chapter 1 and 2\` | Study guide PDF, MC questions PDF, Lab 1 PDFs |
| `Ch 7\` | Study guide PDF, MC questions PDF |
| *(root)* | Syllabi, **textbook PDF**, README, sync script |

### ⚠️ TEXTBOOK LOCATION
**`C:\Users\User\Dropbox\Nu micro\microbiology_-_WEB.pdf`** — OpenStax Microbiology (full textbook)

**RULE: Before writing ANY chapter study guide, read the relevant chapter from this PDF first.**
Do NOT write study guides from general knowledge. Always source content from:
1. `microbiology_-_WEB.pdf` — the actual textbook chapter
2. Lecture slides if available in the chapter folder

Writing from memory = wrong emphasis, wrong terminology, misses what Popa actually tested.
This mistake was made for Ch.7 — study guide was written without reading the textbook.

---

## Materials Per Chapter

### Chapter 1 & 2 — ✓ COMPLETE (Version 2)
**Folder:** `chapter 1 and 2\`
**Scripts:** `Desktop\recent\make_ch1_ch2_pdf_v2.py`, `Desktop\recent\make_ch1_ch2_mc_v2.py`

| File | Version | Status | Built from |
|---|---|---|---|
| BIO203_Ch1_Ch2_Study_Guide.pdf | v1 — RETIRED | ⚠️ Written from memory, do not use | — |
| BIO203_Ch1_Ch2_MC_Questions.pdf | v1 — RETIRED | ⚠️ Written from memory, do not use | — |
| BIO203_Ch1_Ch2_Study_Guide_v2.pdf | **v2 — CURRENT** | ✓ Done | Ch.1 slides (29) + Ch.2 slides (33) + textbook PDF pages 22–82 |
| BIO203_Ch1_Ch2_MC_Questions_v2.pdf (50 Qs) | **v2 — CURRENT** | ✓ Done | All 50 questions cite specific Popa slide + OpenStax section |

**What v2 covers (Ch.1):** microbiology definition, size scale, full history timeline (Leeuwenhoek 1675 through Fleming 1928), key scientists table (Pasteur/Koch/Jenner/Ehrlich/Fleming with exact contributions), taxonomy history (Linnaeus 1758 → Woese/Fox 1970s rRNA → three-domain), binomial nomenclature rules, 8 groups table (Bacteria/Archaea/Algae/Protozoa/Fungi/Helminths/Viruses/Prions) with full detail on viruses and prions, modern biotech/microbiome/CRISPR.

**What v2 covers (Ch.2):** wave properties, light interactions, refraction + immersion oil mechanism, EM spectrum/energy relationship, magnification vs resolution vs contrast (with NA), history of microscopy timeline, all 7 light microscope types (brightfield/darkfield/phase-contrast/DIC/fluorescence/confocal/two-photon) with mechanism+image+best uses, TEM vs SEM full comparison table, scanning probe (STM/AFM), specimen prep (wet mount/smear/fixation), staining principles (basic vs acidic dyes), all 5 stain types (simple/Gram/acid-fast/capsule/endospore/flagella) with full step-by-step.

---

### Chapter 7 — Biochemistry (Thu Apr 30) ✓ COMPLETE
**Folder:** `Ch 7\`
**Scripts:** `Desktop\recent\make_ch7_pdf.py`, `Desktop\recent\make_ch7_mc.py`

| File | Status | Built from |
|---|---|---|
| BIO203_Ch7_Study_Guide.pdf | ✓ Done | Ch.7 slides (49) + textbook PDF pages 267–294 |
| BIO203_Ch7_MC_Questions.pdf (50 Qs) | ✓ Done | All questions cite specific Popa slide + OpenStax section |

---

### Lab 1 — Microscopy ✓ COMPLETE (Version 2)
**Folder:** `chapter 1 and 2\`
**Scripts:** `Desktop\recent\make_lab1_report.py`, `Desktop\recent\make_lab1_guide.py`

| File | Version | Status | Built from |
|---|---|---|---|
| BIO203A_Lab1_Filled.pdf | v1 — RETIRED | ⚠️ No lecture connections, do not use | — |
| BIO203A_Lab1_Study_Guide.pdf | v1 — RETIRED | ⚠️ No lecture connections, do not use | — |
| BIO203A_Lab1_Filled_v2.pdf | **v2 — CURRENT** | ✓ Done | Lab 1 docx + Ch.1 slides + Ch.2 slides |
| BIO203A_Lab1_Study_Guide_v2.pdf | **v2 — CURRENT** | ✓ Done | Lab 1 docx + Ch.1 slides + Ch.2 slides |

**What Lab 1 v2 covers:** Full microscope parts table with critical rules (coarse/fine focus, handling, storage), magnification+FOV table for all 4 objectives with FOV calculation formula, immersion oil/refraction/RI explanation tied to Ch.2 slides 6&10, organisms observed table (Paramecium/yeast/Bacillus/algae/mold) each linked to Ch.1 domain/classification, staining connections (simple/Gram/wet mount/endospore), worked FOV calculation examples (Bacillus 2µm and yeast 10µm across 450µm FOV), 8 practice Q&A pairs, key numbers table with slide citations.

### Lab 2 — Plating of Soil Samples ✓ COMPLETE
**Folder:** `chapter 1 and 2\`
**Scripts:** `Desktop\make_lab2_report.py`, `Desktop\make_lab2_guide.py`

| File | Status | Built from |
|---|---|---|
| BIO203A_Lab2_Filled.pdf | ✓ Done | Lab 2 docx + Ch.7 biochemistry connections |
| BIO203A_Lab2_Study_Guide.pdf | ✓ Done | Lab 2 docx + Ch.7 biochemistry connections |

---

### Chapter 3 — Cell Structure (Tue May 5)
**Folder:** `chapter 3\` *(to be created)*
| File | Status |
|---|---|
| BIO203_Ch3_Study_Guide.pdf | Pending |
| BIO203_Ch3_MC_Questions.pdf | Pending |

---

### Chapter 4 & 5 — Prokaryotes & Eukaryotes (Thu May 7)
**Folder:** `chapter 4 and 5\` *(to be created)*
| File | Status |
|---|---|
| BIO203_Ch4_Ch5_Study_Guide.pdf | Pending |
| BIO203_Ch4_Ch5_MC_Questions.pdf | Pending |

---

### Chapter 6 — Acellular Pathogens (Sat May 9)
**Folder:** `chapter 6\` *(to be created)*
| File | Status |
|---|---|
| BIO203_Ch6_Study_Guide.pdf | Pending |
| BIO203_Ch6_MC_Questions.pdf | Pending |

---

### Next Up
- **Ch.3 — Cell Structure** (Tue May 5)

---

## PDF Print Rules
- All PDFs must be **black and white compatible** — no color-only formatting
- Use borders/lines for table structure instead of colored backgrounds
- Bold text for headers instead of color
- High contrast — dark text on white background only
- No shading that disappears when printed grayscale

---

## PDF Generation — Lessons Learned

### Table Formatting (reportlab)
**Problem:** Table cells with long text or `\n` newlines break layout — text overflows or newlines are ignored.

**Fix — always wrap cell content in Paragraph objects:**
```python
cell_body = ParagraphStyle('cell_body', fontSize=8, fontName='Helvetica', leading=11, spaceAfter=0)
cell_bold = ParagraphStyle('cell_bold', fontSize=8, fontName='Helvetica-Bold', leading=11, spaceAfter=0)

def _cell(val, is_header=False):
    if isinstance(val, str):
        text = val.replace('\n', '<br/>')
        style = cell_bold if is_header else cell_body
        return Paragraph(text, style)
    return val

def tbl(data, col_widths=None):
    wrapped = []
    for i, row in enumerate(data):
        wrapped.append([_cell(cell, is_header=(i == 0)) for cell in row])
    t = Table(wrapped, colWidths=col_widths, repeatRows=1)
    ...
```

**Rules:**
- Never pass raw strings directly into Table data — always wrap via `_cell()`
- Use `\n` in source strings freely; `_cell()` converts them to `<br/>` for Paragraph rendering
- Header row (row 0) gets `Helvetica-Bold`; all other rows get `Helvetica`
- Use `colors.Color(0.82, 0.82, 0.82)` for header background (B&W safe)
- Use `colors.Color(0.95, 0.95, 0.95)` for alternating row background (B&W safe)
- Always set `TOPPADDING`, `BOTTOMPADDING`, `LEFTPADDING`, `RIGHTPADDING` explicitly to 4 — don't use `PADDING` shorthand (less reliable)
- Always set `VALIGN TOP` so multi-line cells align from the top

### General PDF Script Pattern
- All scripts: `make_<chapter>_pdf.py` saved to `C:\Users\User\Desktop\recent\`
- Output always to `C:\Users\User\Dropbox\Nu micro\<chapter folder>\`
- Use `os.makedirs(..., exist_ok=True)` to auto-create output folder
- Style objects defined once at top of file: `h1`, `h2`, `h3`, `body`, `bold`, `note`, `cell_body`, `cell_bold`
- `tbl()` helper used for every table — never raw Table() calls in story

---

## How to Make Everything — Full Workflow for Future Chapters

### STEP 0 — Extract Source Material First (ALWAYS)

**Textbook chapter extraction (Python):**
```python
import pdfplumber
path = r'C:\Users\User\Dropbox\Nu micro\microbiology_-_WEB.pdf'
with pdfplumber.open(path) as pdf:
    # Find chapter start page by scanning for chapter title
    for i, page in enumerate(pdf.pages):
        text = page.extract_text() or ''
        if 'Chapter X' in text or 'Chapter Title' in text:
            print(f'Starts at PDF page index {i}')
            break
    # Extract all chapter pages to file
    full = []
    for i in range(START_INDEX, END_INDEX):
        full.append(f'=== PDF PAGE {i+1} ===')
        full.append(pdf.pages[i].extract_text() or '')
with open(r'C:\Users\User\Desktop\chX_textbook_raw.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(full))
```
- The TOC is around PDF pages 7–10 — scan it to find textbook page numbers for the chapter
- Textbook page ≠ PDF index — offset is ~13–14 pages (check TOC result each time)
- Save raw text to Desktop for reading before writing any study material

**Lecture slides extraction (Python):**
```python
from pptx import Presentation
prs = Presentation(r'C:\Users\User\Dropbox\Nu micro\Ch X\Bio203.chX.pptx')
for i, slide in enumerate(prs.slides):
    print(f'--- SLIDE {i+1} ---')
    for shape in slide.shapes:
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                text = para.text.strip()
                if text:
                    print(text)
```
- Slides are the PRIMARY source — they show exactly what Popa emphasizes and tests
- Textbook fills in detail and examples
- Never write from memory — always extract first

**Lab report docx extraction (Python):**
```python
from docx import Document
doc = Document(r'C:\Users\User\Dropbox\Nu micro\...\LabX.docx')
for para in doc.paragraphs:
    if para.text.strip():
        print(f'style={para.style.name!r}  text={para.text!r}')
for table in doc.tables:
    for row in table.rows:
        print(' | '.join(c.text.strip() for c in row.cells))
```

---

### STEP 1 — Lecture Study Guide (`make_chX_pdf.py`)

**Script location:** `C:\Users\User\Desktop\recent\make_chX_pdf.py`
**Output:** `C:\Users\User\Dropbox\Nu micro\<chapter folder>\BIO203_ChX_Study_Guide.pdf`

**Structure to follow (Ch.7 as the model):**
1. Title block (h1, centered, bordered, grey background)
2. Learning Outcomes — pulled verbatim from slide 2 of the lecture deck
3. One section per textbook section (7.1, 7.2 etc.) — use h1 for section headers
4. Within each section: h2 for sub-topics, tables for comparisons, note-style paragraphs for clinical connections
5. Final page: Quick Reference Summary — the 4 biomolecules table + "Must-Know Microbiology Connections" table
6. Every table uses the `tbl()` helper with Paragraph-wrapped cells (see Table Formatting above)
7. End with `doc.build(story)` + print confirmation

**What to include per section (sourced from textbook + slides):**
- Learning objectives stated at top of each section (textbook has these)
- Key definitions — exact textbook wording where possible
- Popa's specific examples and emphasis (from slides) — these are what get tested
- Clinical/microbiology connections called out explicitly
- Any "Check Your Understanding" or review questions from textbook = likely exam material

---

### STEP 2 — MC Questions (`make_chX_mc.py`)

**Script location:** `C:\Users\User\Desktop\recent\make_chX_mc.py`
**Output:** `C:\Users\User\Dropbox\Nu micro\<chapter folder>\BIO203_ChX_MC_Questions.pdf`

**50 questions — distribution:**
- ~15 questions per major section (for a 5-section chapter like Ch.7)
- Adjust proportionally — bigger sections get more questions
- Section header dividers in the PDF (use h2 style between groups)

**Question writing rules:**
- Source every question from the actual textbook or lecture slide — cite in the answer (e.g., "Popa slide 3; OpenStax 7.1")
- Prioritize: (1) Popa's slide content, (2) textbook learning objectives, (3) "Check Your Understanding" boxes, (4) textbook review questions
- 4 answer choices (A–D); one clearly correct, distractors are plausible but wrong for specific reasons
- Answer explanation: state WHY the correct answer is right AND why the main distractor is wrong
- Format: bold question → indented options a–d → italic answer box with explanation

**Style objects used:**
```python
h1  = ... (chapter/title header)
h2  = ... (section divider)
q   = ParagraphStyle('q', fontName='Helvetica-Bold', fontSize=9, ...)
opt = ParagraphStyle('opt', fontName='Helvetica', fontSize=9, leftIndent=16, ...)
ans = ParagraphStyle('ans', fontName='Helvetica-Oblique', fontSize=8, leftIndent=16,
                     borderPad=3, borderWidth=0.5, backColor=colors.Color(0.96,0.96,0.96), ...)
```

---

### STEP 3 — Lab Report (`make_labX_report.py`)

**Script location:** `C:\Users\User\Desktop\make_labX_report.py`
**Output:** `C:\Users\User\Dropbox\Nu micro\chapter X\BIO203A_LabX_Filled.pdf`

**Workflow:**
1. Extract the .docx lab sheet first (Step 0 above) — get exact question wording and table structure
2. Fill in Table 1 (data collection) with realistic values for NU LA campus / the actual lab date
3. Fill in procedure fields with the actual media/dilutions used in this lab
4. Fill in colony table (Table 2) with realistic colony types for the organism/sample type
5. Show all calculations fully worked — every formula step visible
6. Answer all discussion questions with 2–3 sentence responses connecting to lecture content
7. Add note at top: "Drawings and photos must be added from your own observations"

**Realistic defaults for soil plating (Labs 1–3):**
- Location: NU LA Campus, 5230 Pacific Concourse Drive
- Medium: R2A agar for soil; TSA for body-site samples
- Temperature: 25°C for soil/environmental; 37°C for clinical/body-site
- Dilutions: 10⁻², 10⁻³, 10⁻⁴ — best plate usually 10⁻³
- CFU/g range: 10⁶–10⁹ for soil

---

### STEP 4 — Lab Study Guide (`make_labX_guide.py`)

**Script location:** `C:\Users\User\Desktop\make_labX_guide.py`
**Output:** `C:\Users\User\Dropbox\Nu micro\chapter X\BIO203A_LabX_Study_Guide.pdf`

**Required sections for every lab study guide:**
1. **Purpose** — why this lab matters (1 table: goal → how lab achieves it)
2. **Key technique** — the core skill of the lab (serial dilution, Gram stain, etc.) — step-by-step table
3. **Formulas/calculations** — fully worked example with variable table + step-by-step table + common mistakes table
4. **Materials/reagents** — what each reagent does and why (connects to biochemistry)
5. **Observations/morphology** — what to look for, how to describe it, what it means
6. **Aseptic technique rules** — always include for any wet lab
7. **Lecture chapter connections** — explicit table linking lab observations to the current chapter's biochemistry
8. **Antibiotic Discovery project connection** — if applicable (Labs 2 onward)
9. **Quick Reference** — formulas, key facts, rules in one table at the end

**Ch.7 connection template (use for any lab in Weeks 1–2):**
- Any media choice → connects to carbohydrates (energy source, §7.2) and proteins (peptone/amino acids, §7.4)
- Temperature choice → connects to protein structure/denaturation (§7.4)
- Colony color/pigment → connects to isoprenoids/carotenoids (§7.3)
- Mucoid colonies → connects to polysaccharide capsule (§7.2)
- Diluent choice (saline) → connects to membrane/osmotic balance (§7.3 phospholipids)

---

### Script Naming Convention

| Script | Location | Output file |
|---|---|---|
| `make_chX_pdf_v2.py` | `Dropbox\Nu micro\scripts\` + `Desktop\recent\` | `Dropbox\Nu micro\Ch X\BIO203_ChX_Study_Guide_v2.pdf` |
| `make_chX_mc_v2.py` | `Dropbox\Nu micro\scripts\` + `Desktop\recent\` | `Dropbox\Nu micro\Ch X\BIO203_ChX_MC_Questions_v2.pdf` |
| `make_labX_report.py` | `Dropbox\Nu micro\scripts\` + `Desktop\recent\` | `Dropbox\Nu micro\chapter X\BIO203A_LabX_Filled_v2.pdf` |
| `make_labX_guide.py` | `Dropbox\Nu micro\scripts\` + `Desktop\recent\` | `Dropbox\Nu micro\chapter X\BIO203A_LabX_Study_Guide_v2.pdf` |

**Version suffix rule:** If rebuilding a file that was previously made from memory or without source material, append `_v2` to the filename. New chapters start without suffix (already using the correct method).

**Retired files:** v1 files remain in Dropbox but should not be used. Only use the most recent version.

**Canonical script location:** `Dropbox\Nu micro\scripts\` is the authoritative copy (in git). `Desktop\recent\` is a working copy. Always keep them in sync — after editing on Desktop, copy to scripts/ and commit.

---

### Running Scripts

```powershell
# Set UTF-8 output to avoid encoding errors on Windows
$env:PYTHONIOENCODING="utf-8"

python "C:\Users\User\Dropbox\Nu micro\scripts\make_chX_pdf_v2.py"
python "C:\Users\User\Dropbox\Nu micro\scripts\make_chX_mc_v2.py"
python "C:\Users\User\Dropbox\Nu micro\scripts\make_labX_report.py"
python "C:\Users\User\Dropbox\Nu micro\scripts\make_labX_guide.py"
```

Always run in PowerShell (not Bash). Always set `$env:PYTHONIOENCODING="utf-8"` first — Windows default encoding (cp1252) chokes on Unicode arrows and Greek letters in print statements.

Check for `Done ->` confirmation line before declaring done. If no confirmation, there was a silent error — run again with error capture.

---

## Phone + PC Setup — Remote Control Workflow

### What "Claude Code on phone" actually is

The Claude mobile app (iOS/Android) is **not** a code execution environment. It is a **remote control interface** for a Claude Code session running on your PC.

- Phone: sends messages, monitors progress, gets push notifications
- PC: executes all Python scripts, writes files, runs git — the actual work machine
- Dropbox: syncs PDFs from PC to phone automatically
- GitHub repo: syncs scripts, source text, and the MD file — readable on phone via GitHub app or browser

### Full phone → PDF workflow

```
1. Phone: open Claude app → connect to "Micro" Remote Control session
2. Phone: "Make the Ch3 study guide PDF"
3. PC (Remote Control): runs make_ch3_pdf.py from Dropbox\Nu micro\scripts\
4. PC: PDF saved to Dropbox\Nu micro\Ch 3\ folder
5. Dropbox: auto-syncs PDF to phone within seconds
6. Phone: open Dropbox app → read PDF
```

### One-time PC setup (Remote Control auto-start)

Run this once in PowerShell to register the Task Scheduler entry:

```powershell
schtasks /create /tn "ClaudeCode-Micro-RemoteControl" `
  /tr "cmd /c 'claude --remote-control --name Micro'" `
  /sc ONLOGON /ru "%USERNAME%" /f
```

Or start it manually any time before using from phone:
```powershell
claude --remote-control --name "Micro"
```

**Requirements for Remote Control to work:**
- PC must be powered on and internet connected
- Claude Code CLI must be installed on PC (`npm install -g @anthropic-ai/claude-code`)
- The `--remote-control` process must be running
- Phone and PC do NOT need to be on the same network — works over internet

### Repo structure for phone use

```
Dropbox\Nu micro\               ← git repo (github.com/georgie357/nu-micro)
  NU_Micro_Study_Method.md      ← this file — readable on phone via GitHub
  README.md                     ← course schedule, assignments, key dates
  scripts\                      ← all make_*.py scripts (version controlled)
    make_ch1_ch2_pdf_v2.py
    make_ch1_ch2_mc_v2.py
    make_ch7_pdf.py
    make_ch7_mc.py
    make_lab1_report.py
    make_lab1_guide.py
  source_text\                  ← extracted slide + textbook text (version controlled)
    ch1_slides.txt              ← Popa Ch.1 slides verbatim (29 slides)
    ch2_slides.txt              ← Popa Ch.2 slides verbatim (33 slides)
    ch7_slides.txt              ← Popa Ch.7 slides verbatim (49 slides)
    ch1_textbook_raw.txt        ← OpenStax Ch.1 extracted text
    ch2_textbook_raw.txt        ← OpenStax Ch.2 extracted text
    ch7_textbook_raw.txt        ← OpenStax Ch.7 extracted text
  .gitignore                    ← blocks *.pdf *.pptx *.docx from git
  sync.ps1                      ← auto-sync script (runs daily via Task Scheduler)
```

PDFs, pptx, docx → Dropbox only (not in git)
Scripts, source text, MD → git + Dropbox

### What to tell Claude on phone for Q&A

When starting a new chat session on phone, paste this at the start:
> "I'm studying BIO203 Microbiology at National University with Dr. Popa. Answer my questions using the Popa lecture slides first, then expand with the OpenStax textbook. Cite the slide number and OpenStax section. The source material is in the GitHub repo: github.com/georgie357/nu-micro in source_text/"

Then ask questions normally. Claude can read the source_text files from the repo URL.

### What to tell Claude on phone to make a PDF

Via Remote Control session (PC must be on):
> "Make the Ch3 study guide PDF. Use the script at Dropbox\Nu micro\scripts\make_ch3_pdf.py. Save to Dropbox\Nu micro\Ch 3\"

Claude Code on PC will run the script, PDF lands in Dropbox, syncs to phone.

### Adding source text for future chapters

Every time a new chapter is covered, extract its slides and textbook pages and save to `source_text\`:

```powershell
# After extracting chX_slides.txt and chX_textbook_raw.txt to Desktop:
Copy-Item "C:\Users\User\Desktop\chX_slides.txt" "C:\Users\User\Dropbox\Nu micro\source_text\"
Copy-Item "C:\Users\User\Desktop\chX_textbook_raw.txt" "C:\Users\User\Dropbox\Nu micro\source_text\"
# Then commit — sync.ps1 will pick it up, or commit manually:
cd "C:\Users\User\Dropbox\Nu micro"
git add source_text/
git commit -m "Add Ch.X source text"
git push origin master
```
