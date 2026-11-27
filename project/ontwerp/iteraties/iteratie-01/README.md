# Ontwerpiteratie 01 — Dashboard, scores en broncontrole

**Datum:** 27 november 2026  
**Project:** SummaryCheck  
**Status:** eerste concept / interactief demonstratieprototype; nog geen gebruikerstest uitgevoerd

## 1. Aanleiding en schets

De eerste handgetekende UI-schets toont links een **Rabobank-dashboard** met een documentupload en een voortgangsbalk (93% in de schets). Het volgende scherm bevat links een **samenvatting**, rechts **cirkelindicatoren** voor verschillende evaluatiedimensies en onderaan of naast de samenvatting **gemarkeerde passages**. Een aanvullende notitie verwijst naar gebruik van een LLM voor beoordeling van claims en naar het vertalen van technische scores naar begrijpelijke signalen voor eindgebruikers.

De getekende voorbeeldwaarden, waaronder de scorecirkels, dienen als visuele inspiratie; zij zijn **geen daadwerkelijk berekende evaluatie-uitkomsten**. Deze iteratie vertaalt het idee naar een eerste klikbaar, single-file HTML-prototype.

## 2. Ontwerpdoel

Een analist moet vanuit een rapportoverzicht kunnen navigeren naar een samenvatting, relevante controle-uitkomsten kunnen interpreteren en een verdachte claim kunnen onderzoeken via een bronpaneel, voordat een menselijke beslissing wordt vastgelegd.

**Voorlopige hypothese:** brongebonden deelchecks met een duidelijke route voor handmatige controle zijn begrijpelijker en beter controleerbaar dan één algemene score zonder verdere toelichting.

## 3. Bestanden

| Bestand | Beschrijving |
|---|---|
| [prototype.html](prototype.html) | Zelfstandige, responsieve HTML/CSS/JavaScript-demo met verschillende schermen en klikbare acties |
| [Design-patterns-en-keuzes.md](Design-patterns-en-keuzes.md) | Patroonselectie, concrete implementatie, trade-offs, open vragen en toetsvoorstellen |

## 4. Inhoud van het prototype

- **Dashboard:** voorbeeld van PDF-upload, voortgangsbalk en een demonstratiekaart met drie cirkelindicatoren.
- **Samenvatting:** voorbeeldtekst met een gemarkeerde claim en broncontrole.
- **Scores:** aparte demo-indicatoren voor claimcontrole, dekking en compressie; niet één algemeen betrouwbaarheidspercentage.
- **Brondocument:** een tweede scherm met fictieve bronpassage, teksthighlight en uitleg over onvoldoende bewijs.
- **Menselijke beslissing:** knoppen Vertrouwen, Controleren en Afwijzen; lokaal demonstratiebericht na klikken.
- **Engineer view:** zeer eenvoudige schets voor modelversievergelijking.
- **Foutfeedback:** zichtbare meldknop; formulier en backend volgen in latere iteraties.

## 5. Visuele stijl (revisie 27 november 2026)

Het HTML-prototype is visueel afgestemd op zes aangeleverde referentiepagina's uit het Rabobank Annual Report 2025: een witte en open lay-out, helderblauwe cursieve koppen, oranje cijfers en accenten, dunne scheidingslijnen en sobere grafieken. Deze stijl is toegepast op het dashboard en de overige prototypeschermen; de bestaande demo-interacties blijven gelijk.

De esthetische keuzes, mogelijke risico's en toetsvragen staan in [Design-patterns-en-keuzes.md](Design-patterns-en-keuzes.md#7-visuele-stijlherziening-binnen-iteratie-01--27-november-2026). Er zijn geen originele rapportafbeeldingen gebruikt als UI-assets.

## 6. Afbakening en beperkingen

Het prototype is een **front-end demonstratie**: de geselecteerde PDF wordt niet uitgelezen, er draait geen LLM of documentevaluerende pipeline, er worden geen echte metrics berekend en er worden geen bestanden naar een server geüpload. Uploadbestandsnaam, progressie, scores en brontekst zijn losstaande illustratieve onderdelen. Het ontbreken van gekoppeld bewijs is niet automatisch bewijs dat een claim onwaar is.

De in de whiteboardschets genoemde LLM-judge en spaCy zijn **technische oplossingsrichtingen**, geen geïmplementeerde of gevalideerde componenten van dit prototype. Het precieze gebruik van spaCy voor taalkundige voorbewerking en van een LLM-judge voor claimverificatie vereist apart technisch onderzoek. F1, accuracy of een ander getal kan niet zonder operationele definitie naar een betrouwbaarheidspercentage worden vertaald.

## 7. Open vragen voor de eerste test

1. Begrijpt een analist het verschil tussen scores voor claimcontrole, dekking en compressie?
2. Wordt het percentage in een cirkel ten onrechte gezien als kans op een juiste samenvatting?
3. Is de visuele route van highlight naar bron duidelijk?
4. Is het verschil tussen onvoldoende bewijs en feitelijk onjuist helder?
5. Welke beslissing wordt genomen bij een onvoldoende onderbouwde claim?
6. Hoe reageert de gebruiker als de evaluatie mislukt of geen uitslag heeft?

Een testopzet en meetvoorstellen staan in het [validatieplan](../../05-Validatieplan.md). Er zijn nog geen empirische resultaten.

## 8. Iteratiestatus

**Gemaakt:** HTML-voorbeeld en documentatie van de eerste ontwerpafwegingen.  
**Nog niet gedaan:** stakeholdervalidatie, daadwerkelijke PDF-analyse, echte bronverwijzingen, kalibratie van scores, usabilitymeting en modelprestatie-evaluatie.

[Terug naar overzicht ontwerpiteraties](../README.md) · [Terug naar ontwerp](../../README.md)
