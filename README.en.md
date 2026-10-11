<img src="avatar.jpg" alt="Ivan Kuznetsov" align="right" width="150">

<!-- lang-switch -->
[![Русский](https://img.shields.io/badge/%F0%9F%87%B7%F0%9F%87%BA_Русский-8a8580?style=flat)](README.md) [![English](https://img.shields.io/badge/%F0%9F%87%AC%F0%9F%87%A7_English-a8481c?style=flat)](README.en.md)

# Ivan Kuznetsov

## Senior Python Developer · Backend · LLM agent systems

[![GitHub](https://img.shields.io/badge/GitHub-onelinelater-181717?style=flat&logo=github)](https://github.com/onelinelater)
[![GitLab](https://img.shields.io/badge/GitLab-onelinelater-FC6D26?style=flat&logo=gitlab)](https://gitlab.com/onelinelater)
[![Email](https://img.shields.io/badge/Email-onelinelater@gmail.com-D14836?style=flat&logo=gmail)](mailto:onelinelater@gmail.com)
[![Telegram](https://img.shields.io/badge/Telegram-@onelinelater-2CA5E0?style=flat&logo=telegram)](https://t.me/onelinelater)
[![Location](https://img.shields.io/badge/Location-Khabarovsk,%20Russia-4285F4?style=flat&logo=google-maps)](https://maps.google.com/?q=Khabarovsk)
[![Remote](https://img.shields.io/badge/Format-Remote-34D399?style=flat)](/)

---

## 📊 At a glance

| 🏆 Experience | 🏢 Companies | 🧩 Own platform | 💎 Level | 💰 Expectations |
|:---:|:---:|:---:|:---:|:---:|
| **9+ years** | KPMG · BST · BARS Group · Navio | **14 services · 1000+ commits** | **Senior** | **250,000 ₽/month** |

---

## 👨‍💻 Profile

**Python developer** since 2017: grew from a Junior on Node.js to a Senior who runs code review, interviews developers and single-handedly carries the backend of a client project.

**Backend** is my core: FastAPI, Flask, Django, aiohttp, Tornado. Event-driven processing on Kafka and RabbitMQ (FastStream, pika), durable long-running processes and Sagas on Temporal. PostgreSQL down to query plans: `EXPLAIN ANALYZE`, indexes, and in my own projects `LISTEN/NOTIFY` and `SKIP LOCKED` job queues.

**Quality**: tests on critical modules, Repository and clean architecture where they pay off, SonarQube and code review.

**Full-stack** — a whole product in one pair of hands: Vue 3, Angular, React, Nuxt on the front; Node.js services (Express, Sequelize); one product shipped as web, Electron desktop and Android via Capacitor.

**LLM agent systems** — where I've been living lately: I built a platform where Claude and Codex pick up tasks from a tracker, write code in separate repository copies, review each other and report to my phone.

Open to: **Senior Python / Backend Developer · Platform Engineer · AI / LLM Engineer (agents, orchestration)**

---

## 🛠 Tech stack

### Backend

```
Python            ●●●●●  FastAPI · Flask · Django / DRF · aiohttp · Tornado · asyncio · Pydantic 2
ORM & migrations  ●●●●○  SQLAlchemy (incl. async) · Alembic · asyncpg · Repository pattern
Messaging         ●●●●○  Apache Kafka · RabbitMQ · FastStream · pika · Celery
Long processes    ●●●○○  Temporal / temporalio — Sagas, retries, intermediate states
Auth              ●●●○○  JWT · RBAC · per-user permissions
E-signatures      ●●●○○  CryptoPro · CAdES — a signature verification service end to end
Go                ●●●○○  machine agent: network nodes, reverse channel, rollout with rollback, AAR for Android
```

### Frontend

```
Vue 3             ●●●●○  Composition API · Vue Router · Vuex · Nuxt
Angular           ●●●○○  client modules for enterprise systems
React             ●●●○○  SPAs on top of my own APIs
Node.js           ●●●○○  Express · Sequelize
Desktop & mobile  ●●●○○  Electron + SQLite · Capacitor (Android) — offline builds of a web product
```

### Databases & storage

```
PostgreSQL        ●●●●●  EXPLAIN / ANALYZE · indexes · transactions · LISTEN/NOTIFY · SKIP LOCKED
Redis             ●●●○○  caching · fastapi-cache
MongoDB / NoSQL   ●●●○○
MinIO (S3)        ●●●●○  file and photo storage
ClickHouse        ●●○○○
```

### DevOps & observability

```
Docker            ●●●●○  Docker Compose · multi-container environments · Astra Linux 1.8
CI/CD             ●●●●○  GitLab CI · self-hosted runner · build releases with sha256 and resumable download
Monitoring        ●●●○○  Prometheus · Grafana · Loki · Sentry
ETL               ●●○○○  Airflow
```

### AI / LLM

```
Agents            ●●●●○  Claude Code · Codex · local Qwen — orchestration, agent-to-agent review
MCP               ●●●●○  my own MCP server for a task tracker, agent skills
Speech            ●●●○○  faster-whisper on CUDA · real-time call transcription
```

`Git` `pytest` `Ruff` `MyPy` `uv` `Poetry` `SonarQube` `Jira` `Confluence` `Redmine`

---

## 💼 Experience

### 🟡 iStaff-IT / Navio — Python Developer

**October 2025 — December 2025** · *Logistics / microservices*

- 🧭 **Designed and built a Saga process on Temporal**: a long-running business process with intermediate states, retries and error handling
- 🧱 **Wrote a reusable Repository** that standardized data access and simplified routine operations across services
- 📨 **Built event-driven integrations** between services on Apache Kafka and FastStream
- ⚡ Developed async FastAPI services and REST APIs for clients and internal integrations

`Python` `FastAPI` `Kafka` `FastStream` `Temporal` `PostgreSQL`

### 🟢 Business System Telecom — Senior Web Developer (Python + JavaScript)

**May 2024 — October 2025**

- 🛡 **Designed and built an electronic signature verification service** on CryptoPro and CAdES end to end: backend, frontend, web app integration, async verification, monitoring
- 🧯 **As the sole backend developer, took over a client project** after the previous contractor left, delivered the remaining requirements and handed it over with no technical debt
- 🐍 Developed services on Tornado, Flask, aiohttp and FastAPI; client modules on Vue 3 and Angular; Node.js services (Express, Sequelize)
- 🚀 Set up builds and deployment with Docker and GitLab CI, including Astra Linux 1.8 environments
- 📈 Introduced monitoring with Loki, Prometheus, Grafana and Sentry

`Python` `Tornado` `Flask` `FastAPI` `Vue 3` `Angular` `Node.js` `CryptoPro` `Docker` `GitLab CI`

### 🔵 KPMG — Senior Web Developer (Python + JavaScript)

**September 2021 — May 2024** · *Middle → Senior since July 2023*

- 👥 **Organized the team's work**, reviewed code and interviewed developers
- 🐍 Built Flask microservices communicating over RabbitMQ, frontend on Angular
- 🔍 **Optimized and refactored**: SonarQube, PostgreSQL query plans (`EXPLAIN`, `ANALYZE`), clean architecture
- 🔄 Worked with ETL on Airflow

`Python` `Flask` `RabbitMQ` `Angular` `PostgreSQL` `Airflow` `SonarQube`

### 🟣 BARS Group — Middle Web Developer (Python + JavaScript)

**August 2020 — September 2021**

- Web applications on Django + PostgreSQL, REST integration plugins for external systems

### ⚪ Fogstream — Junior Web Developer (Python)

**March 2019 — August 2020**

- Django, REST microservices, unit tests, PostgreSQL query optimization, frontend on ExtJS and Marionette

### ⚪ ION-DV — Junior Web Developer (Node.js)

**April 2017 — February 2019**

- Node.js web applications, Electron desktop apps, SOAP and REST services, e2e tests with Selenium

---

## 🤝 Client work — Hacker EGE online school

The whole cycle in one pair of hands: requirements, architecture, backend, frontend, builds and deployment.

### 📇 CRM on top of AlfaCRM · `production`

*Python · FastAPI · Vue · RabbitMQ · Redis · PostgreSQL*

- **291 commits in a year**: FastAPI backend, Vue frontend, separate scheduler and notifier services
- **Payment reminders and scheduled messages** to students, with message preview
- **Analytics on students and revenue**: charts, a calendar with attended lessons
- Reworked RBAC with permissions in the user profile, split filters, resilient RabbitMQ connection, CI

`Python` `FastAPI` `SQLAlchemy` `Alembic` `httpx` `Vue` `RabbitMQ` `Redis` `Docker`

### 📐 Math exam trainer (Russian EGE) · `web · desktop · android`

*Python · FastAPI · Vue 3 · TypeScript · Electron · Capacitor*

- **One product, three platforms**: web on FastAPI + PostgreSQL, portable Electron desktop apps with embedded SQLite, an offline APK via Capacitor
- **Separate admin app for content authors**: an editor for the task source; on save the backend rebuilds topics, blocks and tasks for clients
- **Custom block editor** as a standalone package
- Sections → topics → task types; Vue 3 + Vite + Tailwind + Pinia following FSD, Alembic-managed schema, seeding from a snapshot through the same path as the admin import
- A separate service that collects the public structure of sources for content preparation

`Python` `FastAPI` `PostgreSQL` `Vue 3` `TypeScript` `Tailwind` `Pinia` `Electron` `SQLite` `Capacitor`

---

## 🚀 Own projects

### 🛰 Argus — a platform for my machines, phone and AI agents · `pet · used daily`

*Python · Go · Java (Android) · PostgreSQL · FastAPI · GitLab CI*

My own distributed system that I work in every day: **14 services, 1000+ commits since August 2026**. I own all of it — from the data schema to rollouts on nodes and the phone.

- 🧭 **Fleet master**: node registry, reverse channels, the `svc` CLI — start a service on a remote machine, read its logs, run a command, roll out a build
- 🐹 **Machine agent in Go**: discovers the master on the local network by itself; rollouts where the old build goes away only after the new one is up
- 📱 **Native Android app** (Java, no WebView): the phone is a full network node, with a remote machine console running `vim` and `htop`
- 🤖 **Agent orchestrator**: sprint tasks from the tracker go to Claude and Codex, then acceptance checks, review by a second agent, merge of what passes
- 📋 **Task tracker for humans and agents**: REST, CLI and MCP over one service layer; effort tracked in minutes for people and in tokens for agents
- ⏰ **Deferred jobs and pipelines**: a Postgres queue with `SKIP LOCKED` and leases, cron, step graphs with approval from the phone
- 🎙 **Speech**: faster-whisper on CUDA, two-track call transcription, video transcription via RabbitMQ

`Python` `FastAPI` `PostgreSQL` `Go` `Java` `Android` `RabbitMQ` `MCP` `Claude` `Codex` `faster-whisper`

### 📄 Document builder · `pet`

*Python · FastAPI · Vue · PDF*

- Template editor with variable substitution and preview mode, a custom DSL, a separate PDF rendering worker, a CRM part

`Python` `FastAPI` `Vue` `MinIO` `PDF`

### 🌿 Vitawalls — green zone management · `pet`

*Python · FastAPI · Vue · IoT*

- Organizations, users and zones; device and sensor binding, measurement storage, an admin panel, e2e tests

`Python` `FastAPI` `PostgreSQL` `MinIO` `Docker`

---

## 🎓 Education

| Year | Institution | Field |
|------|-------------|-------|
| 2018 | Pacific National University, Khabarovsk | Software for computers and automated systems (incomplete higher education) |

---

## 🌍 Languages

🇷🇺 **Russian** — native  ·  🇬🇧 **English** — B2

---

## 🔎 More

**Teaching**: I tutor Python, Django, FastAPI, SQL and algorithms — I can explain OOP using chairs and tables.

**Work format:** Remote · occasional business trips

---

## 📞 Contacts

| | |
|---|---|
| **Email** | <onelinelater@gmail.com> |
| **Telegram** | [@onelinelater](https://t.me/onelinelater) |
| **GitHub** | [github.com/onelinelater](https://github.com/onelinelater) |
| **GitLab** | [gitlab.com/onelinelater](https://gitlab.com/onelinelater) |

---

*Last updated: October 2026*
