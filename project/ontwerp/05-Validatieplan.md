# 05. Voorlopig validatieplan — SummaryCheck

**Documenttype:** conceptueel gebruikersonderzoek en evaluatieprotocol  
**Datum:** 23 november 2026  
**Status:** voorstel, niet uitgevoerd

## 1. Onderzoeksdoel

De gebruikersevaluatie moet vaststellen of het SummaryCheck-concept de juiste betekenis overbrengt, of gebruikers met evaluatiesignalen passende vervolgstappen kiezen en of brongebonden uitleg het controleren van AI-samenvattingen ondersteunt. De engineerinterface moet afzonderlijk worden getest op correcte interpretatie van modelvergelijkingen en foutdetectiedrempels.

## 2. Onderzoeksvragen

1. Kunnen analisten de betekenis van de drie routes en hun beperkingen correct uitleggen?
2. Leidt de beschikbaarheid van claim-naar-bronverwijzingen tot effectievere controle?
3. In welke mate beïnvloeden scorevorm en kleurgebruik de inschatting van betrouwbaarheid?
4. Herkennen gebruikers het verschil tussen **geen problemen gevonden**, **onvoldoende bewijs** en **evaluatie mislukt**?
5. Kan een engineer de afweging tussen gemiste fouten en onterechte waarschuwingen correct interpreteren?

## 3. Te vergelijken ontwerpvarianten

| Variant | Verandering | Te onderzoeken effect |
|---|---|---|
| A | Ringmeter met expliciet label en detailchecks | Begrip, snelheid en schijnzekerheid |
| B | Alleen afzonderlijke checkresultaten | Vergelijking met de geaggregeerde ring |
| C | Claim-naar-bronlink met passagehighlight | Controleerbaarheid en tijd tot bewijs |
| D | Bronpassage zonder automatische highlight | Verschil in aandachtsturing en interpretatie |

De varianten staan schematisch in [assets/ui-varianten.svg](assets/ui-varianten.svg). Binnen een beperkte steekproef kunnen A/B en C/D als afzonderlijke taken of pilotvergelijkingen worden getest.

## 4. Scenario's voor analisten

| ID | Voorgelegde toestand | Vraag/taak | Observeerbare uitkomst |
|---|---|---|---|
| T1 | Groenblauw: geen aandachtspunten gevonden | 'Wat betekent dit resultaat? Wat zou u nu doen?' | Begrip dat de samenvatting niet gegarandeerd juist is |
| T2 | Oranje: twee aandachtspunten | 'Welk onderdeel controleert u eerst? Waar klikt u?' | Selectie check en navigatie naar relevante claim |
| T3 | Rood: belangrijke onbevestigde claim | 'Kan deze claim worden gebruikt? Waarom?' | Afweging op basis van bewijs in plaats van alleen kleur |
| T4 | Bronverwijzing bij omzetclaim | 'Zoek de passage waarmee u dit cijfer kunt controleren.' | Juiste bronpassage en verificatie |
| T5 | Samenvatting mist belangrijke informatie | 'Meld het probleem in de applicatie.' | Juist feedbacktype en begrijpelijke toelichting |
| T6 | Evaluatie technisch mislukt | 'Wat is er beoordeeld en wat kunt u nu doen?' | Herkennen dat géén kwaliteitsuitspraak is afgegeven |
| T7 | Onjuist routevoorstel | 'Het systeem adviseert Vertrouwen, maar de bron spreekt dit tegen. Wat doet u?' | Kritisch overrulen en vastleggen van reden |

## 5. Scenario's voor AI-engineers

| ID | Voorgelegde toestand | Vraag/taak | Observeerbare uitkomst |
|---|---|---|---|
| E1 | v1 en v2 met scores per criterium | 'Welke versie scoort beter, en op welke criteria niet?' | Correcte interpretatie van verschillen |
| E2 | Hoge recall, lage precision | 'Wat gebeurt er vermoedelijk met de reviewlast?' | Begrip van false positives en gemiste fouten |
| E3 | Nieuwe foutmelding van analist | 'Waar is de melding terug te vinden en wat is de status?' | Correct onderscheid tussen ontvangen, beoordeeld en opgelost |
| E4 | Niet-vergelijkbare testsets | 'Is een directe modelvergelijking op basis van deze gegevens geldig?' | Herkennen van methodologische beperkingen |

## 6. Voorstel voor methodiek

1. **Pre-questioning:** korte semigestructureerde vragen over huidige werkwijze en relevante fouten, zonder SummaryCheck direct als oplossing te presenteren.
2. **Taakgebaseerde prototypesessie:** presenteer gestandaardiseerde scenario's met vooraf vastgelegde waarheidstoestand en gewenste controlehandeling.
3. **Think-aloud:** vraag deelnemers hun interpretatie toe te lichten zonder corrigerende hints te geven.
4. **Post-task vragen:** begrip van meldingen, ervaren duidelijkheid, ervaren werkbelasting en voorkeuren.
5. **Analyse:** codeer gemaakte keuzes, verkeerde interpretaties, benodigde stappen en het verloop per scenario.

De steekproefomvang en rekrutering moeten worden afgestemd op beschikbaarheid; een kleine kwalitatieve pilot ondersteunt ontwerpverbetering, maar is onvoldoende om brede prestatieclaims te onderbouwen.

## 7. Voorgestelde meetmaten

| Meetmaat | Operationalisering | Interpretatiebeperking |
|---|---|---|
| Taaksucces | Percentage taken waarbij een vooraf gedefinieerde juiste handeling is voltooid | Vereist onafhankelijke referentie-uitkomst |
| Foutdetectie | Aantal / aandeel correct gevonden materiële fouten | Afhankelijk van fouttype en voorbeeldselectie |
| Gemiste fouten | Aantal bekende fouten die gebruiker niet identificeert | Onderscheid gebruikersgedrag en modelcheck |
| Onterechte acceptatie | Acceptatie van samenvatting met vooraf bekende materiële fout | Kan onder meer door interface, tijdsdruk of taakcontext komen |
| Beoordelingstijd | Start taak tot definitieve keuze, met eenduidig start- en eindpunt | Korter is niet automatisch beter |
| Bronverificatie | Correct geselecteerde bronpassage en benodigde tijd | Bronkoppeling kan onjuist of ambigu zijn |
| Begrip van onzekerheid | Juiste uitleg van de betekenis en beperkingen van de status | Beoordelen met vooraf vastgesteld coderingsschema |
| Subjectieve bruikbaarheid | Korte post-task schaal en open toelichting | Zelfrapportage is geen objectieve kwaliteitsmeting |

**Vergelijking van ontwerpen:** gebruik voor dezelfde taaktypen bij voorkeur even moeilijke scenario's, wissel de volgorde van condities waar mogelijk af en leg wijzigingen in het testprotocol vast. Scheid exploratieve observaties van confirmatieve conclusies.

## 8. Voorbeeldvragen na een taak

- 'Wat vertelt deze status volgens u over de samenvatting?'
- 'Welke informatie ontbreekt om een definitieve keuze te kunnen maken?'
- 'Welke knop zou u nu gebruiken en waarom?'
- 'Wat verwacht u dat er gebeurt wanneer u op deze actie klikt?'
- 'Waarop baseert u uw vertrouwen in deze specifieke claim?'
- 'Was de verwijzing naar het oorspronkelijke document voldoende om de claim te controleren?'

Vermijd leidende vragen zoals 'Vindt u deze handige controlefunctie duidelijk?'.

## 9. Registratie van bevindingen

Per taak wordt vastgelegd: anonieme deelnemerscode, gebruikersrol, scenarioversie, getoonde UI-variant, waargenomen actie, eventuele verkeerde interpretatie, tijd (indien gemeten), relevante uitspraken en een beschrijving van de noodzakelijke ontwerpverbetering.

### Sjabloon

| Deelnemer | Taak | Variant | Actie | Correct? | Tijd | Observatie | Verbeteridee |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

Er zijn nog geen resultaten ingevuld. Resultaten worden na uitvoering samengevat in [Wiki — Evaluatie](../../wiki/Evaluatie.md).

## 10. Privacy en onderzoeksintegriteit

Leg het doel van het onderzoek uit, vraag passende toestemming, vermijd het vastleggen van onnodige persoonsgegevens en beperk toegang tot onderzoeksdata. Gebruik fictieve of geautoriseerde financiële documenten. Rapporteer beperkingen van de steekproef, afwijkingen van het protocol en negatieve bevindingen.

[Terug naar ontwerpindex](README.md)
