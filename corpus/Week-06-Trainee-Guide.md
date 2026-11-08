**Week 6 Trainee Guide**

RAG Architecture End-to-End

AI Engineer Career Pivot Program · 6-Month Weekend Cohort

# **1\. Learning Objectives**

-   Explain the two halves of RAG: offline ingestion (parse → chunk → embed → store) and online answering (retrieve → assemble → generate).
-   Chunk documents deliberately and explain why chunking dominates RAG quality.
-   Design metadata and stable ids so citations and safe re-ingestion work.
-   Generate answers that cite numbered sources and refuse when the evidence isn’t there.

# **2\. Before Saturday**

1.  Bring your Week 5 repo working — tonight builds directly on it.
2.  Add 5–10 longer documents to your corpus (multi-page if possible); chunking only gets interesting when documents are big.
3.  Confirm your Anthropic key has credit — generation returns this week.

# **3\. Saturday Session — Topic Notes**

## **3.1 Why RAG**

Pasting all documents into the prompt fails three ways: context windows are finite, cost and latency scale with tokens (your Week 2 math), and answers drown in irrelevant text. RAG inverts it: search first, then let the model write only from the search results. The result is cheaper, faster, and — because every claim traces to a retrieved chunk — auditable.

## **3.2 Chunking Is 80% of Quality**

Retrieval returns chunks, so chunks are what the model sees. Too small and the idea is amputated from its context; too big and the top-k slots fill with noise. The heuristic: a chunk should answer one question well — typically 200–400 tokens for prose. Strategies in order of sophistication: fixed-size with overlap (predictable, cuts mid-thought), structural/recursive (split on headings then paragraphs then sentences — the best default because it respects how the author organised meaning), and semantic (split where meaning shifts — powerful, costly, Week 7). Overlap of ~50 tokens carries context across cut points. We build a structural chunker by hand tonight — not because libraries don’t exist, but because you will one day debug one, and you can’t debug what you’ve never built.

## **3.3 Ingestion and Metadata**

Ingestion is a pipeline you’ll re-run constantly, so two design decisions matter from day one. Metadata: store source filename, chunk index, and title with every point — citations become possible only because this exists, and anything you’ll ever filter on must be stored now. Stable ids: derive each point’s id deterministically from (path, chunk index) so re-running ingestion updates points instead of duplicating them — the classic RAG bug is a corpus indexed three times with three copies of everything.

## **3.4 Cited Generation and the Refusal Rule**

Retrieved chunks are numbered \[1\]..\[5\] and pasted into the prompt with their sources. The system prompt enforces three rules: answer ONLY from the numbered sources, cite \[n\] after each claim, and if the sources don’t contain the answer, say a fixed refusal sentence. The refusal is the feature clients care about most — it is the difference between a grounded assistant and a confident liar. Keep temperature at 0–0.3 for factual QA, and log which chunks each answer used: when an answer is wrong, the first question is always “what did retrieval return?”.

# **4\. Coding Walkthrough — week6-rag-chatbot**

## **Step 1 · Scaffold on Week 5**

$ mkdir week6-rag-chatbot && cd week6-rag-chatbot

$ uv venv && source .venv/bin/activate

$ uv pip install "qdrant-client\[fastembed\]" anthropic python-dotenv

$ mkdir corpus # copy your (now larger) corpus in

\# copy config.py + .gitignore pattern; add qdrant\_data/ to it

$ git init && git add -A && git commit -m "Scaffold RAG chatbot" # ✔

## **Step 2 · The chunker**

\# chunker.py — structural, ~350 tokens, 50 overlap

def tok\_len(s: str) -> int:

return max(1, len(s) // 4) # good-enough estimate

def chunk(text: str, max\_tokens: int = 350,

overlap: int = 50) -> list\[str\]:

paras = \[p.strip() for p in text.split("\\n\\n") if p.strip()\]

chunks: list\[str\] = \[\]

buf = ""

for p in paras:

if buf and tok\_len(buf) + tok\_len(p) > max\_tokens:

chunks.append(buf.strip())

buf = buf\[-overlap \* 4:\] # tail as overlap

buf += "\\n\\n" + p

if buf.strip():

chunks.append(buf.strip())

return chunks

Unit-test it on your longest document: print chunk count and the first line of each. Sanity: no chunk should be tiny (<50 tokens) or huge (>500). ✔ Commit.

## **Step 3 · Ingestion with stable ids**

\# ingest.py

import hashlib

from pathlib import Path

from qdrant\_client import QdrantClient

from chunker import chunk

def stable\_id(path: str, i: int) -> int:

h = hashlib.md5(f"{path}:{i}".encode()).hexdigest()

return int(h\[:12\], 16)

client = QdrantClient(path="./qdrant\_data")

docs, meta, ids = \[\], \[\], \[\]

for p in sorted(Path("corpus").glob("\*.\*")):

text = p.read\_text(errors="ignore")

for i, ch in enumerate(chunk(text)):

docs.append(ch)

meta.append({"source": p.name, "chunk": i})

ids.append(stable\_id(p.name, i))

client.add("kb", documents=docs, metadata=meta, ids=ids)

print(f"ingested {len(docs)} chunks")

Prove idempotence: run ingest twice, then check the collection count didn’t double (client.count("kb")). Screenshot or paste that into the README — it’s an acceptance criterion. ✔ Commit.

## **Step 4 · Retrieval + cited answer**

\# rag.py

SYSTEM = (

"Answer ONLY from the numbered sources provided. "

"Cite like \[1\] or \[2\]\[3\] after each claim. "

"If the sources do not contain the answer, reply exactly: "

"'I don't have that in the knowledge base.' "

"Never use outside knowledge.")

def answer(q: str) -> tuple\[str, list\]:

hits = client.query("kb", query\_text=q, limit=5)

context = "\\n\\n".join(

f"\[{i+1}\] ({h.metadata\['source'\]} #{h.metadata\['chunk'\]})"

f"\\n{h.document}" for i, h in enumerate(hits))

reply = call\_llm(system=SYSTEM, max\_tokens=700,

user=f"Sources:\\n{context}\\n\\nQuestion: {q}")

return reply, hits

Test with a question you KNOW is in the corpus — verify the \[n\] citations point at the right chunks by reading them. ✔ Commit.

## **Step 5 · Chat loop + /sources**

last\_hits = \[\]

while True:

q = input("you> ").strip()

if q == "/quit": break

if q == "/sources":

for i, h in enumerate(last\_hits):

print(f"\[{i+1}\] {h.metadata\['source'\]} "

f"#{h.metadata\['chunk'\]} score={h.score:.3f}")

print(" ", h.document\[:120\], "\\n")

continue

reply, last\_hits = answer(q)

print("bot>", reply)

✔ Commit. Then run the two decisive tests: (1) five real questions — record Q, A, and verified citations in the README; (2) two questions your corpus can’t answer — the bot must produce the exact refusal sentence, recorded too.

## **Step 6 · Ship**

README (pipeline diagram in ASCII or an image, the 5 cited Q&As, the 2 refusals, the idempotence proof), branch, PR, submit with #week6. This repo grows into Milestone Project 2 over the next two weeks — keep it clean.

# **5\. Sunday Lab — Exercises**

1.  Chunk-size shootout: re-index at 150 / 350 / 700 tokens; ask the same 5 questions; write down which size won and why.
2.  Citation audit (pairs): verify every claim in your partner’s answers against the cited chunks — report any claim without support.
3.  Refusal test: three out-of-corpus questions; any improvised answer is a fail — fix the system prompt until it isn’t.
4.  Filter + citation combo: answer a question restricted to one document type, with citations still correct.

# **6\. Homework — Due Friday 23:59**

Full spec in the deck: repo week6-rag-chatbot with chunker, idempotent ingestion, cited chat loop, refusal behaviour, and /sources. Acceptance: 5 verified cited Q&As, 2 documented refusals, idempotence proof, type hints, 6+ commits. Submit with #week6.

# **7\. Looking Ahead — Week 7**

Advanced retrieval and — the bigger deal — RAG evaluation. Your Week 3 golden-set habit becomes a real eval harness: retrieval precision, answer faithfulness, and the numbers that let you prove one configuration beats another. Hybrid search and reranking then give you the levers to move those numbers. From Week 7 on, “it feels better” is no longer an argument — you’ll have data.