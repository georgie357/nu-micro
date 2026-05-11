# BIO203 Microbiology — Claude Code Session Instructions

This file is read automatically by Claude Code at session start.
It applies to ALL sessions in this folder — PC and Remote Control from phone.

---

## Who is asking

A student in BIO203 Microbiology at National University (Spring 2026).
Professor: Dr. Radu Popa. Textbook: OpenStax Microbiology (free).
Course runs Apr 27 – Jun 20, 2026. Midterm May 24. Final Jun 20.

---

## How to answer every question about course material

**Step 1 — Run the search script first:**
```
python "C:\Users\User\Dropbox\Nu micro\scripts\answer_question.py" "QUESTION" [ch1|ch2|ch7]
```
This searches the actual Popa slide text and OpenStax textbook and prints the matching content.

**Step 2 — Answer in this order, every time:**
1. **Popa slide answer first** — exact wording from the slide, cite slide number (e.g., "Popa Ch.2 slide 26")
2. **Textbook expansion** — add mechanism/depth from OpenStax, cite section (e.g., "OpenStax 2.4")
3. **Flag Popa emphasis** — if he gave a full slide to it, say so — that's exam priority
4. **Concrete example** — real organism, disease, or lab observation from the course
5. **Lab connection** — tie to Lab 1 or Lab 2 if relevant

**Never answer from general knowledge alone.** Always run the search script first so answers reflect what Popa actually put on his slides.

---

## How to make a PDF

Scripts are in: `C:\Users\User\Dropbox\Nu micro\scripts\`
Output goes to: `C:\Users\User\Dropbox\Nu micro\<chapter folder>\`
PDFs sync automatically to phone via Dropbox.

```powershell
$env:PYTHONIOENCODING="utf-8"
python "C:\Users\User\Dropbox\Nu micro\scripts\make_ch1_ch2_pdf_v2.py"
python "C:\Users\User\Dropbox\Nu micro\scripts\make_ch1_ch2_mc_v2.py"
python "C:\Users\User\Dropbox\Nu micro\scripts\make_ch7_pdf.py"
python "C:\Users\User\Dropbox\Nu micro\scripts\make_ch7_mc.py"
python "C:\Users\User\Dropbox\Nu micro\scripts\make_lab1_report.py"
python "C:\Users\User\Dropbox\Nu micro\scripts\make_lab1_guide.py"
```

For new chapters: extract slides + textbook first (see NU_Micro_Study_Method.md Step 0),
save to `source_text/`, then write a new `make_chX_pdf.py` script.

---

## Source material location

```
source_text/
  ch1_slides.txt        — Popa Ch.1 slides verbatim (29 slides)
  ch2_slides.txt        — Popa Ch.2 slides verbatim (33 slides)
  ch7_slides.txt        — Popa Ch.7 slides verbatim (49 slides)
  ch1_textbook_raw.txt  — OpenStax Ch.1 full text
  ch2_textbook_raw.txt  — OpenStax Ch.2 full text
  ch7_textbook_raw.txt  — OpenStax Ch.7 full text
```

Textbook PDF (too large for git): `C:\Users\User\Dropbox\Nu micro\original textbook\microbiology_-_WEB.pdf`

---

## 🛑🛑🛑 HARD RULE — NEVER ALTER OR DELETE THE TEXTBOOK PDF

**`C:\Users\User\Dropbox\Nu micro\original textbook\microbiology_-_WEB.pdf` is read-only forever.**

- ❌ NEVER delete, move, rename, or overwrite this file
- ❌ NEVER run `rm`, `Remove-Item`, `mv`, `Move-Item` on it
- ✅ ALLOWED: read with pdfplumber, extract text to `source_text/`

If the file is missing: STOP. Tell the user. Do not attempt lab reports without it (citations cannot be verified). Restore from openstax.org/details/books/microbiology.

This rule exists because the file went missing during a script-editing session on May 10, 2026.

---

## 🛑 LAB REPORT FORMAT — Popa requirement (May 2026, STRICT v2)

**Every lab needs a TRADITIONAL lab report Word .docx in addition to the D2L docx quiz form.**

Required sections, in order:
1. Title
2. Name
3. Scope
4. Introduction
5. Materials and Methods
6. Results and Discussion
7. Conclusion
8. References

### ⛔⛔⛔ HARD RULE #1 — TEXTBOOK ONLY FOR CITATIONS, CSE NAME-YEAR FORMAT

**ONLY OpenStax Microbiology may be cited.** No Popa slide cites. No Tiny Earth manual cites. No lab handout cites. No Wikipedia, Google, AI, or journal cites — ever.

**Citation style: CSE Name-Year** (gold standard for biology lab reports)

In-text format: `(Parker et al. 2016)` or `(Parker et al. 2016, §2.3)`

Reference list entry (one per textbook, regardless of how many sections are cited):
```
Parker N, Schneegurt M, Tu A-HT, Lister P, Forster BM. 2016. Microbiology.
Houston (TX): OpenStax. Available from:
https://openstax.org/details/books/microbiology
```

### ⛔⛔⛔ HARD RULE #2 — NO EDITORIAL PARAPHRASING

Every factual sentence in Introduction / Discussion / Conclusion must trace directly to a specific OpenStax passage. No invented connectors ("therefore"), no decorative adjectives ("foundational," "primary"), no smoothing transitions that aren't in the source. Procedure description (M&M) and own observations (Results) don't need citations — those are factual narration.

### ⛔⛔⛔ HARD RULE #4 — NO HANDOUT Q&A IN TRADITIONAL REPORTS

The traditional lab report is a science paper, NOT a fill-in-the-handout document. NEVER include numbered "Q1: …", "Q2: …" question-and-answer blocks in the traditional report. Those belong only in the D2L docx quiz form. In the traditional report, the same information is integrated as flowing prose into Materials and Methods, Results and Discussion, etc.

Test for any sentence: would it appear in a published paper, or only on a worksheet? If worksheet → leave it out.

### 📖 READ vs CITE — pipeline distinction

**READ to understand the lab (not cited):** lab .docx handout, Tiny Earth manual, Popa slides, student's data/photos.

**CITE to back factual claims:** OpenStax textbook only.

This is normal scientific practice — read broadly, cite only the authoritative source.

### ⛔⛔⛔ HARD RULE #3 — VERIFY BEFORE CITING

Before adding `(OpenStax 2024, §X.Y)`:
1. Open `source_text/chN_textbook_raw.txt`
2. Search for the claim
3. Confirm it's there in that section before citing

If the claim isn't in the textbook in that exact section, REMOVE the cite or rewrite the claim. Fake citations have already broken Lab 1 once — don't do it again.

See `NU_Micro_Study_Method.md` (TRADITIONAL LAB REPORT FORMAT — STRICT v2 section) for full rules.

---

## Full production rules

See: `C:\Users\User\Dropbox\Nu micro\NU_Micro_Study_Method.md`
Also on GitHub: github.com/georgie357/nu-micro
