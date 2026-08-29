from __future__ import annotations

import html
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(".")
SKIP_PARTS = {".git"}
TITLE_RE = re.compile(r"<title\b[^>]*>(.*?)</title>", re.I | re.S)
HEADING_RE = re.compile(r"<h([12])\b[^>]*>(.*?)</h\1>", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")
MAPPING_FILENAMES = ("title-mapping.json", "title-mappings.json")


def clean_text(value: str) -> str:
    value = TAG_RE.sub(" ", value)
    return " ".join(html.unescape(value).split())


def title_for(path: Path) -> str:
    text = path.read_text(encoding="utf-8-sig", errors="ignore")
    title_match = TITLE_RE.search(text)
    if title_match:
        title = clean_text(title_match.group(1))
        if title and title.lower() != "table of contents":
            return title

    for heading_match in HEADING_RE.finditer(text):
        heading = clean_text(heading_match.group(2))
        if heading and heading.lower() not in {"contents", "table of contents"}:
            return heading

    return path.parent.name.replace("-", " ").replace("_", " ").title()


def flatten_mapping(data: dict, prefix: tuple[str, ...] = ()) -> dict[str, str]:
    flattened: dict[str, str] = {}
    for key, value in data.items():
        parts = prefix + (str(key),)
        if isinstance(value, dict):
            flattened.update(flatten_mapping(value, parts))
        else:
            flattened["/".join(parts)] = str(value)
    return flattened


def load_title_mappings() -> dict[str, dict[str, str]]:
    mappings: dict[str, dict[str, str]] = {}
    for section_dir in ROOT.iterdir():
        if not section_dir.is_dir() or section_dir.name in SKIP_PARTS:
            continue
        for filename in MAPPING_FILENAMES:
            mapping_path = section_dir / filename
            if not mapping_path.exists():
                continue
            raw = mapping_path.read_text(encoding="utf-8-sig").strip()
            if not raw:
                continue
            data = json.loads(raw)
            mappings[section_dir.name] = flatten_mapping(data)
            break
    return mappings


def mapped_title_for(path: Path, mappings: dict[str, dict[str, str]]) -> str | None:
    if len(path.parts) < 2:
        return None
    section = path.parts[0]
    section_mapping = mappings.get(section, {})
    folder_parts = path.parts[1:-1]
    for index in range(len(folder_parts), 0, -1):
        key = "/".join(folder_parts[:index])
        title = section_mapping.get(key)
        if title:
            return title
    return None


def section_name(part: str) -> str:
    return {
        "culture": "Culture",
        "economics": "Economics",
        "philosophy": "Philosophy",
        "policy-politics": "Policy & Politics",
        "propaganda": "Propaganda",
        "religion": "Religion",
        "science-engineering": "Science & Engineering",
    }.get(part, part.replace("-", " ").replace("_", " ").title())


def collect_posts() -> dict[str, list[tuple[str, str]]]:
    posts: dict[str, list[tuple[str, str]]] = defaultdict(list)
    mappings = load_title_mappings()
    for path in sorted(ROOT.rglob("*.html")):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.name.lower() == "index.html":
            continue
        try:
            rel = path.relative_to(ROOT).as_posix()
            title = mapped_title_for(path, mappings) or title_for(path)
        except OSError:
            continue
        section = section_name(path.parts[0]) if len(path.parts) > 1 else "Posts"
        posts[section].append((title, rel))
    return posts


def render_index(posts: dict[str, list[tuple[str, str]]]) -> str:
    total = sum(len(items) for items in posts.values())
    nav = "\n".join(
        f'<a href="#{html.escape(section.lower().replace(" & ", "-").replace(" ", "-"))}">{html.escape(section)}</a>'
        for section in posts
    )
    sections = []
    for section, items in posts.items():
        section_id = section.lower().replace(" & ", "-").replace(" ", "-")
        links = "\n".join(
            f'''            <li>
              <a href="{html.escape(url, quote=True)}">{html.escape(title)}</a>
            </li>'''
            for title, url in sorted(items, key=lambda item: item[0].lower())
        )
        sections.append(
            f'''      <section id="{html.escape(section_id)}" class="post-section">
        <div class="section-heading">
          <h2>{html.escape(section)}</h2>
          <p>{len(items)} posts</p>
        </div>
        <ol class="post-list">
{links}
        </ol>
      </section>'''
        )

    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Critical Thinking Academy</title>
    <meta
      name="description"
      content="A static archive of critical thinking, philosophy, economics, religion, science, and media analysis essays."
    />
    <style>
      :root {{
        color-scheme: dark;
        --bg: #111413;
        --panel: #181d1b;
        --panel-soft: #202622;
        --text: #f1f3ee;
        --muted: #aab2aa;
        --line: #394039;
        --accent: #86d1c2;
        --accent-2: #e5c56e;
      }}

      * {{
        box-sizing: border-box;
      }}

      body {{
        margin: 0;
        background: var(--bg);
        color: var(--text);
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
          Helvetica, Arial, sans-serif;
        line-height: 1.6;
      }}

      a {{
        color: inherit;
        text-decoration-color: color-mix(in srgb, var(--accent) 72%, transparent);
        text-underline-offset: 0.18em;
      }}

      .site-shell {{
        width: min(1120px, calc(100% - 2rem));
        margin: 0 auto;
        padding: 2.5rem 0 4rem;
      }}

      header {{
        padding: 2rem 0 1.2rem;
        border-bottom: 1px solid var(--line);
      }}

      h1 {{
        margin: 0;
        max-width: 780px;
        font-size: clamp(2rem, 5vw, 4.25rem);
        line-height: 1.02;
        letter-spacing: 0;
      }}

      header p {{
        max-width: 760px;
        margin: 1rem 0 0;
        color: var(--muted);
        font-size: 1.05rem;
      }}

      .stats {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin: 1.25rem 0 0;
      }}

      .stats span,
      nav a {{
        display: inline-flex;
        min-height: 2.25rem;
        align-items: center;
        border: 1px solid var(--line);
        border-radius: 0.45rem;
        padding: 0.35rem 0.65rem;
        background: var(--panel);
        color: var(--muted);
        font-size: 0.92rem;
      }}

      nav {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
        margin: 1.5rem 0 2rem;
      }}

      nav a {{
        color: var(--text);
        text-decoration: none;
      }}

      nav a:hover,
      nav a:focus-visible {{
        border-color: var(--accent);
      }}

      .post-section {{
        padding: 1.4rem 0;
        border-top: 1px solid var(--line);
      }}

      .section-heading {{
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: 0.8rem;
      }}

      h2 {{
        margin: 0;
        font-size: 1.35rem;
      }}

      .section-heading p {{
        margin: 0;
        color: var(--muted);
        font-size: 0.92rem;
      }}

      .post-list {{
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 0.75rem;
        margin: 0;
        padding: 0;
        list-style: none;
      }}

      .post-list li {{
        min-width: 0;
        border: 1px solid var(--line);
        border-radius: 0.45rem;
        background: var(--panel);
      }}

      .post-list a {{
        display: block;
        padding: 0.85rem 0.9rem;
        font-weight: 700;
      }}

      footer {{
        margin-top: 2rem;
        padding-top: 1.25rem;
        border-top: 1px solid var(--line);
        color: var(--muted);
        font-size: 0.92rem;
      }}

      @media (max-width: 760px) {{
        .site-shell {{
          width: min(100% - 1rem, 1120px);
          padding-top: 1.2rem;
        }}

        header {{
          padding-top: 1rem;
        }}

        .post-list {{
          grid-template-columns: 1fr;
        }}

        .section-heading {{
          align-items: flex-start;
          flex-direction: column;
          gap: 0.2rem;
        }}
      }}
    </style>
  </head>
  <body>
    <main class="site-shell">
      <header>
        <h1>Critical Thinking Academy</h1>
        <p>
          A static archive of essays on argumentation, evidence, philosophy,
          economics, religion, science, engineering, media, and propaganda.
        </p>
        <div class="stats">
          <span>{total} posts</span>
          <span>{len(posts)} sections</span>
        </div>
      </header>
      <nav aria-label="Sections">
{nav}
      </nav>
{chr(10).join(sections)}
      <footer>
        <p>Published as a static GitHub Pages project site.</p>
      </footer>
    </main>
  </body>
</html>
'''


def main() -> None:
    posts = collect_posts()
    output = render_index(posts)
    Path("index.html").write_text(output, encoding="utf-8")
    print(f"posts={sum(len(items) for items in posts.values())}")
    for section, items in posts.items():
        print(f"{section}: {len(items)}")


if __name__ == "__main__":
    main()
