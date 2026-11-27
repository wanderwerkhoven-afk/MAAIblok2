# Ontwerpiteratie 01 — SummaryCheck

**Datum oorspronkelijke schets:** 27 november 2026  
**Status:** werkend HTML-concept met echte PDF-weergave en heuristische bronvoorstellen; nog niet gevalideerd via een gebruikerstest.

## Aanleiding

De eerste handgetekende schets voorzag in een Rabobank-dashboard, uploadmogelijkheid, een samenvattingsvenster, cirkelvormige kwaliteitsindicatoren en markeringen van claims en brontekst. Daarnaast werden een LLM-judge en spaCy als mogelijke technische componenten genoemd.

In eerste instantie zijn scorecirkels en fictieve claims als demonstratie uitgewerkt. In de latere revisie van iteratie 01 zijn deze **uit het actuele HTML-prototype verwijderd** en vervangen door daadwerkelijk ingelezen PDF-documenten en automatisch gevonden mogelijke bronverwijzingen.

## Bestanden

| Bestand | Inhoud |
|---|---|
| [prototype.html](prototype.html) | Interactieve single-file HTML-interface voor echte PDF-upload, documentvergelijking, tekstextractie en bronvoorstellen |
| [Design-patterns-en-keuzes.md](Design-patterns-en-keuzes.md) | Historie en verantwoording van ontwerpkeuzes, inclusief verwijdering van fictieve scores en vervanging door echte documenten |

## Werkende functionaliteit

1. **Datasetkeuze:** ABN AMRO, ING of Rabobank, elk met een origineel v0-jaarverslag en een bijbehorende v0-samenvatting uit de repository.
2. **Lokale upload:** origineel en samenvatting afzonderlijk als PDF selecteren.
3. **Documentviewer:** werkelijk gerenderde PDF-pagina's in twee kolommen, onafhankelijk bladeren en zoomen.
4. **Inhoudelijke documentgegevens:** werkelijk aantal PDF-pagina's, geschatte woordenaantallen op basis van PDF-tekstextractie en indicatieve tekstreductie.
5. **Bronverwijzingen:** een reeks zinnen wordt uit de echte samenvatting geëxtraheerd. De tool zoekt maximaal drie mogelijk relevante bronpagina's op basis van overeenkomst van betekenisvolle woorden en toont een tekstfragment.
6. **Navigatie naar bron:** een bronvoorstel opent de geselecteerde PDF-pagina; overlappende woorden worden met een gele markering aangeduid.
7. **Menselijke beslisopties:** lokaal demonstratielabel voor controle of afwijzing; nog geen opslag, workflow of beoordelingsbackend.

## Geen bewezen AI-evaluatie

De bronverwijzingen zijn **heuristische tekstmatches**. Ze kunnen een relevante bron aanwijzen, maar bewijzen **niet** dat de samenvattingsclaim feitelijk correct is. Er kan bijvoorbeeld een getal verkeerd zijn weergegeven, een ontkenning zijn weggelaten of een andere passage dezelfde termen bevatten. Ook is een ontbrekende match geen bewijs voor een onjuiste claim.

Er zijn geen fictieve betrouwbaarheidsscores meer in het actuele prototype. De procentuele tekstreductie is alleen een beschrijvende maat op basis van geëxtraheerde PDF-tekst. Een getoond percentage woordoverlap betreft geen gekalibreerde kans op juistheid.

Er is nog geen LLM-judge, spaCy-verwerking, semantische verificatie, OCR of formele evaluatiemethode geïntegreerd.

## Stijl en interactie

De visuele vormgeving volgt de aangeleverde referentiepagina's uit het Rabobank Annual Report 2025: een witte achtergrond, helderblauwe (soms cursieve) koppen, oranje kerncijfers en accenten, dunne scheidingslijnen en sobere rechthoekige panelen. Originele illustraties en foto's uit het rapport zijn niet overgenomen.

## Technische aanpak

De toepassing gebruikt Mozilla PDF.js via een vastgepinde externe CDN-versie (`3.11.174`). PDF-pagina's worden op canvas gerenderd; `getTextContent()` levert de te doorzoeken tekst. Lokale PDF's worden met `File.arrayBuffer()` geopend en niet naar een applicatieserver gestuurd. De publieke repository-PDF's worden op verzoek gedownload vanuit de repository. Selecties en beslissingen worden bij opnieuw laden niet bewaard.

De bronindex wordt in de browser opgebouwd; het uitlezen van omvangrijke rapporten kan merkbaar tijd kosten. Gescande documenten zonder tekstlaag zijn niet goed doorzoekbaar zonder OCR. Netwerktoegang is nodig om PDF.js en bestaande repositorydocumenten op te halen.

## Testplan en open vragen

- **Juistheid bronvoorstellen:** bepaal met menselijke referentieannotaties hoe vaak de relevante bronpagina in de top drie wordt gevonden.
- **False matches:** test expliciet gewijzigde bedragen, jaartallen, ontkenningen en numerieke tegenstrijdigheden.
- **Begrip:** controleer of analisten een woordoverlap-score onderscheiden van feitelijke juistheid.
- **UX:** test of analisten via een voorgestelde bronpagina sneller tot een onderbouwde beslissing komen dan zonder verwijzing.
- **Techniek:** test prestaties bij grote documenten, verschillende PDF-indelingen, mobiele schermen en ontbrekende netwerktoegang.

**Validatiestatus:** de code is opgeslagen in de repository, maar een volledige browsertest met de echte rapporten en een stakeholdervalidatie zijn nog niet gerapporteerd.

[Prototype openen](prototype.html) · [Design patterns en keuzes](Design-patterns-en-keuzes.md) · [Alle ontwerpiteraties](../README.md) · [Ontwerpdossier](../../README.md)
