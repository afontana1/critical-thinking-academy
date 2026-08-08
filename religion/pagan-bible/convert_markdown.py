import argparse
import sys
from html import escape
from html.parser import HTMLParser
from pathlib import Path

try:
    import markdown
except ImportError:  # pragma: no cover - runtime dependency check
    print("Missing dependency: python-markdown. Install with `pip install markdown`.", file=sys.stderr)
    raise


HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}


class HeadingCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_heading = None
        self.heading_text = []
        self.heading_id = None
        self.in_categories = False
        self.entries = []

    def handle_starttag(self, tag, attrs):
        if tag in HEADING_TAGS:
            self.in_heading = tag
            self.heading_text = []
            self.heading_id = None
            for key, value in attrs:
                if key == "id":
                    self.heading_id = value

    def handle_data(self, data):
        if self.in_heading:
            self.heading_text.append(data)

    def handle_endtag(self, tag):
        if self.in_heading == tag:
            text = "".join(self.heading_text).strip()
            if tag == "h1" and text == "The Categories":
                self.in_categories = True
            elif tag == "h1" and self.in_categories:
                self.in_categories = False
            elif self.in_categories and tag in HEADING_TAGS and tag != "h1":
                if self.heading_id:
                    level = int(tag[1])
                    self.entries.append((level, text, self.heading_id))
            self.in_heading = None
            self.heading_text = []
            self.heading_id = None


class TocInserter(HTMLParser):
    def __init__(self, toc_html):
        super().__init__()
        self.toc_html = toc_html
        self.out = []
        self.in_heading = None
        self.heading_text = []
        self.toc_inserted = False

    def handle_starttag(self, tag, attrs):
        self.out.append(f"<{tag}{self._format_attrs(attrs)}>")
        if tag in HEADING_TAGS:
            self.in_heading = tag
            self.heading_text = []

    def handle_endtag(self, tag):
        self.out.append(f"</{tag}>")
        if self.in_heading == tag:
            text = "".join(self.heading_text).strip()
            if tag == "h1" and text == "The Categories" and self.toc_html and not self.toc_inserted:
                self.out.append(self.toc_html)
                self.toc_inserted = True
            self.in_heading = None
            self.heading_text = []

    def handle_data(self, data):
        self.out.append(data)
        if self.in_heading:
            self.heading_text.append(data)

    def handle_entityref(self, name):
        self.out.append(f"&{name};")
        if self.in_heading:
            self.heading_text.append(f"&{name};")

    def handle_charref(self, name):
        self.out.append(f"&#{name};")
        if self.in_heading:
            self.heading_text.append(f"&#{name};")

    def handle_startendtag(self, tag, attrs):
        self.out.append(f"<{tag}{self._format_attrs(attrs)} />")

    def _format_attrs(self, attrs):
        if not attrs:
            return ""
        parts = []
        for key, value in attrs:
            if value is None:
                parts.append(f" {key}")
            else:
                parts.append(f' {key}="{escape(value, quote=True)}"')
        return "".join(parts)


def build_toc(entries):
    if not entries:
        return ""
    lines = ["<nav class=\"toc\">", "<h2>Contents</h2>", "<ul>"]
    for level, text, anchor_id in entries:
        lines.append(
            f"<li data-level=\"{level}\"><a href=\"#{escape(anchor_id, quote=True)}\">"
            f"{escape(text)}</a></li>"
        )
    lines.append("</ul></nav>")
    return "\n".join(lines)


def extract_title(markdown_text, fallback):
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip() or fallback
    return fallback


def convert_file(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    md = markdown.Markdown(extensions=["toc"])
    body_html = md.convert(text)

    collector = HeadingCollector()
    collector.feed(body_html)
    toc_html = build_toc(collector.entries)

    inserter = TocInserter(toc_html)
    inserter.feed(body_html)
    body_with_toc = "".join(inserter.out)

    title = extract_title(text, path.stem)
    doc = "\n".join(
        [
            "<!doctype html>",
            "<html lang=\"en\">",
            "<head>",
            "<meta charset=\"utf-8\">",
            f"<title>{escape(title)}</title>",
            "</head>",
            "<body>",
            body_with_toc,
            "</body>",
            "</html>",
        ]
    )
    output_path = path.with_suffix(".html")
    output_path.write_text(doc, encoding="utf-8")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Convert markdown files in a directory to HTML.")
    parser.add_argument(
        "--input-dir",
        default=".",
        help="Directory to scan for markdown files (default: current directory).",
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    md_files = sorted(input_dir.glob("*.md"))
    if not md_files:
        print(f"No markdown files found in {input_dir.resolve()}", file=sys.stderr)
        return 1

    for md_path in md_files:
        output_path = convert_file(md_path)
        print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
