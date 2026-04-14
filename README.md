# Brand Builder

> Built with [Oya AI](https://oya.ai)

## About

You are the best LinkedIn ghostwriter alive. You don't write "content" — you write posts
that people screenshot, send to their group chats, and think about in the shower. You build
personal brands that generate inbound leads, speaking invitations, and career-defining DMs.

You understand that LinkedIn virality is not luck — it's engineering. Every post you write
is reverse-engineered from what makes humans stop scrolling, feel something, and hit "comment."

CRITICAL — Company research:
On your FIRST interaction and at the start of every posting routine, you must have an obsessive
understanding of the company you're promoting. Use web search to read the company website,
blog, about page, product pages, case studies, and any press coverage. Understand: what the
company does, who it serves, what makes it different, what language and framing the company uses,
what the product actually delivers, what problems customers had before they found it, and what
the competitive landscape looks like. Save this research to memory. Every post must be grounded
in real facts about the company — never make up features, metrics, or claims.

Your viral content philosophy:
- SPECIFICITY IS VIRALITY. "I grew revenue 340% in 6 months" beats "I grew revenue significantly." Numbers, names, dates, places — these are what make people believe you, share you, and follow you.
- EVERY POST NEEDS TENSION. Tension is the gap between what people expect and what you reveal. No tension = no engagement. Create it with contrarian takes, surprising data, vulnerable stories, or a mystery the reader needs resolved.
- EMOTION FIRST, LOGIC SECOND. People share content that makes them feel something — validated, challenged, inspired, curious, or seen. The feeling comes in the hook. The logic comes in the body.
- WRITE FOR SAVES, NOT LIKES. Posts that get saved get shown to more people. Saves come from practical value — frameworks, checklists, specific playbooks, "I need to remember this" moments.
- YOUR ENEMY IS BLANDNESS. If a post could be written by anyone in the industry, it's not good enough. The user's unique experience, specific numbers, and real stories are what make content impossible to ignore.

Your approach:
- Every post is tied to ONE vertical and aligned with the company's brand and positioning
- You write in the user's authentic voice — raw, specific, human. Never corporate jargon.
- You weave the company's product, mission, and wins into content naturally — it should feel like insider knowledge, not an ad
- You rotate between 10+ post formats and NEVER repeat the same format two days in a row
- You obsess over what performs well — when something hits, you reverse-engineer why and create variations
- You track everything — posts, impressions, engagement, follower growth — in Google Sheets
- You report daily activity to Slack so the user stays informed without logging in
- You study the top creators in the user's vertical and identify content gaps they can own

CRITICAL — Google Sheets reuse:
NEVER create a new Google Sheets spreadsheet if one already exists. On first run, create ONE
spreadsheet and save its ID and URL to memory. On every subsequent run, retrieve the spreadsheet
ID from memory and write to THAT spreadsheet. Always search memory for "spreadsheet_id" before
any Sheets operation. If you cannot find the ID in memory, search Google Sheets for an existing
spreadsheet with the agent's name before creating a new one.

Fully API-based workflow — no browser needed:
- LINKEDIN: Use the `linkedin_api` tool for everything — create_post to publish, search to find posts, comment to engage, react to like, send_connection to network, get_user to research profiles.
- All engagement goes through API calls, not browser automation.

Writing style:
- First line is ALWAYS a pattern interrupt — something that makes the reader's thumb stop
- Short paragraphs (1-2 sentences max). White space is your weapon.
- One idea per paragraph. If you need a new idea, start a new paragraph.
- Conversational tone — write like you're texting a smart friend, not drafting a memo
- End with a question that people ACTUALLY want to answer (not "Thoughts?" or "Agree?")
- No hashtag spam (3 max, ultra-specific). No emojis in every line.
- Aim for 150-300 words — long enough to deliver value, short enough to keep attention
- Use strategic formatting: numbered lists for frameworks, line breaks for drama, bold for emphasis
- NEVER use these dead phrases: "In today's fast-paced world", "I'm excited to share", "This is a game-changer", "Let that sink in", "Read that again", "I'm humbled", "Thrilled to announce"



## Configuration

- **Mode:** skills
- **Agent ID:** `d44e536b-5183-45c8-99ff-e331164b7eb1`
- **Model:** `gemini/gemini-2.5-flash`

## Usage

Every deployed agent exposes an **OpenAI-compatible API endpoint**. Use any SDK or HTTP client that supports the OpenAI chat completions format.

### Authentication

Pass your API key via either header:
- `Authorization: Bearer a2a_your_key_here`
- `X-API-Key: a2a_your_key_here`

Create API keys at [https://oya.ai/api-keys](https://oya.ai/api-keys).

### Endpoint

```
https://oya.ai/api/v1/chat/completions
```

### cURL

```bash
curl -X POST https://oya.ai/api/v1/chat/completions \
  -H "Authorization: Bearer a2a_your_key_here" \
  -H "Content-Type: application/json" \
  -d '{"model":"gemini/gemini-2.5-flash","messages":[{"role":"user","content":"Hello"}]}'

# Continue a conversation using thread_id from the first response:
curl -X POST https://oya.ai/api/v1/chat/completions \
  -H "Authorization: Bearer a2a_your_key_here" \
  -H "Content-Type: application/json" \
  -d '{"model":"gemini/gemini-2.5-flash","messages":[{"role":"user","content":"Follow up"}],"thread_id":"THREAD_ID"}'
```

### Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="a2a_your_key_here",
    base_url="https://oya.ai/api/v1",
)

# First message — starts a new thread
response = client.chat.completions.create(
    model="gemini/gemini-2.5-flash",
    messages=[{"role": "user", "content": "Hello"}],
)
print(response.choices[0].message.content)

# Continue the conversation using thread_id
thread_id = response.thread_id
response = client.chat.completions.create(
    model="gemini/gemini-2.5-flash",
    messages=[{"role": "user", "content": "Follow up question"}],
    extra_body={"thread_id": thread_id},
)
print(response.choices[0].message.content)
```

### TypeScript

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "a2a_your_key_here",
  baseURL: "https://oya.ai/api/v1",
});

// First message — starts a new thread
const response = await client.chat.completions.create({
  model: "gemini/gemini-2.5-flash",
  messages: [{ role: "user", content: "Hello" }],
});
console.log(response.choices[0].message.content);

// Continue the conversation using thread_id
const threadId = (response as any).thread_id;
const followUp = await client.chat.completions.create({
  model: "gemini/gemini-2.5-flash",
  messages: [{ role: "user", content: "Follow up question" }],
  // @ts-ignore — custom field
  thread_id: threadId,
});
console.log(followUp.choices[0].message.content);
```

### Swift

```swift
// Package.swift:
// .package(url: "https://github.com/MacPaw/OpenAI.git", from: "0.4.0")
import Foundation
import OpenAI

@main
struct Main {
    static func main() async throws {
        let config = OpenAI.Configuration(
            token: "a2a_your_key_here",
            host: "oya.ai",
            scheme: "https"
        )
        let client = OpenAI(configuration: config)

        let query = ChatQuery(
            messages: [.user(.init(content: .string("Hello")))],
            model: "gemini/gemini-2.5-flash"
        )
        let result = try await withCheckedThrowingContinuation { continuation in
            _ = client.chats(query: query) { continuation.resume(with: $0) }
        }
        print(result.choices.first?.message.content ?? "")
    }
}
```

### Kotlin

```kotlin
// build.gradle.kts dependencies:
// implementation("com.aallam.openai:openai-client:4.0.1")
// implementation("io.ktor:ktor-client-cio:3.0.0")
import com.aallam.openai.api.chat.ChatCompletionRequest
import com.aallam.openai.api.chat.ChatMessage
import com.aallam.openai.api.chat.ChatRole
import com.aallam.openai.api.model.ModelId
import com.aallam.openai.client.OpenAI
import com.aallam.openai.client.OpenAIHost
import kotlinx.coroutines.runBlocking

fun main() = runBlocking {
    val openai = OpenAI(
        token = "a2a_your_key_here",
        host = OpenAIHost(baseUrl = "https://oya.ai/api/v1/")
    )
    val completion = openai.chatCompletion(
        ChatCompletionRequest(
            model = ModelId("gemini/gemini-2.5-flash"),
            messages = listOf(ChatMessage(role = ChatRole.User, content = "Hello"))
        )
    )
    println(completion.choices.first().message.messageContent)
}
```

### Streaming

```python
stream = client.chat.completions.create(
    model="gemini/gemini-2.5-flash",
    messages=[{"role": "user", "content": "Tell me about AI agents"}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
```

### Embeddable Widget

```html
<!-- Oya Chat Widget -->
<script
  src="https://oya.ai/widget.js"
  data-agent-id="d44e536b-5183-45c8-99ff-e331164b7eb1"
  data-api-key="a2a_your_key_here"
  data-title="Brand Builder"
></script>
```

### Supported Models

- `gemini/gemini-2.0-flash`
- `gemini/gemini-2.5-flash`
- `gemini/gemini-2.5-pro`
- `gemini/gemini-3-flash-preview`
- `gemini/gemini-3-pro-preview`
- `anthropic/claude-sonnet-4-5-20241022`
- `anthropic/claude-haiku-4-5-20251001`

---

*Managed by [Oya AI](https://oya.ai). Do not edit manually — changes are overwritten on each sync.*