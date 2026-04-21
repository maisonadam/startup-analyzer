from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib import colors

# --- DOKUMENT ---
doc = SimpleDocTemplate(
    "apheris_deep_analysis.pdf",
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm
)

# --- FARBEN ---
DUNKELBLAU = colors.HexColor('#1a2744')
HELLGRAU = colors.HexColor('#f5f5f5')
ROT = colors.HexColor('#c0392b')
GRUEN = colors.HexColor('#27ae60')

# --- STYLES ---
styles = getSampleStyleSheet()

titel = ParagraphStyle('Titel', parent=styles['Normal'],
    fontSize=22, textColor=DUNKELBLAU, spaceAfter=4, fontName='Helvetica-Bold')

untertitel = ParagraphStyle('Untertitel', parent=styles['Normal'],
    fontSize=11, textColor=colors.grey, spaceAfter=20, spaceBefore=20)

h2 = ParagraphStyle('H2', parent=styles['Normal'],
    fontSize=14, textColor=DUNKELBLAU, spaceAfter=8, spaceBefore=16,
    fontName='Helvetica-Bold')

h3 = ParagraphStyle('H3', parent=styles['Normal'],
    fontSize=11, textColor=DUNKELBLAU, spaceAfter=6, spaceBefore=10,
    fontName='Helvetica-Bold')

text = ParagraphStyle('Text', parent=styles['Normal'],
    fontSize=9.5, spaceAfter=6, leading=14)

kritik = ParagraphStyle('Kritik', parent=styles['Normal'],
    fontSize=9.5, spaceAfter=6, leading=14, textColor=ROT)

empfehlung = ParagraphStyle('Empfehlung', parent=styles['Normal'],
    fontSize=9.5, spaceAfter=6, leading=14, textColor=GRUEN)

# --- DATEN ---
STAERKEN = [
    "Löst ein fundamentales strukturelles Problem der Pharmaindustrie",
    "Tier-1 Kunden: Roche und Johnson & Johnson bereits an Bord",
    "DSGVO als permanenter regulatorischer Rückenwind",
    "High Switching Costs schützen Kundenbeziehungen langfristig",
    "Frisches Series A Funding: €20.1M Januar 2025",
    "Neutraler Anbieter – struktureller Vorteil gegenüber AWS/Google",
]

RISIKEN = [
    "Big Tech Risiko: AWS und Google könnten den Markt mit günstigeren Alternativen betreten",
    "Langer Sales Cycle von 6-18 Monaten bremst Wachstum",
    "Klumpenrisiko: wenige große Kunden bedeuten hohe Abhängigkeit",
    "Vertikale Abhängigkeit: starker Fokus auf Life Sciences",
    "Kleines Team von ~20 Personen für komplexen Enterprise Sales",
]

EMPFEHLUNGEN = [
    "Spezialisierung vertiefen – Life Sciences Expertise als unkopierbaren Moat ausbauen",
    "Weitere Vertikale erschließen – Climate Tech und Finanzwesen als nächste Märkte",
    "Partnerschaftsstrategie mit Krankenhäusern und Universitäten beschleunigen",
    "Community aufbauen – Datenwissenschaftler als Multiplikatoren gewinnen",
    "Sales Cycle verkürzen durch standardisierte Pilotprojekte",
]

# --- INHALT ---
inhalt = []

inhalt.append(Paragraph("Startup Deep Analysis", titel))
inhalt.append(Paragraph("Apheris AI GmbH · Berlin · April 2026", untertitel))
inhalt.append(HRFlowable(width="100%", thickness=2, color=DUNKELBLAU))
inhalt.append(Spacer(1, 0.4*cm))

# Executive Summary
inhalt.append(Paragraph("Executive Summary", h2))
inhalt.append(Paragraph(
    "Apheris ist ein Berliner DeepTech Startup das sichere Dateninfrastruktur "
    "für die Pharmaindustrie baut – und damit eines der fundamentalsten Probleme "
    "der modernen Medizinforschung löst: 97% aller Healthcare-Daten bleiben "
    "ungenutzt wegen Datenschutzbedenken. Mit Roche und Johnson & Johnson als "
    "Kunden, €20.1M Series A Funding im Januar 2025 und DSGVO als strukturellem "
    "Rückenwind ist Apheris gut positioniert. "
    "Kritisch: Big Tech Konkurrenz und lange Sales Cycles.",
    text
))
inhalt.append(Spacer(1, 0.3*cm))

# 1. Problem-Solution Fit
inhalt.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
inhalt.append(Paragraph("1. Problem-Solution Fit", h2))
inhalt.append(Paragraph(
    "Apheris löst das Problem der zersplitterten Datenlandschaft und "
    "regulatorischer Datenschutzschranken für Pharmaunternehmen die Milliarden "
    "in Forschung investieren. Diese Unternehmen sitzen auf riesigen Datenschätzen "
    "– können sie aber nicht miteinander teilen weil Datenschutzgesetze und "
    "Wettbewerbsinteressen das verhindern.",
    text
))
inhalt.append(Paragraph(
    "<b>Die Lösung:</b> Federated Computing – die KI geht zu den Daten, nicht "
    "die Daten zur KI. Daten verlassen nie den Server des Eigentümers, werden "
    "aber trotzdem für gemeinsames Machine Learning genutzt.",
    text
))
inhalt.append(Paragraph(
    "<b>Eigene Einschätzung:</b> Der Problem-Solution Fit ist überzeugend und "
    "strukturell tief verankert. Krankheiten sind komplex und haben viele Ursachen "
    "– genetisch, sozial, umweltbedingt. Holistische Daten könnten medizinische "
    "Durchbrüche ermöglichen die mit isolierten Datensätzen unmöglich wären. "
    "Apheris macht genau das möglich – und das ist gesellschaftlich bedeutsam.",
    text
))
inhalt.append(Spacer(1, 0.3*cm))

# 2. Business Model
inhalt.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
inhalt.append(Paragraph("2. Business Model", h2))
inhalt.append(Paragraph(
    "Apheris verkauft sichere Dateninfrastruktur als B2B SaaS an große "
    "Pharmaunternehmen – abgerechnet über jährliche Enterprise-Verträge "
    "im Bereich €100k-500k+ pro Kunde.",
    text
))
inhalt.append(Paragraph(
    "Das Modell hat einen starken natürlichen Moat: Ist ein Pharmaunternehmen "
    "erstmal in die Apheris-Infrastruktur eingebettet ist der Wechsel extrem "
    "aufwändig. High Switching Costs schützen den Umsatz langfristig. "
    "Auf der anderen Seite bedeuten wenige große Kunden hohes Klumpenrisiko "
    "und lange Sales Cycles von 6-18 Monaten bremsen das Wachstum.",
    text
))
inhalt.append(Spacer(1, 0.3*cm))

# 3. Unit Economics
inhalt.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
inhalt.append(Paragraph("3. Unit Economics", h2))

unit_data = [
    ["Metrik", "Wert", "Quelle", "Bewertung"],
    ["Funding Total", "$32.5M", "FAKT – Tracxn/PitchBook", "✅ Solide"],
    ["Letzte Runde", "€20.1M Series A", "FAKT – Jan 2025", "✅ Frisch"],
    ["Team", "~20 Personen", "FAKT – Tracxn Dez 2023", "OK"],
    ["ACV (geschätzt)", "€150k-500k/Jahr", "BENCHMARK B2B DeepTech", "✅ Hoch"],
    ["LTV (geschätzt)", "€1.2-1.6M/Kunde", "SCHÄTZUNG – 8 Jahre", "✅ Sehr hoch"],
    ["CAC (geschätzt)", "€50k-150k", "BENCHMARK Enterprise", "Akzeptabel"],
    ["LTV:CAC Ratio", "~10-16:1", "SCHÄTZUNG", "✅ Exzellent"],
    ["NRR (geschätzt)", "110-130%", "BENCHMARK B2B SaaS", "✅ Stark"],
]

t = Table(unit_data, colWidths=[4*cm, 3.5*cm, 4*cm, 4*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DUNKELBLAU),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, HELLGRAU]),
    ('PADDING', (0,0), (-1,-1), 6),
]))
inhalt.append(t)
inhalt.append(Spacer(1, 0.3*cm))

# 4. Outside-In
inhalt.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
inhalt.append(Paragraph("4. Outside-In Analyse", h2))

markt_data = [
    ["Metrik", "Wert", "Quelle"],
    ["TAM Global", "~$45 Milliarden", "FAKT – Healthcare AI Market 2025"],
    ["SAM Federated Learning", "$3-5 Milliarden", "SCHÄTZUNG"],
    ["SOM Apheris (5J)", "$50-100 Millionen", "SCHÄTZUNG – 1-2% SAM"],
    ["Marktwachstum", "~25% jährlich", "BENCHMARK Healthcare AI"],
    ["Regulatorik", "DSGVO – Rückenwind", "FAKT – EU"],
]

t2 = Table(markt_data, colWidths=[5*cm, 5*cm, 5.5*cm])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DUNKELBLAU),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, HELLGRAU]),
    ('PADDING', (0,0), (-1,-1), 6),
]))
inhalt.append(t2)
inhalt.append(Spacer(1, 0.3*cm))

# 5. Kritische Analyse
inhalt.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
inhalt.append(Paragraph("5. Kritische Analyse", h2))

inhalt.append(Paragraph("Stärken", h3))
for s in STAERKEN:
    inhalt.append(Paragraph(f"✅ {s}", empfehlung))

inhalt.append(Spacer(1, 0.2*cm))
inhalt.append(Paragraph("Risiken & Schwächen", h3))
for r in RISIKEN:
    inhalt.append(Paragraph(f"⚠️ {r}", kritik))

inhalt.append(Spacer(1, 0.3*cm))

# 6. Empfehlungen
inhalt.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
inhalt.append(Paragraph("6. Strategische Empfehlungen", h2))
for i, e in enumerate(EMPFEHLUNGEN, 1):
    inhalt.append(Paragraph(f"<b>{i}.</b> {e}", text))

inhalt.append(Spacer(1, 0.3*cm))

# 7. Fazit
inhalt.append(HRFlowable(width="100%", thickness=2, color=DUNKELBLAU))
inhalt.append(Paragraph("7. Fazit", h2))
inhalt.append(Paragraph("<b>Bewertung: INVEST ✅</b>", h3))
inhalt.append(Paragraph(
    "Apheris löst ein fundamentales strukturelles Problem das die gesamte "
    "Pharmaindustrie betrifft – und hat das bereits mit Tier-1 Kunden bewiesen. "
    "Die DSGVO schafft permanenten regulatorischen Rückenwind und das frische "
    "Series A Funding gibt dem Unternehmen die Runway um zu skalieren. "
    "Ein entscheidender Vorteil gegenüber Big Tech: Apheris ist neutral und "
    "unabhängig – Roche wird seine sensibelsten Forschungsdaten niemals auf "
    "Google Cloud verarbeiten. "
    "Entscheidend wird sein ob Apheris schnell genug wächst und eine tiefe "
    "Life-Sciences-Spezialisierung aufbaut bevor Big Tech den Markt mit "
    "günstigeren Alternativen betritt.",
    text
))

inhalt.append(Spacer(1, 0.5*cm))
inhalt.append(Paragraph(
    "Erstellt mit Python & Claude API | Analyse: Adam Marx | April 2026",
    ParagraphStyle('Footer', parent=styles['Normal'],
        fontSize=8, textColor=colors.grey)
))

# --- PDF BAUEN ---
doc.build(inhalt)
print("✅ Apheris Deep Analysis PDF erstellt: apheris_deep_analysis.pdf")
