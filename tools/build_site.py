"""Собирает docs/index.html — сайт-резюме на GitHub Pages — из README.md и README.en.md.

    uv run --with markdown python tools/build_site.py
"""

import html
import json
import re
import shutil
from pathlib import Path

import markdown
from markdown.extensions.toc import slugify_unicode

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

PAGES = {
    "ru": {
        "file": "README.md",
        "tagline": "Backend на Python, агентные системы на LLM · 9+ лет · удалённо",
        "sections": "Разделы",
        "contacts": [("Email", "onelinelater@gmail.com", "mailto:onelinelater@gmail.com"),
                     ("Telegram", "@onelinelater", "https://t.me/onelinelater"),
                     ("GitHub", "onelinelater", "https://github.com/onelinelater"),
                     ("GitLab", "onelinelater", "https://gitlab.com/onelinelater"),
                     ("Город", "Хабаровск · remote", None)],
        "footer": "Сайт собран из README профиля",
    },
    "en": {
        "file": "README.en.md",
        "tagline": "Python backend, LLM agent systems · 9+ years · remote",
        "sections": "Sections",
        "contacts": [("Email", "onelinelater@gmail.com", "mailto:onelinelater@gmail.com"),
                     ("Telegram", "@onelinelater", "https://t.me/onelinelater"),
                     ("GitHub", "onelinelater", "https://github.com/onelinelater"),
                     ("GitLab", "onelinelater", "https://gitlab.com/onelinelater"),
                     ("Location", "Khabarovsk · remote", None)],
        "footer": "Built from the profile README",
    },
}


def split_readme(text: str) -> tuple[str, str, str]:
    """Имя, подзаголовок и тело резюме: шапку с аватаром и бейджами сайт рисует сам."""
    name = re.search(r"^# (.+)$", text, re.M).group(1).strip()
    headline = re.search(r"^## (.+)$", text, re.M).group(1).strip()
    body = text.split("\n---\n", 1)[1]
    return name, headline, body


def render(lang: str, conf: dict) -> tuple[str, dict]:
    name, headline, body = split_readme((ROOT / conf["file"]).read_text(encoding="utf-8"))
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"],
                           extension_configs={"toc": {"slugify": slugify_unicode}})
    article = md.convert(body)
    nav = "\n".join(
        f'<a href="#{t["id"]}">{html.escape(re.sub(r"^[^\w]+", "", t["name"]).split(" — ")[0].strip())}</a>'
        for t in md.toc_tokens
    )
    contacts = "\n".join(
        f'<li><span class="k">{k}</span>'
        + (f'<a href="{href}">{html.escape(v)}</a>' if href else html.escape(v))
        + "</li>"
        for k, v, href in conf["contacts"]
    )
    hidden = "" if lang == "ru" else " hidden"
    section = f"""<section class="page" data-lang="{lang}" lang="{lang}"{hidden}>
  <header class="hero">
    <img class="avatar" src="avatar.jpg" alt="{html.escape(name)}" width="132" height="132">
    <div>
      <h1>{html.escape(name)}</h1>
      <p class="headline">{html.escape(headline)}</p>
      <p class="tagline">{html.escape(conf["tagline"])}</p>
      <ul class="contacts">
{contacts}
      </ul>
    </div>
  </header>
  <nav class="sections" aria-label="{conf["sections"]}">
{nav}
  </nav>
  <article class="resume">
{article}
  </article>
  <footer>{conf["footer"]} · <a href="https://github.com/onelinelater/onelinelater">github.com/onelinelater/onelinelater</a></footer>
</section>"""
    return section, {"title": f"{name} — {headline}", "name": name}


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    sections, meta = [], {}
    for lang, conf in PAGES.items():
        section, meta[lang] = render(lang, conf)
        sections.append(section)
    template = (ROOT / "tools" / "site.html").read_text(encoding="utf-8")
    page = (template.replace("{{TITLE}}", html.escape(meta["ru"]["title"]))
                    .replace("{{DESCRIPTION}}", html.escape(PAGES["ru"]["tagline"]))
                    .replace("{{PAGES}}", "\n".join(sections))
                    .replace("{{META}}", json.dumps(meta, ensure_ascii=False)))
    (DOCS / "index.html").write_text(page, encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    shutil.copyfile(ROOT / "avatar.jpg", DOCS / "avatar.jpg")
    print("docs/index.html:", len(page), "bytes")


if __name__ == "__main__":
    main()
