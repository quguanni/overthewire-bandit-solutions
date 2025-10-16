# 🧾 CHANGELOG

All notable changes to this project will be documented in this file.  
This project follows semantic versioning (`vMAJOR.MINOR.PATCH`).

---

## [v0.1.0] — 2025-10-16
**Initial public release — “Foundations of Red-Team Craft”**

> _From OverTheWire → AI red-teaming. Clean, reproducible, and ethical._

### 🚀 Highlights
- Added complete **solutions 0 → 34** for OverTheWire Bandit with:
  - Minimal spoilers  
  - Emphasis on **commands, concepts, and safety**  
  - Reusable helper functions (`login(){ ssh bandit$1@$HOST -p $PORT; }`)
- **Quick-reference** section for quoting, pipes, redirection, streams, and search tools.
- Added **safety boilerplate**:
  - `SECURITY.md` — disclosure & scope rules  
  - `ETHICS.md` — responsible-use guidelines  
  - `.gitignore` + shell hygiene tips (no real secrets, no creds)
- New section: **🧠 Bandit → AI Red-Team Mapping** — links each level cluster to concrete red-team skills (file ops → agent I/O, git forensics → data-leak analysis, etc.)
- Markdown refactor with collapsible `<details>` for each level; improved readability and copy/paste usability.

### 🧩 Conceptual Additions
| Category | Focus | Application |
|-----------|-------|--------------|
| File I/O & Streams | `cat`, `find`, redirection | Modeling LLM tool pipelines |
| Encodings | base64, ROT13, compression | Detecting obfuscated instructions |
| Network & TLS | `nc`, `openssl`, `nmap` | Agent tool-interface probing |
| Privilege / Cron | SUID & automation | Sandbox evasion and poisoning analogies |
| Git Forensics | History, tags, hooks | Supply-chain & provenance evaluation |

### 📚 Documentation
- Added project overview in README (`How to use this guide` + `Quick reference`)
- Added MIT License badge and author signature block.
- Included minimal release-tag instructions in `README.md` for future contributors.

### ⚖️ Ethics & Safety
- Explicit statement: **no real credentials, no unauthorized testing**.  
- Encouraged reproducible local use (`localhost`, Docker, or VM).  
- Added coordinated-disclosure contact.

### 🛠️ Internal
- Repo structured for GitHub Pages preview and future Jupyter integration.
- Ready for `v0.2.0` milestone: **“Bandit → Agents”** (linking Unix exercises to AI red-team harness scripts).

---

## Upcoming (Roadmap)
- `v0.2.0`: Add small Python scripts that simulate agent toolchains (socket servers, log sanitizers).
- `v0.3.0`: Integrate reproducible attack harnesses for LLM tool-use (prompt-injection kill-chain).
- `v1.0.0`: Publish full **AI Red-Team Foundations Curriculum** (Unix + Git + Model evals).

---

_Authored & maintained by **Jenny Qu (@quguanni)**_  
