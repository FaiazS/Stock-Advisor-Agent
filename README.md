# 📈 Stock Advisor Agent 🚀

> AI-powered stock research assistant using multi-agent collaboration, real-time web scraping, and push notification alerts — built with [CrewAI](https://github.com/joaomdmoura/crewAI), [Serper](https://serper.dev/), and [Pushover](https://pushover.net/).

![CrewAI Powered](https://img.shields.io/badge/Built%20with-CrewAI-blueviolet?style=flat&logo=python)
![Push Notifications](https://img.shields.io/badge/Push-Pushover-blue?style=flat)
![Python](https://img.shields.io/badge/Made%20with-Python-FFD43B?style=flat&logo=python)

---

## 🌟 Overview

**Stock Advisor Agent** is an intelligent multi-agent system that analyzes trending startups and publicly listed companies in the tech sector, performs deep fundamental analysis, and sends real-time stock recommendations to your phone via push notification.

A fully autonomous, production-ready AI workflow combining research, analysis, and delivery in one smart pipeline.

---

## 🧠 What It Does

- 🔍 **Agent 1:** Finds trending tech companies from recent headlines.
  
- 🧾 **Agent 2:** Scrapes and filters out unknown or low-impact companies.
  
- 📊 **Agent 3:** Performs in-depth fundamental analysis.
  
- 📝 **Agent 4:** Summarizes investment insights.
  
- 📲 **Agent 5:** Sends push notifications directly to your phone

All coordinated via **CrewAI** — your own autonomous task force of expert AI agents.

---
📲 Real-Time Example

You'll receive a mobile push notification like:

    💸 Invest in AccioJob for its strong growth in the ed-tech sector and in BellyRubs due to its strong market presence and the rising demand for pet supplies.
---

# Project Highlights

✅ Multi-Agent Orchestration with CrewAI.

✅ Real-time web search using Serper.

✅ Push notification delivery with Pushover.

✅ Custom tools and memory management.

✅ Production-ready modular structure.

---

## 🧠 System flow

```mermaid
flowchart TD
    A[User runs crewai run] --> B[Agent 1: News Researcher]
    B -->|Searches latest tech trends| C[Serper API]

    C --> D[Agent 2: Filter Analyst]
    D -->|Filters unknown/non-trending companies| E[Company Shortlist]

    E --> F[Agent 3: Financial Researcher]
    F -->|Performs deep analysis| G[Online Financial Data Sources]

    G --> H[Agent 4: Equity Manager]
    H -->|Summarizes report| I[Final Recommendation]

    I --> J[Agent 5: Notification Agent]
    J -->|Sends to phone| K[Pushover Notification]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style K fill:#bbf,stroke:#333,stroke-width:2px

