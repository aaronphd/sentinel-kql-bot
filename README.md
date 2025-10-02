# Sentinel KQL Bot

A lightweight bot that converts natural-language intents into ready-to-run KQL queries for Microsoft Sentinel. Use GitHub Issues or Issue comments with the `/kql` command and the bot replies with a generated query.

## Examples

- `/kql failed logins last 24h`
- `/kql failed logins last 12h user:alice@contoso.com`
- `/kql suspicious ip activity last 6h ips:1.2.3.4,5.6.7.8`
- `/kql rare process creation last 48h`
- `/kql large data exfil last 24h`

## How it works

- Templates live in `kql_templates/*.yaml` with placeholders like `{hours}`, `{user}`, `{ips}`.
- A GitHub Actions workflow listens to issues/comments containing `/kql`, runs `main.py`, and posts the KQL back as a comment.

## Add new intents

1. Create or edit a template file under `kql_templates/`.
2. Add a new key with your KQL (use `{hours}`, `{user}`, `{ips}` if needed).
3. Update `parse_command()` in `main.py` to route natural language to your new key.

## Local use

```bash
pip install -r requirements.txt
python main.py
