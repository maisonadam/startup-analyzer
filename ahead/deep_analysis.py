from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib import colors

# --- DOKUMENT ---
doc = SimpleDocTemplate(
    "ahead_deep_analysis.pdf",
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
ORANGE = colors.HexColor('#e67e22')

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

# ============================================
# DATEN – klar gekennzeichnet
# ============================================

# --- FAKTEN [FAKT] ---
GRUENDER = "Kai Koch & John Roggan"
GRUENDUNGSJAHR = 2020
STANDORT = "Berlin, Deutschland"
FUNDING_TOTAL = "$2.29M"
LETZTE_RUNDE = "Oktober 2021"  # [FAKT] Tracxn, PitchBook
INVESTOREN = "Speedinvest, Google for Startups, Play Ventures, Goodwater Capital"
TEAM = 16  # [FAKT] LinkedIn April 2026
APP_STERNE = 4.6
APP_BEWERTUNGEN = 1515
PREIS_MONAT = 19.99
PREIS_JAHR = 99.00
MRR_FRUEH = 65000  # [FAKT] Wefunder 2022

# --- BENCHMARKS [BENCHMARK] ---
CHURN_BENCHMARK = 0.07
CAC_BENCHMARK = 40
CONVERSION_BENCHMARK = 0.05

# --- BERECHNUNGEN [SCHÄTZUNG] ---
ltv = (PREIS_JAHR / 12) / CHURN_BENCHMARK
ltv_cac = ltv / CAC_BENCHMARK
downloads_min = APP_BEWERTUNGEN / 0.05
downloads_max = APP_BEWERTUNGEN / 0.01

# --- DEINE EINSCHÄTZUNGEN ---
STAERKEN = [
    "Klare Differenzierung – emotionale Intelligenz statt Meditation",
    "Starker Viral Loop: ~3 Referrals pro Nutzer (Wefunder)",
    "Solide App Store Performance: 4.6★ bei 1.515 Bewertungen",
    "Wachsender Markt: Europa +15% jährlich",
    "Duolingo-Positionierung ist einprägsam und skalierbar",
]

RISIKEN = [
    "Kein neues Funding seit Oktober 2021 – fast 4 Jahre",
    "LTV:CAC Ratio bei ~2.9:1 – unter dem gesunden Ziel von 3:1",
    "Dark Pattern Vorwurf: Free Trial konvertiert zu Jahresabo",
    "Retention in Mental Health Apps historisch bei 3-5% nach 30 Tagen",
    "Premium-Preis (€99) ohne klare Differenzierungskommunikation",
]

EMPFEHLUNGEN = [
    "Retention als #1 Priorität: Personalisierung der Inhalte vertiefen",
    "Free Trial transparenter gestalten – Vertrauensaufbau statt Dark Pattern",
    "DiGA-Zertifizierung anstreben: Zugang zu 73M GKV-Versicherten",
    "Marketing: Transformation kommunizieren statt Features",
    "B2B-Kanal über Arbeitgeber beschleunigen – niedrigerer CAC",
]

# ============================================
# PDF INHALT
# ============================================
inhalt = []

# --- TITEL ---
inhalt.append(Paragraph("Startup Deep Analysis", titel))
inhalt.append(Paragraph("Ahead Solutions GmbH · Berlin · April 2026", untertitel))
inhalt.append(HRFlowable(width="100%", thickness=2, color=DUNKELBLAU))
inhalt.append(Spacer(1, 0.4*cm))

# --- EXECUTIVE SUMMARY ---
inhalt.append(Paragraph("Executive Summary", h2))
inhalt.append(Paragraph(
    "Ahead ist ein Berliner Mental Health Startup das emotionale Intelligenz "
    "trainiert – positioniert als 'Duolingo für EQ'. Das Produkt adressiert "
    "einen echten, wachsenden Markt ($2.23B Europa, +15% jährlich). "
    "Die Differenzierung von Calm und Headspace ist klar. "
    "Kritisch: Kein neues Funding seit Oktober 2021, LTV:CAC unter 3:1, "
    "und ein Dark Pattern Vorwurf der das Nutzervertrauen gefährdet. "
    "Größte ungenutzte Chance: DiGA-Zertifizierung.",
    text
))
inhalt.append(Spacer(1, 0.3*cm))

# --- PROBLEM SOLUTION FIT ---
inhalt.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
inhalt.append(Paragraph("1. Problem-Solution Fit", h2))
inhalt.append(Paragraph("<b>Das Problem:</b>", h3))
inhalt.append(Paragraph(
    "Emotionale Selbststeuerung ist erlernbar – aber es gibt keinen "
    "zugänglichen Weg sie zu trainieren. Therapie ist teuer und stigmatisiert. "
    "Bücher vermitteln Wissen aber keine Verhaltensänderung.",
    text
))
inhalt.append(Paragraph("<b>Die Lösung:</b>", h3))
inhalt.append(Paragraph(
    "Micro-Sessions von 5 Minuten die konkrete Alltagssituationen trainieren. "
    "Kein passives Lesen – aktives Üben. Wissenschaftlich fundiert durch "
    "Behavior-Change Experten.",
    text
))
inhalt.append(Paragraph("<b>Eigene Einschätzung:</b>", h3))
inhalt.append(Paragraph(
    "Der Problem-Solution Fit ist überzeugend. Ahead ist kein Vitamin sondern "
    "ein Painkiller für funktionale Erwachsene in akuten Lebensphasen – "
    "Burnout, Beziehungsprobleme, Jobstress. Die Werthypothese ist klar: "
    "Verhaltensänderung durch Wiederholung, nicht durch Wissensvermittlung.",
    text
))
inhalt.append(Spacer(1, 0.3*cm))

# --- BUSINESS MODEL ---
inhalt.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
inhalt.append(Paragraph("2. Business Model & Unit Economics", h2))

# Preistabelle
inhalt.append(Paragraph("<b>Preisstruktur [FAKT – App Store April 2026]</b>", h3))
preis_data = [
    ["Modell", "Preis", "Pro Monat", "Strategie"],
    ["Monatlich", "€19.99", "€19.99", "Einstieg"],
    ["Quartal", "€39.99", "€13.33", "Mittelfristig"],
    ["Jährlich", "€99.00", "€8.25", "Empfohlen ← Kernprodukt"],
    ["Lifetime", "€149.00", "–", "LTV-Maximierung"],
]
t = Table(preis_data, colWidths=[3.5*cm, 3*cm, 3*cm, 6*cm])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DUNKELBLAU),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, HELLGRAU]),
    ('PADDING', (0,0), (-1,-1), 6),
    ('BACKGROUND', (0,3), (-1,3), colors.HexColor('#e8f5e9')),
]))
inhalt.append(t)
inhalt.append(Spacer(1, 0.3*cm))

# Unit Economics
inhalt.append(Paragraph("<b>Unit Economics [Berechnung April 2026]</b>", h3))
unit_data = [
    ["Metrik", "Wert", "Quelle", "Bewertung"],
    ["LTV (Jahresabo)", f"€{ltv:.0f}", "SCHÄTZUNG – 7% Churn", "⚠️ Niedrig"],
    ["CAC", f"€{CAC_BENCHMARK}", "BENCHMARK", "OK"],
    ["LTV:CAC Ratio", f"{ltv_cac:.1f}:1", "SCHÄTZUNG", "⚠️ Unter 3:1"],
    ["App Bewertungen", f"{APP_BEWERTUNGEN:,}", "FAKT – App Store", "✅ Solide"],
    ["Downloads (geschätzt)", f"{downloads_min:,.0f}–{downloads_max:,.0f}", "SCHÄTZUNG", "Große Spanne"],
    ["MRR (2022)", f"${MRR_FRUEH:,}", "FAKT – Wefunder", "✅ Organisch"],
]
t2 = Table(unit_data, colWidths=[4*cm, 3*cm, 4.5*cm, 4*cm])
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

# --- MARKT ---
inhalt.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
inhalt.append(Paragraph("3. Markt & Wettbewerb", h2))
markt_data = [
    ["Metrik", "Wert", "Quelle"],
    ["TAM Global", "$8.5 Milliarden", "FAKT – Grand View Research 2025"],
    ["SAM Europa", "$2.23 Milliarden", "FAKT – Grand View Research 2025"],
    ["SOM Ahead", "~$22 Millionen", "SCHÄTZUNG – 1% Marktanteil"],
    ["Marktwachstum", "15% jährlich", "FAKT – Grand View Research 2025"],
    ["DiGA Wachstum DE", "+63% (2024→2025)", "FAKT – Ärzteblatt 2026"],
]
t3 = Table(markt_data, colWidths=[5*cm, 5*cm, 5.5*cm])
t3.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DUNKELBLAU),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, HELLGRAU]),
    ('PADDING', (0,0), (-1,-1), 6),
]))
inhalt.append(t3)
inhalt.append(Spacer(1, 0.3*cm))

# --- KRITISCHE ANALYSE ---
inhalt.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
inhalt.append(Paragraph("4. Kritische Analyse", h2))

inhalt.append(Paragraph("Stärken", h3))
for s in STAERKEN:
    inhalt.append(Paragraph(f"✅ {s}", empfehlung))

inhalt.append(Spacer(1, 0.2*cm))
inhalt.append(Paragraph("Risiken & Schwächen", h3))
for r in RISIKEN:
    inhalt.append(Paragraph(f"⚠️ {r}", kritik))

inhalt.append(Spacer(1, 0.3*cm))

# --- EMPFEHLUNGEN ---
inhalt.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
inhalt.append(Paragraph("5. Strategische Empfehlungen", h2))
inhalt.append(Paragraph(
    "Als Founders Associate würde ich folgende Prioritäten setzen:",
    text
))
for i, e in enumerate(EMPFEHLUNGEN, 1):
    inhalt.append(Paragraph(f"<b>{i}.</b> {e}", text))

inhalt.append(Spacer(1, 0.3*cm))

# --- FAZIT ---
inhalt.append(HRFlowable(width="100%", thickness=2, color=DUNKELBLAU))
inhalt.append(Paragraph("6. Fazit", h2))
inhalt.append(Paragraph(
    "<b>Bewertung: WATCH ⚡</b>",
    h3
))
inhalt.append(Paragraph(
    "Ahead hat einen überzeugenden Problem-Solution Fit und eine klare "
    "Differenzierung im Mental Health Markt. Der Markt wächst stark. "
    "Aber: Fast 4 Jahre ohne neues Funding, LTV:CAC unter 3:1 und ein "
    "Dark Pattern Vorwurf sind kritische Warnsignale. "
    "Das Unternehmen steht an einem Wendepunkt – entweder gelingt die "
    "Skalierung über B2B und DiGA, oder das Modell stagniert. "
    "Ich würde Ahead genau beobachten und bei einer neuen Funding-Runde "
    "oder DiGA-Zertifizierung neu bewerten.",
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
print("✅ Deep Analysis PDF erstellt: ahead_deep_analysis.pdf")
