# 01. Waardepropositie — SummaryCheck

**Documenttype:** conceptuele ontwerpverkenning  
**Datum:** 23 november 2026  
**Status:** hypothese, nog niet gevalideerd

## 1. Context en probleemverkenning

AI-systemen kunnen lange financiële en zakelijke documenten samenvatten. Een samenvatting van een jaarverslag, kredietrapport of dossier kan de benodigde leestijd reduceren, maar brengt risico's met zich mee: onjuiste cijfers, onbevestigde claims, weggelaten relevante informatie en onvoldoende inzicht in de herkomst van uitspraken. Voor een analist is daarom niet alleen de kwaliteit van de samenvatting relevant, maar vooral de vraag **of en onder welke voorwaarden deze voor het werk bruikbaar is**.

SummaryCheck is een concept voor een ondersteunende evaluatielaag. De toepassing combineert een AI-samenvatting met het oorspronkelijke document en presenteert checks, scores, bewijsverwijzingen en een voorgestelde route voor verdere beoordeling. De eindbeslissing blijft bij de analist.

## 2. Waardepropositie voor de analist

**SummaryCheck** gebruikt AI-samenvattingen van jaarverslagen, kredietrapporten en dossiers, in combinatie met evaluatie-uitkomsten zoals checks, scores en routering, om analisten te ondersteunen bij het bepalen of een samenvatting kan worden vertrouwd, extra controle vereist of moet worden afgewezen. Het beoogde effect is een snellere en consistentere identificatie van informatie die nader moet worden gecontroleerd, met behoud van de menselijke eindbeslissing.

De kernpropositie is een **te toetsen verwachting**; tijdwinst, consistentie en behoud van besliskwaliteit zijn nog geen vastgestelde resultaten.

## 3. Waardepropositie volgens het aangeleverde format

| Onderdeel | Voorlopige invulling |
|---|---|
| **Conceptnaam** | SummaryCheck |
| **Using — data** | AI-gegenereerde samenvattingen én oorspronkelijke documenten, zoals jaarverslagen, kredietrapporten en dossiers |
| **To — AI capability** | Samenvattingen beoordelen met evaluatiechecks en scores, waaronder waar passend feitelijke consistentie, dekking (*coverage*), leesbaarheid en classificatiematen, en uitkomsten koppelen aan bronpassages en reviewroutes |
| **We can help — doelgroep** | Analisten die AI-samenvattingen op bruikbaarheid en betrouwbaarheid moeten beoordelen |
| **With a better way to — taak** | Onderbouwd bepalen of een AI-samenvatting kan worden geaccepteerd, nader gecontroleerd of afgewezen, met inzichtelijke bevindingen en toegankelijke zelfcontrole |
| **Because / so that — opbrengst** | Vermoedelijk minder beoordelingstijd en duidelijkere prioritering van benodigde controles |
| **With / without — waarde** | Beoogd: kortere beoordelingstijd zonder aantoonbaar verlies van de kwaliteit van menselijke besluitvorming |

### Methodologische precisering van de metrics

**F1-score, precision, recall en accuracy** zijn alleen betekenisvol wanneer een duidelijk gedefinieerde classificatietaak en geschikte referentielabels beschikbaar zijn, bijvoorbeeld het herkennen van feitelijke fouten. Deze maten zijn niet zonder meer rechtstreeks te interpreteren als een algemene vertrouwensscore voor een complete samenvatting. *Readability* beoordeelt begrijpelijkheid en niet noodzakelijk feitelijke juistheid. *Coverage* beoordeelt in hoeverre relevante broninformatie is meegenomen en vereist een expliciete operationalisering.

De definitieve selectie, weging en drempelwaarden van de checks blijven een onderzoeksvraag.

## 4. Beoogde systeemgrenzen

**Input:** origineel document, AI-samenvatting en eventuele metadata over modelversie en documenttype.

**Evaluatie:** bron-claimvergelijking, controle van getallen en entiteiten, beoordeling van dekking, signalering van onzekerheid en vastlegging van controle-uitkomsten.

**Output:** begrijpelijke deelresultaten, aanklikbare bronverwijzingen, gemarkeerde passages, een beargumenteerd routevoorstel en ruimte voor menselijke correctie.

**Niet beoogd:** automatische definitieve goedkeuring van financiële conclusies, garantie op foutloosheid of vervanging van de professionele verantwoordelijkheid van de analist.

## 5. Onderzoekbare aannames

| ID | Aanname | Mogelijke operationalisering |
|---|---|---|
| WP-01 | Bronverwijzingen maken het eenvoudiger om een claim te controleren | Tijd tot het vinden van een relevante bronpassage; juiste bronkeuze |
| WP-02 | Gespecificeerde checks ondersteunen de interpretatie beter dan één totaalscore | Juist begrip van evaluatie en mate van ongegrond vertrouwen |
| WP-03 | Een routevoorstel ondersteunt prioritering | Juistheid van gekozen vervolgactie in gestandaardiseerde scenario's |
| WP-04 | De interface kan tijd besparen zonder de menselijke beoordeling te verslechteren | Beoordelingstijd én foutdetectie/juistheid tegenover een baseline |
| WP-05 | Het onderscheid tussen de analyst- en engineerrol verbetert taakgerichtheid | Taaksucces en interpretatie per doelgroep |

## 6. Open onderzoeksvragen

1. Welke fouten of omissies zijn voor analisten materieel bij de verschillende documentsoorten?
2. Welke checks zijn valide en uitvoerbaar met de beschikbare brondata?
3. Welke vorm van onzekerheidscommunicatie voorkomt ongerechtvaardigd vertrouwen?
4. Wanneer levert een routeadvies aantoonbare meerwaarde ten opzichte van handmatige documentcontrole?
5. Welke metrics zijn beschikbaar voor eerlijke modelversievergelijkingen?

## 7. Vervolg

De stakeholders, interactiepatronen en concrete UI-uitwerkingen zijn verder uitgewerkt in [02-Stakeholderanalyse](02-Stakeholderanalyse.md), [03-Design-patterns](03-Design-patterns.md) en [04-UI-concept](04-UI-concept.md). Validatievoorstellen staan in [05-Validatieplan](05-Validatieplan.md).

[Terug naar ontwerpindex](README.md)
