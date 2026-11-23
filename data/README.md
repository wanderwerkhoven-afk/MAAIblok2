# Data — SummaryCheck

Deze map bevat de onderzoeksdocumenten en bijbehorende AI-samenvattingen voor de ontwikkeling en evaluatie van **SummaryCheck**.

## Mappenoverzicht

| Map | Inhoud | Voorbeeld |
|---|---|---|
| [raw/](raw/) | Originele, onbewerkte rapporten (bijvoorbeeld PDF) | `ABN_Annual_Report_2025_v0.pdf` |
| [summaries/](summaries/) | AI-gegenereerde samenvattingen, bij voorkeur per model/promptversie herkenbaar | `ABN_Annual_Report_2025_Summary_v0.pdf` |
| [processed/](processed/) | Afgeleide data, zoals geëxtraheerde tekst, JSON of opgedeelde passages | `abn_amro_2025.json` |
| [evaluations/](evaluations/) | Uitkomsten van evaluatiechecks, scorebestanden en controles | `abn_amro_2025_v1.json` |
| [annotations/](annotations/) | Handmatig beoordeelde claims, bronverwijzingen en referentielabels | `abn_amro_2025_labels.csv` |
| [prompts/](prompts/) | Vastgelegde samenvattingsinstructies en documentatie van hun herkomst | `Summarization_Prompt_v1.md` |

## Bestandsnamen en koppelingen

Geef een origineel document een vaste **document-ID**, bijvoorbeeld `abn_amro_2025`. Gebruik diezelfde ID voor de samenvattingen en latere evaluatieresultaten. Voeg bij meerdere samenvattingen een versie toe (`_v0`, `_v1`, `_v2`), zodat het origineel en de verschillende outputs naast elkaar blijven bestaan.

In [manifest.csv](manifest.csv) staan de drie originele jaarverslagen (ABN AMRO, ING en Rabobank) en de drie bijbehorende **v0-samenvattingen**. Elke rij bevat document-ID, organisatie, jaar, versie, bestandstype en relatief pad. De samenvattingsrijen bevatten daarnaast een verwijzing naar de gedocumenteerde prompt en een afzonderlijk veld **prompt_provenance**.

**Belangrijk voor reproduceerbaarheid:** de opgeslagen [Summarization Prompt v1.0](prompts/Summarization_Prompt_v1.md) is een achteraf gereconstrueerde en gestandaardiseerde versie van de gebruikersinstructies, niet de verifieerbaar exact uitgevoerde prompt voor deze drie bestaande samenvattingen. De manifestwaarde `reconstructed_reference_not_verified_as_executed_prompt` voorkomt dat deze reconstructie wordt verward met een authentieke generatielog. De bestandssuffix `_v0` markeert de historische nulmeting. De ongewijzigde originele jaarverslagen hebben om organisatorische redenen eveneens `_v0` in de bestandsnaam; dit zegt niets over een versie van de bronuitgever. Nieuwe met de gestandaardiseerde prompt gegenereerde samenvattingen krijgen `_Summary_v1.pdf`.

Bij toekomstige generaties is het wenselijk om de exacte prompt, model-ID, model-/API-versie, instellingen, datum en eventuele generatiestappen **op het moment van uitvoering** vast te leggen.

## Werkwijze

1. Plaats de ongewijzigde bron-PDF in `raw/`.
2. Plaats de AI-samenvatting in `summaries/`, met dezelfde document-ID en een versienaam.
3. Voeg beide bestanden als afzonderlijke rijen aan `manifest.csv` toe.
4. Registreer bij nieuwe samenvattingen de exact gebruikte prompt en modelinstellingen in het manifest en de promptdocumentatie.
5. Sla latere tekstextracties, evaluatie-uitkomsten en handmatige referenties in de bijpassende mappen op.
6. Wijzig originele bronbestanden niet achteraf; leg eventuele verwerkingen apart vast.

**Let op:** de repository is openbaar. Upload alleen publiek beschikbare of aantoonbaar voor publicatie toegestane rapporten en samenvattingen. Geen vertrouwelijke kredietdossiers, persoonsgegevens, API-sleutels of andere gevoelige informatie toevoegen. Controleer bij grote PDF-bestanden de limieten van Git en overweeg Git LFS.

[Terug naar projectoverzicht](../README.md)
