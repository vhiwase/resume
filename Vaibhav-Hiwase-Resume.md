# Vaibhav Hiwase

AI/ML Engineer & Technical Lead — LLM Applications, Evaluation & Production AI Platforms

Nagpur, India · [(+91) 8999382164](tel:+918999382164) · [hiwase.vaibhav@gmail.com](mailto:hiwase.vaibhav@gmail.com) · [linkedin.com/in/vaibhav-hiwase](https://www.linkedin.com/in/vaibhav-hiwase)

---

## Professional Summary

AI/ML engineer and technical lead with 8+ years building LLM applications and data platforms that run in production. Currently own two production AI systems on Palantir Foundry & AIP: an employee benefits assistant built on Agent Studio, AIP Logic and Foundry Functions, and an automated document-verification workflow on Foundry Automate, along with the AIP Evals suites, guardrails, observability and Marketplace release tooling behind them. Earlier work covers contract-document AI with OpenAI, Claude and Llama models, distributed service architecture on AWS Step Functions and Redis, Databricks pipelines, and Kubernetes deployments on Azure and AWS.

---

## Technical Skills

- **Palantir AIP:** AIP Agent Studio, AIP Logic, AIP Evals, Automate, Foundry ML (models, inference), AI FDE (AI-assisted development)
- **Foundry Ontology & Apps:** Ontology modeling (object, link and action types, interfaces, function-backed actions), Functions (Python/TypeScript), OSDK & Developer Console, Compass API, Workshop, Slate, Contour, Fusion Sheets
- **Foundry Data & DevOps:** Pipeline Builder, Code Repositories & Workspaces (Python transforms), Data Connection (streaming, CDC), Media Sets, Restricted Views & Markings, Global Branching, Marketplace & DevOps, multi-environment releases
- **AI, LLM & Gen-AI:** OpenAI, Claude, Gemini, Llama, VLLM, LangChain, LlamaIndex, RAG, embeddings, vector search (FAISS, Pinecone, Weaviate, Chroma), agentic workflows, Model Context Protocol (MCP), LLM A/B testing, reinforcement learning
- **LLM Application Engineering:** conversational agents, RAG, intent classification and routing, entity extraction, tool/function calling, guardrails, response and citation validation, hallucination mitigation, prompt optimisation, streaming responses, token and cost tracking
- **LLM Evaluation:** LLM-as-a-Judge design and judge–expert alignment, critique shadowing, binary pass/fail rubrics, eval dataset curation, error analysis, regression harnesses, release gating
- **Architecture & Systems:** microservice decomposition, event-driven and asynchronous processing, message brokers and queues (Redis, AWS SQS, RQ), workflow orchestration (AWS Step Functions, Foundry Automate), parallel and chunked processing, autoscaling (KEDA), API gateway and auth (Azure APIM, OAuth 2.0 / OpenID Connect)
- **Computer Vision & Document AI:** Azure Form Recognizer, Azure Custom Vision, Mask R-CNN, layout and table detection, document parsing, image classification, blur and tamper detection
- **Data Engineering:** Spark, PySpark, Polars, DuckDB, Delta Lake, MLflow, Databricks, Unity Catalog, DBFS, incremental pipelines, schema evolution, scalable ETL design, governance and lineage, cluster management
- **Programming:** Python (Advanced), PySpark, Polars, Pandas, NumPy, PyTorch, Scikit-learn, Pydantic, TypeScript, SQL
- **Cloud & MLOps:** Azure (AKS, ML Studio, Key Vault, APIM, Container Apps), AWS (SQS, Step Functions, S3), Kubernetes, Docker, TorchServe, Ollama, GitHub Actions
- **Databases:** MySQL, PostgreSQL, Redis (caching, queues, message broker), vector DBs (FAISS, Pinecone, Chroma, Weaviate)
- **Observability & Monitoring:** Arize Phoenix (LLM & pipeline observability), RQ Dashboard, Opik by Comet
- **Tools:** Git, Docker, Jupyter Notebook, VS Code, Cursor, Antigravity

---

## Experience

### Lead AI/ML Engineer — Palantir Foundry & AIP
**[Innovecture](https://www.innovect.com/)** (Client: [Aptia Group](https://www.aptia-group.com/)) · Remote, India · Dec 2025 – Present

Build a GenAI benefits assistant, its LLM evaluation framework and automated document-verification workflows, and serve as Platform Admin with L3 production support across 5 environments (126 of 140 change proposals merged).

**GenAI Benefits Assistant**
- Raised the coverage answer engine's evaluation pass rate from **68.9% to 97.9%** (238 cases) by replacing about 30 rigid lookup tables with a principle-based prompt on Gemini Flash, which also cut prompt tokens 28% and worst-case latency 48%.
- Achieved a **99.4% pass rate** (167 of 168 AIP Evals runs) on a 26-intent LLM classifier by rebuilding its routing around priority rules for unsupported languages, plan mentions, follow-ups, multi-plan questions and past or future coverage.
- Made answers traceable and reduced hallucination by returning cited source IDs in structured responses, adding grounding rules and an 11-point self-check, and removing duplicate retrieved pages from the prompt (10 copies to 1).

**LLM Evaluation & Quality**
- Designed an evaluation framework grounded in real plan documents, with a 64-cell test matrix and an LLM judge required to agree with experts at least 90% of the time, and shipped a **532-case regression suite** (388 cases written by business users).
- Built an embedding-based RAG retrieval pipeline matching 202 test queries to participants and pages, cutting comparisons **99.9%** (33M to 36K) by de-duplicating 165,750 page rows to 180 unique pages.
- Identified **85 content gaps** across 182 business acceptance-test queries by building a keyword matcher that behaves identically in every environment, and removed a matching tier that caused 60 false matches.
- Shipped evaluation-run analytics with new Eval Run and Test Case object types that track pass rate, tokens, compute and latency per run, and added a Helpfulness criterion to the LLM judge with no regressions.

**Document Verification Automation**
- Prevented verification requests from stalling on pending participant data by building a readiness gate (status field, AIP Logic lookup and 15-minute re-check automation) across **22 automations**, with a 24-hour fallback to manual review.
- Replaced silent failures with a clear result, reason and audit marker for unsupported document types and AI-excluded clients, added end-to-end structured failure reasons and pinned function versions across all actions.
- Enabled testing of **24 of 36** previously untested file-type and entity-type combinations by adding a Clone Verification Request action that re-tests documents without re-uploading, exposing a whitespace bug in entity-type parsing.
- Built an end-to-end load-testing suite that triggers real actions through the Foundry Ontology API and verifies delivery to AWS SQS, measuring throughput, **p50–p99 latency**, error rate and pipeline time from 1× to 250× synthetic load.

**Data Engineering & Pipelines**
- Rebuilt a failing Postgres sync as an incremental Spark join in Pipeline Builder, verified row for row on **8M+ rows**.
- Resolved recurring Pendo ingestion failures, with builds now finishing in **14.5 minutes** and no memory errors, by adding schema evolution with typed nulls, processing one day at a time and removing about 300 lines of duplicate code.
- Corrected a **nearly 3×** overcount of dependent-coverage objects and removed 1,170 duplicate-key rows by sourcing the model from Foundry-computed data, preserving row-level security through a restricted view with no orphaned links.
- Stabilized the assistant's monitoring: fixed a streaming backfill bug, rebuilt enrichment, error and token-usage transforms on a shared timeline, and grew log-parser coverage from 16 to 21, storing user text only as SHA-256 fingerprints.

**Platform Engineering & DevOps**
- Built a deployment validator, covered by **158 unit tests**, that compares Foundry resources across 5 environments and 36 resource types and shows likely matches, field-level differences and duplicates in an interactive HTML dashboard.
- Made Marketplace products deployable to every environment by replacing hard-coded resource IDs with Compass paths, fixing packaging errors and removing a column dependency that broke Stage builds, verified on **22.7M rows**.
- Implemented platform-health and sync-failure monitoring for builds, search indexing and schema failures, with a Python reporting function that sends automated email alerts on separate production and non-production schedules.
- Restored the development ontology by recreating **70+ of 107** action types, including full create, edit and delete sets.
- Flagged two data-exposure risks and designed evaluation pipelines to store fingerprints instead of document content.

### Technical Lead — ML & AI
**[TechnoMile](https://technomile.com/)** · Remote, India · Sept 2023 – Nov 2025

- Built the AI extraction engine behind TechnoMile's **Contract Lifecycle Management** and **Pre-Award** products, pulling clauses, CLINs and sections out of long federal contract PDFs with **OpenAI, Claude and Llama** models. Raised CLIN accuracy from **58% to 90%** across 7 contract domains.
- Shipped contract question-answering with **RAG**, chunking and embedding documents into a **FAISS/Chroma** vector store so answers are grounded in retrieved text rather than model memory.
- Re-architected a monolithic extraction service into four independent CLIN, Clause, Section and Form services orchestrated with **AWS Step Functions**, cutting processing time **40%** through parallel chunk handling and asynchronous PDF-to-image conversion.
- Built the review tooling for QA: a field-by-field accuracy report against ground truth (**Python, Plotly, DataTables**) and a viewer that boxes the exact PDF location each extracted value came from, so reviewers could catch fields the model invented.
- Ran models in production with **MLflow** for experiment tracking and versioning and **Arize Phoenix** to trace prompts, token usage and latency.
- Built Pre-Award Copilot features extracting clauses, deliverables and risk indicators from government solicitations, plus **Model Context Protocol (MCP)** agents that answer questions from internal APIs and databases in plain language.

### Senior Consultant
**[Celebal Technologies](https://celebaltech.com/)** · Remote, India · Sept 2021 – Aug 2023

Data science and ML engineering for enterprise clients: document intelligence, production ML infrastructure, and a forecasting platform built with Microsoft.

- Led development of a payslip forgery detection method reaching **85.23% accuracy**, using **Azure Form Recognizer** for extraction.
- Trained payslip classification and blur detection models on **Azure Custom Vision**, reaching **90.87%** and **95.72%** accuracy.
- Built key information extraction and document similarity capabilities across client engagements, and a Hinglish language model for a client use case.
- Architected a secure, high-throughput serving platform on **Redis, Kubernetes/AKS, Docker, Azure API Management, Key Vault and OAuth 2.0**, cutting processing time **10x**.
- Moved long-running document work onto background workers behind a **Redis** queue, with **KEDA** autoscaling on Azure Kubernetes Service and containerised deployment via **Docker**.
- Partnered with **Microsoft** to build a forecasting platform for energy portfolio management, adding training-loss monitoring across **DeepMC, TFT, N-BEATS and TCN** models with pipelines running on **Azure ML Studio** and **Azure Functions**.
- Fine-tuned sentence-embedding models on retail catalog data to improve ad and product recommendations from search queries.
- Mentored the team across document intelligence and language modelling, and supervised a computer-vision project counting exercise repetitions from mobile and IoT camera video.

### Machine Learning Engineer
**[Konverge.AI](https://konverge.ai/)** · India · Aug 2018 – Aug 2021

- Led a team of **10** on solution architecture and work breakdown for Smart Content Extraction.
- Built data ingestion APIs with **Airbyte** connectors for the WEAV Core libraries.
- Built a clustering-based method for extracting paragraphs and tables from documents.
- Trained a **Mask R-CNN** model to classify fungus, yeast and bacteria at pixel level on stained nail-tissue images.
- Built the backend for media analytics: keyword identification, clustering and recommendations.
- Built a **GIS** system that maps geographic locations found in scanned government documents.

---

## Projects

**Contract Document AI — TechnoMile**
- Trained a layout detection model on **Azure Custom Vision** to find CLIN tables in contract PDFs: **94%** accuracy on 50 annotated documents, rising above **98%** after scaling the training set to 264 with automated retraining.
- Built a reusable ML pipeline library with separate training, inference and deployment components, deployable on **TorchServe, Ollama or VLLM**.
- Wrote a verification tool that matches each extracted value back to its place in the document and scores confidence, so unsupported fields get caught.
- Cut CLIN processing from **370s to 220s** with chunk-level parallelism, keeping memory flat by converting PDF pages to images one at a time.

**Large Language Model Training**
- Fine-tuned a Spanish sentence-embedding model (**Sentence Transformers**) on Walmart Mexico catalog data to improve ad recommendations from search queries.
- Used **FLAN-T5 Large** to generate search keywords from product text, improving those recommendations further.
- Used **FAISS** to make search lookups faster and lighter on memory.
- Ran the work on **Databricks** and validated results against add-to-cart data.

**Payslip Forgery Detection — Celebal Technologies**
- Led the work end to end for a payroll client: research, architecture, engineering and monitoring.
- Layered metadata and pixel-level checks on top of the forgery detector to catch manipulated documents that passed content extraction.
- Built the **Flask** and **React** application, secured with **OAuth 2.0** and **OpenID Connect** behind **Azure API Management**, shipped through **GitHub Actions** to **Azure Container Apps**, with an **RQ dashboard** for queue visibility.

---

## Education

**Master of Technology, Computer Science and Engineering** — [RCOEM](https://www.rknec.edu/), Nagpur, India · Aug 2016 – Aug 2018

**Bachelor of Engineering, Information Technology** — [SVPCET](https://www.stvincentngp.edu.in/), Nagpur, India · Aug 2012 – Aug 2016

---

## Certifications

[STATSX0001: Statistical Learning, StanfordOnline](https://courses.edx.org/certificates/b51d9b57b98e40238921a7430ad46f73) · OAuth 2.0 · Docker · [Data Science](https://www.udemy.com/certificate/UC-FCRNNE54/)

## Achievements & Activities

[Microsoft AI/ML competition (2022)](https://www.credly.com/badges/02d6cb29-e29e-44cc-8823-3533df0c423f?source=linked_in_profile) · [Artificial Intelligence and Machine Learning Workathon (2021)](https://www.credly.com/badges/74f831f7-aa06-4aa5-8a63-40e27ff0048c?source=linked_in_profile) · [Organized and led CSI events (2013–2016)](https://csiindia.org/) · [National Cadet Corps (NCC) cadet with 'A' certificate (2008–2009)](https://indiancc.mygov.in/)
