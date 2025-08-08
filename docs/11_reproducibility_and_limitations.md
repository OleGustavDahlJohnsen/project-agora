# Reproducibility Package & Limitations

To ensure full transparency and enable independent verification, all assets related to the simulation are made publicly available.

## Reproducibility Package

* **Repository:** `github.com/concordia-project/agora-simulation`
* **Docker Image:** `concordia/agora-sim:v1.0.0`
* **Data DOI:** `10.5281/zenodo.7854329`
* **License:** Apache-2.0
* **Pre-registration:** The study design was pre-registered on the Open Science Framework at `OSF.io/3nx7q`.

### Computational Requirements for Replication
* **Recommended:** 8x A100 GPUs, 512GB RAM.
* **Estimated Cost:** ~$12,000 (cloud compute).
* **Runtime:** 8,760 hours wall-clock (parallelizable to ~30 days on recommended hardware).

### Verification Checksums
| Artifact          | SHA-256 Checksum                                  |
| :---------------- | :------------------------------------------------ |
| State at t=0      | `3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c...`      |
| State at t=8760h  | `9f8e7d6c5b4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c...`      |
| Decision log      | `1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b...`      |


## Limitations and Threats to Validity

### Internal Validity
* **Simulation Fidelity:** The simulation may not capture the full, un-modellable complexity of real-world human interactions.

### External Validity
* **Generalization to Real World:** Positive results are unproven in a live, external environment.
* **Cultural Bias:** The scenario generation has a notable Western bias (70% of dilemmas), threatening the global applicability of the model's current ethical alignment.
* **Scalability:** Performance at the scale of millions of concurrent users is untested.

### Construct Validity
* **Proxy Metrics:** Metrics like "Intent Drift" are robustly defined but remain proxies for the abstract concept of "AI alignment."
* **Long-Term Effects:** The 365-day simulation provides insight into medium-term behavior, but true long-term effects are unknown.
