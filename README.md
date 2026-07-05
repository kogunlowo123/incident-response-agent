# Incident Response Agent

[![CI](https://github.com/kogunlowo123/incident-response-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/incident-response-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: DevOps & Platform Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Automated incident management agent that detects production incidents, classifies severity, triggers escalation workflows, coordinates response teams, generates post-incident timelines, and produces blameless post-mortem reports.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `detect_incident` | Analyze alerts and metrics to confirm an incident |
| `classify_severity` | Classify incident severity (SEV1-SEV4) based on impact |
| `escalate` | Trigger escalation to on-call team and stakeholders |
| `create_timeline` | Generate incident timeline from logs and alerts |
| `generate_postmortem` | Generate blameless post-mortem report |
| `run_diagnostic` | Run automated diagnostic checks on affected services |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/incidents` | Create incident |
| `GET` | `/api/v1/incidents/{incident_id}` | Get incident details |
| `POST` | `/api/v1/incidents/{incident_id}/classify` | Classify severity |
| `POST` | `/api/v1/incidents/{incident_id}/escalate` | Escalate incident |
| `GET` | `/api/v1/incidents/{incident_id}/timeline` | Get incident timeline |
| `POST` | `/api/v1/incidents/{incident_id}/postmortem` | Generate post-mortem |

## Features

- Incident Detection
- Severity Classification
- Escalation
- Response Coordination
- Post Mortem Generation

## Integrations

- Pagerduty
- Opsgenie
- Slack Connector
- Prometheus
- Datadog

## Architecture

```
incident-response-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── incident_response_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**PagerDuty + OpsGenie + Slack + Prometheus**

---

Built as part of the Enterprise AI Agent Platform.
