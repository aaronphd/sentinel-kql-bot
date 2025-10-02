import os
import re
import yaml

# -------------------------------
# Load all KQL templates
# -------------------------------
def load_templates():
    templates = {}
    for path in (
        "kql_templates/authentication.yaml",
        "kql_templates/network.yaml",
        "kql_templates/anomalies.yaml",
    ):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
                templates.update(data)
        except FileNotFoundError:
            print(f"⚠️ Warning: {path} not found, skipping.")
    return templates


# -------------------------------
# Parse natural language command
# -------------------------------
def parse_command(text: str):
    t = text.strip().lower()

    # Default parameters
    params = {"hours": 24, "user": "", "ips": ""}

    # Extract hours (e.g., "last 12h" or "past 48 hours")
    m = re.search(r"(last|past)\s+(\d+)\s*(h|hour|hours)", t)
    if m:
        params["hours"] = int(m.group(2))

    # Extract user (e.g., user:alice@contoso.com)
    m = re.search(r"user:\s*([^\s]+)", t)
    if m:
        params["user"] = m.group(1)

    # Extract IPs (e.g., ips:1.2.3.4,5.6.7.8)
    m = re.search(r"ips:\s*([0-9\.,\s]+)", t)
    if m:
        ips = [ip.strip() for ip in m.group(1).split(",") if ip.strip()]
        params["ips"] = ", ".join(f'"{ip}"' for ip in ips)

    # Remove the /kql prefix if present
    if t.startswith("/kql"):
        t = t.replace("/kql", "").strip()

    # Intent routing
