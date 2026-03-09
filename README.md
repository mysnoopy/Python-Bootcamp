# 🐍 Python Bootcamp

**An interactive, browser-based Python learning platform — no installs, no terminal, no setup.**

Download one HTML file. Double-click. Start learning.

---

## ✨ What Is This?

Python Bootcamp is a self-contained, offline-capable learning app packed into a single `.html` file. It runs entirely in your browser using [Pyodide](https://pyodide.org/) — a full Python runtime compiled to WebAssembly — so you can write and execute real Python code without installing anything.

Built for complete beginners who want to learn Python through hands-on projects, with line-by-line explanations for every single line of code.

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/mysnoopy/Python-Bootcamp.git
cd Python-Bootcamp

# Option 1 — just open it
open python_bootcamp_standalone.html

# Option 2 — serve locally (recommended for AI chat features)
python3 -m http.server 7777
# then visit http://localhost:7777/python_bootcamp_standalone.html
```

No npm. No pip. No virtual environments. Nothing to install.

---

## 📚 Curriculum — 23 Lessons Across 10 Phases

| Phase | Topic | Lessons |
|-------|-------|---------|
| 🐍 Phase 1 | **Python Basics** | Hello World & Variables, Conditions & Loops, Don't Panic: Reading Errors |
| 📦 Phase 2 | **Data Types** | Lists & Dictionaries, Functions, String Methods |
| 🏗️ Phase 3 | **OOP** | Library Book System |
| 🔌 Phase 4 | **APIs** | Live Weather Fetcher |
| ⚙️ Phase 5 | **Frameworks** | FastAPI Backend *(interactive simulator)* |
| 🤖 Phase 6 | **AI / LLMs** | AI API Movie Recommender |
| 🧠 Phase 7 | **AI Topics** | Prompt Engineering, RAG Knowledge Base, AI Agents & Tools |
| 🗄️ Phase 8 | **Data & Files** | File I/O, CSV & JSON, Mini Database, Data Analysis |
| 🧪 Phase 9 | **Testing & Debugging** | Reading Errors, Writing Tests, Debugging Tips |
| 🔄 Phase 10 | **Real Projects** | CLI Todo App, Number Guessing Game, Budget Tracker |

---

## 🎯 Features

- **Line-by-line explanations** — every code line has a plain-English description, toggleable with 💡 ON/OFF
- **Built-in code editor** — powered by [CodeMirror](https://codemirror.net/) with syntax highlighting
- **Run in browser** — real Python execution via [Pyodide](https://pyodide.org/) (WebAssembly)
- **Memory trick box** — each lesson opens with a key concept to anchor the learning
- **Progress tracking** — mark lessons done, track completion %, stored in localStorage
- **AI Chat Tutor** — ask questions about any lesson using your own API key (see below)
- **Cheat Sheet** — quick-reference syntax guide with one-click copy
- **Quiz mode** — test yourself across all concepts
- **Dark / Light theme** — toggle with ☀️ / 🌙
- **FastAPI simulator** — interactive REST API sandbox, no server needed
- **Fully offline** — works without internet after initial load *(Google Fonts and Pyodide CDN require one-time network fetch)*

---

## 🤖 AI Chat Tutor

The app includes a built-in AI tutor that can answer questions about any lesson. It supports three providers — you bring your own API key:

| Provider | Model | Status |
|----------|-------|--------|
| 🟢 Google Gemini | `gemini-2.5-flash` | ✅ Tested & working |
| 🟦 OpenAI | `gpt-4o-mini` | ⚠️ Untested — bugs possible |
| 🟠 Anthropic Claude | `claude-haiku-4-5-20251001` | ⚠️ Untested — bugs possible |

> **Note:** Only the **Gemini API key** has been tested end-to-end. The OpenAI and Anthropic integrations are implemented but **have not been tested with real API keys**. If you run into issues with ChatGPT or Claude keys, please [open an issue](https://github.com/mysnoopy/Python-Bootcamp/issues) with the error details — contributions welcome!

**Getting a free Gemini key (recommended):**
1. Visit [aistudio.google.com](https://aistudio.google.com)
2. Click **Get API key** → **Create API key**
3. Paste into **⚙️ Setup AI** in the top-right corner — takes 30 seconds

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Python Runtime | [Pyodide](https://pyodide.org/) (Python 3.11 via WebAssembly) |
| UI Framework | React 18 (Babel standalone — no build step) |
| Code Editor | CodeMirror 5 |
| Fonts | Plus Jakarta Sans + Space Mono (Google Fonts) |
| Storage | `localStorage` (progress + settings) |
| Deployment | Single `.html` file — zero dependencies |

---

## 📁 Project Structure

```
Python-Bootcamp/
├── python_bootcamp_standalone.html   # ← The entire app (one file)
└── README.md
```

The whole platform — curriculum data, UI, Python runtime loader, AI chat, quiz engine — lives in a single file.

---

## 🐛 Known Limitations

- **Pyodide cold start** — takes 3–8s on first load (downloading Python WASM runtime ~10MB)
- **No `sqlite3`** — not included in Pyodide; lessons use dicts/lists instead
- **No `pandas`** — not available by default; data lessons use `csv` + `statistics`
- **No `requests`** — use `pyodide.http.open_url` for HTTP (handled inside lessons)
- **AI lessons require an API key** — they won't execute without one configured
- **OpenAI / Claude API keys untested** — Gemini is the recommended provider for now

---

## 🛠️ Local Development

The app is plain HTML + React + Babel — no build tooling required.

1. Open `python_bootcamp_standalone.html` in VS Code
2. Find the `<script type="text/babel">` tag — all app logic lives here
3. Edit and save
4. Hard-reload in browser: `Cmd+Shift+R` (Mac) / `Ctrl+Shift+R` (Windows/Linux)

**Version tracking:** Each build includes a version stamp + MD5 checksum on the loading screen (e.g. `v2026-03-09c · #44483a6b`) so you always know exactly which version is running.

---

## 🗺️ Roadmap

- [ ] Add missing lessons: While Loops (1c), Modules & Imports (2c), Python Shortcuts (2d)
- [ ] Test and fix OpenAI + Anthropic AI chat integrations
- [ ] Mobile layout improvements
- [ ] Shareable lesson links
- [ ] More real-world projects in Phase 10

---

## 📄 License

MIT — free to use, fork, and build on.

---

*Built with ❤️ by [Clarence](https://github.com/mysnoopy) · Octoix AI*
