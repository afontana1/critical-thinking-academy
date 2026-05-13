#!/usr/bin/env python3
"""
Offline Markdown -> HTML for Blogger, with Mermaid support.

- Converts Markdown to HTML
- Rewrites ```mermaid fenced blocks into: <pre class="mermaid">...</pre>
- Prepends Mermaid import/init snippet (optional)

Install:
  pip install markdown

Usage:
  python md2blogger.py input.md -o output.html
  python md2blogger.py input.md --no-mermaid-script -o body.html
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

try:
    import markdown as mdlib
except ImportError as e:
    raise SystemExit(
        "Missing dependency: 'markdown'\n"
        "Install it with: pip install markdown\n"
    ) from e


MERMAID_FENCE_RE = re.compile(
    r"(^```[ \t]*mermaid[ \t]*\r?\n)(.*?)(\r?\n```[ \t]*$)",
    re.MULTILINE | re.DOTALL,
)

MERMAID_SCRIPT = """<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
  mermaid.initialize({ startOnLoad: true });
</script>
"""


def replace_mermaid_fences(markdown_text: str) -> str:
    """
    Replace ```mermaid ... ``` with raw HTML:
      <pre class="mermaid">...</pre>

    We HTML-escape the diagram text so characters like < or & don't break the page.
    Mermaid reads the text content inside the <pre>.
    """
    def _sub(match: re.Match) -> str:
        diagram = match.group(2).strip("\r\n")
        diagram_escaped = html.escape(diagram, quote=False)
        return f'\n<pre class="mermaid">\n{diagram_escaped}\n</pre>\n'

    return MERMAID_FENCE_RE.sub(_sub, markdown_text)


def markdown_to_html(markdown_text: str) -> str:
    """
    Convert Markdown -> HTML.
    Add/remove extensions depending on what you use.
    """
    return mdlib.markdown(
        markdown_text,
        extensions=[
            "fenced_code",
            "tables",
            "toc",
            "smarty",
        ],
        output_format="html5",
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path, help="Input Markdown file")
    ap.add_argument("-o", "--output", type=Path, default=None, help="Output HTML file (default: stdout)")
    ap.add_argument("--no-mermaid-script", action="store_true", help="Do not prepend the Mermaid <script> import")
    ap.add_argument("--full-page", action="store_true", help="Wrap output in a full HTML document")
    args = ap.parse_args()

    md_text = args.input.read_text(encoding="utf-8")

    # 1) Turn mermaid fences into <pre class="mermaid">...</pre>
    md_text = replace_mermaid_fences(md_text)

    # 2) Convert remaining Markdown -> HTML
    body_html = markdown_to_html(md_text)

    # 3) Optionally prepend Mermaid dependency script
    out_html = body_html
    if not args.no_mermaid_script:
        out_html = MERMAID_SCRIPT + "\n" + out_html

    # 4) Optionally wrap as a full HTML page
    if args.full_page:
        out_html = (
            "<!doctype html>\n"
            "<html>\n<head>\n<meta charset=\"utf-8\">\n</head>\n<body>\n"
            f"{out_html}\n"
            "</body>\n</html>\n"
        )

    if args.output:
        args.output.write_text(out_html, encoding="utf-8")
    else:
        print(out_html)


if __name__ == "__main__":
    main()
