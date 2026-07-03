"""
Day 1, Stage 1: Download latest 10-K filings from SEC EDGAR
Run:  python src/ingest.py
Idempotent: re-running skips already-downloaded filings.
"""
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from edgar import set_identity, Company

# ---------- setup ----------
load_dotenv()
set_identity(os.environ["EDGAR_IDENTITY"])

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

TICKERS = [
    # Energy & Resources
    "XOM", "CVX", "COP", "SLB", "NEE", "DUK",
    # Financial Services
    "JPM", "GS", "BAC", "MS", "AXP", "BLK",
]

# ---------- ingestion ----------
manifest = []   # one metadata record per filing

for ticker in TICKERS:
    out_dir = RAW_DIR / ticker
    meta_path = out_dir / "metadata.json"

    # CACHE CHECK: skip if already downloaded (be polite to SEC servers)
    if meta_path.exists():
        print(f"[skip] {ticker} already downloaded")
        manifest.append(json.loads(meta_path.read_text()))
        continue

    try:
        company = Company(ticker)
        filing = company.get_filings(form="10-K").latest(1)  # newest 10-K

        out_dir.mkdir(exist_ok=True)

        # Save the raw filing HTML (our permanent local copy)
        html = filing.html()
        (out_dir / "filing.html").write_text(html, encoding="utf-8")

        # Save metadata we'll attach to every chunk later
        meta = {
            "ticker": ticker,
            "company": company.name,
            "cik": str(company.cik),
            "form": "10-K",
            "filing_date": str(filing.filing_date),
            "accession_no": filing.accession_no,
        }
        meta_path.write_text(json.dumps(meta, indent=2))
        manifest.append(meta)
        print(f"[ok]   {ticker}: {company.name} ({filing.filing_date})")

    except Exception as e:
        # Log and continue — we fix or substitute failures at the end
        print(f"[FAIL] {ticker}: {e}")

# ---------- summary ----------
(Path("data") / "manifest.json").write_text(json.dumps(manifest, indent=2))
print(f"\nDownloaded {len(manifest)}/{len(TICKERS)} filings.")
print("Manifest written to data/manifest.json")