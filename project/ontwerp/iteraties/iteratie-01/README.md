# Ontwerpiteratie 01 — Dashboard, scores en broncontrole

**Datum:** 27 november 2026  
**Project:** SummaryCheck  
**Status:** interactief prototype met werkende PDF-upload, weergave en heuristische bronkoppeling; nog niet gevalideerd met gebruikers

## 1. Aanleiding en schets

De eerste handgetekende UI-schets toont links een **Rabobank-dashboard** met een documentupload en een voortgangsbalk (93% in de schets). Het volgende scherm bevat links een **samenvatting**, rechts **cirkelindicatoren** voor verschillende evaluatiedimensies en onderaan of naast de samenvatting **gemarkeerde passages**. Een aanvullende notitie verwijst naar gebruik van een LLM voor beoordeling van claims en naar het vertalen van technische scores naar begrijpelijke signalen voor eindgebruikers.

De getekende voorbeeldwaarden, waaronder de scorecirkels, dienen als visuele inspiratie; zij zijn **geen daadwerkelijk berekende evaluatie-uitkomsten**. Deze iteratie vertaalt het idee naar een eerste klikbaar, single-file HTML-prototype.

## Belangrijke revisie — 27 november 2026: echte documenten in plaats van demodata

De eerdere losse demo-claims, fictieve cirkelpercentages, fictieve bronteksten en voorbeeldgrafieken zijn **verwijderd uit het werkende dashboard**. De interface biedt nu:

1. Selectie van de drie echte documentparen uit `data/raw/` en `data/summaries/` (Rabobank, ING en ABN AMRO, v0) via de publieke repositorybestanden.
2. Eigen uploads van een origineel rapport en een PDF-samenvatting; beide worden lokaal geopend.
3. Een echte zij-aan-zij PDF-viewer met paginanavigatie en zoom via PDF.js.
4. Meting van het aantal bronpagina's, samenvattingspagina's, geëxtraheerde woorden en indicatieve tekstreductie.
5. Extractie van zinnen uit de ingelezen samenvatting, met maximaal drie mogelijke bronpagina's per geselecteerde zin op basis van woordoverlap tussen samenvatting en PDF-bron.
6. Een actie **Open bron op pagina** die naar de gevonden pagina springt en overlappende woorden op de gerenderde PDF-pagina markeert.
7. Tekstzoekfuncties per document en een lokaal (niet-opgeslagen) menselijk beslislabel.

### Validiteit van de koppelingen

De bronverwijzing is een **heuristisch zoekresultaat**, geen aangetoonde claimonderbouwing. De huidige implementatie gebruikt eenvoudige tokenisatie, stopwoordfiltering, pagina-overlap en tekstvensters. Dit kan verkeerde passages aanwijzen, semantisch equivalente formuleringen missen en geen numerieke of feitelijke consistentie garanderen. Ook 'overeenkomst van geselecteerde termen' is geen probabilistische betrouwbaarheidsscore. De interface moet de analist expliciet laten controleren of een voorgestelde passage de claim daadwerkelijk ondersteunt.

**Technisch:** grote PDF's kosten tijd bij tekstextractie; gescande PDF's zonder tekstlaag vereisen OCR. De repository-PDF's en PDF.js vereisen een werkende internetverbinding bij laden; eigen bestanden worden door de applicatie niet geüpload. De inhoud wordt bij het verlaten/verversen van de pagina niet bewaard.

**Status toetsing:** code is in de repository verwerkt, maar er zijn nog geen volledige browsertest, gedocumenteerde gebruikersobservaties of gevalideerde matchprestaties geregistreerd.

## 2. Ontwerpdoel

Een analist moet vanuit een rapportoverzicht kunnen navigeren naar een samenvatting, relevante controle-uitkomsten kunnen interpreteren en een verdachte claim kunnen onderzoeken via een bronpaneel, voordat een menselijke beslissing wordt vastgelegd.

**Voorlopige hypothese:** brongebonden deelchecks met een duidelijke route voor handmatige controle zijn begrijpelijker en beter controleerbaar dan één algemene score zonder verdere toelichting.

## 3. Bestanden

| Bestand | Beschrijving |
|---|---|
| [prototype.html](prototype.html) | Zelfstandige, responsieve HTML/CSS/JavaScript-demo met echte lokale PDF-upload, PDF.js-bronviewer, tekstzoekfunctie, paginabesturing en daarnaast nog fictieve evaluatiescores |
| [Design-patterns-en-keuzes.md](Design-patterns-en-keuzes.md) | Patroonselectie, concrete implementatie, trade-offs, open vragen en toetsvoorstellen |

## 4. Inhoud van het prototype

- **Dashboard:** werkende lokale PDF-selectie en weergave van ingelezen status, naast een demonstratiekaart met drie **fictieve** cirkelindicatoren.
- **Samenvatting:** voorbeeldtekst met een gemarkeerde claim en broncontrole.
- **Scores:** aparte demo-indicatoren voor claimcontrole, dekking en compressie; niet één algemeen betrouwbaarheidspercentage.
- **PDF-viewer:** daadwerkelijke bron-PDF en samenvattings-PDF naast elkaar, lokaal ingelezen via PDF.js. Pagina's bladeren, paginanummer invoeren, zoomen, zoeken in extraheerbare PDF-tekst en originele PDF openen.
- **Broncontrole-demo:** het oorspronkelijke scherm met een fictieve claim, fictieve bronpassage en uitleg over onvoldoende bewijs blijft bewaard als conceptvoorbeeld. Dit is **niet** automatisch gekoppeld aan de geüploade PDFs.
- **Menselijke beslissing:** knoppen Vertrouwen, Controleren en Afwijzen; lokaal demonstratiebericht na klikken.
- **Engineer view:** zeer eenvoudige schets voor modelversievergelijking.
- **Foutfeedback:** zichtbare meldknop; formulier en backend volgen in latere iteraties.

## 5. Visuele stijl (revisie 27 november 2026)

Het HTML-prototype is visueel afgestemd op zes aangeleverde referentiepagina's uit het Rabobank Annual Report 2025: een witte en open lay-out, helderblauwe cursieve koppen, oranje cijfers en accenten, dunne scheidingslijnen en sobere grafieken. Deze stijl is toegepast op het dashboard en de overige prototypeschermen; de bestaande demo-interacties blijven gelijk.

De esthetische keuzes, mogelijke risico's en toetsvragen staan in [Design-patterns-en-keuzes.md](Design-patterns-en-keuzes.md#7-visuele-stijlherziening-binnen-iteratie-01--27-november-2026). Er zijn geen originele rapportafbeeldingen gebruikt als UI-assets.

## 6. Afbakening en beperkingen

Het prototype is een **front-end demonstratie met werkende lokale PDF-weergave**: PDF.js leest de geselecteerde bestanden daadwerkelijk in en toont de originele PDF-pagina's. De viewer bevat paginanavigatie, zoom en tekstzoekresultaten per pagina. PDF's worden niet naar de applicatieserver geüpload. Er draait **geen** LLM of documentevaluerende pipeline; claims, scores en de voorbeeldbronpassage in de analyse-demo zijn fictief. Het ontbreken van gekoppeld bewijs is niet automatisch bewijs dat een claim onwaar is. Tekstzoeken werkt alleen wanneer een PDF tekst bevat (gescande pagina's vereisen OCR). De PDF.js-bibliotheek en worker worden via een externe CDN geladen en vereisen een netwerkverbinding.

De in de whiteboardschets genoemde LLM-judge en spaCy zijn **technische oplossingsrichtingen**, geen geïmplementeerde of gevalideerde componenten van dit prototype. Het precieze gebruik van spaCy voor taalkundige voorbewerking en van een LLM-judge voor claimverificatie vereist apart technisch onderzoek. F1, accuracy of een ander getal kan niet zonder operationele definitie naar een betrouwbaarheidspercentage worden vertaald.

## 7. Open vragen voor de eerste test

1. Begrijpt een analist het verschil tussen scores voor claimcontrole, dekking en compressie?
2. Wordt het percentage in een cirkel ten onrechte gezien als kans op een juiste samenvatting?
3. Is de visuele route van highlight naar bron duidelijk?
4. Is het verschil tussen onvoldoende bewijs en feitelijk onjuist helder?
5. Welke beslissing wordt genomen bij een onvoldoende onderbouwde claim?
6. Hoe reageert de gebruiker als de evaluatie mislukt of geen uitslag heeft?

Een testopzet en meetvoorstellen staan in het [validatieplan](../../05-Validatieplan.md). Er zijn nog geen empirische resultaten.

## 8. Technische uitvoering van de PDF-viewer

De viewer en tekstextractie gebruiken [Mozilla PDF.js](https://mozilla.github.io/pdf.js/) via een vastgepinde CDN-versie (`3.11.174`). Een gebruiker kiest een bron-PDF en een samenvattings-PDF; de browser leest de bestanden met `File.arrayBuffer()` in, en PDF.js rendert pagina's in `canvas`. Met `getTextContent()` worden per pagina tekstzoekresultaten gevonden. Er wordt geen document naar een backend verstuurd. De gekozen bestanden verdwijnen bij herladen van de pagina.

**Validatiepunten:** test met de aanwezige jaarverslagen (waaronder PDF's met veel pagina's en grafieken), documentgrootte, mobiele schermen, browsercompatibiliteit, gescande pagina's, beveiligde PDF's en gebruik zonder netwerk. Er is nog geen volledige end-to-end browsertest gerapporteerd.

## 9. Iteratiestatus

**Gemaakt:** een HTML-interface met echte PDF-upload van bron en samenvatting, datasetselectie (ABN AMRO, ING, Rabobank), PDF.js-rendering, paginanavigatie, zoom, tekstzoekfunctie, paginagerichte bronvoorstellen op basis van tekstoverlap en indicatieve tekstreductie.  
**Nog niet gedaan:** stakeholdervalidatie, gevalideerde semantische claim-naar-bronverificatie, precisie van teksthighlights, LLM-judge-integratie, usabilitymeting en modelprestatie-evaluatie. Bronmatches zijn voorstellen, geen factchecks.

[Terug naar overzicht ontwerpiteraties](../README.md) · [Terug naar ontwerp](../../README.md)

**Actuele interface:** [prototype.html](prototype.html) · [ontwerpbeslissingen](Design-patterns-en-keuzes.md)
