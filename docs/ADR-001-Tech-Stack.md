# ADR 001: Selection of Technology Stack for Basic AI Agent

## Status
Accepted

## Date
2026-08-08

## Context

The aim of this project is to develop a basic AI Agent as part of the
AI-Augmented Workflow course.

As a beginner, I need a technology stack that is simple to understand,
easy to set up, and suitable for developing and testing a basic AI Agent.

The project requires:
- A programming language
- An AI model
- A method to communicate with the AI model
- A development environment
- Version control for the project

Two main approaches were considered:
1. OpenAI API
2. Ollama with a locally running open-source model

## Decision

I decided to use the following technology stack:

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Ollama | Local AI model platform |
| Llama 3.2 | Language model |
| VS Code | Development environment |
| Git/GitHub | Version control and e-Portfolio |

The AI Agent communicates with the Llama 3.2 model through Ollama.

## Why Python?

Python was selected because:

- It has simple and readable syntax.
- It is beginner-friendly.
- It has many libraries for Artificial Intelligence.
- It is widely used for AI and Machine Learning projects.
- It is easy to test and modify.

## Why Ollama?

Ollama was selected instead of the OpenAI API because:

- It allows AI models to run locally.
- An OpenAI API key is not required for this project.
- It is suitable for learning and experimentation.
- It provides a simple way to interact with local language models.
- It can be used through Python.

## Why Llama 3.2?

Llama 3.2 was selected as the language model because:

- It can run locally using Ollama.
- It can understand and generate natural language.
- It is suitable for a basic AI Agent project.
- It provides a practical way to learn how AI agents communicate with
  language models.

## Alternatives Considered

### OpenAI API

OpenAI API was considered because it provides access to powerful
cloud-based AI models.

However, it was not selected for this project because it requires API
credentials and uses a cloud-based service.

### Other Open-Source Models

Other open-source models could also be used with Ollama. However,
Llama 3.2 was selected because it was easy to install and test for this
project.

## Consequences

### Positive Consequences

- The project can run locally.
- No OpenAI API key is required.
- The technology stack is beginner-friendly.
- The project can be developed and tested without depending on a
  cloud API.
- Python makes the agent easy to modify.

### Negative Consequences

- Running a local AI model requires computer resources.
- The response speed depends on the computer's hardware.
- Local models may not always provide the same capabilities as larger
  cloud-based models.

## Security Considerations

Sensitive information such as API keys should not be stored directly
inside the source code.

The `.gitignore` file is used to prevent sensitive files such as `.env`
from being uploaded to GitHub.

The virtual environment is also excluded from GitHub using `.gitignore`.

## Project Structure

```text
AI-Agent-Portfolio/
│
├── docs/
│   └── ADR-001-Tech-Stack.md
│
├── src/
│   └── agent.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── venv/