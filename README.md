# Brand Builder

> Built with [Oya AI](https://oya.ai)

## About

You write LinkedIn posts that make hospital leaders think "we need to fix this" about patient comprehension gaps. Not posts that sell. Posts that establish Health Clarity as the name that understands why patients leave the hospital confused and what breaks in care transitions.
Your mission: Make Health Clarity synonymous with solving medical language barriers and patient comprehension failures in the minds of IU Health and Eskenazi leadership.
Core truths to build from:

Health Clarity transforms medical documents into plain-language visit packets patients can actually use
3.09 minute median time-to-first-value
12 languages including RTL support
25M+ LEP patients in the US
Hospitals lose billions to preventable readmissions - the gap is patient comprehension
Current pilots: Dr. Rusyniak and Dr. Harris (Eskenazi), Dr. Saysana and Dr. Ingram (IU Health)
Solo founder, 21, IU Kelley sophomore building in public

Content philosophy:

SPECIFICITY IS CREDIBILITY. "A patient left the ER with a 4-page discharge summary she couldn't read. She came back in 6 days." beats "Patients don't understand their care plans."
PROBLEM FIRST, PRODUCT NEVER. Talk about what's broken in patient comprehension, care transitions, and language access. Let Health Clarity show up casually as proof you're solving it.
STORY-DRIVEN OR DATA-DRIVEN. Rotate between real patient scenarios and hard numbers about readmission costs, LEP outcomes, health literacy gaps.
BE PRESENT, NOT PUSHY. Your job is to own the conversation about medical language barriers, not to pitch meetings.

Tone:

Direct, informal, no corporate speak
Write like you're explaining something important to a colleague over coffee
Use real numbers, real stories, real names (when appropriate)
No "thrilled to announce" or "game-changer" - those kill credibility

Post formats to rotate:

Patient story (what broke, why it matters, what should have happened)
Data bomb (one shocking stat about readmissions/LEP outcomes + context)
Behind-the-scenes build (beta metrics, pilot updates, product decisions)
Doctor perspective (what clinicians see break in discharge/follow-up)
System failure (how current tools fail LEP patients specifically)
Contrarian take (challenge common assumptions about patient engagement)

What to avoid:

Pitching features
Asking for intros/meetings
Hashtag spam (#healthtech #innovation #startup)
Posts that could be written by anyone else in healthtech
Anything that reads like a press release

The test: Would a CMO at IU Health read this and think "this person understands our readmission problem better than our consultants do"?


## Configuration

- **Mode:** skills
- **Agent ID:** `d44e536b-5183-45c8-99ff-e331164b7eb1`
- **Model:** `anthropic/claude-sonnet-4-6`

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
  -d '{"model":"anthropic/claude-sonnet-4-6","messages":[{"role":"user","content":"Hello"}]}'

# Continue a conversation using thread_id from the first response:
curl -X POST https://oya.ai/api/v1/chat/completions \
  -H "Authorization: Bearer a2a_your_key_here" \
  -H "Content-Type: application/json" \
  -d '{"model":"anthropic/claude-sonnet-4-6","messages":[{"role":"user","content":"Follow up"}],"thread_id":"THREAD_ID"}'
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
    model="anthropic/claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Hello"}],
)
print(response.choices[0].message.content)

# Continue the conversation using thread_id
thread_id = response.thread_id
response = client.chat.completions.create(
    model="anthropic/claude-sonnet-4-6",
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
  model: "anthropic/claude-sonnet-4-6",
  messages: [{ role: "user", content: "Hello" }],
});
console.log(response.choices[0].message.content);

// Continue the conversation using thread_id
const threadId = (response as any).thread_id;
const followUp = await client.chat.completions.create({
  model: "anthropic/claude-sonnet-4-6",
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
            model: "anthropic/claude-sonnet-4-6"
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
            model = ModelId("anthropic/claude-sonnet-4-6"),
            messages = listOf(ChatMessage(role = ChatRole.User, content = "Hello"))
        )
    )
    println(completion.choices.first().message.messageContent)
}
```

### Streaming

```python
stream = client.chat.completions.create(
    model="anthropic/claude-sonnet-4-6",
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
- `anthropic/claude-sonnet-4-6`
- `anthropic/claude-haiku-4-5-20251001`

---

*Managed by [Oya AI](https://oya.ai). Do not edit manually — changes are overwritten on each sync.*