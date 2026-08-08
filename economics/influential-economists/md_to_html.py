#!/usr/bin/env python
from __future__ import annotations

import re
import sys
from pathlib import Path


def extract_title(markdown_text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown_text, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()
    return fallback


def build_html_doc(title: str, body_html: str) -> str:
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    :root {{
      color-scheme: light;
    }}
    body {{
      font-family: Georgia, "Times New Roman", serif;
      line-height: 1.6;
      margin: 2.5rem auto;
      max-width: 800px;
      padding: 0 1.5rem;
      color: #1f1f1f;
      background: #fbfbf9;
    }}
    h1, h2, h3 {{
      font-family: "Palatino Linotype", Palatino, serif;
      letter-spacing: 0.2px;
    }}
    h1 {{
      margin-bottom: 0.25rem;
    }}
    hr {{
      border: none;
      border-top: 1px solid #d6d6d0;
      margin: 2rem 0;
    }}
    blockquote {{
      margin: 1.5rem 0;
      padding-left: 1rem;
      border-left: 3px solid #c2c2bb;
      color: #3c3c3c;
    }}
    code, pre {{
      font-family: "Courier New", monospace;
      background: #f1f1ec;
    }}
    pre {{
      padding: 0.75rem 1rem;
      overflow-x: auto;
    }}
    a {{
      color: #0f4c81;
    }}
    a:hover {{
      color: #0b385d;
    }}
  </style>
</head>
<body>
<article>
{body_html}
</article>
</body>
</html>
""".format(title=title, body_html=body_html)


def main() -> int:
    md_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("econ.md")
    html_path = Path(sys.argv[2]) if len(sys.argv) > 2 else md_path.with_suffix(".html")

    if not md_path.exists():
        print(f"Markdown file not found: {md_path}", file=sys.stderr)
        return 1

    try:
        import markdown
    except ImportError:
        print(
            "Missing dependency 'markdown'. Install with: python -m pip install markdown",
            file=sys.stderr,
        )
        return 1

    markdown_text = md_path.read_text(encoding="utf-8")
    title = extract_title(markdown_text, fallback=md_path.stem)
    body_html = markdown.markdown(
        markdown_text,
        extensions=["extra", "sane_lists", "smarty"],
        output_format="html5",
    )

    html_doc = build_html_doc(title, body_html)
    html_path.write_text(html_doc, encoding="utf-8")
    print(f"Wrote {html_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
