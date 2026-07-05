"""Test configuration for Incident Response Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "incident-response-agent", "category": "DevOps & Platform Engineering"}
