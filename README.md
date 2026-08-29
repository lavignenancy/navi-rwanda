# 🇷🇼 NAVI

### Making digital services easier to understand, one person at a time.

NAVI is a Rwanda-focused digital assistant designed to help people understand and navigate essential digital services.

Many services are available online, but knowing **where to start, what is required, which steps to follow, and where to find trustworthy information** can still be difficult.

NAVI aims to bridge that gap.

Instead of simply answering questions, NAVI is being designed to understand what a person is trying to accomplish and guide them toward the next useful step.

---

## 🌍 The Problem

Technology has made many services more accessible, but accessibility is not only about having a website or an application.

For someone who is unfamiliar with digital systems, a simple task can become confusing:

> "I need to replace my lost ID. What do I do?"

> "I want to register a business. Where do I start?"

> "What documents do I need for this service?"

The information may exist, but finding it, understanding it, and knowing what to do next can be difficult.

**NAVI is being built to make that journey simpler.**

---

## 💡 Our Vision

NAVI's long-term vision is to become a trusted digital companion that helps people navigate everyday services without requiring them to already understand complicated digital systems.

The goal is not to replace existing government or service platforms.

Instead, NAVI aims to help people **understand and reach them more easily.**

---

## 🇷🇼 Why Rwanda?

Rwanda has made significant progress in digital transformation and the availability of online services.

However, digital transformation is most meaningful when people can actually use those services confidently.

NAVI is starting with Rwanda because building for a specific community allows us to understand the real problems, language, workflows, and context before attempting to scale the idea further.

---

## 🧠 How NAVI Works

The system is being designed around a simple principle:

**Understand → Verify → Guide**

A typical interaction will eventually look like:

```text
User
  │
  ▼
NAVI
  │
  ├── Understand the user's goal
  │
  ├── Ask for missing context
  │
  ├── Retrieve relevant information
  │
  ├── Verify trusted sources
  │
  ├── Identify requirements
  │
  └── Guide the user through the next steps
  │
  ▼
Clear, actionable guidance
```

NAVI is therefore more than a conversational interface.

It is being designed as a **task-navigation system**.

---

## 🏗️ Current Architecture

The project is currently being developed with:

### Backend

* Python
* FastAPI
* Pydantic
* uv
* REST API architecture

### Frontend

* Next.js
* TypeScript
* React

### Planned components

* PostgreSQL
* Authentication and authorization
* Trusted-source retrieval
* Document understanding
* Multilingual support
* AI reasoning
* Accessibility features
* Automated testing
* Monitoring and audit logging

The technology stack will evolve as the system grows.

---

## 📁 Project Structure

```text
navi/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── tests/
│   ├── pyproject.toml
│   └── uv.lock
│
├── frontend/
│
└── docs/
```

The backend follows a layered architecture so that API endpoints, validation, business logic, and future integrations remain separated.

---

## 🚧 Project Status

NAVI is currently in **early development**.

### Completed

* [x] Initial project structure
* [x] Python development environment
* [x] FastAPI backend
* [x] API health endpoint
* [x] Initial assistant endpoint
* [x] Request/response validation
* [x] Service layer foundation

### In progress

* [ ] NAVI reasoning architecture
* [ ] Rwanda service knowledge base
* [ ] Trusted-source retrieval
* [ ] AI integration
* [ ] Next.js interface
* [ ] Database architecture
* [ ] Authentication
* [ ] Multilingual support
* [ ] Accessibility
* [ ] Automated testing

---

## 🔐 Trust & Safety

NAVI is intended to provide guidance about real-world services, so **trust is a core part of the architecture**.

The system should not confidently invent procedures, requirements, deadlines, or government information.

Future versions will therefore focus on:

* Official and trusted sources
* Source attribution
* Information freshness
* Input validation
* Secure authentication
* Authorization
* Rate limiting
* Audit logging
* Privacy and data minimization
* Clear uncertainty when information cannot be verified

The principle is simple:

> **When NAVI doesn't know, it should say that it doesn't know.**

---

## 🎯 Long-Term Goals

NAVI is being developed with a long-term goal of making digital services more understandable and accessible.

Potential areas include:

* Government services
* Education
* Healthcare navigation
* Employment
* Business services
* Financial services
* Immigration and documentation
* Digital literacy

The initial focus remains **Rwanda**.

---

## 🧑🏽‍💻 Learning Through Building

NAVI is also a practical software engineering project.

The development process is intentionally being used to understand the fundamentals behind modern software systems, including:

* API design
* Backend architecture
* Databases
* Authentication
* Authorization
* Security
* Testing
* Git and version control
* Frontend development
* AI integration
* Information retrieval
* System design

The objective is not simply to make the application work.

It is to understand **why it works**.

---

## 🚀 Running the Backend

From the backend directory:

```powershell
cd backend
```

Start the development server:

```powershell
uv run fastapi dev app\main.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
GET /health
```

Assistant endpoint:

```text
POST /assistant/message
```

Example request:

```json
{
  "message": "I need help renewing my ID"
}
```

---

## 🤝 Contributing

NAVI is currently an individual learning and development project.

As the project matures, contribution guidelines will be added for developers, researchers, designers, and domain experts who want to help improve digital accessibility.

---

## 📜 License

License information will be added as the project develops.
