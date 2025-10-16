# Ethics & Responsible Use

**Ethics > clout.** I publish work that strengthens defenders and improves model/agent safety without enabling harm. This repo focuses on **skills, concepts, and safe habits**—not on live target exploitation.

## 🎯 Intended Use

- Education & training in Unix fundamentals that map to **AI red-team** and **defensive engineering**.
- Building **reproducible evaluations** (prompt-injection, jailbreak taxonomy, RAG integrity) in controlled environments.
- Demonstrating **secure operations**: no hard-coded secrets, clean logs, and responsible disclosure.

## 🚫 Prohibited Use

- Unauthorized access, data exfiltration, denial-of-service, or privacy violations.
- Targeting real users/systems without **explicit written permission**.
- Publishing others’ secrets, private data, or non-public vulnerabilities.

## 🧭 Rules of Engagement (for my work and contributions)

1. **Consent & Scope:** Only test systems I own or have explicit written permission to test.
2. **Legality & ToS:** Follow the law and the platform’s policies. No “grey-area” heroics.
3. **Minimal Impact:** Prefer read-only checks; throttle; avoid resource harm.
4. **Reproducibility:** Seed runs, pin deps, log commands. Artifacts must be rerunnable by others.
5. **Dual-Use Minimization:** I share **techniques and metrics**—not live target lists nor turnkey harm.
6. **Privacy:** Use synthetic or public test data. Redact and de-identify any incidental capture.
7. **Attribution:** Credit upstream ideas/tools. Respect licenses and communities.

## 🔬 AI Red-Team Principles (how I operate)

- **Attack Budgets:** Fixed attempts/tokens to compare defenses fairly.
- **Metrics:** Attack Success Rate, tokens-to-success, time-to-detect, false-positive tradeoffs.
- **Defense-First Reporting:** Always evaluate at least one mitigation (e.g., tool whitelists, content guards, sandboxing).
- **Auditability:** Logs and configs included; runs should be **one-command reproducible**.
- **Safety Notes:** Every demo clearly labels scope, risks, and safe-repro steps.

## 📄 Content Boundaries in This Repo

- No real credentials, API keys, or personal data.
- No instructions to exploit live targets.
- Any “payloads” exist solely in **local, sandboxed** contexts.

## 🤝 Community Conduct

- Be technical and kind. No harassment, doxxing, or gatekeeping.
- Offer constructive PRs and issues. I welcome fixes that improve safety, clarity, and reproducibility.

---
