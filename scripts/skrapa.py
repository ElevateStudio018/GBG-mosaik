"""Skrapar text, bilder och PDF:er från nuvarande hemsida (www.gbgmosaik.se).

Kör från repots rot:  python3 scripts/skrapa.py
Texten per sida hamnar i skrapat/text/*.txt och originalfilerna i skrapat/original/ (samma sökvägar som på
gbgmosaik.se, mappen är inte incheckad). Kör sedan scripts/bilder.py för att göra webbversioner till docs/.
Kräver bara Pythons standardbibliotek.

Sidorna är de som länkas från gbgmosaik.se, även de som bara finns i bortkommenterad HTML på startsidan.
Sidan "Skulptur och Konst" (/17/9/skulptur-och-konst/) ger 404 – bilderna finns i stället på /17/9/foretagsloggor/.
"""
import os
import re
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser

BASE = "https://www.gbgmosaik.se/"
PAGES = {
    "start": "",
    "terrazzo": "17/8/terrazzo/",
    "platsgjuten-terrazzo": "17/3/platsgjuten-terrazzo/",
    "terrazzo-golv-och-vaggplattor": "17/4/terrazzo-golv-och-vaggplattor/",
    "terrazzo-fasad": "17/5/terrazzo-fasad/",
    "terrazzo-trappbekladnad": "17/6/terrazzo-trappbekladnad/",
    "terrazzo-bankskivor-fonsterbankar": "17/7/terrazzo-bankskivor-fonsterbankar/",
    "foretagsloggor-skulptur": "17/9/foretagsloggor/",
    "loggor": "17/15/loggor/",
    "renovering-av-terrazzo": "17/16/",
    "torkzoner": "17/10/torkzoner/",
    "taktila-markeringar": "17/13/taktila-markeringar/",
    "ovriga-produkter": "17/2/ovriga-produkter/",
    "bestall-prover": "17/14/bestall-prover/",
}
# Bakgrundsbilderna i startsidans bildspel sätts i inline-CSS och bilderna i kommenterad HTML hittas inte av parsern.
EXTRA = ["assets/images/gbgmosaik-bg-" + n + ".jpg" for n in ("stentrappa", "marco-salvatori", "restaurang", "purple", "nesite")] + \
        ["files/" + n for n in ("torkzon.jpg", "taktila-markeringar.jpg", "steinfix-ovriga-produkter.jpg", "fasad-ny.jpg",
                                "trappbekladnad.jpg", "bankskivor-fonsterskivor-2.jpg", "skulpturer-konst-2_1000px.jpg")]
OUT_TXT, OUT_ORIG = "skrapat/text", "skrapat/original"
UA = {"User-Agent": "Mozilla/5.0 (gbgmosaik innehallsflytt)"}
FILE_RE = re.compile(r"\.(jpe?g|png|gif|pdf)$", re.I)


class Page(HTMLParser):
    BLOCK = {"p", "div", "section", "br", "tr", "td", "address", "span", "a"}

    def __init__(self, url):
        super().__init__()
        self.url, self.out, self.files, self.skip = url, [], set(), 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "noscript", "svg", "head"):
            self.skip += 1
        if tag in ("h1", "h2", "h3", "h4"):
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li":
            self.out.append("\n* ")
        elif tag in self.BLOCK:
            self.out.append("\n")
        for k in ("src", "href", "data-src"):
            v = a.get(k)
            if v and (tag == "img" or FILE_RE.search(v)):
                self.files.add(urllib.parse.urljoin(self.url, v))
        for u in re.findall(r"url\(['\"]?([^'\")]+)", a.get("style", "")):
            self.files.add(urllib.parse.urljoin(self.url, u))

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg", "head") and self.skip:
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip and d.strip():
            self.out.append(re.sub(r"\s+", " ", d))

    def text(self):
        t = re.sub(r"[ \t]+\n", "\n", "".join(self.out))
        return re.sub(r"\n{3,}", "\n\n", t).strip()


def get(url):
    parts = urllib.parse.urlsplit(url)
    url = urllib.parse.urlunsplit(parts._replace(path=urllib.parse.quote(urllib.parse.unquote(parts.path))))
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return r.read()


def main():
    os.makedirs(OUT_TXT, exist_ok=True)
    files = {urllib.parse.urljoin(BASE, e) for e in EXTRA}
    for name, path in PAGES.items():
        url = BASE + path
        try:
            raw = get(url + ("index.html" if path else "")).decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            print("Kunde inte hämta", url, e)
            continue
        # Även bortkommenterade produktkort på startsidan.
        p = Page(url)
        p.feed(raw.replace("<!--", "").replace("-->", ""))
        with open(os.path.join(OUT_TXT, name + ".txt"), "w", encoding="utf-8") as f:
            f.write(url + "\n\n" + p.text() + "\n")
        files |= {u for u in p.files if urllib.parse.urlsplit(u).netloc.endswith("gbgmosaik.se")}
        print(f"{name}: {len(p.files)} filer")
    ok = 0
    for u in sorted(files):
        if "/resources/" in u or "/favicon/" in u or not FILE_RE.search(u):
            continue
        dest = os.path.join(OUT_ORIG, urllib.parse.unquote(urllib.parse.urlsplit(u).path).lstrip("/"))
        if os.path.exists(dest):
            ok += 1
            continue
        try:
            data = get(u)
        except Exception as e:  # noqa: BLE001
            print("  saknas:", u, e)
            continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as f:
            f.write(data)
        ok += 1
    print(ok, "filer i", OUT_ORIG)


if __name__ == "__main__":
    sys.exit(main())
