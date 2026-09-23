#!/usr/bin/env python3
"""Post-process the rendered multilingual site.

- adds <link rel="alternate" hreflang="..."> for every language version of a page
  (plus x-default pointing at the English page)
- forces the <html lang> attribute per language folder (nn -> nn-hognorsk, pt -> pt-BR)
- replaces %%BUILD_YEAR%% and %%BUILD_STAMP%% (footer) with the render date and time (UTC)

Usage: python tools/post_build.py _site
"""
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SITE_URL = "https://eiriktengesdal.no"
# folder under _site -> BCP 47 tag; "" is the site root (English)
LANGS = {"": "en", "nb": "nb", "nn": "nn-hognorsk", "ja": "ja", "pt": "pt-BR"}
SKIP_PARTS = {"site_libs"}


def language_folder(rel: Path) -> str:
    first = rel.parts[0] if len(rel.parts) > 1 else ""
    return first if first in LANGS else ""


def public_url(folder: str, inner: Path) -> str:
    path = (Path(folder) / inner).as_posix() if folder else inner.as_posix()
    if path.endswith("index.html"):
        path = path[: -len("index.html")]
    return f"{SITE_URL}/{path}"


def main(site: Path) -> None:
    now = datetime.now(timezone.utc)
    stamp = f"{now.day} {now:%B %Y} ({now:%H:%M} UTC)"
    pages = [
        p
        for p in site.rglob("*.html")
        if not any(part in SKIP_PARTS or part.endswith("_files") for part in p.relative_to(site).parts)
    ]
    for page in pages:
        rel = page.relative_to(site)
        folder = language_folder(rel)
        inner = Path(*rel.parts[1:]) if folder else rel
        alternates = [
            (tag, public_url(f, inner))
            for f, tag in LANGS.items()
            if (site / f / inner if f else site / inner).exists()
        ]
        html = page.read_text(encoding="utf-8")
        html = re.sub(r'[ \t]*<link rel="alternate" hreflang="[^"]*" href="[^"]*"\s*/?>\n?', "", html)
        if alternates:
            links = "".join(f'<link rel="alternate" hreflang="{t}" href="{u}">\n' for t, u in alternates)
            english = dict(alternates).get("en")
            if english:
                links += f'<link rel="alternate" hreflang="x-default" href="{english}">\n'
            html = html.replace("</head>", links + "</head>", 1)
        html = re.sub(r'(<html\b[^>]*?\s)lang="[^"]*"', rf'\1lang="{LANGS[folder]}"', html, count=1)
        html = re.sub(r'(<html\b[^>]*?\s)xml:lang="[^"]*"', rf'\1xml:lang="{LANGS[folder]}"', html, count=1)
        html = html.replace("%%BUILD_YEAR%%", str(now.year)).replace("%%BUILD_STAMP%%", stamp)
        page.write_text(html, encoding="utf-8")
    print(f"post_build: processed {len(pages)} pages under {site}")


if __name__ == "__main__":
    main(Path(sys.argv[1] if len(sys.argv) > 1 else "_site"))
