# Göteborgs Mosaikbeläggningar AB – ny webbplats

Ny webbplats för [Göteborgs Mosaikbeläggningar AB](https://www.gbgmosaik.se/) (terrazzo och mosaik sedan 1970).
All text, alla bilder och PDF:er är skrapade från nuvarande gbgmosaik.se och företagets egna PDF:er.

Sajten är en mix av hantverkarsajterna i Elevate Studios repon:

| Från | Vad |
| --- | --- |
| S-Bygg, Antonsson, Ohan | Python-generatorn (`scripts/build.py` → `docs/`), runda piller-knappar, FAQ, offertformulär via FormSubmit med `?typ=` från undersidorna |
| Kungsbacka Mark & Trädgård | Mörk inforad överst, helskärms-hero med verksamhetsrad, filter (här för färgkollektionen), faktablad (Kåbe-mattorna), bildvisning |
| Ängö Entreprenad | Outfit + DM Sans, flersidig struktur med projektsida (renoveringsprojektet steg för steg) |
| JJ El | Stor, stram typografi, mörkt band, arbetsgången i numrerade steg, mjuk inflygning (av vid `prefers-reduced-motion`) |
| Appelgrens Elektriska | Skrapskriptet som hämtar text och bilder från den gamla hemsidan |

Färgerna kommer från materialet: varm terrazzovit botten med diskreta ”stänk”, loggans grafit och terrakotta
(Marco Salvatori-loggan och restaurangbilden) som accent.

## Sidor

Allt ligger i [`docs/`](docs/) – öppna `docs/index.html` i en webbläsare.

- `index.html` – startsidan: bildspel med de fem bakgrundsbilderna från gamla sajten, förtroenderad, om oss,
  tjänstekort, kollektionsband, arbetsgång, renovering, historia, dokument, vanliga frågor, karta
- `platsgjuten-terrazzo.html` – text, fakta och **hela färgkollektionen (87 kulörer)** med filter och bildvisning
- `terrazzoplattor.html` – golv-, vägg-, fasad- och trappplattor (gamla sajtens fyra sidor hade samma katalog),
  färggrupp 3, 5 och 7 med minimumorder, installationsråd
- `bankskivor.html` – färggrupp 8 + övriga, skötselråd från PDF:en
- `loggor-och-konst.html` – loggor och konst i terrazzo
- `renovering.html` – slipning, lagning, grovrengöring, ytfinisher och projektet med 11 bilder
- `torkzoner.html`, `taktila-markeringar.html`, `steinfix.html` – produkterna med specifikationer
- `dokument.html` – alla PDF:er, `om-oss.html`, `kontakt.html` (formulär + beställ prover), `404.html`

Varje kulör i bildvisningen har knappen ”Beställ prov på kulören”, som öppnar formuläret med kulören ifylld.

## Ändra text eller bygga om

```bash
python3 scripts/skrapa.py     # hämtar text (skrapat/text/) och originalfiler (skrapat/original/, inte incheckad)
python3 scripts/bilder.py     # gör webbversioner till docs/img/ och kopierar PDF:erna till docs/dokument/ (kräver Pillow)
python3 scripts/build.py docs # bygger sidorna
```

All text och alla uppgifter finns i `scripts/innehall.py`; layouten i `scripts/build.py`, `docs/assets/site.css`
och `docs/assets/site.js`. Ändra aldrig HTML-filerna i `docs/` direkt – de skrivs över.

## Fakta och förslag – gå igenom före lansering

**Från gbgmosaik.se:** namn, telefon 070-719 02 64, info@gbgmosaik.se, sociala medier, alla texter om terrazzo,
historiken (1970 Stig Hofling, 2011 Andreas Hofling, i branschen sedan 1999), kollektionen och plattorna med
minimumorder, Kåbe- och Steinfix-specifikationerna, taktila markeringar, renoveringsprojektet och alla bilder.

**Behöver bekräftas:**

- **Adressen.** Kartlänken på startsidan pekar på *Transportgatan 37, 422 46 Hisings Backa* och används.
  De äldre undersidorna och broschyren anger *Södra Ågatan 20, Mölndal*, 031-24 20 02 och öppettider
  mån–fre 10–14 – det ser ut som gamla uppgifter och visas inte.
- **Formuläret** skickar via [FormSubmit](https://formsubmit.co) till Elevate Studio under förhandsvisningen. Byt
  `FORM_EMAIL` i `scripts/innehall.py` till info@gbgmosaik.se vid lansering (första förfrågan skickar ett
  aktiveringsmejl).
- Korta texter som vi har skrivit utifrån sajtens innehåll: rubriker, ingresser, korttexterna, frågorna i ”Vanliga
  frågor” (svaren bygger på sajtens och PDF:ernas text) och beskrivningarna av de tre arbetsmomenten.
- Inga certifieringar, priser, kundomdömen eller antal anställda anges.

**Saknas på gamla sajten:** sidan ”Skulptur och konst” ger 404 (bilderna används på Loggor och konst), broschyren
*Platsgjuten Terrazzo* (PDF) är trasig och länken *Prefabricerad Terrazzo* ger 404 – båda är utelämnade tills nya
filer finns. Sidan ”Kakel och klinker” (`/17/58/`) länkas inte från startsidan och är inte med.

## Publicera med GitHub Pages

Settings → Pages → Branch: `main`, mapp: `/docs` → Save. Byt `SITE_URL` i `scripts/innehall.py` om sajten
flyttas till gbgmosaik.se.
