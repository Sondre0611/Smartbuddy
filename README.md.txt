# 🤖 SmartBuddy

SmartBuddy er en AI-chatbot laget med Flask og en enkel frontend, som lar brukere chatte og gi tilbakemeldinger på svarene. Nettsiden kan vises på mobil eller desktop.

## 🚀 Funksjoner

- Chat med en AI-assistent
- Gi tilbakemelding på svar (👍/👎)
- Lær AI-en bedre svar med forslag
- Klart for å deles med andre via GitHub Pages og f.eks. Render eller ngrok

## 🧠 Teknologi

- 🐍 Backend: Python + Flask
- 🌐 Frontend: HTML + JavaScript
- 📦 API-endepunkter:
  - `POST /v1/chat/completions` – send en melding
  - `POST /v1/feedback` – gi feedback

## 🔧 Kom i gang lokalt

1. Installer avhengigheter:

```bash
pip install -r requirements.txt
