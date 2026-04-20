# Startup Analyzer

Dieses Tool analysiert automatisiert mithilfe von KI ein Startup
und prüft es auf Entwicklungschancen.

## Warum habe ich das gebaut?

Ich habe dieses Tool gebaut um zu verstehen, an welchen Stellen
man ein Business-Modell optimieren kann und um gleichzeitig
geschulter im automatisierten Lösen von Aufgaben mithilfe von
KI zu werden. Als angehender Founders Associate oder Product
Manager ist strukturiertes Startup-Screening eine Kernkompetenz.

## Was kann es?

Das Tool untersucht ein Unternehmen in vier Stufen:

1. **Problem-Solution Fit** – Die Werthypothese des Startups
   wird herausgearbeitet: Welches Problem wird gelöst und für wen?

2. **Business Model** – Das Geschäftsmodell wird qualitativ
   analysiert: Wie verdient das Startup Geld?

3. **Unit Economics** – Kosten und Erträge werden auf die
   kleinste Einheit heruntergebrochen: LTV, CAC, Churn Rate
   und MRR.

4. **Outside-In Analyse** – Das Marktumfeld wird untersucht:
   TAM, SAM, SOM, Wettbewerb und regulatorische Chancen.

## Output

Das Tool generiert zwei PDF-Reports:

**1. Basis-Analyse** (`ahead_analyse.pdf`)
Eine strukturierte Übersicht der vier Analyse-Stufen.

**2. Deep Analysis** (`ahead_deep_analysis.pdf`)
Eine kritische Investment-Analyse mit eigenen Einschätzungen,
Stärken/Risiken-Bewertung und strategischen Empfehlungen –
im VC-Stil mit Executive Summary und WATCH/INVEST/PASS Urteil.

## Tech Stack

- **Python** – Programmiersprache
- **Claude API (Anthropic)** – KI-gestützte Analyse
- **ReportLab** – PDF-Generierung
- **Git & GitHub** – Versionskontrolle

## Limitierungen & nächste Schritte

Die aktuelle Version basiert auf manuell recherchierten Daten.
Geplant: automatisches Datenpulling über Crunchbase API,
App Store API und Similarweb.
