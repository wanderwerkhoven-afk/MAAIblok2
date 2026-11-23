# Ontwerp — SummaryCheck

[← Wiki-startpagina](README.md) · [Ontwikkeling →](Ontwikkeling.md)

Deze pagina verwijst naar het gestructureerde ontwerpdossier voor **SummaryCheck**. Het concept onderzoekt hoe evaluatiechecks, scores, bewijsverwijzingen en een routevoorstel analisten kunnen ondersteunen bij het beoordelen van AI-gegenereerde samenvattingen van jaarverslagen, kredietrapporten en dossiers.

> **Status: ontwerpverkenning (23 november 2026).** Onderstaande ontwerpbeslissingen zijn voorstellen, tenzij ze afzonderlijk in [Besluiten en wijzigingen](Besluiten-en-wijzigingen.md) zijn vastgesteld. Gebruikerseffecten en modelprestaties zijn nog niet empirisch aangetoond.

## Ontwerpdossier

| Document | Inhoud |
|---|---|
| [Ontwerpmap — README](../project/ontwerp/README.md) | Overzicht, scope en navigatie |
| [01 — Waardepropositie](../project/ontwerp/01-Waardepropositie.md) | Doelgroep, waardepropositieformat, probleemverkenning en aannames |
| [02 — Stakeholderanalyse](../project/ontwerp/02-Stakeholderanalyse.md) | Analist: 'Kan ik deze samenvatting vertrouwen?' en engineer: 'Is v2 beter dan v1?' |
| [03 — Design patterns](../project/ontwerp/03-Design-patterns.md) | PAIR-gerelateerde patronen en vertaling naar toetsbare interacties |
| [04 — UI-concept](../project/ontwerp/04-UI-concept.md) | Scoreweergave, bronverwijzingen, highlights, schermen, knoppen en berichten |
| [05 — Validatieplan](../project/ontwerp/05-Validatieplan.md) | Onderzoeksvragen, scenario's, vragenlijstonderdelen en observatiematen |
| [UI-varianten (SVG)](../project/ontwerp/assets/ui-varianten.svg) | Schematische vergelijking van score, bronlink en highlights |

## Gebruikers en context

De analist controleert individuele samenvattingen op bruikbaarheid en onderbouwing. De AI-engineer vergelijkt evaluatie-uitkomsten tussen modelversies en onderzoekt fouttypen en instellingen. Deze behoeften vormen vooralsnog hypotheses die in stakeholderonderzoek worden gevalideerd.

## Voorlopige ontwerpcriteria

| ID | Eis of criterium | Prioriteit (voorstel) | Onderbouwing | Toetsing |
|---|---|---|---|---|
| O-01 | Iedere risicomelding maakt duidelijk welke claim wordt bedoeld | Hoog | Navolgbaarheid van de beoordeling | Claimidentificatie in gebruikerstest |
| O-02 | Relevante bronpassages zijn opvraagbaar | Hoog | Zelfstandige verificatie | Bronzoektaak |
| O-03 | De eindbeslissing blijft bij de analist | Hoog | Menselijk toezicht | Override-scenario |
| O-04 | Evaluatiefalen wordt onderscheiden van een goede evaluatie-uitkomst | Hoog | Voorkomen van schijnzekerheid | Faalstatus-scenario |
| O-05 | Scores hebben duidelijke definitie en beperkingen | Hoog | Betekenisvolle interpretatie | Begripstest |
| O-06 | Engineer kan modelversies op vergelijkbare datasets en checks beoordelen | Middel | Eerlijke modelvergelijking | Engineer-taak |

## Oplossingsrichtingen en afwegingen

De huidige verkenning bevat drie aanvullende UI-opties: **circulaire score-indicator**, **verwijzing van claim naar bronpassage** en **highlights in het originele document**. De verwachte gebruikswaarde en risico's staan in [04 — UI-concept](../project/ontwerp/04-UI-concept.md). Deze opties zijn niet als definitieve keuzes vastgesteld.

## Kern van het concept

- **Input:** origineel document en AI-samenvatting.
- **Verwerking:** brongebonden evaluatiechecks met expliciete beperkingen.
- **Output:** gespecificeerde signalen, mogelijke fouten, bronverwijzingen en routevoorstel.
- **Menselijke beslissing:** Vertrouwen / Controleren / Afwijzen.
- **Bekende beperkingen:** onjuiste/missende bronkoppelingen, onvolledige checks, schijnprecisie en mogelijke automation bias.

## Vervolg en vastlegging

Vervolgonderzoek moet inzicht bieden in de betekenis die gebruikers geven aan scores, kleuren en berichten, de praktische controleerbaarheid van claims en verschillen tussen UI-varianten. Resultaten worden opgenomen in [Evaluatie](Evaluatie.md); besluiten en bijbehorende onderbouwing worden vastgelegd in [Besluiten en wijzigingen](Besluiten-en-wijzigingen.md).

---

[Naar onderzoek](Onderzoek.md) · [Naar ontwikkeling](Ontwikkeling.md) · [Naar evaluatie](Evaluatie.md)
