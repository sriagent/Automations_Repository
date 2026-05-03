# Technical Strategy: AI/Tech Startup Scraper (2025-2026)
**Role:** CTO Directive
**Project:** Startup Scraper
**Target:** 50 High-Potential Startups (2025-2026)

## 1. Data Acquisition Strategy
To ensure high-signal discovery, the scraper must aggregate data from three tiers of sources:

### Tier 1: High-Signal Incubators & Accelerators
*   **Y Combinator (YC):** Target "Company" directory, filtering for W25 and S25 batches.
*   **Techstars / Antler:** Focus on recent cohort announcements.

### Tier 2: Launch Platforms & Trends
*   **Product Hunt:** Scrape 'Products of the Day/Week' with tags: `AI`, `LLM`, `Automation`, `Agentic`.
*   **AIChatbot / Futurepedia:** Directories specializing in new AI tools.

### Tier 3: Financial & Market Intelligence
*   **Crunchbase:** Monitor "Recent Funding" for Seed/Series A in AI sectors.
*   **LinkedIn/X:** Search for keywords "Stealth mode", "Founding engineer", "AI agent" within specific timeframe.

## 2. Data Structure (The Startup Summary)
All extracted data must be normalized into the following JSON/Markdown structure for maintenance and analysis:

```json
{
  "startup_id": "string (slug)",
  "name": "string",
  "website": "url",
  "industry": "category",
  "funding_stage": "seed|series_a|bootstrapped",
  "core_product": "concise description of the tool",
  "usp": "Unique Selling Proposition (The 'Why now' and 'Why them')",
  "uniqueness_score": "1-10 (based on verification criteria)",
  "competitors": ["competitor_a", "competitor_b"],
  "competitive_edge": "What makes them better than competitors?",
  "source": "yc|producthunt|crunchbase",
  "discovery_date": "ISO-8601",
  "verification_status": "pending|verified|rejected"
}
```

## 3. Verification Criteria
To prevent "GPT-wrapper" noise, every startup must pass the following filters:

### A. Uniqueness Criteria (The 'Moat' Test)
A startup is considered 'Unique' if it meets at least one of the following:
*   **Proprietary Data:** Has a unique dataset for training/fine-tuning.
*   **Architecture Innovation:** Implements a new way of agentic orchestration (not just a prompt wrapper).
*   **Vertical Depth:** Solves a deeply specific industry pain point where generic LLMs fail.
*   **User Experience Breakthrough:** Simplifies a complex AI workflow in a way that creates high switching costs.

### B. USP (Unique Selling Proposition) Verification
The USP must answer the "10x Rule":
*   Does it provide a 10x improvement in speed, cost, or quality over the existing status quo?
*   If the USP is "AI-powered [X]", it is rejected unless [X] is a previously unsolved problem.

## 4. Directives to the Orchestrator
The Orchestrator must execute the following workflow:

1.  **Phase 1 (Discovery):** Implement a multi-source scraper (Tier 1 $\rightarrow$ Tier 2 $\rightarrow$ Tier 3). Collect 150+ candidates to ensure a filtered pool of 50.
2.  **Phase 2 (Analysis):** Use an LLM-based analyzer to fill the `core_product` and `usp` fields. 
3.  **Phase 3 (Audit):** Cross-reference the `usp` against known competitors. If the product is identical to a top-3 competitor, mark as `rejected`.
4.  **Phase 4 (Finalization):** Deliver the final 50 startups in a structured `startups_summary.json` and a readable `README.md` in the `/root/Automations_Repository` directory.
5.  **Persistence:** Ensure the scraper is modular so a new run can be triggered for the 2026 cycle without rewriting logic.
