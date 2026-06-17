#!/usr/bin/env python3
"""Emulate the Jekyll build of the `minimal` layout for local preview (no Ruby needed).

Resolves the Liquid in _layouts/minimal.html and stitches in each page body so we can
eyeball the actually-ported pages before pushing. NOT a general Jekyll renderer.
"""
import os, re, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_preview_build")
SITE_TITLE = "Jakub Vrabel"
SITE_DESC = "Ph.D. candidate working on ML&Physics."

# (source file, nav key, output filename)
PAGES = [
    ("_pages/about.md",    "about",    "index.html"),
    ("_pages/events.md",   "events",   "events.html"),
    ("_pages/teaching.html","teaching","teaching.html"),
    ("_pages/cv.md",       "cv",       "cv.html"),
]
NAV_HREF = {"about": "index.html", "events": "events.html",
            "teaching": "teaching.html", "cv": "cv.html"}
IMAGES = ["jv_s.jpg", "mode_connectivity.png", "sparsity_custom.png",
          "double_descent.png", "spectra_transfer.png"]


def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    fm_raw, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_raw.splitlines():
        if ":" in line and not line.startswith(" ") and not line.startswith("-"):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    return fm, body


def render(layout, fm, body, nav):
    out = layout
    # title
    title = SITE_TITLE if nav == "about" else f"{fm.get('title','')} — {SITE_TITLE}"
    out = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", out, flags=re.S)
    # description
    desc = fm.get("description", SITE_DESC)
    out = re.sub(r'(<meta name="description" content=")[^"]*(">)',
                 lambda m: m.group(1) + desc + m.group(2), out)
    # asset urls
    out = out.replace("{{ '/assets/css/style.css' | relative_url }}", "style.css")
    out = out.replace("{{ '/assets/js/theme.js' | relative_url }}", "theme.js")
    # nav hrefs
    out = out.replace("{{ '/' | relative_url }}", "index.html")
    out = out.replace("{{ '/events/' | relative_url }}", "events.html")
    out = out.replace("{{ '/teaching/' | relative_url }}", "teaching.html")
    out = out.replace("{{ '/cv/' | relative_url }}", "cv.html")
    # active class blocks: {% if page.nav == "x" %} class="active"{% endif %}
    def active(m):
        return ' class="active"' if m.group(1) == nav else ""
    out = re.sub(r'\{% if page\.nav == "(\w+)" %\} class="active"\{% endif %\}', active, out)
    # the title-conditional in <title> already handled; strip any leftover liquid in title region
    # content + leftover site.title
    body_local = body.replace("/images/", "images/")
    out = out.replace("{{ content }}", body_local)
    out = out.replace("{{ site.title }}", SITE_TITLE)
    return out


def main():
    layout = open(os.path.join(ROOT, "_layouts/minimal.html"), encoding="utf-8").read()
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "images"))
    for img in IMAGES:
        shutil.copy(os.path.join(ROOT, "images", img), os.path.join(OUT, "images", img))
    shutil.copy(os.path.join(ROOT, "assets/css/style.css"), os.path.join(OUT, "style.css"))
    shutil.copy(os.path.join(ROOT, "assets/js/theme.js"), os.path.join(OUT, "theme.js"))
    for src, nav, outname in PAGES:
        text = open(os.path.join(ROOT, src), encoding="utf-8").read()
        fm, body = split_front_matter(text)
        html = render(layout, fm, body, nav)
        open(os.path.join(OUT, outname), "w", encoding="utf-8").write(html)
        print("built", outname)
    # sanity: warn on any unresolved liquid
    for outname in [p[2] for p in PAGES]:
        h = open(os.path.join(OUT, outname), encoding="utf-8").read()
        leftover = re.findall(r"\{\{.*?\}\}|\{%.*?%\}", h)
        if leftover:
            print("  WARNING unresolved in", outname, ":", leftover[:5])


if __name__ == "__main__":
    main()
