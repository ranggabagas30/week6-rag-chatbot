**Week 5 Trainee Guide**

Embeddings & Vector Search

AI Engineer Career Pivot Program · 6-Month Weekend Cohort

# **1\. Learning Objectives**

-   Explain what an embedding is and why semantic search beats keyword search.
-   Use cosine similarity sensibly: rank matters more than absolute score.
-   Choose an embedding model deliberately, including multilingual needs for Southeast Asian products.
-   Build a working semantic search engine with Qdrant: collections, upserts, queries, and metadata filters.

# **2\. Before Saturday**

1.  Prepare 20+ real, ANONYMISED documents from your domain as .txt or .md files in one folder. Anonymise names, IDs, and contacts — same rule as Week 3.
2.  Install ahead: uv pip install "qdrant-client\[fastembed\]" — the first run downloads a small embedding model (~100MB), so do it on good Wi-Fi.
3.  Optional reading: skim the MTEB leaderboard to see how embedding models are compared.

# **3\. Saturday Session — Topic Notes**

## **3.1 Embeddings: Meaning as Coordinates**

An embedding model turns text into a vector — a list of a few hundred numbers — such that texts with similar meaning land near each other in that space. “Invoice overdue 30 days” and “payment is late” share no words, but their vectors are close. That single property is what makes “search by meaning” possible, and it is the foundation of everything RAG does in the coming weeks. Keyword search matches spelling; embedding search matches intent — across synonyms, paraphrases, and (with the right model) across languages.

## **3.2 Similarity**

Closeness is measured with cosine similarity: the angle between two vectors, where 1.0 means identical direction. Two practical rules save you from the classic beginner mistakes. First, scores are relative, not absolute — 0.82 vs 0.79 is a tie, and the useful signal is the ranking. Second, thresholds must be calibrated on your own data: the score below which results become garbage differs per model and per corpus, and finding it is one of tomorrow’s lab exercises.

## **3.3 Choosing a Model**

Three families. Local/open models (bge-m3, the fastembed catalogue) run free on CPU and your data never leaves the machine — the right default for regulated clients. API models (Voyage, OpenAI, Cohere) offer top quality per token with data leaving your infrastructure. For Southeast Asia, test multilingual behaviour explicitly: query in Bahasa or Chinese against English documents and watch whether the model keeps cross-language pairs close — bge-m3 is strong here and it’s a genuine differentiator in our market. The golden rule: documents and queries must be embedded by the SAME model; switching models means re-indexing everything.

## **3.4 Qdrant**

Qdrant is a vector database: it stores vectors with payloads (metadata) and answers nearest-neighbour queries fast, with filtering. This week we run it embedded — QdrantClient(path="./qdrant\_data") — no server, no Docker (that’s Month 4). The convenience API does the embedding for you: .add() accepts raw text and metadata; .query() accepts a raw question. Filters combine semantic search with hard rules — only this user’s documents, only contracts, only 2026 — which is exactly what real products need for access control and scoping.

# **4\. Coding Walkthrough — week5-semantic-search**

## **Step 1 · Scaffold**

$ mkdir week5-semantic-search && cd week5-semantic-search

$ uv venv && source .venv/bin/activate

$ uv pip install "qdrant-client\[fastembed\]"

$ mkdir corpus # copy your 20+ .txt/.md files here

$ printf ".venv/\\n.env\\nqdrant\_data/\\n\_\_pycache\_\_/\\n" > .gitignore

$ git init && git add -A && git commit -m "Scaffold semantic search" # ✔

## **Step 2 · Index the corpus**

\# index.py

from pathlib import Path

from qdrant\_client import QdrantClient

client = QdrantClient(path="./qdrant\_data")

docs, meta, ids = \[\], \[\], \[\]

for n, p in enumerate(sorted(Path("corpus").glob("\*.\*"))):

text = p.read\_text(errors="ignore")

docs.append(text\[:2000\]) # whole-doc for now;

meta.append({"source": p.name, # chunking is Week 6

"type": p.suffix.lstrip(".")})

ids.append(n)

client.add(collection\_name="docs", documents=docs,

metadata=meta, ids=ids)

print(f"indexed {len(docs)} documents")

Run it. First run downloads the embedding model — subsequent runs are instant. ✔ Commit: “Index corpus into embedded Qdrant”.

## **Step 3 · Search CLI**

\# search.py

import sys

from qdrant\_client import QdrantClient

client = QdrantClient(path="./qdrant\_data")

query = " ".join(sys.argv\[1:\])

hits = client.query(collection\_name="docs",

query\_text=query, limit=5)

for h in hits:

print(f"{h.score:.3f} {h.metadata\['source'\]}")

print(" ", h.document\[:100\].replace("\\n", " "), "\\n")

Test the magic: search with a paraphrase that shares no words with the target document and watch it rank first. ✔ Commit.

## **Step 4 · Add a metadata filter**

from qdrant\_client import models

def search(query: str, doc\_type: str | None = None):

flt = None

if doc\_type:

flt = models.Filter(must=\[models.FieldCondition(

key="type",

match=models.MatchValue(value=doc\_type))\])

return client.query(collection\_name="docs",

query\_text=query, query\_filter=flt, limit=5)

Wire a --type flag with argparse. Prove exclusion: a query that normally returns a .md file must not return it when --type txt. ✔ Commit.

## **Step 5 · The 10-query test file**

Create queries.md with 10 queries against your corpus: 5 keyword-style (words that literally appear) and 5 paraphrase-style (same meaning, different words). Run all 10, record which document ranked first and its score. Two things to write in the README: three paraphrase wins, and the score threshold below which results stopped being relevant for your corpus. ✔ Final commit, README, branch, PR, submit with #week5.

# **5\. Sunday Lab — Exercises**

1.  Neighbour intuition: embed 15 sentences from your domain; predict the closest pairs, then check — where was your intuition wrong?
2.  Cross-language probe: query in Bahasa or Chinese against English documents; note what the default model does, and discuss where bge-m3 would change the result.
3.  Filter drill: build a collection with user\_id metadata for two users; prove user A’s searches never surface user B’s documents.
4.  Threshold hunt: for your corpus, find the score where relevance dies — you’ll reuse this number in Week 7’s evals.

# **6\. Homework — Due Friday 23:59**

Full spec in the deck: repo week5-semantic-search, 20+ documents indexed, top-5 CLI search with scores and metadata, at least one filter flag, and the 10-query test file. Acceptance: paraphrase queries demonstrably work (3 examples), filtered search excludes correctly, threshold observation in the README, type hints, 5+ commits. Submit with #week5.

# **7\. Looking Ahead — Week 6**

Next week the search engine becomes a RAG system: we chunk documents properly (the 80% of quality), build a real ingestion pipeline with metadata and stable ids, and generate answers with citations — including the refusal behaviour that keeps the bot honest when the corpus doesn’t contain the answer. Everything you built this week is the foundation; bring it working.