#!/bin/bash
echo "--- RUNNING AURA A/B ABLATION STUDY (72 hours) ---"

# Run simulation with AURA enabled
echo "--- RUNNING WITH AURA ENABLED ---"
python src/app/main.py --simulation-ticks 72 --aura-enabled true --output-file reports/simulation_aura_on.csv

# Run simulation with AURA disabled
echo "--- RUNNING WITH AURA DISABLED ---"
python src/app/main.py --simulation-ticks 72 --aura-enabled false --output-file reports/simulation_aura_off.csv

echo "--- ABLATION STUDY COMPLETE ---"
