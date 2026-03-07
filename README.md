# 🐍 Python Bootcamp — Interactive Learning Platform

A fully self-contained HTML file for learning Python from scratch — no installs, no terminal, no server. Just download and open.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🐍 7 Phases of curriculum | Python Basics → Data Types → OOP → APIs → Frameworks → AI/LLMs → AI Topics |
| 📝 Built-in code editor | **CodeMirror** with Python syntax highlighting, line numbers, bracket matching |
| ▶️ Run Python in browser | Powered by **Pyodide** (Python-in-WebAssembly) — zero backend needed |
| 💡 Line-by-line explanations | Toggle on/off for each lesson |
| 🤖 AI Chat Tutor | Context-aware Python tutor using Gemini, OpenAI, or Anthropic |
| 💾 Progress persistence | Completed lessons, last position, and best quiz score saved via `localStorage` |
| 🌙 Dark / ☀️ Light theme | Toggle anytime — preference remembered across sessions |
| 📱 Mobile-friendly | Responsive layout stacks on small screens |
| 📋 Cheat Sheet | Click-to-copy syntax reference for all key concepts |
| 🧠 Quiz | 8-question syntax quiz with best-score tracking |
| ↔️ Resizable panels | Drag dividers to resize explanation pane, editor, and output |

---

## 🚀 Getting Started

1. Download `python_bootcamp_standalone.html`
2. Double-click to open in your browser (Chrome or Firefox recommended)
3. Wait ~5 seconds for Python (Pyodide) to load — you'll see **🟢 Python Ready** in the header
4. Pick a phase from the sidebar and start coding

**On mobile?** The layout automatically stacks — sidebar hides, panes stack vertically. Works in mobile Chrome/Safari.

No npm. No pip. No server. Just a browser.

---

## 🤖 AI Chat Tutor Setup

The floating **💬 button** opens a Python tutor powered by your own API key. Click **⚙️ Setup AI** in the header.

| Provider | Cost | Model | Where to get key |
|---|---|---|---|
| 🟢 **Google Gemini** | **FREE** ⭐ | gemini-2.0-flash-exp | [aistudio.google.com](https://aistudio.google.com) → Get API Key |
| 🟦 OpenAI | ~$0.60/1M tokens | gpt-4o-mini | [platform.openai.com](https://platform.openai.com) → API Keys |
| 🟠 Anthropic | ~$0.80/1M tokens | claude-haiku | [console.anthropic.com](https://console.anthropic.com) → API Keys |

> **Recommended:** Start with Gemini — it's free and takes 30 seconds to set up (no credit card).

Keys are stored in your browser's `localStorage` only. They are never transmitted anywhere except directly to the respective API provider.

---

## 📚 Curriculum

| Phase | Topics | Project |
|---|---|---|
| 🐍 Phase 1 — Python Basics | Variables, conditions, loops, functions | Student Bio Card, Grade Screener |
| 📦 Phase 2 — Data Types | Lists, dicts, sets, comprehensions | Movie Library Manager, Shopping Cart |
| 🏗️ Phase 3 — OOP | Classes, inheritance, methods | Library Book System |
| 🔌 Phase 4 — APIs | requests, JSON, async | Live Weather Fetcher |
| ⚙️ Phase 5 — Frameworks | FastAPI, routing, Pydantic | Book Store REST API |
| 🤖 Phase 6 — AI/LLMs | Anthropic SDK, prompting | AI Movie Recommender |
| 🧠 Phase 7 — AI Topics | Prompt Engineering, RAG, AI Agents | Knowledge Base, Tool-Use Agent |

---

## 🤖 AI Lessons (Phases 6 & 7)

Phases 6 and 7 teach real AI/LLM programming with live API calls. The code is **automatically adapted** to whichever API key you've saved in ⚙️ Setup AI — no manual editing needed.

| Your key | SDK used | Model |
|---|---|---|
| Anthropic | `anthropic` (native) | `claude-haiku-4-5` |
| OpenAI | `openai` | `gpt-4o-mini` |
| Gemini | `urllib` (no pip needed) | `gemini-2.0-flash` |

- A ✅ green banner confirms which provider your code is configured for
- If no key is saved, a 🔑 banner appears with a direct **⚙️ Setup AI →** button
- Saving a key while a lesson is open instantly injects it into the editor

---

## 💾 Progress Saving

Your progress is automatically saved to `localStorage` every time you:
- Mark a lesson complete
- Switch to a new lesson or phase
- Complete the quiz (best score saved)

When you reopen the file, you'll be taken back to where you left off.

To reset everything, click the 🗑 button in the header (appears once you've completed at least one lesson).

---

## 🔐 API Key Security

> **⚠️ For local / personal use only. Do not host this file on a public server.**

Since this is a local HTML file, API keys stored in `localStorage` are accessible only to your browser on your machine. However, be aware:

| Risk | Level | Notes |
|---|---|---|
| Browser extensions | 🟡 Medium | Malicious extensions can read localStorage |
| Shared computers | 🟡 Medium | Anyone on your machine can read saved keys |
| XSS / code injection | 🟢 Low | Not a concern for a local file |
| Network interception | 🟢 Low | Requests go directly from your browser to the API |
| Public hosting | 🔴 High | **Do not host publicly** — keys would be exposed |

### Best practices

- Set spending limits on your API accounts (all providers support this)
- Use the **Gemini** free tier to avoid any financial risk
- Revoke and rotate keys periodically
- Click **Clear all keys** in the Settings modal when done on a shared machine

### Disclaimer

By using this file, you accept full responsibility for any API keys you store in it and any costs incurred through usage. The author provides no warranty and accepts no liability.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI Framework | React 18 (via CDN) + Babel Standalone |
| Code Editor | **CodeMirror 5** — Python mode, Dracula/Eclipse themes |
| Python Runtime | **Pyodide 0.24.1** (Python in WebAssembly) |
| AI Chat | Gemini / OpenAI / Anthropic REST APIs |
| Storage | Browser `localStorage` |
| Dependencies | Zero npm packages — pure CDN |

---

## 📄 License

MIT — free to use, modify, and share.
