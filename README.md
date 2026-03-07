# 🐍 Python Bootcamp — Interactive Single-File Learning App

A self-contained Python learning platform that runs entirely in your browser. No installs, no terminal, no setup. Just download one HTML file and open it.

---

## ✨ Features

- **7 phases** — Python Basics → Data Types → OOP → APIs → Frameworks → AI/LLMs → AI Topics
- **Line-by-line code explanations** — every line explained in plain English
- **Built-in Python editor** — write and run real Python code in the browser (powered by Pyodide)
- **AI chat tutor** — ask questions about any lesson using your own API key
- **Syntax cheat sheet** — click any line to copy
- **Quiz** — 8 questions to test retention

---

## 🚀 Getting Started

1. Download `python_bootcamp_standalone.html`
2. Double-click to open in your browser
3. Start learning — no installation needed

> **Python runs in the browser via [Pyodide](https://pyodide.org). Requires an internet connection on first load to download the Python runtime (~10MB). Subsequent loads are faster.**

---

## 🤖 AI Chat Tutor (Optional)

The floating 💬 button opens a context-aware Python tutor that knows which lesson you're on. It requires an API key from one of the supported providers.

### Supported Providers

| Provider | Cost | Model | Get Key |
|---|---|---|---|
| 🟢 **Google Gemini** | Free | gemini-2.5-flash | [aistudio.google.com](https://aistudio.google.com) |
| 🟦 **OpenAI** | Paid (~$0.60/1M tokens) | gpt-4o-mini | [platform.openai.com](https://platform.openai.com) |
| 🟠 **Anthropic** | Paid (~$0.80/1M tokens) | claude-haiku | [console.anthropic.com](https://console.anthropic.com) |

**Gemini is recommended** — free with any Google account, no credit card required. Sign in at [aistudio.google.com](https://aistudio.google.com), click "Get API Key", done.

### How to add your key

Click **⚙️ Setup AI** in the top-right corner → paste your key → Save. The key is remembered in your browser.

---

## ⚠️ API Key Security — Please Read

> **This app stores your API key in your browser's `localStorage`. Understand the risks before use.**

### What localStorage means

Your API key is saved as plain text inside your browser's local storage on your computer. It is **never transmitted to any server** by this app — all AI calls go directly from your browser to the AI provider's API.

### Known risks

| Risk | Level | Details |
|---|---|---|
| **Browser extensions** | ⚠️ Medium | Malicious extensions can read `localStorage` from any page. Only use trusted extensions. |
| **Shared computers** | ⚠️ Medium | Anyone with access to the same browser profile can view your key via DevTools → Application → Local Storage. |
| **Physical access** | ⚠️ Medium | If someone else has access to your computer and browser, they can extract the key. |
| **XSS injection** | ✅ Low | Not applicable — this is a local HTML file with no server, no user-generated HTML rendering, and no third-party ad scripts. |
| **Network interception** | ✅ Low | All API calls use HTTPS. Your key is never in a URL parameter. |

### Best practices

- **Use Gemini's free key** — if compromised, you can revoke and regenerate it instantly at no cost
- **Set spending limits** on paid API keys (OpenAI and Anthropic both support this in their dashboards)
- **Never use this on a shared or public computer**
- **Revoke your key immediately** if you suspect it was exposed — takes 10 seconds in any provider's dashboard
- To remove your saved key: open ⚙️ Settings → "Clear all keys"

---

## 🔒 Local Use Only — Not for Public Deployment

> **This app is designed for personal, local use only.**

It is **not safe** to host this file on a public web server, deploy it to a hosting platform (Netlify, Vercel, GitHub Pages, etc.), or share it as a hosted URL. Doing so would expose your app to the open internet where:

- Anyone can open the browser DevTools and potentially inspect stored keys
- You lose control over who accesses the app
- Hosting environments may introduce risks not present in a local file context

**If you share this project, share the HTML file itself — not a hosted version.**

> By using this app and entering your API key, you accept full responsibility for any risks associated with storing credentials in browser localStorage on your device. The author(s) of this project are not liable for any unauthorized access, API key exposure, or resulting charges.

---

## 📚 Curriculum

| Phase | Topic | Projects |
|---|---|---|
| 1 🐍 | Python Basics | Student Bio Card, Grade Screener |
| 2 📦 | Data Types | Movie Library Manager, Shopping Cart |
| 3 🏗️ | OOP | Library Book System |
| 4 🔌 | APIs | Live Weather Fetcher |
| 5 ⚙️ | Frameworks | Book Store REST API (FastAPI) |
| 6 🤖 | AI / LLMs | AI Movie Recommender (Claude API) |
| 7 🧠 | AI Topics | Prompt Engineering, RAG, AI Agents |

---

## 🛠️ Tech Stack

- **React 18** — UI (loaded via CDN, no build step)
- **Babel Standalone** — JSX in the browser
- **Pyodide 0.24** — Python runtime in WebAssembly
- **localStorage** — API key persistence (see security note above)
- Zero dependencies to install

---

## 📄 License

MIT — free to use, modify, and share. Attribution appreciated but not required.
# Python-Bootcamp
