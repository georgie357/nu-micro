# answer_question.py
# Called by Claude Code Remote Control when answering a microbiology question from phone.
# Searches source_text/ files for relevant content and prints it so Claude can answer.
#
# Usage: python answer_question.py "your question here" [chapter]
# Example: python answer_question.py "what is the gram stain" ch2
# Example: python answer_question.py "what is peptidoglycan"   (searches all)

import sys
import os
import re

SOURCE_DIR = r"C:\Users\User\Dropbox\Nu micro\source_text"

# Map chapter keywords to file pairs [slides, textbook]
CHAPTER_FILES = {
    "ch1": ["ch1_slides.txt", "ch1_textbook_raw.txt"],
    "ch2": ["ch2_slides.txt", "ch2_textbook_raw.txt"],
    "ch7": ["ch7_slides.txt", "ch7_textbook_raw.txt"],
}

def load_file(filename):
    path = os.path.join(SOURCE_DIR, filename)
    if not os.path.exists(path):
        return f"[File not found: {filename}]"
    with open(path, encoding="utf-8") as f:
        return f.read()

def search_content(text, keywords, context_lines=4):
    """Return matching chunks from text for given keywords."""
    lines = text.split("\n")
    results = []
    found_indices = set()

    for kw in keywords:
        kw_lower = kw.lower()
        for i, line in enumerate(lines):
            if kw_lower in line.lower() and i not in found_indices:
                start = max(0, i - 1)
                end = min(len(lines), i + context_lines)
                chunk = "\n".join(lines[start:end]).strip()
                if chunk:
                    results.append(chunk)
                    found_indices.update(range(start, end))

    return results

def main():
    if len(sys.argv) < 2:
        print("Usage: python answer_question.py 'question' [ch1|ch2|ch7]")
        sys.exit(1)

    question = sys.argv[1]
    chapter_hint = sys.argv[2].lower() if len(sys.argv) > 2 else None

    # Extract keywords (words > 3 chars, skip common words)
    stopwords = {"what", "when", "where", "which", "does", "that", "this",
                 "with", "from", "have", "they", "their", "there", "than",
                 "explain", "describe", "define", "compare", "why", "how",
                 "the", "and", "for", "are", "was", "were", "will"}
    words = re.findall(r"[a-zA-Z]{3,}", question.lower())
    keywords = [w for w in words if w not in stopwords]

    if not keywords:
        keywords = words  # fallback: use all words

    # Determine which files to search
    if chapter_hint and chapter_hint in CHAPTER_FILES:
        file_pairs = {chapter_hint: CHAPTER_FILES[chapter_hint]}
    else:
        file_pairs = CHAPTER_FILES

    print("=" * 70)
    print(f"QUESTION: {question}")
    print(f"KEYWORDS: {', '.join(keywords)}")
    print("=" * 70)

    any_results = False

    for ch, files in file_pairs.items():
        slides_file, textbook_file = files

        # --- SLIDES FIRST (Popa emphasis) ---
        slides_text = load_file(slides_file)
        slide_hits = search_content(slides_text, keywords, context_lines=5)

        if slide_hits:
            any_results = True
            print(f"\n{'='*70}")
            print(f"POPA SLIDES — {slides_file}")
            print(f"{'='*70}")
            for hit in slide_hits[:8]:  # cap at 8 chunks
                print(hit)
                print("---")

        # --- TEXTBOOK EXPANSION ---
        textbook_text = load_file(textbook_file)
        textbook_hits = search_content(textbook_text, keywords, context_lines=6)

        if textbook_hits:
            any_results = True
            print(f"\n{'='*70}")
            print(f"OPENSTACK TEXTBOOK — {textbook_file}")
            print(f"{'='*70}")
            for hit in textbook_hits[:6]:  # cap at 6 chunks
                print(hit)
                print("---")

    if not any_results:
        print(f"\nNo matches found for keywords: {', '.join(keywords)}")
        print("Try rephrasing or specify a chapter: ch1, ch2, or ch7")

    print("\n" + "=" * 70)
    print("ANSWER PROTOCOL: Lead with Popa slide content above.")
    print("Expand with textbook. Cite slide numbers and OpenStax sections.")
    print("Give a concrete example. Connect to lab if relevant.")
    print("=" * 70)

if __name__ == "__main__":
    main()
