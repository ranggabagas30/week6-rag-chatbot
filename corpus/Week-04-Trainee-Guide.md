**Week 4 Trainee Guide**

Tool Use & Function Calling

AI Engineer Career Pivot Program · 6-Month Weekend Cohort

# **1\. Learning Objectives**

-   Explain the tool-use contract: the model requests, your code executes, results return as tool\_result blocks.
-   Design tool schemas with descriptions that tell the model WHEN to use them.
-   Implement the full tool loop with Pydantic-validated inputs.
-   Handle timeouts, retries, rate limits, and runaway loops like a production engineer.
-   Ship Milestone Project 1: a streaming assistant with three or more tools.

# **2\. Before Saturday**

1.  Pick one free live-data API to wrap as a tool (weather, exchange rates, public holidays — a list is pinned in the cohort channel). Sign up for its key if needed.
2.  Re-read your Week 2 chat loop — Milestone 1 is built directly on top of it.
3.  Think about a third tool that touches files or data: reading a CSV, searching a folder, or calling your Week 3 extractor.

# **3\. Saturday Session — Topic Notes**

## **3.1 The Mental Model**

The model never runs anything. When it decides a tool would help, it stops generating prose and returns a tool\_use block: the tool name plus arguments as JSON. Your code looks up the function, validates the arguments, executes it, and sends the result back as a tool\_result block. The model then continues — maybe answering, maybe calling another tool. Everything an “agent” does in Month 3 is this loop plus planning and memory.

## **3.2 Tool Schemas Are Contracts**

Each tool is defined by a name, a description, and a JSON input schema. The description is the most underrated part: it must say WHEN to use the tool (“Use whenever the user asks about prices in another currency”), not just what it does — the model chooses tools by reading descriptions. Prefer several small, focused tools over one mega-tool with a mode parameter. And never trust incoming arguments: validate them with a Pydantic model before executing, exactly like Week 3.

## **3.3 Production Hygiene**

Tools fail; plan for it. Every external call gets a 5–10 second timeout. Transient failures (network errors, 429s, 5xx) get a retry with exponential backoff; non-idempotent actions never get blind retries. Respect rate limits. Cap tool calls per user request (a loop guard of ~8) so a confused model can’t spin forever. And the golden rule: a tool never raises into the loop — it returns an error STRING as its tool\_result, so the model can read what went wrong and apologise, retry, or route around it.

# **4\. Coding Walkthrough — milestone-1-tool-assistant**

## **Step 1 · Scaffold from Week 2**

$ mkdir milestone-1-tool-assistant && cd milestone-1-tool-assistant

$ uv venv && source .venv/bin/activate

$ uv pip install anthropic python-dotenv pydantic httpx

\# copy config.py, .gitignore, .env pattern from week 2 ✔ commit

## **Step 2 · First tool — exact math**

\# tools/calculator.py

from pydantic import BaseModel

class CalcInput(BaseModel):

expression: str

def run(args: dict) -> str:

expr = CalcInput.model\_validate(args).expression

allowed = set("0123456789+-\*/(). ")

if not set(expr) <= allowed:

return "ERROR: only basic arithmetic is allowed"

try:

return str(eval(expr, {"\_\_builtins\_\_": {}}))

except Exception as e:

return f"ERROR: {e}"

Note both rules in action: inputs validated, and failures returned as strings, never raised. ✔ Commit.

## **Step 3 · Tool registry + definitions**

\# tools/\_\_init\_\_.py

from tools import calculator, fx, files

REGISTRY = {"calculator": calculator.run,

"get\_fx\_rate": fx.run,

"read\_data": files.run}

TOOLS = \[

{"name": "calculator",

"description": "Evaluate an arithmetic expression exactly. "

"Use for ANY math instead of computing yourself.",

"input\_schema": {"type": "object", "properties":

{"expression": {"type": "string"}},

"required": \["expression"\]}},

\# ... fx and files defined the same way

\]

## **Step 4 · The tool loop**

MAX\_TOOL\_CALLS = 8

def run\_turn(msgs: list) -> str:

calls = 0

while True:

resp = client.messages.create(model=MODEL,

max\_tokens=1000, tools=TOOLS, messages=msgs)

if resp.stop\_reason != "tool\_use":

return "".join(b.text for b in resp.content

if b.type == "text")

calls += len(\[b for b in resp.content

if b.type == "tool\_use"\])

if calls > MAX\_TOOL\_CALLS:

return "Stopped: too many tool calls."

msgs.append({"role": "assistant",

"content": resp.content})

results = \[{"type": "tool\_result",

"tool\_use\_id": b.id,

"content": REGISTRY\[b.name\](b.input)}

for b in resp.content

if b.type == "tool\_use"\]

msgs.append({"role": "user", "content": results})

Wire this into your Week 2 chat loop in place of the plain create call. Test: “What is 12.5% of 3,840?” must trigger the calculator. ✔ Commit.

## **Step 5 · Live API tool with timeout**

\# tools/fx.py

import httpx

from pydantic import BaseModel

class FxInput(BaseModel):

base: str

quote: str

def run(args: dict) -> str:

try:

a = FxInput.model\_validate(args)

r = httpx.get(RATE\_URL.format(a.base, a.quote),

timeout=8.0)

r.raise\_for\_status()

return str(r.json()\["rate"\])

except Exception as e:

return f"ERROR: fx lookup failed: {e}"

Test the failure path deliberately: turn off Wi-Fi mid-question and watch the model receive the error string and respond gracefully. ✔ Commit.

## **Step 6 · Third tool + the end-to-end demo**

Add your file/data tool (e.g., read a CSV of expenses, or wrap your Week 3 extractor). Then craft the demo request your README GIF will show — something forcing multiple tools in sequence, like: “Read expenses.csv, total the amounts, and convert the total to USD.” That single request exercising three tools IS the milestone. ✔ Commit, README with architecture sketch + GIF, branch, PR, submit with #milestone1.

# **5\. Sunday Lab — Exercises**

1.  Calculator tool working end-to-end — confirm the model stops doing mental math.
2.  Wrap the live API with timeout and error strings; test the offline failure path.
3.  Bad-input drill: prompt the model into sending wrong argument types; watch Pydantic catch it and the model self-correct.
4.  Loop guard: create a runaway scenario and verify the cap ends it cleanly.

# **6\. Milestone Project 1 — Due Next Friday 23:59**

Full spec is in the deck and mirrors the walkthrough: streaming assistant + tool loop, 3+ tools (computation, live API, file/data), Pydantic-validated inputs, timeouts and error strings, loop guard of 8, README with architecture sketch and demo GIF. Acceptance: a multi-step request works end-to-end, failing tools degrade gracefully with no stack traces, bad arguments self-correct, type hints throughout, 8+ meaningful commits. This is portfolio piece #1 — give the README the care a hiring manager deserves.

# **7\. Looking Ahead — Month 2**

Week 5 opens the RAG month: embeddings and vector search with Qdrant, including multilingual embeddings that matter for Southeast Asian products. Bring 20+ real (anonymised) documents from your domain — they become your searchable knowledge base and, by Week 8, your second portfolio project.