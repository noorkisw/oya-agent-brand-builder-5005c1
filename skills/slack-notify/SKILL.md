---
name: slack-notify
display_name: "Slack Notifications"
description: "Post messages to a Slack channel via webhook, including daily LinkedIn activity status updates and error/rate-limit alerts"
category: communication
icon: message-square
skill_type: sandbox
catalog_type: addon
requirements: "httpx>=0.25"
resource_requirements:
  - env_var: SLACK_WEBHOOK_URL
    name: "Slack Incoming Webhook URL"
    description: "Incoming webhook URL from your Slack app (Slack App > Incoming Webhooks > Webhook URL, e.g. https://hooks.slack.com/services/XXX/YYY/ZZZ)"
tool_schema:
  name: slack-notify
  description: "Post messages to a Slack channel via webhook — use for daily LinkedIn activity status updates and error/rate-limit alerts"
  parameters:
    type: object
    properties:
      action:
        type: "string"
        description: "Which operation to perform"
        enum: ["post_message", "post_status_update", "post_error_alert"]
      message:
        type: "string"
        description: "Plain text message to post (for post_message action)"
        default: ""
      channel:
        type: "string"
        description: "Override the default channel set in the webhook (e.g. '#linkedin-updates'). Leave empty to use webhook default."
        default: ""
      username:
        type: "string"
        description: "Display name for the bot posting the message"
        default: "LinkedIn Bot"
      posts_published:
        type: "integer"
        description: "Number of LinkedIn posts published today (for post_status_update)"
        default: 0
      impressions:
        type: "integer"
        description: "Total impressions today (for post_status_update)"
        default: 0
      likes:
        type: "integer"
        description: "Total likes today (for post_status_update)"
        default: 0
      comments:
        type: "integer"
        description: "Total comments today (for post_status_update)"
        default: 0
      shares:
        type: "integer"
        description: "Total shares today (for post_status_update)"
        default: 0
      post_titles:
        type: "array"
        description: "List of post titles or snippets published today (for post_status_update)"
        items:
          type: "string"
        default: []
      error_type:
        type: "string"
        description: "Type of error (e.g. 'RateLimitError', 'AuthError') for post_error_alert"
        default: ""
      error_message:
        type: "string"
        description: "Detailed error message for post_error_alert"
        default: ""
      retry_after:
        type: "integer"
        description: "Seconds until retry is allowed (for rate limit errors in post_error_alert)"
        default: 0
    required: [action]
---
# Slack Notifications

Post messages to a Slack channel via an Incoming Webhook. Designed to report daily LinkedIn activity summaries and surface errors or rate-limit issues in real time.

## Actions

### post_message
Send a plain text (or markdown) message to the configured Slack channel.

**Example parameters:**