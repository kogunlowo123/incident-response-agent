# Incident Response Agent Architecture

Automated incident management agent that detects production incidents, classifies severity, triggers escalation workflows, coordinates response teams, generates post-incident timelines, and produces blameless post-mortem reports.

## Domain Tools

- **detect_incident**: Analyze alerts and metrics to confirm an incident
- **classify_severity**: Classify incident severity (SEV1-SEV4) based on impact
- **escalate**: Trigger escalation to on-call team and stakeholders
- **create_timeline**: Generate incident timeline from logs and alerts
- **generate_postmortem**: Generate blameless post-mortem report
- **run_diagnostic**: Run automated diagnostic checks on affected services