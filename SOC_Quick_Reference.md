# 🛡️ The Isaacs Group — SOC Quick Reference

**Beginner SOC Queries for Public Education (Microsoft Sentinel)**

This quick reference summarizes the starter KQL templates included in this repo. Use these during investigations or as a training aid for new analysts.

---

## 🔐 Authentication

- **Failed Logins (last X hours)**  
  Detect repeated failed login attempts.  
  Template: `failed_logins_last_hours`

- **Risky Sign-ins (last X hours)**  
  Identify sign-ins flagged with a risk level.  
  Template: `risky_signins_last_hours`

- **Multiple Failed then Success**  
  Spot accounts with many failed attempts followed by a success (possible brute force).  
  Template: `multiple_failed_then_success`

---

## 🌐 Network

- **Suspicious IP Activity**  
  Track sign-ins from specific IPs.  
  Template: `suspicious_ip_activity_last_hours`

- **Rare External Destinations**  
  Find unusual outbound connections.  
  Template: `rare_external_destinations_last_hours`

- **Blocked Firewall Connections**  
  Review blocked network traffic.  
  Template: `blocked_firewall_connections`

---

## ⚠️ Anomalies

- **Rare Process Creation**  
  Highlight processes rarely seen in your environment.  
  Template: `rare_process_creation_last_hours`

- **Suspicious PowerShell Usage**  
  Detect encoded or malicious PowerShell commands.  
  Template: `suspicious_powershell_usage`

- **Large Data Exfiltration**  
  Spot abnormal file downloads (potential data theft).  
  Template: `large_data_exfil_last_hours`

---

## 🧭 Usage Tips

- Run queries in **Microsoft Sentinel → Logs**.
- Adjust `{hours}`, `{user}`, `{ips}` placeholders as needed.
- Use this guide as a **training tool** for junior analysts.

---

## ✍️ Branding

Maintained by **The Isaacs Group** — protecting data, preserving trust, and empowering education.
