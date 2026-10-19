# Vaibhav Hiwase

AI/ML Engineer & Technical Lead — LLM Applications, Evaluation & Production AI Platforms

Nagpur, India · [(+91) 8999382164](tel:+918999382164) · [hiwase.vaibhav@gmail.com](mailto:hiwase.vaibhav@gmail.com) · [linkedin.com/in/vaibhav-hiwase](https://www.linkedin.com/in/vaibhav-hiwase)

---

## Professional Summary

AI/ML engineer and technical lead with 8+ years building LLM applications and data platforms that run in production. Currently own two production AI systems on Palantir Foundry & AIP: an employee benefits assistant built on Agent Studio, AIP Logic and Foundry Functions, and an automated document-verification workflow on Foundry Automate, along with the AIP Evals suites, guardrails, observability and Marketplace release tooling behind them. Earlier work covers contract-document AI with OpenAI, Claude and Llama models, distributed service architecture on AWS Step Functions and Redis, Databricks pipelines, and Kubernetes deployments on Azure and AWS.

---

## Technical Skills

- **Palantir Foundry & AIP:** Ontology modeling (object types, link types, Action Types), AIP Agents & Agent Studio, AIP Logic, AIP Evals, Workshop, Pipeline Builder, Code Repositories, Functions (Python/TypeScript), Data Connection, Automate, Marketplace, Fusion Sheets, Developer Console, Compass API, multi-environment release management
- **AI, LLM & Gen-AI:** OpenAI, Claude, Llama, VLLM, LangChain, LlamaIndex, RAG, embeddings, vector search (FAISS, Pinecone, Weaviate, Chroma), agentic workflows, Model Context Protocol (MCP), LLM A/B testing, reinforcement learning
- **LLM Application Engineering:** conversational agents, RAG, intent classification and routing, entity extraction, tool/function calling, guardrails, response and citation validation, hallucination mitigation, prompt optimisation, streaming responses, token and cost tracking
- **LLM Evaluation:** LLM-as-a-Judge design and judge–expert alignment, critique shadowing, binary pass/fail rubrics, eval dataset curation, error analysis, regression harnesses, release gating
- **Architecture & Systems:** microservice decomposition, event-driven and asynchronous processing, message brokers and queues (Redis, AWS SQS, RQ), workflow orchestration (AWS Step Functions, Foundry Automate), parallel and chunked processing, autoscaling (KEDA), API gateway and auth (Azure APIM, OAuth 2.0 / OpenID Connect)
- **Computer Vision & Document AI:** Azure Form Recognizer, Azure Custom Vision, Mask R-CNN, layout and table detection, document parsing, image classification, blur and tamper detection
- **Data Engineering:** Spark, PySpark, Polars, Delta Lake, MLflow, Databricks, Unity Catalog, DBFS, incremental pipelines, scalable ETL design, governance and lineage, cluster management
- **Programming:** Python (Advanced), PySpark, Polars, Pandas, NumPy, PyTorch, Scikit-learn, Pydantic, TypeScript, SQL
- **Cloud & MLOps:** Azure (AKS, ML Studio, Key Vault, APIM, Container Apps), AWS (SQS, Step Functions, S3), Kubernetes, Docker, TorchServe, Ollama, GitHub Actions
- **Databases:** MySQL, PostgreSQL, Redis (caching, queues, message broker), vector DBs (FAISS, Pinecone, Chroma, Weaviate)
- **Observability & Monitoring:** Arize Phoenix (LLM & pipeline observability), RQ Dashboard, Opik by Comet
- **Tools:** Git, Docker, Jupyter Notebook, VS Code, Cursor, Antigravity

---

## Experience

### Lead AI/ML Engineer — Palantir Foundry & AIP
**[Innovecture](https://www.innovect.com/)** (Client: [Aptia Group](https://www.aptia-group.com/)) · Remote, India · Dec 2025 – Present

- Built and own Aptia's employee benefits AI assistant on Palantir AIP: an **Agent Studio** agent composed of **16 Python Foundry Functions**, answering questions on plans, coverage, dependents, ID cards and HSA/FSA in plain language. Live across Dev, UAT, Stage, Prod and Internal-Prod.
- Designed the intent-routing layer in **AIP Logic**. Each question is classified into one of ~14 paths and answered directly from the **Ontology** where the data exists; the LLM and RAG over approved benefit resources handle only the remainder, which keeps common answers deterministic and traceable.
- Own the release-quality gate: **15+ AIP Evals suites** covering the intent classifier, entity extractors and response validators across an **800+ question** regression set. Every suite must hold above a **90% pass rate** before a release is promoted.
- Aligned the **LLM-as-a-Judge** scorers to benefits domain experts through critique shadowing, with judges written as versioned **Foundry Functions** and **PySpark** pipelines writing each run back to the Ontology as queryable regression history.
- Shipped safety guardrails as **AIP Logic** functions covering legal, medical, tax and financial advice, running at **p95 under 1.6s across 27k+ calls**, with automatic escalation to a human agent. Added citation and response validators that check each answer against the employee's own plan data before delivery.
- Built self-service evaluation apps in **Foundry Workshop** so the benefits team authors test questions and reviews AI scores without engineering. Test cases are seeded from **Fusion Sheets** and materialised as Ontology objects through **Pipeline Builder**.
- Consolidated logs from **21 Foundry Functions** into a single hourly-refreshed timeline of **9M+ events** with per-function error and token-cost breakdowns, then used it to find one fallback agent absorbing **75% of AI spend** and re-route common questions away from it, cutting the cost of a typical question by roughly **95%**.
- Automated dependent-eligibility document verification on **Foundry Automate** and **AIP Logic**: 16 reusable checks across 20 document types, with results returned to the core benefits platform over **AWS SQS**. **~37,000 decisions** processed at roughly a minute each.
- Built an environment comparison tool on the **Compass API** that inventories and diffs all five Foundry environments across 36 resource types, flagging configuration drift, missing resources, failed dataset builds and unindexed object types in a shareable HTML report. Covered by 158 unit tests.
- Modelled the **Ontology** behind both workflows (object types, link types, Action Types) and migrated **~80 Action Types** to a new ontology without breaking downstream consumers.
- Packaged the pipelines and Functions as a **Foundry Marketplace** product that resolves its own resource IDs at install time through the **Compass API**, so it installs into any environment unchanged.
- Rebuilt Salesforce, Pendo, Postgres and S3 ingests as incremental runs on **Polars**, so each build reads only what changed.
- Run releases as **Platform Admin and Platform Approver**, promoting code, ontology and app branches Dev → UAT → Stage → Prod through reviewed proposals, and handle L3 production support.

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

**Employee Benefits AI Platform on Palantir Foundry — Aptia Group**
- **Evaluation platform** — continuous scoring for the intent classifier, 4 entity extractors and 4 response validators. Test cases are modelled as Ontology objects linked to the participant, plan and source resource page each answer must be grounded in; judges are versioned Foundry Functions; every run is kept as a queryable dataset so releases can be compared against one another.
- **Ontology Comparison Tool** — inventories all five Foundry environments through the **Compass API** and diffs them ahead of a release, flagging missing resources, configuration drift, failed dataset builds and unindexed object types. 36 resource types parsed, interactive HTML report with a visual map of resource relationships, 158 unit tests.
- **AI monitoring and cost reporting** — one timeline across 21 agent Functions showing error types, latency and token cost by model, user and day.

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
