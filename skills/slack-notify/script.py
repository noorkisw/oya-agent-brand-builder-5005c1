import os
import json
import httpx
from datetime import datetime


def post_to_slack(webhook_url, payload, timeout=15):
    with httpx.Client(timeout=timeout) as c:
        r = c.post(webhook_url, json=payload, headers={"Content-Type": "application/json"})
        if r.status_code >= 400:
            raise Exception(f"Slack webhook error {r.status_code}: {r.text[:500]}")
        if r.text != "ok":
            raise Exception(f"Slack returned unexpected response: {r.text[:200]}")


def build_base_payload(inp):
    payload = {}
    username = inp.get("username", "LinkedIn Bot")
    if username:
        payload["username"] = username
        payload["icon_emoji"] = ":linkedin:"
    channel = inp.get("channel", "")
    if channel:
        payload["channel"] = channel
    return payload


def do_post_message(webhook_url, inp):
    message = inp.get("message", "").strip()
    if not message:
        return {"error": "Provide a non-empty 'message' to post"}
    payload = build_base_payload(inp)
    payload["text"] = message
    post_to_slack(webhook_url, payload)
    return {"status": "ok", "action": "post_message"}


def do_post_status_update(webhook_url, inp):
    today = datetime.utcnow().strftime("%A, %B %d %Y")
    posts_published = int(inp.get("posts_published", 0))
    impressions = int(inp.get("impressions", 0))
    likes = int(inp.get("likes", 0))
    comments = int(inp.get("comments", 0))
    shares = int(inp.get("shares", 0))
    post_titles = inp.get("post_titles", [])

    titles_text = ""
    if post_titles:
        titles_text = "\n".join(f"  • {t}" for t in post_titles)
    else:
        titles_text = "  _No posts listed_"

    blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": f":bar_chart: LinkedIn Daily Report — {today}", "emoji": True}
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Posts Published*\n{posts_published}"},
                {"type": "mrkdwn", "text": f"*Impressions*\n{impressions:,}"},
                {"type": "mrkdwn", "text": f"*Likes*\n{likes:,}"},
                {"type": "mrkdwn", "text": f"*Comments*\n{comments:,}"},
                {"type": "mrkdwn", "text": f"*Shares*\n{shares:,}"},
            ]
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Posts Published Today:*\n{titles_text}"}
        },
        {
            "type": "context",
            "elements": [{"type": "mrkdwn", "text": f"Report generated at {datetime.utcnow().strftime('%H:%M UTC')}"}]
        }
    ]

    payload = build_base_payload(inp)
    payload["text"] = f":bar_chart: LinkedIn Daily Report — {today}"
    payload["blocks"] = blocks
    post_to_slack(webhook_url, payload)
    return {"status": "ok", "action": "post_status_update", "posts_published": posts_published}


def do_post_error_alert(webhook_url, inp):
    error_type = inp.get("error_type", "UnknownError").strip()
    error_message = inp.get("error_message", "An error occurred.").strip()
    retry_after = int(inp.get("retry_after", 0))

    if not error_message:
        return {"error": "Provide 'error_message' describing what went wrong"}

    retry_text = ""
    if retry_after > 0:
        minutes = retry_after // 60
        seconds = retry_after % 60
        retry_text = f"\n*Retry After:* {minutes}m {seconds}s" if minutes else f"\n*Retry After:* {seconds}s"

    is_rate_limit = "ratelimit" in error_type.lower() or "rate_limit" in error_type.lower() or "429" in error_message
    emoji = ":warning:" if is_rate_limit else ":rotating_light:"
    color = "#FFA500" if is_rate_limit else "#FF0000"

    blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": f"{emoji} LinkedIn Bot Error: {error_type}", "emoji": True}
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Error Details:*\n