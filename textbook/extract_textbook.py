"""
Extraherar textinnehåll från kursbokens PDF till markdown.
Använder PyMuPDF (fitz) för textextraktion med font-baserad koddetektion.

Font-mapping i denna PDF:
  FreeMono = kod (monospace)
  PalatinoLinotype-* / FreeSerif / Helvetica / Arial-* = brödtext
"""
import fitz
import re

PDF_PATH = "Scientific_Computing_with_Python_High-Performance_....pdf"
OUTPUT_PATH = "textbook_content.md"

CODE_FONTS = {"FreeMono"}

# Rader/mönster att hoppa över (sidhuvuden, sidfötter)
SKIP_PATTERNS = [
    "Führer, Claus, et al.",
    "ProQuest Ebook Central",
    "Created from lund on",
    "Copyright © 2021",
]


def is_code_font(font_name):
    return any(cf in font_name for cf in CODE_FONTS)


def is_skip_line(text):
    stripped = text.strip()
    if not stripped:
        return False
    for pat in SKIP_PATTERNS:
        if stripped.startswith(pat):
            return True
    if re.match(r'^\[\s*\d+\s*\]$', stripped):
        return True
    if stripped == "Table of Contents":
        return True
    return False


def extract_page_with_fonts(page):
    """Extrahera text från en sida med font-information.

    Returnerar en lista av (text, is_code) tupler, en per textrad.
    """
    data = page.get_text("dict")
    lines_out = []

    for block in data.get("blocks", []):
        if "lines" not in block:
            continue
        for line in block["lines"]:
            line_text_parts = []
            code_char_count = 0
            total_char_count = 0
            for span in line["spans"]:
                text = span["text"]
                font = span["font"]
                line_text_parts.append(text)
                char_count = len(text.strip())
                total_char_count += char_count
                if is_code_font(font):
                    code_char_count += char_count

            full_text = "".join(line_text_parts)
            if not full_text.strip():
                lines_out.append(("", False))
                continue

            # En rad är "kod" om majoriteten av tecknen har kodfont
            is_code = total_char_count > 0 and (code_char_count / total_char_count) > 0.5
            lines_out.append((full_text, is_code))

    return lines_out


def format_page_as_markdown(lines):
    """Formatera en sidas rader till markdown med fenced code blocks."""
    output = []
    in_code_block = False

    for text, is_code in lines:
        if is_skip_line(text):
            continue

        if is_code and not in_code_block:
            # Starta nytt kodblock
            output.append("```python")
            in_code_block = True
            output.append(text.rstrip())
        elif is_code and in_code_block:
            # Fortsätt kodblock
            output.append(text.rstrip())
        elif not is_code and in_code_block:
            # Avsluta kodblock
            output.append("```")
            in_code_block = False
            output.append(text.rstrip())
        else:
            output.append(text.rstrip())

    # Stäng eventuellt öppet kodblock vid sidslut
    if in_code_block:
        output.append("```")

    return "\n".join(output)


def extract_full_book(pdf_path):
    """Extrahera hela boken med font-medvetenhet."""
    doc = fitz.open(pdf_path)
    skip_pages = set(range(0, 15))  # Sida 0-14 (omslag, copyright, TOC)

    header = """# Scientific Computing with Python (2nd Edition)

> Führer, Solem & Verdier — Packt, 2021
> ISBN 978-1-83882-232-3

---

"""
    all_parts = [header]

    for page_idx in range(len(doc)):
        if page_idx in skip_pages:
            continue

        page = doc[page_idx]
        page_num = page_idx + 1  # 1-indexed

        lines = extract_page_with_fonts(page)
        page_md = format_page_as_markdown(lines)

        if not page_md.strip():
            continue

        all_parts.append(f"\n<!-- PDF page {page_num} -->\n")
        all_parts.append(page_md)

    doc.close()
    return "\n".join(all_parts)


def post_process_markdown(text):
    """Förbättra markdown-formateringen."""

    chapters = {
        1: "Getting Started",
        2: "Variables and Basic Types",
        3: "Container Types",
        4: "Linear Algebra - Arrays",
        5: "Advanced Array Concepts",
        6: "Plotting",
        7: "Functions",
        8: "Classes",
        9: "Iterating",
        10: "Series and Dataframes - Working with Pandas",
        11: "Communication by a Graphical User Interface",
        12: "Error and Exception Handling",
        13: "Namespaces, Scopes, and Modules",
        14: "Input and Output",
        15: "Testing",
        16: "Symbolic Computations - SymPy",
        17: "Interacting with the Operating System",
        18: "Python for Parallel Computing",
        19: "Comprehensive Examples",
    }

    multiline_titles = {
        11: (r'11\nCommunication by a Graphical\nUser Interface',
             '## Chapter 11: Communication by a Graphical User Interface'),
        13: (r'13\nNamespaces, Scopes, and\nModules',
             '## Chapter 13: Namespaces, Scopes, and Modules'),
        16: (r'16\nSymbolic Computations -\nSymPy',
             '## Chapter 16: Symbolic Computations - SymPy'),
        17: (r'17\nInteracting with the Operating\nSystem',
             '## Chapter 17: Interacting with the Operating System'),
        10: (r'10\nSeries and Dataframes -\nWorking with Pandas',
             '## Chapter 10: Series and Dataframes - Working with Pandas'),
        12: (r'12\nError and Exception Handling',
             '## Chapter 12: Error and Exception Handling'),
        18: (r'18\nPython for Parallel Computing',
             '## Chapter 18: Python for Parallel Computing'),
        19: (r'19\nComprehensive Examples',
             '## Chapter 19: Comprehensive Examples'),
    }

    # Multiline kapitelrubriker
    for ch_num, (pattern, replacement) in multiline_titles.items():
        text = re.sub(r'\n' + pattern + r'\n', '\n' + replacement + '\n', text)

    # Singleline kapitelrubriker
    for ch_num, title in chapters.items():
        escaped_title = re.escape(title)
        text = re.sub(
            rf'\n{ch_num}\n{escaped_title}\n',
            f'\n## Chapter {ch_num}: {title}\n',
            text
        )

    # Ta bort upprepade sidhuvuden
    for ch_num, title in chapters.items():
        escaped_title = re.escape(title)
        text = re.sub(rf'\n{escaped_title}\nChapter {ch_num}\n', '\n', text)
        text = re.sub(rf'\nChapter {ch_num}\n{escaped_title}\n', '\n', text)

    # Preface-rubrik
    text = re.sub(r'\nPreface\n', r'\n## Preface\n', text)

    # Underavsnitt först (X.Y.Z)
    text = re.sub(
        r'\n(\d{1,2}\.\d{1,2}\.\d{1,2})\s+([A-Z][^\n]+)\n',
        r'\n#### \1 \2\n',
        text
    )

    # Huvudavsnitt (X.Y)
    text = re.sub(
        r'\n(\d{1,2}\.\d{1,2})\s+([A-Z][^\n]+)\n',
        r'\n### \1 \2\n',
        text
    )

    # Ta bort dubblerade Preface-headers
    text = re.sub(r'\n## Preface\n## Preface\n', '\n## Preface\n', text)

    # Slå ihop konsekutiva kodblock som separeras av bara en sidkommentar
    # ```\n\n<!-- PDF page XX -->\n\n```python  →  ta bort mellanliggande stängning/öppning
    text = re.sub(
        r'```\n+<!-- PDF page \d+ -->\n+```python\n',
        '',
        text
    )

    # Ta bort överflödiga tomma rader (max 2 i rad)
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    return text


def verify(markdown):
    """Verifiera att extraktionen lyckades."""
    print("\nVerifiering:")

    # Kapitel
    for i in range(1, 20):
        if f"Chapter {i}:" in markdown:
            print(f"  ✓ Chapter {i} hittad")
        else:
            print(f"  ✗ Chapter {i} SAKNAS!")

    # Kodblock-balans
    opens = markdown.count("```python")
    closes = markdown.count("```") - opens  # totala ``` minus öppnande
    print(f"\n  Kodblock: {opens} öppnande, {closes} stängande")
    if opens == closes:
        print("  ✓ Kodblock balanserade")
    else:
        print(f"  ✗ Obalanserade kodblock! Diff: {opens - closes}")


def main():
    print(f"Läser PDF: {PDF_PATH}")
    markdown = extract_full_book(PDF_PATH)

    print("Efterbehandlar...")
    markdown = post_process_markdown(markdown)

    lines = markdown.count('\n')
    size_kb = len(markdown.encode('utf-8')) / 1024
    print(f"\nSkriver till: {OUTPUT_PATH}")
    print(f"  {lines} rader, {size_kb:.0f} KB")

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(markdown)

    verify(markdown)


if __name__ == "__main__":
    main()
