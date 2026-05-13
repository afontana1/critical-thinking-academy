import argparse
import re
from pathlib import Path

import markdown

MERMAID_FENCE_RE = re.compile(
    r"(^```[ \t]*mermaid[ \t]*\r?\n)(.*?)(\r?\n```[ \t]*$)",
    re.MULTILINE | re.DOTALL,
)

MERMAID_SCRIPT = """<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
  mermaid.initialize({ startOnLoad: true });
</script>
"""


def convert_markdown(md_text: str) -> str:
    mermaid_found = False

    def _replace_mermaid(match: re.Match) -> str:
        nonlocal mermaid_found
        mermaid_found = True
        code = match.group(2).strip("\r\n")
        return f"<div class=\"mermaid\">\n{code}\n</div>"

    md_text = MERMAID_FENCE_RE.sub(_replace_mermaid, md_text)

    html_body = markdown.markdown(
        md_text,
        extensions=[
            "extra",
            "sane_lists",
            "toc",
            "fenced_code",
            "codehilite",
        ],
        output_format="html5",
    )

    if mermaid_found:
        html_body = f"{MERMAID_SCRIPT}\n{html_body}"

    return html_body


def convert_file(path: Path, out_dir: Path) -> Path:
    md_text = path.read_text(encoding="utf-8")
    html_text = convert_markdown(md_text)
    out_path = out_dir / f"{path.stem}.html"
    out_path.write_text(html_text, encoding="utf-8")
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert Markdown files to Blogger-ready HTML."
    )
    parser.add_argument(
        "inputs",
        nargs="*",
        help="Markdown files to convert. Defaults to all .md in the cwd.",
    )
    parser.add_argument(
        "--out-dir",
        default=".",
        help="Output directory for HTML files (default: current directory).",
    )
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.inputs:
        inputs = [Path(p) for p in args.inputs]
    else:
        inputs = sorted(Path.cwd().glob("*.md"))

    if not inputs:
        print("No markdown files found.")
        return 1

    for md_path in inputs:
        if md_path.suffix.lower() != ".md":
            continue
        out_path = convert_file(md_path, out_dir)
        print(f"Wrote {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
