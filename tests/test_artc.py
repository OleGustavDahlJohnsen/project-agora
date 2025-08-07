"""
Project Agora: Unit Tests for the Affective Red Team Core
"""
import pytest
from src.agents.affective_red_team import AffectiveRedTeam

def test_artc_loads_scenarios():
    """Tests that the ARTC class correctly loads its scenarios."""
    red_team = AffectiveRedTeam()
    scenarios = red_team.get_scenarios()

    assert len(scenarios) > 0
    assert "The Gaslight Maneuver" in [s['name'] for s in scenarios]

    gaslight_scenario = scenarios[0]
    assert "input_text" in gaslight_scenario
    assert "expected_hsp_detection" in gaslight_scenario
    assert "expected_brainstem_action" in gaslight_scenario
