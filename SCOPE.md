# Scope Contract — Audit Copilot v1 (locked 2026-07-03)

## In scope
- 12 companies (list below), most recent 10-K only
- 4 question types: risk factors, revenue recognition, debt/covenants, comparative
- Cited answers (filing + item + passage)
- Hybrid retrieval (vector + BM25), reranking if it fits the timebox
- Eval set (30–50 Qs) + RAGAS metrics in README
- Streamlit UI on Hugging Face Spaces

## Out of scope (v1) — goes to FUTURE_WORK.md
- Multi-turn chat memory
- Fine-tuning
- Table/XBRL numerical analytics
- Multi-year filing comparisons
- Real-time filing alerts

## Companies
Energy & Resources: XOM, CVX, COP, SLB, NEE, DUK
Financial Services: JPM, GS, BAC, MS, AXP, BLK