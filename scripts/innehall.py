"""Innehåll för Göteborgs Mosaikbeläggningar AB – används av build.py (sidorna) och bilder.py (bilderna).

All text här kommer från www.gbgmosaik.se och företagets egna PDF:er (se skrapat/text/ och docs/dokument/),
om inget annat står vid raden. Rader märkta FÖRSLAG är skrivna av oss och bör bekräftas av företaget.
"""

# --- Företaget (gbgmosaik.se) --------------------------------------------------------------------------------------
NAME = "Göteborgs Mosaikbeläggningar AB"
SHORT = "Göteborgs Mosaik"
PHONE, TEL = "070-719 02 64", "+46707190264"
EMAIL = "info@gbgmosaik.se"
# Kartlänken på startsidan pekar på Transportgatan 37. De äldre undersidorna och broschyren anger Södra Ågatan 20,
# Mölndal och 031-24 20 02 – det ser ut som gamla uppgifter och används inte. Bekräfta adressen före lansering.
STREET, POSTAL, CITY = "Transportgatan 37", "422 46", "Hisings Backa"
ADDR = f"{STREET}, {POSTAL} {CITY}"
MAPS_LINK = "https://goo.gl/maps/Wo6gWDYdKcR5Pkze8"
MAP_EMBED = "https://www.google.com/maps?q=Transportgatan+37,+422+46+Hisings+Backa&z=15&hl=sv&output=embed"
SOCIAL = [
    ("Instagram", "https://www.instagram.com/goteborgsmosaikbelaggningar/"),
    ("Facebook", "https://www.facebook.com/G%C3%B6teborgs-Mosaikbel%C3%A4ggningar-AB-913308815442884/"),
    ("LinkedIn", "https://www.linkedin.com/company/33471306/"),
]
FOUNDED = 1970

# Formuläret skickar via FormSubmit. Under förhandsvisningen går förfrågningarna till Elevate Studio – byt till
# info@gbgmosaik.se vid lansering (första förfrågan till en ny adress skickar bara ett aktiveringsmejl).
FORM_EMAIL = "elevate.studio018@gmail.com"
SITE_URL = "https://elevatestudio018.github.io/GBG-mosaik/"

# --- Om oss (startsidan på gbgmosaik.se, ordagrant) ---------------------------------------------------------------
ABOUT = [
    "Göteborgs mosaikbeläggningar AB erbjuder stora möjligheter att skapa miljövänliga terrazzogolv med exceptionell "
    "slitstyrka och unik design. Vi arbetar främst med platsgjutna golv där vi har tagit fram en egen kollektion med "
    "stor variation av färger under åren.",
    "Inga projekt är för stora eller för små. Vi följer er från idé till färdigt unikt golv. Vi vänder oss främst till "
    "arkitekter, byggherrar, konstnärer och designers men tar även emot beställningar från privatpersoner.",
    "Vi besitter en bred kompetens gällande terrazzo då vi har en lång erfarenhet som sträcker sig till 1970 då "
    "företaget grundades av Stig Hofling. År 2011 fick företaget ny regi i form av Andreas Hofling som tog över "
    "rodret. Andreas har varit verksam i branschen sedan 1999.",
    "Oavbrutet utvecklar och förbättrar vi en gammal tradition som funnits i tusentals år för att bevara ett unikt "
    "hantverk. I samarbete med oss blir du en del av denna tradition, samtidigt som du får ett golv som är unikt.",
]
HISTORY = [
    ("1970", "Stig Hofling grundar Göteborgs Mosaikbeläggningar."),
    ("1999", "Andreas Hofling börjar i branschen."),
    ("2011", "Andreas Hofling tar över rodret."),
    ("I dag", "Platsgjutet, prefabricerat och renovering – med en egen färgkollektion."),
]

# --- Platsgjuten terrazzo (17/3/platsgjuten-terrazzo) -------------------------------------------------------------
TERRAZZO_TEXT = [
    "Terrazzo är ett slipbart naturmaterial som i sin grund består av cement och krossad marmor. Uttrycksmöjligheterna "
    "är oändliga då det finns stora möjligheter att jobba konstnärligt med mönster och olika färgkombinationer. Cementen "
    "går att pigmentera i vilken färg som helst och marmorkross finns i en mängd olika färger och storlekar. Utöver det "
    "kan man blanda in glaskross i olika färger och lägga in dekorativa detaljer i form av ren marmor, mässing eller "
    "aluminium.",
    "En trappa eller ett golv av terrazzo är lättstädat, fogfritt och slitstarkt. Det är ett skönt golv att gå på och "
    "passar med alla övriga material inredningsmässigt. Betongbjälklagets värmekapacitet nyttjas effektivt vilket ger "
    "svalare klimat sommartid och energibesparingar vintertid.",
    "Terrazzo är även reparerbart och slipbart vilket gör att det är lätt att bevara nykänslan på. Vid renoveringar är "
    "det ofta det material som bevaras medan andra ytskikt byts ut.",
]
TERRAZZO_SPECS = [
    ("Material", "Cement och krossad marmor, ev. glaskross"),
    ("Kornstorlek", "Upp till 12 mm som standard"),
    ("Tjocklek", "15 mm terrazzo, totalt 75 mm med betongen"),
    ("Underlag", "Träskurad, brädriven eller borstad betong av god hållfasthet"),
    ("Fältstorlek", "Högst 2 × 2 m, längd högst 1,5 × rutans bredd"),
    ("Foglister", "Plast, marmorstavar, aluminium eller mässing"),
]
TERRAZZO_STEPS = [
    ("Läggning", "Terrazzon gjuts på plats med foglister i det mönster ni valt."),
    ("Grovslipning och spackling", "Ytan slipas fram och porer spacklas."),
    ("Finslipning", "Slipningen görs med vatten till önskad finish."),
]
COLLECTION_INTRO = ("Följande kollektion är skapad av Andreas Hofling och Erik ”Professorn” Tobiasson. Vi kan även "
                    "hjälpa er att ta fram just den kulör ni kanske inte ens visste att ni önskade.")
# Grupp -> kulörer. Bilden är files/GMB-<KOD>.jpg på gbgmosaik.se.
COLLECTION = [
    ("Färgskala", ["LIMEGRON", "RAPS", "GUL", "APRIKOS", "ORANGE", "ROD", "LILA", "LAVENDEL", "BLA", "ISBLA", "MARIN",
                   "GRON", "LJUSGRA", "MELLANGRA", "MORKGRA", "SVART", "VIT"]),
    ("Camo", ["CAMO-VIT", "CAMO-GRA", "CAMO-SVART", "CAMO-GRON", "BETONG-1", "BETONG-2", "BETONG-3", "BETONG-4"]),
    ("Returglas", ["RETUR-VIT", "RETUR-GUL", "RETUR-ROD", "RETUR-BLA", "RETUR-GRON", "RETUR-SVART"]),
    ("Industri", ["ST-PETERSBURG", "BERLIN", "ODESSA"]),
    ("Karibien", ["BAHAMAS", "BERMUDA", "ARUBA", "JAMAICA"]),
    ("Saga", ["SNOVIT", "BALOO", "FERDINAND", "SIMBA", "NEMO", "POCAHONTAS", "ELSA", "SHREK"]),
    ("Natur", ["OKEN", "STAPP", "LAVA", "GLACIAR", "FJALL"]),
    ("Reptil", ["REPTIL-GUL", "REPTIL-ROD", "REPTIL-BLA", "REPTIL-GRON"]),
    ("Italienska öar", ["VULCANO", "LIPARI", "SALINA", "PANAREA", "STROMBOLI", "FILICUDI", "ALICUDI", "CAPRI",
                        "MONTECRISTO", "GORGONA", "SICILIEN", "PIANOSA", "GIGLIO", "CAPRAIA", "ISCHIA", "ELBA"]),
    ("Italienska städer", ["MILANO", "TURIN", "GENOVA", "VERONA", "VENEDIG", "PARMA", "FLORENS", "ROM", "BOLOGNA",
                           "SANSEPOLLRO", "BARI", "CATANIA", "TAORMINA", "MESSINA", "PALERMO", "NEAPEL"]),
]

# --- Prefabricerade plattor (17/4, 17/5, 17/6, 17/7) – samma färggrupper på alla fyra sidorna --------------------
# (kod, källfil på gbgmosaik.se, minimumorder)
_A = "assets/images/terrazzo-golv-vaggplattor/"
TILES = [
    ("Färggrupp 3", [
        ("GMB-3-01", "files/GMB-3-01.jpg", ""), ("GMB-3-05", _A + "cortina-09.jpg", ""),
        ("GMB-3-15", _A + "mantova-12.jpg", ""), ("GMB-3-16", _A + "brescia-12.jpg", ""),
        ("GMB-3-20", _A + "rovereto-09.jpg", ""), ("GMB-3-22", _A + "auronzo-09.jpg", ""),
        ("GMB-3-24", "files/GMB-3-24.jpg", "100 m²"), ("GMB-3-25", "files/GMB-3-25.jpg", "100 m²"),
        ("GMB-3-58", "files/asolo.jpg", "100 m²"),
    ]),
    ("Färggrupp 5", [(f"GMB-5-{n}", f"files/gmb-5-{n}.jpg" if n.startswith("82") else f"files/GMB-5-{n}.jpg", "")
                     for n in ("8210", "8220", "8230", "8240", "8250", "8260", "9420", "9432", "9202")]),
    ("Färggrupp 7", [(f"GMB-7-0{n}", f"{_A}gmb-7-0{n}.jpg", "") for n in range(1, 9)]),
    ("Färggrupp 8", [  # bara för bänkskivor och fönsterbänkar
        ("GMB-8-B7", _A + "gmb-8-b7.jpg", ""), ("GMB-8-C9", "files/GMB-8-C9.jpg", ""),
        ("GMB-8-C10", "files/GMB-8-C10.jpg", ""), ("GMB-8-C14", _A + "gmb-8-c14.jpg", ""),
    ] + [(f"GMB-8-{n}", f"files/GMB-8-{n}.jpg", "") for n in ("GS005", "GS008", "G4", "G18", "W7", "W8", "W9", "W12", "W16", "W17")]),
]
TILE_INSTALL = [  # installation-terrazzoplattor.pdf
    "Våra terrazzoplattor består av ca 90 % krossad marmor. Materialet drar fukt från limmet, så använd ett "
    "snabbtorkande lim – med ett långsamt torkande lim kan plattorna böja sig och släppa längs kanterna.",
    "Stora plattor ska dubbellimmas, ett skikt lim på golvet och ett på plattans baksida. Vi brukar rekommendera "
    "Ardex X32.",
]
TILE_TIPS = [
    "Bruksanvisningen gäller för torra utrymmen.",
    "Underlaget och luften ska hålla minst 5 °C.",
    "Mät vattnet noga.",
    "Plattan ska vara helt täckt med lim – 60 × 60 cm och större dubbellimmas.",
    "Låt plattorna ligga i rumstemperatur före installationen.",
]
BENCH_CARE = [  # bankskiva-av-terrazzo.pdf
    "Bänkskivan ska alltid impregneras ordentligt innan användning – minst 2–4 impregneringsomgångar eller enligt "
    "anvisningen på förpackningen. Överflöd torkas bort med en torr trasa. Upprepa impregneringen en gång i halvåret "
    "eller vid behov.",
    "Terrazzo är känslig för syror som kan etsa och ge märken i ytan, till exempel sura rengöringsmedel, vin, ättika, "
    "kolsyra, fruktjuicer och kaffe. Torka upp spill direkt.",
    "Vid daglig rengöring räcker det i allmänhet med en fuktig trasa. Behövs rengöringsmedel, använd såpa, milt "
    "diskmedel eller medel för marmor och natursten, till exempel Steinfix 70.",
]

# --- Renovering (lagning-och-slipning…pdf, gbgmosaik-slipning.pdf, gbgmosaik-grovrengoring.pdf, 17/16) -----------
RENO_INTRO = ("För att öka naturstenens och terrazzogolvets livslängd kan man slipa om golvets ytskikt, spackla sprickor "
              "och laga skador med samma material. Resultatet blir ett golv som inte bara varar längre, utan som är "
              "finare att se på och lättare att hålla rent.")
FINISHES = [
    ("Matt", "2-stegs slipning till 220 grit + behandling",
     "En slät, lättstädad yta. Med regelbundet underhåll med Steinfix 60 blir ytan något blankare med tiden. Förr den "
     "vanligaste finishen på nya terrazzogolv."),
    ("Halvblankt", "3-stegs slipning till 400 grit + behandling",
     "En blank men inte speglande yta som håller sig blank med Steinfix 60. Den vanligaste finishen på terrazzogolv i dag."),
    ("Blankt", "4-stegs slipning till 800 grit + polering eller våtkristallisering",
     "En speglande yta som kräver mer underhåll för att behålla glansen. Vanligast på naturstensgolv."),
]
RENO_SERVICES = [
    ("Slipning", "Terrazzo och natursten",
     "Vi slipar om ytskiktet på golv och trappor och ni väljer finish – matt, halvblankt eller blankt.",
     "gbgmosaik-slipning.pdf"),
    ("Lagning", "Terrazzo och naturstensytor",
     "Vi lagar terrazzo och alla typer av naturstensytor med samma material, så att lagningen smälter in.",
     "gbgmosaik-lagning.pdf"),
    ("Grovrengöring", "Terrazzo, natursten, klinker och betong",
     "En rengöring på djupet som avlägsnar fett och partiklar – ett mycket prisvärt sätt att få fram ny lyster och "
     "ge stenen tillbaka sitt skydd.",
     "gbgmosaik-grovrengoring.pdf"),
]
# Projektet "Reparation och restaurering av terrazzo" (17/16), bildtexterna ordagrant.
PROJECT_TITLE = "Påbyggnad – lagning mot ny trappa"
PROJECT_INTRO = ("Här är ett projekt där en kund valt att bygga på en våning i sin fastighet. Det betyder att det "
                 "blivit en skarv som behöver lagas med ny terrazzo mellan det gamla högsta våningsplanet och den nya "
                 "monterade trappan.")
PROJECT_STEPS = [
    ("IMG_0781.jpg", "Påbyggnad", "Skarven mellan det gamla våningsplanet och den nya trappan."),
    ("IMG_0782.jpg", "Räcke", "Det gamla räcket har behövts kapas bort för montering av den nya trappan."),
    ("IMG_0786.jpg", "Bilning", "Vi har bilat bort delar av det gamla golvet så att nya raka kanter bildas och vi kan fylla med 15 mm ny terrazzo."),
    ("IMG_0787.jpg", "Räcke", "Även det gamla räcket har tagits bort så att det inte blir synligt när det nya golvet lagts."),
    ("IMG_0788.jpg", "Formning", "Mot trappan har vi tillverkat en form, eftersom terrazzomaterialet är flytande när det läggs."),
    ("IMG_0789.jpg", "Nygjutet", "Terrazzolagningen är nygjuten."),
    ("IMG_0790.jpg", "Närbild", "Nygjuten terrazzo på nära håll."),
    ("IMG_0803.jpg", "Slipning", "Terrazzolagningen är färdigslipad."),
    ("IMG_0804.jpg", "Närbild slipning", "Den färdigslipade lagningen på nära håll."),
    ("IMG_0805.jpg", "Skurkant", "En ny skurkant har gjutits."),
    ("IMG_0809.jpg", "Slutresultat", "Färdig terrazzolagning."),
]

# --- Torkzoner (17/10/torkzoner) – Kåbe, ordagranna specifikationer ------------------------------------------------
MATS_INTRO = ("Skrapmattor installeras i entréer för att bevara golvet efter en nyläggning eller renovering, till "
              "exempel i en trappuppgång, en butik eller en hotellentré. De hindrar smuts och väta från att dras in på "
              "golvytorna, vilket håller nere städkostnaderna och ger golven längre livslängd. Vi är återförsäljare och "
              "installerar Kåbe Originalmatta, som är ett effektivt skrapgaller och torkmatta i ett.")
MATS = [
    ("Original", ["kabe-original-eko-2.jpg", "kabe-original-eko-1.jpg"], [
        ("Plattstång", "Aluminiumlegering EN AW-6005-A-T6, 12 × 4,5 mm"),
        ("Gummilist", "EPDM 70° Shore, 22 × 3,7 mm – särskilt motståndskraftig mot extrema temperaturväxlingar"),
        ("Ändprofil", "U 18 × 18 × 2 mm"),
        ("Sammanfogning", "Gummilister och aluminiumstänger nitas ihop med specialnitar; mattan hålls ihop av Ø 2,3 mm rostfri stålwire"),
        ("Matthöjd", "Standard 22 mm, alt. 18 mm vid befintliga försänkningar på 15–19 mm"),
        ("Mattstorlek", "Måttbeställd i valfri storlek och nästan vilken form som helst, max 2000 × 5000 mm i ett stycke. Under 400 mm i A-mått tillkommer ställkostnad"),
        ("Förstärkning", "Gummibussningar"),
        ("Vikt", "Ca 12 kg/m²"),
        ("Ytbehandling", "Naturaluminium som standard, även guld- eller svartanodiserat"),
        ("Miljö", "Deklarerad i Byggvarubedömningen, Sunda Hus"),
        ("EN 16005:2012", "Uppfyller kraven – jämn yta utan ojämnheter, läggs med millimeterpassning kant till kant"),
    ]),
    ("Original Tandad", ["kabe-original-tandad-1.jpg", "kabe-original-tandad-2.jpg", "kabe-original-tandad-3.jpg"], [
        ("Plattstänger", "Aluminiumlegering EN AW-6005-A-T6, 12 × 4,5 mm"),
        ("Gummilist", "EPDM 70° Shore, 22 × 3,7 mm"),
        ("Ändprofil", "U 18 × 18 × 2 mm"),
        ("Matthöjd", "Standard 22 mm"),
        ("Mattstorlek", "Måttbeställd, max 2000 × 5000 mm i ett stycke"),
        ("Vikt", "Ca 12 kg/m²"),
        ("Ytbehandling", "Naturaluminium, guld- eller svartanodiserat"),
        ("Tillval", "Kundvagnsförstärkt, taktila ilägg"),
    ]),
    ("Original Kulör", ["kabe-original-color-1.jpg"], [
        ("Plattstänger", "Aluminiumlegering EN AW-6005-A-T6, 12 × 4,5 mm"),
        ("Gummilist", "TPE 65 Shore, 22 × 3,7 mm, röd RAL 3011 eller grå RAL 7040"),
        ("Ändprofil", "U 18 × 18 × 2 mm"),
        ("Matthöjd", "Standard 22 mm"),
        ("Mattstorlek", "Måttbeställd, max 2000 × 5000 mm i ett stycke"),
        ("Vikt", "Ca 12 kg/m²"),
        ("Ytbehandling", "Naturaluminium, guld- eller svartanodiserat"),
        ("Tillval", "Kundvagnsförstärkt, taktila ilägg"),
    ]),
    ("Original de Luxe", ["kabe-original-deluxe-1.jpg", "kabe-original-deluxe-2.jpg", "kabe-original-deluxe-3.jpg"], [
        ("Fyrkantsprofiler", "Aluminiumlegering EN AW-6005-A-T6, 12 × 12 × 1 mm"),
        ("Gummilist", "Svart EPDM 70° Shore, grå eller röd TPE 65° Shore, 22 × 3,7 mm"),
        ("Ändprofil", "U 18 × 18 × 2 mm"),
        ("Matthöjd", "22 mm"),
        ("Mattstorlek", "Måttbeställd, max 1740 × 2000 mm i ett stycke"),
        ("Vikt", "Ca 11 kg/m²"),
        ("Ytbehandling", "Naturaluminium, guld- eller svartanodiserat"),
    ]),
    ("Original Eko", ["kabe-original-eko-1.jpg", "kabe-original-eko-2.jpg"], [
        ("Trästavar", "Furu, 17 × 12 mm, betsade och klarlackade"),
        ("Gummilist", "Svart EPDM 70° Shore, grå eller röd TPE 65° Shore, 22 × 3,7 mm"),
        ("Ändprofil", "Ek, 20 × 22 mm, kan bekläs med mässingslist"),
        ("Matthöjd", "22 mm"),
        ("Mattstorlek", "Måttbeställd, max 1500 × 2000 mm i ett stycke"),
        ("Sammanfogning", "Klammer; mattan hålls ihop av Ø 2,3 mm rostfri stålvajer"),
        ("Vikt", "Ca 15 kg/m²"),
    ]),
]

# --- Taktila markeringar (17/13) ------------------------------------------------------------------------------------
TACTILE_TEXT = [
    "Kontrastmarkeringar förenklar tillvaron för synskadade. Vi erbjuder kontrastmarkeringar av golv och trappor och "
    "anordnar och markerar taktila ledstråk mellan olika platser, till exempel mellan entré eller hiss och "
    "informationsdisk.",
    "Matting taktila ledstråk i rostfritt stål, Line och Diamond, fräses ur rostfritt stål 316. De installeras med ett "
    "angivet intervall för att vägleda personer med synnedsättning. Vid installationen borras tre hål per element och "
    "ett hål per nit efter en mall, och fästena fixeras med rekommenderat lim i hålen.",
    "Vill du inte borra i underlaget finns element och nitar även utan fäste, för limning eller med applicerad tejp. "
    "De finns även i höjden 3 mm.",
]
TACTILE_TYPES = ["Rostfritt stål", "Rostfritt stål TPU", "Mässing", "Aluminium ledstråk"]

# --- Steinfix (17/2/ovriga-produkter) -------------------------------------------------------------------------------
STEINFIX = [
    ("10", "Fläckborttagning av mineralolja", ["Avlägsnar effektivt alla typer av fläckar av mineralolja, tjära och asfalt",
                                               "Kan användas på alla typer av sten som tål vatten", "pH 8 i koncentrerad form"]),
    ("20", "Fett, olja och vax", ["Absorberande fläckborttagningspasta för vegetabiliskt fett och mineralfett, olja och vax",
                                  "Lätt att applicera, bra sugkapacitet", "Kan användas på alla typer av natursten",
                                  "Finns i 0,5-litersburk"]),
    ("30", "Kalk och rost", ["Mycket effektiv mot fläckar av kalk, rost, cement och korrosion",
                             "Innehåller saltsyra – använd försiktigt på sedimentära bergarter som marmor och kalksten",
                             "För alla typer av sten som tål vatten"]),
    ("40", "Grovrengöring", ["Alkalisk specialprodukt för djuprengöring av sten, betong och terrazzo",
                             "Effektiv men skonsam mot sten och kakel",
                             "Tar bort allmän smuts, stekfett, olja, sot m.m.", "pH 13,2 i koncentrerad form"]),
    ("50", "Fläckborttagning av mineralolja", ["Avlägsnar effektivt alla typer av fläckar av mineralolja, tjära och asfalt",
                                               "Kan användas på alla typer av sten som tål vatten", "pH 8 i koncentrerad form"]),
    ("60", "Natursåpa", ["pH-neutral naturprodukt för behandling och underhåll av sten, betong och terrazzo",
                         "Rengör och ger ytan en hållbar skyddsfilm – skyddar impregneringen vid daglig städning",
                         "Hög fetthalt, pH 7,8 i rengöringslösningen", "Svanenmärkt, tillverkad av vegetabiliska oljor",
                         "Kan också användas för impregnering i koncentrerad form"]),
    ("70", "Daglig rengöring av natursten", ["Specialsåpa i sprayflaska för daglig rengöring och underhåll",
                                             "Särskilt bra på bänkskivor", "Tar bort de flesta fläckar, smuts, olja, sot och fett",
                                             "Skonsam mot stenen och ett miljövänligt alternativ",
                                             "För granit, marmor, gnejs, skiffer, sandsten, kalksten och komposit"]),
    ("100", "Luktfri impregnering med NANO-effekt", ["Impregnering för natursten, betong, terrazzo, keramik m.m.",
                                                     "Tränger in osynligt och påverkar inte materialets utseende",
                                                     "Skyddar mot vatten samt fett- och oljebaserade fläckar och smuts",
                                                     "Inomhus, utomhus och i våtrum – diffusionsöppen och frosttålig",
                                                     "Livsmedel kan placeras på behandlade ytor utan hälsorisk",
                                                     "Förhindrar algbildning"]),
]
DEEP_CLEAN = [  # Instruktioner – djuprengöring (17/2)
    "Golvytan ska vara ren och fri från grus så att den inte skadas när golvet skuras.",
    "Dosera Steinfix 40 med 2 dl till 10 liter vatten – mer vid stark nedsmutsning.",
    "Fördela blandningen och låt den verka i ca 10 minuter. Ytan ska vara våt under tiden.",
    "Skura med den bruna eller svarta rondellen på rengöringsmaskinen.",
    "Ta upp överskottet med mopp eller våtdammsugare, skölj med kallt vatten och sug upp igen.",
    "Låt golvet torka ordentligt innan du eventuellt impregnerar.",
]

# --- Dokument (startsidan på gbgmosaik.se) --------------------------------------------------------------------------
# Broschyren "Platsgjuten Terrazzo" (goteborgsmosaikbelaggningar-platsgjuten-terrazzo.pdf) är trasig på nuvarande
# hemsida och länken "Prefabricerad Terrazzo" ger 404 – båda är utelämnade tills nya filer finns.
DOCS = [
    ("Installation", [
        ("Platsgjuten terrazzo", "gbgmosaik-installation-platsgjutet.pdf"),
        ("Terrazzoplattor", "installation-terrazzoplattor.pdf"),
    ]),
    ("Renovering", [
        ("Lagning – terrazzo och naturstensytor", "gbgmosaik-lagning.pdf"),
        ("Slipning – terrazzo", "gbgmosaik-slipning.pdf"),
        ("Grovrengöring – terrazzo, natursten, klinker och betong", "gbgmosaik-grovrengoring.pdf"),
    ]),
    ("Broschyr", [
        ("Lagning och slipning – stengolv", "lagning-och-slipning-av-stengolv-gtteborgs-mosaikbelaggningar-ab.pdf"),
    ]),
    ("Skötselanvisningar", [
        ("Steinfix 100+ – impregnering", "skotselanvisningar-steinfix-impregnering-100.pdf"),
        ("Steinfix 40 och 60 – terrazzogolv", "skotselanvisning-terrazzogolv-40-60.pdf"),
        ("Bänkskiva av terrazzo", "bankskiva-av-terrazzo.pdf"),
    ]),
    ("Byggvarudeklaration", [
        ("Prefabricerad terrazzo, materialgrupp 2", "gbgmosaik-byggvarudeklaration-prefabricerad-terrazzo-materialgrupp-2.pdf"),
    ]),
]

# --- Bilder: webbnamn -> källfil i skrapat/original ----------------------------------------------------------------
PHOTOS = {
    "hero-stentrappa": "assets/images/gbgmosaik-bg-stentrappa.jpg",
    "hero-restaurang": "assets/images/gbgmosaik-bg-restaurang.jpg",
    "hero-purple": "assets/images/gbgmosaik-bg-purple.jpg",
    "hero-nesite": "assets/images/gbgmosaik-bg-nesite.jpg",
    "hero-salvatori": "assets/images/gbgmosaik-bg-marco-salvatori.jpg",
    "platsgjutet": "files/mercado-mexico-platsgjutet.jpg",
    "plattor": "files/golv-och-vaggplattor.jpg",
    "fasad": "files/fasad-ny.jpg",
    "trappa": "files/trappbekladnad.jpg",
    "bankskiva": "files/bankskivor-fonsterskivor-2.jpg",
    "konst-golv": "files/skulpturer-konst-2_1000px.jpg",
    "dokument": "files/documentation.jpg",
    "fore-efter": "files/Föreefter-Stena3.jpg",
    "torkzon": "files/torkzon.jpg",
    "taktila": "files/taktila-markeringar.jpg",
    "steinfix": "files/steinfix-ovriga-produkter.jpg",
    "logga-audi": "files/audi-logos-gbgmosaik.jpg",
    "logga-2": "files/logo-2.jpg",
    "logga-naber": "files/naber-logos-gbgmosaik.jpg",
    "logga-5": "files/logo-5.jpg",
    "logga-gbg-1": "files/logo-gbgmosaik-1.jpg",
    "logga-gbg-2": "files/logo-gbgmosaik-2.jpg",
    "logga-gbg-3": "files/logo-gbgmosaik-3.jpg",
    "logga-salvatori": "files/logos-marco-salvatori.jpg",
}
PHOTOS.update({f"tm-rostfritt-{n}": f"files/tm-rostfritt-{n}.jpg" for n in range(1, 5)})
PHOTOS.update({f"reno-{i + 1:02d}": s[0] for i, s in enumerate(PROJECT_STEPS)})
for _name, _files, _ in MATS:
    for _f in _files:
        PHOTOS[_f[:-4]] = ("files/1000x1000/" if _f.startswith("kabe-original-eko") else "files/") + _f
# Loggor och konst (17/15/loggor och 17/9/foretagsloggor). Dubbletterna på 17/9 är utelämnade.
GALLERY = [
    ("konst-golv", "Mönstergolv i terrazzo med ett flerfärgat geometriskt motiv, under arbete"),
    ("logga-audi", "Audis logga inlagd i ett terrazzogolv"),
    ("logga-naber", "Nabers logga i terrazzo, vit text på röd botten"),
    ("logga-salvatori", "Marco Salvatoris logga i terrazzo"),
    ("logga-gbg-3", "Älvsborgsbron och texten Göteborgs i terrazzo"),
    ("logga-gbg-2", "Göteborgs siluett utskuren i terrazzo i verkstaden"),
    ("logga-gbg-1", "Utskurna bokstäver i terrazzo"),
    ("logga-2", "Göteborgs siluett och företagsnamnet i en terrazzoskiva"),
    ("logga-5", "Nesites logga i ett terrazzogolv i en lobby"),
]
