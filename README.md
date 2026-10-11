<img src="avatar.jpg" alt="Иван Кузнецов" align="right" width="150">

<!-- lang-switch -->
[![Русский](https://img.shields.io/badge/%F0%9F%87%B7%F0%9F%87%BA_Русский-a8481c?style=flat)](README.md) [![English](https://img.shields.io/badge/%F0%9F%87%AC%F0%9F%87%A7_English-8a8580?style=flat)](README.en.md)

# Иван Кузнецов

## Senior Python Developer · Backend · агентные системы на LLM

[![GitHub](https://img.shields.io/badge/GitHub-onelinelater-181717?style=flat&logo=github)](https://github.com/onelinelater)
[![GitLab](https://img.shields.io/badge/GitLab-onelinelater-FC6D26?style=flat&logo=gitlab)](https://gitlab.com/onelinelater)
[![Email](https://img.shields.io/badge/Email-onelinelater@gmail.com-D14836?style=flat&logo=gmail)](mailto:onelinelater@gmail.com)
[![Telegram](https://img.shields.io/badge/Telegram-@onelinelater-2CA5E0?style=flat&logo=telegram)](https://t.me/onelinelater)
[![Location](https://img.shields.io/badge/Location-Хабаровск-4285F4?style=flat&logo=google-maps)](https://maps.google.com/?q=Хабаровск)
[![Remote](https://img.shields.io/badge/Формат-Remote-34D399?style=flat)](/)

---

## 📊 Статистика

| 🏆 Опыт | 🏢 Компании | 🧩 Своя платформа | 💎 Уровень | 💰 Ожидания |
|:---:|:---:|:---:|:---:|:---:|
| **9+ лет** | KPMG · БСТ · БАРС Груп · Navio | **14 сервисов · 1000+ коммитов** | **Senior** | **250 000 ₽/мес** |

---

## 👨‍💻 Профессиональный профиль

**Python-разработчик** с 2017 года: прошёл путь от Junior на Node.js до Senior, который ведёт ревью, собеседует разработчиков и в одиночку закрывает backend клиентского проекта.

**Backend** — основная специализация: FastAPI, Flask, Django, aiohttp, Tornado. Событийная обработка на Kafka и RabbitMQ (FastStream, pika), устойчивые длительные процессы и Saga на Temporal. PostgreSQL на уровне планов запросов: `EXPLAIN ANALYZE`, индексы, а в своих проектах — `LISTEN/NOTIFY` и очереди на `SKIP LOCKED`.

**Качество**: тесты на критичные модули, Repository и чистая архитектура там, где они окупаются, SonarQube и ревью.

**FullStack** — продукт целиком в одних руках: Vue 3, Angular, React, Nuxt на фронте; сервисы на Node.js (Express, Sequelize); один и тот же продукт — веб, десктоп на Electron и Android на Capacitor.

**Агентные системы на LLM** — направление, в котором живу последние месяцы: построил платформу, где Claude и Codex берут задачи из трекера, пишут код в отдельных копиях репозитория, ревьюят друг друга и отчитываются на телефон.

Открыт к позициям: **Senior Python / Backend Developer · Platform Engineer · AI / LLM Engineer (агенты, оркестрация)**

---

## 🛠 Технический стек

### Backend

```
Python            ●●●●●  FastAPI · Flask · Django / DRF · aiohttp · Tornado · asyncio · Pydantic 2
ORM и миграции    ●●●●○  SQLAlchemy (в т.ч. async) · Alembic · asyncpg · паттерн Repository
Событийность      ●●●●○  Apache Kafka · RabbitMQ · FastStream · pika · Celery
Долгие процессы   ●●●○○  Temporal / temporalio — Saga, повторы, промежуточные состояния
Авторизация       ●●●○○  JWT · RBAC · права в профиле пользователя
ЭП                ●●●○○  КриптоПро · CAdES — сервис проверки подписи под ключ
Go                ●●●○○  агент машины: узлы сети, обратный канал, выкатка с откатом, AAR для Android
```

### Frontend

```
Vue 3             ●●●●○  Composition API · Vue Router · Vuex · Nuxt
Angular           ●●●○○  клиентские модули корпоративных систем
React             ●●●○○  SPA поверх собственных API
Node.js           ●●●○○  Express · Sequelize
Десктоп и мобайл  ●●●○○  Electron + SQLite · Capacitor (Android) — офлайн-версии веб-продукта
```

### Базы данных и хранилища

```
PostgreSQL        ●●●●●  EXPLAIN / ANALYZE · индексы · транзакции · LISTEN/NOTIFY · SKIP LOCKED
Redis             ●●●○○  кэш · fastapi-cache
MongoDB / NoSQL   ●●●○○
MinIO (S3)        ●●●●○  хранение файлов и фото
ClickHouse        ●●○○○
```

### DevOps и наблюдаемость

```
Docker            ●●●●○  Docker Compose · многоконтейнерные окружения · Astra Linux 1.8
CI/CD             ●●●●○  GitLab CI · собственный раннер · выпуск сборок с sha256 и докачкой
Мониторинг        ●●●○○  Prometheus · Grafana · Loki · Sentry
ETL               ●●○○○  Airflow
```

### AI / LLM

```
Агенты            ●●●●○  Claude Code · Codex · локальный Qwen — оркестрация, ревью агентом агента
MCP               ●●●●○  свой MCP-сервер трекера задач, скиллы для агентов
Речь              ●●●○○  faster-whisper на CUDA · стенограмма созвона в реальном времени
```

`Git` `pytest` `Ruff` `MyPy` `uv` `Poetry` `SonarQube` `Jira` `Confluence` `Redmine`

---

## 💼 Опыт работы

### 🟡 iStaff-IT / Navio — Python-разработчик

**Октябрь 2025 — Декабрь 2025** · *Логистика / микросервисы*

- 🧭 **Спроектировал и реализовал Saga-процесс на Temporal**: длительный бизнес-процесс с промежуточными состояниями, повторными попытками и обработкой ошибок
- 🧱 **Написал переиспользуемый Repository**, который стандартизировал работу с данными и упростил типовые операции во всех сервисах
- 📨 **Строил событийные интеграции** между сервисами на Apache Kafka и FastStream
- ⚡ Развивал асинхронные сервисы на FastAPI и REST API для клиентов и внутренних интеграций

`Python` `FastAPI` `Kafka` `FastStream` `Temporal` `PostgreSQL`

### 🟢 Бизнес Система Телеком — Senior Web Developer (Python + JavaScript)

**Май 2024 — Октябрь 2025**

- 🛡 **Спроектировал и реализовал сервис проверки электронной подписи** на КриптоПро и CAdES целиком: backend, frontend, интеграция с веб-приложением, асинхронная обработка проверок, мониторинг
- 🧯 **Единственным backend-разработчиком принял клиентский проект** после ухода предыдущего исполнителя, реализовал оставшиеся требования и сдал без технического долга
- 🐍 Развивал сервисы на Tornado, Flask, aiohttp и FastAPI; клиентские модули на Vue 3 и Angular; сервисы на Node.js (Express, Sequelize)
- 🚀 Настроил сборку и выкатку через Docker и GitLab CI, включая окружения под Astra Linux 1.8
- 📈 Внедрил мониторинг на Loki, Prometheus, Grafana и Sentry

`Python` `Tornado` `Flask` `FastAPI` `Vue 3` `Angular` `Node.js` `КриптоПро` `Docker` `GitLab CI`

### 🔵 KPMG — Senior Web Developer (Python + JavaScript)

**Сентябрь 2021 — Май 2024** · *Middle → Senior с июля 2023*

- 👥 **Организовывал работу команды**, ревьюил код и проводил собеседования с разработчиками
- 🐍 Разрабатывал микросервисы на Flask с обменом через RabbitMQ, фронтенд на Angular
- 🔍 **Оптимизировал и рефакторил**: SonarQube, планы запросов PostgreSQL (`EXPLAIN`, `ANALYZE`), чистая архитектура
- 🔄 Работал с ETL на Airflow

`Python` `Flask` `RabbitMQ` `Angular` `PostgreSQL` `Airflow` `SonarQube`

### 🟣 БАРС Груп — Middle Web Developer (Python + JavaScript)

**Август 2020 — Сентябрь 2021**

- Веб-приложения на Django + PostgreSQL, плагины интеграции с внешними системами по REST

### ⚪ Fogstream — Junior Web Developer (Python)

**Март 2019 — Август 2020**

- Django, REST-микросервисы, unit-тесты, оптимизация запросов PostgreSQL, фронтенд на ExtJS и Marionette

### ⚪ ИОН-ДВ — Junior Web Developer (Node.js)

**Апрель 2017 — Февраль 2019**

- Веб-приложения на Node.js, десктоп на Electron, SOAP и REST сервисы, e2e-тесты на Selenium

---

## 🤝 Проекты на заказ — онлайн-школа «Хакер ЕГЭ»

Весь цикл в одних руках: требования, архитектура, backend, frontend, сборка и выкатка.

### 📇 CRM поверх AlfaCRM · `production`

*Python · FastAPI · Vue · RabbitMQ · Redis · PostgreSQL*

- **291 коммит за год**: backend на FastAPI, frontend на Vue, отдельные сервисы планировщика и рассыльщика
- **Напоминания об оплате и отложенные сообщения** ученикам — по расписанию, с предпросмотром текста
- **Аналитика по ученикам и деньгам**: графики, календарь с отмеченными уроками
- Переработанный RBAC с правами в профиле, раздельные фильтры, устойчивое подключение к RabbitMQ, CI

`Python` `FastAPI` `SQLAlchemy` `Alembic` `httpx` `Vue` `RabbitMQ` `Redis` `Docker`

### 📐 Тренажёр ЕГЭ по математике · `web · desktop · android`

*Python · FastAPI · Vue 3 · TypeScript · Electron · Capacitor*

- **Один продукт — три платформы**: веб на FastAPI + PostgreSQL, портативные десктоп-приложения на Electron со встроенной SQLite, офлайн-APK на Capacitor
- **Отдельная админка для методистов**: редактор источника заданий; при сохранении backend пересобирает темы, блоки и задачи для клиентов
- **Свой блочный редактор** отдельным пакетом
- Структура разделы → темы → типы заданий; Vue 3 + Vite + Tailwind + Pinia по FSD, схема БД на Alembic, сид из снапшота тем же механизмом, что импорт в админке
- Отдельный сервис сбора публичной структуры источников для подготовки контента

`Python` `FastAPI` `PostgreSQL` `Vue 3` `TypeScript` `Tailwind` `Pinia` `Electron` `SQLite` `Capacitor`

---

## 🚀 Собственные проекты

### 🛰 Argus — платформа для своих машин, телефона и ИИ-агентов · `pet · в ежедневной работе`

*Python · Go · Java (Android) · PostgreSQL · FastAPI · GitLab CI*

Своя распределённая система, в которой работаю каждый день: **14 сервисов, 1000+ коммитов с августа 2026**. Отвечаю за всё — от схемы данных до выкатки на узлы и телефон.

- 🧭 **Мастер парка**: реестр узлов, обратные каналы, CLI `svc` — поднять сервис на удалённой машине, прочитать логи, выполнить команду, выкатить сборку
- 🐹 **Агент машины на Go**: сам находит мастера в локальной сети; выкатка, при которой прежняя сборка уходит только после того, как встала новая
- 📱 **Нативное Android-приложение** (Java, без WebView): телефон — полноценный узел сети, консоль удалённой машины с `vim` и `htop`
- 🤖 **Оркестратор агентов**: задачи спринта из трекера раздаются Claude и Codex, приёмка, ревью вторым агентом, мерж принятого
- 📋 **Трекер задач для людей и агентов**: REST, CLI и MCP над одним сервисным слоем; трудозатраты в минутах у человека и в токенах у агента
- ⏰ **Отложенные задачи и пайплайны**: очередь на Postgres с `SKIP LOCKED` и арендой, cron, графы шагов с подтверждением с телефона
- 🎙 **Речь**: faster-whisper на CUDA, стенограмма созвона по двум дорожкам, расшифровка видео через RabbitMQ

`Python` `FastAPI` `PostgreSQL` `Go` `Java` `Android` `RabbitMQ` `MCP` `Claude` `Codex` `faster-whisper`

### 📄 Конструктор документов · `pet`

*Python · FastAPI · Vue · PDF*

- Редактор шаблонов с подстановкой переменных и режимом предпросмотра, свой DSL, отдельный воркер сборки PDF, CRM-часть

`Python` `FastAPI` `Vue` `MinIO` `PDF`

### 🌿 Vitawalls — управление зонами озеленения · `pet`

*Python · FastAPI · Vue · IoT*

- Организации, пользователи и зоны; привязка устройств и сенсоров, хранение измерений, панель администрирования, e2e-тесты

`Python` `FastAPI` `PostgreSQL` `MinIO` `Docker`

---

## 🎓 Образование

| Год | Учебное заведение | Специальность |
|-----|-------------------|---------------|
| 2018 | Тихоокеанский государственный университет, Хабаровск | Программное обеспечение вычислительной техники и автоматизированных систем (неоконченное высшее) |

---

## 🌍 Языки

🇷🇺 **Русский** — родной  ·  🇬🇧 **English** — B2

---

## 🔎 Дополнительно

**Преподаю**: занятия по Python, Django, FastAPI, SQL и алгоритмам — умею объяснить ООП на стульях и столах.

**Форматы работы:** Remote · командировки иногда

---

## 📞 Контакты

| | |
|---|---|
| **Email** | <onelinelater@gmail.com> |
| **Telegram** | [@onelinelater](https://t.me/onelinelater) |
| **GitHub** | [github.com/onelinelater](https://github.com/onelinelater) |
| **GitLab** | [gitlab.com/onelinelater](https://gitlab.com/onelinelater) |

---

*Резюме обновлено: Октябрь 2026*
