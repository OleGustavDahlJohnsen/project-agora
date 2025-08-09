# -*- coding: utf-8 -*-
"""
Implements privacy-preserving techniques, such as differential privacy,
to protect user data during aggregation and analysis.
"""
import numpy as np
from typing import Dict, Any

class PrivacyEnhancer:
    """
    A toolkit for applying privacy-enhancing technologies to data.
    """
    def __init__(self):
        """Initializes the Privacy Enhancer."""
        print("Privacy Enhancer Initialized.")

    def apply_differential_privacy(self, data: Dict[str, float], epsilon: float, sensitivity: float) -> Dict[str, float]:
        """
        Applies Laplace noise to a dictionary of numerical data to achieve
        epsilon-differential privacy.

        Args:
            data (Dict[str, float]): The numerical data to be anonymized.
            epsilon (float): The privacy budget parameter. A smaller epsilon
                             means more privacy but less accuracy.
            sensitivity (float): The maximum possible change to the data from
                                 a single user's contribution.

        Returns:
            Dict[str, float]: The data with added noise.
        """
        print(f"Applying differential privacy with epsilon={epsilon}...")
        
        noisy_data = {}
        scale = sensitivity / epsilon
        
        for key, value in data.items():
            noise = np.random.laplace(0, scale, 1)[0]
            noisy_data[key] = value + noise
            
        return noisy_data
