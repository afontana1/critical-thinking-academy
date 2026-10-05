# Chapter 15 — Verification with Pseudo Data

**Guiding question:** Does the model behave correctly before real-data calibration?

## Chapter deliverable

A finished chapter should make one clear argument, define every concept used later, distinguish established mechanisms from original synthesis, and end by motivating the next chapter.

## Proposed structure

### Verification versus validation

- Verification checks implementation; validation checks usefulness and behavioral adequacy.

### Synthetic population

- Define groups/agents, initial distributions, weights, and generation structure.

### Baseline regime

- Choose transparent parameters with known qualitative implications.

### Unit tests

- Accounting, non-negativity, bounds, reproducibility, and probability sums.

### Extreme conditions

- Zero inequality, no credit, perfect credit, no depreciation, no inheritance, full redistribution, and severe shocks.

### Loop isolation

- Activate one loop at a time and verify expected sign and behavior.

### Synthetic parameter recovery

- Generate data from known parameters and test the calibration pipeline.

### Numerical stability

- Time-step sensitivity, solver comparison, clipping, and long-horizon behavior.

### Acceptance criteria

- Define pass/fail thresholds before using real data.

## Evidence to collect

- Primary theoretical source for every major mechanism.
- Best empirical estimate for each causal relationship or parameter.
- Scope conditions and conflicting findings.

## Planned figures and tables

- One figure only when it clarifies structure, behavior, or measurement.
- One table mapping claims to evidence, variables, equations, or data when useful.

## Writing prompts

- What must the reader believe by the end of this chapter?
- Which claims are literature-backed, and which are hypotheses?
- Which terms require operational definitions?
- Which causal arrows require direct evidence?
- What assumptions or boundary conditions must be explicit?
- How does the final paragraph motivate the next chapter?

## Completion checklist

- [ ] Opening states the chapter problem.
- [ ] Concepts and notation are consistent.
- [ ] Major causal claims are sourced or labeled as hypotheses.
- [ ] Equations are interpretable and dimensionally plausible.
- [ ] Figures and tables have analytical purposes.
- [ ] Limitations are explicit.
- [ ] Closing advances the monograph narrative.
