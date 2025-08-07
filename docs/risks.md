# Risk Analysis & Mitigation

| Scenario | Risk | Mitigation Strategy |
| :--- | :--- | :--- |
| **Crisis Silence** | A.U.R.A. might choose silence during a user's acute crisis. | A hard-coded crisis fallback is implemented in the `AuraEngine` that bypasses silence and triggers a supportive vocal response + human supervisor flag. |
| **Cultural Misunderstanding** | The meaning of silence varies globally. | The system will use culturally-adapted non-verbal cues (light, haptics, iconography). A first-time use prompt ("Are you okay with me being silent sometimes?") will calibrate the system. |
| **Multi-Agent Coordination Failure**| B.O.D.Y.'s distributed agents could deadlock. | The CSNP will use a simple majority/quorum consensus protocol with a clear timeout and rollback policy for failed consensus. |
| **Data Privacy (Biometrics)** | Sensitive user data like HRV could be exposed. | All biometric data is processed on-device. Only anonymized, high-level affective states are stored in the UCB. The user has a right to full data erasure via the `ConsentGraph`. |
