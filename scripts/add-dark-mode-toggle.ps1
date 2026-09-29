param(
    [string]$Root = (Split-Path -Parent $PSScriptRoot)
)

$marker = 'data-cta-theme-toggle'
$block = @'

<!-- CTA dark-mode toggle -->
<style id="cta-theme-toggle-styles">
  :root { color-scheme: light dark; }
  .cta-theme-toggle-wrap {
    box-sizing: border-box;
    display: flex;
    justify-content: flex-end;
    width: min(100%, 980px);
    margin: 0 auto;
    padding: 0.75rem 1rem 0.25rem;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }
  .cta-theme-toggle {
    appearance: none;
    border: 1px solid currentColor;
    border-radius: 999px;
    background: transparent;
    color: inherit;
    cursor: pointer;
    font: inherit;
    font-size: 0.875rem;
    font-weight: 650;
    line-height: 1;
    padding: 0.6rem 0.85rem;
  }
  .cta-theme-toggle:hover { background: color-mix(in srgb, currentColor 10%, transparent); }
  .cta-theme-toggle:focus-visible { outline: 3px solid #60a5fa; outline-offset: 3px; }
  html[data-cta-theme="light"] { color-scheme: light; background: #ffffff; }
  html[data-cta-theme="light"] body,
  html[data-cta-theme="light"] .ep-post,
  html[data-cta-theme="light"] article { background-color: #ffffff; color: #1f2937; }
  html[data-cta-theme="dark"] { color-scheme: dark; background: #111827; }
  html[data-cta-theme="dark"] body,
  html[data-cta-theme="dark"] .ep-post,
  html[data-cta-theme="dark"] article { background-color: #111827; color: #e5e7eb; }
  html[data-cta-theme="dark"] a { color: #93c5fd; }
  html[data-cta-theme="dark"] :where(table, th, td, pre, code, blockquote) {
    border-color: #4b5563;
  }
  html[data-cta-theme="dark"] :where(th, td, pre, blockquote) { background-color: #1f2937; }
  @media (max-width: 720px) {
    .cta-theme-toggle-wrap { width: 100%; padding: 0.6rem 0.85rem 0.15rem; }
    .cta-theme-toggle { min-height: 44px; }
  }
</style>
<div class="cta-theme-toggle-wrap" data-cta-theme-toggle>
  <button class="cta-theme-toggle" type="button" aria-label="Switch color theme" aria-pressed="false">Dark mode</button>
</div>
<script data-cta-theme-toggle-script>
  (() => {
    const root = document.documentElement;
    const key = "cta-color-theme";
    let saved = null;
    try { saved = localStorage.getItem(key); } catch (_) {}
    const preferred = saved === "dark" || saved === "light"
      ? saved
      : (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    root.dataset.ctaTheme = preferred;

    const updateButtons = () => {
      const dark = root.dataset.ctaTheme === "dark";
      document.querySelectorAll(".cta-theme-toggle").forEach((button) => {
        button.textContent = dark ? "Light mode" : "Dark mode";
        button.setAttribute("aria-pressed", String(dark));
      });
    };

    document.querySelectorAll(".cta-theme-toggle").forEach((button) => {
      button.addEventListener("click", () => {
        const next = root.dataset.ctaTheme === "dark" ? "light" : "dark";
        root.dataset.ctaTheme = next;
        try { localStorage.setItem(key, next); } catch (_) {}
        updateButtons();
      });
    });
    updateButtons();
  })();
</script>
'@

$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
$files = Get-ChildItem -LiteralPath $Root -Recurse -File -Filter '*.html' |
    Where-Object { $_.FullName -ne (Join-Path $Root 'index.html') }

$changed = 0
foreach ($file in $files) {
    $text = [System.IO.File]::ReadAllText($file.FullName)
    if ($text.Contains($marker)) {
        $toggleStart = $text.IndexOf('<!-- CTA dark-mode toggle -->', [System.StringComparison]::Ordinal)
        $epPost = [regex]::Match($text, '<div\b[^>]*class=["''][^"'']*\bep-post\b[^>]*>', 'IgnoreCase')
        if ($epPost.Success -and $toggleStart -gt $epPost.Index) {
            $toggleScript = $text.IndexOf('<script data-cta-theme-toggle-script>', $toggleStart, [System.StringComparison]::Ordinal)
            $toggleEnd = $text.IndexOf('</script>', $toggleScript, [System.StringComparison]::Ordinal)
            if ($toggleScript -lt 0 -or $toggleEnd -lt 0) {
                throw "Could not identify the existing toggle block in $($file.FullName)."
            }
            $toggleEnd += 9
            $updated = $text.Remove($toggleStart, $toggleEnd - $toggleStart)
            $newEpPost = [regex]::Match($updated, '<div\b[^>]*class=["''][^"'']*\bep-post\b[^>]*>', 'IgnoreCase')
            $updated = $updated.Insert($newEpPost.Index, $block)
            [System.IO.File]::WriteAllText($file.FullName, $updated, $utf8NoBom)
            $changed++
        }
        continue
    }

    $body = [regex]::Match($text, '<body\b[^>]*>', 'IgnoreCase')
    if ($body.Success) {
        $position = $body.Index + $body.Length
    } else {
        $article = [regex]::Match($text, '<article\b', 'IgnoreCase')
        if ($article.Success) {
            $position = $article.Index
        } else {
            $epPost = [regex]::Match($text, '<div\b[^>]*class=["''][^"'']*\bep-post\b[^>]*>', 'IgnoreCase')
            if ($epPost.Success) {
                $position = $epPost.Index
            } else {
                $lastScript = $text.LastIndexOf('</script>', [System.StringComparison]::OrdinalIgnoreCase)
                $position = if ($lastScript -ge 0) { $lastScript + 9 } else { 0 }
            }
        }
    }

    $updated = $text.Insert($position, $block)
    [System.IO.File]::WriteAllText($file.FullName, $updated, $utf8NoBom)
    $changed++
}

Write-Output "Injected theme toggle into $changed HTML files."
