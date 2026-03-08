# 🐍 Python Bootcamp — Interactive Browser Learner

A fully self-contained Python learning platform that runs entirely in your browser. No installs, no terminal, no server. Just download the HTML file and open it.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Pyodide](https://img.shields.io/badge/Pyodide-0.24.1-green) ![React](https://img.shields.io/badge/React-18-61DAFB) ![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## ✨ Features

- **Run Python in the browser** — powered by [Pyodide](https://pyodide.org/) (Python compiled to WebAssembly)
- **19 hands-on lessons** across 10 phases — from Hello World to AI Agents
- **Line-by-line explanations** — toggle to reveal what every line does
- **Built-in code editor** — CodeMirror with Python syntax highlighting, Dracula/Eclipse themes
- **AI Tutor chatbot** — powered by Gemini (free), OpenAI, or Anthropic
- **Progress tracking** — lessons marked complete, persisted to localStorage
- **Cheat sheet** — quick Python reference always one click away
- **Quiz** — 8-question quiz with best-score tracking
- **Dark / light mode** — toggle anytime
- **FastAPI Simulator** — interactive mock REST API (Phase 5) with live mode support

---

## 🚀 Quick Start

1. Download `python_bootcamp_standalone.html`
2. Open it in Chrome or Firefox
3. Click any lesson and hit **▶ Run**

> Internet connection required for CDN assets (React, CodeMirror, Pyodide) and the AI Tutor.

---

## 📚 Curriculum

| Phase | Topic | Lessons |
|-------|-------|---------|
| 🐍 Phase 1 | Python Basics | 1a: Hello World & Variables · 1b: Conditions & Loops |
| 📦 Phase 2 | Data Types | 2a: Lists & Dictionaries · 2b: Functions |
| 🏗️ Phase 3 | OOP | 3a: Classes & Objects |
| 🔌 Phase 4 | APIs | 4a: REST APIs & HTTP |
| ⚙️ Phase 5 | Frameworks | 5a: FastAPI Backend *(interactive simulator)* |
| 🤖 Phase 6 | AI / LLMs | 6a: AI API — Movie Recommender |
| 🧠 Phase 7 | AI Topics | 7a: Prompt Engineering · 7b: RAG · 7c: AI Agents & Tools |
| 🗄️ Phase 8 | Data & Files | 8a: CSV & JSON · 8b: Mini Database · 8c: Data Analysis |
| 🧪 Phase 9 | Testing & Debugging | 9a: Reading Errors · 9b: Writing Tests · 9c: Debugging Tips |
| 🔄 Phase 10 | Real Projects | 10a: CLI Todo App · 10b: Number Guessing Game · 10c: Budget Tracker |

**Total:** ~9 hours of guided, project-based learning

---

## 🤖 AI Tutor Setup

Click the 💬 button (bottom right) to open the AI Tutor. Paste in one API key — stored locally and never sent anywhere except the provider's API.

| Provider | Model | Cost | Get Key |
|----------|-------|------|---------|
| 🟢 Google Gemini | gemini-2.5-flash | **Free** | [aistudio.google.com](https://aistudio.google.com) |
| 🟦 OpenAI | gpt-4o-mini | ~$0.60/1M tokens | [platform.openai.com](https://platform.openai.com) |
| 🟠 Anthropic | claude-haiku-4-5 | ~$0.80/1M tokens | [console.anthropic.com](https://console.anthropic.com) |

---

## ⚙️ FastAPI Simulator (Phase 5)

Phase 5 includes a full interactive REST API simulator — no server needed.

- **4 endpoints:** `GET /books`, `POST /books`, `PUT /books/{id}`, `DELETE /books/{id}`
- **Live DB panel** — see your in-memory database update in real time
- **Live Mode** — toggle to send real requests to a local FastAPI server at `localhost:8000`

To run Phase 5 with a real server:
```bash
pip install fastapi uvicorn
python main.py
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Python runtime | [Pyodide](https://pyodide.org/) 0.24.1 (WASM) |
| UI framework | React 18 |
| Code editor | CodeMirror 5.65.16 |
| JS compiler | Babel Standalone 7.23.10 |
| AI Tutor | Gemini / OpenAI / Anthropic APIs |

---

## 📁 Files

```
python_bootcamp_standalone.html   # The entire app — single file, ~2300 lines
main.py                           # FastAPI backend for Phase 5 live mode
README.md
```

---

## 🔧 Development

The entire app is a single HTML file with an embedded React + Babel application. To modify:

1. Open `python_bootcamp_standalone.html` in VS Code
2. Edit the `<script type="text/babel">` section
3. Refresh the browser — Babel recompiles on every load

**Curriculum data** lives in the `curriculum` array near the top of the script. Each lesson has:
- `id`, `title`, `duration`, `project` — metadata
- `memTrick` — mnemonic shown above the editor
- `concepts` — badge chips shown in the phase overview
- `lines` — array of `{code, exp}` objects (the step-by-step code)

---

## 🤝 Contributing

PRs welcome! Good first contributions:
- Add new lessons to existing phases
- Fix typos in `exp:` explanation fields
- Add quiz questions
- Improve mobile layout

---

## 📄 License

MIT — use freely, modify freely, share freely.
