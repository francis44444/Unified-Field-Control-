import json
import os
import numpy as np

def run_quantum_emf_layer():
    config_path = "agent_config.json"
    
    # Read the agent's updated variable
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
            freq = config.get("emf_frequency", 100.0)
    else:
        freq = 100.0

    print(f"[Core] Analyzing field resonance at {freq} MHz...")
    
    # Theoretical target resonance vector (e.g., 444.44)
    target = 444.44
    divergence = abs(target - freq)
    
    # Generate structural state log for the agent
    log_payload = {
        "scale": "subatomic_quantum_emf",
        "frequency_tested": freq,
        "divergence_error": round(divergence, 4),
        "status": "STABLE" if divergence < 0.01 else "UNSTABLE"
    }
    
    with open("simulation_log.json", "w") as log_file:
        json.dump(log_payload, log_file, indent=4)
    
    print(f"[Core] Log updated. Status: {log_payload['status']}")

if __name__ == "__main__":
    run_quantum_emf_layer()
