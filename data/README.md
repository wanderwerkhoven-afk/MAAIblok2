# Data — SummaryCheck

Deze map bevat de onderzoeksdocumenten en bijbehorende AI-samenvattingen voor de ontwikkeling en evaluatie van **SummaryCheck**.

## Mappenoverzicht

| Map | Inhoud | Voorbeeld |
|---|---|---|
| [raw/](raw/) | Originele, onbewerkte rapporten (bijvoorbeeld PDF) | `abn_amro_2025.pdf` |
| [summaries/](summaries/) | AI-gegenereerde samenvattingen, bij voorkeur per model/promptversie herkenbaar | `abn_amro_2025_v1.pdf` |
| [processed/](processed/) | Afgeleide data, zoals geëxtraheerde tekst, JSON of opgedeelde passages | `abn_amro_2025.json` |
| [evaluations/](evaluations/) | Uitkomsten van evaluatiechecks, scorebestanden en controles | `abn_amro_2025_v1.json` |
| [annotations/](annotations/) | Handmatig beoordeelde claims, bronverwijzingen en referentielabels | `abn_amro_2025_labels.csv` |

## Bestandsnamen en koppelingen

Geef een origineel document een vaste **document-ID**, bijvoorbeeld `abn_amro_2025`. Gebruik diezelfde ID voor de samenvattingen en latere evaluatieresultaten. Voeg bij meerdere samenvattingen een versie toe (`_v1`, `_v2`), zodat het origineel en de verschillende outputs naast elkaar blijven bestaan.

In [manifest.csv](manifest.csv) worden bestanden geregistreerd met document-ID, organisatie, jaar, versie, type en relatief pad. Het manifest bevat voorlopig alleen de kolomnamen; voeg een rij toe voor elk geplaatst document of gegenereerde samenvatting. Later kunnen onder andere model, promptversie, datum, bronlink en evaluatieconfiguratie worden toegevoegd.

## Werkwijze

1. Plaats de ongewijzigde bron-PDF in `raw/`.
2. Plaats de AI-samenvatting in `summaries/`, met dezelfde document-ID en een versienaam.
3. Voeg beide bestanden als afzonderlijke rijen aan `manifest.csv` toe.
4. Sla latere tekstextracties, evaluatie-uitkomsten en handmatige referenties in de bijpassende mappen op.
5. Wijzig originele bronbestanden niet achteraf; leg eventuele verwerkingen apart vast.

**Let op:** de repository is openbaar. Upload alleen publiek beschikbare of aantoonbaar voor publicatie toegestane rapporten en samenvattingen. Geen vertrouwelijke kredietdossiers, persoonsgegevens, API-sleutels of andere gevoelige informatie toevoegen. Controleer bij grote PDF-bestanden de limieten van Git en overweeg Git LFS.

[Terug naar projectoverzicht](../README.md)
