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

Textbook PDF (too large for git): `C:\Users\User\Dropbox\Nu micro\microbiology_-_WEB.pdf`

---

## Full production rules

See: `C:\Users\User\Dropbox\Nu micro\NU_Micro_Study_Method.md`
Also on GitHub: github.com/georgie357/nu-micro
