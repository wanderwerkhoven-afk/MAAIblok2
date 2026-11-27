# Iteratie 01 — Design patterns en ontwerpkeuzes

**Datum:** 27 november 2026  
**Status:** voorlopige design rationale, nog niet gevalideerd

## 1. Aanleiding en herkomst van de keuzes

De basis is de handgetekende whiteboardschets van 27 november 2026. Deze toont een upload/dashboard-ervaring, een afzonderlijk samenvattingsscherm, cirkelvormige scores, highlights en notities over het gebruik van een LLM-judge en spaCy. De design patterns zijn ontleend aan de eerdere [patternverkenning](../../03-Design-patterns.md), maar de koppeling ervan aan elementen van deze iteratie is een **ontwerpvoorstel**.

## 2. Ontwerpbeslissingen en alternatieven

| ID | Beslissing in prototype | Reden / verwacht voordeel | Risico of alternatief | Status |
|---|---|---|---|---|
| D01 | Dashboard en evaluatieoverzicht zijn afzonderlijke schermen | Het uploadproces scheiden van beoordeling | Extra navigatiestap; één scherm kan sneller zijn | Te testen |
| D02 | Cirkelindicatoren tonen drie afzonderlijke maten | Maakt verschillen tussen controleaspecten zichtbaar | Visuele percentages kunnen schijnzekerheid oproepen; alternatief: tekstlabels en checklijst | Te testen |
| D03 | De voorgestelde 75%, 35% en 92% zijn expliciet fictief | Een demonstratie mogelijk maken zonder niet-bestaande metingen als feiten te presenteren | Effect op intuïtieve interpretatie moet worden onderzocht | Alleen demo |
| D04 | Gemarkeerde zin is aanklikbaar | Claim, check en onderbouwing beter verbinden | Een highlight kan onterecht als bevestiging overkomen | Te testen |
| D05 | Een apart bronpaneel toont een uitleg bij onvoldoende bewijs | Verifieerbaarheid zonder te diep technisch detail | Brontekst en matchkwaliteit zijn in de echte toepassing nog onbekend | Te testen |
| D06 | Analist kan Vertrouwen, Controleren of Afwijzen kiezen | Menselijk toezicht en expliciet besluit | Risico van een te prominent acceptatieknopontwerp | Te testen |
| D07 | Engineer-perspectief is een afzonderlijk scherm | Verschillende informatiebehoeften van analist en engineer | Engineer-metrics zijn nu fictief; werkelijke vergelijkbaarheid ontbreekt | Schets |
| D08 | Het interfacevoorbeeld vermeldt wat het niet doet | Voorkomen dat gebruikers de demo verwarren met een werkende AI | Waarschuwing kan worden genegeerd | Toetsbaar |

## 3. Geselecteerde design patterns

### P01 — Verwachtingen duidelijk maken

**Probleem:** een gebruiker zou het dashboard of de scores als gevalideerde kwaliteitsuitkomst kunnen interpreteren.  
**Toepassing:** expliciete demomelding, labels bij de indicatoren en tekst dat geen echte PDF-analyse draait.  
**Toetsing:** vraag wat een score of status bewijst en wat niet.

### P02 — Uitleg voor begrip

**Probleem:** alleen de term 'controle nodig' biedt onvoldoende inzicht in de mogelijke oorzaak.  
**Toepassing:** een specifiek gemarkeerde claim wordt gekoppeld aan een uitleg en een knop om de broncontext te openen.  
**Toetsing:** laat gebruikers een onduidelijke claim identificeren en uitleggen welke informatie nog nodig is.

### P03 — Vertrouwen zorgvuldig tonen

**Probleem:** één algeheel vertrouwenspercentage kan uiteenlopende kwaliteitsdimensies verhullen.  
**Toepassing:** drie gescheiden, gelabelde indicatoren voor claimcontrole, dekking en compressie. De derde maat beschrijft tekstlengte en is **geen** betrouwbaarheidsscore.  
**Toetsing:** vergelijk interpretatie van scorecirkels met tekstuele checkresultaten.

### P04 — Gebruikers automatisering laten bewaken

**Probleem:** een systeemadvies kan zonder controle als definitieve beslissing worden overgenomen.  
**Toepassing:** de route 'Controleren' is een voorstel; de analist kiest zelfstandig tussen drie acties.  
**Toetsing:** presenteer een scenario waarin de juiste bronuitkomst afwijkt van het routevoorstel.

### P05 — Gebruikersfeedback mogelijk maken

**Probleem:** een foutieve check zonder feedbackmogelijkheid kan de evaluatiepipeline niet eenvoudig verbeteren.  
**Toepassing:** 'Meld een probleem' is aanwezig, maar nog niet gekoppeld aan een feedbackformulier of opslag.  
**Toetsing:** onderzoek of de gewenste meldactie herkenbaar is; test de echte feedbackflow in een latere iteratie.

### P06 — Controle teruggeven bij mislukte automatisering

**Probleem:** een ontbrekende evaluatie kan als positieve check worden opgevat.  
**Toepassing in iteratie 01:** nog niet als volledig afzonderlijk scherm gebouwd. Dit is een **openstaande requirement** voor de volgende iteratie.  
**Toetsing:** test een expliciete 'Geen beoordeling mogelijk'-toestand met handmatige vervolgacties.

## 4. Kleur, tekst en bediening

- **Donkerblauw:** navigatie en primaire handelingen; bewust geen gebruik van groen voor 'vertrouwen' als automatisch oordeel.
- **Groenblauw:** illustratieve checkresultaten; betekent niet dat het gehele document foutloos is.
- **Oranje:** aandachtspunt dat nader onderzoek verdient.
- **Paars:** aparte dekking-indicator om kwaliteitsdimensies niet uitsluitend met groen/rood te communiceren.
- **Geel:** markering van een zin of passage die de gebruiker kan onderzoeken.
- **Rood:** visuele waarschuwing bij het besluit 'Afwijzen'.

Tekstlabels, knoppen en broninformatie blijven nodig omdat kleur op zichzelf niet voldoende informatie overbrengt. Deze keuzes zijn voorlopig en dienen op toegankelijkheid (inclusief contrast en kleuronderscheid) getest te worden.

## 5. Technische brainstorm: LLM-judge en spaCy

De notitie rechts op de aangeleverde schets suggereert twee componenten:

**LLM-as-judge:** het controleren van claims of beoordelen van de relatie tussen samenvatting en bron. Een voorbeeldberekening *correct beoordeelde claims / beoordeelde claims × 100%* is uitsluitend bruikbaar nadat 'correct', de annotatieprocedure, de steekproef en het omgaan met onzekerheid zijn gedefinieerd. Een LLM-oordeel is zelf foutgevoelig en vereist validatie tegen menselijke referentieannotaties.

**spaCy:** mogelijke ondersteuning voor segmentatie, zinsdetectie, entiteitsherkenning en tekstvoorbewerking. spaCy zet niet zelfstandig een technische F1-score om in een begrijpelijke of gevalideerde betrouwbaarheidsscore. De mapping van metrics naar UI-signalen hoort bij een expliciet gespecificeerde evaluatie- en presentatielaag.

Geen van beide componenten is in deze HTML-demo geïmplementeerd.

## 6. Testbaar maken

| Scenario | Taak | Observatie |
|---|---|---|
| Scorebegrip | 'Leg uit wat 75% claimcontrole betekent.' | Wordt 75% onterecht opgevat als garantie op juistheid? |
| Broncontrole | 'Zoek bewijs voor de gemarkeerde omzetclaim.' | Volgt gebruiker de klikroute en herkent die onvoldoende bewijs? |
| Keuze | 'Welke beslissing neem je voor dit voorbeeld?' | Wordt het routevoorstel zelfstandig afgewogen? |
| Faalstatus (volgende iteratie) | 'Het systeem kan geen evaluatie leveren; wat nu?' | Kiest gebruiker handmatige beoordeling? |
| Engineer view | 'Welk model is beter en wat ontbreekt om dit vast te stellen?' | Ziet gebruiker dat fictieve scores niet genoeg zijn? |

**Interpretatie:** dit zijn vooraf geplande observaties, geen uitgevoerde experimenten. Testdatum, deelnemers, rollen, prototypeversie, bevindingen en eventuele aanpassingen moeten na gebruikerstesten afzonderlijk worden geregistreerd.

## 7. Visuele stijlherziening binnen iteratie 01 — 27 november 2026

**Aanleiding:** zes door de gebruiker aangeleverde voorbeeldpagina's van het Rabobank Annual Report 2025, waaronder een 'At a Glance'-spread, geografische aanwezigheid, lopende tekst, financiële KPI's, prestatiegrafieken en vastgoedontwikkeling. Het gaat om visuele referenties voor de interface, niet om datasetresultaten.

**Geobserveerde kenmerken:** een overwegend witte achtergrond, uitgesproken helderblauwe (soms cursieve) koppen, oranje kerncijfers en grafiekaccenten, veel witruimte, fijne scheidingslijnen, sobere rechthoekige informatiepanelen en blauw/oranje datavisualisaties.

**Toepassing in prototype:** de vorige donkere navigatie is vervangen door witte navigatie met blauwe typografie; kaarten hebben rechte hoeken; de dashboardpanelen hebben respectievelijk blauwe en oranje bovenranden; indicatorgetallen zijn oranje; het uploadvak heeft een rustige lichtblauwe achtergrond; de voortgangsbalk is oranje; de grafiekaccenten gebruiken blauw en oranje. Deze stijl geldt ook voor de samenvatting, broncontrole en engineerweergave.

| ID | Visuele ontwerpkeuze | Functionele bedoeling | Toetsbare onzekerheid |
|---|---|---|---|
| V01 | Witte basis, dunne scheidingslijnen, sobere panelen | Rustig document- en analysekarakter | Is het onderscheid tussen groepen informatie nog duidelijk genoeg? |
| V02 | Blauw als hoofdkleur voor koppen, navigatie en primaire knoppen | Consistente visuele hiërarchie | Worden primaire acties sneller herkend? |
| V03 | Oranje voor getallen, voortgang en waarschuwingen | Kerninformatie naar voren halen | Kan oranje als waarschuwing worden verward met een prestatiegetal? |
| V04 | Cursieve koppen zoals in de referentierapportage | Herkenbare visuele richting | Blijft de leesbaarheid goed op klein formaat? |
| V05 | Blauwe en oranje grafiekmarkeringen | Relatie met financiële rapportagetaal | Kunnen gebruikers de betekenis zonder alleen kleur begrijpen? |

**Randvoorwaarde:** de toepassing moet evaluatiesignalen ondubbelzinnig uitleggen; esthetische aansluiting op de referentie mag niet ten koste gaan van toegankelijkheid, voldoende kleurcontrast en onderscheid tussen status en score. Er zijn geen foto's of illustraties uit het jaarverslag in de HTML overgenomen.

De hier beschreven aanpassing betreft uitsluitend de **visuele stijl van de bestaande iteratie**, niet een nieuwe gebruikersgeteste ontwerpiteratie.

## 8. Functionele uitbreiding: echte lokale PDF-upload en bronviewer (27 november 2026)

De bron- en samenvattingsweergave zijn uitgebreid met werkende uploads: twee PDF's kunnen lokaal worden ingelezen en in afzonderlijke PDF.js-canvasvensters worden weergegeven. De navigatie bevat 'PDF-viewer'. Elke viewer heeft paginabesturing, zoom en zoekfunctie over de tekstinhoud van het document. Een klik op een gevonden paginanummer springt naar die pagina.

| ID | Beslissing | Reden | Beperking / te testen |
|---|---|---|---|
| F01 | Twee aparte PDF-selectievelden (bron en samenvatting) | Maakt directe visuele vergelijking mogelijk | Documenten worden niet automatisch gekoppeld aan een manifest |
| F02 | PDF's lokaal via File API + PDF.js lezen | Geen serveropslag nodig voor prototyping; echte paginaweergave | Bibliotheek geladen via CDN, dus netwerk nodig bij initialisatie |
| F03 | Zij-aan-zij viewer met afzonderlijke paginanavigatie | Bron en samenvatting onafhankelijk bekijken | Op kleine schermen wordt gestapeld |
| F04 | Pagina-gebaseerde tekstzoekfunctie | Verhoogt vindbaarheid van claims in lange documenten | Alleen doorzoekbare tekst; OCR en precieze zinhighlights ontbreken |
| F05 | Fictieve scores gescheiden van werkende viewer | Voorkomt dat demo-uitkomsten worden verward met werkende AI | Taal en zichtbaarheid van waarschuwing moeten worden getest |
| F06 | Uploadlimiet van 80 MB | Beperkt geheugengebruik van de browser | Grote PDF's en oudere apparaten vereisen prestatietesten |

**Relevante design patterns:** *gebruikerscontrole* (zelf het originele document kunnen bekijken), *uitleg voor begrip* (documentcontext toegankelijk maken) en *verwachtingen duidelijk maken* (echte viewer vs. fictieve AI-resultaten). Dit is technisch geïmplementeerd; effectiviteit en bruikbaarheid zijn nog niet empirisch bevestigd.

**Geen automatische claim-naar-bronverificatie:** een zoekresultaat laat zien waar woorden voorkomen en is geen bewijs dat een claim feitelijk klopt. Voor daadwerkelijke teksthighlights, semantische bronkoppelingen, OCR en AI-judging zijn nieuwe onderzoek- en ontwikkelstappen nodig.

## 9. Revisie: van fictieve scores naar echte brondata (27 november 2026)

Na de eerste interactieve demo is gekozen om de impressie te baseren op de werkelijke PDF-dataset. De mock-scores en voorbeeldclaims zijn verwijderd. De revisie blijft onderdeel van iteratie 01; er is nog geen stakeholdertest geweest.

| ID | Aanpassing | Onderbouwing | Risico/validatie |
|---|---|---|---|
| F07 | Echte rapporten selecteerbaar via organisatie en v0-documentpaar | Representatieve demonstratie, sluit aan bij de onderzoeksdataset | Laden van grote, externe PDF's en CORS/CDN afhankelijkheden testen |
| F08 | Documentaantallen en tekstreductie worden uit ingelezen PDF's berekend | Reproduceerbaar afgeleid uit werkelijke invoer in plaats van fictieve KPI's | PDF-extractie en woordafbakening kunnen afwijken van de werkelijke inhoud |
| F09 | Samenvattingszinnen worden automatisch verzameld uit de PDF-tekst | De inhoudelijke broncontrole begint bij echte claims/zinnen | Sommige PDF-layouts hebben onregelmatige zinsvolgorde |
| F10 | Heuristische bronpagina's via token-overlap en tekstfragmenten | Verbetert de vindbaarheid van mogelijk relevant bronmateriaal | Geen semantische validatie, ondersteuning of waarheidsoordeel |
| F11 | Klikbare bronverwijzing opent PDF op pagina en markeert overlappende tekstitems | Geeft de analist controle over de bewijscontext | Een geel woordhighlight is géén bewijs; enkele matches kunnen fout zijn |
| F12 | Geen globale AI-betrouwbaarheidsscore tonen zonder gevalideerde evaluatie | Vermijdt schijnprecisie en overmatig vertrouwen | Gebruikers kunnen wel een beoordelingsadvies missen |

**Te onderzoeken design patterns:** *explanation for understanding* (bronfragment), *calibrated trust* (onderscheid tekstmatch en bewijs), *expectation setting* (geen AI-factcheck), *human oversight* (analist neemt besluit) en *failure handling* (geen bronvoorstel tonen als overlap onvoldoende is).

**Onderzoekbare vragen:** (1) Is de voorgestelde bronpagina echt relevant? (2) Hoe vaak wordt de juiste pagina in de top drie gevonden ten opzichte van handmatig gecontroleerde referenties? (3) Wordt de matchscore door gebruikers ten onrechte gezien als betrouwbaarheid? (4) Kunnen kritieke getallen en ontkennende formuleringen verkeerd worden gekoppeld? (5) Hoeveel tijd kost de indexering bij grote rapporten?

Voor een volgende iteratie zijn validatie tegen menselijke annotaties, expliciete 'geen bewijs'/'tegenstrijdig'/'technische fout'-toestanden en een echte claim-verificatiemodule nodig.

## 10. Voorstel voor iteratie 02

Prioriteit: een echte vergelijking van twee UI-varianten voor scoreweergave en een duidelijk afzonderlijk 'Geen beoordeling mogelijk'-scherm. Daarnaast een klikbaar feedbackformulier met de categorieën 'Feit klopt niet', 'Informatie ontbreekt' en 'Onvoldoende bronbewijs'. Nieuwe keuzes alleen als definitief vastleggen na evaluatie.

[Iteratie-overzicht](README.md) · [Prototype](prototype.html) · [Overzicht](../README.md)
