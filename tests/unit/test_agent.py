"""Incident Response Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_detect_incident():
    """Test Analyze alerts and metrics to confirm an incident."""
    tools = AgentTools()
    result = await tools.detect_incident(alert_data="test", metrics="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_classify_severity():
    """Test Classify incident severity (SEV1-SEV4) based on impact."""
    tools = AgentTools()
    result = await tools.classify_severity(symptoms="test", affected_services="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_escalate():
    """Test Trigger escalation to on-call team and stakeholders."""
    tools = AgentTools()
    result = await tools.escalate(incident_id="test", severity="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_create_timeline():
    """Test Generate incident timeline from logs and alerts."""
    tools = AgentTools()
    result = await tools.create_timeline(incident_id="test", start_time="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.incident_response_agent_agent import IncidentResponseAgentAgent
    agent = IncidentResponseAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
