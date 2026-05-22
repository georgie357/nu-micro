# -*- coding: utf-8 -*-
"""
read_lab_docs.py
SessionStart / UserPromptSubmit hook for BIO203A lab report work.

Injects the lab report playbook + key references into Claude's context
whenever a session involves lab reports (keyword-triggered for
UserPromptSubmit; always on for SessionStart).

Outputs JSON: {"hookSpecificOutput": {"hookEventName": "...", "additionalContext": "..."}}
"""
import sys
import json
from pathlib import Path

NU_MICRO = Path(r"C:/Users/User/Dropbox/Nu micro")

PLAYBOOK = NU_MICRO / "lab_report_playbook.md"
FORMAT_REF = NU_MICRO / "BIO203_Lab_Report_Format_Reference.pdf"
SYLLABUS = NU_MICRO / "Syllabus Lab micro Popa Bio203A May2026 v03RP.docx"
REPORTS_DIR = NU_MICRO / "lab reports" / "final traditional reports"


def read_file(path: Path, max_chars: int = 8000) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        if len(text) > max_chars:
            return text[:max_chars] + f"\n... [truncated — {len(text):,} chars total] ..."
        return text
    except Exception as e:
        return f"[Could not read {path.name}: {e}]"


def build_context() -> str:
    L = []
    L.append("=" * 70)
    L.append("BIO203A LAB REPORT — SESSION CONTEXT")
    L.append("=" * 70)
    L.append("")
    L.append("Course: BIO203A Microbiology Laboratory (Spring 2026, Dr. Radu Popa)")
    L.append("Author: George Vela")
    L.append("")

    L.append("=" * 70)
    L.append("📁 TEXTBOOK IS LOCAL — USE IT. NEVER INVENT A CITATION.")
    L.append("=" * 70)
    L.append("")
    L.append("Per-chapter plain text files (one Grep call away):")
    L.append("  C:\\Users\\User\\Dropbox\\Nu micro\\source_text\\ch1_textbook_raw.txt")
    L.append("  C:\\Users\\User\\Dropbox\\Nu micro\\source_text\\ch2_textbook_raw.txt")
    L.append("  ... ch1 through ch26 all available")
    L.append("  C:\\Users\\User\\Dropbox\\Nu micro\\source_text\\ch26_textbook_raw.txt")
    L.append("")
    L.append("Full PDF (do NOT delete — see CLAUDE.md):")
    L.append("  C:\\Users\\User\\Dropbox\\Nu micro\\original textbook\\microbiology_-_WEB.pdf")
    L.append("")
    L.append("Companion reference (READ BEFORE WRITING LAB REPORTS):")
    L.append("  C:\\Users\\User\\Dropbox\\Nu micro\\CLAUDE.md")
    L.append("    — contains the 4 strict hard rules from May 10, 2026 onward")
    L.append("")
    L.append("MANDATORY VERIFICATION before writing any (Parker et al. 2016, §X.X):")
    L.append("  1. Identify the chapter (e.g. Kirby-Bauer = ch14)")
    L.append("  2. Grep ch[N]_textbook_raw.txt for the key term")
    L.append("  3. Find the section header (e.g. '14.6 Testing the Effectiveness')")
    L.append("  4. Only then write the §X.X")
    L.append("")
    L.append("If you write a citation without doing this, you are repeating the")
    L.append("May 21, 2026 Lab 9 failure AND the earlier Lab 1 failure. Don't.")
    L.append("")
    L.append("=" * 70)
    L.append("🛑 CRITICAL RULES — READ BEFORE WRITING A SINGLE WORD")
    L.append("=" * 70)
    L.append("")
    L.append("Added May 21, 2026 after Lab 9 incident — multiple failures of trust.")
    L.append("")
    L.append("1. NEVER INVENT CITATIONS. Only Parker et al. 2016 (textbook,")
    L.append("   located in source_text/ — see paths above) and sources literally")
    L.append("   present in the lab manual. NO CLSI, NO journal articles, NO")
    L.append("   'I think this is from...' citations. If you cannot quote the")
    L.append("   source text from source_text/ch[N]_textbook_raw.txt, do not cite it.")
    L.append("")
    L.append("2. READ THE LAB MANUAL END-TO-END FIRST. Extract with pandoc, read")
    L.append("   ALL of it — footnotes, table captions, 'adapted from:' notes,")
    L.append("   Report Instructions. Never assert 'the manual says X' or 'the")
    L.append("   manual does not say X' without a quotation ready to produce.")
    L.append("")
    L.append("3. NEVER FABRICATE MEASUREMENTS. No mm zone sizes from phone photos.")
    L.append("   No invented percentages, CFU, OD. Qualitative descriptions")
    L.append("   (large/moderate/small/none) are OK if labeled qualitative.")
    L.append("")
    L.append("4. LOOK AT PHOTOS BEFORE DESCRIBING THEM. When student says 'look")
    L.append("   again' or 'you missed X,' re-read the image — do not defend the")
    L.append("   original description.")
    L.append("")
    L.append("5. ASK BEFORE DELETING REQUIRED CONTENT. If student questions")
    L.append("   whether X is needed, point them at the manual's requirement and")
    L.append("   ASK. The lab manual is the source of truth for what is required.")
    L.append("")
    L.append("6. EDIT CONSISTENTLY. Table + figure caption + Scope + Results +")
    L.append("   Discussion + Conclusion + References — all in ONE pass. No")
    L.append("   inconsistent edits where table says one thing and text says")
    L.append("   another.")
    L.append("")
    L.append("7. STUDENT'S VOICE IS LAW. When condensing finished writing, never")
    L.append("   rewrite — only delete, merge with light connectors, fix")
    L.append("   meaning-changing typos. No grammar fixes, no synonyms, no")
    L.append("   rephrased citations.")
    L.append("")
    L.append("=" * 70)
    L.append("")

    # List existing final reports
    if REPORTS_DIR.exists():
        L.append(f"Existing final reports in {REPORTS_DIR}:")
        for p in sorted(REPORTS_DIR.glob("*.docx")):
            try:
                size = p.stat().st_size
                L.append(f"  {p.name}  ({size:,} bytes)")
            except Exception:
                L.append(f"  {p.name}")
        L.append("")

    # Load the playbook
    L.append("=" * 70)
    L.append("PLAYBOOK — lab_report_playbook.md  (full content below)")
    L.append("=" * 70)
    if PLAYBOOK.exists():
        L.append(read_file(PLAYBOOK, max_chars=20000))
    else:
        L.append("[Playbook not found at " + str(PLAYBOOK) + "]")
    L.append("")

    L.append("=" * 70)
    L.append("REFERENCE FILES (read with Read tool on demand)")
    L.append("=" * 70)
    L.append(f"  Playbook .md  : {PLAYBOOK}")
    L.append(f"  Playbook .pdf : {PLAYBOOK.with_suffix('.pdf')}")
    L.append(f"  Format ref    : {FORMAT_REF}")
    L.append(f"  Syllabus      : {SYLLABUS}")
    L.append(f"  Final reports : {REPORTS_DIR}")
    L.append("")
    L.append("=" * 70)
    L.append("END")
    L.append("=" * 70)
    return "\n".join(L)


# Strictly lab-report-specific keywords ONLY.
# Do NOT add: "bio203", "popa", "nu micro", "gram stain", "streptomyces",
# or any organism/technique name — those overlap with quiz/exam work,
# which uses BIO203_Quiz_Lessons.md, a separate workflow.
LAB_KEYWORDS = [
    "lab report",
    "lab 1 ", "lab 2 ", "lab 3 ", "lab 4 ", "lab 5 ",
    "lab 6 ", "lab 7 ", "lab 8 ", "lab 9 ", "lab 10 ", "lab 11 ", "lab 12 ",
    "lab1 ", "lab2 ", "lab3 ", "lab4 ", "lab5 ", "lab6 ", "lab7 ",
    "lab8 ", "lab9 ", "lab10 ", "lab11 ", "lab12 ",
    "traditional report",
    "condense the report", "condense lab",
    "lab report playbook", "lab_report_playbook",
    "lab.docx",
]


def main():
    event_name = sys.argv[1] if len(sys.argv) > 1 else "SessionStart"

    if event_name == "UserPromptSubmit":
        prompt = ""
        try:
            stdin_raw = sys.stdin.buffer.read().decode("utf-8-sig").strip()
            stdin_data = json.loads(stdin_raw)
            prompt = stdin_data.get("prompt", "").lower()
        except Exception:
            prompt = ""

        if not any(kw in prompt for kw in LAB_KEYWORDS):
            print(json.dumps({"continue": True}))
            return

    context = build_context()
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": event_name,
            "additionalContext": context
        }
    }))


if __name__ == "__main__":
    main()
