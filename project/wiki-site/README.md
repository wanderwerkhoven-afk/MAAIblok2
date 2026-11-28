# Projectwiki website

Dit is de broncode van de projectwiki die via GitLab Pages wordt gepubliceerd.

## Lokaal bekijken

1. Installeer Python 3.12.
2. Installeer de dependencies: `python -m pip install -r requirements.txt`.
3. Start de preview vanuit deze map: `mkdocs serve`.
4. Open de lokale URL die MkDocs toont.

De inhoud staat in `docs/` als Markdown. Afbeeldingen en andere figuren komen in `docs/assets/`; verwijs er vanuit een pagina naar met een relatief pad, bijvoorbeeld `![AI-flow](../assets/ai-flow.png)`.

## Publiceren

De root-`.gitlab-ci.yml` bouwt de site en publiceert `project/wiki-site/site` via GitLab Pages wanneer er naar de standaardbranch wordt gepusht. Hetzelfde project kan dus vanuit GitHub met GitLab worden gesynchroniseerd.
