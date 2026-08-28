# Core Concepts in Empirical Economics and Causal Inference

## Table of Contents

- [1. Correlation, Association, and Causation](#1-correlation-association-and-causation)
- [2. Counterfactual Thinking and the Potential Outcomes Framework](#2-counterfactual-thinking-and-the-potential-outcomes-framework)
- [3. DAGs and Causal Graphs](#3-dags-and-causal-graphs)
- [4. Exogeneity and Endogeneity](#4-exogeneity-and-endogeneity)
- [5. Omitted Variable Bias and Confounding](#5-omitted-variable-bias-and-confounding)
- [6. Selection Bias](#6-selection-bias)

## Introduction: What Empirical Economics Is Trying to Do
Empirical economics uses data to study economic behavior, institutions, markets, policies, and social outcomes. But the central purpose of empirical economics is not merely to describe patterns in data. The deeper purpose is often to answer questions about what would happen under an intervention.

A descriptive question asks what is true in the observed world. A causal question asks what would happen if some action were taken. For example:

| Descriptive question | Causal question |
|---|---|
| Do people with more education earn more? | What would happen to a person’s earnings if they received more education? |
| Do cities with more police have more crime? | What would happen to crime if a city increased police presence? |
| Are workers in job training programs more likely to be employed? | What would have happened to those same workers if they had not received job training? |
| Do countries that receive more foreign aid grow more slowly? | What would have happened to those countries’ growth if they had received less aid? |

The first question in each pair is associational. It asks how variables are related in the data. The second question is causal. It asks about the consequence of changing something. This distinction is the foundation of empirical economics. An associational object is often written as: $\mathbb{E}[Y \mid X=x]$ This means: among observations where $X=x$, what is the average value of $Y$? A causal object is closer to: $\mathbb{E}[Y \mid do(X=x)]$ This means: what would the average value of $Y$ be if we intervened and set $X$ equal to $x$? The difference between observing $X=x$ and intervening to make $X=x$ is crucial. Suppose people with sixteen years of education earn more than people with twelve years of education. The observed comparison is: $\mathbb{E}[Wage \mid Education=16] - \mathbb{E}[Wage \mid Education=12]$ This is a comparison between groups of people who chose, reached, or were selected into different levels of education. The causal comparison is: $\mathbb{E}[Wage \mid do(Education=16)] - \mathbb{E}[Wage \mid do(Education=12)]$ This asks what would happen if education itself were changed. The observed difference may not equal the causal effect because education is not randomly assigned. People with different levels of education may also differ in ability, motivation, health, family background, school quality, parental income, neighborhood, social networks, race, gender, expectations, or access to labor markets. These other factors may also affect wages. Therefore, a simple comparison of educated and less educated workers may mix together:

1. the causal effect of education,
2. the effect of ability,
3. the effect of family background,
4. the effect of school quality,
5. the effect of social networks,
6. selection into education,
7. other unobserved determinants of earnings.

Empirical economics is largely about separating these forces. A rigorous empirical study must answer several questions:

1. What is the causal question?
2. What is the intervention or treatment?
3. What is the outcome?
4. What population is being studied?
5. What causal effect is being estimated?
6. What counterfactual comparison is needed?
7. Why is the comparison group credible?
8. What assumptions are required?
9. What evidence supports those assumptions?
10. How uncertain is the estimate?
11. Does the estimate generalize beyond the study setting?
12. Is the estimated effect large enough to matter?

The key lesson is this:

> Data alone do not identify causal effects. Causal inference requires data, theory, research design, institutional knowledge, and assumptions.

The rest of this document develops the main concepts needed to understand and conduct empirical economic research.

---

# 1. Correlation, Association, and Causation

## 1.1 The basic problem
One of the first lessons in empirical economics is that correlation is not causation.

Two variables are correlated when they move together statistically. For example, education and earnings are positively correlated if people with more education tend to earn more. Police presence and crime may be positively correlated if cities with more police also tend to have more crime. Hospital density and illness may be positively correlated if places with more hospitals also have worse health outcomes. But a correlation does not tell us why two variables move together. A relationship between $X$ and $Y$ may exist because:

1. $X$ causes $Y$,
2. $Y$ causes $X$,
3. a third variable causes both $X$ and $Y$,
4. $X$ and $Y$ are jointly determined,
5. the sample is selected,
6. both variables trend over time,
7. the relationship is produced by conditioning on the wrong variable,
8. the relationship is coincidental.

Causal inference is the discipline of deciding which interpretation is credible. A statistical relationship is not enough. To make a causal claim, we need a credible answer to the question:

> What would have happened otherwise?

This “otherwise” is the counterfactual. For example, suppose workers who attend a job training program later earn more than workers who do not attend. That difference might mean the program increased earnings. But it might also mean that workers who chose to attend were already more motivated, better informed, more employable, or more connected. The causal question is not:

> Do trained workers earn more than untrained workers?

The causal question is:

> What would the trained workers have earned if they had not received training?

That second question is harder because the answer is not directly observed.

## 1.2 Correlation
A correlation measures the degree to which two variables move together.

Formally, the correlation between $X$ and $Y$ is: $\operatorname{Corr}(X,Y) = \frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$ where $\operatorname{Cov}(X,Y)$ is the covariance between $X$ and $Y$, and $\sigma_X$ and $\sigma_Y$ are the standard deviations of $X$ and $Y$. If: $\operatorname{Corr}(X,Y)>0$ then higher values of $X$ tend to be associated with higher values of $Y$. If: $\operatorname{Corr}(X,Y)<0$ then higher values of $X$ tend to be associated with lower values of $Y$. If: $\operatorname{Corr}(X,Y)=0$ then there is no linear correlation between $X$ and $Y$, although there may still be a nonlinear relationship. Correlation is useful for description and prediction. If education and earnings are strongly correlated, education may help predict earnings. If income and consumption are strongly correlated, income may help forecast consumption. If interest rates and housing demand are correlated, interest rates may be useful in a predictive model of housing markets. But prediction is not causation. A variable can be useful for prediction without being causal. For example, carrying an umbrella predicts rain, but carrying an umbrella does not cause rain. Similarly, hospital admission predicts poor health, but hospital admission does not necessarily cause poor health. It may simply indicate that a person was already sick.

## 1.3 Association as conditional expectation
Economists often describe associations using conditional expectations.

The conditional expectation: $\mathbb{E}[Y \mid X=x]$ means the expected or average value of $Y$ among units with $X=x$. For example: $\mathbb{E}[Wage \mid Education=16]$ means the average wage among people with sixteen years of education. A difference in conditional expectations compares groups: $\mathbb{E}[Y \mid X=x_1] - \mathbb{E}[Y \mid X=x_0]$ For education and wages, this might be: $\mathbb{E}[Wage \mid Education=16] - \mathbb{E}[Wage \mid Education=12]$ This tells us how average wages differ between people with sixteen years of education and people with twelve years of education. But this is not automatically the causal effect of four more years of education. The problem is that the groups may differ in many ways other than education. The people with sixteen years of education may have had different family backgrounds, different schools, different neighborhoods, different abilities, different expectations, different health, and different labor market opportunities. So the observed difference can be decomposed conceptually into two parts: $Observed\ Difference = Causal\ Effect + Selection\ Difference$ The causal effect is the part caused by education itself. The selection difference is the part caused by the fact that different kinds of people select into different levels of education. The hard empirical problem is separating those two components.

## 1.4 Causation as intervention
Causation asks what would happen if we changed something.

A causal effect is not merely a relationship between variables. It is the effect of an intervention, treatment, exposure, policy, or action. In causal language, we compare: $\mathbb{E}[Y \mid X=x]$ with: $\mathbb{E}[Y \mid do(X=x)]$ The first expression conditions on observing $X=x$. The second expression represents an intervention that sets $X=x$. The notation $do(X=x)$ comes from Judea Pearl’s causal framework. It means that $X$ is externally set to $x$, rather than passively observed at $x$. This distinction matters because observing and intervening are different operations. Suppose we observe that people who take medication are less healthy than people who do not. The associational comparison is: $\mathbb{E}[Health \mid Medication=1] - \mathbb{E}[Health \mid Medication=0]$ This may be negative because sick people are more likely to take medication. But the causal question is: $\mathbb{E}[Health \mid do(Medication=1)] - \mathbb{E}[Health \mid do(Medication=0)]$ This asks what would happen to health if we caused people to take the medication rather than not take it. The observed association may suggest medication is linked to worse health. The causal effect may be that medication improves health. The difference arises because people who take medication are not comparable to people who do not. This is why causal inference requires counterfactual reasoning.

## 1.5 Examples of associational versus causal questions
The distinction becomes clearer when the same topic is framed as an observed association versus an intervention:

| Topic | Associational question | Causal question | Main threats to causal interpretation |
|---|---|---|---|
| Education and earnings | Do people with more education earn more? | What would happen to a person’s earnings if they received more education? | Ability bias; family background; school quality; social networks; motivation; local labor markets; selection into schooling. |
| Police and crime | Do places with more police have more crime? | What would happen to crime if police presence increased? | Police are deployed to high-crime areas; crime causes police presence; political pressure affects police budgets; reporting rates differ; police may affect measured crime differently from actual crime. |
| Hospitals and health | Do places with more hospitals have worse health outcomes? | What would happen to health outcomes if hospital access increased? | Hospitals are built where people are sicker; older populations require more hospitals; urban areas have more hospitals and different health risks; hospital density may reflect demand for care. |
| Job training and employment | Are people in job training programs more likely to be employed? | What would employment have been for participants if they had not received training? | Motivated workers may select into training; struggling workers may enroll; caseworkers may select likely beneficiaries; local labor market conditions affect both enrollment and employment. |
| Minimum wage and employment | Are places with higher minimum wages associated with lower employment? | What would employment have been if the minimum wage had not increased? | High-wage places may adopt higher minimum wages; economic conditions may differ; other labor regulations may change at the same time; firms and workers may anticipate changes. |

In each case, the associational question can be answered directly from observed data. The causal question requires an identification strategy.

## 1.6 Reverse causality
Reverse causality occurs when the outcome causes the explanatory variable, rather than the explanatory variable causing the outcome.

Suppose we estimate: $Crime_c = \alpha + \beta Police_c + u_c$ where $c$ indexes cities. If we find: $\hat{\beta}>0$ we might be tempted to conclude:

> Police increase crime.

But this may be wrong. Cities with more crime may hire more police. In that case, the causal arrow runs from crime to police: $Crime \rightarrow Police$ not merely from police to crime: $Police \rightarrow Crime$ The estimated coefficient $\hat{\beta}$ may therefore reflect the fact that police are assigned to high-crime places. This is reverse causality. Reverse causality is a form of endogeneity because the explanatory variable is related to the error term. In the police example, unobserved determinants of crime, such as gang activity, poverty, drug markets, or political pressure, may influence police deployment. If those unobserved factors are in the error term $u_c$, then: $\operatorname{Cov}(Police_c,u_c) \neq 0$ When this happens, ordinary regression does not recover the causal effect of police on crime. Other examples:

* Poor countries may receive more foreign aid, making aid negatively associated with growth even if aid helps.
* Sick patients may receive more intensive treatment, making treatment associated with worse outcomes even if treatment improves health.
* Firms may advertise more when demand is already rising, making advertising appear more effective than it is.
* Governments may spend more during recessions, making spending appear associated with weak growth even if spending stimulates demand.

The practical lesson is:

> Before interpreting $X$ as a cause of $Y$, ask whether $Y$ could be causing $X$.

## 1.7 Omitted third variables
A correlation between $X$ and $Y$ may arise because a third variable $Z$ affects both.

Suppose: $Z \rightarrow X$ and: $Z \rightarrow Y$ Then $X$ and $Y$ may be correlated even if $X$ has no causal effect on $Y$. For example, ability may affect both education and earnings: $Ability \rightarrow Education$ $Ability \rightarrow Earnings$ If people with higher ability obtain more education and also earn more, then education and earnings will be correlated even if part of the relationship is actually due to ability. This does not mean education has no causal effect. It means the observed association may overstate or understate the causal effect. A third variable that causes both the treatment and the outcome is called a confounder. Confounding is one of the central problems in causal inference. A confounder creates a non-causal path between $X$ and $Y$. If that path is not blocked by design or adjustment, the estimated relationship between $X$ and $Y$ mixes causal and non-causal components.

## 1.8 Simultaneity and equilibrium
Simultaneity occurs when two or more variables are jointly determined.

This is especially common in economics because many economic variables are equilibrium outcomes. Consider price and quantity. Quantity demanded depends on price: $Q_d = f(P, Income, Preferences, Substitutes)$ Quantity supplied also depends on price: $Q_s = g(P, Costs, Technology, Expectations)$ In equilibrium: $Q_d = Q_s$ The observed price and quantity are determined together by supply and demand. If we estimate: $Q_i = \alpha + \beta P_i + u_i$ the coefficient $\beta$ may not identify a demand curve or a supply curve. It may simply describe equilibrium points generated by shifts in both curves. For example, if demand is high, both price and quantity may be high. That can produce a positive relationship between price and quantity, even though a demand curve slopes downward. This is not because the law of demand is false. It is because the observed data are not tracing out a demand curve. They are tracing out market equilibria. To estimate demand, we need variation in price that is not caused by demand shocks. For example, supply shocks may shift price while holding demand conditions fixed. That kind of variation can help identify the demand curve. The general lesson is:

> When variables are jointly determined, a simple regression may not isolate a one-way causal effect.

Simultaneity appears in many settings:

* wages and labor supply,
* prices and quantities,
* interest rates and investment,
* health insurance and healthcare use,
* crime and policing,
* migration and local wages,
* school quality and neighborhood housing prices.

In these settings, economists often need structural models, instrumental variables, natural experiments, or policy variation to identify causal effects.

## 1.9 Spurious correlation in time series
Time series data create a special problem: variables can be correlated because they share a trend.

Suppose: $X_t = a + bt + \varepsilon_t$ and: $Y_t = c + dt + \eta_t$ where both variables trend over time. Even if $X_t$ has no causal effect on $Y_t$, a regression of $Y_t$ on $X_t$ may show a strong relationship. This is called spurious correlation or spurious regression. For example, over a long period, both healthcare spending and average life expectancy may rise. That does not automatically mean every increase in healthcare spending caused the increase in life expectancy. Other factors may also be changing, such as nutrition, sanitation, education, income, technology, and public health. Similarly, smartphone use and online shopping may both rise over time. A regression of online shopping on smartphone use may show a strong relationship, but the relationship could partly reflect a broader time trend in digital technology adoption. Spurious time-series relationships often have warning signs:

1. both variables trend over time,
2. the regression has a high $R^2$,
3. coefficients are statistically significant,
4. residuals are autocorrelated,
5. there is no clear causal mechanism,
6. results disappear after detrending or differencing,
7. results are sensitive to the time period studied.

Economists use several tools to reduce the risk of spurious time-series inference:

* including time trends,
* differencing the data,
* using growth rates rather than levels,
* including time fixed effects,
* checking stationarity,
* testing for cointegration,
* using event-study designs,
* checking pre-trends,
* modeling serial correlation,
* comparing treated and untreated units over time.

The deeper point is that time creates structure. Observations close together in time are often related. Trends, cycles, seasonality, and persistence must be taken seriously.

## 1.10 Causation requires a counterfactual
A causal effect compares what happened to what would have happened under a different intervention.

For a treatment $D$, the causal effect is not simply: $\mathbb{E}[Y \mid D=1] - \mathbb{E}[Y \mid D=0]$ That is the observed difference between treated and untreated units. The causal question is: $\mathbb{E}[Y(1) - Y(0)]$ where:

* $Y(1)$ is the outcome under treatment,
* $Y(0)$ is the outcome without treatment.

The challenge is that for any unit, we observe either $Y(1)$ or $Y(0)$, but not both. This is the fundamental problem of causation. If a worker receives training, we observe their earnings with training. We do not observe what their earnings would have been without training. If a worker does not receive training, we observe their earnings without training. We do not observe what their earnings would have been with training. Therefore, causal inference requires constructing or defending a comparison group that represents the missing counterfactual. A comparison group is credible only if it answers the right counterfactual question. For example, if participants in a training program are compared to all nonparticipants, the comparison may be biased. But if participants were randomly selected from eligible workers, then nonparticipants may provide a credible estimate of what would have happened to participants without training. The credibility of a causal estimate depends on the credibility of the counterfactual.

## 1.11 Causal mechanisms
A causal claim should usually be supported by a plausible mechanism.

A mechanism explains how $X$ affects $Y$. For example, education may increase earnings through several channels: $Education \rightarrow Skills \rightarrow Productivity \rightarrow Wages$ or: $Education \rightarrow Credentials \rightarrow Employer Beliefs \rightarrow Wages$ or: $Education \rightarrow Networks \rightarrow Job Opportunities \rightarrow Wages$ Different mechanisms imply different policy interpretations. If education raises wages mainly by increasing skills, then expanding education may increase productivity. If education raises wages mainly by signaling ability, then expanding education may change credentials without increasing productivity as much. If education works through networks, then school quality and peer composition may matter. Mechanisms do not automatically prove causality, but they help make causal claims more credible and interpretable. A causal estimate without a plausible mechanism may still be correct, but it deserves scrutiny. A plausible mechanism without credible identification is also not enough. Good empirical work needs both.

## 1.12 Causal claims and research design
A research design is a strategy for constructing a credible comparison.

Different designs solve the correlation-causation problem in different ways.

- **Randomized controlled trials.** Randomization makes treatment independent of potential outcomes in expectation. Treated and control groups are comparable because treatment assignment is determined by chance.
- **Difference-in-differences.** Difference-in-differences compares changes over time between treated and control groups. It relies on the assumption that, without treatment, the groups would have followed parallel trends.
- **Regression discontinuity.** Regression discontinuity compares units just above and below a cutoff. It relies on the idea that units near the cutoff are similar except for treatment status.
- **Instrumental variables.** Instrumental variables use a source of variation that affects treatment but affects the outcome only through treatment.
- **Fixed effects.** Fixed effects compare units to themselves over time, removing stable unobserved differences across units.
- **Matching and weighting.** Matching and weighting compare treated and untreated units that look similar on observed characteristics. These methods require the assumption that all relevant confounders are observed and properly adjusted for.
Each design has assumptions. No method produces causality automatically. The question is not:

> Which statistical method was used?

The question is:

> What variation identifies the effect, and why is that variation plausibly exogenous?

## 1.13 Common mistakes

1. **Mistake 1: Treating a regression coefficient as automatically causal.** A regression coefficient measures a conditional association unless the research design and assumptions justify a causal interpretation.
For example: $Wage_i = \alpha + \beta Education_i + u_i$ The coefficient $\beta$ is not automatically the causal return to education. It may be biased by ability, family background, school quality, or selection.

2. **Mistake 2: Controlling for everything.** Many beginners think adding more control variables always improves causal inference.
This is false. Some controls are good because they block confounding paths. Other controls are bad because they block causal pathways or open non-causal paths. For example, if education affects occupation and occupation affects earnings, then occupation is a mediator: $Education \rightarrow Occupation \rightarrow Earnings$ If we control for occupation, we may remove part of the total effect of education. Similarly, conditioning on a collider can create bias. The right controls depend on the causal structure, not just on data availability.

3. **Mistake 3: Ignoring timing.** For $X$ to cause $Y$, $X$ must occur before $Y$. If the supposed cause happens after the outcome, the causal interpretation is usually invalid.
Timing is especially important in panel data, policy evaluation, and event studies.

4. **Mistake 4: Ignoring equilibrium behavior.** In economics, people respond to incentives. Firms adjust prices, workers change labor supply, consumers substitute across goods, governments respond to conditions, and markets clear.
Because of this, observed relationships often reflect equilibrium adjustments rather than simple one-way causation.

5. **Mistake 5: Confusing statistical significance with causality.** A statistically significant estimate is not necessarily causal. Statistical significance measures whether an estimate is distinguishable from zero under a statistical model. It does not prove that the estimate has a causal interpretation.
A biased estimate can be very statistically significant.

6. **Mistake 6: Ignoring external validity.** Even if a study identifies a causal effect in one setting, the effect may not generalize to other populations, time periods, institutions, or scales.
A tutoring program that works in one city may not work equally well elsewhere. A tax policy effect estimated during a recession may not apply during a boom. A small pilot program may not scale nationally.

## 1.14 Application checklist
When evaluating any empirical claim, ask the following questions.

1. **Identify the claim.** What is the claimed relationship?
$X \rightarrow Y$
What is the treatment, exposure, or policy? What is the outcome?

2. **Distinguish association from causation.** Is the claim merely that $X$ and $Y$ are related, or that changing $X$ would change $Y$?
3. **Define the intervention.** What does it mean to intervene on $X$?
For example, “education” is broad. Does the intervention mean one more year of schooling, smaller class sizes, college attendance, school quality, compulsory schooling, or tutoring? A causal question must define the intervention precisely.

4. **Define the counterfactual.** What would have happened to the treated units without treatment?
What would have happened to the untreated units with treatment? Which missing comparison matters for the estimand?

5. **Look for confounding.** Could another variable cause both $X$ and $Y$?
If yes, how is that addressed?

6. **Check reverse causality.** Could $Y$ cause $X$?
If yes, a simple regression may not identify the effect of $X$ on $Y$.

7. **Check simultaneity.** Are $X$ and $Y$ jointly determined in equilibrium?
If yes, what source of variation isolates one causal direction?

8. **Check timing.** Does the supposed cause occur before the outcome?
Are there anticipation effects? Are there lagged effects?

9. **Evaluate the research design.** What variation identifies the effect?
Is it random assignment, a cutoff, a policy shock, an instrument, a before-after comparison, or within-unit variation? Why is that variation plausibly exogenous?

10. **State the assumptions.** Every causal estimate depends on assumptions. What are they?
Can they be tested directly? If not, can they be supported indirectly?

11. **Interpret the estimate carefully.** What effect is estimated?
For whom? Over what time horizon? Under what conditions? Does it represent an average effect, a local effect, an effect on treated units, or something else?

## 1.15 Summary
Correlation describes how variables move together.

Association describes how average outcomes differ across observed values of a variable. Causation asks what would happen if a variable were changed by intervention. The main problem is that observed comparisons often do not equal causal effects. People, firms, schools, cities, and countries select into treatments and policies. Economic variables are often jointly determined. Time trends can create misleading relationships. Third variables can generate confounding. Outcomes can influence treatments. Therefore, credible empirical economics requires more than data and regression. It requires a clearly defined causal question, a credible counterfactual, a research design that justifies the comparison, and explicit assumptions. The core lesson of this section is:

> A statistical relationship tells us what is observed. A causal effect tells us what would happen under an intervention. The purpose of empirical research design is to bridge that gap.

# 2. Counterfactual Thinking and the Potential Outcomes Framework

## 2.1 Why counterfactuals are central to causal inference
Causal inference is built around counterfactual thinking. A counterfactual is a statement about what would have happened under a different condition from the one actually observed.

For example:

> If this worker had not received job training, their earnings would have been lower.

> If this city had not increased police patrols, crime would have followed a different path.

> If this student had not attended college, their earnings would have been different.

> If this patient had not received treatment, their health outcome would have been worse.

These statements are not directly observed facts. They refer to alternative possible states of the world. The worker either received job training or did not. The city either increased patrols or did not. The student either attended college or did not. The patient either received treatment or did not. The central difficulty is that causal effects compare what actually happened to what would have happened under a different action. That is why causal inference is harder than description. Description uses observed outcomes. Causation requires reasoning about missing outcomes. Suppose a worker participates in a job training program and later earns \$35,000. The observed fact is: $Observed\ Earnings = 35{,}000$ But to know whether the program helped, we need to know what that same worker would have earned without the program. If they would have earned \$30,000 without training, the program helped by \$5,000. If they would have earned \$35,000 anyway, the program had no effect. If they would have earned \$40,000 without training, the program harmed them by \$5,000. The causal effect cannot be read from the observed outcome alone. It depends on a comparison between the observed outcome and the counterfactual outcome. This idea is the foundation of modern causal inference.

## 2.2 Factual outcomes and counterfactual outcomes
For each unit of analysis, there are outcomes that are observed and outcomes that are not observed.

A unit may be a person, worker, firm, school, hospital, neighborhood, city, state, country, or time period. The treatment may be a policy, program, exposure, price change, law, educational intervention, medical treatment, or economic shock. Consider a binary treatment: $D_i \in \{0,1\}$ where:

- $D_i=1$ means unit $i$ receives treatment,
- $D_i=0$ means unit $i$ does not receive treatment.

For each unit, define two potential outcomes: $Y_i(1)$ and: $Y_i(0)$ where:

- $Y_i(1)$ is the outcome unit $i$ would have if treated,
- $Y_i(0)$ is the outcome unit $i$ would have if untreated.

These are called potential outcomes because they represent the outcomes that are possible under different treatment states. For example, if the unit is a worker and the treatment is job training:

- $Y_i(1)$: worker $i$'s earnings if they receive job training,
- $Y_i(0)$: worker $i$'s earnings if they do not receive job training.

If the unit is a student and the treatment is tutoring:

- $Y_i(1)$: student $i$'s test score if they receive tutoring,
- $Y_i(0)$: student $i$'s test score if they do not receive tutoring.

If the unit is a city and the treatment is a minimum wage increase:

- $Y_i(1)$: city $i$'s employment level if the minimum wage increases,
- $Y_i(0)$: city $i$'s employment level if the minimum wage does not increase.

The individual causal effect is: $\tau_i = Y_i(1) - Y_i(0)$ This equation says that the causal effect for unit $i$ is the difference between that unit's outcome under treatment and that same unit's outcome without treatment. The phrase "that same unit" is essential. Causal inference does not fundamentally compare one treated person to a different untreated person. It compares the same unit under two possible treatment states. Since we cannot observe both states for the same unit at the same time, empirical methods try to find credible substitutes for the missing potential outcome.

## 2.3 The observed outcome equation
Although each unit has two potential outcomes, only one is observed.

If unit $i$ is treated, then $D_i=1$, and we observe: $Y_i = Y_i(1)$ If unit $i$ is untreated, then $D_i=0$, and we observe: $Y_i = Y_i(0)$ The observed outcome can be written compactly as: $Y_i = D_iY_i(1) + (1-D_i)Y_i(0)$ This is called the switching equation or observed outcome equation. To see why it works, consider the two cases. If $D_i=1$: $Y_i = 1\cdot Y_i(1) + (1-1)Y_i(0)$ $Y_i = Y_i(1)$ If $D_i=0$: $Y_i = 0\cdot Y_i(1) + (1-0)Y_i(0)$ $Y_i = Y_i(0)$ This equation makes the missing-data structure of causal inference explicit. The observed outcome is one of the two potential outcomes. The other potential outcome is missing. For treated units, $Y_i(0)$ is missing. For untreated units, $Y_i(1)$ is missing. This is not ordinary missing data caused by a survey problem or database error. It is missing by the logic of causation. A unit cannot simultaneously receive and not receive the same treatment at the same time under the same conditions.

## 2.4 The fundamental problem of causation
The individual treatment effect is: $\tau_i = Y_i(1)-Y_i(0)$
But for any individual unit, we observe only one of the two potential outcomes.

If treated: $Y_i(1) \text{ is observed, but } Y_i(0) \text{ is missing.}$ If untreated: $Y_i(0) \text{ is observed, but } Y_i(1) \text{ is missing.}$ Therefore, the individual causal effect $\tau_i$ is generally not directly observable. This is called the fundamental problem of causation. The problem is not that researchers lack enough data. Even with perfect data collection, one cannot observe both potential outcomes for the same unit in the same moment. A worker either attended the training program or did not. A city either passed the policy or did not. A student either received tutoring or did not. Causal inference is therefore a problem of missing counterfactuals. The main question becomes:

> How can we use observed data to learn about the missing potential outcomes?

Different research designs answer this question differently. An RCT uses random assignment so that the untreated group can stand in for what would have happened to the treated group without treatment. Difference-in-differences uses the control group's change over time to approximate the treated group's counterfactual change. Regression discontinuity uses units just on the other side of a cutoff as a comparison for units just across the cutoff. Instrumental variables use variation in treatment induced by an instrument to isolate a specific causal effect. Fixed effects compare units to themselves over time, removing time-invariant differences. The methods differ, but the underlying problem is the same: construct a credible substitute for the missing counterfactual.

## 2.5 Why causal inference usually focuses on average effects
Because individual treatment effects are usually unobservable, empirical research often focuses on average treatment effects.

The average treatment effect, or ATE, is: $ATE = \mathbb{E}[Y_i(1)-Y_i(0)]$ This is the average causal effect in the population. Using linearity of expectation: $ATE = \mathbb{E}[Y_i(1)] - \mathbb{E}[Y_i(0)]$ The ATE asks:

> What is the average difference between outcomes if everyone were treated and outcomes if everyone were untreated?

For a job training program, the ATE asks:

> On average, how much would earnings change if everyone received training compared with if no one received training?

For a tutoring program, the ATE asks:

> On average, how much would test scores change if everyone received tutoring compared with if no one received tutoring?

The ATE is often useful, but it is not always the most relevant estimand. Sometimes we care about other averages. The average treatment effect on the treated, or ATT, is: $ATT = \mathbb{E}[Y_i(1)-Y_i(0) \mid D_i=1]$ This asks:

> What is the average effect of treatment for those who actually received treatment?

For a voluntary job training program, ATT asks whether the program helped participants. The average treatment effect on the untreated, or ATU, is: $ATU = \mathbb{E}[Y_i(1)-Y_i(0) \mid D_i=0]$ This asks:

> What would the average effect be for those who did not receive treatment?

For policy expansion, ATU can be important. If a program worked for participants, policymakers may want to know whether it would also work for nonparticipants. The conditional average treatment effect, or CATE, is: $CATE(x)=\mathbb{E}[Y_i(1)-Y_i(0) \mid X_i=x]$ This asks:

> What is the average effect for units with characteristics $X_i=x$?

For example, a training program may work better for young workers than older workers, or better for workers with low baseline skills than workers with high baseline skills. The local average treatment effect, or LATE, often appears in instrumental variables settings. It is the average treatment effect for compliers: units whose treatment status changes because of the instrument. The key point is that "the causal effect" is often not a single universal number. Researchers must be precise about which causal effect they are trying to estimate.

## 2.6 Naive comparisons and selection bias
A common mistake is to compare treated and untreated units directly: $\mathbb{E}[Y_i \mid D_i=1] - \mathbb{E}[Y_i \mid D_i=0]$
Using the observed outcome equation, this equals: $\mathbb{E}[Y_i(1) \mid D_i=1] - \mathbb{E}[Y_i(0) \mid D_i=0]$
This compares treated units under treatment to untreated units without treatment.

But the ATT is: $ATT = \mathbb{E}[Y_i(1)-Y_i(0) \mid D_i=1]$ which can be written as: $ATT = \mathbb{E}[Y_i(1) \mid D_i=1] - \mathbb{E}[Y_i(0) \mid D_i=1]$ The missing term is: $\mathbb{E}[Y_i(0) \mid D_i=1]$ This is the average outcome treated units would have had if they had not been treated. The naive comparison uses instead: $\mathbb{E}[Y_i(0) \mid D_i=0]$ This is the average untreated outcome among untreated units. The naive comparison identifies ATT only if: $\mathbb{E}[Y_i(0) \mid D_i=1] = \mathbb{E}[Y_i(0) \mid D_i=0]$ In words: treated and untreated units would have had the same average outcome without treatment. This condition often fails. For example, people who voluntarily enroll in job training may be more motivated than people who do not. If motivation increases earnings even without training, then: $\mathbb{E}[Y_i(0) \mid D_i=1] > \mathbb{E}[Y_i(0) \mid D_i=0]$ In that case, the naive comparison overstates the effect of training. But selection can also go the other way. People who enroll in job training may be those struggling most in the labor market. If they would have had lower earnings even without training, then: $\mathbb{E}[Y_i(0) \mid D_i=1] < \mathbb{E}[Y_i(0) \mid D_i=0]$ In that case, the naive comparison may understate the effect of training. Selection bias is the difference between the untreated potential outcomes of treated and untreated units: $\text{Selection Bias} = \mathbb{E}[Y_i(0) \mid D_i=1] - \mathbb{E}[Y_i(0) \mid D_i=0]$ The observed treated-control difference can be written as:

$$
\mathbb{E}[Y_i \mid D_i=1] - \mathbb{E}[Y_i \mid D_i=0]
= ATT + Selection\ Bias
$$

This decomposition is one of the most important results in causal inference. It shows why treated-control comparisons are not automatically causal.

## 2.7 Identification versus estimation
Counterfactual thinking clarifies the distinction between identification and estimation.

An estimand is the causal quantity we want to learn. Examples include ATE, ATT, CATE, and LATE. An estimator is the statistical procedure we use to estimate that quantity. Examples include a difference in means, an OLS coefficient, a two-stage least squares estimate, a difference-in-differences coefficient, or a regression discontinuity estimate. Identification asks whether the causal estimand can be expressed in terms of observed data under stated assumptions. For example, the ATE is: $ATE = \mathbb{E}[Y_i(1)-Y_i(0)]$ But $Y_i(1)$ and $Y_i(0)$ are not both observed for each unit. So the ATE is not automatically identified. If treatment is randomly assigned, then: $D_i \perp (Y_i(1),Y_i(0))$ This means treatment assignment is independent of potential outcomes. Under random assignment: $\mathbb{E}[Y_i(1)] = \mathbb{E}[Y_i \mid D_i=1]$ and: $\mathbb{E}[Y_i(0)] = \mathbb{E}[Y_i \mid D_i=0]$ Therefore: $ATE = \mathbb{E}[Y_i \mid D_i=1] - \mathbb{E}[Y_i \mid D_i=0]$ In this case, the causal estimand is identified by an observable difference in means. Estimation then concerns how accurately we can estimate that difference using sample data. Identification is about whether the causal question can be answered in principle using the available design and assumptions. Estimation is about how precisely we answer it with finite data. A study can have precise estimates of the wrong estimand. A regression coefficient can have small standard errors and still fail to identify a causal effect. Precision does not solve identification.

## 2.8 Key assumptions in the potential outcomes framework
The potential outcomes framework requires assumptions that connect observed data to causal quantities. Some assumptions are conceptual; others are identifying assumptions.

- **2.8.1 Consistency.** Consistency means that the observed outcome equals the potential outcome corresponding to the treatment actually received.
If $D_i=1$, then: $Y_i = Y_i(1)$ If $D_i=0$, then: $Y_i = Y_i(0)$ This may sound obvious, but it requires that the treatment be well defined. For example, suppose the treatment is "job training." What exactly does that mean?

- A one-week online course?
- A six-month classroom program?
- Apprenticeship with an employer?
- Resume coaching?
- Technical certification?
- Mandatory or voluntary attendance?

If different people receive very different versions of "job training," then $Y_i(1)$ may not be well defined. The potential outcome under treatment depends on which version of treatment is received. Consistency requires that treatment categories correspond to meaningful, well-defined interventions.

- **2.8.2 No interference.** No interference means one unit's treatment does not affect another unit's outcome.
Formally, unit $i$'s potential outcomes depend only on unit $i$'s treatment, not on the treatment status of other units. Under no interference, we can write: $Y_i(D_i)$ rather than: $Y_i(D_1,D_2,\dots,D_n)$ This assumption can fail in many economic settings. For example:

- A job training program may help participants get jobs, but if jobs are limited, it may reduce employment opportunities for nonparticipants.
- Vaccination affects not only vaccinated individuals but also others through herd immunity.
- Tutoring one student may affect classmates through peer effects.
- A policing intervention in one neighborhood may displace crime to nearby neighborhoods.
- A minimum wage increase in one city may affect nearby labor markets.

When interference is present, the causal effect of treatment depends on who else is treated. The simple two-potential-outcome framework becomes incomplete.

- **2.8.3 SUTVA.** SUTVA stands for the Stable Unit Treatment Value Assumption. It usually combines two ideas:
1. no interference between units,
2. no hidden versions of treatment.

No hidden versions of treatment means that treatment is sufficiently well defined. If two units are both labeled treated, they should be receiving the same relevant treatment for purposes of the analysis. SUTVA is often stated casually, but it is substantively important. Many policy interventions have multiple versions, variable intensity, imperfect implementation, or spillovers. In such cases, researchers must be clear about what treatment means. For example, "access to healthcare" could mean insurance coverage, physical proximity to clinics, lower prices, appointment availability, quality of care, or actual treatment received. These are not the same intervention. A vague treatment definition leads to vague causal interpretation.

- **2.8.4 Ignorability or unconfoundedness.** In observational studies, researchers often rely on an assumption called ignorability, unconfoundedness, or selection on observables.
The assumption is: $(Y_i(1),Y_i(0)) \perp D_i \mid X_i$ This means that after conditioning on observed covariates $X_i$, treatment assignment is independent of potential outcomes. In plain English:

> Once we compare units with the same observed characteristics, treatment status is as good as random.

If this assumption holds, then differences in outcomes between treated and untreated units with the same $X_i$ can be interpreted causally. For example, suppose we compare job training participants and nonparticipants with the same age, education, prior earnings, employment history, location, and industry. If there are no remaining unobserved differences affecting both participation and earnings, then treatment may be considered unconfounded conditional on those variables. This is a strong assumption. It fails if selection depends on unobserved motivation, ability, private information, family support, health, or employer connections. Matching, regression adjustment, weighting, and stratification often rely on some version of this assumption.

- **2.8.5 Positivity or overlap.** Positivity, also called overlap or common support, requires that each unit has a positive probability of receiving each treatment level for relevant values of covariates.
For binary treatment: $0 < P(D_i=1 \mid X_i=x) < 1$ for all relevant $x$. In plain English:

> For units with a given set of characteristics, there must be both treated and untreated observations to compare.

If all highly educated workers receive training and no less educated workers receive training, then we cannot compare treated and untreated workers at every education level. Without overlap, causal inference requires extrapolation beyond the data. Overlap is often checked using propensity scores, covariate balance tables, and visual comparisons of treated and untreated distributions. Poor overlap means that the treated and untreated groups are too different to support credible comparison without strong modeling assumptions.

## 2.9 Random assignment as the benchmark
Random assignment is conceptually important because it solves the missing counterfactual problem in expectation.

If treatment is randomly assigned, then: $D_i \perp (Y_i(1),Y_i(0))$ This says that treatment status is independent of potential outcomes. Under random assignment, treated and control groups may differ in realized outcomes after treatment, but before treatment they are comparable in expectation. The control group provides an estimate of what would have happened to the treated group without treatment. In an RCT: $\mathbb{E}[Y_i(1) \mid D_i=1] = \mathbb{E}[Y_i(1) \mid D_i=0]$ and: $\mathbb{E}[Y_i(0) \mid D_i=1] = \mathbb{E}[Y_i(0) \mid D_i=0]$ Therefore: $ATE = \mathbb{E}[Y_i \mid D_i=1] - \mathbb{E}[Y_i \mid D_i=0]$ Randomization does not make every treated unit identical to every untreated unit. In finite samples, random imbalance can occur. But randomization ensures that, on average over repeated random assignments, treatment status is unrelated to both observed and unobserved determinants of outcomes. This is why random assignment is often treated as the benchmark for causal inference. However, RCTs are not perfect. They can still face noncompliance, attrition, spillovers, measurement problems, Hawthorne effects, implementation failures, and limited external validity. Random assignment solves confounding in expectation, but it does not solve every empirical problem.

## 2.10 Observational studies and the search for credible counterfactuals
In many economic settings, random assignment is impossible, unethical, impractical, or too expensive.

Researchers cannot usually randomly assign:

- years of schooling,
- unemployment,
- immigration status,
- exposure to war,
- pollution exposure,
- incarceration,
- tax rates,
- minimum wage laws,
- monetary policy,
- family structure,
- neighborhood of childhood.

When treatment is not randomized, researchers must explain why the observed comparison approximates a valid counterfactual. This is the purpose of research design. A good observational study does not merely add control variables and hope for the best. It identifies a source of variation in treatment that is plausibly unrelated to potential outcomes. Examples:

- A school entry cutoff may create quasi-random variation in age at school entry.
- A draft lottery may create quasi-random variation in military service.
- A judge assignment system may create variation in sentencing severity.
- A policy rollout may affect some regions earlier than others.
- Weather shocks may affect agricultural income independently of farmer choices.
- Administrative eligibility thresholds may create discontinuities in treatment.

Each design tries to answer the same question:

> Why is this comparison group a credible stand-in for the missing counterfactual?

The credibility of an observational study depends less on the complexity of the statistical model and more on the plausibility of the identifying assumptions.

## 2.11 Counterfactuals in Pearl's ladder of causation
Judea Pearl describes causal reasoning as a ladder with three levels.

1. **Level 1: Association.** The first level concerns patterns in observed data.
$P(Y \mid X)$
This answers questions like:

> Are people with college degrees more likely to earn high wages?

> Are cities with more police more likely to have high crime?

> Are patients who take medication more likely to recover?

These are associational questions. They describe what is observed.

2. **Level 2: Intervention.** The second level concerns what happens when an action is taken.
$P(Y \mid do(X=x))$
This answers questions like:

> What happens to earnings if we make someone attend college?

> What happens to crime if police presence increases?

> What happens to recovery if patients are assigned medication?

These are causal intervention questions.

3. **Level 3: Counterfactuals.** The third level concerns what would have happened under a different condition for the same unit.
Examples:

> Would this worker have earned less if they had not received training?

> Would this city have had more crime if it had not increased policing?

> Would this patient have recovered if they had not taken the medication?

These are counterfactual questions. The potential outcomes framework is especially natural for Level 3 reasoning because it explicitly defines outcomes under alternative treatment states. Pearl's do-operator framework and the potential outcomes framework use different notation, but they are deeply connected. Both distinguish observing from intervening. Both require assumptions to move from observed data to causal claims. Both emphasize that causal inference cannot be reduced to ordinary conditioning.

## 2.12 Subjunctive conditionals and disciplined imagination
Counterfactual claims are often expressed as subjunctive conditionals:

> If the worker had not received training, they would have earned less.

> If the city had not passed the law, employment would have followed the same trend as similar cities.

> If the student had scored just above the cutoff, they would have received the scholarship.

> If the firm had not adopted the technology, productivity would have grown more slowly.

These statements are claims about alternative possible worlds. They require imagination, but not unconstrained imagination. Empirical research disciplines counterfactual imagination using data, research design, and assumptions. For example, in difference-in-differences, the central counterfactual claim is:

> If the treated group had not received treatment, it would have followed the same trend as the control group.

This is the parallel trends assumption. In regression discontinuity, the central counterfactual claim is:

> Units just above and just below the cutoff would have had similar outcomes in the absence of treatment.

This is the continuity assumption. In instrumental variables, the central counterfactual claim is:

> The instrument changes the treatment but affects the outcome only through that treatment.

This is the exclusion restriction. In matching, the central counterfactual claim is:

> After adjusting for observed characteristics, treated and untreated units are comparable.

This is the unconfoundedness assumption. Every empirical method makes counterfactual claims. The difference between strong and weak empirical work is whether those claims are explicit, plausible, and probed with evidence.

## 2.13 Treatment definition and the importance of well-defined interventions
A causal question is only as clear as its treatment definition.

Consider the question:

> What is the effect of education on earnings?

This sounds simple, but "education" could mean many things:

- one additional year of schooling,
- high school completion,
- college attendance,
- college graduation,
- attending a selective college,
- school quality,
- class size,
- teacher quality,
- field of study,
- vocational training,
- online education,
- compulsory schooling laws.

Each is a different intervention and may have a different causal effect. The same issue arises with many treatments. "Healthcare access" could mean insurance coverage, lower prices, more clinics, shorter wait times, better doctors, transportation to appointments, or legal eligibility. "Policing" could mean more officers, different patrol locations, higher arrest rates, community policing, surveillance technology, stop-and-frisk, faster response times, or better clearance rates. "Job training" could mean classroom instruction, employer-based training, apprenticeships, resume support, job search assistance, certification, wage subsidies, or counseling. A vague treatment produces a vague causal estimand. A rigorous causal question should specify:

1. who receives the treatment,
2. what exactly the treatment is,
3. when the treatment occurs,
4. how intense the treatment is,
5. what comparison condition is used,
6. what outcome is measured,
7. over what time horizon the outcome is measured.

For example, instead of asking:

> What is the effect of job training?

ask:

> What is the effect of being offered a six-month subsidized technical training program on annual earnings two years later among unemployed workers aged 25 to 45?

The second question is much more suitable for causal analysis.

## 2.14 Counterfactuals and time
Time is central to causal inference.

A cause must occur before its effect. Therefore, the timing of treatment, outcome measurement, and confounders matters. A basic causal timeline is: $\text{Pre-treatment variables} \rightarrow \text{Treatment} \rightarrow \text{Post-treatment outcomes}$ Pre-treatment variables are determined before treatment. They may be confounders and may be appropriate controls. Post-treatment variables are determined after treatment. They may be outcomes, mediators, or consequences of treatment. Controlling for them can create bias if the goal is to estimate the total effect of treatment. For example: $Education \rightarrow Occupation \rightarrow Earnings$ If the goal is to estimate the total effect of education on earnings, controlling for occupation may be inappropriate because occupation is partly caused by education. It lies on the causal pathway. Similarly, suppose a health intervention affects employment, and employment affects later health: $Health\ Program \rightarrow Employment \rightarrow Later\ Health$ Controlling for employment may block part of the program's effect. Timing also matters for anticipation effects. If people change behavior before a policy begins because they expect it, then outcomes may start changing before treatment is officially observed. For example, firms may adjust employment before a minimum wage increase takes effect. Households may change purchases before a tax increase. Students may alter effort before a scholarship cutoff is applied. A rigorous counterfactual analysis must therefore specify:

- when treatment is assigned,
- when treatment is received,
- when outcomes are measured,
- whether anticipation is possible,
- whether effects are immediate or delayed,
- whether treatment effects persist, fade, or grow over time.

## 2.15 Counterfactuals, mechanisms, and mediation
A counterfactual effect tells us whether treatment changes an outcome. But researchers often also want to know why.

A mechanism is a causal pathway through which treatment affects the outcome. For example: $\text{Job Training} \rightarrow \text{Skills} \rightarrow \text{Employment} \rightarrow \text{Earnings}$ or: $\text{Education} \rightarrow \text{Credentials} \rightarrow \text{Employer Beliefs} \rightarrow \text{Wages}$ or: $\text{Pollution} \rightarrow \text{Respiratory Illness} \rightarrow \text{Labor Supply} \rightarrow \text{Earnings}$ Mechanisms matter because they affect interpretation and policy design. If job training increases earnings by raising skills, then improving training quality may increase effects. If it works mainly by signaling motivation to employers, then scaling it up may reduce its signaling value. If it works by connecting workers to employers, then networks and placement services may be central. However, mechanism analysis requires caution. Suppose treatment affects a mediator $M$, and the mediator affects outcome $Y$: $D \rightarrow M \rightarrow Y$ If we control for $M$, we may block part of the treatment effect. That may be useful if we want a direct effect holding $M$ fixed, but it is not appropriate if we want the total effect. For example, if education affects earnings partly through occupation, controlling for occupation estimates something closer to the effect of education holding occupation fixed. It does not estimate the total effect of education. Mechanism analysis therefore requires a clear distinction between:

- total effects,
- direct effects,
- indirect effects,
- mediated effects.

Counterfactual thinking helps clarify these distinctions.

## 2.16 Counterfactuals with continuous or multi-valued treatments
The simple potential outcomes setup uses binary treatment, $D_i \in \{0,1\}$. Many economic treatments are not binary.

Examples:

- years of education,
- hours of training,
- tax rates,
- pollution levels,
- minimum wage levels,
- interest rates,
- class size,
- police patrol intensity,
- benefit generosity.

For a multi-valued or continuous treatment, potential outcomes can be written as: $Y_i(d)$ where $d$ is a possible treatment level. For example: $Y_i(12), Y_i(13), Y_i(14), Y_i(15), Y_i(16)$ could represent earnings under different years of education. A causal effect can compare two treatment levels: $Y_i(d_1)-Y_i(d_0)$ For continuous treatments, researchers may be interested in marginal effects: $\frac{\partial Y_i(d)}{\partial d}$ or average dose-response functions: $\mathbb{E}[Y_i(d)]$ The conceptual problem remains the same. For each unit, we observe the outcome at the treatment level actually received, but not the outcomes under all other possible treatment levels. Continuous treatments also raise additional challenges:

- treatment may not be well defined at every level,
- overlap may fail for some values of $d$,
- effects may be nonlinear,
- marginal effects may differ from large policy changes,
- changing treatment intensity may alter behavior differently than changing treatment status.

For example, the effect of increasing schooling from 11 to 12 years may differ from the effect of increasing schooling from 15 to 16 years. The effect of a small tax increase may differ from the effect of a large tax reform.

## 2.17 Counterfactuals and external validity
A causal estimate is always tied to a population, setting, treatment version, and time period.

Suppose an RCT estimates the effect of tutoring on test scores for ninth-grade students in one city. The estimated effect answers a counterfactual question for that sample and setting:

> What would have happened to these students' test scores if they had not received this tutoring program under these implementation conditions?

It does not automatically answer:

- Would the same program work for younger students?
- Would it work in another country?
- Would it work if scaled nationally?
- Would it work with different tutors?
- Would it work during remote learning?
- Would it work for students with much higher or lower baseline achievement?

External validity is itself a counterfactual problem. It asks what would happen if the same or similar treatment were implemented in a different setting. Generalizing a causal effect requires assumptions about mechanisms, populations, institutions, implementation, and equilibrium responses. For example, a small job training program may help participants because employers value the credential and the program places workers into available jobs. But if the program is scaled nationally, the labor market may become saturated with credentialed workers, and the effect may change. The question is not simply whether the original estimate was internally valid. The question is whether the counterfactual conditions in the new setting are sufficiently similar.

## 2.18 Practical example: job training and earnings
Consider a voluntary job training program for unemployed workers.

Let: $D_i=1$ if worker $i$ participates in training, and: $D_i=0$ if worker $i$ does not participate. Let: $Y_i(1)$ be worker $i$'s earnings one year later if they participate, and: $Y_i(0)$ be worker $i$'s earnings one year later if they do not participate. The individual treatment effect is: $\tau_i = Y_i(1)-Y_i(0)$ Suppose the observed data show: $\mathbb{E}[Y_i \mid D_i=1] = 36{,}000$ and: $\mathbb{E}[Y_i \mid D_i=0] = 32{,}000$ The naive difference is: $36{,}000 - 32{,}000 = 4{,}000$ Can we conclude that training raises earnings by \$4,000? Not necessarily. The naive difference is: $\mathbb{E}[Y_i(1) \mid D_i=1] - \mathbb{E}[Y_i(0) \mid D_i=0]$ But the ATT is: $\mathbb{E}[Y_i(1) \mid D_i=1] - \mathbb{E}[Y_i(0) \mid D_i=1]$ The missing counterfactual is: $\mathbb{E}[Y_i(0) \mid D_i=1]$ What would participants have earned without training? If participants were more motivated than nonparticipants, they might have earned \$34,000 even without training. Then: $ATT = 36{,}000 - 34{,}000 = 2{,}000$ The naive estimate overstates the effect. If participants were more disadvantaged and would have earned only \$28,000 without training, then: $ATT = 36{,}000 - 28{,}000 = 8{,}000$ The naive estimate understates the effect. If participants would have earned \$32,000 without training, then the naive estimate equals the ATT: $ATT = 36{,}000 - 32{,}000 = 4{,}000$ The empirical challenge is to determine which counterfactual is credible. Possible research designs:

- Randomly offer training to eligible workers.
- Use a lottery when program slots are limited.
- Compare workers just above and below an eligibility cutoff.
- Use random assignment to encouragement as an instrument for participation.
- Use difference-in-differences if comparable nonparticipants followed similar pre-program trends.
- Use panel fixed effects if workers are observed over time and selection is related to stable traits.

Each design is an attempt to estimate the missing term: $\mathbb{E}[Y_i(0) \mid D_i=1]$

## 2.19 Practical example: minimum wages and employment
Suppose a state raises its minimum wage and employment falls afterward.

The observed fact is: $Employment_{after} < Employment_{before}$ But the causal question is not whether employment fell after the policy. The causal question is:

> What would employment have been in the state after the policy date if the minimum wage had not increased?

Let: $Y_{st}(1)$ be employment in state $s$ at time $t$ if the higher minimum wage is in effect, and: $Y_{st}(0)$ be employment in state $s$ at time $t$ if the higher minimum wage is not in effect. For the treated state after the policy, we observe: $Y_{st}(1)$ but we do not observe: $Y_{st}(0)$ The missing counterfactual is what employment would have been without the policy. Employment may have fallen because of the minimum wage. But it may also have fallen because of a recession, industry decline, seasonal changes, population shifts, or another policy. A difference-in-differences design tries to approximate the missing counterfactual using a control group. The key assumption is that, absent the minimum wage increase, the treated state would have followed a trend similar to the control states. Again, the issue is counterfactual credibility.

## 2.20 Common mistakes in counterfactual reasoning

1. **Mistake 1: Treating before-after comparisons as automatically causal.** If an outcome changes after treatment, the change is not necessarily caused by treatment.
Before-after comparisons can be biased by time trends, shocks, seasonality, mean reversion, anticipation, or other simultaneous changes. The question is not:

> Did the outcome change after treatment?

The question is:

> How did the outcome compare to what would have happened without treatment?

2. **Mistake 2: Treating untreated units as automatically comparable.** Untreated units are not automatically a valid counterfactual for treated units.
They may differ in motivation, resources, baseline outcomes, geography, institutions, demographics, or exposure to other policies. A comparison group must be justified, not assumed.

3. **Mistake 3: Ignoring treatment definition.** A vague treatment leads to an unclear causal effect.
For example, "the effect of education" is not a single well-defined effect unless the intervention is specified.

4. **Mistake 4: Conditioning on post-treatment variables.** Controlling for variables affected by treatment can block part of the causal effect or introduce bias.
Researchers must distinguish pre-treatment confounders from post-treatment mediators, colliders, and outcomes.

5. **Mistake 5: Ignoring spillovers.** If treatment affects untreated units, then untreated units may no longer represent the no-treatment counterfactual.
Examples include peer effects, disease transmission, labor market displacement, neighborhood spillovers, and general equilibrium effects.

6. **Mistake 6: Confusing prediction with counterfactual prediction.** A model may predict outcomes well without estimating causal effects.
For example, prior earnings may predict future earnings, but that does not mean changing prior earnings would change future earnings. Prediction models learn associations. Causal models require assumptions about interventions.

## 2.21 Application checklist
When approaching a causal question, use the following checklist.

1. **Define the unit.** What is the unit of analysis?
Examples: individuals, firms, schools, neighborhoods, cities, countries, years, markets.

2. **Define the treatment.** What exactly is the intervention?
Is it binary, multi-valued, continuous, or repeated over time? Is the treatment well defined? Are there multiple versions or intensities?

3. **Define the outcome.** What outcome is being measured?
When is it measured? Is it affected by measurement error? Does it capture the concept of interest?

4. **Define potential outcomes.** What is $Y_i(1)$?
What is $Y_i(0)$? For continuous treatment, what is $Y_i(d)$?

5. **Define the estimand.** Are you interested in ATE, ATT, ATU, CATE, LATE, a distributional effect, or a dynamic effect?
For whom is the effect defined? Over what time horizon?

6. **Identify the missing counterfactual.** For treated units, what untreated outcome is missing?
For untreated units, what treated outcome is missing? Which missing potential outcome matters for the estimand?

7. **Propose a comparison group.** What observed group or variation will stand in for the missing counterfactual?
Why should that comparison be credible?

8. **State the identifying assumption.** What assumption connects the observed comparison to the causal estimand?
Examples:

- random assignment,
- conditional independence,
- parallel trends,
- continuity at a cutoff,
- exclusion restriction,
- no time-varying confounding,
- no interference.

9. **Assess the assumption.** Can the assumption be tested directly?
If not, what indirect evidence supports it? Examples:

- balance tests,
- pre-trend tests,
- placebo tests,
- manipulation tests,
- institutional details,
- robustness checks,
- sensitivity analysis.

10. **Interpret the result.** What causal effect was estimated?
For whom? Under what conditions? What assumptions are required? What are the main threats? Does the result generalize?

## 2.22 Summary
Counterfactual thinking is the foundation of causal inference.

For each unit, potential outcomes describe what would happen under different treatment states. With binary treatment, these are: $Y_i(1)$ and: $Y_i(0)$ The individual causal effect is: $\tau_i = Y_i(1)-Y_i(0)$ But only one potential outcome is observed for each unit. This is the fundamental problem of causation. The observed outcome is: $Y_i = D_iY_i(1) + (1-D_i)Y_i(0)$ Causal inference is therefore about finding credible substitutes for missing potential outcomes. Naive treated-control comparisons are causal only under strong assumptions. In general: $Observed\ Difference = Causal\ Effect + Selection\ Bias$ Research designs such as RCTs, difference-in-differences, regression discontinuity, instrumental variables, fixed effects, matching, and weighting are different strategies for constructing credible counterfactuals. The most important question in empirical work is not simply what the data show. It is:

> Why does the observed comparison tell us what would have happened under the relevant counterfactual?

A rigorous causal analysis defines the treatment, outcome, unit, estimand, missing counterfactual, comparison group, identifying assumptions, threats to validity, and scope of interpretation. The central lesson is:

> Causal inference is disciplined counterfactual reasoning. It uses data and assumptions to compare the world that occurred with the relevant world that did not occur.

# 3. DAGs and Causal Graphs

## 3.1 Why causal graphs matter
Empirical economics is not only about estimating equations. It is also about reasoning carefully about the structure that generated the data. Before deciding what to control for, what comparison group to use, or what research design is credible, a researcher needs a theory of how the relevant variables are causally related.

A causal graph is a way to make that theory explicit. A **DAG**, or directed acyclic graph, is a diagram that represents causal relationships among variables. DAGs are useful because they force the researcher to state assumptions about what causes what. They help distinguish confounders from mediators, colliders, outcomes, instruments, and bad controls. They also clarify which variables should be adjusted for and which variables should not be adjusted for. This matters because causal inference is not solved by automatically adding more control variables. Some controls reduce bias. Other controls introduce bias. The difference depends on the causal structure. For example, suppose we want to estimate the causal effect of education on earnings. A simple causal story might be: $Ability \rightarrow Education \rightarrow Earnings$ and: $Ability \rightarrow Earnings$ This graph says that ability affects education and also directly affects earnings. If ability is omitted, the observed relationship between education and earnings partly reflects ability. In this case, ability is a confounder. Now consider occupation: $Education \rightarrow Occupation \rightarrow Earnings$ Occupation is different from ability. It is not a pre-existing cause of education. It is partly caused by education and lies on the path from education to earnings. If we control for occupation while trying to estimate the total effect of education, we may block part of the effect we want to estimate. The lesson is:

> Whether a variable is a good control depends on its position in the causal graph.

DAGs provide a language for making these distinctions precise.

## 3.2 What a DAG is
A DAG has three components:

1. **Nodes**, which represent variables.
2. **Directed edges**, or arrows, which represent direct causal effects.
3. **Acyclicity**, which means the graph contains no directed cycles.

The word **directed** means arrows have a direction. If $X$ causes $Y$, we write: $X \rightarrow Y$ The word **acyclic** means there is no sequence of arrows that leads from a variable back to itself. For example, the following is not allowed in a DAG: $X \rightarrow Y \rightarrow Z \rightarrow X$ That structure is cyclic because $X$ eventually causes itself through a feedback loop. Many economic systems involve feedback over time. For example, income affects education choices, and education affects later income. This can still be represented with a DAG if we index variables by time: $Income_{t-1} \rightarrow Education_t \rightarrow Income_{t+1}$ The graph remains acyclic because the arrows move forward in time. The key is to avoid representing simultaneous feedback as if it were a static one-period DAG unless the time ordering is made explicit. A DAG is not just a picture. It is a set of assumptions. When we draw: $X \rightarrow Y$ we are claiming that changing $X$ can directly change $Y$, holding other direct causes constant. When we do not draw an arrow between two variables, we are also making an assumption: there is no direct causal effect between them, at least within the level of detail represented in the graph. Thus, DAGs are useful precisely because they make causal assumptions visible.

## 3.3 Causal parents, children, ancestors, and descendants
Causal graphs use family-language terminology.

If there is an arrow: $X \rightarrow Y$ then $X$ is a **parent** of $Y$, and $Y$ is a **child** of $X$. If there is a longer directed path: $X \rightarrow M \rightarrow Y$ then $X$ is an **ancestor** of $Y$, and $Y$ is a **descendant** of $X$. A **direct cause** is represented by a single arrow. An **indirect cause** operates through one or more intermediate variables. For example: $Education \rightarrow Skills \rightarrow Productivity \rightarrow Wages$ Education is a direct cause of skills, skills are a direct cause of productivity, and productivity is a direct cause of wages. Education is an indirect cause of productivity and wages through the pathway shown. This distinction matters because a causal effect can be total or direct. The **total effect** of education on wages includes all pathways from education to wages: $Education \rightarrow Skills \rightarrow Productivity \rightarrow Wages$ $Education \rightarrow Credentials \rightarrow Employer\ Beliefs \rightarrow Wages$ $Education \rightarrow Networks \rightarrow Job\ Opportunities \rightarrow Wages$ A **direct effect** asks for the effect of education on wages holding some mediating variables fixed. Direct effects are often harder to interpret because holding a mediator fixed may require imagining an intervention that blocks part of the natural causal process.

## 3.4 Paths
A **path** is any route connecting two variables through arrows, regardless of arrow direction.

For example, in the graph: $X \leftarrow C \rightarrow Y$ there is a path from $X$ to $Y$ through $C$: $X \leftarrow C \rightarrow Y$ Even though the arrows do not all point from $X$ to $Y$, this path connects $X$ and $Y$ statistically. A **directed path** is a path where all arrows point in the same direction from one variable to another. For example: $X \rightarrow M \rightarrow Y$ is a directed path from $X$ to $Y$. A directed path represents a causal pathway. A **non-causal path** is a path connecting treatment and outcome that does not represent the causal effect of interest. Non-causal paths are often sources of bias. For example: $Education \leftarrow Ability \rightarrow Earnings$ is a non-causal path from education to earnings. It connects education and earnings through ability, but it does not represent education causing earnings. Instead, ability causes both education and earnings. One of the central tasks of causal graph analysis is to identify which paths should remain open and which paths should be blocked.

## 3.5 Confounders
A **confounder** is a variable that causally affects both the treatment and the outcome.

The basic structure is: $C \rightarrow X$ and: $C \rightarrow Y$ where $X$ is the treatment or explanatory variable of interest, $Y$ is the outcome, and $C$ is the confounder. Equivalently: $X \leftarrow C \rightarrow Y$ This structure creates a non-causal association between $X$ and $Y$. For example: $Ability \rightarrow Education$ and: $Ability \rightarrow Earnings$ If we want the effect of education on earnings, ability is a confounder. People with greater ability may obtain more education and earn more regardless of education. Therefore, a comparison of more-educated and less-educated people may overstate the causal effect of education. Another example: $Baseline\ Health \rightarrow Medical\ Treatment$ and: $Baseline\ Health \rightarrow Later\ Health$ If sicker patients are more likely to receive treatment and also more likely to have poor later health, baseline health confounds the relationship between treatment and later health. A confounder opens a **backdoor path** from treatment to outcome. In the education example, the backdoor path is: $Education \leftarrow Ability \rightarrow Earnings$ To estimate the causal effect of education on earnings, this path must be blocked. One possible way is to control for ability, if ability is observed and measured well. Another is to use a design that makes education independent of ability, such as random assignment or a credible natural experiment. The key point is:

> Confounding occurs when treatment and outcome share a common cause.

## 3.6 Mediators
A **mediator** is a variable that lies on the causal pathway from treatment to outcome.

The basic structure is: $X \rightarrow M \rightarrow Y$ Here $X$ affects $M$, and $M$ affects $Y$. The variable $M$ transmits part or all of the effect of $X$ on $Y$. For example: $Education \rightarrow Occupation \rightarrow Earnings$ Occupation is a mediator between education and earnings. Education affects what occupations people enter, and occupation affects earnings. Another example: $Job\ Training \rightarrow Skills \rightarrow Employment$ Skills are a mediator between job training and employment. Mediators are not confounders. A confounder comes before the treatment and causes both treatment and outcome. A mediator comes after the treatment and is part of the mechanism through which treatment affects the outcome. This distinction is crucial for control-variable decisions. If the goal is to estimate the **total effect** of $X$ on $Y$, controlling for a mediator is usually a mistake because it blocks part of the causal effect. Suppose the true causal chain is: $Education \rightarrow Occupation \rightarrow Earnings$ If we regress earnings on education while controlling for occupation, we are no longer estimating the total effect of education on earnings. We are estimating something closer to the effect of education holding occupation fixed. That may answer a legitimate question, but it is a different question. The total effect asks:

> What happens to earnings if education changes, allowing occupation to change as it naturally would?

The controlled direct effect asks:

> What happens to earnings if education changes but occupation is held fixed?

Both questions can be meaningful, but they are not the same.

## 3.7 Colliders
A **collider** is a variable that is caused by two other variables.

The basic structure is: $X \rightarrow C \leftarrow Y$ The variable $C$ is called a collider because two arrows collide into it. Colliders are important because conditioning on them can create a false association between their causes. Suppose both talent and luck affect admission to an elite school: $Talent \rightarrow Admission \leftarrow Luck$ In the general population, talent and luck may be independent. But among admitted students, talent and luck can become negatively associated. If a student had less luck, they needed more talent to be admitted. If a student had less talent, they needed more luck to be admitted. By conditioning on admission, we create an association between talent and luck even if none existed in the population. This is collider bias. Another example comes from labor markets. Suppose both worker ability and family connections affect employment at an elite firm: $Ability \rightarrow Elite\ Firm\ Job \leftarrow Connections$ Among people hired by the elite firm, ability and connections may be negatively correlated. Someone with weaker connections may need very high ability to be hired. Someone with lower ability may need strong connections. If we analyze only elite-firm employees, we are conditioning on a collider. This can distort relationships among the variables that caused selection into the sample. Colliders are one reason why selected samples are dangerous. Examples of possible colliders include:

- college admission,
- employment status,
- hospitalization,
- loan approval,
- program participation,
- survey response,
- survival,
- publication,
- being observed in a dataset.

The key rule is:

> Do not condition on a common effect of treatment and outcome, or on a variable affected by common causes of treatment and outcome, unless the causal question specifically requires it and the consequences are understood.

## 3.8 Conditioning and control variables
To **condition on** a variable means to restrict, stratify, adjust, regress on, match on, weight by, or otherwise hold that variable fixed in the analysis.

Common forms of conditioning include:

- including a variable as a regression control,
- matching treated and untreated units on that variable,
- stratifying the sample by that variable,
- restricting the sample to one value of the variable,
- weighting observations using that variable,
- selecting observations based on that variable.

DAGs help determine whether conditioning is helpful or harmful. Conditioning on a confounder can block a non-causal path: $X \leftarrow C \rightarrow Y$ If we control for $C$, we block the path from $X$ to $Y$ through $C$. Conditioning on a mediator can block part of the causal effect: $X \rightarrow M \rightarrow Y$ If we control for $M$, we remove the part of the effect that flows through $M$. Conditioning on a collider can open a non-causal path: $X \rightarrow C \leftarrow Y$ If we control for $C$, we create an association between $X$ and $Y$ through $C$. This is why the command “control for more variables” is not a general solution to causal inference. Controls must be chosen based on causal reasoning. The question is not:

> Is this variable correlated with the outcome?

The better question is:

> What role does this variable play in the causal graph?

## 3.9 Open and closed paths
A path between two variables can be **open** or **closed**.

An open path allows statistical association to flow between variables. A closed path blocks statistical association. The rules depend on the type of structure.

- **Chains.** A chain has the form: $X \rightarrow M \rightarrow Y$
or: $X \leftarrow M \leftarrow Y$
or: $X \leftarrow M \rightarrow Y$
If we do not condition on $M$, the path is open. If we condition on $M$, the path is closed.

For example: $Education \rightarrow Occupation \rightarrow Earnings$ Without conditioning on occupation, education and earnings are associated through this path. If we condition on occupation, we block this pathway.

- **Forks.** A fork has the form: $X \leftarrow C \rightarrow Y$
This is the confounding structure. The path is open unless we condition on $C$.

For example: $Education \leftarrow Ability \rightarrow Earnings$ Controlling for ability blocks this non-causal path.

- **Colliders.** A collider has the form: $X \rightarrow C \leftarrow Y$
This path is closed by default. But conditioning on $C$ opens it.

For example: $Talent \rightarrow Admission \leftarrow Luck$ In the full population, talent and luck may be unrelated. But conditioning on admission opens the path and makes talent and luck associated among admitted students. This collider rule is one of the most unintuitive but important lessons in causal inference.

## 3.10 D-separation
**D-separation**, short for directional separation, is a graphical criterion for determining whether two variables are independent conditional on a set of variables in a DAG.

The full formal theory can become technical, but the applied intuition is straightforward. A conditioning set $Z$ d-separates $X$ and $Y$ if, after conditioning on $Z$, all paths between $X$ and $Y$ are closed. If all non-causal paths between treatment $X$ and outcome $Y$ are closed, then the remaining association between $X$ and $Y$ can be interpreted as causal, provided the graph is correct and other assumptions hold. The path-closing rules are:

1. For a chain $X \rightarrow M \rightarrow Y$, conditioning on $M$ blocks the path.
2. For a fork $X \leftarrow C \rightarrow Y$, conditioning on $C$ blocks the path.
3. For a collider $X \rightarrow C \leftarrow Y$, the path is blocked unless we condition on $C$ or a descendant of $C$.

The third rule includes descendants. If: $X \rightarrow C \leftarrow Y$ and: $C \rightarrow S$ then conditioning on $S$ can also open the collider path. For example: $Ability \rightarrow Job\ Offer \leftarrow Connections$ and: $Job\ Offer \rightarrow Employment$ Conditioning on employment may partially condition on the collider job offer, inducing association between ability and connections. D-separation is useful because it gives a rule-based way to evaluate adjustment strategies. It asks:

> After controlling for these variables, are the unwanted paths between treatment and outcome blocked?

## 3.11 Backdoor paths
A **backdoor path** from treatment $X$ to outcome $Y$ is a path that begins with an arrow into $X$.

For example: $X \leftarrow C \rightarrow Y$ is a backdoor path from $X$ to $Y$ because it starts with an arrow pointing into $X$. Backdoor paths are important because they create non-causal association between treatment and outcome. Suppose the causal effect of interest is: $Education \rightarrow Earnings$ but the graph also contains: $Ability \rightarrow Education$ and: $Ability \rightarrow Earnings$ Then the full graph contains a backdoor path: $Education \leftarrow Ability \rightarrow Earnings$ This path creates confounding. To estimate the causal effect of education on earnings, we need to block this path. A backdoor path does not necessarily involve only one confounder. It can be longer: $X \leftarrow C_1 \rightarrow C_2 \rightarrow Y$ or: $X \leftarrow C_1 \leftarrow C_2 \rightarrow Y$ The general problem is the same: association flows from $X$ to $Y$ through a path that is not part of the causal effect of $X$ on $Y$. The goal of adjustment is to block backdoor paths without blocking causal paths and without opening collider paths.

## 3.12 The backdoor criterion
A set of variables $Z$ satisfies the **backdoor criterion** relative to treatment $X$ and outcome $Y$ if:

1. no variable in $Z$ is a descendant of $X$, and
2. $Z$ blocks every path between $X$ and $Y$ that begins with an arrow into $X$.

If a set $Z$ satisfies the backdoor criterion, then adjusting for $Z$ identifies the causal effect of $X$ on $Y$. Under the backdoor criterion, the causal effect can be written as: $P(Y \mid do(X=x)) = \sum_z P(Y \mid X=x, Z=z)P(Z=z)$ For continuous $Z$, the sum becomes an integral: $P(Y \mid do(X=x)) = \int P(Y \mid X=x, Z=z) f_Z(z)\,dz$ In expectation form, the adjustment idea is: $\mathbb{E}[Y \mid do(X=x)] = \sum_z \mathbb{E}[Y \mid X=x, Z=z]P(Z=z)$ This formula says: compare treated and untreated units within levels of the control variables, then average those comparisons over the distribution of the controls. For example, if ability $A$ is the only confounder between education and earnings, then:

$$
\mathbb{E}[Earnings \mid do(Education=e)]
= \sum_a \mathbb{E}[Earnings \mid Education=e, Ability=a]P(Ability=a)
$$

This adjustment works only if the graph is correct and ability is measured appropriately. The backdoor criterion is powerful because it gives a principled answer to the question:

> What should I control for?

But it also gives a warning:

> Do not control for variables simply because they are available. Control for variables that block backdoor paths, and avoid variables that create new bias.

## 3.13 Bad controls
A **bad control** is a variable that should not be controlled for because doing so changes the estimand or introduces bias.

Bad controls often include:

1. mediators,
2. colliders,
3. descendants of colliders,
4. variables affected by treatment,
5. post-treatment outcomes,
6. selection variables,
7. variables that proxy for a collider or post-treatment process.

- **Bad control: mediator.** Suppose: $Education \rightarrow Occupation \rightarrow Earnings$
If we control for occupation while estimating the effect of education on earnings, we block one mechanism through which education affects earnings. This may underestimate the total effect.

- **Bad control: collider.** Suppose: $Motivation \rightarrow Program\ Participation \leftarrow Eligibility$
If we restrict the sample to participants, we condition on a collider. This can create an association between motivation and eligibility even if they were otherwise unrelated.

- **Bad control: post-treatment variable.** Suppose: $Job\ Training \rightarrow Job\ Search \rightarrow Employment$
Job search after training may be part of the treatment effect. Controlling for post-training job search changes the question. It no longer estimates the total effect of training.

- **Bad control: outcome proxy.** Suppose a researcher estimates the effect of education on wages but controls for current occupation, current firm, and current job title. These variables may all be consequences of education. Adding them may remove much of the effect the researcher intended to estimate.
The concept of bad controls is especially important in applied work because many datasets contain rich variables measured after treatment. Rich data can increase bias if used thoughtlessly.

## 3.14 Good controls
A **good control** is a variable that helps block non-causal paths without blocking causal paths or opening collider paths.

Good controls are often pre-treatment confounders. For example, suppose: $Family\ Background \rightarrow Education$ and: $Family\ Background \rightarrow Earnings$ If family background is measured before education decisions and affects both education and earnings, then controlling for family background may help reduce confounding. Other examples of potentially good controls:

- baseline income before a program,
- pre-treatment health status,
- prior test scores before an education intervention,
- age before treatment,
- pre-policy industry composition,
- geographic characteristics determined before treatment,
- historical variables that affect treatment assignment and outcome.

However, whether a control is good depends on the graph. Prior test scores may be a good control when estimating the effect of tutoring on later test scores. But if prior test scores are themselves affected by earlier exposure to the same program, they may be post-treatment relative to a longer-run treatment process. The timing and causal role of the variable matter. A useful rule is:

> Prefer controls that are determined before treatment and that plausibly cause both treatment and outcome. Be cautious with variables determined after treatment.

## 3.15 Minimal sufficient adjustment sets
A **sufficient adjustment set** is a set of variables that blocks all backdoor paths from treatment to outcome.

A **minimal sufficient adjustment set** is a sufficient set where no variable can be removed without reopening a backdoor path. Suppose the graph is: $C_1 \rightarrow X \rightarrow Y$ $C_1 \rightarrow Y$ $C_2 \rightarrow X$ $C_2 \rightarrow Y$ Then both $C_1$ and $C_2$ confound the effect of $X$ on $Y$. A sufficient adjustment set is: $\{C_1, C_2\}$ If both are necessary to block different backdoor paths, then this set is minimal. But suppose: $C_1 \rightarrow C_2 \rightarrow X$ and: $C_1 \rightarrow Y$ The backdoor path is: $X \leftarrow C_2 \leftarrow C_1 \rightarrow Y$ Controlling for $C_1$ may block the path. Controlling for $C_2$ may also block the path. Depending on the full graph, either may be sufficient. The minimal adjustment set is not always “all pre-treatment variables.” This matters for precision and interpretation. Including unnecessary controls can increase variance, introduce measurement error, or create post-treatment bias if timing is misclassified. The goal is not the largest possible set of controls. The goal is a justified sufficient set.

## 3.16 Overcontrol bias
**Overcontrol bias** occurs when a researcher controls for variables that lie on the causal pathway from treatment to outcome.

Suppose: $D \rightarrow M \rightarrow Y$ If the researcher controls for $M$, the estimated effect of $D$ on $Y$ excludes the part of the effect that operates through $M$. For example: $Education \rightarrow Skills \rightarrow Wages$ If we control for skills, we may remove an important part of the effect of education. Another example: $Minimum\ Wage \rightarrow Firm\ Prices \rightarrow Employment$ If we control for firm prices when estimating the effect of the minimum wage on employment, we may block a mechanism through which minimum wages affect employment. Overcontrol bias is not always a mistake. Sometimes the researcher intentionally wants a direct effect. But it is a mistake if the researcher claims to estimate the total effect while controlling for mediators. The key question is:

> Is this variable a cause of treatment, or is it caused by treatment?

Pre-treatment causes may be confounders. Post-treatment consequences may be mediators, colliders, or outcomes.

## 3.17 Selection bias as conditioning on a collider
Selection bias can often be represented as collider bias.

Suppose both treatment and outcome affect whether an observation appears in the sample: $D \rightarrow Sample \leftarrow Y$ If we analyze only sampled observations, we condition on $Sample=1$. Since $Sample$ is a collider, conditioning on it can create an association between $D$ and $Y$. For example, suppose we study the relationship between startup strategy and firm performance using only surviving firms. $Strategy \rightarrow Survival \leftarrow Unobserved\ Firm\ Quality$ If survival depends on both strategy and unobserved quality, then conditioning on survival can distort the relationship between strategy and performance. This is survivorship bias. Another example is hospitalization: $Disease\ Severity \rightarrow Hospitalization \leftarrow Insurance\ Status$ Among hospitalized patients, disease severity and insurance status may be associated in ways that do not reflect their relationship in the broader population. Publication bias can also be understood this way: $True\ Effect \rightarrow Publication \leftarrow Statistical\ Significance$ If published studies are selected based on significance and effect size, the published literature may overstate true effects. Thinking about selection as collider conditioning helps explain why sample construction is part of causal design.

## 3.18 DAGs and omitted variable bias
DAGs provide a graphical interpretation of omitted variable bias.

Suppose the true structure is: $Z \rightarrow X \rightarrow Y$ and: $Z \rightarrow Y$ If $Z$ is omitted, the backdoor path: $X \leftarrow Z \rightarrow Y$ remains open. The estimated association between $X$ and $Y$ combines the causal effect of $X$ on $Y$ with the non-causal association induced by $Z$. In regression terms, suppose the true model is: $Y = \alpha + \beta X + \gamma Z + u$ but the estimated model omits $Z$: $Y = \alpha + \tilde{\beta}X + e$ The omitted variable $Z$ becomes part of the error term: $e = \gamma Z + u$ If $Z$ is correlated with $X$, then: $\operatorname{Cov}(X,e) \neq 0$ The DAG explains why this covariance is nonzero: $Z$ is a common cause of $X$ and $Y$. The graphical and regression views are two ways of describing the same problem.

## 3.19 DAGs and regression controls
Regression adjustment can be understood through DAGs.

Suppose we estimate: $Y_i = \alpha + \beta X_i + \gamma Z_i + u_i$ The coefficient $\beta$ compares units with different values of $X_i$ but the same value of $Z_i$, at least in the linear-regression sense. If $Z$ is a confounder, this may help identify the causal effect of $X$ on $Y$. If $Z$ is a mediator, it may block part of the effect. If $Z$ is a collider, it may introduce bias. If $Z$ is unrelated to the causal structure, it may improve precision, reduce precision, or do little. Thus, the meaning of a regression coefficient depends on the causal role of the controls. This is especially important when interpreting “holding all else equal.” In regression, holding a variable fixed is a statistical operation. In causal inference, we need to ask whether holding that variable fixed corresponds to the causal comparison we want. For example, estimating the effect of education on wages while controlling for occupation means comparing workers with different education levels but the same occupation. That is not necessarily the total effect of education, because education may affect which occupation a worker enters. Regression adjustment is a tool. DAGs help determine whether the tool is being used correctly.

## 3.20 DAGs and instrumental variables
DAGs also clarify instrumental variables.

An instrument $Z$ for the effect of treatment $X$ on outcome $Y$ should satisfy three core graphical conditions. First, relevance: $Z \rightarrow X$ The instrument must affect treatment. Second, exclusion: $Z \nrightarrow Y \quad \text{except through } X$ The instrument must not directly affect the outcome through any path other than treatment. Third, independence: $Z \perp U$ where $U$ represents unobserved causes of $Y$. A simple valid IV graph is: $Z \rightarrow X \rightarrow Y$ with: $U \rightarrow X$ and: $U \rightarrow Y$ The instrument $Z$ shifts $X$, while $U$ confounds the relationship between $X$ and $Y$. If $Z$ is independent of $U$ and affects $Y$ only through $X$, then $Z$ can isolate variation in $X$ that is not confounded by $U$. A bad instrument might have a direct effect: $Z \rightarrow Y$ or share a cause with the outcome: $U \rightarrow Z$ and: $U \rightarrow Y$ DAGs do not prove that an instrument is valid. But they make the required assumptions visible.

## 3.21 DAGs and difference-in-differences
Difference-in-differences can also be described using causal graphs, although its key assumption is usually expressed in terms of potential outcomes and trends.

In a DiD setting, treatment adoption may be confounded by underlying trends. For example: $Economic\ Decline \rightarrow Policy\ Adoption$ and: $Economic\ Decline \rightarrow Employment\ Trend$ If states adopt a policy because employment is already declining, then treated and control states may not have parallel counterfactual trends. A DAG can help identify possible sources of non-parallel trends:

- prior economic shocks,
- demographic changes,
- political changes,
- industry composition,
- local institutions,
- anticipation effects,
- simultaneous policies.

The DiD assumption is not merely statistical. It is a causal claim about what would have happened to treated units without treatment. A causal graph can help ask:

> What factors affected both treatment timing and outcome trends?

Those factors are threats to identification.

## 3.22 DAGs and regression discontinuity
In regression discontinuity, treatment changes at a cutoff of a running variable.

For example: $Score \rightarrow Treatment$ and: $Treatment \rightarrow Outcome$ The running variable may also affect the outcome smoothly: $Score \rightarrow Outcome$ RD is credible near the cutoff if potential outcomes are continuous in the running variable and units cannot precisely manipulate treatment status. A DAG can help represent manipulation threats: $Ability \rightarrow Score$ $Ability \rightarrow Outcome$ If ability affects score smoothly, comparing students close to the cutoff may still be credible. But if students or administrators manipulate scores to cross the cutoff, then treatment status near the cutoff may be related to unobserved determinants of the outcome. For example: $Motivation \rightarrow Manipulation \rightarrow Crossing\ Cutoff$ and: $Motivation \rightarrow Outcome$ This creates a threat to RD validity. DAGs help identify what could cause sorting around the cutoff and whether those causes also affect the outcome.

## 3.23 DAGs and mechanisms
DAGs are especially useful for thinking about mechanisms.

Suppose a policy affects an outcome through several channels: $Policy \rightarrow Income \rightarrow Health$ $Policy \rightarrow Insurance\ Coverage \rightarrow Health$ $Policy \rightarrow Stress \rightarrow Health$ The total effect of the policy includes all of these pathways. If researchers want to understand mechanisms, they may examine intermediate outcomes. But they must be careful. Controlling for a mediator changes the estimand. For example, if the policy affects health partly through income, then controlling for income removes that part of the effect. The resulting coefficient does not represent the total effect of the policy. Mechanism analysis often asks questions like:

- Does the policy affect the mediator?
- Does the mediator affect the outcome?
- How much of the total effect operates through this pathway?
- Are there multiple mediators?
- Are there mediator-outcome confounders?
- Are those confounders affected by treatment?

These questions are more complex than simply adding mediators to a regression.

## 3.24 DAGs and time ordering
Causal graphs should respect time.

A cause must occur before its effect. Therefore, when drawing a DAG, it is often useful to label variables by time. For example: $Health_{t-1} \rightarrow Employment_t \rightarrow Health_{t+1}$ This graph says prior health affects current employment, and current employment affects later health. If we instead draw: $Health \leftrightarrow Employment$ we lose the time ordering. Since DAGs do not allow cycles, dynamic relationships should be represented with time subscripts. Time ordering also helps avoid bad controls. Pre-treatment variables may be confounders: $X_{pre} \rightarrow D \rightarrow Y_{post}$ and: $X_{pre} \rightarrow Y_{post}$ Post-treatment variables may be mediators: $D \rightarrow M_{post} \rightarrow Y_{post}$ or colliders: $D \rightarrow S_{post} \leftarrow U \rightarrow Y_{post}$ Controlling for variables measured after treatment can therefore be dangerous. A practical rule is:

> Draw the graph with time subscripts whenever timing is important.

## 3.25 Unobserved variables in DAGs
Not all relevant variables are observed.

DAGs can include unobserved variables, often represented as $U$. For example: $U \rightarrow X$ and: $U \rightarrow Y$ Here $U$ is an unobserved confounder. It might represent ability, motivation, health, risk preference, political pressure, institutional quality, or some other omitted factor. If $U$ is unobserved, we cannot simply control for it. We need another strategy. Possible strategies include:

- randomization,
- instrumental variables,
- fixed effects if $U$ is time-invariant,
- difference-in-differences if $U$ affects levels but not trends,
- regression discontinuity if $U$ changes smoothly at the cutoff,
- proxy controls if valid proxies are available,
- sensitivity analysis,
- bounding,
- structural modeling.

A graph with unobserved confounding is useful because it clarifies why ordinary regression may fail. For example: $Ability \rightarrow Education \rightarrow Earnings$ and: $Ability \rightarrow Earnings$ If ability is unobserved, the backdoor path remains open. Controlling for observed variables such as age or gender may not solve the problem unless they block the relevant path or proxy for ability under defensible assumptions.

## 3.26 Proxies and measurement
Researchers often use proxy variables for unobserved concepts.

For example:

- test scores as proxies for ability,
- parental education as a proxy for family background,
- prior earnings as a proxy for labor market skill,
- neighborhood poverty as a proxy for local disadvantage,
- firm size as a proxy for productivity,
- credit score as a proxy for default risk.

Proxies can help, but they rarely solve confounding perfectly. Suppose true ability $A$ confounds education and earnings: $A \rightarrow Education$ $A \rightarrow Earnings$ We observe a test score $T$: $A \rightarrow T$ Controlling for $T$ may reduce confounding, but unless $T$ fully captures the relevant variation in $A$, residual confounding may remain. Measurement error in controls can therefore leave backdoor paths partially open. DAGs can help distinguish between controlling for the true confounder and controlling for an imperfect proxy.

## 3.27 Front-door adjustment as an advanced idea
Most introductory causal graph analysis focuses on backdoor adjustment. But there is also a **front-door criterion**, which can identify causal effects in some cases even when there is unobserved confounding between treatment and outcome.

Suppose the graph is: $X \rightarrow M \rightarrow Y$ with unobserved confounding between $X$ and $Y$: $U \rightarrow X$ $U \rightarrow Y$ Ordinary adjustment for $U$ is impossible if $U$ is unobserved. But if all of the effect of $X$ on $Y$ flows through mediator $M$, and if certain additional conditions hold, the causal effect may be identified through the mediator. The front-door criterion requires, roughly:

1. $M$ intercepts all directed paths from $X$ to $Y$,
2. there is no unblocked backdoor path from $X$ to $M$,
3. all backdoor paths from $M$ to $Y$ are blocked by conditioning on $X$.

The front-door formula is more advanced and less commonly used in applied economics than backdoor adjustment, IV, DiD, or RD. But it illustrates an important point:

> Causal graphs can reveal identification strategies that are not obvious from regression equations alone.

## 3.28 Causal graphs versus regression equations
Regression equations and DAGs serve different purposes.

A regression equation describes a statistical model, such as: $Y_i = \alpha + \beta X_i + \gamma Z_i + u_i$ A DAG describes causal assumptions, such as: $Z \rightarrow X \rightarrow Y$ and: $Z \rightarrow Y$ The regression equation tells us what is being estimated statistically. The DAG tells us whether the estimate can be interpreted causally. A regression coefficient can be computed without a causal graph. But interpreting it causally requires assumptions about the causal graph, whether stated explicitly or not. DAGs are therefore not a replacement for statistical modeling. They are a complement to it. Good empirical work connects:

1. the causal question,
2. the causal graph,
3. the identification strategy,
4. the statistical estimator,
5. the assumptions needed for interpretation.

## 3.29 Common mistakes when using DAGs

1. **Mistake 1: Treating DAGs as proven facts.** A DAG is not discovered automatically from data in most applied settings. It is a representation of assumptions, theory, institutional knowledge, and prior evidence.
The graph may be wrong. If the graph is wrong, the adjustment strategy based on it may also be wrong.

2. **Mistake 2: Drawing arrows for correlation rather than causation.** An arrow should represent a causal effect, not merely an association.
If education and earnings are correlated, that alone does not justify: $Education \rightarrow Earnings$ The arrow represents the claim that intervening on education would change earnings.

3. **Mistake 3: Omitting important variables.** A graph that leaves out important common causes may falsely suggest that no adjustment is needed.
If ability affects both education and earnings but is omitted from the graph, the graph may understate confounding.

4. **Mistake 4: Controlling for descendants of treatment.** Variables caused by treatment are often not appropriate controls for total effects.
For example, occupation may be caused by education. Controlling for occupation may block part of the education effect.

5. **Mistake 5: Conditioning on colliders.** Restricting a sample, controlling for selection variables, or analyzing only observed cases can induce collider bias.
6. **Mistake 6: Ignoring time.** A static DAG may hide dynamic feedback. Variables should be indexed by time when ordering matters.
7. **Mistake 7: Believing one graph is enough.** In many empirical settings, several causal graphs may be plausible. Researchers should consider alternative graphs and ask whether conclusions are robust to different assumptions.

## 3.30 Application example: education and earnings
Suppose we want to estimate the effect of education on earnings.

A naive causal graph is: $Education \rightarrow Earnings$ If this were the whole graph, a simple comparison of earnings by education level might be causal. But this is unlikely. A more realistic graph includes ability and family background: $Family\ Background \rightarrow Education$ $Family\ Background \rightarrow Earnings$ $Ability \rightarrow Education$ $Ability \rightarrow Earnings$ $Education \rightarrow Earnings$ There are backdoor paths: $Education \leftarrow Family\ Background \rightarrow Earnings$ and: $Education \leftarrow Ability \rightarrow Earnings$ These paths confound the education-earnings relationship. Now add occupation: $Education \rightarrow Occupation \rightarrow Earnings$ Occupation is a mediator. If we want the total effect of education, we should not control for occupation. If we do, we block part of the causal effect. Now add college admission: $Ability \rightarrow College\ Admission \leftarrow Family\ Background$ If we analyze only admitted students, we condition on a collider. That may distort the relationship between ability and family background. This example shows why control choices depend on the causal graph. A reasonable adjustment strategy might control for pre-treatment family background variables and pre-treatment measures of ability, while avoiding post-education variables such as occupation, industry, and firm type if the goal is the total effect. But even this may not solve all problems if ability is imperfectly measured. That is why researchers often seek stronger designs, such as compulsory schooling reforms, school-entry cutoffs, twin designs, or instrumental variables.

## 3.31 Application example: policing and crime
Suppose we want to estimate the effect of police presence on crime.

A naive graph is: $Police \rightarrow Crime$ But crime also affects police deployment: $Crime \rightarrow Police$ In a static DAG, this is a cycle. To represent it properly, use time: $Crime_{t-1} \rightarrow Police_t \rightarrow Crime_{t+1}$ There may also be confounders: $Poverty \rightarrow Police$ $Poverty \rightarrow Crime$ $Political\ Pressure \rightarrow Police$ $Political\ Pressure \rightarrow Crime\ Reporting$ Police presence may affect measured crime differently from actual crime: $Police \rightarrow Detection \rightarrow Reported\ Crime$ This means the outcome definition matters. Are we studying reported crime, victimization, arrests, emergency calls, or true underlying crime? A credible design might use sudden changes in police deployment due to terror alerts, shift changes, weather shocks, or administrative boundaries, provided those changes are not themselves caused by expected crime. The DAG helps identify why ordinary cross-sectional comparisons are weak and what kind of variation would be more credible.

## 3.32 Application example: medical treatment and health
Suppose we want to estimate the effect of a medical treatment on health.

A naive graph is: $Treatment \rightarrow Health$ But baseline severity affects treatment: $Severity \rightarrow Treatment$ and: $Severity \rightarrow Health$ This creates confounding: $Treatment \leftarrow Severity \rightarrow Health$ A naive comparison may show treated patients have worse outcomes because they were sicker to begin with. Now suppose hospitalization is used as a sample restriction: $Severity \rightarrow Hospitalization \leftarrow Insurance$ If we analyze only hospitalized patients, we condition on hospitalization, a collider. This can induce an association between severity and insurance. Medical examples make clear that more controls and more restrictions do not automatically improve causal inference. The researcher must understand how patients enter treatment and how they enter the dataset.

## 3.33 Practical workflow for using DAGs
When applying DAGs to an empirical question, use the following workflow.

1. **Define the causal effect of interest.** What is the treatment $X$?
What is the outcome $Y$? What is the intervention? What is the estimand?

2. **List possible causes of treatment.** What determines whether units receive treatment?
Examples: preferences, eligibility, institutions, prices, prior outcomes, geography, ability, health, political conditions.

3. **List possible causes of the outcome.** What determines the outcome besides treatment?
Examples: baseline characteristics, shocks, resources, institutions, prior outcomes, unobserved traits.

4. **Identify common causes.** Which variables cause both treatment and outcome?
These are potential confounders.

5. **Identify mediators.** Which variables are caused by treatment and then affect the outcome?
These are mechanisms, not ordinary controls for total effects.

6. **Identify colliders and selection variables.** Was the sample selected based on treatment, outcome, or their causes?
Are there variables caused by two other variables that might be conditioned on?

7. **Determine adjustment set.** Which variables block backdoor paths?
Which variables should be avoided? Is the adjustment set measured before treatment?

8. **Consider unobserved variables.** What important variables are missing?
Can they be proxied? Is a different research design needed?

9. **Connect graph to research design.** Does the graph support regression adjustment, matching, IV, DiD, RD, fixed effects, or another design?
What assumptions are required?

10. **Test and probe what can be tested.** DAG assumptions are often not fully testable, but researchers can examine:
- balance on observed covariates,
- pre-treatment trends,
- manipulation around cutoffs,
- placebo outcomes,
- sensitivity to controls,
- alternative samples,
- institutional details,
- robustness to alternative graphs.

## 3.34 Summary
DAGs are diagrams that encode causal assumptions. They consist of variables connected by directed arrows and contain no directed cycles.

They help researchers reason about:

- confounding,
- mediation,
- collider bias,
- selection bias,
- backdoor paths,
- adjustment sets,
- bad controls,
- mechanisms,
- identification strategies.

The most important structures are: Confounding: $X \leftarrow C \rightarrow Y$ Mediation: $X \rightarrow M \rightarrow Y$ Collider bias: $X \rightarrow C \leftarrow Y$ A good control blocks non-causal backdoor paths. A bad control blocks causal paths or opens non-causal paths. The backdoor criterion gives a formal rule for choosing adjustment variables. A set $Z$ is valid if it blocks all backdoor paths from treatment to outcome and contains no descendants of treatment. DAGs do not prove causality by themselves. They make assumptions explicit. Their value comes from forcing the researcher to state what causes what, what is observed, what is unobserved, what is being conditioned on, and what comparison is supposed to identify the causal effect. The central lesson is:

> Control variables are not automatically good or bad. Their value depends on the causal graph. DAGs provide a disciplined way to decide what should be adjusted for, what should be left alone, and what assumptions are required for a causal interpretation.

# 4. Exogeneity and Endogeneity

## 4.1 Why exogeneity and endogeneity matter
Exogeneity and endogeneity are among the most important concepts in empirical economics. They determine whether a statistical relationship can be interpreted as causal.

In ordinary language, a variable is **exogenous** if it is determined outside the system being studied. A variable is **endogenous** if it is determined inside the system being studied or is related to unobserved factors that also affect the outcome. In causal inference and econometrics, the distinction is more precise. A variable is exogenous relative to a model if the variation used to estimate its effect is unrelated to the unobserved determinants of the outcome. A variable is endogenous if it is correlated with those unobserved determinants. Consider the regression: $Y_i = \alpha + \beta X_i + u_i$ where:

- $Y_i$ is the outcome,
- $X_i$ is the explanatory variable, treatment, exposure, or policy variable,
- $u_i$ is the error term,
- $\beta$ is the coefficient of interest.

If we want to interpret $\beta$ causally, we need more than a regression line. We need the variation in $X_i$ to be unrelated to the unobserved causes of $Y_i$ contained in $u_i$. The key condition is often written as: $\mathbb{E}[u_i \mid X_i] = 0$ This says that, conditional on $X_i$, the average value of the error term is zero. Equivalently, the unobserved determinants of $Y_i$ are not systematically related to $X_i$. If this condition holds, $X_i$ is exogenous in the regression model. If this condition fails, $X_i$ is endogenous. The difference matters because ordinary least squares estimates conditional associations. Those associations become causal only when the identifying assumptions justify treating variation in $X_i$ as independent of the relevant counterfactual outcomes or unobserved determinants of $Y_i$. In simple terms:

> Exogeneity is what allows a regression coefficient to have a causal interpretation.

Endogeneity is what breaks that interpretation.

---

## 4.2 Exogeneity is relative to a model
A common mistake is to treat variables as intrinsically exogenous or endogenous.

This is not quite right. Exogeneity is not a permanent property of a variable. It is a property of a variable **relative to a particular model, causal question, population, and source of variation**. For example, weather is often treated as exogenous in economic studies. If a researcher studies the effect of rainfall on agricultural output, rainfall may be plausibly outside farmers' control: $Rainfall \rightarrow Crop\ Yield$ In that setting, rainfall may provide useful exogenous variation. But even rainfall is not automatically exogenous in every research design. Suppose richer farmers live in regions with better irrigation, better soil, and different long-run rainfall patterns. If rainfall exposure is measured using location, and location is related to wealth, infrastructure, crop choice, and technology, then rainfall may be entangled with other determinants of output. Similarly, price is often endogenous in demand estimation because price is determined by supply and demand together. But in some settings, a price may be exogenously changed by a randomized subsidy, a tax rule, an administrative formula, or a supply shock unrelated to demand. Thus, the same variable can be endogenous in one design and exogenous in another. Examples:

- Education is usually endogenous in a wage regression because people choose education, but education induced by a compulsory schooling law may provide more plausibly exogenous variation.
- Price is usually endogenous in a demand regression, but price variation caused by randomized discounts may be exogenous.
- Police presence is usually endogenous in a crime regression because police are deployed to high-crime areas, but police deployment caused by a randomized patrol experiment may be exogenous.
- Healthcare use is usually endogenous in a health regression because sick people seek care, but insurance coverage assigned by lottery may create exogenous variation in access.

The right question is not:

> Is $X$ exogenous?

The right question is:

> Is the variation in $X$ used by this research design plausibly unrelated to the unobserved determinants of $Y$ for the causal effect being estimated?

---

## 4.3 The regression error term as unobserved causes
In regression, the error term is not just random noise. For causal interpretation, it is useful to think of the error term as containing all determinants of the outcome that are not explicitly included in the model.

Suppose the outcome is wages: $Wage_i = \alpha + \beta Education_i + u_i$ The error term $u_i$ may contain:

- ability,
- motivation,
- family background,
- parental education,
- neighborhood quality,
- school quality,
- health,
- social networks,
- local labor market conditions,
- discrimination,
- personality,
- job search effort,
- luck.

If these unobserved determinants are unrelated to education, then education may be exogenous. But if people with more education also tend to have higher ability, stronger family support, better schools, or better networks, then: $\mathbb{E}[u_i \mid Education_i] \neq 0$ or equivalently: $\operatorname{Cov}(Education_i,u_i) \neq 0$ In that case, education is endogenous. The coefficient $\beta$ no longer isolates the causal effect of education. It captures both the effect of education and the influence of omitted factors correlated with education. This is why the error term is conceptually important. Endogeneity means the explanatory variable is partly standing in for omitted causes.

---

## 4.4 Conditional mean independence
The most common exogeneity condition for cross-sectional regression is **conditional mean independence**: $\mathbb{E}[u_i \mid X_i] = 0$
This means the expected value of the error term is zero at every value of $X_i$.

For a regression with controls: $Y_i = \alpha + \beta X_i + \gamma'W_i + u_i$ where $W_i$ is a vector of control variables, the condition becomes: $\mathbb{E}[u_i \mid X_i,W_i] = 0$ This says that after conditioning on both $X_i$ and $W_i$, the unobserved determinants of $Y_i$ have mean zero. For causal interpretation of $\beta$, the key idea is usually:

> Among units with the same controls $W_i$, variation in $X_i$ is as good as random.

For example, suppose we estimate the effect of job training on earnings: $Earnings_i = \alpha + \beta Training_i + \gamma'W_i + u_i$ where $W_i$ includes age, education, prior earnings, prior employment, location, and industry. The coefficient $\beta$ can be interpreted causally only if, after comparing workers with the same values of $W_i$, training participation is unrelated to unobserved determinants of earnings. That means there must be no remaining unobserved motivation, ability, private information, caseworker selection, health, family constraint, or employer connection that affects both training participation and earnings. This is a strong assumption. Adding controls does not automatically solve endogeneity. It solves endogeneity only if the controls are sufficient to make the remaining variation in treatment conditionally exogenous.

---

## 4.5 Covariance form of exogeneity
A weaker-looking condition often used in regression is: $\operatorname{Cov}(X_i,u_i)=0$
This says the explanatory variable is uncorrelated with the error term.

For simple ordinary least squares, if: $Y_i = \alpha + \beta X_i + u_i$ then the OLS estimator is centered on the true slope when: $\operatorname{Cov}(X_i,u_i)=0$ If instead: $\operatorname{Cov}(X_i,u_i) \neq 0$ then OLS is biased or inconsistent for the causal parameter. The conditional mean assumption: $\mathbb{E}[u_i \mid X_i]=0$ implies: $\operatorname{Cov}(X_i,u_i)=0$ but the reverse is not always true. Conditional mean independence is stronger because it requires the average error to be zero at each value of $X_i$, not merely that the linear covariance be zero. For causal inference, the conditional version is usually more meaningful because it says that unobserved determinants of the outcome are not systematically related to treatment status.

---

## 4.6 Exogeneity in potential outcomes language
In the potential outcomes framework, exogeneity is often stated as an independence condition.

For a binary treatment $D_i$, define potential outcomes: $Y_i(1)$ and: $Y_i(0)$ where $Y_i(1)$ is the outcome under treatment and $Y_i(0)$ is the outcome without treatment. A strong exogeneity condition is random assignment: $D_i \perp \big(Y_i(1),Y_i(0)\big)$ This means treatment assignment is independent of both potential outcomes. Under random assignment: $\mathbb{E}[Y_i(1) \mid D_i=1] = \mathbb{E}[Y_i(1) \mid D_i=0]$ and: $\mathbb{E}[Y_i(0) \mid D_i=1] = \mathbb{E}[Y_i(0) \mid D_i=0]$ Therefore, the untreated group can serve as a credible counterfactual for the treated group, and the treated group can serve as a credible counterfactual for the untreated group. In observational studies, researchers often invoke conditional independence: $D_i \perp \big(Y_i(1),Y_i(0)\big) \mid X_i$ This means treatment is independent of potential outcomes after conditioning on observed covariates $X_i$. In plain English:

> Within groups of units with the same observed characteristics, treatment assignment is as good as random.

This assumption is also called:

- unconfoundedness,
- ignorability,
- selection on observables,
- conditional exchangeability.

It is the potential-outcomes version of saying that, conditional on controls, treatment is exogenous.

---

## 4.7 Exogeneity in DAG language
In causal graphs, endogeneity often appears as an open backdoor path between treatment and outcome.

Suppose we want the effect of education on wages: $Education \rightarrow Wage$ But ability affects both education and wages: $Ability \rightarrow Education$ $Ability \rightarrow Wage$ The full structure is: $Education \leftarrow Ability \rightarrow Wage$ and: $Education \rightarrow Wage$ The path: $Education \leftarrow Ability \rightarrow Wage$ is a backdoor path. It creates association between education and wages that is not caused by education. If ability is unobserved and omitted from the model, then ability is part of the error term: $u_i = \text{unobserved determinants of } Wage_i$ Because ability affects education, education is correlated with the error term: $\operatorname{Cov}(Education_i,u_i) \neq 0$ This is endogeneity. In DAG terms, exogeneity requires that the research design block non-causal paths from treatment to outcome while leaving the causal path of interest open. This can be achieved by:

- randomization,
- conditioning on appropriate confounders,
- using an instrumental variable,
- exploiting a discontinuity,
- comparing trends under parallel trends,
- using fixed effects for time-invariant confounding,
- using other credible designs.

The important point is that exogeneity is not a purely statistical property. It is a causal claim about how treatment is assigned relative to potential outcomes and unobserved causes.

---

## 4.8 Strict exogeneity in panel data
Panel data observe the same units over time. In panel models, economists often use stronger exogeneity conditions.

A basic panel model is: $Y_{it} = \alpha_i + \beta X_{it} + u_{it}$ where:

- $i$ indexes units,
- $t$ indexes time,
- $\alpha_i$ is a unit fixed effect,
- $X_{it}$ is a time-varying explanatory variable,
- $u_{it}$ is the time-varying error term.

A common condition is **strict exogeneity**: $\mathbb{E}[u_{it} \mid X_{i1},X_{i2},\dots,X_{iT},\alpha_i] = 0$ This says that the error term at time $t$ is unrelated to the explanatory variable in every time period: past, present, and future. This is stronger than requiring only: $\mathbb{E}[u_{it} \mid X_{it},\alpha_i] = 0$ Strict exogeneity can fail when future treatment responds to past shocks. Example: A worker experiences a negative wage shock in year $t$: $u_{it} < 0$ In response, the worker enrolls in job training in year $t+1$: $Training_{i,t+1}=1$ Then the future treatment variable is related to the current error term: $\operatorname{Cov}(Training_{i,t+1},u_{it}) \neq 0$ Strict exogeneity fails. This matters because fixed effects models often rely on within-unit variation over time. If changes in treatment are responses to prior unobserved shocks, the within-unit comparison may still be endogenous. Examples where strict exogeneity may fail:

- A firm adopts technology after an unobserved demand shock.
- A worker enters training after a negative earnings shock.
- A city increases policing after a crime shock.
- A government changes policy in response to worsening economic conditions.
- A patient begins treatment after symptoms worsen.

Fixed effects remove time-invariant confounding. They do not automatically solve time-varying endogeneity.

---

## 4.9 Sequential exogeneity
In dynamic settings, researchers sometimes rely on **sequential exogeneity** rather than strict exogeneity.

Sequential exogeneity allows treatment at time $t$ to depend on past observed history, but not on future unobserved shocks. A simplified version is: $\mathbb{E}[u_{it} \mid X_{i1},\dots,X_{it},Y_{i1},\dots,Y_{i,t-1},W_{i1},\dots,W_{it}] = 0$ This means that after conditioning on observed history, the current treatment is not related to current unobserved determinants of the outcome. Sequential exogeneity is common in longitudinal causal inference. Example: Suppose patients receive treatment over time based on past health. If researchers observe the full health history used to assign treatment, then treatment may be conditionally exogenous given that history. But if treatment depends on unobserved symptoms or private information not in the data, sequential exogeneity fails. Sequential exogeneity is especially important when treatments and confounders change over time. It underlies methods such as:

- marginal structural models,
- inverse probability weighting,
- dynamic treatment regime analysis,
- some panel data designs.

The practical lesson is:

> In panel settings, one must ask not only whether treated and untreated units differ, but whether changes in treatment timing are responses to unobserved shocks.

---

## 4.10 Main sources of endogeneity
Endogeneity can arise from several sources. The most common are:

1. omitted variable bias,
2. reverse causality,
3. simultaneity,
4. selection bias,
5. measurement error,
6. dynamic feedback,
7. bad controls,
8. model misspecification.

Each source creates a relationship between the explanatory variable and the error term. Formally, endogeneity means: $\mathbb{E}[u_i \mid X_i] \neq 0$ or: $\operatorname{Cov}(X_i,u_i) \neq 0$ Conceptually, endogeneity means the observed variation in $X_i$ is not clean causal variation. The following subsections explain each source in detail.

---

## 4.11 Omitted variable bias
Omitted variable bias occurs when an excluded variable affects the outcome and is correlated with an included explanatory variable.

Suppose the true model is: $Y_i = \alpha + \beta X_i + \gamma Z_i + \varepsilon_i$ but we estimate: $Y_i = \alpha + \tilde{\beta}X_i + u_i$ The omitted variable $Z_i$ becomes part of the error term: $u_i = \gamma Z_i + \varepsilon_i$ If $Z_i$ is correlated with $X_i$, then $X_i$ is correlated with the error term: $\operatorname{Cov}(X_i,u_i) = \operatorname{Cov}(X_i,\gamma Z_i + \varepsilon_i)$ If: $\operatorname{Cov}(X_i,Z_i) \neq 0$ and: $\gamma \neq 0$ then omitted variable bias occurs. In the simple case, the bias is:

$$
\operatorname{Bias}(\tilde{\beta})
=
\gamma \frac{\operatorname{Cov}(X_i,Z_i)}{\operatorname{Var}(X_i)}
$$

This formula shows that the direction of bias depends on two things:

1. whether $Z_i$ increases or decreases $Y_i$,
2. whether $Z_i$ is positively or negatively correlated with $X_i$.

Example: education and wages. Let:

- $Y_i = Wage_i$,
- $X_i = Education_i$,
- $Z_i = Ability_i$.

If ability raises wages, then: $\gamma > 0$ If ability is positively correlated with education, then: $\operatorname{Cov}(Education_i,Ability_i)>0$ Therefore, the bias is positive: $\operatorname{Bias}(\tilde{\beta})>0$ The estimated return to education overstates the causal effect. Omitted variable bias is the classic form of endogeneity.

---

## 4.12 Reverse causality
Reverse causality occurs when the outcome affects the explanatory variable.

Suppose we estimate: $Crime_c = \alpha + \beta Police_c + u_c$ A positive estimate of $\beta$ might seem to suggest that police increase crime. But cities with high crime may hire more police. Then the causal direction runs from crime to police: $Crime \rightarrow Police$ In that case, police presence is not randomly assigned. It responds to crime conditions, including some that may be unobserved by the researcher. If unobserved crime risk affects police deployment, then: $\operatorname{Cov}(Police_c,u_c) \neq 0$ The regression coefficient does not isolate the effect of police on crime. Other examples:

- Sicker patients receive more treatment.
- Poorer countries receive more foreign aid.
- Firms advertise more when demand is rising.
- Governments spend more during recessions.
- Students seek tutoring after poor performance.
- Workers enter training after job loss.

Reverse causality is especially common when individuals, firms, or governments actively respond to the outcome being studied. The practical diagnostic question is:

> Could the outcome or expected outcome influence the treatment variable?

If yes, endogeneity is likely.

---

## 4.13 Simultaneity and equilibrium determination
Simultaneity occurs when $X$ and $Y$ are jointly determined.

This is central in economics because many variables are equilibrium outcomes. Consider demand and supply: $Q^d = a - bP + \varepsilon^d$ $Q^s = c + dP + \varepsilon^s$ In equilibrium: $Q^d = Q^s = Q$ Price $P$ and quantity $Q$ are determined together. A regression of quantity on price: $Q_i = \alpha + \beta P_i + u_i$ does not automatically estimate the demand curve. If demand shocks raise both price and quantity, observed data may show a positive relationship between price and quantity even though demand slopes downward. The problem is that price is endogenous. It reflects both demand shocks and supply shocks. To identify demand, researchers need variation in price caused by supply factors that are unrelated to demand. To identify supply, researchers need variation in price caused by demand factors that are unrelated to supply. Simultaneity appears in many settings:

- wages and labor supply,
- prices and quantities,
- interest rates and investment,
- rent and housing supply,
- crime and policing,
- healthcare use and insurance coverage,
- school quality and neighborhood housing prices.

The general lesson is:

> When variables are determined together in equilibrium, ordinary regression may describe equilibrium correlations rather than causal effects.

---

## 4.14 Selection bias
Selection bias arises when treatment status or sample inclusion is related to potential outcomes.

Suppose treatment is voluntary. People who choose treatment may differ from people who do not. Example: job training. Workers who enroll in training may be more motivated, better informed, more available, more desperate, or more connected than workers who do not enroll. The naive comparison is: $\mathbb{E}[Y_i \mid D_i=1] - \mathbb{E}[Y_i \mid D_i=0]$ This equals:

$$
\mathbb{E}[Y_i(1) \mid D_i=1]
-
\mathbb{E}[Y_i(0) \mid D_i=0]
$$

But the average treatment effect on the treated is: $ATT = \mathbb{E}[Y_i(1)-Y_i(0) \mid D_i=1]$ or:

$$
ATT = \mathbb{E}[Y_i(1) \mid D_i=1]
-
\mathbb{E}[Y_i(0) \mid D_i=1]
$$

The missing counterfactual is: $\mathbb{E}[Y_i(0) \mid D_i=1]$ The naive comparison uses: $\mathbb{E}[Y_i(0) \mid D_i=0]$ Selection bias arises when:

$$
\mathbb{E}[Y_i(0) \mid D_i=1]
\neq
\mathbb{E}[Y_i(0) \mid D_i=0]
$$

Selection creates endogeneity because treatment status is related to potential outcomes and unobserved determinants of the outcome. Selection bias can occur through:

- voluntary participation,
- administrative targeting,
- eligibility rules,
- nonresponse,
- attrition,
- survivorship,
- selective migration,
- selective program take-up,
- selective compliance.

A central task of empirical design is to make treated and untreated units comparable with respect to their counterfactual outcomes.

---

## 4.15 Measurement error
Measurement error is another source of endogeneity.

Suppose the true model is: $Y_i = \alpha + \beta X_i^* + u_i$ where $X_i^*$ is the true explanatory variable. But researchers observe a mismeasured version: $X_i = X_i^* + e_i$ where $e_i$ is measurement error. If we regress $Y_i$ on the observed $X_i$, then the regression error contains the difference between true and measured $X$. In the classical measurement error case, where $e_i$ is random noise independent of $X_i^*$ and $u_i$, the OLS coefficient is biased toward zero. This is called **attenuation bias**. The intuition is simple: measurement error adds noise to the explanatory variable. If observed education, income, pollution, or treatment exposure is measured with error, then the estimated relationship between the measured variable and the outcome may be weaker than the true relationship. Examples:

- Self-reported income may be mismeasured.
- Years of schooling may not measure actual skill acquisition.
- Pollution exposure may be measured at a regional monitor rather than individual location.
- Program participation may be recorded incorrectly.
- Crime may be underreported.
- Health status may be measured with survey error.

Measurement error can be more complicated than simple attenuation. If measurement error is correlated with the outcome, treatment, or other covariates, the direction of bias may be unpredictable. For example, if high-income people underreport income differently from low-income people, measurement error is not classical. If pollution monitors are placed in certain neighborhoods, measured pollution may be systematically related to neighborhood characteristics. Measurement quality is therefore not a minor technical issue. It affects identification and interpretation.

---

## 4.16 Dynamic feedback
Dynamic feedback occurs when past outcomes influence future treatments or exposures.

Example: job training. A worker's earnings fall in year $t$: $Earnings_{it} \downarrow$ The worker responds by enrolling in training in year $t+1$: $Training_{i,t+1}=1$ If the original earnings decline was partly due to unobserved factors, then future training is related to past unobserved shocks. This creates endogeneity in panel data. Dynamic feedback is common in economics because agents respond to past outcomes. Examples:

- Students seek tutoring after low test scores.
- Firms invest after demand shocks.
- Governments change policy after recessions.
- Patients seek treatment after symptoms worsen.
- Police are deployed after crime increases.
- Households migrate after income shocks.
- Banks adjust lending after defaults rise.

Dynamic feedback creates problems for simple before-after and fixed effects designs. If treatment timing is a response to shocks, then comparing outcomes before and after treatment may confound treatment effects with the shocks that caused treatment. A rigorous design must distinguish:

- treatment causing outcome changes,
- outcome changes causing treatment,
- both being driven by earlier shocks.

---

## 4.17 Bad controls as a source of endogeneity
Controls are not automatically good. Some controls can create bias.

A **bad control** is a variable that should not be conditioned on for the causal question being asked. Common bad controls include:

- mediators,
- colliders,
- variables affected by treatment,
- post-treatment outcomes,
- selection indicators.

- **Mediator control.** Suppose: $Education \rightarrow Occupation \rightarrow Wage$
If we want the total effect of education on wages, controlling for occupation blocks part of the causal pathway. The coefficient on education then no longer represents the total effect.

- **Collider control.** Suppose: $Talent \rightarrow Admission \leftarrow Luck$
Conditioning on admission can induce an association between talent and luck, even if they are unrelated in the population.

If treatment and outcome both affect selection into the sample, controlling for or restricting to selected observations can create collider bias.

- **Post-treatment control.** Suppose: $Treatment \rightarrow Health \rightarrow Employment$
If employment is the outcome and health is affected by treatment, controlling for post-treatment health may block a mechanism or introduce bias.

The key rule is:

> Choose controls based on causal structure, not on whether they improve predictive fit.

A control variable can reduce omitted variable bias, do nothing, or make bias worse.

---

## 4.18 Model misspecification
Model misspecification can also create misleading estimates.

A model may be misspecified if:

- the functional form is wrong,
- important interactions are omitted,
- nonlinearities are ignored,
- treatment effects are heterogeneous,
- the wrong comparison group is used,
- the timing of effects is misspecified,
- the outcome or treatment is poorly defined,
- the level of aggregation is inappropriate.

Example: Suppose the true relationship between class size and learning is nonlinear. Reducing class size from 40 to 30 may have a large effect, while reducing it from 20 to 10 may have a smaller effect. A linear model may average these effects in a misleading way. Another example: Suppose a minimum wage affects teen workers differently from adult workers. A single average coefficient may hide important heterogeneity. Misspecification does not always fit neatly into the simple formula: $\operatorname{Cov}(X_i,u_i) \neq 0$ but it can still undermine causal interpretation by making the estimated coefficient correspond to an unclear or irrelevant estimand. The solution is not merely to make models more complex. The solution is to align the model with the causal question, theory, data structure, and research design.

---

## 4.19 How research designs create exogenous variation
Because endogeneity is common, empirical economists look for research designs that generate or isolate exogenous variation.

The goal is to find variation in treatment that is unrelated to potential outcomes except through treatment. Different designs do this in different ways.

- **Randomized controlled trials.** Randomization makes treatment assignment independent of potential outcomes: $D_i \perp \big(Y_i(1),Y_i(0)\big)$
This is the clearest form of exogeneity.

- **Natural experiments.** Natural experiments use events, rules, or shocks that create variation in treatment that is plausibly as-good-as-random.
Examples include lotteries, administrative cutoffs, judge assignment, weather shocks, or sudden policy changes.

- **Instrumental variables.** An instrument $Z_i$ creates exogenous variation in an endogenous treatment $X_i$ if it satisfies relevance and exclusion.
Relevance: $\operatorname{Cov}(Z_i,X_i) \neq 0$ Exclusion: $Z_i \text{ affects } Y_i \text{ only through } X_i$ The instrument isolates the part of $X_i$ that is plausibly exogenous.

- **Regression discontinuity.** Regression discontinuity uses a cutoff rule. Units just above and below the cutoff are assumed to be comparable except for treatment assignment.
The key idea is that near the cutoff, treatment status changes sharply while other determinants of outcomes change smoothly.

- **Difference-in-differences.** Difference-in-differences uses changes over time in treated and control groups. It assumes that, absent treatment, treated and control groups would have followed parallel trends.
This creates a counterfactual trend for the treated group.

- **Fixed effects.** Fixed effects remove time-invariant unobserved differences across units. They use within-unit variation over time.
They help when endogeneity comes from stable unobserved traits, but they do not solve time-varying confounding. The common theme is:

> Exogeneity comes from the research design, not from the regression command.

---

## 4.20 Diagnosing endogeneity
Endogeneity cannot usually be proven or disproven with a single statistical test. It is a causal concern that requires theory, institutional knowledge, and empirical evidence.

Still, researchers can look for warning signs.

1. **Warning sign 1: Treatment is chosen by agents.** If individuals, firms, schools, doctors, or governments choose treatment based on expected outcomes, endogeneity is likely.
2. **Warning sign 2: Treatment responds to the outcome.** If the treatment is assigned in response to the outcome or expected outcome, reverse causality is likely.
3. **Warning sign 3: Treated and untreated units differ at baseline.** Large baseline differences suggest selection or confounding.
4. **Warning sign 4: Pre-trends differ.** In panel or policy settings, different trends before treatment undermine simple comparisons and difference-in-differences designs.
5. **Warning sign 5: Treatment timing is predictable.** If treatment adoption can be predicted by prior outcomes or trends, treatment timing may be endogenous.
6. **Warning sign 6: Results change dramatically with controls.** Large sensitivity to controls may suggest confounding, though stability alone does not prove causality.
7. **Warning sign 7: Placebo outcomes show effects.** If treatment appears to affect outcomes that it could not plausibly affect, the design may be capturing confounding.
8. **Warning sign 8: There is no plausible assignment story.** If the researcher cannot explain why variation in treatment is plausibly exogenous, causal interpretation is weak.
Useful diagnostic tools include:

- balance tests,
- pre-trend plots,
- placebo tests,
- falsification tests,
- robustness checks,
- sensitivity analysis,
- institutional analysis,
- alternative comparison groups,
- event-study graphs,
- manipulation tests in RD,
- first-stage diagnostics in IV.

Diagnostics do not mechanically prove exogeneity. They build or weaken the credibility of the identifying assumptions.

---

## 4.21 Exogeneity, prediction, and causation
A variable can be useful for prediction even if it is endogenous.

For example, hospital admission predicts poor health. But that does not mean hospital admission causes poor health. Sick people are more likely to be admitted. Similarly, police presence may predict crime, but police presence may be high because crime risk is high. Prediction asks: $\mathbb{E}[Y \mid X=x]$ Causation asks: $\mathbb{E}[Y \mid do(X=x)]$ Endogeneity is not necessarily a problem for prediction. If the goal is only to forecast $Y$, an endogenous variable may be highly useful. But endogeneity is a major problem for causal inference. If the goal is to know what would happen if $X$ changed, then the source of variation in $X$ matters. Example: Suppose a model predicts that people taking medication have worse health outcomes. This may be useful for risk prediction. But it would be wrong to conclude that medication causes worse health if sicker people are more likely to take medication. The lesson is:

> Predictive usefulness does not imply causal validity.

---

## 4.22 Practical example: education and wages
Suppose we estimate: $\log(Wage_i) = \alpha + \beta Education_i + u_i$
A positive $\beta$ means that workers with more education earn more, on average.

Can we interpret $\beta$ as the causal return to education? Only if: $\mathbb{E}[u_i \mid Education_i]=0$ This requires that unobserved determinants of wages are unrelated to education. But education is likely related to:

- ability,
- family background,
- parental education,
- school quality,
- motivation,
- social networks,
- neighborhood,
- health,
- labor market opportunities.

If these factors affect wages and are omitted, then: $\operatorname{Cov}(Education_i,u_i) \neq 0$ Education is endogenous. Adding controls may help: $\log(Wage_i) = \alpha + \beta Education_i + \gamma'W_i + u_i$ where $W_i$ includes observed background variables. But causal interpretation still requires: $\mathbb{E}[u_i \mid Education_i,W_i]=0$ If unobserved ability or motivation remains, endogeneity remains. Possible research designs include:

- compulsory schooling reforms,
- school entry age rules,
- distance to college as an instrument,
- twin or sibling comparisons,
- panel designs,
- regression discontinuity around admission thresholds.

Each design attempts to isolate variation in education that is less related to unobserved determinants of wages. The key question is not whether education predicts wages. It clearly does. The key causal question is whether the variation in education used by the study is exogenous.

---

## 4.23 Practical example: police and crime
Suppose we estimate: $Crime_{ct} = \alpha + \beta Police_{ct} + u_{ct}$
where $c$ indexes cities and $t$ indexes time.

A positive coefficient may reflect reverse causality: $Crime \rightarrow Police$ Cities increase police presence when crime rises. A negative coefficient may also be difficult to interpret because cities that invest in policing may also invest in other crime-reduction strategies. The error term may include:

- gang activity,
- drug markets,
- poverty shocks,
- local economic conditions,
- demographic changes,
- political pressure,
- reporting rates,
- other policies.

If these factors affect police deployment, then: $\operatorname{Cov}(Police_{ct},u_{ct}) \neq 0$ Police presence is endogenous. Possible research designs include:

- randomized patrol allocation,
- sudden police redeployment due to external events,
- terrorism alerts affecting police presence,
- administrative rules for staffing,
- difference-in-differences around policy changes,
- instrumental variables affecting police deployment but not crime directly.

Again, the causal question is:

> What would crime have been if police presence had been different?

A credible answer requires exogenous variation in police presence.

---

## 4.24 Practical example: price and demand
Suppose a firm wants to estimate demand: $Quantity_i = \alpha + \beta Price_i + u_i$
The firm expects $\beta<0$: higher prices reduce quantity demanded.

But observed price variation may be endogenous. If demand is high, the firm may raise prices and sell more units. This can create a positive association between price and quantity even if the demand curve slopes downward. The problem is: $\operatorname{Cov}(Price_i,u_i) \neq 0$ where $u_i$ includes demand shocks. Possible solutions:

- randomized price experiments,
- coupons randomly assigned to consumers,
- supply cost shocks,
- tax changes,
- inventory shocks,
- exchange rate shocks for imported goods,
- instruments that shift price but not demand directly.

The key idea is to find price variation not caused by demand shocks. This example shows why endogeneity is not just a statistical concern. It is tied to economic behavior and equilibrium.

---

## 4.25 Practical example: healthcare and health outcomes
Suppose we estimate: $Health_i = \alpha + \beta MedicalCare_i + u_i$
A naive regression may show that people receiving more medical care have worse health outcomes.

This does not necessarily mean medical care harms health. Sick people receive more care. The causal structure is: $Underlying\ Health_i \rightarrow MedicalCare_i$ and: $Underlying\ Health_i \rightarrow Health_i$ Underlying health is often imperfectly observed. If it is in the error term, then: $\operatorname{Cov}(MedicalCare_i,u_i) \neq 0$ Medical care is endogenous. Possible research designs include:

- randomized insurance expansions,
- lotteries for Medicaid access,
- distance to hospitals,
- physician prescribing variation,
- policy changes affecting coverage,
- regression discontinuities in eligibility rules.

The key question is not whether people who receive more care are healthier or sicker. The key question is what would have happened to their health if they had received a different amount or type of care.

---

## 4.26 Application checklist
When evaluating whether a variable is exogenous or endogenous, use the following checklist.

1. **Define the causal question.** What effect are you trying to estimate?
What is the treatment or explanatory variable? What is the outcome?

2. **Define the model.** What is the regression or empirical specification?
Example: $Y_i = \alpha + \beta X_i + \gamma'W_i + u_i$ What is included in $u_i$?

3. **Interpret the error term.** What unobserved factors affect $Y_i$?
Could they include ability, motivation, demand shocks, health, institutional quality, expectations, or selection forces?

4. **Ask whether those factors are related to $X_i$.** Is: $\mathbb{E}[u_i \mid X_i,W_i]=0$
plausible?

Or is it likely that: $\operatorname{Cov}(X_i,u_i) \neq 0$

5. **Identify the source of variation in $X_i$.** What variation identifies $\beta$?
Is it cross-sectional variation, within-unit variation, policy timing, a cutoff, an instrument, a shock, or random assignment?

6. **Check for omitted variables.** Could a third variable affect both $X_i$ and $Y_i$?
If yes, is it observed and properly controlled for?

7. **Check for reverse causality.** Could $Y_i$ or expected $Y_i$ affect $X_i$?
8. **Check for simultaneity.** Are $X_i$ and $Y_i$ jointly determined in equilibrium?
9. **Check for selection.** Do units select into treatment?
Are treated and untreated units systematically different?

10. **Check timing.** Does treatment occur before the outcome?
Could treatment timing respond to prior shocks? Are there anticipation effects?

11. **Check measurement.** Is $X_i$ measured accurately?
Is $Y_i$ measured accurately? Is measurement error classical or systematic?

12. **Check controls.** Are controls pre-treatment confounders?
Or are they mediators, colliders, or post-treatment variables?

13. **State the identifying assumption.** What assumption makes the variation in $X_i$ exogenous?
Examples:

- random assignment,
- conditional independence,
- parallel trends,
- no manipulation around a cutoff,
- exclusion restriction,
- no time-varying confounding.

14. **Evaluate credibility.** What evidence supports the assumption?
What tests, diagnostics, institutional facts, or robustness checks are available?

15. **Interpret cautiously.** If exogeneity is credible, interpret $\beta$ causally.
If exogeneity is not credible, interpret $\beta$ as an association.

---

## 4.27 Common mistakes

1. **Mistake 1: Saying a variable is simply exogenous or endogenous.** A variable is exogenous or endogenous relative to a model and source of variation.
Weather, price, education, and policy can all be exogenous in some designs and endogenous in others.

2. **Mistake 2: Assuming controls solve endogeneity.** Controls solve endogeneity only if they block the relevant confounding paths and do not create new bias.
Unobserved confounding remains a threat.

3. **Mistake 3: Ignoring the assignment process.** To evaluate exogeneity, one must understand how treatment was assigned or chosen.
Who decided treatment? Based on what information? At what time? In response to what incentives?

4. **Mistake 4: Treating fixed effects as a cure-all.** Fixed effects remove time-invariant confounders. They do not remove time-varying confounders, reverse causality, dynamic feedback, or measurement error.
5. **Mistake 5: Confusing prediction with causality.** An endogenous variable may predict the outcome well. That does not mean changing it would change the outcome in the estimated way.
6. **Mistake 6: Overlooking equilibrium.** Economic variables often respond to each other. Prices, wages, quantities, employment, migration, and policy choices are frequently jointly determined.
7. **Mistake 7: Ignoring measurement error.** Poor measurement can bias estimates even when the conceptual design is strong.
8. **Mistake 8: Believing statistical significance proves exogeneity.** A statistically significant coefficient may be precisely biased. Statistical significance does not solve identification.
---

## 4.28 Summary
Exogeneity and endogeneity describe whether the variation in an explanatory variable is suitable for causal inference.

In a regression: $Y_i = \alpha + \beta X_i + u_i$ $X_i$ is exogenous if the unobserved determinants of $Y_i$ contained in $u_i$ are unrelated to $X_i$: $\mathbb{E}[u_i \mid X_i]=0$ or, in a weaker linear form: $\operatorname{Cov}(X_i,u_i)=0$ $X_i$ is endogenous if this condition fails: $\mathbb{E}[u_i \mid X_i]\neq 0$ or: $\operatorname{Cov}(X_i,u_i)\neq 0$ Endogeneity can arise from omitted variables, reverse causality, simultaneity, selection bias, measurement error, dynamic feedback, bad controls, and model misspecification. In potential outcomes language, exogeneity means treatment assignment is independent of potential outcomes, either unconditionally: $D_i \perp \big(Y_i(1),Y_i(0)\big)$ or conditionally: $D_i \perp \big(Y_i(1),Y_i(0)\big) \mid X_i$ In DAG language, endogeneity appears when non-causal paths between treatment and outcome remain open. The central lesson is:

> A regression coefficient becomes causal only when the variation identifying it is exogenous for the causal question being asked.

Exogeneity is not guaranteed by data, controls, fixed effects, or statistical significance. It must be argued through research design, institutional knowledge, theory, and evidence. The most important question is always:

> Why is the variation in treatment unrelated to the counterfactual outcomes or unobserved determinants of the outcome?

# 5. Omitted Variable Bias and Confounding

## 5.1 Why omitted variable bias matters
Omitted variable bias is one of the most important reasons a regression coefficient fails to have a causal interpretation.

A regression coefficient describes how an outcome varies with a regressor, holding included variables fixed. But if an important variable is left out of the model, and that omitted variable is related to both the regressor and the outcome, the coefficient on the included regressor will generally mix together multiple effects. For example, suppose we estimate the relationship between education and wages: $Wage_i = \alpha + \beta Education_i + u_i$ A tempting interpretation is:

> $\beta$ is the causal effect of education on wages.

But that interpretation requires strong assumptions. People with more education may also differ from people with less education in ability, family background, parental education, school quality, neighborhood, motivation, health, social networks, and expectations about the future. If these omitted factors affect wages and are correlated with education, then the estimated coefficient on education does not isolate the causal effect of education. The problem is not merely that the model is incomplete. Every model is incomplete. The problem is that the omitted factor is systematically related to the included explanatory variable. Omitted variable bias arises when two conditions hold:

1. The omitted variable affects the outcome.
2. The omitted variable is correlated with the included explanatory variable.

If either condition fails, omitting the variable does not create omitted variable bias for the coefficient of interest. For causal inference, omitted variable bias is closely related to confounding. A confounder is a variable that causally affects both the treatment and the outcome. When a confounder is omitted, the estimated treatment-outcome relationship combines the causal effect of treatment with the non-causal association generated by the confounder. The central lesson is:

> A regression coefficient is not causal merely because it controls for some variables. It is causal only if the remaining omitted determinants of the outcome are not systematically related to the treatment or regressor of interest.

## 5.2 The basic omitted variable bias setup
Suppose the true causal model is: $Y_i = \alpha + \beta X_i + \gamma Z_i + u_i$
where:

- $Y_i$ is the outcome,
- $X_i$ is the explanatory variable or treatment of interest,
- $Z_i$ is another variable that affects $Y_i$,
- $u_i$ contains other unobserved determinants of $Y_i$,
- $\beta$ is the causal effect of $X_i$ on $Y_i$, holding $Z_i$ fixed,
- $\gamma$ is the effect of $Z_i$ on $Y_i$, holding $X_i$ fixed.

Assume for the moment that the true model satisfies: $\mathbb{E}[u_i \mid X_i,Z_i]=0$ This means that after controlling for $X_i$ and $Z_i$, the remaining unobserved determinants of $Y_i$ are unrelated to the included variables. Now suppose the researcher omits $Z_i$ and estimates: $Y_i = a + \tilde{\beta}X_i + e_i$ The estimated coefficient $\tilde{\beta}$ generally does not equal $\beta$. Why? Because the omitted variable $Z_i$ is absorbed into the new error term: $e_i = \gamma Z_i + u_i$ If $X_i$ is correlated with $Z_i$, then $X_i$ is correlated with $e_i$: $\operatorname{Cov}(X_i,e_i) = \operatorname{Cov}(X_i,\gamma Z_i + u_i)$ Using linearity of covariance: $\operatorname{Cov}(X_i,e_i) = \gamma \operatorname{Cov}(X_i,Z_i) + \operatorname{Cov}(X_i,u_i)$ If $\operatorname{Cov}(X_i,u_i)=0$, then: $\operatorname{Cov}(X_i,e_i) = \gamma \operatorname{Cov}(X_i,Z_i)$ So if $\gamma \neq 0$ and $\operatorname{Cov}(X_i,Z_i) \neq 0$, then: $\operatorname{Cov}(X_i,e_i) \neq 0$ That violates the exogeneity condition needed for ordinary least squares to identify the causal effect of $X_i$. The omitted variable becomes part of the error term. Because the included regressor is correlated with that omitted variable, the included regressor is correlated with the error term. This is endogeneity.

## 5.3 Deriving the omitted variable bias formula
In the simple two-variable case, the omitted variable bias formula is: $\operatorname{Bias}(\tilde{\beta}) = \gamma \cdot \frac{\operatorname{Cov}(X_i,Z_i)}{\operatorname{Var}(X_i)}$
Equivalently: $\tilde{\beta} = \beta + \gamma \cdot \frac{\operatorname{Cov}(X_i,Z_i)}{\operatorname{Var}(X_i)}$
This formula is worth understanding carefully.

Start with the true model: $Y_i = \alpha + \beta X_i + \gamma Z_i + u_i$ If we regress $Y_i$ only on $X_i$, the population regression coefficient is: $\tilde{\beta} = \frac{\operatorname{Cov}(X_i,Y_i)}{\operatorname{Var}(X_i)}$ Substitute the true model into the covariance:

$$
\operatorname{Cov}(X_i,Y_i)
=
\operatorname{Cov}(X_i,\alpha + \beta X_i + \gamma Z_i + u_i)
$$

Because covariance with a constant is zero:

$$
\operatorname{Cov}(X_i,Y_i)
=
\beta \operatorname{Var}(X_i)
+
\gamma \operatorname{Cov}(X_i,Z_i)
+
\operatorname{Cov}(X_i,u_i)
$$

Assume: $\operatorname{Cov}(X_i,u_i)=0$ Then:

$$
\operatorname{Cov}(X_i,Y_i)
=
\beta \operatorname{Var}(X_i)
+
\gamma \operatorname{Cov}(X_i,Z_i)
$$

Divide by $\operatorname{Var}(X_i)$:

$$
\tilde{\beta}
=
\frac{\beta \operatorname{Var}(X_i)}{\operatorname{Var}(X_i)}
+
\frac{\gamma \operatorname{Cov}(X_i,Z_i)}{\operatorname{Var}(X_i)}
$$

So:

$$
\tilde{\beta}
=
\beta
+
\gamma \cdot \frac{\operatorname{Cov}(X_i,Z_i)}{\operatorname{Var}(X_i)}
$$

The second term is the omitted variable bias. This formula shows that the bias depends on two forces:

1. How strongly the omitted variable affects the outcome: $\gamma$.
2. How strongly the omitted variable is related to the included regressor: $\operatorname{Cov}(X_i,Z_i)$.

The variance of $X_i$ scales the bias but does not determine its sign.

## 5.4 Direction of omitted variable bias
The sign of omitted variable bias depends on the sign of: $\gamma \cdot \operatorname{Cov}(X_i,Z_i)$
Because $\operatorname{Var}(X_i)>0$, the direction of bias is determined by:

1. whether $Z_i$ increases or decreases $Y_i$,
2. whether $Z_i$ is positively or negatively correlated with $X_i$.

A useful table is:

| Effect of omitted variable on outcome | Relationship between omitted variable and included regressor | Direction of bias |
|---|---|---|
| $\gamma>0$ | $\operatorname{Cov}(X,Z)>0$ | Positive bias |
| $\gamma>0$ | $\operatorname{Cov}(X,Z)<0$ | Negative bias |
| $\gamma<0$ | $\operatorname{Cov}(X,Z)>0$ | Negative bias |
| $\gamma<0$ | $\operatorname{Cov}(X,Z)<0$ | Positive bias |

Positive bias means: $\tilde{\beta} > \beta$ Negative bias means: $\tilde{\beta} < \beta$ This does not necessarily mean the estimated coefficient is positive or negative. It means the coefficient is above or below the true causal effect. For example, suppose the true effect of education on wages is positive: $\beta>0$ If ability is omitted, ability raises wages: $\gamma>0$ and ability is positively correlated with education: $\operatorname{Cov}(Education,Ability)>0$ then the estimated education coefficient is biased upward: $\tilde{\beta}>\beta$ The regression overstates the causal return to education because part of the estimated education effect is actually the effect of ability. But omitted variable bias can also bias an estimate downward. Suppose disadvantaged workers are more likely to enter a job training program, and disadvantage lowers earnings. If disadvantage is omitted, treatment may be negatively selected. A naive regression may understate the effect of training or even make a helpful program appear harmful. The direction of bias is an economic question, not a purely statistical one. It requires substantive reasoning about the omitted variable.

## 5.5 Example: education, ability, and wages
Consider the causal effect of education on wages.

A researcher estimates: $Wage_i = \alpha + \beta Education_i + u_i$ The concern is that ability is omitted. Suppose the more complete model is: $Wage_i = \alpha + \beta Education_i + \gamma Ability_i + u_i$ where $Ability_i$ includes cognitive skills, non-cognitive skills, motivation, persistence, health, family support, or other productivity-related traits. If ability affects wages, then: $\gamma \neq 0$ If ability is related to education, then: $\operatorname{Cov}(Education_i,Ability_i) \neq 0$ The omitted variable bias is: $\gamma \cdot \frac{\operatorname{Cov}(Education_i,Ability_i)}{\operatorname{Var}(Education_i)}$ The common concern is upward bias. If ability increases wages and people with greater ability obtain more education, then: $\gamma>0$ and: $\operatorname{Cov}(Education_i,Ability_i)>0$ so: $\operatorname{Bias}(\tilde{\beta})>0$ The estimated coefficient on education partly reflects ability. However, the bias need not always be upward. Suppose some high-ability people leave school early because they have strong entrepreneurial opportunities, or some people obtain more education because they face discrimination in the labor market and need extra credentials. Then the relationship between education and omitted determinants of wages may be more complex. This example illustrates an important point:

> Omitted variable bias is not diagnosed by listing possible omitted variables. It requires reasoning about whether those variables affect the outcome and whether they are correlated with the regressor of interest.

## 5.6 Example: job training and motivation
Suppose we want to estimate the effect of a voluntary job training program on earnings.

A simple regression is: $Earnings_i = \alpha + \beta Training_i + u_i$ where $Training_i=1$ if worker $i$ participated in the program. The concern is that motivation is omitted. A more complete model might be: $Earnings_i = \alpha + \beta Training_i + \gamma Motivation_i + u_i$ If motivation increases earnings and motivated workers are more likely to enroll in training, then: $\gamma>0$ and: $\operatorname{Cov}(Training_i,Motivation_i)>0$ The estimated training coefficient is biased upward. The regression may attribute to training what is partly due to motivation. But selection into training can also work in the opposite direction. Workers who enroll may be those with worse job prospects, weaker networks, lower baseline skills, or longer unemployment spells. If these disadvantages lower earnings and are positively related to training participation, then the omitted variable bias may be negative. For example, let $Disadvantage_i$ represent barriers to employment: $Earnings_i = \alpha + \beta Training_i + \gamma Disadvantage_i + u_i$ where: $\gamma<0$ If more disadvantaged workers are more likely to enter training: $\operatorname{Cov}(Training_i,Disadvantage_i)>0$ then: $\operatorname{Bias}(\tilde{\beta})<0$ The estimated effect of training is biased downward. This example shows why the sign of selection is often ambiguous. Participants can be positively selected on motivation and negatively selected on baseline labor market prospects at the same time. A credible research design must address both possibilities.

## 5.7 Example: police and crime
Suppose we estimate: $Crime_c = \alpha + \beta Police_c + u_c$
where $c$ indexes cities or neighborhoods.

A positive coefficient on police could be misread as evidence that police increase crime. But police are not randomly assigned. Areas with higher expected crime often receive more police. A more complete model might be: $Crime_c = \alpha + \beta Police_c + \gamma UnderlyingCrimeRisk_c + u_c$ where $UnderlyingCrimeRisk_c$ includes poverty, gang activity, drug markets, population density, nightlife, commercial activity, reporting behavior, or other determinants of crime. If underlying crime risk increases crime, then: $\gamma>0$ If police are assigned to areas with higher underlying crime risk, then: $\operatorname{Cov}(Police_c,UnderlyingCrimeRisk_c)>0$ The coefficient on police is biased upward. This does not tell us whether the true causal effect of police is positive, negative, or zero. It tells us that a simple cross-sectional comparison is not credible because police deployment responds to crime risk. A better design might use:

- random police patrol allocation,
- sudden police redeployments unrelated to local crime trends,
- instrumental variables based on staffing shocks,
- difference-in-differences around policy changes,
- event studies of temporary police surges,
- regression discontinuity if deployment follows a threshold rule.

The core omitted variable problem is that high-police areas are not comparable to low-police areas.

## 5.8 Confounding as a causal graph problem
Omitted variable bias has a natural interpretation using DAGs.

Suppose we want the effect of $X$ on $Y$, but there is a confounder $C$: $C \rightarrow X$ and: $C \rightarrow Y$ and the causal effect of interest is: $X \rightarrow Y$ The DAG is: $C \rightarrow X \rightarrow Y$ $C \rightarrow Y$ There is a causal path from $X$ to $Y$: $X \rightarrow Y$ But there is also a backdoor path: $X \leftarrow C \rightarrow Y$ This backdoor path creates an association between $X$ and $Y$ that is not caused by $X$. If $C$ is omitted, the observed relationship between $X$ and $Y$ includes both:

1. the causal effect of $X$ on $Y$,
2. the non-causal association induced by $C$.

Controlling for $C$ blocks the backdoor path: $X \leftarrow C \rightarrow Y$ If $C$ is the only confounder, and if controlling for it does not create new bias, then conditioning on $C$ helps isolate the causal effect of $X$ on $Y$. This is the graphical meaning of omitted variable bias.

## 5.9 Confounding in the potential outcomes framework
In the potential outcomes framework, confounding means that treatment assignment is related to potential outcomes.

For a binary treatment $D_i$, the potential outcomes are: $Y_i(1)$ and: $Y_i(0)$ Treatment is unconfounded if: $(Y_i(1),Y_i(0)) \perp D_i$ This means treatment assignment is independent of the outcomes units would have under treatment and control. In randomized experiments, this independence is created by random assignment. In observational studies, it often fails. For example, in a voluntary training program, participants may differ from nonparticipants in ways that affect their potential earnings under either treatment status. In notation: $\mathbb{E}[Y_i(0) \mid D_i=1] \neq \mathbb{E}[Y_i(0) \mid D_i=0]$ This means treated and untreated units would have had different average outcomes even without treatment. A common observational assumption is conditional unconfoundedness: $(Y_i(1),Y_i(0)) \perp D_i \mid X_i$ This says that after conditioning on observed covariates $X_i$, treatment assignment is independent of potential outcomes. In plain English:

> Among units with the same observed characteristics, treatment is as good as randomly assigned.

This assumption justifies methods such as regression adjustment, matching, weighting, and stratification. But it is strong. It fails if treatment depends on unobserved variables that affect outcomes. For example, if training participation depends on unobserved motivation, and motivation affects earnings, then conditioning on observed variables may not remove confounding.

## 5.10 Omitted variables versus confounders
The terms omitted variable and confounder are related but not identical.

An omitted variable is simply a variable not included in a regression model. A confounder is a variable that causally affects both the treatment and the outcome. All omitted confounders are omitted variables, but not all omitted variables are confounders. Suppose we estimate the effect of education on wages. A variable such as favorite color is omitted. But if favorite color does not affect education or wages, it is not a confounder. A variable such as ability may be a confounder if it affects both education and wages. A variable such as occupation may be affected by education and then affect wages: $Education \rightarrow Occupation \rightarrow Wages$ Occupation is not a pre-treatment confounder. It is a mediator. Omitting it does not create omitted variable bias for the total effect of education. Including it may instead block part of the causal effect. A variable such as college admission may be affected by both ability and family resources: $Ability \rightarrow Admission \leftarrow FamilyResources$ Admission is a collider on this path. Conditioning on it can create bias. Therefore, the question is not simply:

> Did we omit any variable related to the outcome?

The better question is:

> Did we omit a pre-treatment common cause of treatment and outcome, or did we condition on a variable that distorts the causal comparison?

## 5.11 Good controls and bad controls
A control variable is not automatically good because it improves prediction. For causal inference, a good control is one that helps make the comparison between treated and untreated units more credible.

A good control is usually a pre-treatment variable that blocks a non-causal backdoor path. A bad control is a variable that creates bias, blocks part of the causal effect, or changes the estimand in an unintended way.

- **Good controls.** Suppose we want the effect of education on wages and family background affects both education and wages: $FamilyBackground \rightarrow Education$
$FamilyBackground \rightarrow Wages$ Controlling for family background may help block the backdoor path: $Education \leftarrow FamilyBackground \rightarrow Wages$ Good controls are typically:

- determined before treatment,
- causes of treatment,
- causes of outcome,
- not themselves caused by treatment,
- not colliders,
- not descendants of colliders,
- measured well enough to adjust for confounding.

- **Bad control: mediator.** Suppose: $Education \rightarrow Occupation \rightarrow Wages$
If we control for occupation, we block part of the effect of education on wages. This may be appropriate if we want the direct effect of education holding occupation fixed, but it is not appropriate if we want the total effect of education.

- **Bad control: post-treatment variable.** Suppose a job training program affects job search effort, and job search effort affects earnings: $Training \rightarrow JobSearch \rightarrow Earnings$
If we control for job search effort after training begins, we may remove part of the training effect.

- **Bad control: collider.** Suppose ability and luck both affect admission to an elite school: $Ability \rightarrow Admission \leftarrow Luck$
If we condition on admitted students only, ability and luck can become associated even if they are unrelated in the general population. Among admitted students, those with less luck may need more ability to be admitted.

Conditioning on a collider can open a non-causal path and create bias. The rule is:

> Choose controls based on the causal structure, not based only on statistical significance or predictive power.

## 5.12 The danger of controlling for outcomes or consequences of treatment
One common mistake is controlling for variables measured after treatment.

Post-treatment controls are dangerous because they may be affected by treatment. If a control variable is affected by treatment, then including it can change the causal estimand or introduce bias. For example, suppose we want the effect of education on earnings: $Education \rightarrow Occupation \rightarrow Earnings$ If we estimate: $Earnings_i = \alpha + \beta Education_i + \delta Occupation_i + u_i$ then $\beta$ is not the total effect of education on earnings. It is closer to the effect of education among people with the same occupation. But occupation is partly a result of education. Holding occupation fixed removes an important channel through which education affects earnings. In some research questions, this is exactly what we want. If the question is:

> What is the direct effect of education on earnings holding occupation fixed?

then controlling for occupation may be appropriate. But if the question is:

> What is the total effect of education on earnings?

then controlling for occupation is a bad control. Another example: $Treatment \rightarrow HealthBehavior \rightarrow HealthOutcome$ If a health program changes behavior, and behavior changes health, controlling for behavior estimates a different effect from the total effect of the program. The general principle is:

> Do not control for variables that are consequences of treatment unless the estimand explicitly requires doing so.

## 5.13 Proxy controls and imperfect measurement
Sometimes the true confounder is unobserved, but a proxy is observed.

For example, ability may be unobserved, but test scores are observed. Socioeconomic status may be unobserved, but parental income and parental education are observed. Motivation may be unobserved, but prior attendance or prior performance is observed. Suppose the true model is: $Y_i = \alpha + \beta X_i + \gamma Z_i + u_i$ but $Z_i$ is unobserved. Instead, we observe a proxy $W_i$: $W_i = Z_i + \nu_i$ If $W_i$ is a noisy measure of $Z_i$, controlling for $W_i$ may reduce omitted variable bias but usually does not eliminate it completely. The reason is that residual variation in the true confounder remains uncontrolled. If the proxy is very informative, it may help a lot. If the proxy is weak or measured with substantial error, it may help little. For example, controlling for test scores may reduce ability bias in returns-to-education estimates, but test scores may not capture motivation, persistence, family networks, health, or school quality. Proxy controls require caution. Researchers should ask:

1. What confounder is the proxy intended to measure?
2. How strongly is the proxy related to the true confounder?
3. What aspects of the confounder remain unmeasured?
4. Could the proxy itself be affected by treatment?
5. Does the proxy introduce new bias?

A proxy can be useful, but it is not magic. It must be interpreted substantively.

## 5.14 Measurement error and omitted variable bias
Measurement error can interact with omitted variable bias in important ways.

Suppose the researcher controls for a confounder $Z_i$, but observes it with error: $Z_i^{obs} = Z_i + \nu_i$ The regression includes $Z_i^{obs}$ rather than $Z_i$: $Y_i = \alpha + \beta X_i + \delta Z_i^{obs} + e_i$ If $Z_i^{obs}$ is an imperfect measure of $Z_i$, then controlling for $Z_i^{obs}$ may not fully block the backdoor path through $Z_i$. For example, suppose family background confounds the relationship between education and wages. If family background is measured only by parental income in one year, that measure may not capture wealth, parental education, neighborhood quality, expectations, social capital, or childhood environment. The residual unmeasured part of family background can still bias the education coefficient. Measurement error in the treatment variable can also create bias. If $X_i$ is measured with classical error, the estimated coefficient may be attenuated toward zero. If the measurement error is related to omitted factors, the bias can be more complex. Therefore, causal inference requires attention not only to which variables are included but also to how well they are measured.

## 5.15 Multiple omitted variables
Real empirical problems usually involve more than one omitted variable.

Suppose the true model is: $Y_i = \alpha + \beta X_i + \gamma_1 Z_{1i} + \gamma_2 Z_{2i} + \cdots + \gamma_K Z_{Ki} + u_i$ If the researcher omits all the $Z$ variables and regresses $Y_i$ on $X_i$, the total omitted variable bias is the combined contribution of all omitted variables related to $X_i$ and $Y_i$. In general: $\tilde{\beta} = \beta + \sum_{k=1}^{K} \gamma_k \cdot \frac{\operatorname{Cov}(X_i,Z_{ki})}{\operatorname{Var}(X_i)}$ This expression applies cleanly in the simple case where $X_i$ is the only included regressor besides the intercept. With additional included controls, the idea remains the same, but the formula uses residualized variables. Multiple omitted variables can push bias in different directions. For example, in estimating the effect of job training:

- motivation may create upward bias,
- disadvantage may create downward bias,
- prior employment history may create either direction,
- caseworker selection may create upward or downward bias depending on assignment rules.

The net bias is the sum of these forces. This is why simply saying “there may be omitted variables” is not enough. A serious analysis asks which variables are omitted, how they relate to treatment, how they affect outcomes, and which direction the resulting bias likely goes.

## 5.16 Omitted variable bias with included controls
Most regressions include more than one explanatory variable. Suppose the researcher estimates: $Y_i = \alpha + \beta X_i + \delta W_i + e_i$
where $W_i$ is a vector of included controls. But the true model also includes an omitted confounder $Z_i$: $Y_i = \alpha + \beta X_i + \delta W_i + \gamma Z_i + u_i$
In this case, omitted variable bias depends on the relationship between $Z_i$ and the part of $X_i$ not explained by $W_i$.

To see this, residualize $X_i$ with respect to $W_i$. Let $\tilde{X}_i$ be the residual from regressing $X_i$ on $W_i$. Then the bias in the coefficient on $X_i$ depends on: $\operatorname{Cov}(\tilde{X}_i,Z_i)$ not simply on: $\operatorname{Cov}(X_i,Z_i)$ In words:

> After controlling for $W_i$, is the remaining variation in $X_i$ still correlated with the omitted variable $Z_i$?

This is a key point. A variable may be correlated with treatment overall, but not correlated with the residual variation in treatment after controls. Conversely, a variable may become more important after conditioning on controls. For example, suppose education is correlated with family background. If the regression controls for parental income, parental education, and neighborhood, the remaining variation in education may be less correlated with family background. But if these controls are incomplete, omitted family background can still bias the estimate. The question is not whether treatment is unconditionally related to omitted factors. The question is whether treatment is related to omitted factors after conditioning on the included controls.

## 5.17 Fixed effects as a response to omitted variable bias
Fixed effects are a common way to address omitted variable bias from unobserved factors that are constant within units over time.

Suppose we observe unit $i$ over time $t$: $Y_{it} = \alpha_i + \beta X_{it} + u_{it}$ The term $\alpha_i$ represents all time-invariant characteristics of unit $i$. For a person, $\alpha_i$ might include stable ability, childhood background, personality, early health, or family environment. For a firm, $\alpha_i$ might include management quality, firm culture, location, or long-run productivity. For a city, $\alpha_i$ might include geography, historical institutions, climate, or persistent industrial structure. By including unit fixed effects, the model compares each unit to itself over time. The identifying variation comes from within-unit changes in $X_{it}$. Fixed effects remove omitted variable bias from factors that are:

1. unobserved,
2. related to treatment,
3. related to the outcome,
4. constant over time within units.

However, fixed effects do not solve all omitted variable problems. They do not remove time-varying confounders. For example, suppose firms adopt new technology when demand is rising. Firm fixed effects remove stable firm quality, but they do not remove the time-varying demand shock that both causes technology adoption and increases productivity. The model: $Productivity_{it} = \alpha_i + \lambda_t + \beta Technology_{it} + u_{it}$ controls for firm fixed effects $\alpha_i$ and common time shocks $\lambda_t$, but it still fails if firm-specific demand shocks are correlated with technology adoption. Fixed effects are powerful, but they require the remaining within-unit variation in treatment to be plausibly exogenous.

## 5.18 Difference-in-differences as a response to omitted variable bias
Difference-in-differences can be understood as a method for addressing omitted variable bias from stable group differences and common time shocks.

Suppose a policy affects a treated group but not a control group. The basic model is: $Y_{it} = \alpha_i + \lambda_t + \beta D_{it} + u_{it}$ where:

- $\alpha_i$ are unit fixed effects,
- $\lambda_t$ are time fixed effects,
- $D_{it}$ indicates treatment exposure,
- $\beta$ is the difference-in-differences estimate.

Unit fixed effects remove time-invariant differences between treated and control units. Time fixed effects remove shocks common to all units. But difference-in-differences still requires an assumption about omitted variables:

> In the absence of treatment, treated and control units would have followed parallel trends.

This assumption rules out time-varying omitted factors that differentially affect treated units exactly when treatment occurs. For example, if a state raises the minimum wage during a local economic downturn that would have reduced employment anyway, then the estimated policy effect may be biased downward. Difference-in-differences does not eliminate all confounding. It changes the omitted variable problem from a levels problem to a trends problem. The key question becomes:

> Are there omitted factors that cause treated and control groups to have different counterfactual trends?

## 5.19 Instrumental variables as a response to omitted variable bias
Instrumental variables can address omitted variable bias when treatment is endogenous because of unobserved confounding.

Suppose: $Y_i = \alpha + \beta X_i + u_i$ and: $\operatorname{Cov}(X_i,u_i) \neq 0$ An instrument $Z_i$ is a variable that shifts $X_i$ but is otherwise unrelated to the omitted determinants of $Y_i$. The two core requirements are:

- **Relevance.** $\operatorname{Cov}(Z_i,X_i) \neq 0$
The instrument must affect the endogenous variable.

- **Exclusion restriction.** The instrument must affect the outcome only through $X_i$.
In DAG form: $Z \rightarrow X \rightarrow Y$ and there must be no direct path: $Z \rightarrow Y$ and no open backdoor path from $Z$ to $Y$. For example, compulsory schooling laws may be used as instruments for education if they affect schooling but do not affect wages through channels other than education. IV can be powerful because it isolates a source of variation in $X_i$ that is not contaminated by the omitted variable. However, IV does not remove omitted variable bias automatically. The instrument itself must be credible. If the instrument is related to omitted determinants of the outcome, IV is also biased. The relevant question is:

> Does the instrument generate variation in treatment that is plausibly independent of the omitted causes of the outcome?

## 5.20 Matching, weighting, and selection on observables
Matching and weighting attempt to address confounding by comparing treated and untreated units with similar observed characteristics.

The key assumption is conditional unconfoundedness: $(Y_i(1),Y_i(0)) \perp D_i \mid X_i$ where $X_i$ includes observed confounders. In words:

> After conditioning on observed variables, treatment assignment is independent of potential outcomes.

Matching tries to pair treated units with similar untreated units. Weighting tries to reweight the untreated group so that its observed covariate distribution resembles that of the treated group. These methods can reduce omitted variable bias from observed confounders. They do not solve bias from unobserved confounders unless the unobserved confounders are fully captured by observed proxies or are unrelated to treatment after conditioning. For example, matching job training participants and nonparticipants on age, education, prior earnings, and employment history may improve comparability. But if participants differ in unobserved motivation or family support, matching may not eliminate bias. Matching and weighting also require overlap: $0 < P(D_i=1 \mid X_i=x) < 1$ for relevant values of $x$. Without overlap, there are no comparable untreated units for some treated units, or no comparable treated units for some untreated units. The main lesson is:

> Matching and weighting are only as credible as the assumption that the relevant confounders are observed and adequately measured.

## 5.21 Randomization and omitted variable bias
Randomization is the benchmark solution to omitted variable bias.

If treatment is randomly assigned, then: $D_i \perp (Y_i(1),Y_i(0))$ Treatment is independent of both observed and unobserved determinants of potential outcomes. Randomization does not require the researcher to observe all confounders. It balances them in expectation. For example, in a randomized job training experiment, motivated and less motivated workers should be assigned to treatment and control at similar rates in expectation. Ability, family background, prior networks, and other omitted factors should also be balanced in expectation. This means: $\mathbb{E}[Y_i(0) \mid D_i=1] = \mathbb{E}[Y_i(0) \mid D_i=0]$ and: $\mathbb{E}[Y_i(1) \mid D_i=1] = \mathbb{E}[Y_i(1) \mid D_i=0]$ Therefore, the difference in average observed outcomes identifies the ATE: $ATE = \mathbb{E}[Y_i \mid D_i=1] - \mathbb{E}[Y_i \mid D_i=0]$ In finite samples, randomization may still produce chance imbalance. Researchers often check baseline covariate balance and may improve precision by controlling for pre-treatment covariates. But the causal credibility comes from random assignment, not from the controls. RCTs can still have other problems, such as attrition, noncompliance, spillovers, and implementation failures. But randomization directly addresses omitted variable bias from baseline confounders.

## 5.22 Why adding controls can change the estimand
Adding controls changes the comparison being made.

A regression without controls compares units with different values of $X$ overall. A regression with controls compares units with different values of $X$ but the same values of the included controls. For example: $Wage_i = \alpha + \beta Education_i + u_i$ compares wages across people with different education levels. But: $Wage_i = \alpha + \beta Education_i + \delta Occupation_i + u_i$ compares people with different education levels but the same occupation. This may be a very different question. If occupation is a consequence of education, then holding occupation fixed removes an important pathway from education to wages. Similarly: $Health_i = \alpha + \beta Insurance_i + \delta DoctorVisits_i + u_i$ may not estimate the total effect of health insurance if insurance affects doctor visits. Controls do not merely remove noise. They define the comparison. Therefore, before adding a control, ask:

1. Is this variable determined before treatment?
2. Is it a cause of treatment and outcome?
3. Is it a consequence of treatment?
4. Is it a mediator?
5. Is it a collider?
6. Does controlling for it change the estimand?
7. Is the resulting estimand the one we want?

## 5.23 Omitted variable bias and model misspecification
Omitted variable bias is one form of model misspecification, but model misspecification is broader.

A model may be misspecified because:

- a confounder is omitted,
- the functional form is wrong,
- relationships are nonlinear,
- interactions are omitted,
- treatment effects are heterogeneous,
- the timing of treatment effects is wrong,
- measurement error is ignored,
- equilibrium behavior is ignored,
- standard errors are incorrectly estimated,
- the wrong unit of analysis is used.

For example, suppose the effect of education on wages differs by gender, race, field of study, or local labor market. A model with a single constant effect may hide important heterogeneity. Or suppose the relationship between class size and learning is nonlinear. Reducing class size from 40 to 30 may matter more than reducing it from 20 to 10. A linear model may misrepresent the effect. Omitted variable bias specifically concerns excluded variables that are related to both treatment and outcome. But even if all confounders were controlled, a poorly specified model could still produce misleading estimates. A rigorous empirical analysis should therefore consider both identification and specification.

## 5.24 Sensitivity analysis
Because omitted variables are often unobserved, researchers should ask how sensitive their conclusions are to possible omitted confounding.

Sensitivity analysis asks:

> How strong would an omitted confounder have to be to change the conclusion?

For example, suppose a study estimates that a training program increases earnings by USD 2,000. A sensitivity analysis might ask how strongly an unobserved variable would need to affect both training participation and earnings to reduce the estimated effect to zero. Common sensitivity approaches include:

- adding richer sets of controls,
- comparing estimates with and without controls,
- using pre-treatment outcomes as controls,
- placebo outcomes,
- placebo treatments,
- bounding exercises,
- Oster-style coefficient stability analysis,
- Rosenbaum bounds for matching,
- negative control outcomes,
- negative control exposures,
- instrumental variables as a robustness strategy,
- alternative comparison groups,
- pre-trend analysis in panel settings.

No sensitivity analysis proves that omitted variable bias is absent. But it can show whether the conclusion is fragile or robust to plausible forms of confounding. A strong paper does not simply say:

> We control for many variables.

It asks:

> What important confounders might remain, how large would their influence need to be, and what evidence suggests they are or are not driving the result?

## 5.25 Practical diagnostic questions
When evaluating a study, ask these questions.

1. **What is the treatment?.** Is the treatment clearly defined?
Examples:

- years of education,
- college attendance,
- job training participation,
- minimum wage exposure,
- pollution exposure,
- police presence,
- health insurance coverage.

2. **What is the outcome?.** Is the outcome clearly measured?
Examples:

- wages,
- employment,
- test scores,
- crime rates,
- mortality,
- firm productivity,
- household consumption.

3. **What omitted variables might affect both treatment and outcome?.** List possible confounders.
For education and wages:

- ability,
- family background,
- school quality,
- neighborhood,
- motivation,
- networks.

For training and earnings:

- motivation,
- prior employment,
- local labor market conditions,
- caseworker selection,
- health,
- family constraints.

4. **What direction would each omitted variable bias the estimate?.** For each omitted variable, ask:
1. Does it increase or decrease the outcome?
2. Is it positively or negatively related to treatment?
3. Does it push the estimate upward or downward?

5. **Are the controls pre-treatment?.** Controls should usually be determined before treatment. Post-treatment controls can create bias or change the estimand.
6. **Are any controls mediators?.** If a variable lies on the causal path from treatment to outcome, controlling for it may block part of the effect.
7. **Are any controls colliders?.** If a variable is caused by both treatment and outcome determinants, controlling for it can open a non-causal path.
8. **What variation identifies the coefficient?.** After controls are included, what variation in treatment remains?
Is that remaining variation plausibly exogenous?

9. **Is there overlap?.** Are treated and untreated units comparable within the relevant covariate strata?
If not, estimates may rely heavily on extrapolation.

10. **What robustness checks support the claim?.** Look for:
- alternative control sets,
- pre-treatment outcome controls,
- placebo tests,
- sensitivity analysis,
- alternative designs,
- falsification tests,
- institutional evidence.

## 5.26 Applied example: estimating the return to education
Suppose the research question is:

> What is the causal effect of an additional year of schooling on wages?

A naive model is: $\log(Wage_i) = \alpha + \beta Schooling_i + u_i$ Here, $\beta$ is often interpreted approximately as the percentage change in wages associated with one additional year of schooling. But this coefficient may be biased by omitted variables. Possible omitted confounders include:

- ability,
- motivation,
- parental education,
- family income,
- school quality,
- neighborhood,
- health,
- social networks,
- local labor markets.

A richer model might include controls: $\log(Wage_i) = \alpha + \beta Schooling_i + X_i'\delta + u_i$ where $X_i$ includes observed background characteristics. This helps only if the included controls capture the relevant confounding. A DAG might be: $FamilyBackground \rightarrow Schooling$ $FamilyBackground \rightarrow Wages$ $Ability \rightarrow Schooling$ $Ability \rightarrow Wages$ $Schooling \rightarrow Wages$ If family background and ability are omitted, the schooling coefficient is confounded. Possible research designs include:

- sibling fixed effects,
- twin studies,
- compulsory schooling laws,
- school construction programs,
- distance-to-college instruments,
- regression discontinuity around admissions or scholarship cutoffs,
- panel data approaches.

Each design addresses omitted variable bias differently and identifies a potentially different estimand. For example, compulsory schooling laws may identify the return to education for individuals whose schooling was changed by the law. That may differ from the return to college for people who would attend college voluntarily. A careful conclusion would not say:

> Education increases wages by $\beta$ for everyone.

It would say something like:

> Under the identifying assumptions of this design, the estimate suggests that the schooling variation induced by the policy increased wages for the affected group by approximately this amount.

## 5.27 Applied example: health insurance and health outcomes
Suppose we estimate: $Health_i = \alpha + \beta Insurance_i + u_i$
where $Insurance_i=1$ if person $i$ has health insurance.

The coefficient $\beta$ may not identify the causal effect of insurance because insurance coverage is not random. Possible omitted confounders include:

- income,
- employment,
- age,
- baseline health,
- risk preferences,
- access to care,
- education,
- state policy,
- family structure.

The direction of bias is ambiguous. Higher-income people may be more likely to have insurance and better health, creating upward bias if health is measured positively. But sicker people may seek insurance more actively or qualify for public insurance, creating downward bias if poor health leads to coverage. The observed association could therefore make insurance look more beneficial or less beneficial than it really is. A better design might use:

- Medicaid eligibility expansions,
- age-based eligibility thresholds,
- employer mandate changes,
- randomized insurance lotteries,
- difference-in-differences across states,
- regression discontinuity around income thresholds.

Again, the empirical challenge is to find variation in insurance coverage that is not driven by omitted determinants of health.

## 5.28 Applied example: class size and test scores
Suppose we estimate: $TestScore_i = \alpha + \beta ClassSize_i + u_i$
where $ClassSize_i$ is the number of students in the classroom.

A negative coefficient may suggest smaller classes improve learning. But class size may be endogenous. Possible confounding:

- struggling students may be placed in smaller classes,
- wealthier schools may have smaller classes and more resources,
- experienced teachers may be assigned to certain class sizes,
- parents may sort into schools with smaller classes,
- school administrators may allocate class size based on expected performance.

If weaker students are placed into smaller classes, then smaller classes may be associated with lower test scores even if they help. This creates bias against finding a beneficial effect. If wealthy schools have both smaller classes and better outcomes, then the effect of smaller classes may be overstated. A credible design might use:

- random assignment of students or teachers,
- class-size rules based on enrollment thresholds,
- regression discontinuity from maximum class-size laws,
- within-school variation across cohorts,
- policy changes that alter class size independently of student ability.

The key is to separate the effect of class size from the characteristics of students, teachers, and schools that determine class size.

## 5.29 Application checklist
Use the following checklist when thinking about omitted variable bias and confounding.

1. **Write the target causal relationship.** What effect do you want?
$X \rightarrow Y$
Define $X$, $Y$, the population, and the time horizon.

2. **List possible common causes.** What variables might cause both $X$ and $Y$?
These are candidate confounders.

3. **Draw a DAG.** Draw the treatment, outcome, and possible confounders.
Look for backdoor paths: $X \leftarrow C \rightarrow Y$

4. **Decide which paths need to be blocked.** Identify non-causal paths between $X$ and $Y$.
Find variables that block those paths without blocking causal paths or opening collider paths.

5. **Separate confounders, mediators, and colliders.** Ask whether each variable is:
- a pre-treatment confounder,
- a mediator,
- a collider,
- a descendant of treatment,
- a proxy,
- an outcome.

Do not treat all controls as equally valid.

6. **Check timing.** A confounder must be determined before treatment. A variable affected by treatment is not a standard confounder for the total effect.
7. **Assess measurement.** Are the confounders observed? Are they measured well? Are proxies sufficient?
8. **Evaluate overlap.** Are there comparable treated and untreated units at similar values of the controls?
9. **State the identifying assumption.** For regression or matching, the assumption is often: $(Y_i(1),Y_i(0)) \perp D_i \mid X_i$
Is that plausible?

10. **Consider alternative designs.** If omitted confounding is likely, consider:
- RCTs,
- IV,
- RD,
- DiD,
- fixed effects,
- synthetic control,
- panel methods,
- natural experiments.

11. **Analyze bias direction.** For each omitted variable, determine whether it likely biases the estimate upward or downward.
12. **Conduct sensitivity checks.** Ask how robust the result is to possible omitted confounding.

## 5.30 Summary
Omitted variable bias occurs when a variable is left out of a model and that variable both affects the outcome and is correlated with the included regressor of interest.

In the simple case, if the true model is: $Y_i = \alpha + \beta X_i + \gamma Z_i + u_i$ but the researcher estimates: $Y_i = a + \tilde{\beta}X_i + e_i$ then:

$$
\tilde{\beta}
=
\beta
+
\gamma \cdot \frac{\operatorname{Cov}(X_i,Z_i)}{\operatorname{Var}(X_i)}
$$

The omitted variable creates bias if: $\gamma \neq 0$ and: $\operatorname{Cov}(X_i,Z_i) \neq 0$ In causal language, omitted variable bias often arises from confounding. A confounder is a common cause of treatment and outcome: $C \rightarrow X$ $C \rightarrow Y$ If $C$ is omitted, the backdoor path remains open: $X \leftarrow C \rightarrow Y$ The observed relationship between $X$ and $Y$ then mixes causal and non-causal components. Controls can help if they block confounding paths. But controls can harm if they are mediators, colliders, descendants of treatment, or poorly chosen post-treatment variables. The deeper lesson is:

> Omitted variable bias is not solved by adding many controls. It is addressed by understanding the causal structure and constructing a credible comparison.

A rigorous empirical analysis identifies possible confounders, reasons about the direction of bias, distinguishes good controls from bad controls, assesses whether confounders are measured, and uses research design to justify the causal interpretation.

# 6. Selection Bias

## 6.1 Why selection bias matters
Selection bias is one of the most common reasons empirical comparisons fail to identify causal effects.

Selection bias occurs when the units we observe, compare, or analyze are not comparable to the units needed for the causal question. The problem is not merely that the sample is small or imperfect. The problem is that inclusion in the sample, treatment group, control group, or observed dataset is systematically related to the outcome or to potential outcomes. In empirical economics, selection bias appears in many forms:

- people choose whether to enroll in a program,
- firms choose whether to adopt a technology,
- patients choose or are assigned to treatments based on severity,
- workers choose whether to migrate,
- students choose whether to attend college,
- survey respondents choose whether to answer,
- participants drop out of a study,
- researchers observe only surviving firms,
- policymakers target interventions to places already changing,
- analysts condition on a selected subgroup.

The central issue is that the observed comparison may not represent the counterfactual comparison needed for causality. For example, suppose participants in a job training program earn more than nonparticipants. This could mean the program increased earnings. But it could also mean that people who enrolled were more motivated, more informed, more connected, or more likely to find jobs even without training. The causal question is:

> What would participants have earned if they had not participated?

The naive comparison uses nonparticipants as a substitute for that missing counterfactual. Selection bias occurs when nonparticipants are not a credible substitute. The main lesson is:

> Selection bias arises when the process determining who is observed, treated, retained, or compared is related to the outcome we want to study.

---

## 6.2 Selection bias as a counterfactual problem
Causal inference requires comparing observed outcomes to missing counterfactual outcomes.

For a binary treatment, let: $D_i \in \{0,1\}$ where $D_i=1$ means unit $i$ is treated and $D_i=0$ means unit $i$ is untreated. Let the potential outcomes be: $Y_i(1)$ and: $Y_i(0)$ where:

- $Y_i(1)$ is unit $i$'s outcome if treated,
- $Y_i(0)$ is unit $i$'s outcome if untreated.

The observed outcome is: $Y_i = D_iY_i(1) + (1-D_i)Y_i(0)$ A common empirical comparison is: $\mathbb{E}[Y_i \mid D_i=1] - \mathbb{E}[Y_i \mid D_i=0]$ Using potential outcomes, this is: $\mathbb{E}[Y_i(1) \mid D_i=1] - \mathbb{E}[Y_i(0) \mid D_i=0]$ This compares treated units under treatment to untreated units without treatment. But the average treatment effect on the treated, or ATT, is: $ATT = \mathbb{E}[Y_i(1)-Y_i(0) \mid D_i=1]$ which equals: $ATT = \mathbb{E}[Y_i(1) \mid D_i=1] - \mathbb{E}[Y_i(0) \mid D_i=1]$ The missing counterfactual is: $\mathbb{E}[Y_i(0) \mid D_i=1]$ This is the average outcome treated units would have had if they had not been treated. The naive comparison substitutes: $\mathbb{E}[Y_i(0) \mid D_i=0]$ for: $\mathbb{E}[Y_i(0) \mid D_i=1]$ Selection bias occurs when these are different: $\mathbb{E}[Y_i(0) \mid D_i=1] \neq \mathbb{E}[Y_i(0) \mid D_i=0]$ In words:

> Treated and untreated units would have had different outcomes even if neither group had been treated.

That is the essence of selection bias in causal inference.

---

## 6.3 Decomposing the naive treated-control difference
The naive treated-control difference can be decomposed into a causal effect plus selection bias.

Start with the observed difference:

$$
\Delta_{naive}
=
\mathbb{E}[Y_i \mid D_i=1] - \mathbb{E}[Y_i \mid D_i=0]
$$

Using potential outcomes:

$$
\Delta_{naive}
=
\mathbb{E}[Y_i(1) \mid D_i=1] - \mathbb{E}[Y_i(0) \mid D_i=0]
$$

Add and subtract $\mathbb{E}[Y_i(0) \mid D_i=1]$:

$$
\Delta_{naive}
=
\mathbb{E}[Y_i(1) \mid D_i=1]
-
\mathbb{E}[Y_i(0) \mid D_i=1]
+
\mathbb{E}[Y_i(0) \mid D_i=1]
-
\mathbb{E}[Y_i(0) \mid D_i=0]
$$

Group the terms:

$$
\Delta_{naive}
=
ATT
+
\left(
\mathbb{E}[Y_i(0) \mid D_i=1]
-
\mathbb{E}[Y_i(0) \mid D_i=0]
\right)
$$

Therefore: $\Delta_{naive} = ATT + Selection\ Bias$ where:

$$
Selection\ Bias
=
\mathbb{E}[Y_i(0) \mid D_i=1]
-
\mathbb{E}[Y_i(0) \mid D_i=0]
$$

This decomposition is extremely important. It shows that a treated-control difference is causal only if the selection bias term is zero:

$$
\mathbb{E}[Y_i(0) \mid D_i=1]
=
\mathbb{E}[Y_i(0) \mid D_i=0]
$$

That condition says treated and untreated units would have had the same average untreated outcome. This is not a statistical detail. It is the core identifying assumption behind naive comparisons.

---

## 6.4 Positive and negative selection
Selection bias can go in either direction.

- **Positive selection.** Positive selection occurs when treated units would have had better outcomes than untreated units even without treatment.
Formally:

$$
\mathbb{E}[Y_i(0) \mid D_i=1]
>
\mathbb{E}[Y_i(0) \mid D_i=0]
$$

Example: a voluntary job training program attracts highly motivated workers. Even without training, these workers would have searched harder, networked more, and earned more than nonparticipants. In this case, the naive comparison overstates the effect of training. Suppose: $\mathbb{E}[Y_i(1) \mid D_i=1] = 40{,}000$ $\mathbb{E}[Y_i(0) \mid D_i=0] = 32{,}000$ The naive difference is: $40{,}000 - 32{,}000 = 8{,}000$ But if participants would have earned $36{,}000$ without training, then: $ATT = 40{,}000 - 36{,}000 = 4{,}000$ The naive comparison overstates the causal effect by $4{,}000$.

- **Negative selection.** Negative selection occurs when treated units would have had worse outcomes than untreated units even without treatment.
Formally:

$$
\mathbb{E}[Y_i(0) \mid D_i=1]
<
\mathbb{E}[Y_i(0) \mid D_i=0]
$$

Example: a job training program targets workers who are especially disadvantaged. Even without training, participants would have earned less than nonparticipants. In this case, the naive comparison understates the effect of training. Suppose: $\mathbb{E}[Y_i(1) \mid D_i=1] = 34{,}000$ $\mathbb{E}[Y_i(0) \mid D_i=0] = 32{,}000$ The naive difference is: $34{,}000 - 32{,}000 = 2{,}000$ But if participants would have earned only $26{,}000$ without training, then: $ATT = 34{,}000 - 26{,}000 = 8{,}000$ The naive comparison understates the causal effect. Selection bias is therefore not always upward or downward. Its direction depends on how selected units differ in their untreated potential outcomes.

---

## 6.5 Selection into treatment
Selection into treatment occurs when units receive treatment because of characteristics related to their potential outcomes.

This is common in economics because treatment is often chosen by individuals, firms, institutions, or policymakers. Examples:

- Students choose whether to attend college.
- Workers choose whether to enroll in job training.
- Firms choose whether to adopt new technology.
- Families choose where to live.
- Patients and doctors choose medical treatments.
- Governments choose where to implement policies.
- Banks choose which borrowers receive credit.

Treatment is rarely assigned randomly in observational data.

- **Example: college and earnings.** Suppose we compare earnings of college graduates and non-graduates.
The observed difference is:

$$
\mathbb{E}[Earnings_i \mid College_i=1]
-
\mathbb{E}[Earnings_i \mid College_i=0]
$$

This difference may reflect the causal effect of college. But it may also reflect selection into college. People who attend college may differ from non-attendees in:

- academic preparation,
- family income,
- parental education,
- neighborhood,
- school quality,
- health,
- expectations,
- motivation,
- social networks,
- risk tolerance,
- information about labor markets.

Many of these factors affect earnings even without college. Therefore:

$$
\mathbb{E}[Y_i(0) \mid College_i=1]
\neq
\mathbb{E}[Y_i(0) \mid College_i=0]
$$

The observed college wage premium is not automatically the causal return to college.

- **Example: firms adopting technology.** Suppose firms that adopt a new technology become more productive.
The naive comparison is:

$$
\mathbb{E}[Productivity_i \mid Adopt_i=1]
-
\mathbb{E}[Productivity_i \mid Adopt_i=0]
$$

But more productive firms may be more likely to adopt technology in the first place. They may have better managers, more capital, more skilled workers, and stronger demand. In that case, adoption is selected. The estimated relationship may overstate the causal effect of technology adoption.

- **Example: medical treatment.** Suppose patients receiving intensive treatment have worse outcomes than patients receiving standard treatment.
This does not necessarily mean intensive treatment is harmful. Sicker patients may be more likely to receive intensive treatment. This is negative selection into treatment. Treated patients have worse baseline prognosis. Without careful adjustment or design, the treatment may appear ineffective or harmful even if it improves outcomes relative to what would have happened otherwise.

---

## 6.6 Selection on observables and selection on unobservables
Selection bias is often classified by whether the variables driving selection are observed.

- **Selection on observables.** Selection on observables means treatment assignment depends on variables the researcher can measure.
Let $X_i$ be observed covariates, such as age, education, prior earnings, baseline health, test scores, location, or industry. A common identifying assumption is: $(Y_i(1),Y_i(0)) \perp D_i \mid X_i$ This is called conditional independence, unconfoundedness, ignorability, or selection on observables. It means:

> After comparing units with the same observed characteristics, treatment assignment is as good as random.

If this assumption is true, methods such as regression adjustment, matching, stratification, and inverse probability weighting can identify causal effects. For example, to estimate the effect of job training, one might compare participants and nonparticipants with the same:

- age,
- education,
- prior earnings,
- prior employment history,
- occupation,
- industry,
- local labor market,
- baseline unemployment duration.

If all relevant selection factors are observed and properly controlled, then selection bias may be removed. But this is a strong assumption.

- **Selection on unobservables.** Selection on unobservables means treatment assignment depends on variables the researcher does not observe.
Examples include:

- motivation,
- ability,
- ambition,
- family support,
- private health information,
- risk tolerance,
- managerial quality,
- political pressure,
- informal networks,
- expectations about future earnings.

If these unobserved factors affect both treatment and outcomes, then conditioning on observed variables is not enough. Formally, even after controlling for $X_i$: $(Y_i(1),Y_i(0)) \not\perp D_i \mid X_i$ In that case, regression controls, matching, and weighting may remain biased. Selection on unobservables often motivates stronger research designs, such as:

- randomized controlled trials,
- instrumental variables,
- regression discontinuity,
- difference-in-differences,
- fixed effects,
- natural experiments,
- sensitivity analysis,
- structural modeling.

The distinction between selection on observables and selection on unobservables is central to applied empirical work.

---

## 6.7 Selection bias as a sampling problem
Selection bias is not only about treatment assignment. It can also arise from how the sample is constructed.

A sample is selected if inclusion in the data is related to the outcome or to variables that affect the outcome.

- **Example: surveying gym members.** Suppose we want to estimate average exercise frequency in the general population but survey only gym members.
Gym members are more health-conscious and physically active than the average person. Therefore, the sample average will overstate exercise frequency in the population. The problem is:

$$
\mathbb{E}[Exercise_i \mid In\ Sample_i=1]
\neq
\mathbb{E}[Exercise_i]
$$

The sample is not representative of the population of interest.

- **Example: estimating wages using employed workers.** Suppose we estimate the relationship between education and wages using only employed workers.
Wages are observed only for people who work. But employment itself is selected. People who are employed may differ from non-employed people in:

- health,
- skills,
- preferences,
- family responsibilities,
- local labor market opportunities,
- reservation wages,
- access to childcare,
- discrimination.

If the selection into employment is related to wages, then estimates based only on employed workers may not generalize to the full working-age population. This is a classic sample selection problem.

- **Example: firm datasets.** Datasets often include only firms that survive long enough to be observed.
If weak firms exit before the data are collected, the sample contains surviving firms only. Estimates of productivity, growth, or technology effects may be biased because failed firms are missing. This is related to survivorship bias, discussed below. The general sampling problem is:

$$
\mathbb{E}[Y_i \mid S_i=1]
\neq
\mathbb{E}[Y_i]
$$

where $S_i=1$ indicates that unit $i$ is selected into the observed sample. A sample selection problem becomes a causal problem when the selection process distorts the comparison needed to estimate a causal effect.

---

## 6.8 Nonresponse and attrition
Selection bias can arise after a study begins if some units are not observed in later periods.

- **Nonresponse.** Nonresponse occurs when selected units do not provide data.
For example, a household survey may sample a representative group of households, but high-income households may be less likely to respond. If income is the outcome, nonresponse can bias estimates. Let $R_i=1$ indicate that unit $i$ responds. If:

$$
\mathbb{E}[Y_i \mid R_i=1]
\neq
\mathbb{E}[Y_i \mid R_i=0]
$$

then response is related to the outcome. If response also differs by treatment status, treatment effect estimates may be biased.

- **Attrition.** Attrition occurs when units leave a study over time.
For example, suppose researchers evaluate a job training program and follow participants for three years. If low-earning participants are more likely to disappear from the data, the program may appear more successful than it really is. Attrition is especially dangerous when it is differential by treatment status. Let $A_i=1$ indicate that unit $i$ remains observed. A treatment effect estimated among observed units is:

$$
\mathbb{E}[Y_i \mid D_i=1,A_i=1]
-
\mathbb{E}[Y_i \mid D_i=0,A_i=1]
$$

This may differ from the treatment effect in the original sample if attrition is related to potential outcomes. For example, if struggling treated workers are more likely to drop out of the survey, then observed treated workers will look unusually successful.

- **Diagnosing attrition.** Researchers often examine:
1. overall attrition rates,
2. attrition rates by treatment status,
3. whether baseline covariates predict attrition,
4. whether treatment affects attrition,
5. whether results are robust to assumptions about missing outcomes.

- **Responses to attrition.** Possible responses include:
- intensive tracking,
- administrative data linkage,
- inverse probability weighting,
- imputation,
- bounding exercises,
- Lee bounds,
- sensitivity analysis,
- intent-to-treat analysis,
- transparent reporting of missing data.

Attrition cannot be fixed simply by ignoring missing observations. If missingness is systematically related to outcomes, complete-case analysis may be biased.

---

## 6.9 Survivorship bias
Survivorship bias occurs when analysis focuses only on units that survived some selection process.

The classic structure is:

1. many units begin,
2. some fail or disappear,
3. researchers observe only the survivors,
4. conclusions are drawn as if survivors represent all units.

- **Example: successful firms.** Suppose we study the habits of successful startups and find that many of them expanded aggressively early on.
A naive conclusion might be:

> Aggressive expansion causes startup success.

But if many failed startups also expanded aggressively, and those failures are missing from the sample, the conclusion is biased. The sample includes: $Firms\ observed = Firms\ that\ survived$ not all firms that attempted the strategy.

- **Example: mutual funds.** Suppose we evaluate mutual fund performance using only funds that exist today. Poorly performing funds may have closed or merged. The surviving funds are positively selected.
Average historical returns among surviving funds may overstate the returns investors would have earned by choosing from the original set of funds.

- **Example: workers in an occupation.** Suppose we study wages among people who remain in a demanding occupation after ten years. Those who left may have had lower wages, worse conditions, or different preferences. The remaining workers are selected survivors.
The general problem is:

$$
\mathbb{E}[Y_i \mid Survived_i=1]
\neq
\mathbb{E}[Y_i]
$$

If survival is related to the outcome, then analyzing survivors alone can produce misleading conclusions. Survivorship bias is common in business, finance, labor economics, education, health, and historical research.

---

## 6.10 Selection from conditioning on a collider
Selection bias can also arise from conditioning on a variable that is caused by two other variables. Such a variable is called a collider.

Suppose: $X \rightarrow S \leftarrow Y$ Here $S$ is a collider because both $X$ and $Y$ cause $S$. If we condition on $S$, we can create an association between $X$ and $Y$ even if no causal relationship exists between them.

- **Example: elite college admissions.** Suppose admission to an elite college depends on talent and luck: $Talent \rightarrow Admission \leftarrow Luck$
Among admitted students, talent and luck may be negatively correlated. A student with less luck needed more talent to be admitted. A student with less talent needed more luck.

If we analyze only admitted students, we condition on admission. This can create misleading associations.

- **Example: hospitalization.** Suppose both chronic illness and accident severity affect whether someone is hospitalized: $Chronic\ Illness \rightarrow Hospitalized \leftarrow Accident\ Severity$
Among hospitalized patients, chronic illness and accident severity may be negatively associated. Patients with less severe accidents may be hospitalized only if they have chronic illness, while otherwise healthy patients may be hospitalized only for severe accidents.

- **Example: publication bias.** Suppose both study quality and surprising results affect whether a paper is published: $Study\ Quality \rightarrow Published \leftarrow Surprising\ Result$
Among published papers, low-quality studies may need more surprising results to be published, while high-quality studies may be published with less surprising results. Conditioning on publication can distort the relationship between quality and results.

This form of selection bias is sometimes called collider bias, endogenous selection, or selection on a common effect. The key lesson is:

> Conditioning on selected samples can create associations that do not exist in the broader population.

---

## 6.11 Policy targeting and endogenous treatment assignment
Selection bias is especially important in policy evaluation because policies are often targeted.

Governments rarely assign policies randomly. They may target programs to people or places with the greatest need, the strongest political support, or the highest expected returns.

- **Example: aid and economic growth.** Countries receiving more foreign aid may grow more slowly. A naive interpretation might be:
> Aid reduces growth.

But aid is often targeted to poorer countries, countries experiencing crises, or countries with weak institutions. These countries may have grown slowly even without aid. The comparison between high-aid and low-aid countries is selected.

- **Example: school funding.** Schools with more funding may have lower test scores if funding is targeted to disadvantaged schools.
A naive regression might suggest: $TestScores_i = \alpha + \beta Funding_i + u_i$ with $\hat{\beta}<0$. But this does not necessarily mean funding lowers achievement. Low-performing schools may receive more funding because policymakers target resources to need.

- **Example: policing.** High-crime neighborhoods often receive more police. A positive correlation between police and crime may reflect policy targeting rather than the causal effect of police.
- **Example: hospital resources.** Areas with poor health may receive more hospitals, clinics, or doctors. A positive association between medical resources and poor health may reflect need-based allocation.
The common structure is: $Baseline\ Need \rightarrow Treatment$ and: $Baseline\ Need \rightarrow Outcome$ Baseline need is a confounder. If it is not adequately addressed, estimates of policy effects may be biased. Policy targeting often creates negative selection: treated units are worse off at baseline. In such cases, naive comparisons may understate beneficial effects or make helpful policies look harmful.

---

## 6.12 Dynamic selection
Selection can change over time.

In panel and longitudinal settings, treatment may depend on past outcomes, and future outcomes may depend on past treatment. Example: $Y_{i,t-1} \rightarrow D_{it} \rightarrow Y_{it}$ If units receive treatment because of prior outcomes, treatment is dynamically selected.

- **Example: training after job loss.** Workers may enroll in training after experiencing unemployment or wage declines.
The timing might be: $Wage\ Decline_{t-1} \rightarrow Training_t \rightarrow Earnings_{t+1}$ A simple before-after comparison may be misleading because workers entered training after a negative shock. Earnings might rise afterward partly because of mean reversion, not because of training.

- **Example: medical treatment adjustment.** Doctors may intensify treatment when a patient's health worsens.
$Poor\ Health_{t-1} \rightarrow Treatment_t \rightarrow Health_t$
If prior health is not properly accounted for, treatment may appear harmful because sicker patients receive more treatment.

- **Example: firm investment.** Firms may invest in new technology after productivity falls or after demand rises.
If investment responds to past shocks, estimating its effect requires careful timing and controls. Dynamic selection creates challenges because:

- past outcomes may confound current treatment,
- treatment may affect future confounders,
- controlling for time-varying variables can block causal pathways,
- lagged outcomes may introduce bias in short panels,
- anticipation and feedback may be present.

Methods for dynamic selection include:

- event studies,
- difference-in-differences with pre-trend analysis,
- fixed effects,
- marginal structural models,
- instrumental variables,
- dynamic panel methods,
- structural models,
- careful timing restrictions.

---

## 6.13 Selection bias and regression
Selection bias often appears in regression through correlation between the explanatory variable and the error term.

Consider: $Y_i = \alpha + \beta D_i + u_i$ where $D_i$ is treatment. The coefficient $\beta$ can be interpreted causally only if: $\mathbb{E}[u_i \mid D_i] = 0$ This means unobserved determinants of $Y_i$ are not systematically related to treatment status. Selection bias violates this condition. Suppose: $u_i = Ability_i + Motivation_i + FamilyBackground_i + \varepsilon_i$ If ability, motivation, or family background affect both treatment and outcomes, then:

$$
\mathbb{E}[u_i \mid D_i=1]
\neq
\mathbb{E}[u_i \mid D_i=0]
$$

Equivalently: $\operatorname{Cov}(D_i,u_i) \neq 0$ In that case, ordinary least squares estimates a mixture of the treatment effect and selection differences. Adding controls may help if the controls capture the selection process. But adding controls does not automatically solve selection bias. If selection occurs through unobserved variables, the regression remains endogenous. Regression is a tool for adjustment. It is not, by itself, a research design.

---

## 6.14 Methods for addressing selection bias
There is no universal solution to selection bias. The appropriate method depends on the source of selection and the available data.

- **Randomization.** Random assignment solves selection into treatment in expectation.
If treatment is randomly assigned: $D_i \perp (Y_i(1),Y_i(0))$ Then treated and control groups are comparable in expectation, and a difference in means can identify the causal effect. Randomization is powerful because it addresses both observed and unobserved selection. However, RCTs may still suffer from:

- noncompliance,
- attrition,
- spillovers,
- measurement error,
- implementation failure,
- external validity limitations.

- **Regression controls.** Regression adjustment can address selection on observables.
A controlled regression might be: $Y_i = \alpha + \beta D_i + X_i'\gamma + u_i$ This can identify a causal effect if: $(Y_i(1),Y_i(0)) \perp D_i \mid X_i$ The problem is that this assumption fails if important unobserved confounders remain.

- **Matching.** Matching compares treated units to untreated units with similar observed characteristics.
The goal is to approximate treated-control comparability within strata of $X_i$. Matching can be useful when treated and untreated units overlap well on observables. It does not solve selection on unobservables.

- **Weighting.** Inverse probability weighting uses the probability of treatment, often called the propensity score: $p(X_i) = P(D_i=1 \mid X_i)$
Weights are used to create a pseudo-population in which covariates are balanced between treated and untreated groups.

Weighting relies on the same core assumptions as matching:

1. conditional independence,
2. overlap.

- **Fixed effects.** Fixed effects remove time-invariant unobserved differences across units.
A fixed effects model is: $Y_{it} = \alpha_i + \beta D_{it} + u_{it}$ The unit fixed effect $\alpha_i$ controls for stable characteristics of unit $i$. This helps if selection is based on fixed traits, such as stable ability, geography, or institutional quality. Fixed effects do not solve selection based on time-varying unobservables.

- **Difference-in-differences.** Difference-in-differences compares changes over time between treated and control groups.
It can address fixed differences between groups if the parallel trends assumption holds. The key assumption is:

> In the absence of treatment, treated and control groups would have followed parallel trends.

DiD does not solve selection bias if treated and control groups were already on different trajectories before treatment.

- **Regression discontinuity.** Regression discontinuity uses a cutoff that determines treatment assignment.
If units just above and below the cutoff are comparable, RD can reduce selection bias near the threshold. The key assumption is continuity of potential outcomes at the cutoff.

- **Instrumental variables.** Instrumental variables address selection bias by using a source of variation in treatment that is plausibly unrelated to unobserved determinants of the outcome.
An instrument $Z_i$ must satisfy:

1. relevance: $\operatorname{Cov}(Z_i,D_i) \neq 0$
2. exclusion:

$Z_i$ affects $Y_i$ only through $D_i$. IV can address selection on unobservables if the instrument is valid. But valid instruments are difficult to find, and IV estimates are often local to compliers.

- **Bounds and sensitivity analysis.** Sometimes selection bias cannot be eliminated convincingly. In that case, researchers may ask how large selection bias would need to be to overturn the result.
Sensitivity analysis examines whether conclusions are robust to plausible violations of assumptions. Bounding methods estimate a range of possible treatment effects under weaker assumptions. This is often more honest than pretending selection bias has been fully solved.

---

## 6.15 Heckman selection models
A classic econometric response to sample selection is the Heckman selection model.

This model is often used when the outcome is observed only for a selected sample. Example: wages are observed only for people who are employed. Let the outcome equation be: $Y_i = X_i'\beta + u_i$ But $Y_i$ is observed only if: $S_i=1$ where selection is determined by a latent index: $S_i^* = Z_i'\gamma + v_i$ and: $S_i = 1 \quad \text{if} \quad S_i^*>0$ The selection problem arises if: $\operatorname{Cov}(u_i,v_i) \neq 0$ That means unobserved factors affecting selection also affect the outcome. The Heckman model corrects for selection under distributional and functional form assumptions, often using an inverse Mills ratio. The method is useful, but it is not magic. It relies heavily on assumptions. It is most credible when there is an exclusion restriction: a variable that affects selection into the sample but does not directly affect the outcome. For example, in a wage equation, the number of young children might affect labor force participation but may not directly affect offered wages, conditional on other characteristics. Whether this is credible depends on the context. The broader lesson is:

> Sample selection models require assumptions just like design-based methods do. Modeling selection is not the same as eliminating it.

---

## 6.16 Diagnosing selection bias
Selection bias cannot always be tested directly because it involves missing counterfactuals. But researchers can look for warning signs.

Useful diagnostic questions include:

1. Who receives treatment?
2. Who does not receive treatment?
3. Why do some units receive treatment and others do not?
4. Is treatment chosen by individuals, firms, doctors, schools, or policymakers?
5. Are treated and untreated units similar before treatment?
6. Do treated and untreated units have similar baseline outcomes?
7. Do observable characteristics predict treatment?
8. Do unobservable characteristics likely predict treatment?
9. Is treatment targeted based on need or expected benefit?
10. Are some units missing from the sample?
11. Is attrition related to treatment or baseline characteristics?
12. Are only survivors observed?
13. Is the analysis conditioning on a selected subgroup?
14. Could selection create the observed relationship even if the causal effect were zero?

Empirical diagnostics include:

- baseline balance tables,
- comparison of pre-treatment outcomes,
- graphical comparison of trends,
- placebo outcomes,
- placebo treatments,
- attrition analysis,
- overlap checks,
- propensity score distributions,
- sensitivity analysis,
- bounding exercises,
- institutional investigation of assignment rules.

None of these diagnostics automatically proves that selection bias is absent. But they help evaluate whether the identifying assumptions are plausible.

---

## 6.17 Practical example: voluntary job training
Suppose a city offers a voluntary job training program to unemployed workers.

The researcher observes: $\mathbb{E}[Earnings_i \mid D_i=1] = 38{,}000$ and: $\mathbb{E}[Earnings_i \mid D_i=0] = 34{,}000$ The naive estimate is: $38{,}000 - 34{,}000 = 4{,}000$ Can we interpret this as the causal effect of training? Only if:

$$
\mathbb{E}[Y_i(0) \mid D_i=1]
=
\mathbb{E}[Y_i(0) \mid D_i=0]
$$

That is, participants and nonparticipants would have had equal earnings without the program. This assumption may fail for several reasons.

- **Positive selection possibility.** Participants may be more motivated, more informed, or more able to navigate public programs. If so, they may have earned more even without training.
Then:

$$
\mathbb{E}[Y_i(0) \mid D_i=1]
>
\mathbb{E}[Y_i(0) \mid D_i=0]
$$

The naive estimate overstates the effect.

- **Negative selection possibility.** Participants may be the most disadvantaged unemployed workers. Caseworkers may refer people with the worst job prospects. If so, participants may have earned less without training.
Then:

$$
\mathbb{E}[Y_i(0) \mid D_i=1]
<
\mathbb{E}[Y_i(0) \mid D_i=0]
$$

The naive estimate understates the effect.

- **Possible research designs.** A stronger design might use:
- a lottery if program slots are limited,
- random encouragement to participate,
- an eligibility cutoff,
- difference-in-differences with comparable nonparticipants,
- worker fixed effects with panel data,
- matching on rich pre-program characteristics,
- administrative data to reduce attrition.

The key question is not whether participants earned more. The key question is:

> What would participants have earned without training?

---

## 6.18 Practical example: online reviews
Selection bias is not limited to formal policy analysis. It also appears in everyday data.

Suppose a product has an average online rating of 4.8 stars. Does that mean the average customer experience is 4.8 stars? Not necessarily. The observed average is: $\mathbb{E}[Rating_i \mid Review_i=1]$ But the desired average customer experience may be: $\mathbb{E}[Rating_i]$ These are equal only if reviewers are representative of all customers. That may fail because people who leave reviews are often:

- extremely satisfied,
- extremely dissatisfied,
- unusually engaged,
- incentivized,
- repeat customers,
- more technologically comfortable,
- different from silent customers.

Therefore:

$$
\mathbb{E}[Rating_i \mid Review_i=1]
\neq
\mathbb{E}[Rating_i]
$$

This is sample selection. The same logic applies to course evaluations, employee satisfaction surveys, app ratings, restaurant reviews, and voluntary feedback forms. The broader lesson is:

> Observed data often come from people who chose to be observed.

---

## 6.19 Practical example: college earnings comparisons
Suppose we compare average earnings of graduates from elite colleges to average earnings of graduates from non-elite colleges.

The observed difference may be large. But students are selected into elite colleges. They may differ before college in:

- test scores,
- family income,
- parental education,
- ambition,
- high school quality,
- peer networks,
- geography,
- information,
- career goals.

A naive comparison estimates:

$$
\mathbb{E}[Y_i \mid Elite_i=1]
-
\mathbb{E}[Y_i \mid Elite_i=0]
$$

But the causal effect for elite-college students is: $\mathbb{E}[Y_i(1)-Y_i(0) \mid Elite_i=1]$ where:

- $Y_i(1)$ is earnings if student $i$ attends an elite college,
- $Y_i(0)$ is earnings if the same student attends a non-elite college.

The missing counterfactual is: $\mathbb{E}[Y_i(0) \mid Elite_i=1]$ What would elite-college students have earned if they had attended non-elite colleges? Non-elite college graduates may not provide a valid comparison if they differ substantially before college. Possible strategies include:

- comparing students admitted to the same elite schools but making different enrollment choices,
- using admissions cutoffs,
- using financial aid variation,
- controlling for rich pre-college measures,
- comparing applicants with similar test scores and backgrounds,
- using sibling comparisons where appropriate.

Each strategy has assumptions. None automatically solves selection.

---

## 6.20 Common mistakes

1. **Mistake 1: Assuming large samples eliminate selection bias.** Large samples reduce sampling error. They do not eliminate selection bias.
A huge biased sample can produce a very precise biased estimate. If the sample is selected, increasing the sample size may simply estimate the wrong quantity more precisely.

2. **Mistake 2: Treating controls as a cure-all.** Adding controls helps only if the controls capture the relevant selection process and are not themselves bad controls.
If treatment selection depends on unobserved motivation, ability, or private information, ordinary controls may not solve the problem.

3. **Mistake 3: Ignoring who is missing.** Missing observations are often informative.
If people drop out of a survey, firms exit the market, patients stop reporting outcomes, or students leave school, the missingness may be related to the outcome. Ignoring missing data can bias results.

4. **Mistake 4: Comparing treated and untreated units without asking why treatment occurred.** Treatment assignment always has a story. Someone chose, assigned, targeted, or became exposed to treatment for a reason.
A researcher should ask:

> Why did these units get treated while those units did not?

The answer often reveals the main selection problem.

5. **Mistake 5: Conditioning on selected samples without recognizing it.** Many analyses implicitly condition on selection:
- employed workers,
- admitted students,
- surviving firms,
- hospitalized patients,
- published studies,
- survey respondents,
- program participants.

The conclusions may apply only to that selected group, and even within that group, conditioning may create bias.

6. **Mistake 6: Confusing representativeness with causal validity.** A representative sample is useful for describing a population. But representativeness alone does not identify causal effects.
A nonrepresentative sample can sometimes identify a causal effect internally if treatment is randomized within the sample. A representative sample can fail to identify a causal effect if treatment is selected. Sampling validity and causal identification are related but distinct.

---

## 6.21 Application checklist
When evaluating possible selection bias, use the following checklist.

1. **Define the target quantity.** Are you trying to estimate:
- a population mean,
- a descriptive relationship,
- ATE,
- ATT,
- ATU,
- CATE,
- LATE,
- a policy-relevant effect for a specific group?

Selection bias depends on the target.

2. **Identify the selection process.** Who is included in the sample?
Who receives treatment? Who remains observed? Who is excluded? Who chooses participation? Who assigns treatment?

3. **Compare selected and non-selected units.** Are selected units different from non-selected units in observed characteristics?
Are they likely different in unobserved characteristics? Do they differ in baseline outcomes?

4. **Identify the missing counterfactual.** For treated units, what untreated outcome is missing?
For untreated units, what treated outcome is missing? For missing units, what outcome is unobserved?

5. **Determine the likely direction of selection.** Are treated units positively selected?
Are they negatively selected? Could selection go in both directions? Is the sign theoretically ambiguous?

6. **Assess whether controls are sufficient.** Are the selection variables observed?
Are they measured well? Are there important unobservables? Is there overlap between treated and untreated units?

7. **Look for design-based variation.** Is there random assignment?
A lottery? An eligibility cutoff? A policy shock? A natural experiment? An instrument? Panel variation? Pre-treatment trends?

8. **Examine missing data and attrition.** How much data are missing?
Is missingness related to treatment? Is missingness related to baseline outcomes? Could attrition explain the result?

9. **Conduct robustness and sensitivity analysis.** How large would selection bias need to be to overturn the conclusion?
Do results change with different comparison groups? Do placebo tests fail or pass? Do results hold under bounding assumptions?

10. **Interpret scope carefully.** Do results apply to:
- all units,
- treated units,
- compliers,
- observed survivors,
- respondents,
- units near a cutoff,
- a selected subgroup?

State the scope explicitly.

---

## 6.22 Summary
Selection bias occurs when the process determining who is treated, untreated, observed, retained, or analyzed is systematically related to outcomes or potential outcomes.

In causal inference, the key condition for a naive treated-control comparison to identify the ATT is:

$$
\mathbb{E}[Y_i(0) \mid D_i=1]
=
\mathbb{E}[Y_i(0) \mid D_i=0]
$$

When this fails, treated and untreated units would have differed even without treatment. The naive difference can be decomposed as:

$$
\mathbb{E}[Y_i \mid D_i=1] - \mathbb{E}[Y_i \mid D_i=0]
=
ATT + Selection\ Bias
$$

Selection bias can arise from:

- voluntary treatment participation,
- policy targeting,
- sample selection,
- nonresponse,
- attrition,
- survivorship,
- conditioning on colliders,
- dynamic treatment assignment,
- missing data,
- unobserved heterogeneity.

Selection can be positive or negative. It can make treatment effects look larger, smaller, zero, or even opposite in sign. Methods such as randomization, controls, matching, weighting, fixed effects, difference-in-differences, regression discontinuity, instrumental variables, selection models, bounds, and sensitivity analysis are all attempts to address different forms of selection. None works automatically. Each relies on assumptions. The central question is always:

> Why is the observed comparison a credible substitute for the missing counterfactual?

A rigorous empirical analysis does not merely report differences between selected groups. It explains the selection process, states the assumptions required to overcome it, and evaluates whether those assumptions are plausible.
