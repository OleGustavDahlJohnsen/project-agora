"""
Project Agora: Unit Tests for Core Systems
Part of The Concordia Project v8.2

This file contains the unit tests for modules in `src/core_systems/`,
such as the TrustKernel and RollbackArchive.
"""
import pytest
from src.core_systems.trust_kernel import TrustKernel
from src.core_systems.rollback_archive import RollbackArchive

# --- Tests for TrustKernel ---

def test_trust_kernel_token_request():
    """Tests that an ethical token is requested only for high-risk DEFCON levels."""
    kernel = TrustKernel()
    # DEFCON 1, 2, and 3 are high-risk and should request a token
    assert "token_approved" in kernel.request_ethical_token(1)
    assert "token_approved" in kernel.request_ethical_token(3)
    # DEFCON 4 and 5 are lower risk and should not require a token
    assert "token_not_required" in kernel.request_ethical_token(4)
    assert "token_not_required" in kernel.request_ethical_token(5)

# --- Tests for RollbackArchive ---

@pytest.fixture
def archive():
    """A pytest fixture to provide a clean RollbackArchive instance for each test."""
    return RollbackArchive()

def test_rollback_store_state(archive):
    """Tests that storing a state correctly adds it to all buffers."""
    state1 = {"id": "state_001", "data": "alpha"}
    archive.store_state(state1)
    
    assert len(archive.buffers["buffer1"]) == 1
    assert len(archive.buffers["buffer2"]) == 1
    assert len(archive.buffers["buffer3"]) == 1
    assert archive.buffers["buffer1"][0]["data"] == "alpha"

def test_rollback_trigger(archive):
    """Tests that triggering a rollback correctly restores the last state."""
    state1 = {"id": "state_001", "data": "alpha"}
    state2 = {"id": "state_002", "data": "beta"}
    archive.store_state(state1)
    archive.store_state(state2)

    assert len(archive.buffers["buffer1"]) == 2

    # Trigger rollback
    result = archive.trigger_rollback()

    assert result["status"] == "restored"
    assert result["state"]["data"] == "beta" # Should restore the last state
    assert len(archive.buffers["buffer1"]) == 1 # The state should be removed after rollback

def test_rollback_on_empty_archive(archive):
    """Tests that triggering a rollback on an empty archive returns an error."""
    result = archive.trigger_rollback()
    assert result["status"] == "error"
