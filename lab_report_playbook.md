# BIO203A Lab Report Playbook
**Course:** BIO203A Microbiology Laboratory (Spring 2026, Dr. Radu Popa)
**Author:** George Vela
**Purpose:** How to write and condense traditional lab reports to fit 2 pages while keeping the student's own voice.

---

## 📁 TEXTBOOK LOCATION — READ BEFORE WRITING ANY CITATION

**The textbook is local. There is no excuse for inventing citations.**

### Per-chapter plain text (use these to verify claims):
```
C:\Users\User\Dropbox\Nu micro\source_text\ch1_textbook_raw.txt
C:\Users\User\Dropbox\Nu micro\source_text\ch2_textbook_raw.txt
... (all 26 chapters available)
C:\Users\User\Dropbox\Nu micro\source_text\ch26_textbook_raw.txt
```

### Full PDF (read-only, never delete):
```
C:\Users\User\Dropbox\Nu micro\original textbook\microbiology_-_WEB.pdf
```

### Chapter page-number map:
```
C:\Users\User\Dropbox\Nu micro\source_text\chapter_map.json
```

### Verification procedure (mandatory before adding ANY `(Parker et al. 2016, §X.X)` citation):
1. Identify which chapter the topic is in (Lab 9 antibiotic susceptibility → Chapter 14)
2. Open `source_text/ch[N]_textbook_raw.txt` (e.g. `ch14_textbook_raw.txt`)
3. Use Grep on key terms from the student's sentence (e.g. "Kirby-Bauer", "Mueller-Hinton", "MIC")
4. Find the section header (e.g. `14.6 Testing the Effectiveness of Antimicrobials`) where the content lives
5. ONLY THEN write the §X.X citation

### Companion reference docs in this folder:
- `CLAUDE.md` — full production rules including 4 hard rules for traditional reports
- `NU_Micro_Study_Method.md` — extended study and report-writing procedures
- `BIO203_Quiz_Lessons.md` — separate; do NOT read during lab report work

---

## 🛑 HARD RULES — IN PRIORITY ORDER

### 🛑 RULE −2 — NEVER INVENT CITATIONS (added May 21, 2026)

**Every citation in the report must come from a source that is physically open in the conversation.** No exceptions.

- The textbook (Parker et al. 2016, OpenStax Microbiology) is allowed by default.
- Anything else must be present in either (a) the lab manual the student dropped into the chat, or (b) a source the student explicitly named.
- If a fact "feels like it should have a citation," that is **not** permission to add one. Either find the source in the manual/textbook or do not make the claim.

**What happened (Lab 9, May 21, 2026):** Added "CLSI 2020 Performance Standards" to references list on the very first build. The breakpoint values came from the lab manual's Table 1, but I attributed them to CLSI from training memory before ever reading the manual carefully. The user spent multiple rounds catching and removing this fake citation. **Second offense — Lab 1 was broken by fake citations earlier in the semester, and `CLAUDE.md` in `C:\Users\User\Dropbox\Nu micro\` already had this rule. The reason I missed it: my session working directory was elsewhere, so the auto-loaded `CLAUDE.md` was a different file. The textbook locations were never re-stated in `lab_report_playbook.md` or in the lab hook injection. That is now fixed.**

**Specific guards:**
1. Before adding ANY non-Parker citation, paste the exact source text from the manual/file proving it's required.
2. Never write "(Parker et al. 2016, §X.X)" for a fact unless you can name §X.X content from the actual textbook section.
3. Never name a section number unless verified.

### 🛑 RULE −1 — READ THE LAB MANUAL END-TO-END BEFORE WRITING ANY WORD (added May 21, 2026)

**When the student drops a lab manual into the chat, extract it with pandoc and read all of it — including footnotes, table captions, "Adapted from:" notes, and Report instructions.** Then write the report.

- Do NOT start drafting until you have read the entire manual at least once.
- After drafting, before delivering, do a SECOND read targeted at: required sections, required table columns, required questions to answer, citation sources mentioned in footnotes.
- If you make a claim about "what the lab guide says" or "what the lab guide doesn't say," that claim must be backed by a quotation you can produce on demand.

**What happened (Lab 9):** I asserted "the lab guide doesn't cite CLSI" when the manual literally says "(Table 1 is adapted from: Clinical and Laboratory Standards Institute (CLSI). Performance Standards for Antimicrobial Susceptibility Testing. 30th ed. 2020.)" — text I had already extracted earlier. I asserted a negative I had not verified.

### 🛑 RULE −0.5 — NEVER FABRICATE MEASUREMENTS (added May 21, 2026)

**If the student does not have measurements, do not invent them.** Specifically:

- Do NOT produce zone sizes in mm from a phone photo of a plate. Phones are not calipers.
- Do NOT produce specific percentages, OD values, CFU counts, or any other numeric measurement without source data.
- Qualitative descriptions (large/moderate/small/none) are acceptable AS LONG AS you say they are qualitative.
- If the student has actual data, use exactly what they provide. Do not "interpret" their numbers into different numbers.

**What happened (Lab 9):** First draft contained "AM ~30 mm, TE ~33 mm, N ~34 mm, P ~22 mm" for B. subtilis and "AM ~15, TE ~14, N ~9, P ~13" for C. sporogenes. These numbers were eyeballed from a phone photo at an angle. The student pushed back; we replaced with qualitative scheme.

### 🛑 RULE −0.25 — LOOK AT THE PHOTO BEFORE WRITING ABOUT THE PHOTO (added May 21, 2026)

**Read every image the student provides with the Read tool, look carefully, and only then describe.** When the student says you misread an image, look again before defending the original description.

**What happened (Lab 9):** Looked at C. sporogenes plate, concluded "no lawn, test failed." Student had to say "definitely measurable. there is lawn. maybe you are looking at wrong image." There was a clear textured lawn with visible zones around all four disks.

### 🛑 RULE −0.1 — ASK BEFORE DELETING REQUIRED CONTENT (added May 21, 2026)

**If the student asks "why do we need X in the table/report," do not delete X. Ask whether they want it removed or want consistency restored.**

The lab manual is the source of truth for "what is required." If X is in the manual's Table 2 / Report Instructions / required-questions list, X stays. If the student is questioning whether it's needed, point them at the manual's requirement and ask.

**What happened (Lab 9):** Student said "we are not using sir anymore, why do we need it in the table" — pointing out a text/table inconsistency. I deleted S/I/R from both, then student pointed out the lab manual's Table 1 has Resistant/Intermediate/Susceptible columns and S/I/R is REQUIRED in the report. Should have asked, not deleted.

### 🛑 RULE −0.05 — EDIT CONSISTENTLY: TABLE + TEXT + REFERENCES TOGETHER (added May 21, 2026)

**When removing or changing a concept, edit every location of that concept in one pass.** Table cells, figure captions, results text, discussion text, conclusion, references list — all in one go.

**What happened (Lab 9):** Removed CLSI from text but left in references list. Removed S/I/R from table but left in text. Each round of inconsistent edits cost the student trust.

**Checklist before delivering any edit:**
- [ ] Table cells updated
- [ ] Figure caption updated
- [ ] All references to the concept in Results updated
- [ ] All references to the concept in Discussion updated
- [ ] All references to the concept in Conclusion updated
- [ ] References list entry added/removed
- [ ] Scope updated if relevant

### 🛑 RULE 0 — CHECK LINE SPACING FIRST (added May 17, 2026)

**Before ANY text condensing, fix line spacing.** A doc set to double-spacing (`line="480"`) at 950 words will print as **5 pages**, not 2. At single (`line="240"`) the same content fits in 2 pages.

**Two places to fix:**
1. `unpacked/word/styles.xml` — `<w:spacing w:line="480"/>` in `<w:docDefaults>`
2. `unpacked/word/document.xml` — per-paragraph `<w:spacing w:line="480"/>` overrides (these override styles.xml!)

Both must be set to `240` (single) or `276` (1.15×). Single-line search/replace `w:line="480"` → `w:line="240"` across both files.

**This was the single biggest cause of "report won't fit on 2 pages" in Labs 2–6.** Do this first; everything else is secondary.

### 🛑 RULE 1 — COLLAPSE TITLE BLOCK TO 2 LINES

Word docs often have ~10–14 paragraphs of title-block padding (4 empty paragraphs at top + centered name/course/date each on its own line + more empty paragraphs). At any spacing this eats half a page.

**Collapse to 2 lines:**
1. **Bold combined title:** `Lab N: [topic] — [subtitle]` (Times New Roman, 14pt, bold, centered)
2. **Compact byline:** `George Vela | BIO203A — Microbiology Laboratory | Instructor: Dr. Radu Popa | [date(s)]` (centered, normal weight)

Then **immediately** the "Scope" header — no empty paragraph buffer of more than 1 line.

This typically saves ~1 full page on its own.

### 🛑 RULE 2 — STRUCTURAL CONTENT TO PARAGRAPHS

Convert these to flowing paragraphs (NOT bulleted lists or tables):
- **Materials list:** 10 bullet items become 1 paragraph with `;` separators
- **Result tables:** Multi-row data table becomes 1 paragraph with `Patch 1 — …; Patch 2 — …` format
- **Calculation blocks:** Indented multi-line equations become 1 dense paragraph with `=` and `;` connectors

A 6-row table at default Word row height = ~3 inches. As a paragraph it's ~0.6 inches. **5× compression** per table.

### 🛑 RULE 3 — SHRINK IMAGES TO ≤ 3.2" WIDE

Default Word image insertion is ~4.5–6.5 inches wide and 3–6 inches tall. Each image at default size eats half a page or more.

**Target: ≤ 3.2 inches wide.** Maintain aspect ratio. EMU value to use for cx: `2926080` (= 3.2 × 914400).

In XML: edit both `<wp:extent cx="..." cy="..."/>` AND `<a:ext cx="..." cy="..."/>` (drawing has two extent attributes).

### 🛑 RULE 4 — STUDENT'S VOICE IS LAW (when text-condensing)

When condensing a finished draft, **never rewrite the student's wording**. Only:
- Delete non-essential sentences
- Merge adjacent sentences with light connectors (`and`, `while`, `then`, `—`)
- Fix obvious typos that change meaning (e.g. `Subtitles` → `subtilis`, `ecoli` → `E. coli`)
- Combine fragmented paragraphs by removing line breaks

**Do NOT:**
- Reword for "better" grammar
- Change scientific terminology
- Substitute synonyms
- Rephrase citations — keep `(Parker et al. 2016, §X.X)` verbatim

---

## Standard Report Structure (every lab)

| Section | Length target | Notes |
|---|---|---|
| Title block | 6–8 lines | Lab N + subtitle / Name / Course / Date / Instructor / Dates |
| **Scope** | 2–3 sentences | What we did + why |
| **Introduction** | 2 paragraphs max | Background + theory + key citations |
| **Materials** | Bullet list | Keep tight, one item per line |
| **Methods** | 2–3 short paragraphs | Procedure only — drop carrying, cord wrap, over-flaming |
| **Results and Discussion** | 1–2 paragraphs + figures/tables | What was observed |
| **Figure/Table captions** | 1–2 sentences each | What it shows + date |
| **Interpretation** (optional) | 1 short paragraph | New insights only — don't repeat Intro/Results |
| **Conclusion** | 3–5 sentences | Objective met + main result + significance |
| **References** | 1 line | Parker et al. 2016 (OpenStax Microbiology) |

---

## Word-Count Targets (body text only)

| Configuration | Target | Notes |
|---|---|---|
| Plain text only | ≤ 1100 words | Easiest to fit |
| With 1 figure | ≤ 950 words | Lab 1 fit at 944 words |
| With 1 table | ≤ 950 words | Tables take ~3" vertical |
| With table **and** figure | ≤ 800 words | Tight — be ruthless in Intro/Discussion |

Page setup: US Letter (8.5×11), 1" margins, 12pt, **1.15× line spacing** (NOT 2.0× / double-spaced — that doubles the page count).

**⚠️ CHECK FIRST when condensing:** Open `unpacked/word/styles.xml` and look at `<w:spacing w:line="X" />`. If `X=480` the doc is double-spaced — change to `X=276` (1.15×) before anything else. Lab 1 was at 276 and fit 2 pages; Labs 2–6 came in at 480 and were spilling to 5 pages until this was fixed (May 17, 2026).

---

## What to Cut FIRST (priority order)

1. **Redundancy across sections** — Discussion sentences that just repeat Introduction or Results. (Pick ONE place to say each thing.)
2. **Conclusion sentences that repeat Discussion** — Conclusion ≠ summary of summary.
3. **Procedural over-detail** — carrying the microscope, wrapping the cord, flame-flame-flame, "we re-racked the tube"
4. **Stacked empty paragraphs** — Word docs often have 3–5 blank paragraphs between sections. Keep one.
5. **Self-evident sentences** — "These measurements enabled the calculations" / "Next we did the next step"
6. **Repeated citation phrases** — `(Parker et al. 2016, §2.3)` on every sentence in a row → keep once at the end of the paragraph
7. **Hedge sentences** — "However to be sure we would have to do further experiments" can compress to "Definitive identification would require more than [X]."

---

## Common Errors Found in Labs 1–6 (watch for these)

- Typos that need fixing during condense: `dohnut`, `ahtough`, `Subtitles` (→ subtilis), `ecoli` (→ E. coli), `microscop` (→ microscope), `Epidermedis` (→ epidermidis)
- Missing space before section header: `simple-staining.Introduction` / `Materials and Methods`
- Duplicated phrase typed twice: `diversity of colonies. diversity of colonies.`
- "Conclusion" header accidentally merged into the previous paragraph
- Section bleed: Intro paragraph 3 reads like Methods, or Discussion paragraph reads like Intro

---

## Pre-Submit Checklist (use before every report)

- [ ] Scope ≤ 3 sentences
- [ ] Introduction is 2 paragraphs, every citation has a `§X.X` reference
- [ ] Methods don't include carrying the scope, wrapping cords, or over-detailed flame steps
- [ ] Results lists actual observations + at least one citation back to Parker for theoretical context
- [ ] Discussion (or "Interpretation") adds insights NOT already in Results or Intro
- [ ] Conclusion: 4–5 sentences (objective met + main result + significance for Antibiotic Discovery Project)
- [ ] No section text bleeding into next section header line
- [ ] Body word count under target for this lab's table/figure config
- [ ] All `Parker et al. 2016, §X.X` citations present
- [ ] Typos fixed (run a quick visual scan for the common ones above)

---

## How Claude Condenses a Report (technical procedure)

When asked to condense a `.docx` lab report, do these steps **in order**. The first 4 are structural/cosmetic and produce the biggest page savings — text condensing is last.

1. **Unpack:**
   ```
   python scripts/office/unpack.py "lab.docx" unpacked_labN/
   ```

2. **[RULE 0] Fix line spacing.** Search `unpacked_labN/word/styles.xml` AND `unpacked_labN/word/document.xml` for `w:line="480"` (double-spacing). Replace with `w:line="240"` (single). Without this step the report will be 5 pages no matter what.

3. **[RULE 1] Collapse the title block.** ~10–14 paragraphs of title padding → 2 paragraphs (bold combined title, then byline). Delete all empty padding paragraphs before "Scope".

4. **[RULE 2] Convert structural content to paragraphs:**
   - Materials bullet list → 1 paragraph (semicolons between items, remove `<w:numPr>`)
   - Tables (`<w:tbl>`) → 1 paragraph (build prose summary, then `parent.remove(tbl)`)
   - Calculation blocks → 1 paragraph (dense with `=` and `;`)

5. **[RULE 3] Shrink images.** Find every `<wp:extent>` and `<a:ext>` with `cx > 2926080`. Scale to `cx="2926080"` (3.2") and `cy` proportionally. Both extent tags must be updated together.

6. **[RULE 4] Text condense** (only after 0–3). Read `unpacked_labN/word/document.xml`, identify cut targets per the cut-priority order, and apply edits via Python script that matches paragraphs by their joined text content (because Word splits text into multiple `<w:r>` runs, raw find/replace on the XML often fails):
   ```python
   # Match paragraph by normalized text, replace all runs with a single run
   if norm(para_text(p)) == norm(find_str):
       replace_para_text(p, new_text)
   ```

7. **Pack back:**
   ```
   python scripts/office/pack.py unpacked_labN/ lab.docx --original lab.docx --validate false
   ```
   Use `--validate false` on Windows — the validator's `→` print throws cp1252 errors.

8. **Word count & paragraph count check:**
   ```python
   for t in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
       if t.text: total += t.text + ' '
   print(f'{len(total.split())} words, {len(list(tree.iter(W("p"))))} paragraphs')
   ```
   Targets after compaction:
   - Paragraphs: < 40 (was 60–94 before)
   - Words: see word-count table above

9. **Tell the user** to open in Word Online or Google Docs (drag .docx into drive.google.com) — WordPad does NOT show page breaks and will look like one long page.

## Reusable scripts (in `C:\Users\User\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\.../docx/`)

- `compact_labs_3to6.py` — title-block + materials + table + image-shrink pipeline; adapt the `LAB_CONFIG` dict for each new lab
- `apply_edits2.py` — paragraph-level text edits (find/replace by paragraph text content, not raw XML)

Pattern for a new lab (Lab 7+):
1. Unpack lab7.docx
2. Fill in `LAB_CONFIG[7]` with title strings, combined title, byline, materials, table data (if any)
3. Run the script
4. Pack back
5. Verify in Google Docs

---

## What's Left This Semester (Labs 7+)

Based on the syllabus pattern, upcoming labs likely include:
- Acid-Fast / Endospore staining
- Streak-plate isolation
- Selective/differential media
- Antibiotic susceptibility testing (Kirby-Bauer)
- Antibiotic Discovery Project (uses the library plate from Lab 3)
- Possibly: UV mutagenesis, biochemical tests, identification keys

Each follow-up report can reuse the same structure. The **Antibiotic Discovery Project** thread runs through the back half of the semester — make sure each related lab's Discussion / Conclusion refers back to it ("This patch will be useful for the antibiotic-screening portion…").

---

## Citations Style Sheet

- Always: `Parker N, Schneegurt M, Tu A-HT, Lister P, Forster BM. 2016. Microbiology. Houston (TX): OpenStax. Available from: https://openstax.org/details/books/microbiology`
- In-text: `(Parker et al. 2016, §X.X)`
- Verified sections (cross-checked against `source_text/chN_textbook_raw.txt` on May 21, 2026):
  - §1.3 — microbe sizes
  - §2.3 — light microscopy
  - §2.4 — staining (basic/acidic dyes, Gram, differential)
  - §3.3 — cell shapes & arrangements
  - §4.1 — Prokaryote Habitats, Relationships, and Microbiomes (soil microbiota diversity)
  - §4.2 — Proteobacteria (E. coli, P. aeruginosa, Pseudomonas pigments)
  - §4.4 — Gram-Positive Bacteria (S. aureus, S. epidermidis, Bacillus, Streptomyces)
  - §7.5 — Using Biochemistry to Identify Microorganisms (pyocyanin/pyoverdin yellow-green pigments on cetrimide agar)
  - §9.2 — Oxygen Requirements for Microbial Growth (obligate anaerobes, facultative)
  - §9.6 — Media Used for Bacterial Growth (selective, differential, MSA, MacConkey, phenol red, neutral red, bile salts)
  - §13.1 — aseptic technique
  - §13.2 — flaming the loop
  - §14.1 — History of Chemotherapy and Antimicrobial Discovery (Fleming, Florey, Chain, Waksman)
  - §14.2 — Fundamentals of Antimicrobial Chemotherapy (bacteriostatic vs bactericidal)
  - §14.3 — Mechanisms of Antibacterial Drugs (β-lactams, aminoglycosides like neomycin, tetracyclines)
  - §14.5 — Drug Resistance (β-lactamases, ESKAPE pathogens)
  - §14.6 — Testing the Effectiveness of Antimicrobials (Kirby-Bauer, MIC, Mueller-Hinton)
  - §14.7 — Current Strategies for Antimicrobial Discovery
  - §21.2 — Bacterial Infections of the Skin and Eyes (pyocyanin and pyoverdin as siderophores)

**Previous WRONG entries (do not reuse):**
- ~~§9.1 — CFU / viable plate count / serial dilution~~ (§9.1 is actually "How Microbes Grow", general metabolism — selective/differential media live in §9.6, NOT §9.1)
- ~~§14.1 — for anything Kirby-Bauer related~~ (§14.1 is discovery history; Kirby-Bauer is §14.6)

---

## File Locations

- Final reports: `C:\Users\User\Dropbox\Nu micro\lab reports\final traditional reports\`
- This playbook: `C:\Users\User\Dropbox\Nu micro\lab_report_playbook.md`
- Format reference PDF: `C:\Users\User\Dropbox\Nu micro\BIO203_Lab_Report_Format_Reference.pdf`
- Quiz lessons (separate file, separate workflow): `BIO203_Quiz_Lessons.md`
- Syllabus: `Syllabus Lab micro Popa Bio203A May2026 v03RP.docx`
