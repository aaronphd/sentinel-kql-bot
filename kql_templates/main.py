import os
import re
import yaml

def load_templates():
    templates = {}
    for path in ("kql_templates/authentication.yaml",
                 "kql_templates/network.yaml",
                 "kql_templates/anomalies.yaml"):
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
            templates.update(data)
    return templates

def parse_command(text):
    # Normalize
    t = text.strip().lower()

    # Default values
    params = {"hours": 24, "user": "", "ips": ""}

    # Hours (e.g., "last 12h" or "past 48 hours")
    m = re.search(r"(last|past)\s+(\d+)\s*(h|hour|hours)", t)
    if m:
        params["hours"] = int(m.group(2))

    # User (e.g., user:alice@contoso.com)
    m = re.search(r"user:\s*([^\s]+)", t)
    if m:
        params["user"] = m.group(1)

    # IP list (e.g., ips:1.2.3.4,5.6.7.8)
    m = re.search(r"ips:\s*([0-9\.,\s]+)", t)
    if m:
        ips = [ip.strip() for ip in m.group(1).split(",") if ip.strip()]
        params["ips"] = ", ".join(f'"{ip}"' for ip in ips)  # quoted for KQL

    # Intent routing
    intent = None
    if "/kql" in t or t.startswith("kql "):
        t = t.replace("/kql", "").strip()

    if "failed login" in t and params["user"]:
        intent = "failed_logins_by_user_last_hours"
    elif "failed login" in t or "failed signin" in t:
        # Azure vs Windows hint
        if "azure" in t or "aad" in t:
            intent = "azure_failed_signins_last_hours"
        else:
            intent = "failed_logins_last_hours"
    elif "suspicious ip" in t or "ip activity" in t:
        intent = "suspicious_ip_activity_last_hours"
    elif "rare process" in t:
        intent = "rare_process_creation_last_hours"
    elif "exfil" in t or "downloaded" in t:
        intent = "large_data_exfil_last_hours"
    elif "rare destination" in t or "external destinations" in t:
        intent = "rare_external_destinations_last_hours"

    return intent, params

def render_query(templates, intent, params):
    if not intent or intent not in templates:
        return "No matching template found. Try: '/kql failed logins last 24h' or '/kql suspicious ip activity last 12h ips:1.2.3.4,5.6.7.8'."
    # Ensure required placeholders exist
    q = templates[intent]
    # Supply defaults for any missing placeholders
    if "{hours}" in q:
        q = q.format(hours=params.get("hours", 24),
                     user=params.get("user", ""),
                     ips=params.get("ips", ""))
    else:
        q = q.format(user=params.get("user", ""),
                     ips=params.get("ips", ""))
    return q

def main():
    comment = os.environ.get("ISSUE_COMMENT", "")
    templates = load_templates()
    intent, params = parse_command(comment)
    kql = render_query(templates, intent, params)
    # Print for logs and expose as output for the workflow
    print(kql)
    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
        f.write(f"kql<<EOF\n{kql}\nEOF\n")

if __name__ == "__main__":
    main()
