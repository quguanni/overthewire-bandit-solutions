# Security Policy

This repo exists to **build muscle memory for safe, ethical hacking** and to support **reproducible AI red-team research**. No real secrets are ever used; all examples are synthetic and scoped for local practice.

## 🚧 Scope

- **In-scope:** This repository, its code, docs, and demo artifacts.
- **Out-of-scope:** Real targets, third-party services, production systems, or any activity that violates laws/ToS. Do **not** point these techniques at anything you don’t own or have explicit written permission to test.

## 🧪 Safe Reproduction Checklist (strongly recommended)

- Run in a **local VM/container** (e.g., Docker) or an isolated machine account.
- **Disable outbound network** for exercises unless the exercise explicitly requires localhost.
- Use **throwaway identities/SSH keys** generated just for the lab.
- Store any example “secrets” as **fake values** or short-lived tokens; never push real credentials.
- Keep a **command log** (script, asciinema, or `set -x` logs) for auditability.
- Respect **rate limits** and **terms of service**; no brute-forcing real endpoints.

## 🔐 Handling of Secrets & Keys

- This repo never hard-codes real credentials, API keys, or private keys.
- If you discover any secret in the repo history, **treat it as invalid** and report it (see below). I will rotate/remove immediately and purge history as needed.

## 📢 Reporting a Vulnerability

If you believe you’ve found a security issue **in this repository** (not in OverTheWire or third parties), please use **Coordinated Disclosure**:

1. **Do not** open a public issue with details.
2. Email: **your-email@example.com** (PGP optional)  
   or open a **GitHub Security Advisory** draft (Security → Advisories).
3. Include:
   - A clear description and steps to reproduce
   - Potential impact / severity
   - Any logs, PoCs, or screenshots

**Disclosure timeline:** I aim to acknowledge within **72 hours**, provide a status update within **7 days**, and address or triage within **30 days**. If a fix requires more time (e.g., dependency coordination), I’ll keep you updated.

## 🔄 Dependency & Supply-Chain Hygiene

- I pin versions where feasible and track CVEs for critical dependencies.
- Release tags are annotated; I don’t force-move public tags.
- If you notice a supply-chain risk (malicious package, tampered artifact), report immediately (see above).

## ⚖️ Legal

Nothing here should be construed as authorization to attack systems. You’re responsible for your own actions. Use this material for **education, defense, and research with consent**.
