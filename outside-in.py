# ============================================
# OUTSIDE-IN ANALYSE: AHEAD SOLUTIONS
# ============================================
# Alle Zahlen mit Quelle gekennzeichnet

# --- MARKTGRÖSSE ---
# [FAKT] Quelle: Grand View Research, April 2025
TAM_GLOBAL_2025 = 8_500_000_000  # $8.5 Milliarden
TAM_WACHSTUM_JAEHRLICH = 0.15  # 15% CAGR

# [FAKT] Quelle: Grand View Research Europa, April 2025
SAM_EUROPA_2025 = 2_230_000_000  # $2.23 Milliarden

# [SCHÄTZUNG] Realistischer Marktanteil für Ahead
SOM_PROZENT = 0.01  # 1% des europäischen Markts
SOM = SAM_EUROPA_2025 * SOM_PROZENT  # ~$22 Millionen

# --- WETTBEWERB ---
# [FAKT] Quellen: App Store, Choosing Therapy, April 2026

wettbewerber = [
    {
        "name": "Calm",
        "fokus": "Meditation & Schlaf",
        "preis_jahr": 70,
        "app_bewertungen": 2_000_000,
        "sterne": 4.8,
        "direkte_konkurrenz": False,  # anderer Fokus als Ahead
    },
    {
        "name": "Headspace",
        "fokus": "Meditation & Achtsamkeit",
        "preis_jahr": 70,
        "app_bewertungen": 1_000_000,
        "sterne": 4.8,
        "direkte_konkurrenz": False,
    },
    {
        "name": "Wysa",
        "fokus": "CBT Chatbot",
        "preis_jahr": 75,
        "app_bewertungen": 21_700,
        "sterne": 4.9,
        "direkte_konkurrenz": True,
    },
    {
        "name": "Woebot",
        "fokus": "CBT Chatbot kostenlos",
        "preis_jahr": 0,
        "app_bewertungen": 0,
        "sterne": 4.0,
        "direkte_konkurrenz": True,
    },
    {
        "name": "Ahead",
        "fokus": "Emotionale Intelligenz & Verhaltensänderung",
        "preis_jahr": 99,
        "app_bewertungen": 1_515,
        "sterne": 4.6,
        "direkte_konkurrenz": False,  # eigenes Segment
    },
]

# --- AUSGABE ---
print("=" * 55)
print("OUTSIDE-IN ANALYSE: AHEAD SOLUTIONS")
print("=" * 55)

# Marktgröße
print("\n📊 MARKTGRÖSSE [FAKT - Grand View Research, 2025]")
print(f"  TAM global:     ${TAM_GLOBAL_2025 / 1_000_000_000:.1f} Milliarden")
print(f"  SAM Europa:     ${SAM_EUROPA_2025 / 1_000_000_000:.2f} Milliarden")
print(f"  SOM Ahead:      ${SOM / 1_000_000:.0f} Millionen [SCHÄTZUNG 1%]")
print(f"  Marktwachstum:  {TAM_WACHSTUM_JAEHRLICH * 100:.0f}% jährlich")

# Wettbewerb
print("\n📊 WETTBEWERBSLANDSCHAFT")
print(
    f"  {'Name':<12} {'Fokus':<35} {'Preis/Jahr':>10} {'Bewertungen':>12} {'Sterne':>7}"
)
print("  " + "-" * 80)

for w in wettbewerber:
    direkt = "🎯" if w["direkte_konkurrenz"] else "  "
    print(
        f"  {direkt} {w['name']:<10} {w['fokus']:<35} €{w['preis_jahr']:>8} {w['app_bewertungen']:>12,} {w['sterne']:>7}"
    )

print("\n  🎯 = direkte Konkurrenz")

# Ahead Positionierung
print("\n📊 AHEAD POSITIONIERUNG")
ahead = next(w for w in wettbewerber if w["name"] == "Ahead")
direkte_konkurrenten = [w for w in wettbewerber if w["direkte_konkurrenz"]]

print(f"  Ahead Preis vs. Markt:")
preise = [w["preis_jahr"] for w in wettbewerber if w["preis_jahr"] > 0]
durchschnitt = sum(preise) / len(preise)
print(f"  Durchschnitt Markt: €{durchschnitt:.0f}/Jahr")
print(f"  Ahead:              €{ahead['preis_jahr']}/Jahr")
if ahead["preis_jahr"] > durchschnitt:
    print(f"  → Ahead ist Premium-positioniert ⚠️")
else:
    print(f"  → Ahead ist wettbewerbsfähig ✅")

# DiGA Chance
print("\n📊 DIGA REGULATORIK [FAKT - Ärzteblatt, April 2026]")
print("  DiGA Nutzung 2024→2025: +63%")
print("  GKV Ausgaben 2024:      €106 Millionen")
print("  Ahead DiGA Status:      ❌ Nicht zertifiziert")
print("  → Große Wachstumschance aber komplexer Prozess")

print("\n" + "=" * 55)
print("⚠️  Schätzungen basieren auf öffentlichen Benchmarks")
print("=" * 55)
