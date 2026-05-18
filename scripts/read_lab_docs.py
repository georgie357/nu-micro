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

    L.append("HARD RULE: When condensing existing lab reports, NEVER rewrite the")
    L.append("student's words. Only delete, merge, join with light connectors.")
    L.append("No grammar fixes, no synonym swaps, no rephrased citations.")
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


LAB_KEYWORDS = [
    "lab report", "lab 1", "lab 2", "lab 3", "lab 4", "lab 5",
    "lab 6", "lab 7", "lab 8", "lab 9", "lab 10", "lab 11",
    "lab1", "lab2", "lab3", "lab4", "lab5", "lab6", "lab7",
    "bio203", "microbiology lab", "traditional report",
    "condense", "playbook", "popa", "nu micro",
    "serial dilution", "pick and patch", "gram stain",
    "library plate", "antibiotic discovery",
    "streptomyces", "tsa plate", "agar slant",
    "methylene blue", "simple stain", "aseptic technique",
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
