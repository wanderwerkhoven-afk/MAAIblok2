# Samenvattingsprompts — SummaryCheck

Deze map documenteert de instructies die bij het samenstellen van samenvattingen worden gebruikt of achteraf zijn gereconstrueerd. Dit ondersteunt herleidbaarheid en methodologische transparantie.

| Document | Beschrijving | Herkomst |
|---|---|---|
| [Summarization_Prompt_v1.md](Summarization_Prompt_v1.md) | Uitgebreide instructie voor een ongeveer 10%-samenvatting met hiërarchische chunking, behoud van feiten en financiële cijfers, consistente PDF-opmaak en expliciete kwaliteitscontroles | **Gereconstrueerd en gestandaardiseerd op 23-11-2026; niet aangetoond als exact uitgevoerde prompt voor de bestaande samenvattingen** |

## Herkomst en versiebeheer

De oorspronkelijke v1-PDF's van ABN AMRO, ING en Rabobank zijn eerder met ChatGPT gemaakt. Uit de eerdere opdracht zijn onder meer de 10%-doelstelling, de gevraagde hierarchical chunk-merging-aanpak en de consistente opmaak bekend. De volledige exacte uitvoeringsprompt, interne stappen en modelinstellingen zijn echter niet beschikbaar als verifieerbare generatielog.

**Belangrijk:** de titel `v1.0` van het promptdocument is een **documentversie**, geen bewijs dat die prompt letterlijk bij de bestaande `Summary_v1.pdf`-bestanden is gebruikt.

Het [manifest](../manifest.csv) verwijst bij de bestaande samenvattingen naar deze prompt als *reconstructed reference* en legt deze onzekerheid expliciet vast. Bij volgende generaties moet vóór uitvoering een stabiele promptversie worden opgeslagen, samen met exacte model- en procesmetadata.

[Terug naar data-overzicht](../README.md)
