# 🛡️ The Isaacs Group — Sentinel KQL Bot

**Cyber Weekly Tools for Public Education SOCs**

This repository provides a lightweight bot that converts natural-language prompts into ready-to-run KQL queries for Microsoft Sentinel. It is designed to help **beginner SOC teams in K‑12 and higher education** quickly generate useful detections and hunting queries.

---

## 🎓 Why This Matters for Education

Schools and districts face unique challenges:
- Limited IT/security staff
- High-value targets (student data, financial systems, learning platforms)
- Frequent phishing and account compromise attempts

This bot helps bridge the gap by giving SOC analysts **ready-made, defensible KQL queries** aligned with common threats in education.

---

## 🚀 How It Works

- Templates live in `kql_templates/*.yaml` with placeholders like `{hours}`, `{user}`, `{ips}`.
- A GitHub Actions workflow listens to issues/comments containing `/kql`, runs `main.py`, and posts the KQL back as a comment.
- Queries are grouped into:
  - **Authentication** (failed logins, risky sign-ins)
  - **Network** (suspicious IPs, rare destinations, blocked connections)
  - **Anomalies** (rare processes, suspicious PowerShell, data exfiltration)

---

## 📖 Example Usage
👉 See the [SOC Quick Reference](SOC_Quick_Reference.md) for a one‑page guide to all starter queries.
Open a GitHub Issue or comment with:

- `/kql failed logins last 24h`
- `/kql risky signins last 12h`
- `/kql suspicious ip activity last 6h ips:1.2.3.4,5.6.7.8`
- `/kql rare process creation last 48h`
- `/kql large data exfil last 24h`

The bot will reply with a formatted KQL query you can paste directly into Microsoft Sentinel.

---

## 🧩 Extending the Bot

1. Create or edit templates under `kql_templates/`.
2. Update `parse_command()` in `main.py` to route natural language to your new template.
3. Commit and push — the bot will immediately support the new query.

---

## ✍️ Branding

This project is maintained by **The Isaacs Group** — a cybersecurity and risk management consultancy specializing in **governance, compliance, and operational resilience** for education and nonprofit sectors.

> *Protecting data. Preserving trust. Empowering education.*
