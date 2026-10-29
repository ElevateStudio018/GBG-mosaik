"""Bygger docs/*.html för Göteborgs Mosaikbeläggningar AB.

Kör:  python3 scripts/build.py docs

Texterna och uppgifterna ligger i scripts/innehall.py, bilderna görs av scripts/bilder.py.
"""
import html
import json
import pathlib
import sys
from urllib.parse import quote

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import innehall as C  # noqa: E402

# Elevate Studio's credit under every footer: the mark and the name, the whole of it one link to elevatestudio.nu.
ELEVATE_CREDIT = '''<!-- elevate-credit -->
<style>.elevate-credit{max-width:1240px;margin:24px auto 0;padding:20px 16px 0;border-top:1px solid rgba(128,128,128,.25);display:flex;justify-content:center;box-sizing:border-box}.elevate-credit a{display:inline-flex;align-items:center;gap:8px;padding:8px 0;font:inherit;font-size:13px;line-height:1;color:inherit;opacity:.55;text-decoration:none;transition:opacity .2s}.elevate-credit a:hover,.elevate-credit a:focus-visible{opacity:1}.elevate-credit svg{width:16px;height:16px;flex:none;display:block}@media(min-width:1024px){.elevate-credit a{font-size:14px}}</style>
<div class="elevate-credit"><a href="https://elevatestudio.nu" target="_blank" rel="noopener"><svg viewBox="0 0 1884.3 1353.9" aria-hidden="true"><path d="M0.0 1353.9 L1218.7 0.0 L1218.7 329.1 L479.7 1136.4 L786.7 1132.4 L1215.5 687.4 L1884.3 1349.9 L1590.1 1349.9 L1218.6 994.7 L865.4 1349.9Z" fill="currentColor"/></svg>Byggd av Elevate Studio</a></div>
'''


OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
E = html.escape
N_COLORS = sum(len(codes) for _, codes in C.COLLECTION)
N_TILES = sum(len(t) for _, t in C.TILES)

# --- Sidor och meny -------------------------------------------------------------------------------------------------
TERRAZZO = [
    ("platsgjuten-terrazzo", "Platsgjuten terrazzo", "platsgjutet",
     "Fogfria, slitstarka golv och trappor som gjuts på plats – i en egen kollektion med " + str(N_COLORS) + " kulörer."),
    ("terrazzoplattor", "Golv-, vägg- och fasadplattor", "plattor",
     "Prefabricerade terrazzoplattor för golv, väggar, fasader och trappbeklädnad."),
    ("bankskivor", "Bänkskivor och fönsterbänkar", "bankskiva",
     "Kök, badrum och fönsterbänkar i terrazzo, med en egen färggrupp för skivor."),
    ("loggor-och-konst", "Loggor och konst", "logga-naber",
     "Er logga, ett mönster eller ett konstverk – ingjutet i terrazzo."),
]
RENO = ("renovering", "Renovering", "fore-efter", "Slipning, lagning och grovrengöring av terrazzo och natursten.")
OTHER = [
    ("torkzoner", "Torkzoner", "torkzon", "Kåbe skrapgaller och torkmattor som skyddar golvet i entrén."),
    ("taktila-markeringar", "Taktila markeringar", "taktila", "Ledstråk och kontrastmarkeringar för synskadade."),
    ("steinfix", "Steinfix golvvård", "steinfix", "Rengöring, fläckborttagning och impregnering för sten och terrazzo."),
]
CARDS = TERRAZZO + [RENO, OTHER[0]]
NAV = [
    ("Terrazzo", None, TERRAZZO),
    ("Renovering", "renovering.html", None),
    ("Produkter", None, OTHER + [("dokument", "Dokument och skötsel", None, "")]),
    ("Färgkollektion", "platsgjuten-terrazzo.html#kollektion", None),
    ("Om oss", "om-oss.html", None),
    ("Kontakt", "kontakt.html", None),
]
WORK_TYPES = ["Platsgjuten terrazzo", "Terrazzoplattor", "Bänkskiva / fönsterbänk", "Logga eller konst",
              "Renovering, slipning eller lagning", "Torkzoner", "Taktila markeringar", "Steinfix-produkter",
              "Beställ prover", "Annat"]

# --- Ikoner ---------------------------------------------------------------------------------------------------------
def icon(d, cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>')


I_PHONE = icon('<path d="M21 16.5v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 1.1 3.8 2 2 0 0 1 3.1 1.6h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L7.1 9.5a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>')
I_MAIL = icon('<rect x="2.5" y="4.5" width="19" height="15" rx="2"/><path d="m3 6 9 7 9-7"/>')
I_PIN = icon('<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>')
I_PDF = icon('<path d="M14 2.5H6.5a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2V8z"/><path d="M14 2.5V8h5.5M8.5 13h7M8.5 17h5"/>')
I_ARROW = icon('<path d="M5 12h14M13 6l6 6-6 6"/>')
I_DROP = icon('<circle cx="6" cy="7" r="1.6"/><circle cx="15" cy="5" r="1.1"/><circle cx="18" cy="13" r="2"/><circle cx="9" cy="15" r="1.3"/><circle cx="13" cy="19.5" r="1"/><circle cx="4.5" cy="18" r="1"/>')
I_CLOCK = icon('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')
I_LAYERS = icon('<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>')
I_USERS = icon('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>')
I_IG = icon('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/>')
I_FB = icon('<path d="M15 3.5h-2.5A3.5 3.5 0 0 0 9 7v3H6.5v3.5H9V21h3.5v-7.5H15l.5-3.5h-3V7.5a1 1 0 0 1 1-1H15z"/>')
I_IN = icon('<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10.5V17M8 7.5v.01M12 17v-4a2.5 2.5 0 0 1 5 0v4M12 10.5V17"/>')
SOCIAL_ICON = {"Instagram": I_IG, "Facebook": I_FB, "LinkedIn": I_IN}


# --- Byggstenar -----------------------------------------------------------------------------------------------------
def img(name, alt, sizes="100vw", lazy=True, pos="50% 50%", cls=""):
    small = (OUT / "img/foto" / f"{name}-s.jpg").exists()
    srcset = f' srcset="img/foto/{name}-s.jpg 800w, img/foto/{name}.jpg 1800w" sizes="{sizes}"' if small else ""
    load = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="img/foto/{name}.jpg"{srcset} alt="{E(alt)}"{load} decoding="async" '
            f'style="object-position:{pos}">')


def call_btn(cls="btn-accent", label=None):
    return f'<a class="btn {cls}" href="tel:{C.TEL}">{I_PHONE}<span>{label or "Ring " + C.PHONE}</span></a>'


def offer_btn(typ=None, label="Begär offert", cls="btn-ghost"):
    q = f"?typ={quote(typ)}" if typ else ""
    return f'<a class="btn {cls}" href="kontakt.html{q}#offert">{label}</a>'


def samples_btn(cls="btn-ghost", kulor=None):
    q = "?typ=" + quote("Beställ prover") + (f"&amp;kulor={quote(kulor)}" if kulor else "")
    return f'<a class="btn {cls}" href="kontakt.html{q}#offert">{I_DROP}<span>Beställ prover</span></a>'


def eyebrow(t):
    return f'<p class="eyebrow">{t}</p>'


def card(slug, title, photo, short, sizes="(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw"):
    return (f'<li class="card"><a href="{slug}.html"><span class="card-ph">{img(photo, "", sizes)}</span>'
            f'<span class="card-tx"><h3>{title}</h3><p>{short}</p><span class="more">Läs mer {I_ARROW}</span></span></a></li>')


def pills(items, skip=None):
    return "".join(f'<a class="pill" href="{s}.html">{t}</a>' for s, t, *_ in items if s != skip)


def crumbs(*parts):
    links = ['<a href="index.html">Start</a>'] + [f'<a href="{h}">{t}</a>' for t, h in parts[:-1]]
    return (f'<nav class="crumbs" aria-label="Brödsmulor">{" / ".join(links)} / '
            f'<span aria-current="page">{parts[-1][0]}</span></nav>')


def page_hero(title, lead, photo, crumb, btns, alt="", pos="50% 50%"):
    return f'''<section class="hero hero-sub" aria-labelledby="ph-h">
  <div class="hero-bg">{img(photo, alt, lazy=False, pos=pos)}</div>
  <div class="wrap hero-in">
    {crumb}
    <h1 id="ph-h">{title}</h1>
    <p class="hero-lead">{lead}</p>
    <div class="btns">{btns}</div>
  </div>
</section>'''


def specs(rows, cls=""):
    return f'<dl class="specs {cls}">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"


def swatch(code, label, group, note=""):
    c = code.lower()
    n = f'<small>Minimumorder {note}</small>' if note else ""
    caption = f"{label} · minimumorder {note}" if note else label
    return (f'<li data-group="{E(group)}"><button class="sw" type="button" data-lb="img/kulor/{c}.jpg" '
            f'data-caption="{E(caption)}" data-code="{E(label)}">'
            f'<img src="img/kulor/{c}-s.jpg" alt="" loading="lazy" decoding="async" width="240" height="240">'
            f'<span>{E(label)}</span>{n}</button></li>')


def collection_explorer():
    chips = '<button class="chip" type="button" aria-pressed="true" data-filter="*">Alla <b>' + str(N_COLORS) + "</b></button>"
    chips += "".join(f'<button class="chip" type="button" aria-pressed="false" data-filter="{E(g)}">{g} <b>{len(c)}</b></button>'
                     for g, c in C.COLLECTION)
    grid = "".join(swatch(f"GMB-{c}", f"GMB-{c}", g) for g, codes in C.COLLECTION for c in codes)
    return f'<div class="chips" role="group" aria-label="Filtrera kulörer">{chips}</div><ul class="swatches" data-filtered>{grid}</ul>'


def tiles(groups):
    out = []
    for g, items in C.TILES:
        if g not in groups:
            continue
        out.append(f'<h3 class="tile-h">{g}</h3><ul class="swatches">'
                   + "".join(swatch(code, code, g, note) for code, _, note in items) + "</ul>")
    return "".join(out)


def gallery(items, cls=""):
    return (f'<ul class="gallery {cls}">' + "".join(
        f'<li><button type="button" class="gal" data-lb="img/foto/{n}.jpg" data-caption="{E(cap)}">'
        f'{img(n, alt, "(min-width: 960px) 33vw, 50vw")}</button></li>' for n, alt, cap in items) + "</ul>")


def docs_list(groups=None):
    out = []
    for g, files in C.DOCS:
        if groups and g not in groups:
            continue
        lis = "".join(f'<li><a href="dokument/{f}" target="_blank" rel="noopener">{I_PDF}<span>{t}</span><small>PDF</small></a></li>'
                      for t, f in files)
        out.append(f'<div class="doc-group"><h3>{g}</h3><ul class="docs">{lis}</ul></div>')
    return "".join(out)


def cta_band(title="Har du ett projekt på gång?", text=None):
    text = text or ("Berätta om golvet, trappan eller ytan – så hjälper vi dig från idé till färdigt resultat. "
                    "Vill du se materialet först skickar vi gärna prover.")
    return f'''<section class="sec cta" aria-label="Kontakt">
  <div class="wrap cta-in">
    <div><h2>{title}</h2><p>{text}</p></div>
    <div class="btns">{call_btn()}{samples_btn("btn-light")}</div>
  </div>
</section>'''


# --- Sidhuvud och sidfot --------------------------------------------------------------------------------------------
def header(current):
    def link(slug):
        return f'{slug}.html'

    items, mob = [], []
    for label, href, sub in NAV:
        if sub:
            active = any(s == current for s, *_ in sub)
            subs = "".join(f'<li><a href="{link(s)}"{" aria-current=page" if s == current else ""}>{t}</a></li>' for s, t, *_ in sub)
            items.append(f'<li class="has-sub{" on" if active else ""}"><button type="button" class="sub-btn" aria-expanded="false">{label}'
                         f'<svg viewBox="0 0 12 12" aria-hidden="true"><path d="m2.5 4.5 3.5 3.5 3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></button>'
                         f'<ul class="sub">{subs}</ul></li>')
            mob.append(f'<li class="m-h">{label}</li>' + "".join(f'<li><a href="{link(s)}">{t}</a></li>' for s, t, *_ in sub))
        else:
            on = href.split(".")[0] == current
            items.append(f'<li><a href="{href}"{" aria-current=page" if on else ""}>{label}</a></li>')
            mob.append(f'<li><a href="{href}">{label}</a></li>')
    social = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{SOCIAL_ICON[n]}</a>' for n, u in C.SOCIAL)
    return f'''<a class="skip" href="#main">Hoppa till innehållet</a>
<div class="topbar">
  <div class="wrap topbar-in">
    <span>Terrazzo och mosaik sedan {C.FOUNDED}</span>
    <span class="topbar-r"><a href="tel:{C.TEL}">{I_PHONE}{C.PHONE}</a><a href="mailto:{C.EMAIL}">{I_MAIL}{C.EMAIL}</a><span class="soc">{social}</span></span>
  </div>
</div>
<header class="head">
  <div class="wrap bar">
    <a class="logo" href="index.html" aria-label="{C.NAME}, till startsidan"><img src="img/logo.png" alt="{C.NAME}" width="560" height="192"></a>
    <nav class="nav" aria-label="Huvudmeny"><ul>{"".join(items)}</ul></nav>
    {samples_btn("btn-accent head-cta")}
    <a class="round head-call" href="tel:{C.TEL}" aria-label="Ring {C.PHONE}">{I_PHONE}</a>
    <button class="burger" id="menuBtn" type="button" aria-expanded="false" aria-controls="menu" aria-label="Meny"><span></span><span></span><span></span></button>
  </div>
  <nav class="menu" id="menu" aria-label="Meny" hidden>
    <div class="wrap">
      <ul>{"".join(mob)}</ul>
      <div class="btns">{call_btn()}{samples_btn()}</div>
    </div>
  </nav>
</header>'''


def footer():
    t = "".join(f'<li><a href="{s}.html">{n}</a></li>' for s, n, *_ in TERRAZZO + [RENO])
    o = "".join(f'<li><a href="{s}.html">{n}</a></li>' for s, n, *_ in OTHER) + '<li><a href="dokument.html">Dokument och skötsel</a></li>'
    social = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{SOCIAL_ICON[n]}</a>' for n, u in C.SOCIAL)
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a class="logo" href="index.html"><img src="img/logo-vit.png" alt="{C.NAME}" width="560" height="192" loading="lazy"></a>
        <p>Platsgjuten och prefabricerad terrazzo, renovering och golvvård – sedan {C.FOUNDED}.</p>
        <p class="soc">{social}</p>
      </div>
      <div><p class="foot-h">Terrazzo</p><ul>{t}</ul></div>
      <div><p class="foot-h">Produkter</p><ul>{o}</ul></div>
      <div>
        <p class="foot-h">Kontakt</p>
        <p><a href="tel:{C.TEL}">{C.PHONE}</a><br><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
        <p>{C.STREET}<br>{C.POSTAL} {C.CITY}</p>
        <p><a href="om-oss.html">Om oss</a> · <a href="kontakt.html">Kontakt</a></p>
      </div>
    </div>
    <div class="foot-end">
      <span>© <span data-year>2026</span> {C.NAME}</span>
    </div>
  </div>
{ELEVATE_CREDIT}</footer>
<dialog class="lb" id="lb" aria-label="Bildvisning">
  <figure><img id="lb-img" alt=""><figcaption><span id="lb-cap"></span><a class="btn btn-accent btn-sm" id="lb-order" href="kontakt.html" hidden>{I_DROP}<span>Beställ prov på kulören</span></a></figcaption></figure>
  <button class="lb-x" type="button" data-lb-close aria-label="Stäng">×</button>
  <button class="lb-nav lb-prev" type="button" data-lb-step="-1" aria-label="Föregående">‹</button>
  <button class="lb-nav lb-next" type="button" data-lb-step="1" aria-label="Nästa">›</button>
</dialog>
<script src="assets/site.js" defer></script>
</body>
</html>
'''


def jsonld():
    data = {
        "@context": "https://schema.org", "@type": "HomeAndConstructionBusiness", "name": C.NAME, "url": C.SITE_URL,
        "telephone": C.TEL, "email": C.EMAIL, "foundingDate": str(C.FOUNDED), "founder": {"@type": "Person", "name": "Stig Hofling"},
        "image": C.SITE_URL + "img/foto/hero-stentrappa.jpg", "logo": C.SITE_URL + "img/logo.png",
        "address": {"@type": "PostalAddress", "streetAddress": C.STREET, "postalCode": C.POSTAL.replace(" ", ""),
                    "addressLocality": C.CITY, "addressCountry": "SE"},
        "areaServed": "Göteborg", "sameAs": [u for _, u in C.SOCIAL],
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def page(name, title, desc, main, current=None, image="hero-stentrappa", home=False):
    url = C.SITE_URL + ("" if name == "index.html" else name)
    doc = f'''<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="sv_SE">
<meta property="og:site_name" content="{C.NAME}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{C.SITE_URL}img/foto/{image}.jpg">
<meta name="theme-color" content="#f6f2ec">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=Outfit:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="assets/site.css">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
{jsonld() if home else ''}
</head>
<body>
{header(current)}
<main id="main">
{main}
</main>
{footer()}'''
    (OUT / name).write_text(doc, encoding="utf-8")


# --- Startsidan -----------------------------------------------------------------------------------------------------
HERO_SLIDES = [
    ("hero-stentrappa", "Spiraltrappa i ljus terrazzo sedd uppifrån"),
    ("hero-restaurang", "Restaurang med mönstergolv i terrazzo"),
    ("hero-purple", "Lobby med inlagt terrazzomönster i golvet"),
    ("hero-nesite", "Nesites logga ingjuten i terrazzogolvet i en entré"),
]
FAQ = [
    ("Vilka arbetar ni med?",
     "Vi vänder oss främst till arkitekter, byggherrar, konstnärer och designers men tar även emot beställningar från "
     "privatpersoner. Inga projekt är för stora eller för små."),
    ("Vad är terrazzo?",
     "Ett slipbart naturmaterial som i grunden består av cement och krossad marmor. Cementen kan pigmenteras i vilken "
     "färg som helst och man kan blanda in glaskross och lägga in detaljer i marmor, mässing eller aluminium."),
    ("Hur tjockt blir ett platsgjutet golv?",
     "Terrazzon läggs 15 mm tjock med kornstorlekar upp till 12 mm. Betong och terrazzo ska tillsammans vara 75 mm."),
    ("Hur lång tid tar det?",
     "Arbetet delas grovt in i tre moment – läggning, grovslipning med spackling och finslipning – som i de flesta fall "
     "görs under tre olika dagar."),
    ("Går det att renovera ett gammalt terrazzogolv?",
     'Ja. Terrazzo går att slipa om och laga med samma material, och ni väljer själva finish: matt, halvblankt eller '
     'blankt. Läs mer under <a href="renovering.html">Renovering</a>.'),
    ("Kan jag få prover?",
     f'Ja, <a href="kontakt.html?typ={quote("Beställ prover")}#offert">beställ prover</a> så skickar vi dem till dig. '
     'Skriv gärna vilka kulörer du är intresserad av.'),
    ("Hur sköter jag golvet?",
     'Vid daglig städning används Steinfix 60, en pH-neutral natursåpa som skyddar impregneringen. Se '
     '<a href="dokument.html">skötselanvisningarna</a>.'),
]


def index():
    slides = "".join(f'<div class="slide{" on" if i == 0 else ""}">{img(n, a, lazy=i > 0)}</div>' for i, (n, a) in enumerate(HERO_SLIDES))
    trust = [(I_CLOCK, f"Sedan {C.FOUNDED}", "Grundat av Stig Hofling"), (I_DROP, f"{N_COLORS} egna kulörer", "Platsgjuten kollektion"),
             (I_LAYERS, "Platsgjutet och prefab", f"{N_TILES} plattkulörer"), (I_USERS, "Stora som små projekt", "Från idé till färdigt golv")]
    trust_html = "".join(f"<li>{i}<div><b>{a}</b><span>{b}</span></div></li>" for i, a, b in trust)
    cards = "".join(card(*c) for c in CARDS)
    strip_codes = [c for _, codes in C.COLLECTION for c in codes][::2][:36]
    strip = "".join(f'<li><img src="img/kulor/gmb-{c.lower()}-s.jpg" alt="" loading="lazy" width="240" height="240"></li>' for c in strip_codes)
    steps = "".join(f'<li><span class="n">{i + 1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(C.TERRAZZO_STEPS))
    history = "".join(f"<li><b>{y}</b><span>{t}</span></li>" for y, t in C.HISTORY)
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    main = f'''<section class="hero hero-home" aria-labelledby="hero-h">
  <div class="hero-bg slides" aria-hidden="false">{slides}</div>
  <div class="wrap hero-in">
    {eyebrow(f"Göteborg · sedan {C.FOUNDED}")}
    <h1 id="hero-h">Terrazzo med exceptionell slitstyrka och unik design</h1>
    <p class="hero-lead">Vi gjuter, slipar och renoverar terrazzogolv, trappor och ytor – och följer er från idé till färdigt, unikt golv.</p>
    <div class="btns">{samples_btn("btn-accent")}<a class="btn btn-light" href="platsgjuten-terrazzo.html#kollektion">Se färgkollektionen</a></div>
  </div>
</section>

<section class="trust" aria-label="I korthet"><ul class="wrap trust-in">{trust_html}</ul></section>

<section class="sec" aria-labelledby="intro-h">
  <div class="wrap split">
    <figure class="ph tall">{img("platsgjutet", "Platsgjuten terrazzo i flera färger med fält avdelade av trälister", "(min-width: 960px) 50vw, 100vw")}</figure>
    <div>
      {eyebrow("Göteborgs Mosaikbeläggningar AB")}
      <h2 id="intro-h">En tradition som funnits i tusentals år</h2>
      <p class="lead">{C.ABOUT[0]}</p>
      <p>{C.ABOUT[1]}</p>
      <div class="btns">{offer_btn(label="Berätta om ditt projekt", cls="btn-dark")}<a class="btn btn-ghost" href="om-oss.html">Om oss</a></div>
    </div>
  </div>
</section>

<section class="sec tint" id="tjanster" aria-labelledby="tj-h">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Det här gör vi")}<h2 id="tj-h">Terrazzo för golv, trappor, väggar och kök</h2></div>
    <ul class="cards">{cards}</ul>
    <div class="also"><span>Vi säljer och installerar också</span>{pills(OTHER[1:])}</div>
  </div>
</section>

<section class="sec dark kollektion-band" aria-labelledby="kol-h">
  <div class="wrap split">
    <div>
      {eyebrow("Egen kollektion")}
      <h2 id="kol-h">{N_COLORS} kulörer – eller den du inte visste att du önskade</h2>
      <p class="lead">{C.COLLECTION_INTRO}</p>
      <div class="btns"><a class="btn btn-light" href="platsgjuten-terrazzo.html#kollektion">Utforska kollektionen</a>{samples_btn("btn-outline-light")}</div>
    </div>
    <ul class="strip" aria-hidden="true">{strip}</ul>
  </div>
</section>

<section class="sec" aria-labelledby="pr-h">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Så läggs ett platsgjutet golv")}<h2 id="pr-h">Tre moment, oftast tre dagar</h2></div>
    <ol class="steps">{steps}</ol>
  </div>
</section>

<section class="sec tint" aria-labelledby="re-h">
  <div class="wrap split rev">
    <figure class="ph">{img("fore-efter", "Före och efter: terrazzogolv vid en trappa som lagats och slipats", "(min-width: 960px) 50vw, 100vw")}</figure>
    <div>
      {eyebrow("Renovering")}
      <h2 id="re-h">Terrazzo går att slipa och laga – i stället för att bytas ut</h2>
      <p class="lead">{C.RENO_INTRO}</p>
      <ul class="ticks">{"".join(f"<li><b>{t}</b> {s}</li>" for t, s, *_ in C.RENO_SERVICES)}</ul>
      <div class="btns"><a class="btn btn-dark" href="renovering.html">Renovering och projekt</a></div>
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="hi-h">
  <div class="wrap split">
    <div>
      {eyebrow("Familjeföretag")}
      <h2 id="hi-h">Över femtio år av terrazzo i Göteborg</h2>
      <p class="lead">{C.ABOUT[2]}</p>
      <ol class="timeline">{history}</ol>
    </div>
    <figure class="ph">{img("logga-gbg-3", "Älvsborgsbron och texten Göteborgs ingjutet i terrazzo", "(min-width: 960px) 50vw, 100vw")}</figure>
  </div>
</section>

<section class="sec tint" aria-labelledby="dk-h">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Dokumentation")}<h2 id="dk-h">Installation, renovering och skötsel</h2></div>
    <div class="doc-grid">{docs_list()}</div>
  </div>
</section>

<section class="sec" id="fragor" aria-labelledby="fq-h">
  <div class="wrap narrow">
    <div class="sec-head">{eyebrow("Vanliga frågor")}<h2 id="fq-h">Bra att veta om terrazzo</h2></div>
    <div class="faq">{faq}</div>
  </div>
</section>

{cta_band()}

<section class="map" aria-label="Karta">
  <iframe src="{C.MAP_EMBED}" title="Karta: {C.ADDR}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</section>'''
    page("index.html", f"Terrazzo och mosaik i Göteborg sedan {C.FOUNDED} | {C.NAME}",
         f"{C.NAME} – platsgjuten och prefabricerad terrazzo, renovering och golvvård i Göteborg sedan {C.FOUNDED}. "
         f"Ring {C.PHONE}.", main, home=True)


# --- Undersidor -----------------------------------------------------------------------------------------------------
def platsgjuten():
    steps = "".join(f'<li><span class="n">{i + 1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(C.TERRAZZO_STEPS))
    main = page_hero("Platsgjuten terrazzo", "Lättstädat, fogfritt och slitstarkt – gjutet på plats i det mönster och den kulör ni väljer.",
                     "hero-restaurang", crumbs(("Terrazzo", "platsgjuten-terrazzo.html"), ("Platsgjuten terrazzo", "")),
                     samples_btn("btn-accent") + offer_btn("Platsgjuten terrazzo", cls="btn-light"),
                     "Restaurang med mönstergolv i platsgjuten terrazzo") + f'''
<section class="sec">
  <div class="wrap split">
    <div class="prose">
      <h2>Ett golv som håller i generationer</h2>
      {"".join(f"<p>{p}</p>" for p in C.TERRAZZO_TEXT)}
      <p>Vi utför även inredningsdetaljer i terrazzo som bord och sittmöbler, allt efter kundens önskemål.</p>
    </div>
    <aside class="factbox">
      <h3>Fakta</h3>
      {specs(C.TERRAZZO_SPECS)}
      <p class="small"><a href="dokument/gbgmosaik-installation-platsgjutet.pdf" target="_blank" rel="noopener">{I_PDF} Installationsanvisning (PDF)</a></p>
    </aside>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Arbetsgång")}<h2>Tre moment, oftast under tre olika dagar</h2><p>Slipningen görs med vatten.</p></div>
    <ol class="steps">{steps}</ol>
  </div>
</section>
<section class="sec" id="kollektion" aria-labelledby="kol-h">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Färgkollektion")}<h2 id="kol-h">{N_COLORS} kulörer i egen kollektion</h2><p>{C.COLLECTION_INTRO} Klicka på en kulör för att se den större och beställa prov.</p></div>
    {collection_explorer()}
  </div>
</section>
{cta_band("Hittar du inte rätt kulör?", "Vi tar gärna fram en egen kulör för ert projekt. Beställ prover eller ring oss, så hjälper vi dig vidare.")}'''
    page("platsgjuten-terrazzo.html", f"Platsgjuten terrazzo – {N_COLORS} kulörer | {C.NAME}",
         f"Platsgjutna terrazzogolv och trappor i Göteborg. Fogfritt, slitstarkt och reparerbart. Egen kollektion med {N_COLORS} kulörer.",
         main, "platsgjuten-terrazzo", "hero-restaurang")


def plattor():
    uses = [("plattor", "Golv- och väggplattor", "Badrum med mönsterlagt golv av terrazzoplattor"),
            ("fasad", "Fasad", "Kontorshus med fasad i ljusa terrazzoplattor"),
            ("trappa", "Trappbeklädnad", "Trappa beklädd med ljus terrazzo")]
    use_html = "".join(f'<li><figure class="ph">{img(n, a, "(min-width: 960px) 33vw, 100vw")}</figure><h3>{t}</h3></li>' for n, t, a in uses)
    main = page_hero("Golv-, vägg- och fasadplattor", "Prefabricerad terrazzo för golv, väggar, fasader och trappor – i tre färggrupper.",
                     "plattor", crumbs(("Terrazzo", "platsgjuten-terrazzo.html"), ("Terrazzoplattor", "")),
                     samples_btn("btn-accent") + offer_btn("Terrazzoplattor", cls="btn-light"),
                     "Badrum med mönsterlagt golv av terrazzoplattor") + f'''
<section class="sec">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Användning")}<h2>Samma kollektion – golv, vägg, fasad och trappa</h2></div>
    <ul class="uses">{use_html}</ul>
  </div>
</section>
<section class="sec tint" id="farger">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Kulörer")}<h2>Färggrupper för plattor</h2><p>Klicka på en platta för att se den större. Vissa kulörer har en minimumorder på 100 m².</p></div>
    {tiles(["Färggrupp 3", "Färggrupp 5", "Färggrupp 7"])}
  </div>
</section>
<section class="sec">
  <div class="wrap split">
    <div class="prose">
      <h2>Installation av terrazzoplattor</h2>
      {"".join(f"<p>{p}</p>" for p in C.TILE_INSTALL)}
      <p><a href="dokument/installation-terrazzoplattor.pdf" target="_blank" rel="noopener">{I_PDF} Installationsanvisning (PDF, svenska och engelska)</a></p>
    </div>
    <aside class="factbox"><h3>Tänk på</h3><ul class="ticks">{"".join(f"<li>{t}</li>" for t in C.TILE_TIPS)}</ul></aside>
  </div>
</section>
{cta_band()}'''
    page("terrazzoplattor.html", f"Terrazzoplattor för golv, vägg och fasad | {C.NAME}",
         "Prefabricerade terrazzoplattor för golv, väggar, fasader och trappbeklädnad. Se färggrupperna och beställ prover.",
         main, "terrazzoplattor", "plattor")


def bankskivor():
    main = page_hero("Bänkskivor och fönsterbänkar", "Terrazzo i köket, badrummet och fönstret – med en egen färggrupp för skivor.",
                     "bankskiva", crumbs(("Terrazzo", "platsgjuten-terrazzo.html"), ("Bänkskivor", "")),
                     samples_btn("btn-accent") + offer_btn("Bänkskiva / fönsterbänk", cls="btn-light"),
                     "Kök med bänkskiva i mörk terrazzo") + f'''
<section class="sec tint" id="farger">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Kulörer")}<h2>Färggrupper för bänkskivor och fönsterbänkar</h2><p>Färggrupp 8 finns bara för skivor. Klicka på en kulör för att se den större.</p></div>
    {tiles(["Färggrupp 8", "Färggrupp 3", "Färggrupp 5", "Färggrupp 7"])}
  </div>
</section>
<section class="sec">
  <div class="wrap split">
    <div class="prose">
      <h2>Skötsel av bänkskivan</h2>
      {"".join(f"<p>{p}</p>" for p in C.BENCH_CARE)}
      <p><a href="dokument/bankskiva-av-terrazzo.pdf" target="_blank" rel="noopener">{I_PDF} Skötselanvisning (PDF, svenska och engelska)</a></p>
    </div>
    <figure class="ph">{img("steinfix", "Golvvård med Steinfix", "(min-width: 960px) 50vw, 100vw")}</figure>
  </div>
</section>
{cta_band()}'''
    page("bankskivor.html", f"Bänkskivor och fönsterbänkar i terrazzo | {C.NAME}",
         "Bänkskivor och fönsterbänkar i terrazzo med egen färggrupp. Se kulörerna och läs om skötseln.", main, "bankskivor", "bankskiva")


def loggor():
    items = [(n, a, a) for n, a in C.GALLERY]
    main = page_hero("Loggor och konst i terrazzo", "Vi kan tillverka er logga i terrazzo enligt era önskemål – inlagd i golvet, utskuren eller som ett eget konstverk.",
                     "logga-salvatori", crumbs(("Terrazzo", "platsgjuten-terrazzo.html"), ("Loggor och konst", "")),
                     offer_btn("Logga eller konst", "Berätta om din idé", "btn-accent") + call_btn("btn-light"),
                     "Marco Salvatoris logga i terrazzo") + f'''
<section class="sec">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Urval")}<h2>Loggor, mönster och motiv</h2><p>Från företagsloggor i entrégolv till Göteborgs siluett i sten. Klicka för att se bilderna större.</p></div>
    {gallery(items)}
  </div>
</section>
{cta_band("Vill ni ha er logga i terrazzo?", "Kontakta oss med logga, mått och plats så berättar vi hur vi kan göra den.")}'''
    page("loggor-och-konst.html", f"Loggor och konst i terrazzo | {C.NAME}",
         "Företagsloggor, mönster och konst i terrazzo – inlagt i golv eller utskuret. Göteborgs Mosaikbeläggningar AB.",
         main, "loggor-och-konst", "logga-salvatori")


def renovering():
    fin = "".join(f'<li><h3>{t}</h3><p class="grit">{g}</p><p>{d}</p></li>' for t, g, d in C.FINISHES)
    svc = "".join(f'<li class="svc"><h3>{t}</h3><p class="grit">{s}</p><p>{d}</p>'
                  f'<a href="dokument/{f}" target="_blank" rel="noopener">{I_PDF} Läs mer (PDF)</a></li>' for t, s, d, f in C.RENO_SERVICES)
    proj = "".join(f'<li><button type="button" class="gal" data-lb="img/foto/reno-{i + 1:02d}.jpg" data-caption="{E(t)} – {E(d)}">'
                   f'{img(f"reno-{i + 1:02d}", f"{t}: {d}", "(min-width: 960px) 25vw, 50vw")}</button>'
                   f'<p><span class="n">{i + 1}</span><b>{t}</b> {d}</p></li>' for i, (_, t, d) in enumerate(C.PROJECT_STEPS))
    main = page_hero("Renovering av terrazzo och natursten", C.RENO_INTRO, "fore-efter",
                     crumbs(("Renovering", "")), offer_btn("Renovering, slipning eller lagning", cls="btn-accent") + call_btn("btn-light"),
                     "Före och efter: lagat och slipat terrazzogolv vid en trappa") + f'''
<section class="sec">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Tjänster")}<h2>Slipning, lagning och grovrengöring</h2></div>
    <ul class="svcs">{svc}</ul>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Ytfinish")}<h2>Ni väljer själva hur ert ”nya” golv ska se ut</h2></div>
    <ul class="finishes">{fin}</ul>
  </div>
</section>
<section class="sec" aria-labelledby="pj-h">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Projekt · reparation och restaurering")}<h2 id="pj-h">{C.PROJECT_TITLE}</h2><p>{C.PROJECT_INTRO}</p></div>
    <ol class="project">{proj}</ol>
  </div>
</section>
<section class="sec tint">
  <div class="wrap split">
    <div class="prose">
      <h2>Skydda golvet efter renoveringen</h2>
      <p>Skrapmattor i entrén hindrar smuts och väta från att dras in, och taktila ledstråk och kontrastmarkeringar kan läggas in i samband med renoveringen. Vi är återförsäljare av Steinfix och guidar er till rätt golvvårdsprodukter.</p>
      <div class="btns">{pills(OTHER)}</div>
    </div>
    <figure class="ph">{img("torkzon", "Entré med torkmatta framför en karusselldörr", "(min-width: 960px) 50vw, 100vw")}</figure>
  </div>
</section>
{cta_band("Behöver ert golv en ny lyster?", "Berätta om golvet eller trappan, så föreslår vi slipning, lagning eller grovrengöring.")}'''
    page("renovering.html", f"Renovering, slipning och lagning av terrazzo | {C.NAME}",
         "Slipning, lagning och grovrengöring av terrazzo och natursten. Matt, halvblank eller blank finish. Se ett renoveringsprojekt steg för steg.",
         main, "renovering", "fore-efter")


def torkzoner():
    blocks = []
    for i, (name, photos, rows) in enumerate(C.MATS):
        items = [(p[:-4], f"Kåbe {name}", f"Kåbe {name}") for p in photos]
        blocks.append(f'''<article class="mat{' rev' if i % 2 else ''}" id="kabe-{i + 1}">
  <div>{gallery(items, "mini")}</div>
  <div><h3>Kåbe {name}</h3>{specs(rows, "compact")}</div>
</article>''')
    nav = "".join(f'<a class="pill" href="#kabe-{i + 1}">Kåbe {n}</a>' for i, (n, *_) in enumerate(C.MATS))
    main = page_hero("Torkzoner – Kåbe skrapgaller och torkmattor", C.MATS_INTRO.split(". ")[0] + ".", "torkzon",
                     crumbs(("Produkter", "torkzoner.html"), ("Torkzoner", "")),
                     offer_btn("Torkzoner", cls="btn-accent") + call_btn("btn-light"), "Entré med torkmatta framför en karusselldörr") + f'''
<section class="sec">
  <div class="wrap narrow prose"><p class="lead">{C.MATS_INTRO}</p><div class="btns">{nav}</div></div>
</section>
<section class="sec tint"><div class="wrap mats">{"".join(blocks)}</div></section>
{cta_band("Behöver entrén en ny torkzon?", "Ge oss en ritning eller mall, så tar vi fram en måttbeställd matta i nästan vilken form som helst.")}'''
    page("torkzoner.html", f"Torkzoner och skrapmattor – Kåbe | {C.NAME}",
         "Kåbe Originalmatta – skrapgaller och torkmatta i ett, måttbeställd för entréer. Återförsäljare och installation i Göteborg.",
         main, "torkzoner", "torkzon")


def taktila():
    items = [(f"tm-rostfritt-{n}", f"Taktil markering i rostfritt stål, exempel {n}", f"Rostfritt stål – exempel {n}") for n in range(1, 5)]
    main = page_hero("Taktila markeringar", "Kontrastmarkeringar och taktila ledstråk som gör det lättare för synskadade att hitta rätt.",
                     "taktila", crumbs(("Produkter", "torkzoner.html"), ("Taktila markeringar", "")),
                     offer_btn("Taktila markeringar", cls="btn-accent") + call_btn("btn-light"), "Taktila ledstråk i ett stengolv") + f'''
<section class="sec">
  <div class="wrap split">
    <div class="prose">
      <h2>Ledstråk i rostfritt stål</h2>
      {"".join(f"<p>{p}</p>" for p in C.TACTILE_TEXT)}
      <p><b>Önskar du en specialversion eller hjälp med installationen?</b> <a href="kontakt.html?typ={quote("Taktila markeringar")}#offert">Kontakta oss!</a></p>
    </div>
    <aside class="factbox"><h3>Material</h3><ul class="ticks">{"".join(f"<li>{t}</li>" for t in C.TACTILE_TYPES)}</ul></aside>
  </div>
</section>
<section class="sec tint"><div class="wrap"><div class="sec-head"><h2>Rostfritt stål</h2></div>{gallery(items, "four")}</div></section>
{cta_band()}'''
    page("taktila-markeringar.html", f"Taktila markeringar och ledstråk | {C.NAME}",
         "Taktila ledstråk och kontrastmarkeringar i rostfritt stål, mässing och aluminium för golv och trappor.",
         main, "taktila-markeringar", "taktila")


def steinfix():
    prods = "".join(f'<li class="prod"><img src="img/steinfix/{nr}.png" alt="Steinfix {nr}" loading="lazy" width="480" height="480">'
                    f'<div><h3>Steinfix {nr}</h3><p class="grit">{t}</p><ul class="ticks">{"".join(f"<li>{b}</li>" for b in bs)}</ul></div></li>'
                    for nr, t, bs in C.STEINFIX)
    deep = "".join(f"<li>{s}</li>" for s in C.DEEP_CLEAN)
    main = page_hero("Steinfix golvvård", "Vi är återförsäljare av Steinfix. Vi guidar er till rätt produkt för att underhålla golv och trappor av sten och terrazzo.",
                     "steinfix", crumbs(("Produkter", "torkzoner.html"), ("Steinfix", "")),
                     offer_btn("Steinfix-produkter", "Fråga om produkterna", "btn-accent") + call_btn("btn-light"), "Golv som moppas med Steinfix 60") + f'''
<section class="sec"><div class="wrap"><ul class="prods">{prods}</ul></div></section>
<section class="sec tint">
  <div class="wrap split">
    <div class="prose"><h2>Djuprengöring med Steinfix 40</h2><ol class="numlist">{deep}</ol><p>Impregnera därefter, till exempel med Steinfix 100 eller Steinfix 60.</p></div>
    <div><h2 class="h3">Skötselanvisningar</h2>{docs_list(["Skötselanvisningar"])}</div>
  </div>
</section>
{cta_band("Osäker på vilken produkt du behöver?", "Kontakta oss så guidar vi dig till rätt sorts produkt för rätt ändamål.")}'''
    page("steinfix.html", f"Steinfix – rengöring och impregnering av sten | {C.NAME}",
         "Steinfix 10–100: fläckborttagning, grovrengöring, natursåpa och impregnering för natursten, betong och terrazzo.",
         main, "steinfix", "steinfix")


def dokument():
    main = page_hero("Dokument och skötsel", "Installationsanvisningar, renovering, skötsel och byggvarudeklaration att ladda ner.",
                     "dokument", crumbs(("Dokument", "")), call_btn() + offer_btn(cls="btn-light"), "Pärmar med dokument") + f'''
<section class="sec"><div class="wrap"><div class="doc-grid">{docs_list()}</div></div></section>
{cta_band()}'''
    page("dokument.html", f"Dokument och skötselanvisningar | {C.NAME}",
         "Ladda ner installationsanvisningar, skötselanvisningar och byggvarudeklaration för terrazzo.", main, "dokument", "dokument")


def om_oss():
    history = "".join(f"<li><b>{y}</b><span>{t}</span></li>" for y, t in C.HISTORY)
    main = page_hero("Om Göteborgs Mosaikbeläggningar", f"Ett familjeföretag som har arbetat med terrazzo sedan {C.FOUNDED}.",
                     "hero-stentrappa", crumbs(("Om oss", "")), call_btn() + offer_btn(cls="btn-light"),
                     "Spiraltrappa i ljus terrazzo sedd uppifrån") + f'''
<section class="sec">
  <div class="wrap split">
    <div class="prose">{"".join(f"<p{' class=lead' if i == 0 else ''}>{p}</p>" for i, p in enumerate(C.ABOUT))}</div>
    <aside class="factbox"><h3>Historia</h3><ol class="timeline">{history}</ol></aside>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <div class="sec-head">{eyebrow("Det här gör vi")}<h2>Våra områden</h2></div>
    <ul class="cards">{"".join(card(*c) for c in CARDS)}</ul>
  </div>
</section>
{cta_band()}'''
    page("om-oss.html", f"Om oss – terrazzo sedan {C.FOUNDED} | {C.NAME}",
         f"Göteborgs Mosaikbeläggningar grundades {C.FOUNDED} av Stig Hofling och drivs sedan 2011 av Andreas Hofling.",
         main, "om-oss", "hero-stentrappa")


def quote_form():
    opts = "".join(f"<option>{E(t)}</option>" for t in WORK_TYPES)
    req = '<span class="req" aria-hidden="true">*</span>'
    return f'''<form class="form" id="qform" novalidate data-endpoint="https://formsubmit.co/ajax/{C.FORM_EMAIL}">
  <div class="row2">
    <p class="field"><label for="f-typ">Vad gäller det?</label><select id="f-typ" name="Typ"><option value="">– Välj –</option>{opts}</select></p>
    <p class="field"><label for="f-kulor">Kulörer eller artiklar</label><input id="f-kulor" name="Kulörer" placeholder="T.ex. GMB-RAPS, GMB-3-15"></p>
  </div>
  <div class="row2">
    <p class="field"><label for="f-namn">Namn{req}</label><input id="f-namn" name="Namn" autocomplete="name" required><span class="err" id="e-namn" hidden>Skriv ditt namn.</span></p>
    <p class="field"><label for="f-foretag">Företag</label><input id="f-foretag" name="Företag" autocomplete="organization"></p>
  </div>
  <div class="row2">
    <p class="field"><label for="f-tel">Telefon{req}</label><input id="f-tel" name="Telefon" type="tel" autocomplete="tel"><span class="err" id="e-tel" hidden>Skriv telefonnummer eller e-post.</span></p>
    <p class="field"><label for="f-epost">E-post</label><input id="f-epost" name="E-post" type="email" autocomplete="email"><span class="err" id="e-epost" hidden>Kontrollera e-postadressen.</span></p>
  </div>
  <p class="field" id="adr-field"><label for="f-adr">Adress för prover</label><input id="f-adr" name="Adress" autocomplete="street-address" placeholder="Gata, postnummer och ort"></p>
  <p class="field"><label for="f-besk">Berätta om projektet</label><textarea id="f-besk" name="Beskrivning" rows="5" placeholder="Var, ungefär hur stor yta och när?"></textarea></p>
  <p class="hp" aria-hidden="true"><label for="f-web">Lämna tomt</label><input id="f-web" name="_honey" tabindex="-1" autocomplete="off"></p>
  <p class="small">{req} Telefon eller e-post räcker. Uppgifterna används bara för att svara dig.</p>
  <p><button class="btn btn-dark" type="submit">Skicka</button></p>
  <p class="send-err" id="send-err" role="alert" hidden>Det gick inte att skicka just nu. Försök igen, ring <a href="tel:{C.TEL}">{C.PHONE}</a> eller mejla <a href="mailto:{C.EMAIL}">{C.EMAIL}</a>.</p>
</form>
<div class="done" id="qdone" tabindex="-1" hidden>
  <p class="done-h">Tack! Vi har fått ditt meddelande.</p>
  <p>Vi hör av oss så snart vi kan. Brådskar det, ring <a href="tel:{C.TEL}">{C.PHONE}</a>.</p>
  <p><button class="link" type="button" id="qagain">Skicka ett nytt meddelande</button></p>
</div>'''


def kontakt():
    social = "".join(f'<a class="pill" href="{u}" target="_blank" rel="noopener">{SOCIAL_ICON[n]}{n}</a>' for n, u in C.SOCIAL)
    main = f'''<section class="sec page-top">
  <div class="wrap">
    {crumbs(("Kontakt", ""))}
    <div class="contact">
      <div>
        <h1>Kontakta oss</h1>
        <p class="lead">Ring, mejla eller fyll i formuläret för frågor, prover eller om ni vill boka tid för ett möte.</p>
        <ul class="contact-list">
          <li>{I_PHONE}<div><b>Telefon</b><a href="tel:{C.TEL}">{C.PHONE}</a></div></li>
          <li>{I_MAIL}<div><b>E-post</b><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></div></li>
          <li>{I_PIN}<div><b>Adress</b><a href="{C.MAPS_LINK}" target="_blank" rel="noopener">{C.STREET}, {C.POSTAL} {C.CITY}</a></div></li>
        </ul>
        <p class="label">Följ oss</p>
        <div class="btns">{social}</div>
      </div>
      <div class="form-card" id="offert">
        <h2>Skicka en förfrågan eller beställ prover</h2>
        {quote_form()}
      </div>
    </div>
  </div>
</section>
<section class="map" aria-label="Karta">
  <iframe src="{C.MAP_EMBED}" title="Karta: {C.ADDR}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</section>'''
    page("kontakt.html", f"Kontakt och beställ prover | {C.NAME}",
         f"Kontakta {C.NAME}: {C.PHONE}, {C.EMAIL}. Beställ prover på terrazzo eller boka ett möte.", main, "kontakt")


def not_found():
    main = f'''<section class="sec page-top"><div class="wrap narrow"><h1>Sidan finns inte</h1>
<p class="lead">Sidan kan ha flyttats när hemsidan gjordes om.</p>
<div class="btns"><a class="btn btn-dark" href="index.html">Till startsidan</a>{call_btn()}</div></div></section>'''
    page("404.html", f"Sidan finns inte | {C.NAME}", "Sidan kunde inte hittas.", main)


def seo_files():
    urls = ["index.html"] + [f"{s}.html" for s, *_ in TERRAZZO + [RENO] + OTHER] + ["dokument.html", "om-oss.html", "kontakt.html"]
    locs = "".join(f"<url><loc>{C.SITE_URL}{'' if u == 'index.html' else u}</loc></url>" for u in urls)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{locs}</urlset>\n', encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {C.SITE_URL}sitemap.xml\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f in (index, platsgjuten, plattor, bankskivor, loggor, renovering, torkzoner, taktila, steinfix, dokument, om_oss,
              kontakt, not_found):
        f()
    seo_files()
    print("Byggde", len(list(OUT.glob("*.html"))), "sidor i", OUT)
