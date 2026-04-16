import anthropic
import os
import urllib.request

# 1. Website-Text holen
url = "https://www.ahead-app.com"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
response = urllib.request.urlopen(req)
html = response.read().decode("utf-8")

# Nur ersten 3000 Zeichen nehmen
website_text = html[:3000]

# 2. Claude mit Kontext fragen
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": f"""
Hier ist der Website-Text von Ahead Solutions:

{website_text}

Analysiere basierend auf diesem Text:
1. Welches Problem löst Ahead?
2. Für wen ist es gedacht?
3. Was ist die Kernlösung?
"""}
    ]
)

print(message.content[0].text)
