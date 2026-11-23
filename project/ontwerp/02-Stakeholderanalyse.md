# 02. Stakeholderverkenning en pre-questioning

**Documenttype:** hypothesegedreven stakeholderanalyse  
**Datum:** 23 november 2026  
**Status:** voorlopig; geen uitgevoerde interviews of vastgestelde gebruikersbevindingen

## 1. Doel en onderzoekscontext

Het concept kent twee primaire gebruiksperspectieven: een **analist** die een individuele samenvatting beoordeelt en een **AI-engineer** die de evaluatiemethode en eventuele verschillen tussen samenvattingsmodellen onderzoekt. Hun informatiebehoeften verschillen: directe, begrijpelijke beslisondersteuning tegenover reproduceerbare en gedetailleerde kwaliteitsanalyse.

De hier beschreven behoeften zijn afgeleid uit de aangeleverde casus en ontwerpbrainstorm. Zij moeten door gebruikers of representatieve stakeholders worden bevestigd, bijgesteld of verworpen.

## 2. Stakeholder A — Analist

### Kernvraag

> **Kan ik deze samenvatting vertrouwen?**

### Veronderstelde taakcontext

De analist moet beoordelen of een AI-samenvatting geschikt is voor verdere verwerking. Hierbij kunnen feitelijke afwijkingen, ontbrekende informatie, niet-onderbouwde claims en interpretatie van cijfers relevant zijn.

### Conceptuele functionaliteit

De toepassing presenteert per samenvatting uitgevoerde evaluatiechecks, afzonderlijke resultaten en aandachtspunten. Bij een bevinding kan een koppeling naar de relevante passage in het brondocument worden geopend. Een routevoorstel — **Vertrouwen / Controleren / Afwijzen** — ondersteunt de prioritering; de analist kiest en motiveert de definitieve actie.

### Te onderzoeken vragen

- Welke informatie is nodig voordat de analist een samenvatting accepteert?
- Wordt een totaalscore begrepen, of werkt een set onderbouwde deelchecks beter?
- Leidt de zichtbaarheid van een positief statussignaal tot overmatig vertrouwen?
- Welke fouten worden na presentatie van de interface correct opgemerkt?
- Hoe snel kan een analist van een verdachte claim naar het bijbehorende bronbewijs navigeren?

**Beoogde toetsing:** taakgebaseerde gebruikerstest met bekende juiste, onjuiste, incomplete en onbeslisbare voorbeelden. Observeer keuze, brongebruik, foutdetectie en beoordelingstijd.

## 3. Stakeholder B — AI-engineer

### Kernvraag

> **Is summariser v2 beter dan v1, en waarin?**

### Veronderstelde taakcontext

De engineer vergelijkt versies van een samenvattingsmodel op vergelijkbare documentsets, met gelijke evaluatiecriteria. Eén gemiddeld cijfer is onvoldoende om prestatieverschillen te duiden als sommige fouttypen verbeteren terwijl andere verslechteren.

### Conceptuele functionaliteit

Het ontwerp toont resultaten uitgesplitst naar modelversie, documenttype en evaluatiedimensie. Waar beschikbaar worden **coverage, factual consistency, gemiste relevante informatie, false positives en false negatives** vergeleken. Voorbeelden van fouten en feedback van analisten ondersteunen diepgaand onderzoek.

### Te onderzoeken vragen

- Welke metrics en casussen zijn nodig om v1 en v2 eerlijk te vergelijken?
- Wat is een betekenisvol kwaliteitsverschil en welke onzekerheid hoort daarbij?
- Hoe worden regressies op specifieke fouttypen zichtbaar gemaakt?
- Welke invloed heeft een gewijzigde signaleringsdrempel op precision, recall en reviewlast?
- Hoe worden analystfeedback en modelinstellingen reproduceerbaar vastgelegd?

**Beoogde toetsing:** vergelijkende evaluatietaak met dezelfde, vooraf gelabelde documenten en foutcategorieën voor beide versies. Rapporteer ook spreiding, aantallen en uitzonderingen.

## 4. Verschillende informatiebehoeften

| Ontwerpdimensie | Analist | AI-engineer |
|---|---|---|
| Primaire vraag | Kan deze samenvatting worden gebruikt? | Waarin verschillen modelversies? |
| Detailniveau | Begrijpelijke bevindingen met bronbewijs | Metrics, fouttypen, datasets en configuraties |
| Hoofdactie | Vertrouwen, controleren of afwijzen | Vergelijken, inspecteren en evaluatie-instellingen onderzoeken |
| Belangrijk risico | Onterecht vertrouwen of gemiste fout | Verkeerde interpretatie van metrics of regressies |
| Vereiste controle | Zelf bronnen inzien en advies overrulen | Instellingen en resultaten kunnen controleren en reproduceren |

## 5. Pre-questioning: voorstel voor interviews vóór ontwerpvalidatie

De onderstaande open vragen vermijden waar mogelijk het voorschrijven van een gewenste oplossing.

**Voor analisten**

1. Hoe wordt nu vastgesteld of een samenvatting betrouwbaar genoeg is?
2. Welke type fout leidt meestal tot extra documentcontrole?
3. Welke informatie is noodzakelijk om een afwijking te begrijpen?
4. Wanneer wordt een samenvatting afgewezen in plaats van gecorrigeerd?
5. Hoe wordt momenteel gecontroleerd of belangrijke informatie ontbreekt?

**Voor AI-engineers**

1. Welke evaluatietaken en referentiedata zijn beschikbaar?
2. Welke performanceverschillen tussen modellen zijn werkelijk relevant?
3. Hoe worden fouttypen, gemiste fouten en onterechte waarschuwingen geregistreerd?
4. Wat zijn randvoorwaarden voor reproduceerbare modelversievergelijkingen?
5. Wie mag signaleringsdrempels wijzigen, en hoe wordt het effect gevalideerd?

## 6. Beperkingen

Er zijn nog geen interviewtranscripten, echte gebruikerstestobservaties of andere empirische bevindingen opgenomen. De rollen vormen een eerste analytisch kader; andere belanghebbenden, zoals compliance, privacy/security en teamleiding, kunnen later relevant blijken.

## 7. Vervolg

De behoeftehypothesen worden vertaald naar [design patterns](03-Design-patterns.md), [interfaceconcepten](04-UI-concept.md) en [toetsbare scenario's](05-Validatieplan.md).

[Terug naar ontwerpindex](README.md)
