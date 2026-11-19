# Vaibhav Hiwase

Lead Palantir Foundry & AIP Engineer — Ontology, Pipelines, AIP Agents, RAG/OAG

Nagpur, India · Open to relocation to Abu Dhabi, UAE · [(+91) 8999382164](tel:+918999382164) · [hiwase.vaibhav@gmail.com](mailto:hiwase.vaibhav@gmail.com) · [linkedin.com/in/vaibhav-hiwase](https://www.linkedin.com/in/vaibhav-hiwase)

---

## Professional Summary

Palantir Foundry & AIP engineer with 8+ years in data and AI engineering. As Lead AI/ML Engineer and Platform Admin at Aptia Group, own two production AIP solutions end to end: an employee benefits copilot on AIP Agent Studio and AIP Logic, grounded with RAG and Ontology-Augmented Generation (OAG), and a document-verification decision workflow on Automate, plus the AIP Evals suites and pipelines behind them. Strong in Python, PySpark, SQL and data modelling, and work directly with non-technical business users. Before Foundry: 7 years of LLM, RAG, document AI and data pipelines on AWS, Azure and Databricks.

---

## Technical Skills

- **Palantir AIP:** RAG and Ontology-Augmented Generation (OAG), AIP Agent Studio (copilots), AIP Logic (intent routing, decision support), AIP Evals, Automate (workflow automation), Foundry ML (models, inference), AI FDE
- **Foundry Ontology & Apps:** Ontology design and data modelling (object, link and action types, interfaces, function-backed actions), Functions (Python/TypeScript), Workshop, Slate, Contour, Fusion Sheets, OSDK, Developer Console, Compass API
- **Foundry Data & DevOps:** Pipeline Builder, Code Repositories & Workspaces (Python/PySpark transforms), Data Connection (batch, streaming, CDC), Media Sets, Restricted Views & Markings, Global Branching, Marketplace, multi-environment releases
- **Data Engineering:** Python (advanced), PySpark, SQL, Spark, Polars, DuckDB, Pandas, Delta Lake, Databricks, Unity Catalog, incremental ETL and transformations, schema evolution, data quality and reconciliation, lineage and governance
- **GenAI & LLM:** OpenAI, Claude, Gemini, Llama, vLLM, LangChain, LlamaIndex, embeddings, vector search (FAISS, Pinecone, Weaviate, Chroma), agentic workflows, MCP, tool calling, guardrails, hallucination mitigation, prompt optimisation, cost tracking
- **LLM Evaluation:** LLM-as-a-judge, judge–expert alignment, critique shadowing, eval datasets, regression testing, release gates
- **Cloud, MLOps & Databases:** AWS (SQS, Step Functions, S3), Azure (AKS, ML Studio, Functions, Key Vault, APIM), Kubernetes, Docker, KEDA, Redis, PostgreSQL, MySQL, MLflow, Arize Phoenix, Git, GitHub Actions, OAuth 2.0 / OpenID Connect
- **ML & Document AI:** PyTorch, Scikit-learn, Sentence Transformers, Azure Form Recognizer, Azure Custom Vision, Mask R-CNN
- **Domains:** employee benefits, payroll and KYC document verification, federal government contracting, insurance risk (research)

---

## Experience

### Lead AI/ML Engineer — Palantir Foundry & AIP
**[Innovecture](https://www.innovect.com/)** (Client: **[Aptia Group](https://www.aptia-group.com/)**) · Remote, India · December 2025 – Present

Lead the design, development, and production delivery of enterprise AI solutions on Palantir Foundry and AIP. Own technical architecture, implementation, platform operations, release engineering, and production reliability.

#### AIP Copilot — Employee Benefits AI Assistant

- Architected and built an enterprise AI assistant using **AIP Agent Studio, AIP Logic, Python Foundry Functions, and Foundry Ontology**.
- Designed a hybrid architecture that combines structured Ontology queries with RAG over employer-specific benefit documents.
- Built an intent-routing layer in AIP Logic to classify employee questions and direct them to the appropriate workflows.
- Developed deterministic workflows using Python Foundry Functions to retrieve participant, enrollment, dependent, and plan information directly from the Ontology.
- Built agentic workflows in AIP Agent Studio to handle complex questions requiring multiple data sources, document retrieval, and contextual reasoning.
- Implemented semantic vector search to retrieve relevant passages from benefit documents and combine them with structured plan data.
- Added streaming responses and source citations so employees can trace answers to their supporting documents.
- Implemented source-priority rules and response-grounding controls to keep answers aligned with authoritative benefit information.

#### AI Evaluation & Responsible AI

- Built **15+ AIP evaluation suites covering 800+ regression questions** to test classification, retrieval, answer accuracy, completeness, and safety.
- Developed LLM-as-a-Judge workflows using Claude models to evaluate response quality, factual grounding, and policy adherence.
- Established a **90% minimum evaluation quality threshold** as part of the release validation process.
- Introduced binary evaluation criteria to make automated assessments more consistent and actionable.
- Implemented parallel safety validators for legal, medical, tax, and financial-advice scenarios, with restricted requests routed to human support.
- Built embedding-based evaluation workflows to map test questions to relevant document pages and improve retrieval debugging.
- Developed an internal evaluation application that enables business stakeholders to submit test questions, run evaluations, and review results without engineering support.
- Integrated regression evaluations into the release process to identify quality issues before production deployment.

#### Dependent Eligibility Verification — Document Intelligence

- Built an automated document verification solution supporting **20 document types and 16 validation checks**.
- Developed document-processing workflows to extract information, validate submitted details, and determine dependent eligibility.
- Implemented validation rules to identify missing information, inconsistent details, name mismatches, and failed eligibility conditions.
- Generated structured verification results with clear pass/fail outcomes and explanations for failed checks.
- Designed human-in-the-loop workflows to route unsuccessful or inconclusive cases for manual review.
- Reduced document verification processing time to approximately **one minute per case**, improving operational efficiency and auditability.
- Implemented event-driven integrations to exchange verification outcomes with downstream systems.

#### Palantir Foundry — Platform Engineering & Administration

- Serve as a **Palantir Foundry Platform Administrator**, owning platform operations, application deployments, environment governance, and production support.
- Manage application delivery across Development, UAT, Staging, Production, and Internal Production environments.
- Develop and maintain Foundry data pipelines, datasets, Ontology integrations, and reusable deployment workflows.
- Own release execution, from data modelling and pipeline development to incremental ingestion, packaging, deployment validation, and environment promotion.
- Built automated monitoring and alerts for failed builds, data synchronization, and search-indexing operations.
- Developed an Environment Health Check application to compare configurations and validate consistency across four environments.
- Automated **158 validation tests across 36 resource types**, replacing manual pre-release checks with one-click HTML reports.
- Provide L3 production support, resolving application failures, data issues, integration problems, and deployment-related incidents.

### Technical Lead — ML & AI
**[TechnoMile](https://technomile.com/)** · Remote, India · Sept 2023 – Nov 2025

- Built the LLM extraction engine for TechnoMile's **Contract Lifecycle Management** and **Pre-Award** products (**OpenAI, Claude, Llama**), raising CLIN accuracy on federal contracts from **58% to 90%** across 7 contract domains.
- Shipped contract question-answering with **RAG**, chunking and embedding documents into a **FAISS/Chroma** vector store so answers are grounded in retrieved text rather than model memory.
- Built Pre-Award **Copilot** features that extract clauses, deliverables and risk indicators from government solicitations, plus **Model Context Protocol (MCP)** agents that answer plain-language questions from internal APIs and databases.
- Split a monolithic extraction service into four CLIN, Clause, Section and Form services orchestrated with **AWS Step Functions**, cutting CLIN processing time **40%** (370s to 220s) with parallel chunk handling.
- Built QA tooling that scores each extracted field against ground truth and boxes its source location in the PDF, so reviewers catch invented fields. Tracked models with **MLflow** and **Arize Phoenix**.

### Senior Consultant
**[Celebal Technologies](https://celebaltech.com/)** · Remote, India · Sept 2021 – Aug 2023

- Led payslip forgery detection for a payroll client (**85.23%** accuracy) with **Azure Form Recognizer** and tamper checks.
- Built key-information extraction for KYC documents and receipts at **94%+** accuracy, and payslip classification and blur detection models on **Azure Custom Vision** at **90.87%** and **95.72%** accuracy.
- Architected a secure serving platform on **Redis, AKS, Docker, Azure API Management, Key Vault and OAuth 2.0**, with queue workers autoscaled by **KEDA**, cutting processing time **10x**.
- Partnered with **Microsoft** on a forecasting platform for energy portfolio management, adding training-loss monitoring across **DeepMC, TFT, N-BEATS and TCN** models with pipelines on **Azure ML Studio** and **Azure Functions**.
- Fine-tuned a Spanish sentence-embedding model on Walmart Mexico catalog data on **Databricks**, adding **FLAN-T5** keyword generation and **FAISS** search to improve ad recommendations, validated against add-to-cart data.

### Machine Learning Engineer
**[Konverge.AI](https://konverge.ai/)** · India · Aug 2018 – Aug 2021

- Led a team of **10** on solution architecture and work breakdown for Smart Content Extraction.
- Built data ingestion APIs with **Airbyte** connectors for the WEAV Core libraries.
- Built eKYC components that match faces across video frames and read identity cards with OCR.

---

## Education

**Master of Technology, Computer Science and Engineering** — [RCOEM](https://www.rknec.edu/), Nagpur, India · Aug 2016 – Aug 2018

**Bachelor of Engineering, Information Technology** — [SVPCET](https://www.stvincentngp.edu.in/), Nagpur, India · Aug 2012 – Aug 2016

---

## Publications

- [Dimensionality Reduction for Improving the Performance of Risk Calculation Using Machine Learning Algorithms](http://helix.dnares.in/2018/09/07/dimensionality-reduction-for-improving-the-performance-of-risk-calculation-using-machine-learning-algorithms/), HELIX, 2018
- [Review on Application of Data Mining in Life Insurance](https://www.sciencepubco.com/index.php/ijet/article/view/20035), International Journal of Engineering & Technology, 2018

## Certifications, Achievements & Languages

- **Certifications:** [Statistical Learning, StanfordOnline](https://courses.edx.org/certificates/b51d9b57b98e40238921a7430ad46f73) · OAuth 2.0 · Docker · [Data Science](https://www.udemy.com/certificate/UC-FCRNNE54/)
- **Achievements:** [Microsoft AI/ML competition (2022)](https://www.credly.com/badges/02d6cb29-e29e-44cc-8823-3533df0c423f?source=linked_in_profile) · [Artificial Intelligence and Machine Learning Workathon (2021)](https://www.credly.com/badges/74f831f7-aa06-4aa5-8a63-40e27ff0048c?source=linked_in_profile)
- **Languages:** English (C1 Advanced, professional working proficiency)
