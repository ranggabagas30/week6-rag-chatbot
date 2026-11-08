**AI Engineer Career Pivot Program**

6-Month Weekend Syllabus

-   **Format:** Weekends only · 24 weeks · Cohort-based
-   **Schedule:** Saturday 4h live teaching + Sunday 3h guided lab/office hours, plus 8–10h self-paced homework on weekdays
-   **Who this is for:** Working professionals with basic programming exposure (any language) pivoting into AI engineering
-   **Outcome:** Job-ready or project-ready AI Engineer with a deployed portfolio of 3 production-grade projects + 1 capstone
-   **Guarantee:** Money-back if you don’t land a job or paid project after completing the program (see “Job Guarantee — Eligibility Conditions” at the end of this syllabus)

# **How This Program Is Designed**

1.  Build in public from Week 1 — every week produces a shippable artifact (repo, demo, or write-up) that compounds into your portfolio.
2.  Production over toys — evals, observability, cost control, and guardrails are taught alongside features, not as an afterthought.
3.  Employer-signal driven — the syllabus maps to what AI engineering job descriptions and freelance briefs actually ask for: LLM APIs, RAG, agents, evals, deployment.
4.  Client simulation — Months 4–5 run like a real consulting engagement: discovery → proposal → build → acceptance criteria → handover.

# **Month 1 — Foundations: Python, LLM APIs & Prompt Engineering (Weeks 1–4)**

***Goal:*** *From zero AI experience to shipping a working LLM-powered CLI app.*

## **Week 1 — Orientation & Modern Python for AI**

-   Program overview and a career map of AI engineering roles (AI engineer vs ML engineer vs data scientist)
-   Dev environment: VS Code, Git/GitHub, uv/pip, virtual environments, secrets management
-   Python essentials refresher: functions, typing, dataclasses/Pydantic, async basics
-   **Homework:** GitHub profile setup + first repo; Python drills

## **Week 2 — How LLMs Actually Work (An Engineer’s View)**

-   Tokens, context windows, temperature, sampling — what matters in practice
-   Model landscape: Claude, GPT, Gemini, open-weight models; how to choose (capability, cost, latency)
-   First API calls: chat completions, system prompts, streaming
-   **Homework:** Build a CLI chatbot with streaming and conversation history

## **Week 3 — Prompt Engineering as Engineering**

-   Prompt structure: role, instructions, few-shot examples, output schemas
-   Structured outputs: JSON mode, Pydantic validation, retries on parse failure
-   Prompt versioning and prompt-as-code patterns
-   **Homework:** Document extraction tool (unstructured text → validated JSON)

## **Week 4 — Tool Use & Function Calling**

-   Function calling / tool use APIs; designing good tool schemas
-   Error handling, retries, timeouts, rate limits
-   **Milestone Project 1:** LLM-powered assistant with 3+ tools (e.g., weather, calculator, web fetch) — delivered as a CLI with a README and demo GIF

# **Month 2 — RAG & Knowledge Systems (Weeks 5–8)**

***Goal:*** *Build a production RAG system on real documents with measurable retrieval quality.*

## **Week 5 — Embeddings & Vector Search**

-   Embeddings intuition; similarity metrics
-   Embedding model selection (e.g., bge-m3, Voyage, OpenAI) — including multilingual considerations for Southeast Asian markets
-   Vector databases: Qdrant hands-on (collections, payloads, filtering)
-   **Homework:** Semantic search over a document set

## **Week 6 — RAG Architecture End-to-End**

-   Chunking strategies (fixed, recursive, semantic, structural) and why chunking is 80% of RAG quality
-   Ingestion pipelines: PDF/DOCX/HTML parsing, metadata design
-   Retrieval → context assembly → generation, with citations
-   **Homework:** RAG chatbot over your own domain documents

## **Week 7 — Advanced Retrieval & RAG Evaluation**

-   Hybrid search (dense + BM25), reranking, query rewriting, HyDE
-   RAG evals: retrieval precision/recall, faithfulness, answer relevance; building a golden test set
-   Tooling: Ragas or a custom eval harness
-   **Homework:** Eval report comparing two retrieval configurations, with numbers

## **Week 8 — RAG in Production**

-   Caching, cost estimation, latency budgets
-   Handling stale data, incremental re-indexing, access control on documents
-   **Milestone Project 2:** Domain RAG assistant (legal, healthcare, finance, or your own industry) with an eval suite, deployed with a simple web UI (Streamlit/Gradio/FastAPI)

# **Month 3 — AI Agents & Orchestration (Weeks 9–12)**

***Goal:*** *Design, build, and debug multi-step agents that do real work.*

## **Week 9 — Agent Fundamentals**

-   The agent loop: reason → act → observe; the ReAct pattern
-   When agents beat pipelines (and when they don’t)
-   Building a minimal agent from scratch (no framework) to understand the internals
-   **Homework:** From-scratch agent that plans and executes a 3-step task

## **Week 10 — Agent Frameworks & MCP**

-   Framework survey: Claude Agent SDK, LangGraph, CrewAI — tradeoffs and when to use each
-   Model Context Protocol (MCP): building and consuming MCP servers
-   Skills/instructions patterns: giving agents reusable capabilities
-   **Homework:** Build one custom MCP server (e.g., an internal API wrapper) and connect it to an agent

## **Week 11 — Memory, State & Multi-Agent Patterns**

-   Short-term vs long-term memory; conversation summarization; memory stores
-   Sub-agents, orchestrator patterns, human-in-the-loop checkpoints
-   Failure modes: loops, hallucinated tool calls, runaway costs — and mitigations
-   **Homework:** Agent with persistent memory across sessions

## **Week 12 — Agent Evaluation & Safety**

-   Trajectory evals, task success metrics, LLM-as-judge (and its pitfalls)
-   Guardrails: input/output validation, permission boundaries, sandboxing
-   **Milestone Project 3:** Autonomous agent that completes a real workflow (e.g., research + report generation, data pipeline monitoring, customer support triage) with logged trajectories and an eval report

# **Month 4 — Production Engineering & MLOps for LLMs (Weeks 13–16)**

***Goal:*** *Turn prototypes into systems a company would actually pay to run.*

## **Week 13 — Backend & API Design for AI Products**

-   FastAPI deep-dive: async endpoints, streaming responses (SSE), background jobs
-   Auth basics, rate limiting, request validation
-   **Homework:** Wrap Milestone Project 2 or 3 behind a proper API

## **Week 14 — Observability & LLMOps**

-   Tracing with Langfuse: spans, generations, scores, user feedback loops
-   Logging, cost dashboards, alerting on quality regressions
-   Prompt and config management across environments
-   **Homework:** Instrument your project fully; produce a cost & latency report

## **Week 15 — Deployment & Infrastructure**

-   Docker fundamentals; containerizing an AI service
-   Deployment options: Railway/Render/Fly.io, cloud basics (GCP/AWS), serverless tradeoffs
-   CI/CD with GitHub Actions; environment secrets
-   **Homework:** Fully deployed, publicly accessible AI service with CI

## **Week 16 — Security, Compliance & Responsible AI**

-   Prompt injection, data leakage, jailbreak mitigation
-   PII handling; regional compliance awareness (e.g., PDPA in Singapore, sector rules in healthcare/legal)
-   Model risk documentation for enterprise clients
-   **Deliverable:** Security & compliance checklist applied to your own project

# **Month 5 — Capstone: Client-Grade Build (Weeks 17–20)**

***Goal:*** *One substantial project run like a paid engagement — your portfolio centerpiece and interview talking track.*

## **Week 17 — Discovery & Scoping**

-   Real-world discovery process: stakeholder questions, problem framing, success metrics
-   Writing a mini-PRD with acceptance criteria
-   Build-vs-buy analysis for your chosen solution
-   **Deliverable:** Approved capstone proposal (your instructor plays the role of the client)

## **Weeks 18–19 — Build Sprints**

-   Two structured sprints with standups, code review, and demo checkpoints
-   Instructor and peer code reviews each Saturday; pair-debugging labs on Sunday
-   Mid-capstone eval gate: does the build meet the acceptance criteria so far?

## **Week 20 — Hardening & Handover**

-   Load and edge-case testing, eval suite finalization, documentation (README, architecture diagram, runbook)
-   **Deliverable:** Deployed capstone + demo video (3–5 min) + written case study (problem → approach → results → metrics)

## **Capstone Track Options (pick one)**

1.  Domain RAG product (e.g., legal research assistant, clinic FAQ bot with escalation)
2.  Agentic workflow automation (e.g., report generation, data ops agent)
3.  AI SaaS feature (e.g., GEO/SEO content engine, multilingual support bot)

# **Month 6 — Career Sprint & Placement (Weeks 21–24)**

***Goal:*** *Convert your new skills into offers or paid projects.*

## **Week 21 — Portfolio & Personal Brand**

-   Portfolio site assembly (3 milestone projects + capstone case study)
-   GitHub cleanup: pinned repos, READMEs, contribution signal
-   LinkedIn repositioning for AI engineering (headline, banner, featured section, case-study posts)
-   **Deliverable:** Live portfolio + rewritten LinkedIn + resume tailored to 3 target job descriptions

## **Week 22 — Interview Preparation**

-   The AI engineering interview landscape: system design (design a RAG system, design an agent), coding rounds, take-home projects
-   Mock system design interviews (recorded, with feedback)
-   Talking about your projects with metrics: “reduced hallucination rate from X to Y”, “cut cost per query by Z%”
-   **Deliverable:** Two completed mock interviews with a scored rubric

## **Week 23 — Freelance & Consulting Track**

-   Finding your first paid projects: Upwork/Contra positioning, local SME outreach, community networks
-   Scoping and pricing small AI engagements; the paid-discovery model; simple SOW templates
-   Proposal writing workshop using your capstone as proof
-   **Deliverable:** One real proposal sent to a real prospect OR 10 tailored job applications submitted

## **Week 24 — Demo Day & Launch**

-   Public demo day: you present your capstone to an invited audience from the AI community, including hiring managers and founders
-   Individual career roadmap session (your 90-day post-program plan)
-   Alumni channel onboarding: ongoing job leads, project referrals, monthly check-ins

# **Weekly Rhythm**

| **Day** | **Activity** | **Hours** |
| --- | --- | --- |
| Saturday | Live teaching + live coding + Q&A | 4h |
| Sunday | Guided lab, pair work, office hours | 3h |
| Weekdays | Homework, project work, reading (self-paced) | 8–10h |

**Total commitment: approximately 15–17 hours per week.**

# **Assessment & Progress Gates**

-   **Weekly:** Homework submission via GitHub (pass/redo)
-   **Monthly:** Milestone project demo + rubric score (functionality, code quality, evals, documentation)
-   **Gate at Week 12:** Projects 1–3 must be shipped to enter the capstone phase; a remediation track is available otherwise
-   **Final:** Capstone acceptance against written criteria + demo day presentation

# **Job Guarantee — Eligibility Conditions**

The money-back guarantee applies when you have completed the program in full. To be eligible, you will need to have:

1.  Attended at least 90% of live sessions
2.  Submitted all weekly homework and all 3 milestone projects on time
3.  Completed and deployed the capstone to its written acceptance criteria
4.  Applied to at least 40 relevant jobs and/or sent at least 10 freelance proposals within 90 days after the program, with evidence
5.  Attended all mock interviews and implemented the feedback
6.  Guarantee window: 6 months after program completion; a “project” means any paid engagement at or above a stated minimum value

Full terms are provided in your enrollment agreement, along with a monthly completion checklist we review together.

# **Core Tooling Stack**

-   **Languages & frameworks:** Python, FastAPI, Pydantic, Streamlit/Gradio (prototyping)
-   **LLM APIs:** Anthropic Claude, OpenAI, one open-weight option (Ollama/vLLM awareness)
-   **RAG:** Qdrant, bge-m3 / Voyage embeddings, hybrid search + reranking
-   **Agents:** Claude Agent SDK or LangGraph, MCP, plus a custom from-scratch agent
-   **Evals & observability:** Langfuse, Ragas or a custom harness, LLM-as-judge patterns
-   **Infrastructure:** Docker, GitHub Actions, Railway/Render/Fly.io, cloud basics
-   **Collaboration:** GitHub, Discord/Slack cohort channel, Notion for curriculum

# **Prerequisites & Intake**

-   Basic programming in any language (there is a short 30-minute coding exercise during intake)
-   A laptop capable of running Docker; an API budget of roughly USD 30–50/month
-   A written commitment to the weekly hours — this program works because you show up