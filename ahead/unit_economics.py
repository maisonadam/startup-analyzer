# ============================================
# UNIT ECONOMICS: AHEAD SOLUTIONS
# ============================================
# Datenquellen klar gekennzeichnet:
# [FAKT] = verifizierte Daten
# [BENCHMARK] = Branchen-Durchschnitt
# [SCHÄTZUNG] = eigene Berechnung

# --- ECHTE DATEN ---
# [FAKT] Preise (App Store, April 2026)
PREIS_MONATLICH = 19.99
PREIS_QUARTAL = 39.99
PREIS_JAHR = 99.00
PREIS_LIFETIME = 149.00

# [FAKT] App Store (April 2026)
APP_BEWERTUNG = 4.6
APP_BEWERTUNGEN_ANZAHL = 1515

# [FAKT] Team (LinkedIn, April 2026)
TEAM_GROESSE = 16

# [FAKT] Funding (Crunchbase)
FUNDING_PRESEED = 1120000  # €1.12M

# [FAKT] Früher MRR (Wefunder, 2022)
MRR_FRÜH = 65000  # $65k organisch

# --- BRANCHEN-BENCHMARKS ---
# [BENCHMARK] Mental Health Apps (Quelle: Sensor Tower, 2023)
CONVERSION_FREE_TO_PAID = 0.05      # 5% typisch
CHURN_RATE_MONATLICH = 0.07         # 7% typisch
RETENTION_30_TAGE = 0.12            # 12% typisch
CAC_BENCHMARK = 40                  # $40 typisch

# --- BERECHNUNGEN ---
print("=" * 50)
print("UNIT ECONOMICS: AHEAD SOLUTIONS")
print("=" * 50)

# 1. Effektiver Monatspreis
preis_quartal_pro_monat = PREIS_QUARTAL / 3
preis_jahr_pro_monat = PREIS_JAHR / 12

print("\n📊 PREISSTRUKTUR [FAKT]")
print(f"  Monatlich:     €{PREIS_MONATLICH}")
print(f"  Quartal/Monat: €{preis_quartal_pro_monat:.2f}")
print(f"  Jährlich/Monat:€{preis_jahr_pro_monat:.2f}")

# 2. LTV Berechnung
# LTV = Durchschnittspreis / Churn Rate
ltv_monatlich = PREIS_MONATLICH / CHURN_RATE_MONATLICH
ltv_jährlich = preis_jahr_pro_monat / CHURN_RATE_MONATLICH

print("\n📊 LIFETIME VALUE [SCHÄTZUNG]")
print(f"  LTV (Monat-Abo):  €{ltv_monatlich:.0f}")
print(f"  LTV (Jahr-Abo):   €{ltv_jährlich:.0f}")
print(f"  Basis: Churn {CHURN_RATE_MONATLICH*100}% [BENCHMARK Mental Health Apps]")

# 3. LTV:CAC Ratio
ltv_cac_ratio = ltv_jährlich / CAC_BENCHMARK

print("\n📊 LTV:CAC RATIO [SCHÄTZUNG]")
print(f"  LTV:CAC = {ltv_cac_ratio:.1f}:1")
if ltv_cac_ratio >= 3:
    print(f"  ✅ Gesund (Ziel: >3:1)")
else:
    print(f"  ⚠️  Kritisch (Ziel: >3:1)")

# 4. Nutzer-Schätzung aus Reviews
# [SCHÄTZUNG] Typisch: 1-5% der Nutzer schreiben Reviews
nutzer_konservativ = APP_BEWERTUNGEN_ANZAHL / 0.05
nutzer_optimistisch = APP_BEWERTUNGEN_ANZAHL / 0.01

print("\n📊 NUTZERSCHÄTZUNG [SCHÄTZUNG]")
print(f"  Downloads geschätzt: {nutzer_konservativ:,.0f} - {nutzer_optimistisch:,.0f}")
print(f"  Basis: 1-5% Review-Rate [BENCHMARK App Store]")

# 5. MRR Schätzung heute
paid_nutzer_konservativ = nutzer_konservativ * CONVERSION_FREE_TO_PAID
mrr_heute_konservativ = paid_nutzer_konservativ * preis_jahr_pro_monat

print("\n📊 MRR SCHÄTZUNG HEUTE [SCHÄTZUNG]")
print(f"  Paid Nutzer (konservativ): {paid_nutzer_konservativ:,.0f}")
print(f"  MRR Schätzung: €{mrr_heute_konservativ:,.0f}")
print(f"  Früher MRR (2022, Fakt): ${MRR_FRÜH:,}")

print("\n" + "=" * 50)
print("⚠️  HINWEIS: Schätzungen basieren auf öffentlichen")
print("Benchmarks. Echte Zahlen nur intern verfügbar.")
print("=" * 50)
