---
name: slack-notifier
display_name: "Slack Notifier"
description: "Post messages to a Slack channel via webhook to send status updates, activity reports, and error notifications"
category: communication
icon: message-square
skill_type: sandbox
catalog_type: addon
requirements: "httpx>=0.25"
resource_requirements:
  - env_var: SLACK_WEBHOOK_URL
    name: "Slack Webhook URL"
    description: "Incoming Webhook URL from Slack (Slack App > Incoming Webhooks > Webhook URL, e.g. https://hooks.slack.com/services/T.../B.../...)"
tool_schema:
  name: slack-notifier
  description: "Post messages to a Slack channel via webhook to send status updates, activity reports, and error notifications"
  parameters:
    type: object
    properties:
      action:
        type: "string"
        description: "Which operation to perform"
        enum: ["post_message", "post_status_update", "post_error"]
      message:
        type: "string"
        description: "The message text to post to Slack (plain text or Slack markdown)"
        default: ""
      title:
        type: "string"
        description: "Optional title/header for the message block (used in post_status_update and post_error)"
        default: ""
      fields:
        type: "object"
        description: "Optional key-value pairs to display as structured fields (e.g. {\"Posts Today\": \"3\", \"Impressions\": \"1240\"})"
        default: {}
      color:
        type: "string"
        description: "Sidebar color for the attachment: 'good' (green), 'warning' (yellow), 'danger' (red), or a hex color like '#3B82F6'"
        default: "good"
    required: [action, message]
---
# Slack Notifier

Post messages to a Slack channel via Incoming Webhooks. Ideal for sending daily LinkedIn activity summaries, engagement metrics, and error or rate-limit alerts — keeping your team informed without leaving your workflow.

## Setup

To use this skill, you must configure the `SLACK_WEBHOOK_URL` environment variable:

1. Go to your Slack workspace and open **Apps**
2. Search for or create an **Incoming Webhooks** app
3. Click **Add New Webhook to Workspace** and choose a channel
4. Copy the generated **Webhook URL** (starts with `https://hooks.slack.com/services/...`)
5. Set it as the `SLACK_WEBHOOK_URL` environment variable in your agent configuration

## Actions

### post_message
Send a simple plain-text or Slack-markdown message to the configured channel.

**Example parameters:**

    {
      "action": "post_message",
      "message": "Hello from your agent! :wave:"
    }

### post_status_update
Send a structured message with an optional title, body text, key-value fields, and a colored sidebar.

**Example parameters:**

    {
      "action": "post_status_update",
      "title": "Daily LinkedIn Summary",
      "message": "Here is your activity report for today.",
      "fields": {
        "Posts Today": "3",
        "Impressions": "1240",
        "New Connections": "5"
      },
      "color": "good"
    }

### post_error
Send an error notification with a red sidebar, optional title, and structured fields.

**Example parameters:**

    {
      "action": "post_error",
      "title": "Rate Limit Hit",
      "message": "LinkedIn API returned 429 Too Many Requests.",
      "fields": {
        "Retry After": "60s",
        "Endpoint": "/posts"
      },
      "color": "danger"
    }