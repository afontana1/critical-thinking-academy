# Causal Inference Interview Guide


## Purpose

This interview is designed to test whether a candidate can reason about causal inference intuitively, verbally, and from first principles. The goal is not to test whether the candidate has memorized a list of estimators. The goal is to determine whether they can:

- Define a causal question precisely.
- Explain why causal effects are not directly observed.
- Distinguish observation from intervention.
- Recognize confounding, collider bias, selection bias, and post-treatment bias.
- Explain why matching or weighting may be useful.
- Justify one design or estimator over another.
- State the assumptions that identify an effect.
- Diagnose overlap, heterogeneity, measurement, interference, and external-validity problems.
- Critique an econometric study by reasoning from the data-generating process rather than from regression output alone.

The interview should repeatedly return to one organizing question:

> What would have happened to the same units under a different treatment, and why should the proposed design recover a credible approximation to that missing outcome?

---

## Suggested Format

- **Length:** 75–100 minutes for the complete sequence.
- **Style:** Conversational. Allow the candidate to think aloud.
- **Order:** Begin with intuition, then introduce notation and methods.
- **Interviewer behavior:** Ask the follow-up probes before supplying terminology.
- **Scoring priority:** Reward clarity, assumptions, and causal logic more than jargon.

Each section contains:

1. A primary interview question.
2. A detailed expected answer.
3. Follow-up probes.
4. Model answers to the follow-up probes.
5. Strong signals and warning signs.

---

# 1. The Fundamental Problem of Causal Inference

## Primary question

> A patient takes a new drug and recovers. Did the drug cause the recovery?

## Detailed expected answer

The candidate should explain that the observation is not sufficient to establish an individual causal effect. We observe the patient's outcome after taking the drug, but we do not observe what would have happened to that same patient, at the same time and under otherwise identical circumstances, had the patient not taken the drug.

Let the two potential outcomes be:

$$
Y_i(1)
$$

for the outcome of individual $$i$$ under treatment, and

$$
Y_i(0)
$$

for the outcome of the same individual under no treatment.

The individual causal effect is:

$$
\tau_i = Y_i(1)-Y_i(0).
$$

Only one of these two potential outcomes is observed:

$$
Y_i = T_iY_i(1)+(1-T_i)Y_i(0),
$$

where:

$$
T_i \in \{0,1\}.
$$

The other potential outcome is counterfactual. Therefore, the individual causal effect cannot generally be observed directly.

A strong verbal explanation would be:

> Recovery after treatment is compatible with several possibilities. The patient may have recovered because of the drug, may have recovered anyway, or may even have recovered despite a harmful drug. To isolate causation, we need a credible estimate of the unobserved outcome under the alternative treatment state.

The candidate may then explain that causal inference shifts the problem from observing individual causal effects to estimating average effects by comparing suitably comparable groups.

For example, the average treatment effect is:

$$
ATE = \mathbb{E}[Y(1)-Y(0)].
$$

## Follow-up probe 1

> Why is this called a fundamental problem rather than merely a small-sample problem?

### Model answer

The problem does not disappear with a larger sample because, for each unit, only one treatment state is realized. Even with millions of observations, we still never observe both potential outcomes for the same individual in the same causal instance. More data can improve estimation of population averages, but it does not reveal the missing individual counterfactual.

A repeated-measures design does not generally solve the problem either because time, prior treatment, learning, disease progression, and other conditions change. Observing the same person treated at one time and untreated at another does not recreate the same causal situation.

## Follow-up probe 2

> If individual causal effects are not observable, how can science estimate causal effects at all?

### Model answer

Science estimates average causal effects by constructing groups that are exchangeable with respect to their potential outcomes. In a randomized experiment, treatment assignment makes the treatment and control groups comparable in expectation. In an observational study, comparability must be argued using assumptions, design choices, covariate adjustment, matching, weighting, instruments, discontinuities, timing, or other sources of identifying variation.

The key move is to use the observed outcomes of one group as an estimate of the missing counterfactual outcomes for another group.

For the treated group, the missing average counterfactual is:

$$
\mathbb{E}[Y(0)\mid T=1].
$$

A valid design provides a credible way to estimate that quantity.

## Follow-up probe 3

> Is causal inference best understood as a missing-data problem, a design problem, or both?

### Model answer

It is both. It is a missing-data problem because one potential outcome is missing for every unit. It is a design problem because the missing potential outcome cannot be recovered through statistical modeling alone unless the design or assumptions make an observed comparison group informative about it.

The missingness is also unusual: it is deterministic with respect to treatment assignment. When treatment is received, the untreated potential outcome is missing; when treatment is not received, the treated potential outcome is missing. The credibility of causal inference therefore depends on how treatment was assigned and whether the comparison group is exchangeable with the target group.

## Strong signals

- Explains the missing counterfactual without hiding behind terminology.
- Distinguishes an observed outcome from an individual causal effect.
- Understands that larger samples do not eliminate the fundamental problem.
- Connects average effects to construction of a credible comparison group.

## Warning signs

- Says the only problem is insufficient sample size.
- Treats temporal ordering as sufficient for causation.
- Moves immediately to statistical significance.
- Assumes a regression coefficient automatically supplies the missing counterfactual.

---

# 2. Why Randomization Works

## Primary question

> If we cannot observe both potential outcomes for one person, why does randomization help?

## Detailed expected answer

Randomization does not reveal both potential outcomes for any individual. It instead makes the treatment and control groups comparable in expectation.

Under ideal random assignment:

$$
T \perp \!\!\! \perp \{Y(1),Y(0)\}.
$$

This means treatment assignment is independent of the potential outcomes. Consequently:

$$
\mathbb{E}[Y(0)\mid T=1] = \mathbb{E}[Y(0)\mid T=0]
$$

and:

$$
\mathbb{E}[Y(1)\mid T=1] = \mathbb{E}[Y(1)\mid T=0].
$$

Therefore, the observed difference in mean outcomes identifies the average treatment effect:

$$
\mathbb{E}[Y\mid T=1]-\mathbb{E}[Y\mid T=0]
= \mathbb{E}[Y(1)-Y(0)].
$$

A strong intuitive answer is:

> Randomization prevents the reasons people receive treatment from also predicting their potential outcomes. The untreated group can therefore stand in for what would have happened to the treated group without treatment, apart from sampling variation.

## Follow-up probe 1

> What does “comparable in expectation” mean?

### Model answer

It means that before treatment is assigned, the expected distribution of both measured and unmeasured baseline characteristics is the same across treatment groups. A particular realized sample may show chance imbalance, but the randomization procedure itself does not systematically direct high-risk or low-risk units into one arm.

The phrase does not mean every covariate will be numerically identical in a finite sample. It means any imbalance arises from chance rather than from a systematic treatment-assignment mechanism linked to potential outcomes.

## Follow-up probe 2

> Does randomization guarantee perfect balance in a finite sample?

### Model answer

No. Randomization guarantees balance in expectation over repeated assignments, not exact balance in every realized experiment. Small samples may have important chance imbalances. Stratified, blocked, paired, or rerandomized designs can improve balance on key baseline covariates.

Covariate adjustment in a randomized experiment may improve precision and can account for chance imbalance, but the causal identification still comes primarily from randomization rather than from the regression model.

## Follow-up probe 3

> What could still go wrong in a randomized study?

### Model answer

Several things can threaten interpretation:

- Noncompliance can make treatment assignment differ from treatment received.
- Attrition can reintroduce selection if outcome observation depends on treatment and prognosis.
- Treatment contamination can blur the contrast between groups.
- Interference can occur when one unit's treatment affects another unit's outcome.
- Outcome measurement can differ across groups.
- Randomization can be implemented incorrectly.
- The study may identify an intention-to-treat effect but be interpreted as a treatment-on-the-treated effect.
- The sample or treatment implementation may not generalize to the policy population.

A strong candidate distinguishes the intention-to-treat estimand from effects involving actual receipt.

## Strong signals

- Explains randomization as a mechanism for exchangeability.
- Distinguishes identification from exact finite-sample balance.
- Distinguishes assignment from receipt.
- Recognizes attrition, interference, and implementation failures.

## Warning signs

- Says randomization works merely because the sample is large.
- Treats balance tests as proof of valid randomization.
- Ignores noncompliance or attrition.

---

# 3. Confounding and the Back-Door Criterion

## Primary question

Consider the graph:

```text
Z ──► X ──► Y
└────────► Y
```

> Why might the observed association between the treatment and outcome fail to equal the causal effect?

## Detailed expected answer

The candidate should identify $$Z$$ as a common cause of treatment $$X$$ and outcome $$Y$$. There are two relevant paths between the treatment and outcome:

```text
X ──► Y
```

which is the causal path, and:

```text
X ◄── Z ──► Y
```

which is a noncausal back-door path.

The back-door path creates association because units with different values of $$X$$ also tend to have different values of $$Z$$, and $$Z$$ affects the outcome. The observed conditional mean difference therefore mixes the causal effect with differences attributable to $$Z$$.

A valid adjustment set blocks all back-door paths while avoiding inappropriate conditioning that blocks the causal effect or opens new noncausal paths.

Under conditional exchangeability:

$$
\{Y(1),Y(0)\} \perp \!\!\! \perp X \mid Z,
$$

the average treatment effect can be identified through adjustment:

$$
\mathbb{E}_Z\left[
\mathbb{E}[Y\mid X=1,Z]
-
\mathbb{E}[Y\mid X=0,Z]
\right].
$$

## Follow-up probe 1

> What is the back-door criterion trying to achieve conceptually?

### Model answer

It is trying to identify a set of pre-treatment variables such that, once we condition on them, the remaining association between treatment and outcome is transmitted only through causal paths from treatment to outcome.

Graphically, the set must block every path between treatment and outcome that begins with an arrow pointing into treatment. It must also avoid descendants of treatment and should not open previously closed collider paths.

Conceptually, the adjustment set aims to make treated and untreated units comparable with respect to the potential outcomes.

## Follow-up probe 2

> Why is “control for everything available” not a valid strategy?

### Model answer

Some variables are harmful controls. Conditioning on a mediator can remove part of the total causal effect. Conditioning on a collider can create an association that did not previously exist. Conditioning on a descendant of treatment may introduce post-treatment bias. Including strong instruments or treatment predictors can also worsen finite-sample performance without improving confounding control.

Variable selection should therefore be based on causal structure, timing, and the estimand, not on a rule that more controls are always better.

## Follow-up probe 3

> Why should adjustment variables generally be measured before treatment?

### Model answer

Variables caused by treatment may lie on the causal pathway, may be colliders, or may encode consequences of treatment and unmeasured causes of the outcome. Conditioning on such variables can change the estimand or create bias.

For a total-effect estimand, pre-treatment common causes of treatment and outcome are typically candidates for adjustment. Post-treatment variables require a different causal question and usually a more explicit mediation or longitudinal framework.

## Strong signals

- Distinguishes causal paths from noncausal paths.
- Explains adjustment as a design decision.
- Connects graphical blocking to potential-outcome exchangeability.
- Rejects control selection based only on predictive strength or significance.

## Warning signs

- Recommends controlling for every available variable.
- Includes mediators while claiming to estimate a total effect.
- Cannot articulate why temporal ordering matters.

---

# 4. Collider Bias and Bad Controls

## Primary question

Consider the graph:

```text
Ability ──► Hiring ◄── Networking
```

Assume ability and networking are unrelated in the overall applicant population.

> If we analyze only people who were hired, would ability and networking remain unrelated? Why?

## Detailed expected answer

No. Hiring is a common effect of ability and networking. In graphical terminology, hiring is a collider.

Before conditioning on hiring, the path:

```text
Ability ──► Hiring ◄── Networking
```

is closed. The causes of a common effect need not be associated.

After restricting the sample to hired applicants, information about one cause becomes informative about the other. Among hired people, someone with relatively low ability must, on average, have had stronger networking or some other favorable hiring factor to pass the selection threshold. Conversely, someone with weak networking is more likely to have compensated with high ability.

Thus, conditioning on hiring induces an association between ability and networking even though no such association existed in the applicant population.

A concise intuition is:

> Once we know the common outcome occurred, the alternative explanations for that outcome compete with one another.

## Follow-up probe 1

> Explain collider bias without using the word “collider.”

### Model answer

When we select people based on an outcome that can be produced by multiple causes, the causes become related inside the selected group. Knowing that one cause was weak makes it more likely that another cause was strong, because everyone in the group had to satisfy the selection rule somehow.

This is why studies restricted to hospitalized patients, admitted students, hired workers, survivors, or program participants can show relationships that do not exist in the broader population.

## Follow-up probe 2

> Why can controlling for more variables make an estimate worse?

### Model answer

Conditioning changes which paths in the causal graph transmit association. Controlling for a common cause may close a noncausal path, but controlling for a common effect may open one. Controlling for a mediator may block part of the effect being estimated. Controlling for a post-treatment consequence can also mix treatment effects with selection effects.

Therefore, the direction of bias is determined by causal structure, not by the number of controls.

## Follow-up probe 3

> Can conditioning on a descendant of a collider also create bias?

### Model answer

Yes. A descendant contains information about the collider. Conditioning on that descendant can partially reveal whether the collider occurred or how strongly it occurred, thereby opening or partially opening the path through the collider.

For example:

```text
X ──► C ◄── U ──► Y
      │
      ▼
      D
```

Conditioning on $$D$$ can induce association between $$X$$ and $$U$$ through the information $$D$$ provides about $$C$$. This creates a noncausal path from $$X$$ to $$Y$$.

## Follow-up probe 4

> How is a collider different from a confounder?

### Model answer

A confounder is a common cause of treatment and outcome:

```text
X ◄── Z ──► Y
```

Conditioning on it generally blocks a noncausal path.

A collider is a common effect:

```text
X ──► C ◄── Y
```

Conditioning on it generally opens a path that was closed.

The distinction is not based on correlation alone. It is based on the direction of causal arrows and on how conditioning changes path connectivity.

## Strong signals

- Explains induced dependence intuitively.
- Recognizes sample restriction as conditioning.
- Understands descendants of colliders.
- Distinguishes a common cause from a common effect.

## Warning signs

- Defines a collider as merely a variable correlated with both treatment and outcome.
- Assumes all conditioning reduces bias.
- Cannot explain why the induced association appears.

---

# 5. Conditioning Versus Intervention

## Primary question

> What is the conceptual difference between observing everyone whose treatment naturally equals a particular value and forcing everyone to take that value?

## Detailed expected answer

The two operations answer different questions.

Conditioning asks about units in the existing world whose treatment naturally took a particular value:

$$
P(Y\mid X=x).
$$

This selects a slice of the observed joint distribution. The mechanisms and causes that produced $$X$$ remain intact. If age, severity, preference, wealth, or another factor influenced treatment assignment, the conditioned group retains the resulting composition.

Intervention asks about a modified world in which the treatment is externally set:

$$
P(Y\mid do(X=x)).
$$

The normal assignment mechanism for $$X$$ is replaced. In a causal graph, incoming arrows into $$X$$ are removed while outgoing causal effects of $$X$$ remain.

A concise verbal distinction is:

> Conditioning learns about people who selected or were selected into a treatment state. Intervention changes the rule that assigns the treatment state.

## Follow-up probe 1

> What remains intact when we condition that does not remain intact when we intervene?

### Model answer

Conditioning preserves the natural causes of treatment and the associations those causes create. Intervention removes the influence of those causes on treatment by fixing treatment externally.

Suppose severity affects both treatment and outcome:

```text
Severity ──► Treatment ──► Outcome
    └────────────────────► Outcome
```

Among naturally treated patients, severity may be high. Under an intervention assigning treatment, patients of all severity levels can be assigned treatment according to the intervention rule. The treated populations are therefore compositionally different unless assignment was already unconfounded.

## Follow-up probe 2

> When would observation and intervention give the same result?

### Model answer

They coincide when treatment is unconfounded for the causal contrast of interest. In the simplest case:

$$
Y(x) \perp \!\!\! \perp X.
$$

Then:

$$
P(Y\mid X=x)=P(Y\mid do(X=x)).
$$

This can occur under genuine random assignment or when all relevant back-door paths are blocked after conditioning on an adequate covariate set:

$$
P(Y\mid do(X=x))
=
\sum_z P(Y\mid X=x,Z=z)P(Z=z).
$$

The equality is not a purely statistical fact; it depends on causal assumptions.

## Follow-up probe 3

> Why is an observational association not automatically an intervention effect?

### Model answer

Because people who naturally receive treatment may differ from those who do not in ways that also affect the outcome. The observational association combines the treatment effect with the consequences of the assignment mechanism.

For example, if sicker patients are more likely to receive treatment, treated patients may have worse outcomes even when the treatment is beneficial. Conversely, if highly motivated people self-select into a program, the observed association may overstate the program's effect.

## Follow-up probe 4

> Is the intervention distribution always a literal randomized experiment?

### Model answer

No. The intervention distribution is a causal quantity defined by a modified data-generating process. A randomized experiment may identify it, but valid observational designs can also identify it under assumptions. The notation describes the target causal distribution, not the dataset used to estimate it.

## Strong signals

- Says intervention changes the assignment mechanism.
- Explains removal of incoming arrows.
- States conditions under which observation and intervention coincide.
- Does not reduce the distinction to experimental versus observational datasets.

## Warning signs

- Treats the intervention notation as decorative conditioning notation.
- Says intervention merely means a stronger association.
- Cannot explain the role of treatment assignment.

---

# 6. Why Matching Is Used

## Primary question

> If randomization is unavailable, why might we match treated and untreated observations?

## Detailed expected answer

Matching attempts to construct a comparison group whose observed pre-treatment characteristics resemble those of the target treated or untreated group. The purpose is to make the observed outcomes of one group more credible as estimates of the missing counterfactual outcomes of the other.

For the average treatment effect among the treated:

$$
ATT = \mathbb{E}[Y(1)-Y(0)\mid T=1],
$$

the observed component is:

$$
\mathbb{E}[Y(1)\mid T=1],
$$

while the missing counterfactual is:

$$
\mathbb{E}[Y(0)\mid T=1].
$$

Matching uses outcomes from comparable untreated units to estimate that missing quantity.

Matching is therefore not primarily a prediction technique or a way to maximize fit. It is a design technique intended to reduce reliance on outcome-model extrapolation and to improve covariate comparability before estimating effects.

## Follow-up probe 1

> Why might an unmatched comparison or regression be misleading?

### Model answer

If treated and untreated units occupy different regions of the covariate space, a regression may compare unlike units or extrapolate beyond available support. The estimated treatment coefficient can then depend heavily on functional-form assumptions.

Matching can reveal that some treated units have no credible controls and can restrict the analysis to comparisons supported by the data. It does not guarantee unbiasedness, but it can make the comparison more transparent and reduce model dependence.

## Follow-up probe 2

> Which variables should be used for matching?

### Model answer

Variables should be selected using subject-matter and causal knowledge. Good candidates include pre-treatment causes of the outcome, especially variables that also affect treatment assignment. Strong outcome predictors can improve precision and sometimes reduce bias even if their relationship with treatment is modest.

Variables caused by treatment should generally be excluded for a total-effect analysis. Pure instruments may need caution because they predict treatment without predicting the outcome except through treatment; including them can amplify finite-sample instability or sensitivity to unmeasured confounding.

The candidate should not use automated significance testing as the main basis for covariate selection.

## Follow-up probe 3

> Does successful matching make the study equivalent to a randomized experiment?

### Model answer

No. Matching balances observed covariates according to the chosen procedure. It does not guarantee balance on unobserved confounders and does not validate consistency, positivity, no interference, or measurement assumptions.

A more accurate statement is:

> Matching attempts to emulate selected design features of an experiment with respect to observed baseline variables.

## Follow-up probe 4

> Why might strong outcome predictors be useful even if they weakly predict treatment?

### Model answer

Balancing strong outcome predictors reduces residual variation in outcomes and can improve precision. If such variables are imbalanced, they can also contribute to bias in finite samples. The treatment model and the outcome model serve different purposes; a variable need not strongly predict treatment to be substantively important for outcome comparability.

## Strong signals

- Connects matching directly to estimation of missing counterfactual outcomes.
- Treats matching as a design stage.
- Selects variables using causal timing and substantive knowledge.
- Clearly states that unmeasured confounding remains possible.

## Warning signs

- Says matching is required in every observational study.
- Claims matching recreates randomization automatically.
- Chooses variables solely by treatment-prediction accuracy or statistical significance.

---

# 7. Choosing and Justifying a Matching Strategy

## Primary question

> You observe age, income, education, prior health, and geographic location. How would you choose a matching strategy rather than automatically using propensity score matching?

## Detailed expected answer

The candidate should begin by clarifying:

- The estimand.
- The target population.
- Which covariates require exact or near-exact balance.
- The dimensionality and scale of the covariates.
- The degree of overlap.
- Whether matching with replacement is acceptable.
- The cost of discarding observations.
- Whether transparency or sample retention is a priority.

A strong candidate then compares methods.

### Exact matching

Exact matching is attractive when a small number of discrete covariates are critical. For example, matching exactly within region, sex, or baseline disease category can prevent substantively implausible comparisons. It becomes infeasible as the number of variables or categories grows because strata become sparse.

### Coarsened exact matching

Continuous variables are grouped into substantively meaningful intervals and units are matched exactly within the resulting strata. This is transparent and allows the analyst to define acceptable imbalance in advance. The estimand may change when unmatched strata are removed, and conclusions can depend on the coarsening choices.

### Mahalanobis-distance matching

This method standardizes multivariate distances using the covariance structure. It can work well with a modest number of approximately continuous covariates. It becomes less reliable in high dimensions and may give inadequate priority to covariates that are substantively crucial unless combined with exact matching or calipers.

### Nearest-neighbor matching

Each target unit is paired with one or more comparison units minimizing a chosen distance. The analyst must justify whether matching occurs with replacement, how many neighbors are used, how ties are handled, and whether poor matches are rejected.

### Caliper matching

A caliper imposes a maximum acceptable distance. It reduces bias from poor matches but may discard units and redefine the population to which the estimate applies.

### Optimal matching

Optimal matching chooses the set of pairings or matched sets that minimizes total distance globally. It may improve overall match quality relative to greedy nearest-neighbor matching, although it does not eliminate the need for balance diagnostics.

### Full matching

Full matching forms sets containing one or more treated and control units. It can retain more observations and support broad estimands, but the resulting weights and interpretation require care.

### Propensity score matching

This matches units on estimated treatment probability:

$$
e(X)=P(T=1\mid X).
$$

It is useful for reducing a high-dimensional covariate problem to a scalar balancing score. However, closeness in propensity score does not guarantee closeness on every substantively important covariate in finite samples.

## Follow-up probe 1

> What would make exact matching preferable to propensity score matching?

### Model answer

Exact matching is preferable when certain covariates define qualitatively different populations or treatment regimes and cross-category matches would be scientifically implausible. For example, comparing patients across different disease stages or employees across incompatible job families may be unacceptable even if their estimated propensity scores are similar.

Exact matching is also more transparent: the analyst can state that all comparisons occur within specific baseline categories. Propensity scores may hide offsetting differences, where two units have the same score for very different covariate combinations.

## Follow-up probe 2

> When would you impose a caliper?

### Model answer

A caliper is useful when nearest-neighbor matching would otherwise force target units to accept poor controls. It formalizes the principle that no match is better than an implausible match.

The caliper should be justified through substantive similarity, the propensity-score scale, simulation evidence, or established design practice. After imposing it, the analyst must report which units were lost and redefine the estimand for the retained population.

## Follow-up probe 3

> What trade-off is created when matching discards treated units?

### Model answer

Discarding poorly supported treated units can reduce extrapolation and improve internal validity for the remaining units. However, it changes the target population and may move the estimand away from the effect among all treated units.

The resulting estimate may be closer to:

$$
\mathbb{E}[Y(1)-Y(0)\mid T=1, S=1],
$$

where $$S=1$$ denotes inclusion after matching, rather than the original treated-population effect.

There is therefore a trade-off between credible local comparison and broad population coverage.

## Follow-up probe 4

> How would your choice change for the average effect among treated units versus the average effect in the full population?

### Model answer

For the effect among treated units, the matching design naturally uses treated units as anchors and finds controls representing their untreated counterfactuals. Matching with replacement may be useful when control units are scarce in parts of the treated covariate distribution.

For the full-population average effect, the design must represent both treated and untreated target units under both treatment states. Full matching, weighting, subclassification, or doubly robust estimators may be more natural. If overlap is weak, the full-population effect may not be supported even when the effect among treated or overlap units is.

## Strong signals

- Begins with the estimand and overlap rather than the method name.
- Explains how method choice changes retained units and target population.
- Recognizes that balance on key covariates matters more than propensity-score closeness alone.
- Discusses replacement, calipers, and match ratios as design choices.

## Warning signs

- Treats propensity score matching as universally optimal.
- Lists methods without explaining when each is appropriate.
- Ignores the estimand after units are discarded.

---

# 8. Why Propensity Scores Work and Where They Fail

## Primary question

> Why should matching or conditioning on one estimated probability help balance many covariates?

## Detailed expected answer

The propensity score is:

$$
e(X)=P(T=1\mid X).
$$

The key result is that the true propensity score is a balancing score:

$$
T \perp \!\!\! \perp X \mid e(X).
$$

Within strata of the true propensity score, treated and untreated units have the same distribution of observed covariates. Under conditional exchangeability:

$$
\{Y(1),Y(0)\} \perp \!\!\! \perp T \mid X,
$$

conditioning on the propensity score is sufficient for exchangeability:

$$
\{Y(1),Y(0)\} \perp \!\!\! \perp T \mid e(X).
$$

The important property is balance, not merely dimensionality reduction.

## Follow-up probe 1

> Is a highly accurate treatment classifier necessarily a good propensity score model?

### Model answer

No. Predictive accuracy can be high because the model separates treated and untreated units very well, but extreme separation can reveal poor overlap and generate unstable matches or weights. For causal adjustment, the goal is not simply to predict treatment labels; it is to estimate treatment probabilities well enough to achieve covariate balance in the region where comparisons are possible.

A model with slightly lower classification accuracy may produce better balance and more stable weights.

## Follow-up probe 2

> Why can flexible machine learning be useful, and why is it not automatically sufficient?

### Model answer

Flexible models can capture nonlinearities and interactions in treatment assignment, reducing misspecification. However, they can also overfit, produce extreme probabilities, or optimize prediction rather than balance.

Cross-fitting, regularization, trimming, and direct balance assessment can help. Most importantly, no machine-learning method can recover unmeasured confounders or create overlap where no comparable units exist.

## Follow-up probe 3

> What happens if the propensity model is misspecified?

### Model answer

The estimated score may fail to balance observed covariates. Matching or weighting based on it can leave residual confounding. Under inverse probability weighting, misspecification can also create biased and unstable weights.

The analyst should inspect post-adjustment balance directly rather than assuming that a fitted treatment model has achieved its purpose.

## Follow-up probe 4

> Does excellent observed balance prove there is no unmeasured confounding?

### Model answer

No. It shows that the design balanced the measured variables included in the diagnostic. It does not establish balance on omitted or poorly measured causes of treatment and outcome.

Observed balance is necessary evidence that the implemented design behaved as intended, but the no-unmeasured-confounding assumption remains a substantive identification assumption.

## Strong signals

- States the balancing property.
- Distinguishes prediction from causal design.
- Treats balance diagnostics as essential.
- Recognizes the limits of measured covariates and overlap.

## Warning signs

- Says propensity scores work only because one dimension is easier than many.
- Uses classification accuracy as the main validation criterion.
- Claims propensity scores solve hidden confounding.

---

# 9. Alternatives to Propensity Score Matching

## Primary question

> Why might you choose weighting, direct balancing, regression adjustment, or a doubly robust method instead of propensity score matching?

## Detailed expected answer

A strong candidate should say that the method should follow the estimand, overlap, sample structure, and desired bias-variance trade-off.

### Inverse probability weighting

For the average treatment effect, a common weighting scheme is:

$$
w_i = \frac{T_i}{e(X_i)} + \frac{1-T_i}{1-e(X_i)}.
$$

These weights create a pseudo-population in which observed covariates are balanced, assuming a correct propensity model and positivity. Extreme scores generate large weights and high variance.

### Weighting for the effect among treated units

A common scheme is:

$$
w_i = T_i + (1-T_i)\frac{e(X_i)}{1-e(X_i)}.
$$

Treated units retain weight one, while controls are weighted to resemble the treated population.

### Overlap weighting

Typical overlap weights are:

$$
w_i = T_i\bigl(1-e(X_i)\bigr)+(1-T_i)e(X_i).
$$

They emphasize units with meaningful probability of receiving either treatment and de-emphasize units with near-deterministic assignment. This often improves stability but targets the overlap population rather than the original full population.

### Entropy balancing

Entropy balancing chooses weights that directly satisfy moment-balance constraints while remaining close to base weights. It avoids relying exclusively on a treatment-prediction model, but it still requires adequate overlap and no unmeasured confounding.

### Regression adjustment

Regression adjustment models:

$$
\mathbb{E}[Y\mid T,X].
$$

It can be efficient and retain all observations, but estimates may depend heavily on functional-form assumptions, especially in regions with weak overlap.

### Doubly robust estimation

A doubly robust estimator combines a treatment model and an outcome model. Under standard conditions, consistency may be retained if either the propensity model or the outcome model is correctly specified.

A schematic augmented inverse-probability-weighted estimator is:

$$
\widehat{ATE}
=
\frac{1}{n}\sum_{i=1}^{n}
\left[
\widehat{m}_1(X_i)-\widehat{m}_0(X_i)
+
\frac{T_i\left(Y_i-\widehat{m}_1(X_i)\right)}{\widehat{e}(X_i)}
-
\frac{(1-T_i)\left(Y_i-\widehat{m}_0(X_i)\right)}{1-\widehat{e}(X_i)}
\right].
$$

Double robustness does not mean immunity to all misspecification, finite-sample instability, positivity failure, or unmeasured confounding.

## Follow-up probe 1

> Why might weighting be preferable when retaining more units matters?

### Model answer

Weighting can retain all units while changing their contribution to the estimand. This may preserve information and avoid the discrete loss caused by one-to-one matching. It is especially useful when the desired estimand is naturally represented by a weighting function.

However, nominal sample retention can be misleading. A few extreme weights may reduce the effective sample size dramatically, so the analyst must inspect weight concentration and effective information.

## Follow-up probe 2

> Why might matching be preferable for transparency?

### Model answer

Matching can make the actual comparisons concrete. The analyst can inspect which treated units are compared with which controls, identify unsupported units, and explain the design to nontechnical stakeholders.

Weighting can be less intuitive because every unit may contribute fractionally to a synthetic population. Matching may therefore be preferable when auditability and case-level comparability are important, provided the loss of units and estimand change are acceptable.

## Follow-up probe 3

> What population does overlap weighting target?

### Model answer

It targets units with substantial probability of receiving either treatment. Informally, these are units for whom treatment assignment is most uncertain and for whom treated-versus-control comparisons are best supported.

The target is not necessarily the full population or the treated population. Under heterogeneity, the overlap-weighted effect can differ meaningfully from both the full-population and treated-population effects.

## Follow-up probe 4

> What does “doubly robust” mean, and what does it not mean?

### Model answer

It means that, under appropriate regularity and identification conditions, the estimator can remain consistent if either the treatment-assignment model or the outcome-regression model is correctly specified.

It does not mean:

- Both models can be arbitrarily wrong.
- Positivity violations are harmless.
- Unmeasured confounding disappears.
- Finite-sample bias or variance is automatically small.
- The causal estimand is identified without consistency and exchangeability assumptions.

## Strong signals

- Compares methods through estimands and weighting populations.
- Recognizes effective sample size and extreme-weight instability.
- Explains double robustness precisely.
- States that estimator sophistication cannot repair failed identification.

## Warning signs

- Lists fashionable methods without explaining trade-offs.
- Treats weighting as retaining the full information regardless of extreme weights.
- Describes doubly robust estimators as assumption-free.

---

# 10. Diagnosing Matching and Weighting

## Primary question

> After matching or weighting, how do you determine whether the design worked?

## Detailed expected answer

The candidate should focus on balance, overlap, and the induced target population before examining treatment effects.

Useful diagnostics include:

- Standardized mean differences.
- Variance ratios.
- Quantile and tail comparisons.
- Empirical cumulative distribution functions.
- Joint-distribution and interaction balance where substantively relevant.
- Propensity-score or covariate overlap.
- Match distances and caliper violations.
- Weight distributions and maximum weights.
- Effective sample size.
- The fraction and characteristics of discarded units.
- Sensitivity to reasonable alternative design choices.

A standardized mean difference for a continuous covariate can be represented as:

$$
SMD = \frac{\overline{X}_1-\overline{X}_0}{s_{pooled}}.
$$

For weighted data, the means and variances should be calculated using the analysis weights.

The candidate should explain that balance diagnostics evaluate the design rather than the estimated treatment effect. A statistically significant treatment effect is not evidence that matching worked.

## Follow-up probe 1

> Why is a nonsignificant covariate difference not proof of balance?

### Model answer

A hypothesis test combines imbalance magnitude with sample size. In a small sample, a large and substantively important imbalance may be nonsignificant. In a large sample, a trivial imbalance may be statistically significant.

Balance diagnostics should therefore emphasize standardized differences and distributional discrepancies rather than relying on tests of the null hypothesis of equal means.

## Follow-up probe 2

> Should the outcome be examined while refining the matching design?

### Model answer

Ideally, the design should be developed without using outcomes to choose specifications, mirroring the separation between design and analysis in an experiment. Looking repeatedly at outcomes while tuning the match creates opportunities to select a design that produces a preferred treatment effect.

Outcome-blind design is not always operationally perfect, but the principle reduces researcher degrees of freedom and strengthens credibility.

## Follow-up probe 3

> What do extreme weights tell you?

### Model answer

Extreme weights indicate that some observed units are being asked to represent many units in a target pseudo-population. This often arises from propensity scores near zero or one and signals limited overlap, model misspecification, or both.

Extreme weights increase variance, make estimates sensitive to a small number of observations, and reduce effective sample size. Stabilization or truncation may improve precision but changes the estimator and can introduce bias; those choices must be reported and interpreted.

## Follow-up probe 4

> What if means are balanced but tails are not?

### Model answer

Mean balance can hide important distributional differences. If treatment effects or outcomes are nonlinear in a covariate, tail imbalance can leave residual confounding even when means match.

The analyst should examine quantiles, empirical distributions, transformations, interactions, and substantively important thresholds. Balance should be evaluated at the level needed to support the outcome relationship, not only through first moments.

## Strong signals

- Separates design diagnostics from effect estimation.
- Checks full distributions and effective sample size.
- Reports discarded units and estimand implications.
- Treats observed balance as necessary but not sufficient.

## Warning signs

- Declares success based on a treatment-effect p-value.
- Uses only propensity-score histograms.
- Checks only raw mean differences.

---

# 11. Overlap, Positivity, and Unsupported Comparisons

## Primary question

> Nearly every high-risk patient receives treatment, while nearly every low-risk patient does not. Can matching or modeling recover the full-population causal effect?

## Detailed expected answer

Not necessarily. The design lacks empirical overlap. For some covariate profiles, one treatment state is absent or extremely rare.

The positivity condition requires:

$$
0 < P(T=1\mid X=x) < 1
$$

for covariate values relevant to the target population.

When this condition fails, the data do not reveal what happens under both treatment states for those covariate profiles. A flexible model can extrapolate, but the resulting estimate depends on unverifiable functional-form assumptions rather than observed comparison.

Appropriate responses may include:

- Restricting the target population to the region of common support.
- Trimming unsupported observations.
- Changing from a full-population estimand to an overlap-population estimand.
- Collecting data in missing treatment-covariate regions.
- Reporting that the desired effect is not identified from the available data.

## Follow-up probe 1

> Is poor overlap a modeling problem or a design problem?

### Model answer

It is fundamentally a support and design problem. A model can produce numerical predictions in unsupported regions, but it cannot create empirical information about outcomes under an unobserved treatment state.

Modeling choices affect how extrapolation is performed, but they do not remove the underlying lack of comparison.

## Follow-up probe 2

> What happens under inverse probability weighting when treatment probabilities approach zero or one?

### Model answer

Weights contain inverse probabilities, so they can become extremely large:

$$
\frac{1}{e(X)}
$$

for treated units and:

$$
\frac{1}{1-e(X)}
$$

for controls.

This creates high variance, sensitivity to a few units, and small effective sample size. It can also magnify the consequences of propensity-score estimation error.

## Follow-up probe 3

> How does trimming affect interpretation?

### Model answer

Trimming may improve internal validity by removing units without credible comparisons, but it changes the target population. The estimate applies to units satisfying the trimming rule rather than to the original population.

The analyst should explicitly describe the retained population and avoid labeling the result as the original full-population effect unless additional transport assumptions are supplied.

## Strong signals

- Is willing to say that the available data cannot answer the original question.
- Distinguishes extrapolation from identification.
- Redefines the target population after trimming.

## Warning signs

- Claims a more flexible model always solves non-overlap.
- Trims silently while preserving the original estimand label.
- Ignores extreme-weight sensitivity.

---

# 12. Treatment-Effect Heterogeneity and Estimands

## Primary question

> Suppose treatment effects vary substantially across people. What exactly is the estimator estimating?

## Detailed expected answer

The candidate should respond that there is no single answer without specifying the estimand, design, estimator, and target population.

Common estimands include:

### Average treatment effect

$$
ATE = \mathbb{E}[Y(1)-Y(0)].
$$

### Average treatment effect among treated units

$$
ATT = \mathbb{E}[Y(1)-Y(0)\mid T=1].
$$

### Average treatment effect among untreated units

$$
ATC = \mathbb{E}[Y(1)-Y(0)\mid T=0].
$$

### Conditional average treatment effect

$$
CATE(x)=\mathbb{E}[Y(1)-Y(0)\mid X=x].
$$

### Local average treatment effect

Under instrumental-variables assumptions, the local average treatment effect is:

$$
LATE = \mathbb{E}[Y(1)-Y(0)\mid \text{complier}].
$$

Different matching, weighting, regression, and instrumental-variable procedures place different weights on heterogeneous unit-level effects. Therefore, two valid methods can estimate different causal quantities.

## Follow-up probe 1

> Why might the effect among treated units differ from the full-population average effect?

### Model answer

The treated population may differ in baseline risk, treatment responsiveness, preferences, access, or institutional context. If those factors modify treatment effects, the average effect among treated units will differ from the average across everyone.

For example, a medical treatment may be assigned disproportionately to severe patients, and severe patients may receive greater or smaller benefit than mild patients.

## Follow-up probe 2

> Which estimand does nearest-neighbor matching with treated units as anchors naturally target?

### Model answer

It naturally targets the effect among the matched treated units. If every treated unit is retained and matched adequately, this approximates the treated-population effect. If treated units are discarded, the target becomes the effect among the retained treated units, not necessarily all treated units.

## Follow-up probe 3

> Why does an instrumental-variable estimate generally not identify the full-population average effect?

### Model answer

Under the standard monotonicity framework, the instrument changes treatment only for compliers. The ratio estimator therefore captures the average treatment effect for units whose treatment status responds to the instrument, not for always-takers, never-takers, or necessarily the full population.

The instrumental-variable estimand is:

$$
\frac{\mathbb{E}[Y\mid Z=1]-\mathbb{E}[Y\mid Z=0]}
{\mathbb{E}[T\mid Z=1]-\mathbb{E}[T\mid Z=0]},
$$

which is interpreted as the complier average causal effect under the required assumptions.

## Follow-up probe 4

> When does heterogeneity become an external-validity problem?

### Model answer

When the distribution of effect modifiers differs between the study population and the decision population. Even a perfectly identified study effect may not transport if the target population has different baseline characteristics, institutional conditions, treatment versions, or compliance patterns that alter treatment response.

## Strong signals

- Immediately asks which estimand and population are intended.
- Understands that methods induce different weighting of heterogeneous effects.
- Does not interpret a local effect as universal.

## Warning signs

- Assumes one constant treatment effect without justification.
- Uses the labels interchangeably.
- Ignores population changes after trimming or matching.

---

# 13. Selection Bias

## Primary question

> Who enters the analytic sample, and how could that create bias?

## Detailed expected answer

Selection bias occurs when inclusion in the observed or analyzed sample depends on variables connected to treatment and outcome. Selection can create a nonrepresentative population, induce collider bias, or alter the causal contrast.

Examples include:

- Studying only hired workers when hiring depends on qualifications and connections.
- Studying only hospitalized patients when hospitalization depends on exposure and disease severity.
- Complete-case analysis when missingness depends on treatment and prognosis.
- Attrition caused by treatment side effects and health status.
- Conditioning on program completion when completion is affected by treatment and motivation.
- Survivorship analysis when survival depends on exposure and underlying resilience.

The candidate should distinguish:

1. Selection into treatment.
2. Selection into the initial study sample.
3. Selection into the final analytic sample.
4. Selection into having an observed outcome.

Each can require a different correction or estimand.

## Follow-up probe 1

> How is sample selection related to collider bias?

### Model answer

If sample inclusion is a common effect of treatment and an outcome cause, conditioning on inclusion opens a noncausal path.

For example:

```text
Treatment ──► Included ◄── Prognosis ──► Outcome
```

Analyzing only included units induces association between treatment and prognosis, even if they were unrelated before selection. This biases the treatment-outcome comparison.

## Follow-up probe 2

> What is the difference between selection into treatment and selection into the sample?

### Model answer

Selection into treatment concerns why units receive one treatment rather than another and is typically addressed through exchangeability or an identification design.

Selection into the sample concerns why some units are observed or retained. It affects which population is represented and can create additional bias even if treatment assignment was initially valid.

A randomized trial can have valid treatment assignment but biased complete-case results if attrition depends jointly on treatment and potential outcomes.

## Follow-up probe 3

> When can inverse probability-of-selection weighting help?

### Model answer

It can help when the probability of being observed or retained can be modeled using observed variables sufficient to make selection conditionally independent of the relevant potential outcomes.

If:

$$
S \perp \!\!\! \perp Y(t) \mid T,X,
$$

then weights based on:

$$
\frac{1}{P(S=1\mid T,X)}
$$

can reweight observed units to represent the target population. This requires correct modeling, positivity of observation, and no unmeasured causes of both selection and outcome after conditioning.

## Follow-up probe 4

> Can a large sample eliminate selection bias?

### Model answer

No. A large selected sample may estimate the wrong population quantity with great precision. Sample size reduces random error but does not correct systematic distortion caused by inclusion mechanisms.

## Strong signals

- Separates treatment assignment from sample inclusion and outcome observation.
- Recognizes selection as a graphical and estimand problem.
- States assumptions required for selection weighting.

## Warning signs

- Uses selection bias as a vague synonym for confounding.
- Assumes representativeness follows from sample size.
- Ignores post-treatment attrition.

---

# 14. Identification Assumptions Across Econometric Designs

## Primary question

> What assumptions identify the causal effect in a study, and which of those assumptions can actually be tested?

## Detailed expected answer

The candidate should first state that identification comes from assumptions connecting observed data to potential outcomes. Estimation begins only after the estimand is identified.

They should distinguish fully testable design implications from fundamentally untestable counterfactual claims.

## Observational adjustment, matching, or weighting

Typical assumptions include:

### Conditional exchangeability

$$
\{Y(1),Y(0)\} \perp \!\!\! \perp T \mid X.
$$

### Positivity

$$
0<P(T=1\mid X=x)<1.
$$

### Consistency

If a unit receives treatment level $$t$$, its observed outcome equals the corresponding potential outcome:

$$
T=t \implies Y=Y(t).
$$

### No relevant interference

A unit's potential outcome is indexed adequately by its own treatment rather than by the complete treatment vector of all units.

Observed balance and overlap can be examined, but conditional exchangeability cannot be proven from observed data alone.

## Instrumental variables

Typical assumptions include:

### Relevance

$$
P(T=1\mid Z=1) \neq P(T=1\mid Z=0).
$$

### Independence

The instrument is as-if randomly assigned with respect to potential outcomes and treatment response types.

### Exclusion restriction

The instrument affects the outcome only through treatment.

### Monotonicity

The instrument does not cause some units to move into treatment while causing others to move out in the opposite direction.

Relevance is empirically assessable. Independence, exclusion, and monotonicity are primarily substantive assumptions, though they can have testable implications in richer settings.

## Difference-in-differences

A central assumption is parallel trends in untreated potential outcomes:

$$
\mathbb{E}[Y_t(0)-Y_{t-1}(0)\mid T=1]
=
\mathbb{E}[Y_t(0)-Y_{t-1}(0)\mid T=0].
$$

Additional concerns include:

- No anticipation.
- Stable group composition.
- No differential contemporaneous shocks.
- Appropriate treatment of staggered adoption and heterogeneous effects.
- No treatment-induced changes in outcome measurement.

Pre-treatment trends can provide evidence, but failure to reject differences does not prove future counterfactual parallel trends.

## Regression discontinuity

Typical assumptions include:

- Potential outcomes vary continuously at the assignment threshold.
- Units cannot precisely manipulate assignment around the threshold.
- Other determinants do not jump discontinuously at the same threshold.
- The analysis estimates a local effect near the cutoff.

## Follow-up probe 1

> What evidence would increase confidence in an untestable assumption?

### Model answer

Useful evidence includes institutional knowledge of the assignment mechanism, balance on predetermined covariates, absence of discontinuities in placebo outcomes, stable pre-treatment trends, robustness to bandwidths or specifications, replication in settings with different confounding structures, and sensitivity analyses showing that an implausibly strong hidden factor would be required to overturn the result.

Such evidence can make an assumption more plausible, but it does not logically prove the counterfactual claim.

## Follow-up probe 2

> What would falsify an identification strategy?

### Model answer

The answer depends on the strategy:

- Strong imbalance in predetermined variables may undermine as-if random assignment.
- A jump in a pre-treatment outcome at a regression-discontinuity cutoff undermines continuity.
- Effects appearing before treatment undermine no-anticipation or parallel-trends stories.
- An instrument directly changing the outcome through another channel undermines exclusion.
- Severe lack of overlap undermines adjustment-based identification for the stated population.

A strong candidate proposes tests tied to specific assumptions rather than generic robustness checks.

## Follow-up probe 3

> What is the difference between failing to reject an assumption and validating it?

### Model answer

Failure to reject may reflect limited power, noisy measurement, a short pre-period, or an insensitive test. It means the observed data did not provide strong evidence against a particular implication. It does not prove the full identifying assumption, which often concerns unobserved counterfactual outcomes.

## Follow-up probe 4

> Why should the candidate state assumptions before discussing standard errors or estimators?

### Model answer

Standard errors describe sampling uncertainty around an estimand under the model and design. They do not address whether the estimand corresponds to the desired causal effect. An extremely precise estimate can still be causally invalid if identification assumptions fail.

## Strong signals

- States assumptions in substantive and formal terms.
- Distinguishes testable implications from untestable assumptions.
- Tailors falsification tests to the design.
- Separates identification from estimation and inference.

## Warning signs

- Claims pre-trend tests prove parallel trends.
- Claims observed balance proves no hidden confounding.
- Cannot explain exclusion in substantive terms.

---

# 15. Measurement Error, Treatment Definition, and Consistency

## Primary question

> What happens if treatment, outcome, or confounders are measured poorly?

## Detailed expected answer

The consequences depend on what is mismeasured, how it is mismeasured, and whether measurement depends on treatment, outcome, or other variables.

### Treatment measurement error

Misclassification can mix treatment groups and distort the treatment contrast. Nondifferential misclassification does not always produce simple attenuation in nonlinear or heterogeneous settings. If treatment records are more accurate for severe cases, the error can be differential and bias can move in either direction.

### Outcome measurement error

Classical random outcome noise may reduce precision, but differential outcome assessment can create bias. For example, managers who know an employee completed a program may rate performance more favorably even without a true productivity change.

### Confounder measurement error

A noisy confounder may leave residual confounding after adjustment. Conditioning on an imperfect proxy does not generally make treatment exchangeable.

### Treatment-version ambiguity

Consistency requires a well-defined treatment. If the label “training program” contains materially different curricula, durations, instructors, or compliance levels, then the potential outcome under treatment may not be a single coherent quantity.

## Follow-up probe 1

> Why does measurement error in a confounder not merely reduce precision?

### Model answer

Because confounder adjustment aims to block a causal path. If the measured variable only partially captures the true confounder, the path remains partially open. Treated and untreated units can still differ in the unmeasured component of the confounder, producing residual bias.

## Follow-up probe 2

> What if treatment status is more accurately recorded for people with severe outcomes?

### Model answer

Then treatment misclassification depends on the outcome or its causes. This differential measurement can induce or distort treatment-outcome associations. Standard correction formulas based on nondifferential error would be inappropriate.

The analyst would need validation data, repeated measures, an explicit measurement model, or a sensitivity analysis reflecting differential recording.

## Follow-up probe 3

> How would validation data help?

### Model answer

A validation subsample with higher-quality measurements can estimate sensitivity, specificity, reliability, or calibration relationships. These can be incorporated through probabilistic bias analysis, latent-variable models, regression calibration, multiple imputation, or corrected likelihood methods.

Validation data are most useful when they are themselves representative of the measurement process in the analytic population.

## Follow-up probe 4

> Why is treatment definition part of causal identification rather than mere data cleaning?

### Model answer

A causal effect compares potential outcomes under specified interventions. If the treatment is not well defined, it is unclear which intervention is being contrasted. Different versions may have different effects, and observed variation in treatment implementation may violate the consistency assumption.

## Strong signals

- Avoids saying all measurement error attenuates effects toward zero.
- Connects confounder error to residual confounding.
- Recognizes treatment-version ambiguity.
- Proposes validation or sensitivity approaches.

## Warning signs

- Treats proxies as equivalent to true confounders.
- Ignores differential measurement.
- Views consistency as purely notational.

---

# 16. Model Dependence and Specification Sensitivity

## Primary question

> Two defensible specifications produce meaningfully different causal estimates. What does that tell you?

## Detailed expected answer

It indicates that the estimated effect may be sensitive to modeling choices, support restrictions, covariate adjustment, functional form, or implicit weighting of heterogeneous effects.

Possible explanations include:

- Weak overlap makes estimates depend on extrapolation.
- Different models approximate nonlinear response surfaces differently.
- Interaction terms change adjustment for effect modification or confounding.
- Different trimming rules change the target population.
- Weighting and matching schemes target different estimands.
- Outliers or influential observations drive one specification.
- Researcher degrees of freedom permit selective reporting.

The candidate should investigate why estimates differ rather than selecting the preferred result.

## Follow-up probe 1

> Is specification stability proof of causal validity?

### Model answer

No. Many specifications can reproduce the same biased estimate if they share the same invalid identification assumption, omitted confounder, selection mechanism, or measurement error. Stability is useful evidence about model dependence but does not establish identification.

## Follow-up probe 2

> Why can machine learning improve nuisance estimation without fixing identification?

### Model answer

Machine learning can estimate complex treatment and outcome relationships more flexibly. This can reduce functional-form error in nuisance models and improve efficiency.

However, it cannot observe missing confounders, correct a fundamentally invalid instrument, create untreated observations where positivity fails, or define an incoherent treatment. Identification is supplied by design and assumptions, not predictive flexibility.

## Follow-up probe 3

> What is the danger of choosing specifications based on the desired treatment effect?

### Model answer

It turns specification search into an implicit multiple-testing or optimization process. Reported standard errors do not account for the selection procedure, and the estimate may reflect researcher preference rather than a prespecified design.

Pre-analysis plans, blinded design, specification curves, multiverse analyses, and transparent reporting can reduce or reveal this risk.

## Strong signals

- Separates identification, estimation, and robustness.
- Treats instability as diagnostic evidence.
- Recognizes estimand changes across methods.
- Mentions researcher degrees of freedom.

## Warning signs

- Selects the model with the smallest p-value.
- Assumes flexible prediction equals causal validity.
- Treats robustness checks as ceremonial.

---

# 17. Interference, Spillovers, and Equilibrium Effects

## Primary question

> What if treating one person changes another person's outcome?

## Detailed expected answer

Then the standard no-interference version of the stable-unit-treatment-value assumption is violated. A unit's outcome may depend on the complete treatment allocation rather than only its own treatment.

Instead of potential outcomes indexed only by individual treatment:

$$
Y_i(t_i),
$$

we may need potential outcomes indexed by the treatment vector:

$$
Y_i(\mathbf{t}).
$$

Examples include:

- Vaccination reducing infection risk for untreated people.
- Job-training programs changing competition for local jobs.
- Educational interventions affecting classmates.
- Information or behavior spreading through networks.
- Policies changing market prices and wages.

The appropriate estimand may distinguish direct, indirect, total, and overall effects and may depend on treatment saturation or network exposure.

## Follow-up probe 1

> How would cluster randomization help?

### Model answer

If interference occurs mainly within clusters, randomizing clusters can prevent treatment and control units from directly contaminating each other within the same cluster. It can identify effects of assigning entire clusters to treatment under assumptions about between-cluster interference.

It does not solve interference that crosses cluster boundaries, and it changes the estimand from an individual assignment effect to a cluster-policy effect.

## Follow-up probe 2

> What is the difference between a direct effect and a spillover effect?

### Model answer

A direct effect compares a unit's outcomes under different own-treatment states while holding the surrounding treatment exposure fixed.

A spillover effect compares outcomes under different treatment exposure among other units while holding the unit's own treatment fixed.

The exact definitions depend on the exposure mapping and design.

## Follow-up probe 3

> Could scaling a policy change the sign or size of the effect?

### Model answer

Yes. A small job-training program might benefit participants when they compete with mostly untreated workers, but a universal program could saturate the credential or increase labor-market competition. A subsidy may raise supply prices when implemented broadly. These equilibrium responses can make scaled policy effects differ from partial-equilibrium study effects.

## Follow-up probe 4

> Do clustered standard errors solve interference?

### Model answer

No. Clustered standard errors adjust an inference calculation for correlated residuals. They do not redefine the potential outcomes, remove treatment contamination, or identify direct and spillover effects. Interference is an estimand and design problem, not merely a variance-estimation problem.

## Strong signals

- Redefines potential outcomes or exposure appropriately.
- Distinguishes direct and spillover effects.
- Recognizes equilibrium and saturation effects.
- Rejects the idea that clustered errors solve the causal problem.

## Warning signs

- Treats interference solely as correlated errors.
- Assumes individual study effects scale mechanically to policy effects.

---

# 18. External Validity and Transportability

## Primary question

> Suppose you fully believe a study's internal causal estimate. Why might you still decline to use it for a policy decision?

## Detailed expected answer

The study may identify a valid effect for a population, time, institution, treatment version, or implementation environment different from the policy target.

Potential transport problems include:

- Different distributions of effect modifiers.
- Different baseline risks.
- Different treatment adherence or take-up.
- Different provider quality or institutional capacity.
- Different market responses at scale.
- Different treatment intensity or implementation fidelity.
- Eligibility or selection rules that produce a different study population.

Internal validity asks whether the effect is credible for the study population and design. External validity asks whether that effect applies to the target population and intervention.

## Follow-up probe 1

> What information would you need to transport an estimate?

### Model answer

The analyst needs information about variables that modify treatment effects and how their distributions differ between the study and target populations. They also need evidence that the treatment versions and relevant structural relationships are comparable.

Under suitable assumptions, sampling or transport weights may reweight the study population to the target population. However, unmeasured effect modifiers and different institutional mechanisms can prevent credible transport.

## Follow-up probe 2

> Why might a small pilot differ from a national rollout?

### Model answer

Pilots often receive more resources, stronger implementation teams, more motivated participants, and less market saturation. At scale, capacity constraints, heterogeneous providers, behavioral adaptation, price changes, spillovers, and political responses can change effects.

The pilot may identify an efficacy effect under favorable implementation rather than an effectiveness or equilibrium effect under scale.

## Follow-up probe 3

> How do sample selection and treatment-effect heterogeneity interact?

### Model answer

If study participation depends on variables that also modify treatment effects, the study average effect can differ from the target average even when the study effect is internally valid. Representativeness of outcomes or covariates alone is not enough; what matters is representativeness with respect to effect modification and implementation.

## Strong signals

- Separates internal validity from transportability.
- Connects transport to effect modifiers and implementation.
- Recognizes scale and equilibrium effects.

## Warning signs

- Believes randomization guarantees universal applicability.
- Treats demographic representativeness alone as sufficient.

---

# 19. Negative Controls, Placebos, and Sensitivity Analysis

## Primary question

> How would you investigate whether unmeasured confounding or another design failure is driving the result?

## Detailed expected answer

No single diagnostic generally proves the absence of hidden bias. A strong candidate should propose checks tied to specific causal threats.

Possible tools include:

- Negative-control outcomes that treatment should not plausibly affect.
- Negative-control exposures that should not causally affect the outcome.
- Placebo treatment dates.
- Event-study leads.
- Falsification populations.
- Alternative comparison groups.
- Sensitivity analysis for unmeasured confounding.
- Bounds under specified violations.
- Replication across settings with different confounding structures.
- Triangulation across distinct identification strategies.

## Follow-up probe 1

> What would a successful placebo test tell you?

### Model answer

It would show that one particular falsification implication is consistent with the design. For example, absence of an effect before treatment reduces concern about certain anticipatory or preexisting trend explanations.

It increases credibility with respect to the failure mode targeted by the placebo.

## Follow-up probe 2

> What would a successful placebo test not tell you?

### Model answer

It would not prove the absence of all confounding, selection, measurement error, or misspecification. A confounder may affect the true outcome but not the placebo outcome. A placebo can have low power. The tested period or population may not reveal the relevant violation.

## Follow-up probe 3

> How would you explain a sensitivity analysis to a nontechnical stakeholder?

### Model answer

A useful explanation is:

> The estimate assumes we measured all important factors that jointly affect treatment and outcome. The sensitivity analysis asks how strong an omitted factor would need to be to explain away the result. It does not prove that no such factor exists, but it tells us whether a weak, moderate, or implausibly strong hidden factor would be required.

## Follow-up probe 4

> Why is triangulation across designs useful?

### Model answer

Different designs rely on different assumptions and may be vulnerable to different biases. If adjustment, an instrumental-variable design, a discontinuity, and a natural experiment yield similar conclusions, it becomes harder for one shared failure mode to explain all results.

Agreement is not proof, especially if the designs share data or assumptions, but well-chosen triangulation can strengthen causal credibility.

## Strong signals

- Links each check to a specific threat.
- Treats placebos as evidence, not proof.
- Interprets sensitivity magnitudes substantively.

## Warning signs

- Claims one negative control validates the study.
- Lists robustness checks without specifying what they diagnose.

---

# 20. Integrative Referee Exercise

## Primary prompt

> A paper claims that a policy increased earnings by twelve percent. You do not yet have the code. Walk me through the questions you would ask before believing the claim.

## Detailed expected answer

A strong candidate should begin with the causal question and design, not with statistical significance.

### Step 1: Define the causal contrast

The candidate should ask:

- What exactly is the policy exposure?
- What is the comparison treatment state?
- What outcome and time horizon are used?
- What population is targeted?
- Is the estimand a full-population, treated-population, local, or overlap effect?
- Are there multiple versions or intensities of the policy?

### Step 2: Understand assignment

They should ask:

- Why did some units receive the policy and others not?
- What institution or rule generated the variation?
- Could units anticipate, manipulate, or self-select into treatment?
- Is treatment timing related to prior outcome trends?

### Step 3: State identification assumptions

They should require the authors to state the assumptions in substantive terms. Examples include no unmeasured confounding, parallel trends, exclusion, continuity, or as-if random timing.

### Step 4: Examine sample construction and selection

They should ask:

- Who enters the dataset?
- Who is excluded?
- Is outcome observation complete?
- Is there selective attrition?
- Does the analysis condition on a post-treatment variable?
- Does sample inclusion create a collider?

### Step 5: Assess support and comparison quality

They should ask:

- Are treated and comparison units similar before treatment?
- Is the estimate driven by extrapolation?
- Are weights extreme?
- Which units are discarded?
- What population remains after design restrictions?

### Step 6: Evaluate measurement

They should ask:

- Is treatment exposure measured accurately?
- Are earnings observed consistently across groups?
- Could policy exposure affect reporting, labor-force participation, or data inclusion?
- Does the earnings measure include zeros and missing employment spells appropriately?

### Step 7: Consider heterogeneity

They should ask:

- Does the effect vary by baseline earnings, geography, age, industry, or treatment intensity?
- Which heterogeneous effects receive the greatest estimator weight?
- Is the reported average meaningful for the policy decision?

### Step 8: Examine falsification and robustness

They should ask:

- Are there pre-treatment effects?
- Are placebo outcomes affected?
- Are results robust to reasonable bandwidths, windows, covariates, and comparison groups?
- Do alternative designs produce consistent conclusions?
- Are results sensitive to hidden-bias assumptions?

### Step 9: Consider interference and equilibrium

They should ask whether treated units affect untreated units through migration, wages, prices, labor-market competition, or employer behavior. A policy can change the untreated comparison group's outcomes and thereby alter the estimand.

### Step 10: Assess transportability

They should ask whether the study population, period, and implementation match the intended policy context. A credible local effect may not justify a national rollout.

## Follow-up probe 1

> What would you ask before looking at the regression table?

### Model answer

I would ask how treatment was assigned, what the counterfactual comparison is, which units support that comparison, and what assumptions connect the observed contrast to the causal estimand. Regression output is meaningful only after the design is credible.

## Follow-up probe 2

> Suppose the estimate is extremely precise. Does that change your identification concerns?

### Model answer

No. Precision narrows sampling uncertainty around the estimated quantity. It does not show that the quantity equals the desired causal effect. A precisely estimated biased association remains biased.

## Follow-up probe 3

> What answer would make you conclude that the paper's question is not supported by its data?

### Model answer

Examples include no credible untreated comparisons for the treated population, treatment assignment driven by unmeasured prognosis with no valid design, an implausible instrument exclusion restriction, treatment and outcome measured only after selective survival, or a policy applied universally with no source of counterfactual variation.

A strong researcher should be willing to narrow the population, change the estimand, or state that the desired effect is not identified.

## Strong signals

- Starts with the assignment mechanism and estimand.
- Organizes criticism around identification assumptions.
- Separates internal validity, heterogeneity, and transportability.
- Is willing to reject unsupported causal claims.

## Warning signs

- Begins with significance stars, model fit, or sample size.
- Equates many robustness regressions with identification.
- Never asks how treatment was assigned.

---

# 21. Continuous Applied Interview Dialogue

## Case setup

A company introduces an optional professional-development program. Employees who enroll subsequently receive higher performance ratings than employees who do not enroll.

## Question 1

> Can we conclude that the program improved performance?

### Expected answer

No. Enrollment is voluntary, so participants may differ from nonparticipants in motivation, prior performance, manager support, role, workload, available time, or career ambition. These variables may affect both enrollment and future ratings. The observed difference combines any program effect with selection into participation.

## Follow-up

> What precise causal quantity might the company care about?

### Follow-up answer

One possible target is the average effect of offering or assigning the program to all eligible employees:

$$
\mathbb{E}[Y(1)-Y(0)].
$$

Another is the average effect among employees who actually enrolled:

$$
\mathbb{E}[Y(1)-Y(0)\mid T=1].
$$

These are different when program effects or selection differ across employees. The company should specify whether it is deciding about universal rollout, targeted enrollment, or an offer rather than actual participation.

## Question 2

> What is the missing counterfactual?

### Expected answer

For each participating employee, it is the performance rating that employee would have received during the same period without participating. For a treated-population effect, the missing group-level quantity is:

$$
\mathbb{E}[Y(0)\mid T=1].
$$

## Follow-up

> Why can the average rating of nonparticipants fail to estimate that quantity?

### Follow-up answer

Nonparticipants may have different baseline performance, motivation, managers, roles, or opportunities. Their observed untreated outcomes therefore need not represent what the participants would have experienced without the program.

## Question 3

> Why would random assignment help?

### Expected answer

Random assignment would make program assignment independent of potential performance outcomes in expectation. Nonassigned employees could then estimate the missing untreated outcomes for assigned employees. Assignment would identify an intention-to-treat effect even if some assigned employees did not attend.

## Follow-up

> What if employees assigned to the program do not attend?

### Follow-up answer

The difference by assignment identifies the effect of offering or assigning the program. Estimating the effect of actual attendance requires additional assumptions. Assignment might serve as an instrument for attendance if relevance, exclusion, independence, and monotonicity are plausible, yielding a local effect among employees whose attendance responds to assignment.

## Question 4

> Suppose randomization is impossible. Why match employees?

### Expected answer

Matching would create a set of nonparticipants resembling participants on relevant pre-program characteristics. Their outcomes would then provide a more credible estimate of participants' missing untreated outcomes, under no unmeasured confounding and adequate overlap.

## Follow-up

> Is matching required, or could another design be better?

### Follow-up answer

Matching is not inherently required. Weighting, regression adjustment, entropy balancing, a phased rollout, an eligibility cutoff, manager-level encouragement, or a difference-in-differences design may be more appropriate depending on assignment, timing, overlap, and the target estimand. The method should follow the source of credible variation.

## Question 5

> Which variables would you match on?

### Expected answer

Pre-program variables affecting enrollment and performance, such as prior ratings, tenure, role, business unit, manager, workload, promotion track, baseline training history, schedule flexibility, and relevant career indicators.

The candidate should avoid variables caused by enrollment, such as post-enrollment project assignment, attendance completion, or manager perceptions formed after program participation.

## Follow-up

> Would you match on manager?

### Follow-up answer

Often yes, if managers influence both program access and performance ratings. Exact matching or fixed strata within manager may be valuable. However, if treatment occurs at the manager level or spillovers occur within teams, manager matching may remove relevant variation or require a clustered design. The answer depends on the assignment mechanism and estimand.

## Question 6

> Would you automatically use propensity score matching?

### Expected answer

No. I would first inspect sample size, covariate dimensionality, overlap, the need for exact matching on manager or role, the estimand, and the cost of discarding units. Coarsened exact matching, Mahalanobis matching within exact strata, full matching, overlap weighting, entropy balancing, or doubly robust estimation may be more suitable.

## Follow-up

> What would make propensity score matching unattractive here?

### Follow-up answer

It would be unattractive if enrollment is nearly deterministic for some roles, if exact manager or job-family comparability is essential, if the sample is small, if propensity-score matches conceal large covariate differences, or if many participants would be discarded. It may also be less attractive when weighting can target the desired population more directly and retain better-supported information.

## Question 7

> How would you assess the design after matching or weighting?

### Expected answer

I would examine standardized differences, distributions, prior rating trajectories, manager and role composition, overlap, match distances, discarded units, weight concentration, and effective sample size. I would define the resulting target population before examining performance outcomes.

## Follow-up

> What if prior mean ratings are balanced but rating trends are not?

### Follow-up answer

Different pre-program trends suggest that a single baseline level may not make groups comparable. I would balance or model prior trajectories, reconsider the design, or use a longitudinal identification strategy if its assumptions are plausible. Mean-level balance alone would be insufficient.

## Question 8

The company analyzes only employees promoted during the year. Promotion depends on both program participation and managerial sponsorship.

> What problem does this create?

### Expected answer

Promotion is a common effect of participation and sponsorship. Restricting to promoted employees conditions on a collider and induces association between participation and sponsorship. Since sponsorship may also affect ratings or career outcomes, the restriction can create a spurious treatment-outcome path.

## Follow-up

> Could controlling for sponsorship repair the problem?

### Follow-up answer

Not automatically. If sponsorship is fully observed and correctly placed in the causal structure, conditioning on it might block part of the opened path, but selection on promotion may involve other unmeasured causes. The cleaner solution is often to avoid conditioning on the post-treatment selection variable or to define a specific principal-stratification or selection estimand.

## Question 9

> What is the difference between observing employees who enrolled and forcing otherwise eligible employees to enroll?

### Expected answer

Observed enrollees retain the selection mechanism: motivation, manager support, ambition, and available time influenced enrollment. An intervention sets enrollment externally and breaks those incoming causes of treatment assignment. Therefore:

$$
P(Y\mid T=1)
$$

need not equal:

$$
P(Y\mid do(T=1)).
$$

## Follow-up

> When might they be equal?

### Follow-up answer

They may be equal under randomized assignment or after adequate adjustment if enrollment is conditionally exchangeable given measured baseline covariates, positivity holds, the treatment is well defined, and interference is absent or properly modeled.

## Question 10

> Program effects are large for junior employees and zero for senior employees. What does the reported estimate represent?

### Expected answer

It depends on the estimator's weighting of junior and senior employees. A treated-population match represents the composition of enrolled employees. A full-population estimator represents the eligible workforce. Overlap weighting emphasizes employees with uncertain enrollment. The reported average must be interpreted relative to those weights.

## Follow-up

> Could two correct analyses report different effects?

### Follow-up answer

Yes. If one estimates the effect among enrollees and another estimates the effect in the overlap population, heterogeneous effects can produce different results even when both analyses are valid. The apparent disagreement may be an estimand difference rather than an error.

## Question 11

> Nearly all high-performing employees enroll and nearly no low-performing employees enroll. What then?

### Expected answer

The study has poor overlap. The untreated outcomes of high-performing enrollees and treated outcomes of low-performing nonenrollees are weakly supported or unsupported. Matching may discard many units, and weighting may create extreme weights. The full-workforce effect may not be identifiable without strong extrapolation.

## Follow-up

> What would you report instead?

### Follow-up answer

I might report an effect for the region of common support or the overlap population, clearly describing which employees are represented. I would also show who is excluded and explain that the data do not support a universal effect claim.

## Question 12

> What else could invalidate or limit the study?

### Expected answer

Potential problems include:

- Unmeasured motivation or manager favoritism.
- Ratings influenced by knowledge of participation.
- Treatment versions differing across instructors or teams.
- Participants receiving better projects after enrollment, creating mediation or post-treatment selection.
- Attrition or departures related to participation and performance.
- Team spillovers.
- Manager-level interference.
- Changing promotion or rating standards.
- Different effects across business units.
- Limited transportability to future cohorts or other firms.

## Follow-up

> Which of those threats would you investigate first?

### Follow-up answer

I would prioritize threats that directly undermine identification and are plausible given the assignment process: voluntary selection, manager sponsorship, prior performance trends, and rating measurement. I would then evaluate overlap and post-treatment changes in project assignment. The order should be driven by the causal structure and institutional context, not by which diagnostic is easiest to run.

---

# 22. Scoring Rubric

Score each dimension from one to four.

## A. Counterfactual reasoning

**1 — Weak:** Treats association as causation and cannot identify the missing counterfactual.

**2 — Developing:** Knows potential-outcome terminology but gives a mechanical explanation.

**3 — Strong:** Clearly explains why one potential outcome is missing and how a design approximates it.

**4 — Exceptional:** Uses counterfactual reasoning to diagnose unfamiliar studies, estimands, and target populations.

## B. Graphical and conditioning intuition

**1 — Weak:** Recommends controlling for every available variable.

**2 — Developing:** Defines confounders and colliders but struggles with new graphs.

**3 — Strong:** Correctly explains blocking, opening, mediation, and collider bias.

**4 — Exceptional:** Anticipates descendants of colliders, post-treatment selection, and changes in estimands.

## C. Observation versus intervention

**1 — Weak:** Treats the following quantities as equivalent:

$$
P(Y\mid X=x)
$$

and:

$$
P(Y\mid do(X=x)).
$$

**2 — Developing:** Knows the notation but gives only an experimental-versus-observational slogan.

**3 — Strong:** Explains that intervention changes the assignment mechanism and removes incoming arrows.

**4 — Exceptional:** Connects interventions to structural equations, exchangeability, identification, and policy interpretation.

## D. Matching and design judgment

**1 — Weak:** Applies propensity score matching automatically.

**2 — Developing:** Can list matching approaches but cannot justify a choice.

**3 — Strong:** Chooses among matching and weighting methods using overlap, estimand, balance, and transparency.

**4 — Exceptional:** Anticipates target-population changes, effective sample size, sensitivity, and unsupported comparisons.

## E. Identification awareness

**1 — Weak:** Focuses on regression specification and p-values.

**2 — Developing:** Names assumptions but treats diagnostics as proof.

**3 — Strong:** States assumptions, distinguishes testable implications, and proposes falsification checks.

**4 — Exceptional:** Evaluates substantive plausibility and recognizes when the desired effect is not identified.

## F. Threats to validity

**1 — Weak:** Mentions only omitted-variable bias.

**2 — Developing:** Lists several threats but discusses them generically.

**3 — Strong:** Distinguishes selection, overlap, measurement, heterogeneity, interference, and transportability.

**4 — Exceptional:** Connects each threat to the specific assignment mechanism, estimand, and comparison population.

## G. Communication

**1 — Weak:** Relies on jargon and cannot explain concepts intuitively.

**2 — Developing:** Gives correct but overly technical explanations.

**3 — Strong:** Explains concepts clearly to technical and nontechnical audiences.

**4 — Exceptional:** Uses simple examples while preserving precise assumptions and qualifications.

---

# 23. Overall Hiring Signals

## Strong hire

The candidate:

- Starts with the causal question, estimand, and target population.
- Explains the missing counterfactual naturally.
- Distinguishes conditioning from intervention.
- Understands both confounding and collider bias.
- Justifies matching or weighting rather than using defaults.
- Checks overlap and balance before estimating outcomes.
- States identification assumptions explicitly.
- Distinguishes testable evidence from untestable causal assumptions.
- Recognizes heterogeneity and estimator-induced weighting.
- Critiques studies through design rather than statistical significance.
- Is comfortable concluding that available data may not identify the requested effect.

## Mixed signal

The candidate:

- Knows standard definitions and estimators.
- Can execute familiar procedures.
- Gives limited discussion of target populations and assumptions.
- Treats diagnostics mechanically.
- Has difficulty transferring intuition to unfamiliar examples.

## Weak signal

The candidate:

- Equates prediction with causality.
- Recommends controlling for every variable.
- Treats intervention notation as ordinary conditioning.
- Uses propensity score matching automatically.
- Ignores overlap, selection, or estimand changes.
- Cannot state the assumptions supporting the causal claim.
- Interprets statistical significance as causal credibility.

---

# 24. Compact Interviewer Checklist

Before believing a causal estimate, ask:

1. What is the treatment intervention?
2. What is the comparison state?
3. What is the outcome and time horizon?
4. What is the estimand?
5. What is the target population?
6. What is the missing counterfactual?
7. How was treatment assigned?
8. What makes the comparison groups exchangeable?
9. Which variables are confounders, mediators, colliders, or descendants of treatment?
10. Is there sufficient overlap?
11. What population remains after matching, weighting, or trimming?
12. Could treatment effects be heterogeneous?
13. Is sample inclusion selective?
14. Are treatment, outcome, and confounders measured adequately?
15. Is the treatment well defined?
16. Is there interference or spillover?
17. Which identifying assumptions are required?
18. Which implications can be tested?
19. What evidence could falsify the design?
20. Does the estimate transport to the intended policy context?

---

# Closing Principle

The interview should reward candidates who repeatedly ask:

> Why does this observed comparison recover the outcome that would have occurred under the alternative treatment?

Regression adjustment, matching, weighting, instrumental variables, difference-in-differences, and regression discontinuity are not substitutes for that reasoning. They are tools whose validity depends on the assignment mechanism, the target estimand, the available support, and the plausibility of their identification assumptions.
