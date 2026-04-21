import os
import json
import httpx
from datetime import datetime, timezone

print(f"A2ABASEAI_FILE: script.py")


def post_to_slack(webhook_url: str, payload: dict, timeout: int = 15) -> None:
    with httpx.Client(timeout=timeout) as c:
        r = c.post(webhook_url, json=payload, headers={"Content-Type": "application/json"})
        if r.status_code >= 400:
            raise Exception(f"Slack API {r.status_code}: {r.text[:500]}")
        # Slack returns plain "ok" on success, not JSON
        if r.text.strip() != "ok":
            raise Exception(f"Unexpected Slack response: {r.text[:200]}")


def build_simple_payload(message: str) -> dict:
    return {"text": message}


def build_attachment_payload(title: str, message: str, fields: dict, color: str) -> dict:
    timestamp = int(datetime.now(tz=timezone.utc).timestamp())
    attachment = {
        "color": color,
        "fallback": title or message,
        "ts": timestamp,
    }
    if title:
        attachment["title"] = title
    if message:
        attachment["text"] = message
    if fields:
        attachment["fields"] = [
            {"title": k, "value": str(v), "short": True}
            for k, v in fields.items()
        ]
    return {"attachments": [attachment]}


def do_post_message(webhook_url: str, inp: dict) -> dict:
    message = inp.get("message", "").strip()
    if not message:
        return {"error": "Provide a non-empty 'message' to post"}
    payload = build_simple_payload(message)
    post_to_slack(webhook_url, payload)
    return {"status": "ok", "action": "post_message"}


def do_post_status_update(webhook_url: str, inp: dict) -> dict:
    message = inp.get("message", "").strip()
    if not message:
        return {"error": "Provide a non-empty 'message' for the status update"}
    title = inp.get("title", "").strip()
    fields = inp.get("fields", {})
    color = inp.get("color", "good").strip() or "good"
    if not isinstance(fields, dict):
        fields = {}
    payload = build_attachment_payload(title, message, fields, color)
    post_to_slack(webhook_url, payload)
    return {"status": "ok", "action": "post_status_update"}


def do_post_error(webhook_url: str, inp: dict) -> dict:
    message = inp.get("message", "").strip()
    if not message:
        return {"error": "Provide a non-empty 'message' describing the error"}
    title = inp.get("title", "🚨 Error").strip() or "🚨 Error"
    fields = inp.get("fields", {})
    color = inp.get("color", "danger").strip() or "danger"
    if not isinstance(fields, dict):
        fields = {}
    payload = build_attachment_payload(title, message, fields, color)
    post_to_slack(webhook_url, payload)
    return {"status": "ok", "action": "post_error"}


try:
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL", "").strip()
    if not webhook_url:
        raise Exception(
            "SLACK_WEBHOOK_URL environment variable is not set. "
            "Please configure it with your Slack Incoming Webhook URL "
            "(e.g. https://hooks.slack.com/services/T.../B.../...). "
            "You can create one at: Slack App > Incoming Webhooks > Add New Webhook to Workspace."
        )
    if not webhook_url.startswith("https://hooks.slack.com/"):
        raise Exception("SLACK_WEBHOOK_URL does not look like a valid Slack webhook URL (should start with https://hooks.slack.com/)")

    inp = json.loads(os.environ.get("INPUT_JSON", "{}"))
    action = inp.get("action", "").strip()

    if action == "post_message":
        result = do_post_message(webhook_url, inp)
    elif action == "post_status_update":
        result = do_post_status_update(webhook_url, inp)
    elif action == "post_error":
        result = do_post_error(webhook_url, inp)
    else:
        result = {
            "error": f"Unknown action: '{action}'. Available actions: post_message, post_status_update, post_error"
        }

    print(json.dumps(result))

except Exception as e:
    print(json.dumps({"error": str(e)}))