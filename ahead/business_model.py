import anthropic
import os
import urllib.request

# --- SCHRITT 1: Website-Text holen ---
url = "https://www.ahead-app.com"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
response = urllib.request.urlopen(req)
html = response.read().decode("utf-8")
website_text = html[:3000]

# --- SCHRITT 2: Claude fragen ---
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2048,
   messages=[
       {"role": "user", "content": f"""
   Du bist ein erfahrener Startup-Analyst.

   Hier ist der Website-Text von Ahead Solutions:

   {website_text}

   WICHTIGE REGELN:
   - Erfinde KEINE Zahlen
   - Trenne klar zwischen FAKT und SCHÄTZUNG
   - Wenn du keine Daten hast, schreib: [KEINE DATEN - Quelle nötig]
   - Wenn du Branchen-Benchmarks nutzt, schreib: [BENCHMARK: Quelle]
   - Nur qualitative Aussagen wenn keine Zahlen verfügbar

   Analysiere das Business Model:

   ## 1. REVENUE MODEL
   Nur basierend auf dem Website-Text:
   - Wie verdienen sie Geld?
   - Wer zahlt?
   - Welches Preismodell ist erkennbar?

   ## 2. KUNDENAKQUISE
   Nur was aus dem Text erkennbar ist:
   - Welche Kanäle sind erwähnt oder erkennbar?

   ## 3. KOSTENSTRUKTUR
   Qualitativ – keine Zahlen erfinden:
   - Was sind die wahrscheinlichen Hauptkostenpositionen?

   ## 4. OFFENE FRAGEN
   - Was wissen wir NICHT und müssten recherchieren?
   - Welche Datenquellen würden helfen?
   """}
   ]
)

# --- SCHRITT 3: Ausgabe ---
print("=" * 50)
print("BUSINESS MODEL ANALYSE: AHEAD SOLUTIONS")
print("=" * 50)
print(message.content[0].text)
