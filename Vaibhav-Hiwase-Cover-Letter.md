# Vaibhav Hiwase

AI/ML Engineer & Technical Lead — LLM Applications, Evaluation & Production AI Platforms

Nagpur, India · [(+91) 8999382164](tel:+918999382164) · [hiwase.vaibhav@gmail.com](mailto:hiwase.vaibhav@gmail.com) · [linkedin.com/in/vaibhav-hiwase](https://www.linkedin.com/in/vaibhav-hiwase)

---

25 August 2026

> [Hiring Manager Name]
> [Company Name]
> [City, Country]

Dear [Hiring Manager],

I'm writing to apply for the [Role Title] role at [Company]. I currently own two production AI systems end to end on Palantir Foundry and AIP, and what I would bring to [Company] is less about any single platform than about a specific discipline: getting LLM systems past the demo stage and keeping them dependable once real people rely on them every day.

At Aptia Group I built and own an employee benefits assistant that answers questions on plans, coverage, dependents, ID cards and HSA/FSA in plain language — an Agent Studio agent composed of 16 Foundry Functions, live across five environments. The design decision I would point to first is the routing. An intent classifier sends each question down one of roughly 14 paths and answers it directly from the Ontology wherever the data already exists, so the LLM is invoked only where it genuinely has to be. That keeps common answers deterministic and traceable. It also proved its worth commercially: after I merged logs from 21 Functions into a single timeline, the data showed one fallback agent absorbing 75% of our AI spend, and re-routing common questions away from it cut the cost of a typical question by roughly 95%.

The part of this work I care most about is evaluation. I own 15+ evaluation suites over an 800+ question regression set, scored by LLM judges aligned to benefits domain experts through critique shadowing rather than tuned against an invented rubric. Every suite has to hold above a 90% pass rate before a release is promoted. I also built the Workshop apps that let the benefits team author their own test questions and review AI scores directly, because the people who define what "correct" means should own that standard rather than engineering.

Alongside the products I run the platform: modelling the Ontology behind both workflows, migrating ~80 Action Types without breaking downstream consumers, packaging pipelines as a Marketplace product that installs into any environment unchanged, and approving promotions from Dev through to Production as Platform Admin. Before Foundry I led contract-document AI at TechnoMile, raising extraction accuracy from 58% to 90% across seven domains and decomposing a monolithic service into four orchestrated services that ran 40% faster.

I would welcome the chance to talk about [specific team, product or problem at Company] and where this experience would be most useful. Thank you for your time and consideration.

Sincerely,

Vaibhav Hiwase
