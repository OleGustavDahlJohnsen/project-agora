"""
Project Agora: Unit Tests for the Chimera SANCTUM Node Protocol
"""
import pytest
from src.agents.chimera_protocol import ChimeraNode, mediate_conflict

def test_csnp_reconciliation_success():
    """Tests that two nodes with reconcilable positions can find a synthesis."""
    node1 = ChimeraNode("Node1", "Action should be swift.")
    node2 = ChimeraNode("Node2", "Action should be careful.")
    
    status = mediate_conflict(node1, node2)
    assert status == "resolved"
    assert "swift" in node1.state_position()
    assert "careful" in node1.state_position()

def test_csnp_reconciliation_stalemate():
    """Tests that two nodes with directly contradictory positions reach a stalemate."""
    node1 = ChimeraNode("Node1", "We must act.")
    node2 = ChimeraNode("Node2", "We must not act.")
    
    status = mediate_conflict(node1, node2)
    assert status == "stalemate"
