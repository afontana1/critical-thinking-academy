# Appendix D — Pseudo-Data Test Plan

## Test categories

1. Accounting identities
2. Bounds and non-negativity
3. Extreme conditions
4. Loop isolation
5. Known-equilibrium tests
6. Shock responses
7. Synthetic parameter recovery
8. Time-step sensitivity
9. Random-seed reproducibility
10. Long-horizon stability

| Test ID | Version | Setup | Expected behavior | Actual | Pass/fail | Notes |
|---|---|---|---|---|---|---|
| V-001 | MVP | Equal states and parameters | No endogenous divergence | | | |
| V-002 | MVP | Group 1 has higher assets | Persistent/widening gap under R1 | | | |
| V-003 | Credit | Disable credit loop | R2 effect disappears | | | |
| V-004 | Policy | Full equalizing transfer | Gap narrows subject to other loops | | | |
