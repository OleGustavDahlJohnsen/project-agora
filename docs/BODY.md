# The B.O.D.Y. Framework (MVP Implementation)

**B.O.D.Y. (Binding Of Distributed Yields)** is the techno-philosophical framework that enables Project Agora v2.0. This document serves as an index for the core modules implemented in the `v2.0-alpha1` release.

### Module Index

| Module | Source Implementation | Unit Tests |
| :--- | :--- | :--- |
| **MCL/UCB**| [`multimodal_fusion_layer.py`](../src/sensors/multimodal_fusion_layer.py) <br> [`unified_context_buffer.py`](../src/agents/unified_context_buffer.py) | [`test_mcl.py`](../tests/test_mcl.py) |
| **A.U.R.A.** | [`aura_engine.py`](../src/aura/aura_engine.py) | [`test_aura.py`](../tests/test_aura.py) |
| **CTL** | [`causal_ledger.py`](../src/agents/causal_ledger.py) | [`test_agents.py`](../tests/test_agents.py) |
| **ARTC** | [`affective_red_team.py`](../src/agents/affective_red_team.py)| [`test_artc.py`](../tests/test_artc.py) |
| **TMW-E** | [`temporal_memory.py`](../src/agents/temporal_memory.py) | [`test_temporal_memory.py`](../tests/test_temporal_memory.py) |
| **SMSL** | [`synesthesia_layer.py`](../src/sensors/synesthesia_layer.py) | [`test_sensors.py`](../tests/test_sensors.py) |
| **THVI** | [`trust_horizon.py`](../src/visualization/trust_horizon.py) | [`test_trust_horizon.py`](../tests/visualization/test_trust_horizon.py) |
| **CSNP** | [`chimera_protocol.py`](../src/agents/chimera_protocol.py) | [`test_csnp.py`](../tests/test_csnp.py) |
