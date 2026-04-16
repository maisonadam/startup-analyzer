from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

# --- DOKUMENT ERSTELLEN ---
doc = SimpleDocTemplate(
    "ahead_analyse.pdf",
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm
)

# --- STYLES ---
styles = getSampleStyleSheet()
titel_style = ParagraphStyle(
    'Titel',
    parent=styles['Heading1'],
    fontSize=20,
    spaceAfter=12
)
abschnitt_style = ParagraphStyle(
    'Abschnitt',
    parent=styles['Heading2'],
    fontSize=14,
    spaceAfter=8,
    spaceBefore=16
)
text_style = ParagraphStyle(
    'Text',
    parent=styles['Normal'],
    fontSize=10,
    spaceAfter=6
)
# --- INHALTE ERSTELLEN ---
inhalt = []

# Titel
inhalt.append(Paragraph("Startup Analyse: Ahead Solutions", titel_style))
inhalt.append(Paragraph("Erstellt mit Python & Claude API | April 2026", text_style))
inhalt.append(Spacer(1, 0.5*cm))

# 1. Problem-Solution Fit
inhalt.append(Paragraph("1. Problem-Solution Fit", abschnitt_style))
inhalt.append(Paragraph(
    "Ahead adressiert das Problem der emotionalen Selbststeuerung. "
    "Viele Menschen merken dass sie in Konflikten, unter Stress oder in "
    "Beziehungen nicht so reagieren wie sie es möchten. Therapie ist teuer "
    "und stigmatisiert – Ahead bietet eine zugängliche Alternative.",
    text_style
))
inhalt.append(Paragraph("<b>Kernhypothese:</b> Verhaltensänderung entsteht durch "
    "wiederholtes Üben in echten Momenten – nicht durch Wissensvermittlung.", 
    text_style
))
inhalt.append(Paragraph("<b>Zielgruppe:</b> Funktionale Erwachsene (25-45 Jahre) "
    "in akuten Lebensphasen – Burnout, Beziehungsprobleme, Jobstress.", 
    text_style
))
inhalt.append(Spacer(1, 0.3*cm))

# 2. Business Model
inhalt.append(Paragraph("2. Business Model", abschnitt_style))
inhalt.append(Paragraph(
    "Ahead nutzt ein Freemium-Modell mit Premium-Subscription. "
    "Die App ist kostenlos erhältlich, voller Zugang erfordert ein Abo. "
    "Langfristig ist ein B2B-Kanal über Arbeitgeber geplant.",
    text_style
))

# Preistabelle
preis_daten = [
    ["Modell", "Preis", "Bemerkung"],
    ["Monatlich", "€19.99", "Höchster Preis pro Monat"],
    ["Quartal", "€39.99", "€13.33/Monat"],
    ["Jährlich", "€99.00", "€8.25/Monat – Empfohlen"],
    ["Lifetime", "€149.00", "Einmalig"],
]

preis_tabelle = Table(preis_daten, colWidths=[4*cm, 3*cm, 8*cm])
preis_tabelle.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.black),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.lightgrey]),
    ('PADDING', (0,0), (-1,-1), 6),
]))
inhalt.append(preis_tabelle)
inhalt.append(Spacer(1, 0.3*cm))
# 3. Unit Economics
inhalt.append(Paragraph("3. Unit Economics", abschnitt_style))
inhalt.append(Paragraph(
    "Basierend auf verifizierten Preisdaten und Branchen-Benchmarks. "
    "Alle Schätzungen sind transparent gekennzeichnet.",
    text_style
))

unit_daten = [
    ["Metrik", "Wert", "Quelle"],
    ["Preis Jahresabo", "€99/Jahr", "FAKT – App Store"],
    ["App Bewertungen", "1.515 (4.6★)", "FAKT – App Store Apr 2026"],
    ["Team", "~16 Personen", "FAKT – LinkedIn Apr 2026"],
    ["Funding", "€1.12M Pre-Seed", "FAKT – Crunchbase"],
    ["LTV (Jahresabo)", "€118", "SCHÄTZUNG – 7% Churn"],
    ["CAC Benchmark", "€40", "BENCHMARK – Mental Health Apps"],
    ["LTV:CAC Ratio", "2.9:1 ⚠️", "SCHÄTZUNG – unter Ziel 3:1"],
    ["MRR Schätzung", "€12.499", "SCHÄTZUNG – konservativ"],
]

unit_tabelle = Table(unit_daten, colWidths=[5*cm, 4*cm, 6*cm])
unit_tabelle.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.black),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.lightgrey]),
    ('PADDING', (0,0), (-1,-1), 6),
]))
inhalt.append(unit_tabelle)
inhalt.append(Spacer(1, 0.3*cm))

# 4. Outside-In Analyse
inhalt.append(Paragraph("4. Outside-In Analyse", abschnitt_style))

markt_daten = [
    ["Metrik", "Wert", "Quelle"],
    ["TAM Global", "$8.5 Milliarden", "FAKT – Grand View Research 2025"],
    ["SAM Europa", "$2.23 Milliarden", "FAKT – Grand View Research 2025"],
    ["SOM Ahead", "~$22 Millionen", "SCHÄTZUNG – 1% Marktanteil"],
    ["Marktwachstum", "15% jährlich", "FAKT – Grand View Research 2025"],
    ["DiGA Wachstum", "+63% (2024→2025)", "FAKT – Ärzteblatt Apr 2026"],
    ["Ahead DiGA Status", "Nicht zertifiziert", "FAKT – BfArM"],
]

markt_tabelle = Table(markt_daten, colWidths=[5*cm, 4*cm, 6*cm])
markt_tabelle.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.black),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.lightgrey]),
    ('PADDING', (0,0), (-1,-1), 6),
]))
inhalt.append(markt_tabelle)
inhalt.append(Spacer(1, 0.3*cm))

# 5. Fazit
inhalt.append(Paragraph("5. Fazit & Offene Fragen", abschnitt_style))
inhalt.append(Paragraph(
    "<b>Stärken:</b> Klare Differenzierung von Calm/Headspace, "
    "wachsender Markt, starker Viral Loop (~3 Referrals/Nutzer), "
    "solide App Store Performance (4.6★).",
    text_style
))
inhalt.append(Paragraph(
    "<b>Risiken:</b> LTV:CAC Ratio unter 3:1, noch keine DiGA-Zertifizierung, "
    "Retention in Mental Health Apps historisch niedrig (3-5% nach 30 Tagen).",
    text_style
))
inhalt.append(Paragraph(
    "<b>Größte Chance:</b> DiGA-Zertifizierung würde Zugang zu "
    "73 Millionen GKV-Versicherten in Deutschland öffnen.",
    text_style
))

# --- PDF BAUEN ---
doc.build(inhalt)
print("✅ PDF erstellt: ahead_analyse.pdf")
