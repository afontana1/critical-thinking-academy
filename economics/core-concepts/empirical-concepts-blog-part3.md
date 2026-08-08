# Core Concepts in Empirical Economics and Causal Inference, Part 3

## Table of Contents

- [13. Panel Data, Cross-Sectional Data, and Longitudinal Research Design](#13-panel-data-cross-sectional-data-and-longitudinal-research-design)
- [14. Fixed Effects and Random Effects](#14-fixed-effects-and-random-effects)
- [15. Internal Validity, External Validity, and the Broader Validity Framework](#15-internal-validity-external-validity-and-the-broader-validity-framework)
- [16. Heterogeneous Treatment Effects](#16-heterogeneous-treatment-effects)
- [17. Effect Size, Economic Significance, and Uncertainty](#17-effect-size-economic-significance-and-uncertainty)
- [18. Type 1 and Type 2 Errors, Power, Multiple Testing, and Bayesian Evidence](#18-type-1-and-type-2-errors-power-multiple-testing-and-bayesian-evidence)
- [19. Cost-Benefit Analysis and Policy Evaluation](#19-cost-benefit-analysis-and-policy-evaluation)

## Introduction to Part 3

This document continues the empirical concepts series. Part 1 introduced the foundations of causal inference: correlation versus causation, counterfactual reasoning, causal graphs, exogeneity, omitted variable bias, and selection bias. Part 2 developed the major design-based tools used to estimate causal effects, including randomized controlled trials, natural experiments, identification strategies, instrumental variables, difference-in-differences, and regression discontinuity. Part 3 turns to data structure, longitudinal reasoning, and interpretation. The same causal questions remain central, but the form of the data changes what can be learned. In particular, panel and longitudinal data allow researchers to observe the same units over time. This creates powerful opportunities for causal inference, but it also introduces new threats: dynamic feedback, anticipation, attrition, serial correlation, changing composition, treatment timing, and time-varying confounding. The goal of this part is to explain how economists use repeated observations over time, what problems those data solve, what problems they create, and how concepts such as fixed effects, random effects, internal validity, external validity, heterogeneous treatment effects, uncertainty, and cost-benefit analysis fit into a rigorous empirical workflow.

---

# 13. Panel Data, Cross-Sectional Data, and Longitudinal Research Design
## 13.1 Why data structure matters
Empirical economics is not only about which variables are measured. It is also about how the data are organized. The same variables can support very different kinds of empirical analysis depending on whether they are observed once, repeatedly over time, across groups, across locations, or across treatment regimes. For example, suppose we want to study the relationship between education and wages. We might have:
- a one-time survey of workers in 2026
- repeated surveys of different workers each year
- repeated observations of the same workers over many years
- matched employer-employee records
- administrative data tracking workers before and after a policy change
- regional data on wages and schooling over several decades

Each dataset allows different comparisons. A one-time cross-section compares different people to each other. A panel dataset can compare the same person to themselves over time. A repeated cross-section can compare population-level changes over time but may not follow the same individuals. Administrative panel data may allow precise timing of treatment, outcomes, and employment histories. These distinctions matter because causal inference depends on counterfactual comparisons. A cross-sectional comparison might ask:
$\mathbb{E}[Y_i \mid D_i=1] - \mathbb{E}[Y_i \mid D_i=0]$ This compares treated and untreated units at a point in time. A panel comparison might ask:
$Y_{it}^{after} - Y_{it}^{before}$ This compares the same unit before and after a change. A difference-in-differences comparison combines both:
$$
\left( Y_{treated,after} - Y_{treated,before} \right)
-
\left( Y_{control,after} - Y_{control,before} \right)
$$

This compares changes over time between treated and untreated groups. The choice of data structure determines which sources of variation are available and which assumptions are needed. The central lesson of this section is:

> Data structure shapes causal identification. Cross-sectional data compare different units. Panel data compare units over time. Longitudinal designs can remove some confounding, but they also introduce new threats that must be handled explicitly.

## 13.2 Cross-sectional data

Cross-sectional data observe many units at one point in time, or over a short period that is treated as one time period. A unit may be an individual, household, firm, school, hospital, city, state, country, or market. Examples of cross-sectional data include:
- wages, education, age, and occupation for workers in 2026
- income, consumption, and family size for households in a survey year
- productivity, employment, and capital stock for firms in one fiscal year
- test scores, class size, and school funding for schools in one academic year
- crime rates, police staffing, and poverty rates across cities in one year

A typical cross-sectional regression is:

$Y_i = \alpha + \beta X_i + u_i$ where:
- $i$ indexes units
- $Y_i$ is the outcome
- $X_i$ is the explanatory variable or treatment
- $u_i$ contains unobserved determinants of $Y_i$

For example:

$Wage_i = \alpha + \beta Education_i + u_i$

This regression compares workers with different levels of education at the same point in time. The main advantage of cross-sectional data is that they are often easy to collect and can contain rich information about many units. They are useful for description, prediction, inequality measurement, market characterization, and exploratory analysis. But cross-sectional data face a major causal problem: units differ from each other in many unobserved ways. Workers with more education may differ from less educated workers in ability, motivation, family background, school quality, health, local labor market access, social networks, and expectations. Cities with more police may differ from cities with fewer police in poverty, crime history, political preferences, reporting behavior, demographics, and urban density. Firms that adopt new technology may differ from firms that do not in management quality, market power, financing access, and growth opportunities. In cross-sectional data, these differences can create confounding. A cross-sectional regression identifies a causal effect only under strong assumptions, such as:
$\mathbb{E}[u_i \mid X_i] = 0$ or, in potential outcomes language:

$(Y_i(1),Y_i(0)) \perp D_i \mid X_i$

if the treatment is binary and controls are included. This means that, after conditioning on observed variables, treatment assignment is unrelated to unobserved potential outcomes. In many observational cross-sections, this assumption is difficult to defend. Cross-sectional data can still be valuable for causal research when combined with strong design features, such as:

- randomized assignment measured at one point in time
- regression discontinuity around a cutoff
- instrumental variables
- rich pre-treatment controls
- credible institutional variation
- matching or weighting under selection-on-observables assumptions

But without a credible design, cross-sectional regressions are usually best interpreted as associations rather than causal effects.

## 13.3 Repeated cross-sectional data
Repeated cross-sectional data observe different samples from the same population at multiple points in time. For example:
- a labor force survey samples different households every month
- a national health survey samples different people each year
- a consumer expenditure survey repeatedly samples households over time
- annual school-level data observe different cohorts of students each year
- election surveys sample different voters in each election cycle

Repeated cross-sections have a time dimension, but they do not necessarily follow the same units. A repeated cross-section may contain observations such as:
$Y_{it}$

where $i$ indexes individuals observed in time period $t$, but the individuals observed in period $t$ may not be the same individuals observed in period $t+1$. 

This structure allows researchers to study changes in population averages over time:

$\mathbb{E}[Y \mid t=after] - \mathbb{E}[Y \mid t=before]$ 

It can also support difference-in-differences designs if some groups are treated and others are not:

$$
\left( \bar{Y}_{treated,after} - \bar{Y}_{treated,before} \right)
-
\left( \bar{Y}_{control,after} - \bar{Y}_{control,before} \right)
$$

Repeated cross-sections are especially common in policy evaluation because many public surveys are not true panels. For example, suppose a state raises its minimum wage. A researcher may not observe the same workers before and after the policy, but they may observe representative samples of workers in treated and control states before and after the change. The estimand is then about population-level changes, not necessarily within-person changes. Repeated cross-sections are useful when:

- the population is stable or well defined
- samples are representative within each period
- treatment occurs at a group level
- the outcome of interest is a group or population average
- following the same units is unnecessary or impossible

However, repeated cross-sections raise composition concerns. If the people observed after treatment are different from the people observed before treatment, changes in outcomes may reflect changes in composition rather than changes caused by treatment. For example, suppose a city implements a housing policy and average neighborhood income rises afterward. This could happen because existing residents earn more, or because lower-income residents leave and higher-income residents move in. A repeated cross-section may show the average change, but it may not reveal whether the same people benefited. This distinction matters for policy interpretation. A repeated cross-section can answer:

> How did the average outcome in this population or place change?

A panel can answer:

> How did outcomes change for the same units over time?

Both questions can be important, but they are not the same.

## 13.4 Panel data

Panel data observe the same units repeatedly over time. A panel dataset has at least two dimensions:
- a unit dimension, indexed by $i$
- a time dimension, indexed by $t$

The outcome is usually written as:
$Y_{it}$ where $Y_{it}$ is the outcome for unit $i$ at time $t$. Examples include:
- workers followed annually from 2015 to 2026
- firms observed quarterly over ten years
- schools observed across academic years
- hospitals observed monthly
- counties observed annually
- countries observed over decades
- households followed through a longitudinal survey

A basic panel regression is:
$Y_{it} = \alpha + \beta X_{it} + u_{it}$
where $X_{it}$ varies across units and over time. Panel data are powerful because they allow researchers to observe within-unit change. Instead of only comparing different workers to each other, we can ask:

> When the same worker gets more training, do their wages change?

Instead of only comparing different firms to each other, we can ask:

> When the same firm adopts a new technology, does productivity change?

Instead of only comparing different cities to each other, we can ask:

> When the same city changes policing policy, does crime change?

This is valuable because many confounders are stable over time. For example, a worker's early family background, innate ability, place of birth, and childhood environment may be mostly fixed during adulthood. A firm's founding culture, industry, location, and long-run management quality may be relatively stable. A city's geography, climate, and historical infrastructure may change slowly. Panel data can help control for these stable differences by comparing each unit to itself over time. This idea leads naturally to fixed effects, which are covered in the next section.

## 13.5 Balanced and unbalanced panels
A panel is balanced if every unit is observed in every time period. For example, if 1,000 firms are observed every year from 2010 through 2020, and no firm is missing in any year, the panel is balanced. A panel is unbalanced if some units are missing in some periods. For example, a firm may enter the dataset in 2014, exit in 2018, skip reporting in 2016, or merge with another firm. A household may be surveyed for some years but not others. A worker may disappear from administrative records if they leave formal employment. Balanced panels are analytically convenient, but unbalanced panels are common in real data. Unbalancedness is not automatically a problem. It becomes a problem when missingness is related to treatment and outcomes. Suppose a job training study follows workers for five years. If low-earning treated workers are more likely to disappear from the data, the observed treatment group will look more successful than it really is. If struggling firms are more likely to exit after a policy change, estimates using surviving firms may be biased. This is attrition or selection from the panel. Researchers should ask:
- Which units enter the panel?
- Which units exit the panel?
- Is entry or exit related to treatment?
- Is entry or exit related to outcomes?
- Are missing observations random or systematic?
- Does treatment affect the probability of being observed?

A common diagnostic is to estimate whether treatment predicts attrition:
$Attrit_{it} = \alpha + \beta D_{it} + \gamma X_{it} + u_{it}$ If treatment changes the probability of remaining in the data, outcome estimates may be biased. Possible responses include:
- reporting attrition rates by treatment status
- testing whether baseline covariates predict attrition
- inverse probability weighting
- bounding exercises
- administrative data linkage
- sensitivity analysis
- redefining the estimand to include attrition-related outcomes
- using intent-to-treat analysis when appropriate

## 13.6 Longitudinal studies
A longitudinal study follows units over time to study change, persistence, development, or dynamic effects. All panel studies are longitudinal in a broad sense, but the term longitudinal is especially common when researchers follow people, households, children, patients, firms, or communities over a meaningful portion of their life cycle. Examples include:
- following children from early childhood into adulthood
- tracking workers before and after job displacement
- observing families across generations
- following firms from startup to exit
- tracking neighborhoods before and after redevelopment
- observing patients before and after a health intervention

Longitudinal data allow researchers to ask questions that cannot be answered with one-time observations:
- How persistent are income differences?
- Do early childhood interventions have long-run effects?
- How do workers recover after unemployment?
- Do firms become more productive after adopting technology?
- How long do policy effects last?
- Do treatment effects grow, fade, or reverse over time?

A dynamic treatment effect can be written as:
$\tau_k = \mathbb{E}[Y_{i,t+k}(1) - Y_{i,t+k}(0)]$
where $k$ is the number of periods after treatment. For example, $\tau_1$ might be the effect one year after treatment, while $\tau_5$ is the effect five years later. This matters because many policies have time profiles. A job training program may reduce earnings at first while participants spend time in training, then increase earnings later. An early childhood program may have modest short-run test score effects but large long-run effects on graduation, earnings, or crime. A tax incentive may produce an immediate investment response that fades over time. Longitudinal data make it possible to study these patterns.

## 13.7 Within-unit and between-unit variation
Panel data contain two major types of variation: between-unit variation and within-unit variation. Between-unit variation compares different units to each other. For example:

> Do firms with more technology have higher productivity than firms with less technology?

Within-unit variation compares a unit to itself over time. For example:

> Does a firm's productivity increase after it adopts more technology?

These are different comparisons. A simple panel model without fixed effects may use both between-unit and within-unit variation:
$Y_{it} = \alpha + \beta X_{it} + u_{it}$ But a fixed effects model uses within-unit variation:
$Y_{it} = \alpha_i + \beta X_{it} + u_{it}$
Here $\alpha_i$ captures all time-invariant differences across units. The coefficient $\beta$ is identified by changes in $X_{it}$ within the same unit over time. This distinction is important because between-unit comparisons and within-unit comparisons may answer different questions. For example, firms that use more technology may be more productive than firms that use less technology. But this does not prove that technology caused productivity. More productive firms may have better managers and more resources, allowing them to adopt technology. The within-firm question is different:

> When the same firm adopts technology, does productivity rise?

This comparison removes stable firm differences, but it still may be biased if firms adopt technology when demand is already rising. Thus, within-unit variation can solve some problems but not all.

## 13.8 Unit fixed differences and the motivation for panel methods
Many units have unobserved characteristics that are stable over time. For workers, these may include:
- childhood environment
- innate ability
- family background
- early schooling quality
- personality traits
- long-run health endowments
- baseline preferences

For firms, these may include:
- management quality
- industry
- location
- firm culture
- production technology
- brand reputation
- founding conditions

For places, these may include:
- geography
- climate
- historical institutions
- transportation infrastructure
- long-run political culture
- industrial history
- natural resources

If these stable traits affect both treatment and outcome, cross-sectional comparisons are confounded. A useful panel model decomposes the error term into a time-invariant unit component and an idiosyncratic component:
$Y_{it} = \alpha + \beta X_{it} + a_i + \varepsilon_{it}$ where:
- $a_i$ is an unobserved unit-specific factor that does not vary over time
- $\varepsilon_{it}$ is a time-varying error term

If $a_i$ is correlated with $X_{it}$, then estimating a pooled regression without accounting for $a_i$ produces bias. For example, suppose more able workers obtain more training and also earn higher wages. If ability is stable and unobserved, then:
$\operatorname{Cov}(Training_{it},a_i) \neq 0$ A pooled regression of wages on training may be biased. Panel methods, especially fixed effects, try to remove $a_i$ by comparing each unit to itself over time.

## 13.9 First differences
One simple way to remove time-invariant unit heterogeneity is to take first differences. Suppose the model is:
$Y_{it} = \alpha + \beta X_{it} + a_i + \varepsilon_{it}$ For two periods, $t=1$ and $t=2$:
$Y_{i2} = \alpha + \beta X_{i2} + a_i + \varepsilon_{i2}$
$Y_{i1} = \alpha + \beta X_{i1} + a_i + \varepsilon_{i1}$ Subtract the second equation from the first:
$Y_{i2}-Y_{i1} = \beta(X_{i2}-X_{i1}) + (\varepsilon_{i2}-\varepsilon_{i1})$ The unit-specific term $a_i$ disappears because it is the same in both periods. Define:
$\Delta Y_i = Y_{i2}-Y_{i1}$ and:
$\Delta X_i = X_{i2}-X_{i1}$ Then:
$\Delta Y_i = \beta \Delta X_i + \Delta \varepsilon_i$ This first-difference model estimates whether changes in $X$ are associated with changes in $Y$. For example:
$\Delta Wage_i = \beta \Delta Training_i + \Delta \varepsilon_i$
This asks whether workers whose training status changed also experienced wage changes. First differencing removes time-invariant confounders, but it does not remove time-varying confounders. If workers receive training exactly when their earnings trajectory is already changing, then:
$\operatorname{Cov}(\Delta Training_i, \Delta \varepsilon_i) \neq 0$ and the first-difference estimate is still biased.

## 13.10 Fixed effects intuition
Fixed effects generalize the same idea to more than two periods. A unit fixed effects model is:
$Y_{it} = \alpha_i + \beta X_{it} + \varepsilon_{it}$
where $\alpha_i$ is a separate intercept for each unit. The fixed effect absorbs all characteristics of unit $i$ that are constant over time. This includes both observed and unobserved time-invariant characteristics. For example, in a worker panel:
$Wage_{it} = \alpha_i + \beta Training_{it} + \varepsilon_{it}$
The worker fixed effect $\alpha_i$ captures stable worker traits such as long-run ability, family background, baseline motivation, and early education. The coefficient $\beta$ is estimated from within-worker changes in training status and wages. In a firm panel:
$Productivity_{it} = \alpha_i + \beta Technology_{it} + \varepsilon_{it}$ The firm fixed effect captures stable firm quality, industry, location, culture, and management differences. In a county panel:
$Crime_{it} = \alpha_i + \beta Police_{it} + \varepsilon_{it}$ The county fixed effect captures stable geographic, institutional, and demographic features of the county. The fixed effects idea can be summarized as:

> Compare each unit to itself over time, rather than comparing different units to each other.

This is powerful because many confounders are stable. But it is not magic. Fixed effects do not solve bias from time-varying confounders.

## 13.11 Time fixed effects
Panel data often include shocks common to all units in a given time period. Examples include:
- recessions
- inflation
- national policy changes
- technological change
- pandemics
- wars
- seasonality
- interest rate changes
- commodity price shocks

A model with time fixed effects is:
$Y_{it} = \alpha + \lambda_t + \beta X_{it} + \varepsilon_{it}$
where $\lambda_t$ is a separate intercept for each time period. Time fixed effects absorb shocks common to all units in period $t$. A two-way fixed effects model includes both unit and time fixed effects:
$Y_{it} = \alpha_i + \lambda_t + \beta X_{it} + \varepsilon_{it}$ where:
- $\alpha_i$ controls for time-invariant unit differences
- $\lambda_t$ controls for common time shocks
- $\beta$ is identified by within-unit changes in $X_{it}$ relative to common changes over time

For example, in a state-level minimum wage study:
$Employment_{st} = \alpha_s + \lambda_t + \beta MinimumWage_{st} + \varepsilon_{st}$
State fixed effects control for stable differences across states. Year fixed effects control for national shocks affecting all states. The estimate uses within-state changes in minimum wages relative to national time patterns. This model is common, but it requires strong assumptions. It assumes that after controlling for state and year fixed effects, changes in the minimum wage are not correlated with other state-specific time-varying shocks affecting employment.

## 13.12 What panel data can solve
Panel data can help with several empirical problems.
- **Time-invariant omitted variables.**
If an omitted confounder is constant over time, fixed effects can remove it. For example, suppose worker ability is fixed and affects both training and wages. Worker fixed effects remove the stable ability component.
- **Baseline differences in levels.**
Treated and control units may have different baseline outcome levels. Panel methods can allow these level differences while focusing on changes. Difference-in-differences uses this logic. Treated units do not need to have the same level as control units. They need to have a credible counterfactual trend.
- **Dynamic patterns.**
Panel data allow researchers to study effects before and after treatment. For example, an event-study model can estimate whether outcomes changed before treatment and how effects evolved afterward.
- **Persistence and lagged effects.**
Many effects are delayed. Panel data allow the estimation of treatment effects at multiple horizons. For example:
$Y_{i,t+k} = \alpha_i + \lambda_t + \beta_k D_{it} + \varepsilon_{i,t+k}$ where $\beta_k$ is the effect $k$ periods after treatment.
- **Repeated treatment exposure.**
Some treatments are repeated or continuous over time, such as pollution exposure, schooling, policing, healthcare access, or tax rates. Panel data allow researchers to measure cumulative or lagged exposure. For example:
$Y_{it} = \alpha_i + \lambda_t + \beta_0 Pollution_{it} + \beta_1 Pollution_{i,t-1} + \beta_2 Pollution_{i,t-2} + \varepsilon_{it}$ This allows current outcomes to depend on current and past exposure.

## 13.13 What panel data cannot solve
Panel data do not automatically identify causal effects. They cannot solve every form of confounding.
- **Time-varying confounding.**
If unobserved confounders change over time and are correlated with treatment changes, fixed effects do not remove them. For example, suppose firms adopt technology when demand is rising. Demand shocks are time-varying. A firm fixed effect does not remove them. $Technology_{it} \leftarrow DemandShock_{it} \rightarrow Productivity_{it}$ If the demand shock is omitted, the estimated effect of technology may be biased.
- **Reverse causality over time.**
The outcome may affect future treatment. For example, low wages may cause a worker to seek training. Poor health may cause a person to obtain insurance. Rising crime may cause cities to hire more police. This creates dynamic feedback:
$Y_{i,t-1} \rightarrow D_{it} \rightarrow Y_{it}$ If past outcomes affect treatment timing, simple panel models may be biased.
- **Anticipation effects.**
Units may respond before treatment begins. For example, firms may adjust hiring before a law takes effect. Students may change effort before a scholarship rule is applied. Households may move before a zoning policy is implemented. If outcomes change before observed treatment, a before-after design may mismeasure the effect.
- **Measurement error.**
Panel methods can sometimes worsen measurement error problems. If $X_{it}$ is measured with error, differencing may amplify noise because the signal in changes may be small relative to measurement error. Suppose:
$X_{it}^{obs} = X_{it}^{true} + \nu_{it}$ Then:
$\Delta X_i^{obs} = \Delta X_i^{true} + \Delta \nu_i$ If true changes are small and measurement error is large, first-difference or fixed effects estimates can be severely attenuated.
- **Limited within-unit variation.**
Fixed effects require within-unit changes in treatment. If treatment barely changes over time within units, fixed effects may estimate effects imprecisely or rely on a small subset of changers. For example, if most people never change education after adulthood, a worker fixed effects model cannot estimate the effect of education well using adult panel data.
- **Bad controls.**
Panel data contain many variables measured over time. Some are pre-treatment confounders, some are mediators, and some are post-treatment outcomes. Controlling for variables affected by prior treatment can introduce bias. For example:
$Training_{it} \rightarrow Employment_{i,t+1} \rightarrow Earnings_{i,t+2}$ If the goal is to estimate the total effect of training on later earnings, controlling for employment at $t+1$ may block part of the effect.

## 13.14 Strict exogeneity in panel data
A key condition in many panel models is strict exogeneity. Consider the model:
$Y_{it} = \alpha_i + \beta X_{it} + u_{it}$ Strict exogeneity requires:
$\mathbb{E}[u_{it} \mid X_{i1}, X_{i2}, \dots, X_{iT}, \alpha_i] = 0$
for all $t$. This means that the error term at time $t$ is unrelated to the explanatory variable in every time period: past, present, and future. This is stronger than requiring $u_{it}$ to be unrelated only to $X_{it}$. Strict exogeneity fails if future treatment responds to current shocks. For example, suppose a worker receives a negative wage shock in year $t$, and this causes them to enroll in training in year $t+1$. Then:
$u_{it} \rightarrow Training_{i,t+1}$
The current error term is related to future treatment. Strict exogeneity fails. Strict exogeneity also fails if treatment is chosen in anticipation of future shocks. For example, a firm may adopt technology because it expects demand to rise next year. If expected demand is related to future productivity shocks, treatment timing is endogenous. The practical implication is important:

> Fixed effects remove time-invariant confounding, but causal interpretation still requires that within-unit treatment changes are not driven by time-varying unobserved shocks related to outcomes.

## 13.15 Lagged dependent variables
Researchers often include lagged outcomes as controls:
$Y_{it} = \alpha + \rho Y_{i,t-1} + \beta X_{it} + u_{it}$
This can be useful when outcomes are persistent. For example, wages, health, test scores, crime, and productivity often depend on their past values. However, lagged dependent variables require caution in panel data. If there are unit fixed effects, the dynamic panel model becomes:
$Y_{it} = \alpha_i + \rho Y_{i,t-1} + \beta X_{it} + u_{it}$
In short panels, including $Y_{i,t-1}$ with fixed effects can produce bias because the lagged dependent variable is mechanically correlated with the transformed error term. This is often called dynamic panel bias or Nickell bias. The issue arises because demeaning the data uses the unit's time average, and the lagged outcome is related to the time average of the error. Dynamic panel models may require specialized methods, such as:
- Arellano-Bond estimators
- system GMM
- longer panels
- bias corrections
- careful modeling of initial conditions

Beyond the technical issue, lagged outcomes also have causal interpretation challenges. A lagged outcome may be a proxy for prior confounding, but it may also be affected by earlier treatment. If prior treatment affects both lagged outcomes and later outcomes, controlling for lagged outcomes may block part of the treatment effect. For example:
$D_{i,t-1} \rightarrow Y_{i,t-1} \rightarrow Y_{it}$ If $Y_{i,t-1}$ is controlled for, the estimated coefficient on current treatment may not represent the total effect of the treatment history.

## 13.16 Time-varying covariates
Panel data often include covariates that vary over time. Examples include:
- income
- employment status
- health status
- marital status
- firm size
- industry conditions
- local unemployment
- school funding
- neighborhood composition

Including time-varying covariates can improve causal inference if they are true time-varying confounders. For example:
$Y_{it} = \alpha_i + \lambda_t + \beta D_{it} + \gamma X_{it} + u_{it}$ where $X_{it}$ is a time-varying confounder. But time-varying controls are dangerous when they are affected by treatment. Suppose:
$D_{it} \rightarrow X_{i,t+1} \rightarrow Y_{i,t+2}$ Then $X_{i,t+1}$ is a mediator, not a pre-treatment confounder. Controlling for it changes the estimand. Even more complicated, a variable can be both:
- a confounder for future treatment
- a mediator of past treatment

This occurs in longitudinal treatment settings. For example, health status may affect whether someone receives future medical treatment, but past treatment may also affect current health status:
$D_{i,t-1} \rightarrow Health_{it} \rightarrow D_{it} \rightarrow Y_{i,t+1}$ In such settings, ordinary regression adjustment can fail. Researchers may need methods designed for time-varying treatment and time-varying confounding, such as:
- marginal structural models
- inverse probability of treatment weighting
- g-computation
- structural nested models
- dynamic treatment regime methods

The central lesson is:

> In panel data, whether a covariate is a good control depends on timing and causal structure.

## 13.17 Serial correlation
Panel data often have serial correlation, meaning errors are correlated over time within a unit. For example, if a worker has an unusually high wage in one year, they may also have an unusually high wage the next year. If a county has high crime in one year, it may have high crime the next year. If a firm has a positive productivity shock, the shock may persist. Formally, serial correlation means:
$\operatorname{Cov}(u_{it},u_{is}) \neq 0$
for different time periods $t \neq s$ within the same unit. Serial correlation matters for statistical inference. If researchers ignore it, standard errors may be too small, leading to overconfident conclusions. In panel settings, researchers often cluster standard errors at the unit level. Clustering allows arbitrary correlation of errors within units over time:
$\operatorname{Cov}(u_{it},u_{is}) \neq 0$ while assuming independence across clusters. For example:
- state-level panels often cluster by state
- county-level panels often cluster by county
- firm-level panels often cluster by firm
- school-level panels often cluster by school

If treatment varies at a group level, standard errors should usually be clustered at the level of treatment assignment or higher. For example, if a policy varies by state, clustering at the individual level is not enough even if the data contain individuals. The treatment shock is common within state, so inference should account for state-level dependence. Serial correlation is especially important in difference-in-differences, where treatment often changes once and outcomes are persistent.

## 13.18 Dynamic treatment effects
Panel data allow treatment effects to vary over time. A treatment may have no immediate effect, a short-run effect, a delayed effect, or an effect that accumulates. Let treatment occur at time $T_i$. A dynamic effect at event time $k$ can be written as:
$\tau_k = \mathbb{E}[Y_{i,T_i+k}(1) - Y_{i,T_i+k}(0)]$ where $k$ indexes time relative to treatment. Examples:
- $k=-2$: two periods before treatment
- $k=-1$: one period before treatment
- $k=0$: treatment period
- $k=1$: one period after treatment
- $k=5$: five periods after treatment

Event-study designs estimate dynamic patterns by including leads and lags of treatment:
$Y_{it} = \alpha_i + \lambda_t + \sum_{k \neq -1} \beta_k \mathbf{1}\{t-T_i=k\} + u_{it}$
The omitted period, often $k=-1$, serves as the reference period. Pre-treatment coefficients, where $k<0$, are used to assess whether treated units were already trending differently before treatment. Post-treatment coefficients, where $k \geq 0$, describe how effects evolve after treatment. Dynamic treatment effects are important because a single average effect may hide the actual policy path. For example:
- job training may reduce earnings during training but increase earnings later
- infrastructure investments may take years to affect productivity
- policing interventions may have immediate effects that fade
- early childhood programs may have long-term effects not visible in the short run
- environmental exposures may affect health with long delays

A rigorous panel study should think carefully about the relevant time horizon.

## 13.19 Anticipation effects
Anticipation occurs when units respond before treatment begins because they expect the treatment. For example:
- firms reduce hiring before a minimum wage increase takes effect
- households buy goods before a tax increase
- students increase effort before scholarship eligibility is determined
- investors move capital before a regulation begins
- local governments alter behavior before a grant formula changes

Anticipation violates the idea that pre-treatment outcomes are untreated potential outcomes. If units change behavior before treatment, then periods labeled pre-treatment may already be affected by the future treatment. In event-study notation, anticipation may appear as nonzero coefficients for leads of treatment:
$\beta_k \neq 0 \quad \text{for some } k<0$ But interpretation is subtle. Nonzero pre-treatment coefficients may reflect anticipation, differential pre-trends, selection into treatment, or noise. Researchers should ask:
- Was the policy announced before implementation?
- Did units know treatment was coming?
- Could they adjust behavior in advance?
- Should the treatment date be the announcement date rather than implementation date?
- Are there institutional reasons to expect anticipation?

When anticipation is likely, the treatment period may need to be redefined. For some policies, the relevant intervention begins when agents learn about the policy, not when the policy formally takes effect.

## 13.20 Attrition in panel data
Attrition occurs when units leave the dataset over time. Attrition can happen because:
- survey respondents stop responding
- people move
- firms exit
- students transfer schools
- patients die or leave a health system
- workers leave formal employment
- administrative records fail to link units across time

Attrition is especially problematic when it is related to treatment and potential outcomes. Suppose a job training program is evaluated using survey data. If unemployed participants are harder to reach after the program, and employed participants are easier to reach, the observed treated group will overrepresent successful participants. Let $R_{it}$ indicate whether unit $i$ is observed at time $t$:
$R_{it}=1 \quad \text{if observed}$
$R_{it}=0 \quad \text{if missing}$ The observed sample consists of units with $R_{it}=1$. If:
$R_{it} \not\perp Y_{it}(d)$ then observed outcomes may not represent the intended population. Attrition is especially serious if treatment affects observation:
$D_i \rightarrow R_{it}$ and observation is related to outcomes:
$Y_{it} \rightarrow R_{it}$ This can create selection bias. Practical diagnostics include:
- comparing attrition rates by treatment status
- comparing baseline characteristics of attriters and non-attriters
- testing whether treatment predicts attrition
- checking whether baseline outcomes predict attrition
- reporting bounds under different assumptions about missing outcomes

Possible remedies include:
- intensive tracking
- administrative data linkage
- inverse probability weighting
- multiple imputation
- Lee bounds
- worst-case and best-case bounds
- sensitivity analysis

No statistical correction is a substitute for understanding why units disappear.

## 13.21 Changing composition
Panel data follow units over time, but the population represented by the data may still change. For example:
- firms enter and exit an industry
- people move into or out of a city
- students enter and leave schools
- neighborhoods gentrify
- hospitals merge or close
- countries enter or exit a sample due to data availability

This creates composition effects. Suppose a city-level policy appears to increase average income. This could reflect income growth among existing residents, or it could reflect low-income residents leaving and high-income residents moving in. If the unit is the city, the effect on average city income is real as a city-level outcome. But it may not mean the original residents benefited. This illustrates the importance of defining the unit and estimand. A place-level estimand might ask:

> What is the effect of the policy on average income among residents of the place after treatment?

An individual-level estimand might ask:

> What is the effect of the policy on the people who lived in the place before treatment?

These are different causal questions. Panel data can sometimes distinguish them if individuals are tracked even after moving. But if data are only at the place level, composition changes may be hard to separate from individual-level effects.

## 13.22 Repeated treatments and treatment histories
Many treatments are not one-time events. They occur repeatedly or accumulate over time. Examples include:
- years of schooling
- repeated job training participation
- annual exposure to pollution
- repeated unemployment spells
- monthly medication use
- repeated policing exposure
- cumulative tax incentives
- repeated school funding changes

In such settings, a unit's outcome may depend on its entire treatment history, not just current treatment. Let treatment history up to time $t$ be:
$\bar{D}_{it} = (D_{i1},D_{i2},\dots,D_{it})$ Then potential outcomes may be written as:
$Y_{it}(\bar{D}_{it})$ This means the outcome at time $t$ depends on the sequence of treatments received up to that time. For example, the health effect of pollution may depend on cumulative exposure:
$CumulativePollution_{it} = \sum_{s=1}^{t} Pollution_{is}$ A model might be:
$Health_{it} = \alpha_i + \lambda_t + \beta CumulativePollution_{it} + u_{it}$
But estimating cumulative effects is difficult because past exposure, current health, residential location, income, and future exposure may all influence one another. Repeated treatment settings require careful attention to:
- timing
- treatment histories
- dynamic selection
- lagged effects
- time-varying confounding
- cumulative exposure
- treatment duration
- treatment intensity

## 13.23 Panel data and difference-in-differences
Difference-in-differences is one of the most common uses of panel or repeated cross-sectional data. The basic two-way fixed effects version is:
$Y_{it} = \alpha_i + \lambda_t + \beta D_{it} + u_{it}$
where $D_{it}$ equals one when unit $i$ is treated at time $t$. This model compares treated units to themselves before and after treatment, while also using untreated or not-yet-treated units to account for common time shocks. The identifying assumption is not merely that fixed effects are included. The key assumption is that untreated potential outcomes would have followed parallel trends:

$$
\mathbb{E}[Y_{it}(0)-Y_{i,t-1}(0) \mid Treated=1]
=
\mathbb{E}[Y_{it}(0)-Y_{i,t-1}(0) \mid Treated=0]
$$

or a suitable generalization in multi-period settings. Panel data make it possible to inspect pre-treatment trends, estimate event studies, and test placebo treatment dates. But these checks do not prove the assumption. They only provide evidence about its plausibility. Panel DiD can fail when:
- treated units had different trends before treatment
- treatment timing is endogenous
- treatment effects are heterogeneous under staggered adoption
- anticipation occurs
- spillovers affect controls
- composition changes
- standard errors ignore serial correlation

Thus, panel data are a tool, not a guarantee.

## 13.24 Panel data and causal graphs
DAGs can help clarify panel data problems, but time must be represented carefully. A simple dynamic DAG might be:
$Y_{i,t-1} \rightarrow D_{it} \rightarrow Y_{it}$ and:
$Y_{i,t-1} \rightarrow Y_{it}$
This says past outcomes affect treatment and also predict current outcomes. If $Y_{i,t-1}$ is pre-treatment relative to $D_{it}$, it may be a confounder. But if past treatment affected $Y_{i,t-1}$, then controlling for $Y_{i,t-1}$ may block part of the effect of treatment history. A more complex DAG might be:
$D_{i,t-1} \rightarrow X_{it} \rightarrow D_{it} \rightarrow Y_{i,t+1}$ and:
$X_{it} \rightarrow Y_{i,t+1}$
Here $X_{it}$ is affected by past treatment, affects current treatment, and affects future outcomes. This is time-varying confounding affected by prior treatment. Ordinary regression adjustment can be biased in such settings. The lesson is:

> In longitudinal data, whether a variable is a confounder, mediator, or collider depends on its timing relative to treatment and outcome.

A rigorous panel study should map the timing of variables explicitly.

## 13.25 Panel data and external validity
Panel data often provide rich evidence for a particular population or institutional setting. But causal estimates from panels still have external validity limits. For example, suppose a study follows workers displaced during one recession and estimates the long-run earnings losses from job displacement. The results may depend on:
- the severity of the recession
- unemployment insurance rules
- worker age
- industry composition
- local labor markets
- retraining opportunities
- macroeconomic recovery
- household wealth
- employer behavior

The effect may not generalize to displacements during a boom, to another country, or to workers in different industries. Similarly, a firm panel study of technology adoption may estimate effects for firms that adopt technology during the observed period. These firms may differ from firms that never adopt or firms that adopted earlier. Panel data can improve internal validity by controlling for stable unobserved heterogeneity, but they do not automatically ensure external validity. Researchers should ask:
- Which units identify the effect?
- Are effects estimated from switchers, adopters, entrants, survivors, or all units?
- Do the identifying units represent the policy-relevant population?
- Does the time period matter?
- Could effects differ under scale-up?
- Are treatment effects dynamic or context-specific?

## 13.26 Practical example: technology adoption and firm productivity
Suppose we want to estimate the effect of adopting a new technology on firm productivity. A cross-sectional regression might be:
$Productivity_i = \alpha + \beta Technology_i + u_i$
If firms using the technology are more productive, $\hat{\beta}$ may be positive. But this does not prove technology caused productivity. More productive firms may be more likely to adopt technology because they have better managers, more capital, better workers, stronger demand, or greater access to finance. A panel model with firm fixed effects is:
$Productivity_{it} = \alpha_i + \lambda_t + \beta Technology_{it} + u_{it}$
This compares a firm to itself before and after adopting technology, controlling for common time shocks. This removes stable firm differences, such as industry, location, founding quality, and long-run management culture. But the estimate may still be biased if technology adoption is timed with time-varying shocks. For example, firms may adopt technology when demand is rising:
$DemandShock_{it} \rightarrow Technology_{it}$ and:
$DemandShock_{it} \rightarrow Productivity_{it}$ Then $Technology_{it}$ remains endogenous. Possible strategies include:
- controlling for observable demand shocks
- using instruments for technology adoption
- exploiting subsidy eligibility rules
- comparing adopters to similar non-adopters with similar pre-trends
- using event studies to inspect productivity before adoption
- studying randomized technology grants if available

The key lesson is that panel data improve the comparison but do not eliminate the need for identification.

## 13.27 Practical example: worker training and wages
Suppose workers are observed annually, and some enroll in training programs. A worker fixed effects model is:
$Wage_{it} = \alpha_i + \lambda_t + \beta Training_{it} + u_{it}$
This compares each worker's wages in periods with training to their own wages in periods without training, controlling for year effects. This removes stable worker characteristics:
- ability
- family background
- baseline motivation
- early schooling
- long-run personality traits

But several problems remain. First, training may occur after a negative wage shock. A worker may enroll because they lost a job or expect wages to fall.

$WageShock_{i,t-1} \rightarrow Training_{it}$
This can make training look less effective than it is. Second, training may be chosen by workers expecting better opportunities. This can make training look more effective than it is. Third, training may temporarily reduce earnings because workers spend time in class rather than working. The short-run effect may differ from the long-run effect. Fourth, workers who leave the dataset after training may differ from those who remain. A better study would examine:
- wage trends before training
- employment status before training
- whether training timing is predictable
- short-run and long-run effects
- attrition after training
- differences by worker type
- whether program access was quasi-random

Again, the panel structure helps but does not by itself identify the causal effect.

## 13.28 Practical example: pollution exposure and health
Suppose we observe counties over time and want to estimate the effect of air pollution on hospitalizations. A basic panel model is:
$Hospitalizations_{ct} = \alpha_c + \lambda_t + \beta Pollution_{ct} + u_{ct}$ where:
- $c$ indexes counties
- $t$ indexes time
- $\alpha_c$ controls for stable county characteristics
- $\lambda_t$ controls for common time shocks

This compares hospitalizations within the same county when pollution is higher versus lower. County fixed effects remove stable differences such as geography, baseline health, long-run income, and hospital infrastructure. Time fixed effects remove common shocks such as national flu seasons or national health policy changes. But pollution may still be endogenous. For example, economic activity may increase pollution and also affect health through employment, income, stress, or population movement:
$EconomicActivity_{ct} \rightarrow Pollution_{ct}$ and:
$EconomicActivity_{ct} \rightarrow Hospitalizations_{ct}$
Weather can also affect both pollution and health. Temperature inversions, wind direction, and wildfire smoke may provide more plausibly exogenous variation in pollution exposure. A stronger design might use:
- wind direction as an instrument
- regulatory changes affecting pollution sources
- plant openings or closures
- high-frequency data with weather controls
- event studies around pollution shocks
- monitors linked to local exposure

The causal question is not whether polluted counties are less healthy. It is whether changes in pollution exposure cause changes in health, holding fixed relevant counterfactual conditions.

**Common mistakes with panel data.**
1. **Assuming fixed effects solve all confounding:** Fixed effects remove time-invariant confounders. They do not remove time-varying confounders. If treatment changes when unobserved conditions change, fixed effects estimates can be biased.
2. **Ignoring treatment timing:** Panel data require careful timing. Researchers must know when treatment is assigned, when it is received, when outcomes respond, and when covariates are measured.
3. **Controlling for post-treatment variables:** Including variables affected by treatment can block part of the effect or introduce collider bias.
4. **Ignoring anticipation:** If units respond before treatment begins, pre-treatment periods may already be affected.
5. **Ignoring attrition:** Panel estimates can be biased if units leave the dataset in ways related to treatment and outcomes.
6. **Ignoring serial correlation:** Panel errors are often correlated within units over time. Standard errors should account for this dependence.
7. **Confusing within-unit and between-unit effects:** A fixed effects estimate is identified by within-unit changes. It may differ from the effect implied by between-unit comparisons.
8. **Ignoring limited variation:** If few units change treatment status, fixed effects estimates may rely on a small and unrepresentative group of switchers.
9. **Treating repeated cross-sections as true panels:** Repeated cross-sections follow populations, not necessarily the same units. Composition changes must be considered.
10. **Ignoring dynamic effects:** A single average treatment coefficient may hide short-run losses, long-run gains, fade-out, delayed effects, or cumulative effects.

**Application checklist.**
When using or evaluating panel data, ask the following questions.
1. **Identify the data structure:** Is the dataset:
    - cross-sectional
    - repeated cross-sectional
    - panel
    - balanced panel
    - unbalanced panel
    - administrative longitudinal data
    - event-based data?
2. **Define the unit and time period:** What is the unit of observation? What is the time interval? Examples: person-year, firm-quarter, school-year, county-month, country-year.
3. **Define treatment timing:** When is treatment assigned? When is it received? Can treatment vary over time? Can units enter and exit treatment? Is treatment absorbing, reversible, repeated, or continuous?
4. **Define outcome timing:** When is the outcome measured relative to treatment? Are effects immediate, delayed, cumulative, or temporary?
5. **Identify within-unit variation:** Which units change treatment status? How much variation is within units versus between units? Are the switchers representative of the population of interest?
6. **Identify time-invariant confounders:** What stable unobserved traits might affect both treatment and outcome? Can fixed effects remove them?
7. **Identify time-varying confounders:** What changing factors might affect both treatment and outcome? Are they observed? Are they pre-treatment or post-treatment?
8. **Assess strict exogeneity:** Could current shocks affect future treatment? Could future treatment be anticipated? Could treatment timing respond to past outcomes?
9. **Examine pre-treatment trends:** Do treated units show unusual trends before treatment? Are outcomes already changing before treatment?
10. **Check attrition and missingness:** Do units leave the panel? Is attrition related to treatment? Is attrition related to baseline outcomes?
11. **Account for serial correlation:** Are errors correlated over time within units? At what level should standard errors be clustered?
12. **Interpret the estimand:** Is the estimate a within-unit effect? Does it apply to all units or only switchers? Is it short-run, long-run, cumulative, or dynamic? Does it generalize beyond the observed sample and period?

## 13.29 Summary
Cross-sectional data observe many units at one point in time. They are useful for describing differences across units, but causal interpretation is difficult because units differ in many observed and unobserved ways. Repeated cross-sectional data observe different samples from a population over time. They can support policy evaluation and difference-in-differences designs, but researchers must consider composition changes. Panel data observe the same units repeatedly over time. They allow researchers to study within-unit change, control for time-invariant unobserved heterogeneity, examine dynamics, and construct stronger counterfactual comparisons. A basic panel model is:
$Y_{it} = \alpha + \beta X_{it} + u_{it}$ A unit fixed effects model is:
$Y_{it} = \alpha_i + \beta X_{it} + u_{it}$ A two-way fixed effects model is:
$Y_{it} = \alpha_i + \lambda_t + \beta X_{it} + u_{it}$ Panel data are powerful because they can remove time-invariant confounding and reveal dynamic patterns. But they do not automatically solve causal inference. Major threats include:
- time-varying confounding
- endogenous treatment timing
- reverse causality
- anticipation
- attrition
- changing composition
- serial correlation
- measurement error
- bad controls
- limited within-unit variation
- dynamic treatment histories

The central lesson is:

> Panel data improve the set of possible comparisons, but causal credibility still depends on the research design and identifying assumptions. Observing the same units over time helps construct counterfactuals, but it does not eliminate the need to explain why the observed within-unit variation is plausibly exogenous.

# 14. Fixed Effects and Random Effects
## 14.1 Why unit-level heterogeneity matters
Empirical researchers often study units that differ from one another in persistent ways. Workers differ in ability, motivation, health, family background, risk tolerance, and social networks. Firms differ in management quality, productivity, culture, technology, market power, and access to capital. Schools differ in leadership, teacher quality, peer composition, neighborhood context, and resources. Regions differ in climate, infrastructure, institutions, industry mix, political culture, and local labor markets. Many of these differences are difficult or impossible to measure directly. Yet they may affect both the explanatory variable of interest and the outcome. For example, suppose we want to estimate the effect of technology adoption on firm productivity. More productive firms may be more likely to adopt new technologies. If we compare firms that adopted the technology to firms that did not, the adopters may have been better firms even before adoption. A simple cross-sectional regression might be:
$Productivity_i = \alpha + \beta Technology_i + u_i$ The problem is that $u_i$ may contain unobserved firm quality. If high-quality firms are more likely to adopt technology, then:
$\operatorname{Cov}(Technology_i,u_i) \neq 0$
In that case, the coefficient $\beta$ does not isolate the causal effect of technology. It combines the effect of technology with pre-existing differences between firms. Panel data help because they observe the same units over time. Instead of comparing different firms to each other, we can compare the same firm before and after technology adoption. Fixed effects and random effects are two major ways to model persistent differences across units. The central problem is unobserved heterogeneity: stable differences across units that affect the outcome and may be related to treatment or regressors.

---

## 14.2 The basic panel data model
A common starting point is:
$Y_{it} = \alpha + \beta X_{it} + a_i + u_{it}$ where:
- $i$ indexes units, such as workers, firms, schools, cities, or countries
- $t$ indexes time
- $Y_{it}$ is the outcome for unit $i$ at time $t$
- $X_{it}$ is the explanatory variable or treatment
- $a_i$ is an unobserved unit-specific component
- $u_{it}$ is an idiosyncratic time-varying error term

The term $a_i$ represents stable unobserved characteristics of unit $i$. For a worker, $a_i$ might include stable ability, early-life family background, personality, or long-run health. For a firm, $a_i$ might include management quality, organizational culture, location advantages, or permanent productivity differences. For a school, $a_i$ might include neighborhood environment, school leadership, or long-standing institutional quality. The key question is whether $a_i$ is correlated with $X_{it}$. If:
$\operatorname{Cov}(a_i,X_{it}) = 0$ then the unobserved unit effect is unrelated to the explanatory variable. In that case, random effects may be appropriate. If:
$\operatorname{Cov}(a_i,X_{it}) \neq 0$
then the unobserved unit effect is related to the explanatory variable. In that case, fixed effects are usually safer for causal inference. This distinction is the core difference between fixed effects and random effects.

---

## 14.3 Fixed effects: the basic idea
Fixed effects allow each unit to have its own intercept. The fixed effects model is:
$Y_{it} = \alpha_i + \beta X_{it} + u_{it}$ where $\alpha_i$ is a separate intercept for each unit. The term $\alpha_i$ absorbs all time-invariant characteristics of unit $i$, whether observed or unobserved. The intuition is:

> Compare each unit to itself over time.

Instead of asking whether firms that use technology are more productive than firms that do not, fixed effects ask:

> When the same firm changes its technology use, does its productivity change?

Instead of asking whether workers with more training earn more than workers with less training, fixed effects ask:

> When the same worker receives training, do their earnings change?

Instead of asking whether states with stricter environmental regulation have different pollution outcomes than other states, fixed effects ask:

> When the same state changes regulation, do pollution outcomes change?

This is powerful because many confounders are stable over time. If they are stable, fixed effects remove them.

---

## 14.4 What fixed effects remove
Fixed effects remove time-invariant unit-level confounders. Suppose the true model is:
$Y_{it} = \alpha + \beta X_{it} + \gamma A_i + u_{it}$
where $A_i$ is an unobserved characteristic that does not change over time. If $A_i$ is correlated with $X_{it}$, then omitting $A_i$ creates bias in pooled OLS. But if $A_i$ is constant over time, fixed effects absorb it into $\alpha_i$:
$Y_{it} = \alpha_i + \beta X_{it} + u_{it}$ This means the researcher does not need to observe $A_i$ directly. Examples of time-invariant confounders that fixed effects may remove include:
- innate ability
- childhood family background
- birth cohort characteristics if cohort is fixed within person
- permanent firm culture
- long-run school quality
- geography
- climate
- historical institutions
- stable neighborhood characteristics
- permanent industry classification

For example, suppose more able workers are more likely to seek training and also earn higher wages. A cross-sectional regression may overstate the effect of training. Worker fixed effects remove any stable component of ability, because each worker is compared to themselves. The fixed effects model uses within-unit variation, not between-unit variation.

---

## 14.5 The within transformation
Fixed effects can be understood through the within transformation. Start with:
$Y_{it} = \alpha_i + \beta X_{it} + u_{it}$ Take the average over time for each unit:
$\bar{Y}_i = \alpha_i + \beta \bar{X}_i + \bar{u}_i$ where:
$\bar{Y}_i = \frac{1}{T_i}\sum_t Y_{it}$ and:
$\bar{X}_i = \frac{1}{T_i}\sum_t X_{it}$ Subtract the unit average from the original equation:
$Y_{it} - \bar{Y}_i = \beta (X_{it}-\bar{X}_i) + (u_{it}-\bar{u}_i)$ The fixed effect $\alpha_i$ disappears because it is constant over time:
$\alpha_i - \alpha_i = 0$
This transformed equation estimates $\beta$ using deviations from each unit's own average. That is why fixed effects are also called within estimators. The coefficient $\beta$ is identified only by changes in $X_{it}$ within units over time. Units whose $X_{it}$ never changes do not contribute to the estimation of $\beta$. For example, if the treatment is college completion and some people are always college graduates while others are never college graduates, person fixed effects cannot estimate the effect of college completion unless some people change status over time in a meaningful way. Fixed effects require within-unit variation in the treatment.

---

## 14.6 Fixed effects with two time periods: first differences
When there are only two periods, fixed effects are closely related to first differencing. Suppose:
$Y_{i1} = \alpha_i + \beta X_{i1} + u_{i1}$ and:
$Y_{i2} = \alpha_i + \beta X_{i2} + u_{i2}$ Subtract period 1 from period 2:
$Y_{i2}-Y_{i1} = \beta(X_{i2}-X_{i1}) + (u_{i2}-u_{i1})$ The fixed effect $\alpha_i$ drops out. Define:
$\Delta Y_i = Y_{i2}-Y_{i1}$ and:
$\Delta X_i = X_{i2}-X_{i1}$ Then:
$\Delta Y_i = \beta \Delta X_i + \Delta u_i$ This shows that fixed effects with two periods estimate whether changes in $X$ are associated with changes in $Y$ within the same unit. The causal interpretation still requires an assumption:
$\mathbb{E}[\Delta u_i \mid \Delta X_i]=0$
In words: changes in the explanatory variable must be unrelated to changes in unobserved determinants of the outcome. Fixed effects remove stable confounders, but they do not remove time-varying confounders.

---

## 14.7 What fixed effects do not remove
Fixed effects are powerful, but they are not magic. They do not solve all endogeneity problems. Fixed effects do not remove confounders that change over time within units. Suppose firms adopt new technology when demand for their products is rising. Demand shocks may increase productivity and also cause technology adoption. Firm fixed effects remove stable firm quality, but they do not remove the time-varying demand shock. The model is:
$Productivity_{it} = \alpha_i + \beta Technology_{it} + DemandShock_{it} + u_{it}$ If $DemandShock_{it}$ is omitted and correlated with $Technology_{it}$, then:
$\operatorname{Cov}(Technology_{it},u_{it}) \neq 0$ Fixed effects do not solve the problem. Other examples of time-varying confounding include:
- workers seek training after a negative wage shock
- cities increase policing after a rise in crime
- schools adopt reforms after test scores fall
- firms change prices when demand shifts
- governments expand welfare programs during recessions
- hospitals adopt new protocols after patient composition changes

Fixed effects also do not automatically solve:
- reverse causality
- simultaneity
- measurement error
- dynamic feedback
- anticipation effects
- spillovers
- attrition
- time-varying selection
- post-treatment control bias

The correct interpretation is:

> Fixed effects remove time-invariant unit-level confounding. They do not remove time-varying confounding.

---

## 14.8 Two-way fixed effects
A common panel data model includes both unit fixed effects and time fixed effects:
$Y_{it} = \alpha_i + \lambda_t + \beta X_{it} + u_{it}$ where:
- $\alpha_i$ are unit fixed effects
- $\lambda_t$ are time fixed effects
- $X_{it}$ is the treatment or explanatory variable
- $u_{it}$ is the remaining error term

Unit fixed effects control for stable differences across units. Time fixed effects control for shocks common to all units at a given time. For example, in a state-year panel:
- state fixed effects control for stable differences across states
- year fixed effects control for national shocks affecting all states in a given year

The model becomes:
$Y_{st} = \alpha_s + \lambda_t + \beta Policy_{st} + u_{st}$ This asks:

> When a state changes policy relative to its own average, and relative to national year-specific shocks, how does its outcome change?

Two-way fixed effects are widely used in policy evaluation. However, the causal interpretation still requires that policy changes are not correlated with unobserved state-specific time-varying shocks. The identifying assumption is not simply that fixed effects were included. The key assumption is closer to:
$\mathbb{E}[u_{it} \mid X_{i1}, X_{i2}, \dots, X_{iT}, \alpha_i, \lambda_t] = 0$
In words: after accounting for unit and time fixed effects, the timing and intensity of treatment must be as-good-as-random with respect to remaining unobserved shocks.

---

## 14.9 Fixed effects and difference-in-differences
Difference-in-differences is closely related to fixed effects. A standard DiD regression is:
$Y_{it} = \alpha_i + \lambda_t + \beta D_{it} + u_{it}$ where $D_{it}$ equals 1 when unit $i$ is treated at time $t$. This is a two-way fixed effects model. The causal interpretation depends on a parallel trends assumption:

> In the absence of treatment, treated and comparison units would have followed similar trends.

Fixed effects remove level differences across units. They do not prove parallel trends. For example, suppose treated states were already on a different trajectory before adopting a policy. State fixed effects remove permanent differences in state levels, but they do not remove different trends. A fixed effects model may therefore be written correctly and still fail as a causal design. This is an important lesson:

> Fixed effects are a statistical adjustment. Difference-in-differences is a research design. The design requires a credible counterfactual trend, not merely fixed effects in a regression.

---

## 14.10 Unit-specific trends
Sometimes researchers add unit-specific trends:
$Y_{it} = \alpha_i + \lambda_t + \theta_i t + \beta X_{it} + u_{it}$
where $\theta_i t$ allows each unit to have its own linear trend. This can help when units have different underlying trajectories. For example, if some states have steadily rising employment and others have steadily falling employment, state-specific trends may absorb those differences. But unit-specific trends should be used carefully. They can reduce bias if untreated potential outcomes truly follow different smooth trends. But they can also absorb part of the treatment effect if the treatment effect grows gradually over time. For example, suppose a policy has a slowly increasing effect. A unit-specific trend may mistakenly treat part of that effect as a continuation of the prior trend. The decision to include unit-specific trends should be motivated by the causal setting, pre-treatment data, and robustness checks, not by a mechanical desire to add more controls.

---

## 14.11 Time-varying controls
Fixed effects models often include time-varying controls:
$Y_{it} = \alpha_i + \lambda_t + \beta X_{it} + \gamma W_{it} + u_{it}$
where $W_{it}$ is a vector of observed variables that change over time. Time-varying controls can help if they are genuine pre-treatment confounders. For example, in a study of training and wages, local unemployment rates may affect both program participation and wages. If local unemployment is measured before treatment, controlling for it may help. But time-varying controls can be dangerous if they are affected by treatment. Suppose:
$X_{it} \rightarrow W_{it} \rightarrow Y_{it}$
Then $W_{it}$ is a mediator. Controlling for it blocks part of the treatment effect. Or suppose $W_{it}$ is a collider affected by treatment and another cause of the outcome. Conditioning on it can create bias. The rule is the same as in DAG analysis:

> Do not control for a variable just because it is available. Control variables must be justified by the causal structure and timing.

---

## 14.12 Random effects: the basic idea
Random effects also model unit-level heterogeneity, but they do so differently. The random effects model is:
$Y_{it} = \alpha + \beta X_{it} + a_i + u_{it}$ where:
$a_i \sim \text{some distribution with mean } 0$ The unit-specific effect $a_i$ is treated as a random variable drawn from a population distribution. The key assumption is:
$\operatorname{Cov}(a_i,X_{it}) = 0 \quad \text{for all } t$ In words:

> The unobserved unit-specific effect is uncorrelated with the explanatory variables in every period.

If this assumption holds, random effects can be more efficient than fixed effects because it uses both within-unit and between-unit variation. If the assumption fails, random effects are biased for causal interpretation. For example, if high-ability workers obtain more training and also earn higher wages, then worker ability is part of $a_i$ and is correlated with training. Random effects would generally be biased. Fixed effects are often preferred for causal inference because they allow $a_i$ to be correlated with $X_{it}$.

---

## 14.13 Fixed effects versus random effects
The core contrast is:
- fixed effects allow arbitrary correlation between $a_i$ and $X_{it}$
- random effects require $a_i$ to be uncorrelated with $X_{it}$

In fixed effects, the unit effect is treated as a separate parameter for each unit:
$Y_{it} = \alpha_i + \beta X_{it} + u_{it}$ In random effects, the unit effect is treated as part of the error structure:
$Y_{it} = \alpha + \beta X_{it} + a_i + u_{it}$
The difference is not merely technical. It changes what variation is used. Fixed effects estimate $\beta$ using within-unit variation. Random effects use both within-unit and between-unit variation. Between-unit variation can be informative for prediction. But for causal inference, between-unit variation may be contaminated by unobserved differences across units. For example, suppose better-managed firms are both more productive and more likely to adopt technology. Random effects may attribute some of the productivity advantage of better-managed firms to technology. Fixed effects remove stable management quality by comparing firms to themselves.

---

## 14.14 The random effects assumption
The random effects assumption can be written as:
$\mathbb{E}[a_i \mid X_{i1},X_{i2},\dots,X_{iT}] = 0$ This says the unobserved unit effect is mean independent of the entire history of regressors. This is a strong assumption in many economic settings. It may be plausible when:
- units are randomly sampled from a population
- regressors are randomly assigned or plausibly exogenous
- unobserved unit traits are not related to the regressors
- the goal is prediction rather than causal interpretation
- the unit effects represent random variation in a hierarchical structure

It is less plausible when:
- individuals choose treatment based on stable traits
- firms adopt policies based on permanent productivity
- states adopt laws based on political culture
- schools implement reforms based on long-standing quality differences
- neighborhoods receive interventions based on persistent disadvantage

In applied causal work, this assumption must be defended substantively. It should not be accepted because software labels a model as random effects.

---

## 14.15 Random effects and partial pooling
Random effects are especially important in hierarchical or multilevel modeling. Suppose students are nested in schools:
$Score_{ij} = \alpha + \beta X_{ij} + a_j + u_{ij}$ where:
- $i$ indexes students
- $j$ indexes schools
- $a_j$ is a school-level random effect

The model assumes school effects are drawn from a common distribution:
$a_j \sim N(0,\sigma_a^2)$
This allows partial pooling. Partial pooling means estimates for small schools are pulled toward the overall mean more than estimates for large schools. This can improve prediction and stabilize noisy estimates. For example, if a small school has only five observed students, its raw average test score may be very noisy. A random effects model uses information from the broader distribution of schools to produce a more stable estimate of that school's effect. This is useful for prediction, ranking, forecasting, and modeling hierarchical structure. But partial pooling is not automatically a causal solution. If school-level unobserved quality is correlated with treatment, causal interpretation still requires assumptions.

---

## 14.16 The Hausman test intuition
The Hausman test is often used to compare fixed effects and random effects. The intuition is simple. If the random effects assumption is true, both fixed effects and random effects are consistent, but random effects are more efficient. If the random effects assumption is false, fixed effects may remain consistent, while random effects are inconsistent. So the test compares the fixed effects estimate and the random effects estimate. If they differ substantially, that suggests the random effects assumption may be violated. Formally, the null hypothesis is that random effects are consistent:
$H_0: \operatorname{Cov}(a_i,X_{it}) = 0$ The alternative is:
$H_1: \operatorname{Cov}(a_i,X_{it}) \neq 0$
A rejection suggests that random effects may be inappropriate. However, the Hausman test should not replace substantive reasoning. It can be sensitive to specification, heteroskedasticity, clustering, and finite-sample issues. A failure to reject does not prove that random effects are causally valid. The most important question remains:

> Is it credible that unobserved unit traits are unrelated to the regressors?

---

## 14.17 Fixed effects and variables that do not change over time
A limitation of fixed effects is that they cannot estimate the effects of variables that are constant within units over time. Suppose we estimate:
$Y_{it} = \alpha_i + \beta X_{it} + \gamma Z_i + u_{it}$
where $Z_i$ does not vary over time. Because $Z_i$ is perfectly collinear with the unit fixed effect $\alpha_i$, its coefficient $\gamma$ cannot be estimated in a standard fixed effects model. Examples of time-invariant variables include:
- birth sex in many datasets
- race or ethnicity in many contexts
- birthplace
- childhood family background
- historical geography
- baseline institutional features
- permanent group membership

Fixed effects absorb these variables. This is not a flaw if those variables are confounders that need to be controlled for. But it means fixed effects cannot estimate their coefficients directly. If the research question concerns a time-invariant variable, fixed effects may not be the right estimator unless the design uses interactions, cohort variation, policy changes, or other sources of within-unit change.

---

## 14.18 Fixed effects and measurement error
Fixed effects can worsen measurement error problems. Suppose:
$X_{it}^{obs} = X_{it}^{true} + e_{it}$ where $e_{it}$ is measurement error. Fixed effects rely on within-unit changes:
$X_{it}^{obs} - \bar{X}_i$
If the true variable changes little over time but measurement error varies from period to period, then a large share of the within-unit variation may be noise. This can attenuate estimates toward zero. For example, annual income is noisy. If we use worker fixed effects to estimate the effect of income on consumption, year-to-year measurement error in income may be large relative to true persistent changes. The fixed effects estimate may be severely attenuated. This is one reason fixed effects estimates can differ from cross-sectional estimates. A smaller fixed effects estimate may mean cross-sectional estimates were confounded. But it may also mean the within estimator suffers from measurement error, limited variation, or different causal variation. Interpretation requires care.

---

## 14.19 Fixed effects and dynamic outcomes
Many outcomes are persistent over time. For example:
- wages depend on past wages
- health depends on past health
- test scores depend on past test scores
- productivity depends on past productivity
- crime depends on past crime
- income depends on past income

A dynamic model might be:
$Y_{it} = \rho Y_{i,t-1} + \beta X_{it} + \alpha_i + u_{it}$
Including lagged outcomes in fixed effects models can create complications, especially when the number of time periods is small. This is known as dynamic panel bias or Nickell bias. The lagged outcome $Y_{i,t-1}$ is mechanically related to the transformed error term after demeaning. Dynamic panel methods, such as Arellano-Bond estimators, are sometimes used in these settings. But they require additional assumptions and instruments. The key lesson is that fixed effects do not automatically solve dynamic causal problems. When outcomes are persistent and treatment responds to past outcomes, careful modeling of timing and feedback is necessary.

---

## 14.20 Fixed effects and staggered treatment timing
Many policies are adopted at different times by different units. For example, states may adopt minimum wage changes, tax reforms, environmental laws, or healthcare expansions in different years. A traditional two-way fixed effects model is:
$Y_{it} = \alpha_i + \lambda_t + \beta D_{it} + u_{it}$
where $D_{it}$ equals 1 after unit $i$ adopts treatment. This model can be problematic when treatment effects differ across units or over time. Already-treated units may implicitly serve as controls for later-treated units. If treatment effects evolve dynamically, this can create misleading weighted averages. Modern difference-in-differences methods address this by comparing treated units to appropriate not-yet-treated or never-treated units and estimating cohort-time-specific effects. This issue is not caused by fixed effects alone, but it often appears in two-way fixed effects policy regressions. The lesson is:

> In staggered adoption settings, a two-way fixed effects coefficient may not equal a simple average treatment effect unless treatment effects and timing assumptions are appropriate.

---

## 14.21 Example: worker training and wages
Suppose we want to estimate the effect of job training on wages using worker panel data. A pooled regression is:
$Wage_{it} = \alpha + \beta Training_{it} + u_{it}$
This compares trained workers to untrained workers. The problem is that workers who receive training may differ from those who do not. They may have different ability, motivation, education, family support, career goals, or employer quality. A worker fixed effects model is:
$Wage_{it} = \alpha_i + \beta Training_{it} + u_{it}$
This compares each worker's wages in periods with training to that same worker's wages in periods without training. This removes stable worker traits such as permanent ability or background. But problems remain. Workers may receive training after a promotion, after a wage shock, after switching employers, or when their industry is changing. If those time-varying factors also affect wages, then fixed effects do not identify the causal effect of training. A more credible design might use:
- random assignment to training
- an eligibility cutoff
- employer-level policy changes
- variation in training availability
- difference-in-differences with pre-trend checks
- an instrument for training participation

Fixed effects help, but the causal design still matters.

---

## 14.22 Example: firm technology adoption and productivity
Suppose we study whether adopting a new technology raises firm productivity. A cross-sectional model is:
$Productivity_{it} = \alpha + \beta Technology_{it} + u_{it}$ This may be biased because better-managed firms adopt technology earlier and are also more productive. A firm fixed effects model is:
$Productivity_{it} = \alpha_i + \lambda_t + \beta Technology_{it} + u_{it}$
This controls for stable firm quality and common year shocks. The estimate comes from changes in technology adoption within firms. However, if firms adopt technology when demand is rising, or when they hire new managers, or after receiving investment, then adoption is still endogenous. A credible study might examine whether productivity changes after adoption relative to pre-adoption trends and relative to similar non-adopting firms. It might also use an instrument, such as variation in broadband rollout or technology subsidies, if the assumptions are credible. Again, fixed effects address stable heterogeneity but not all selection into adoption.

---

## 14.23 Example: state policies and outcomes
Suppose we estimate the effect of a state policy on employment. A common model is:
$Employment_{st} = \alpha_s + \lambda_t + \beta Policy_{st} + u_{st}$ where:
- $\alpha_s$ are state fixed effects
- $\lambda_t$ are year fixed effects
- $Policy_{st}$ indicates whether the policy is in place

State fixed effects control for stable differences across states, such as geography, historical institutions, long-run industry mix, and political culture. Year fixed effects control for national shocks, such as recessions, federal policy changes, and national inflation. The coefficient $\beta$ is identified by changes in policy within states over time, relative to other states in the same years. The key causal question is:

> Would the treated states have followed the same employment trend as comparison states if they had not adopted the policy?

If yes, the design may be credible. If no, the fixed effects regression may be biased. For example, states may adopt the policy because employment is already changing. If adoption responds to state-specific labor market shocks, then:

$\operatorname{Cov}(Policy_{st},u_{st}) \neq 0$ Fixed effects do not solve that problem.


**Common mistakes.**
1. **Thinking fixed effects automatically make estimates causal:** Fixed effects remove time-invariant confounders. They do not remove time-varying confounders, reverse causality, simultaneity, measurement error, anticipation, or spillovers. A fixed effects regression is not automatically a causal design.
2. **Ignoring the source of variation:** Fixed effects estimates are based on within-unit changes. Researchers must ask what causes those changes. If changes in treatment are caused by shocks that also affect the outcome, the estimate may still be biased.
3. **Controlling for post-treatment variables:** Adding time-varying controls can create bias if those controls are affected by treatment. Control variables must be chosen based on causal timing and structure.
4. **Using random effects when the key assumption is implausible:** Random effects require unobserved unit traits to be uncorrelated with the regressors. This is often implausible in observational causal research.
5. **Forgetting that fixed effects remove time-invariant variables:** Fixed effects cannot estimate coefficients on variables that do not change within units over time.
6. **Treating two-way fixed effects as always valid DiD:** Two-way fixed effects models can be problematic in staggered adoption settings with heterogeneous treatment effects.
7. **Ignoring standard errors:** Panel data often have serial correlation within units. Standard errors should often be clustered at the unit level or at the level of treatment assignment.

---

**Application checklist.**
When using fixed effects or random effects, ask the following questions.
1. **What is the unit of analysis?** Is the unit a person, firm, school, city, state, country, market, or other entity?
2. **What unobserved unit-level traits might matter?** List stable characteristics that may affect the outcome and be correlated with treatment. Examples: ability, management quality, geography, institutions, culture, baseline health, permanent productivity.
3. **Are those traits time-invariant?** Fixed effects remove only traits that are stable over time within units.
4. **Is there enough within-unit variation?** Fixed effects require units to change treatment or explanatory variables over time. If $X_{it}$ barely changes, the estimate may be imprecise or driven by noise.
5. **What causes within-unit changes in treatment?** This is the key identification question. Are changes plausibly exogenous, or do they respond to time-varying shocks?
6. **Are time fixed effects needed?** Are there shocks common to all units in each period? If yes, include time fixed effects.
7. **Are time-varying controls appropriate?** Are they pre-treatment confounders, or are they affected by treatment? Avoid bad controls.
8. **Is random effects plausible?** Is it credible that the unobserved unit effect is uncorrelated with regressors? If not, fixed effects are usually safer for causal inference.
9. **Are standard errors appropriate?** Panel errors are often correlated within units over time. Consider clustering at the unit level or treatment-assignment level.
10. **What is the estimand?** Does the estimate represent a within-unit effect, a policy effect, a local effect, a dynamic effect, or a weighted average of heterogeneous effects?
11. **What are the remaining threats?** Consider time-varying confounding, anticipation, spillovers, measurement error, attrition, and dynamic feedback.


## 14.24 Summary

Fixed effects and random effects are tools for modeling unit-level heterogeneity in panel and hierarchical data. Fixed effects allow each unit to have its own intercept:
$Y_{it} = \alpha_i + \beta X_{it} + u_{it}$ They estimate effects using within-unit variation over time. They remove time-invariant unobserved confounders, even if those confounders are correlated with treatment. The central intuition is:

> Compare each unit to itself.

Random effects model unit-level heterogeneity as a random component:
$Y_{it} = \alpha + \beta X_{it} + a_i + u_{it}$ They require:
$\operatorname{Cov}(a_i,X_{it})=0$
If this assumption holds, random effects can be efficient and useful, especially for hierarchical modeling and prediction. If it fails, random effects are generally biased for causal interpretation. Fixed effects are often safer for causal inference, but they are not automatic solutions. They do not remove time-varying confounding, reverse causality, simultaneity, measurement error, anticipation, spillovers, or dynamic feedback. The most important question is not whether a regression includes fixed effects. The most important question is:

> What within-unit variation identifies the effect, and why is that variation plausibly exogenous?

Fixed effects are a way to control for stable unobserved heterogeneity. Causal identification still requires a credible research design.

# 15. Internal Validity, External Validity, and the Broader Validity Framework

## 15.1 Why validity matters
Validity concerns whether a study supports the conclusions drawn from it. An empirical estimate is not useful simply because it is statistically significant, precisely estimated, or produced by a sophisticated method. The estimate must be valid for the question being asked. In empirical economics and causal inference, validity usually has two central dimensions:
1. **Internal validity**: whether the estimated effect is credible for the study sample and setting.
2. **External validity**: whether the estimated effect generalizes beyond the study sample and setting.
A study can have strong internal validity but weak external validity. For example, a randomized controlled trial may credibly estimate the effect of a tutoring program in one school district, but the result may not generalize to another country, another age group, or a scaled national program. A study can also have broad external relevance but weak internal validity. For example, a national observational dataset may cover many people and places, but if treatment is highly confounded, the estimated relationship may not be causal. The key distinction is:

> Internal validity asks whether the study estimates the causal effect correctly in the studied context.

> External validity asks whether that causal effect applies elsewhere.

Both matter. A study with weak internal validity does not provide a credible causal estimate. A study with weak external validity may provide a credible estimate, but only for a narrow context. Validity is not all-or-nothing. It is an argument. Researchers must explain what their study identifies, under what assumptions, for whom, and with what limitations.

## 15.2 Internal validity
Internal validity asks:

> Does the research design credibly identify the causal effect in the study sample and setting?

A study has high internal validity if the estimated effect can reasonably be interpreted as causal for the units, treatment, outcome, and time period studied. Suppose a researcher estimates the effect of a job training program on earnings. Internal validity asks whether the estimated earnings difference reflects the causal effect of training rather than selection bias, omitted variables, reverse causality, attrition, measurement error, or other threats. In potential outcomes terms, suppose the target estimand is the average treatment effect on the treated:
$ATT = \mathbb{E}[Y_i(1)-Y_i(0) \mid D_i=1].$ For treated units, we observe $Y_i(1)$ but not $Y_i(0)$. Internal validity depends on whether the study has a credible way to estimate:
$\mathbb{E}[Y_i(0) \mid D_i=1].$
That is, what would treated units have experienced without treatment? Every causal design proposes an answer to this missing-counterfactual problem. An RCT says: use the randomly assigned control group. Difference-in-differences says: use the control group's change over time to infer the treated group's counterfactual trend. Regression discontinuity says: use units just on the other side of the cutoff. Instrumental variables says: use treatment variation induced by an instrument that is unrelated to potential outcomes except through treatment. Fixed effects says: compare each unit to itself over time, removing stable unobserved heterogeneity. Internal validity asks whether that proposed counterfactual is credible.

## 15.3 Common threats to internal validity
Internal validity can fail for many reasons. The most important threats are the same threats that motivate causal research design.
- **Confounding.**
Confounding occurs when a variable affects both treatment and outcome. A confounder $C$ creates a backdoor path:
$D \leftarrow C \rightarrow Y.$
If this path is not blocked, the estimated relationship between treatment $D$ and outcome $Y$ mixes the causal effect of $D$ with the non-causal association induced by $C$. Example: motivated workers may be more likely to participate in job training and more likely to earn higher wages even without training. Motivation confounds the relationship between training and wages.
- **Selection bias.**
Selection bias occurs when treatment, participation, observation, or sample inclusion is systematically related to potential outcomes. For example, if healthier patients are more likely to enroll in a voluntary health program, comparing participants to nonparticipants may overstate the program's effect. Selection bias is especially common when treatment is voluntary, when samples are non-representative, or when outcomes are observed only for selected units.
- **Omitted variable bias.**
Omitted variable bias occurs when a relevant variable is excluded from the model and is correlated with an included explanatory variable. Suppose the true model is:
$Y_i = \alpha + \beta D_i + \gamma C_i + u_i,$ but the researcher estimates:
$Y_i = \alpha + \tilde{\beta}D_i + e_i.$ If $C_i$ affects $Y_i$ and is correlated with $D_i$, then $D_i$ is correlated with the error term, and $\tilde{\beta}$ is biased.
- **Reverse causality.**
Reverse causality occurs when the outcome affects the treatment or explanatory variable. Example: cities with more crime may hire more police. A regression of crime on police may show a positive relationship, not because police cause crime, but because crime causes police deployment. The causal arrow may be:
$Y \rightarrow D,$ rather than:
$D \rightarrow Y.$
- **Simultaneity.**
Simultaneity occurs when treatment and outcome are jointly determined. In markets, price and quantity are determined together by supply and demand. A regression of quantity on price may not identify either demand or supply unless the researcher isolates variation from one side of the market.
- **Measurement error.**
Measurement error occurs when treatment, outcome, or controls are measured with error. If the outcome is measured poorly, estimates may be noisy or biased. If the treatment variable is measured with error, coefficients can be attenuated or distorted. If key controls are measured poorly, residual confounding may remain. For example, if education quality is measured only by years of schooling, then studies of schooling may miss important differences in school resources, teachers, peers, and curriculum.
- **Attrition.**
Attrition occurs when units leave the sample over time. Attrition threatens internal validity if dropout is related to treatment and potential outcomes. Example: a job training program tracks participants for two years, but low-earning participants are more likely to disappear from the survey. The remaining sample may overstate program success. Attrition is especially important in experiments, panel studies, long-term follow-ups, and program evaluations.
- **Noncompliance.**
Noncompliance occurs when assigned treatment differs from actual treatment received. In an RCT, some people assigned to treatment may not take it up, and some assigned to control may access treatment elsewhere. This creates a distinction between:
- the effect of being assigned treatment
- the effect of actually receiving treatment

The intent-to-treat effect is often internally valid under random assignment, but it may not equal the effect of actual treatment receipt.
- **Spillovers and interference.**
Spillovers occur when treatment assigned to one unit affects outcomes for other units. In potential outcomes language, this violates no interference. Instead of writing:
$Y_i(D_i),$ we may need:
$Y_i(D_1,D_2,\dots,D_n).$ Examples:
- job training may help participants compete for jobs, reducing opportunities for nonparticipants
- vaccination protects untreated people through herd immunity
- policing in one neighborhood may displace crime to another
- tutoring one student may affect classmates through peer effects

If spillovers contaminate the control group, the estimated treatment effect may be biased.
- **Anticipation effects.**
Anticipation occurs when units change behavior before treatment begins because they expect treatment. For example, firms may adjust employment before a minimum wage increase takes effect. Households may change spending before a tax change. Students may change effort before scholarship rules are applied. Anticipation can make pre-treatment periods partly treated, undermining designs that rely on clean before-after comparisons.
- **Regression to the mean.**
Regression to the mean occurs when units selected because of extreme outcomes tend to move closer to average outcomes over time, even without treatment. Example: schools with unusually low test scores receive an intervention. If their scores improve later, the improvement may partly reflect natural reversion rather than the intervention. This is a major threat in before-after evaluations of programs targeted to extreme cases.
- **History and simultaneous shocks.**
A study may attribute a change in outcomes to treatment when another event occurred at the same time. Example: a state increases the minimum wage during a local economic downturn. If employment falls, the decline may be due to the downturn, the policy, or both. Difference-in-differences attempts to handle common shocks using a control group, but it can fail if treated and control groups are exposed to different shocks.
- **Maturation and natural trends.**
Outcomes may change over time for reasons unrelated to treatment. Children learn as they age. Patients recover naturally. Firms adapt to market conditions. Workers gain experience. Neighborhoods change. Before-after comparisons can confuse natural progression with treatment effects.
- **Hawthorne effects and experimenter effects.**
A Hawthorne effect occurs when subjects change behavior because they know they are being studied. Experimenter effects occur when researchers, administrators, or implementers influence outcomes through expectations or behavior. These threats can matter in field experiments, lab experiments, education interventions, workplace studies, and medical trials.

## 15.4 Internal validity by research design
Different research designs face different internal validity threats.
- **Randomized controlled trials.**
RCTs often have strong internal validity because random assignment makes treatment independent of potential outcomes in expectation:
$D_i \perp (Y_i(1),Y_i(0)).$ Under proper randomization, the control group estimates the treated group's missing counterfactual. However, RCTs can still fail internally because of:
    - failed randomization
    - noncompliance
    - attrition
    - spillovers
    - treatment contamination
    - bad outcome measurement
    - small samples
    - implementation failure
    - differential survey response
    - manipulation of assignment
    - multiple testing

Randomization solves confounding at assignment, but it does not automatically solve all design, implementation, and measurement problems.

- **Difference-in-differences.**
Difference-in-differences depends on the parallel trends assumption:

> In the absence of treatment, treated and control groups would have followed similar trends.

Formally, in a two-period setting:

$$
\mathbb{E}[Y_{i1}(0)-Y_{i0}(0) \mid D_i=1]
=
\mathbb{E}[Y_{i1}(0)-Y_{i0}(0) \mid D_i=0].
$$

Threats to internal validity include:
    - differential pre-trends
    - simultaneous policies
    - anticipation effects
    - spillovers
    - changing group composition
    - endogenous treatment timing
    - heterogeneous treatment effects with staggered adoption
    - serial correlation and incorrect standard errors
- **Regression discontinuity.**
Regression discontinuity depends on continuity of potential outcomes at the cutoff. The core assumption is that, absent treatment, units just above and below the cutoff would have had similar outcomes. Threats include:
    - precise manipulation of the running variable
    - sorting around the cutoff
    - other policies changing at the same cutoff
    - inappropriate bandwidth choice
    - functional form sensitivity
    - discrete or heaped running variables
    - weak first stage in fuzzy RD

RD can have strong internal validity near the cutoff, but only if the cutoff really creates quasi-random treatment variation locally.
- **Instrumental variables.**
IV depends on assumptions about the instrument $Z$. The main assumptions are:
1. relevance:
$\operatorname{Cov}(Z_i,D_i) \neq 0,$
2. independence or as-good-as-random assignment of $Z_i$,
3. exclusion restriction:
$Z_i \rightarrow D_i \rightarrow Y_i,$ with no direct path:
$Z_i \rightarrow Y_i,$
4. monotonicity, for LATE interpretation.

Threats include:
    - weak instruments
    - direct effects of the instrument
    - correlation between the instrument and omitted variables
    - multiple channels
    - defiers
    - invalid exclusion restriction
    - misunderstanding the local population of compliers
    - **Fixed effects.**
    Fixed effects control for time-invariant unobserved heterogeneity. A basic unit fixed effects model is:
$Y_{it} = \alpha_i + \beta D_{it} + u_{it}.$ The unit fixed effect $\alpha_i$ absorbs all stable characteristics of unit $i$. Threats include:
    - time-varying confounding
    - reverse causality
    - dynamic feedback
    - measurement error amplified by within variation
    - anticipation
    - treatment timing related to shocks
    - bad controls
    - limited within-unit variation

Fixed effects do not make treatment random. They only remove confounding from variables that are constant within units over time.
- **Matching and weighting.**
Matching and weighting rely on conditional independence:
$(Y_i(1),Y_i(0)) \perp D_i \mid X_i.$ This means treatment is as good as random after conditioning on observed covariates. Threats include:
    - unobserved confounding
    - poor overlap
    - model dependence
    - inappropriate covariate adjustment
    - matching on post-treatment variables
    - sensitivity to specification

Matching can improve comparability on observed variables, but it cannot solve selection on unobservables without additional assumptions.

## 15.5 Diagnosing internal validity
Internal validity cannot usually be proven. It must be argued using design logic, institutional knowledge, and diagnostic evidence. Common diagnostics include:

1. **Balance tests:** Balance tests examine whether treated and control groups are similar on pre-treatment covariates. In an RCT, balance tests can detect randomization failures or unusual finite-sample imbalance. In observational studies, balance tests show whether adjustment, matching, or weighting improved comparability. However, balance on observed variables does not prove balance on unobserved variables.

2. **Pre-trend tests:** Pre-trend tests examine whether treated and control groups followed similar trends before treatment. They are especially important in difference-in-differences and event-study designs. If treated and control groups diverged before treatment, the parallel trends assumption is less credible. However, failure to reject different pre-trends does not prove parallel trends. Tests may have low power, and unobserved counterfactual trends after treatment may still differ.

3. **Placebo tests:** Placebo tests apply the research design to settings where no effect should exist. Examples:
    - estimating an effect before treatment occurred
    - using an outcome that should not be affected by treatment
    - using a fake cutoff in RD
    - using a fake policy date in DiD

    A significant placebo effect suggests the design may be capturing something other than the causal effect.

4. **Falsification tests:** Falsification tests examine implications that should be false if the causal story is correct. For example, if a policy affects adult earnings through schooling, it should not affect predetermined childhood characteristics. If it does, the treated and control groups may not be comparable.

5. **Manipulation tests:** In RD designs, researchers often test whether units manipulate the running variable around the cutoff. If there is bunching just above or below the cutoff, treatment assignment may not be as-good-as-random near the threshold.

6. **Attrition analysis:** Researchers should compare attrition rates across treatment and control groups. They should ask:
    - Is attrition higher in one group?
    - Are attriters different from stayers?
    - Is attrition related to baseline outcomes?
    - Are results robust to bounds or weighting?

7. **Robustness checks:** Robustness checks examine whether results change under reasonable alternative specifications. Examples:
    - adding or removing controls
    - changing bandwidths in RD
    - using alternative control groups
    - excluding influential observations
    - testing alternative functional forms
    - clustering standard errors differently
    - using alternative outcome definitions

    Robustness does not prove validity, but fragility can reveal design weaknesses.

8. **Sensitivity analysis:** Sensitivity analysis asks how strong an unobserved bias would need to be to overturn the result. This is especially important when unobserved confounding cannot be ruled out. For example, in an observational study of education and earnings, sensitivity analysis might ask how large an unmeasured ability difference would need to be to explain away the estimated return to education.

## 15.6 External validity
External validity asks:

> Does the causal effect estimated in this study generalize to other populations, settings, treatments, time periods, or scales?

A study's internal validity concerns whether the estimate is credible where it was estimated. External validity concerns where else the result applies. Suppose an RCT finds that a tutoring program raises test scores by $0.25$ standard deviations among middle-school students in one urban district. External validity asks:
- Would the program work for elementary students?
- Would it work for high school students?
- Would it work in rural schools?
- Would it work in another country?
- Would it work if delivered online?
- Would it work if scaled to thousands of schools?
- Would it work with different tutors?
- Would it work five years later?

These are not secondary questions. They are central to policy interpretation.

## 15.7 Dimensions of external validity
External validity can fail along several dimensions.

1. **Population external validity:** Population external validity asks whether the result applies to different people or units. A program estimated on unemployed adults may not apply to teenagers, older workers, college graduates, immigrants, or workers with disabilities. Treatment effects may vary by:
    - age
    - gender
    - race
    - income
    - baseline skill
    - education
    - health
    - geography
    - prior exposure
    - motivation
    - institutional context

    If treatment effects are heterogeneous, the average effect in one population may not equal the average effect in another. Formally, suppose the effect depends on covariates $X_i$:
    $\tau_i = Y_i(1)-Y_i(0),$ and:
    $\mathbb{E}[\tau_i \mid X_i=x]$ varies with $x$. Then changing the distribution of $X_i$ changes the population average treatment effect:
    $ATE = \mathbb{E}[\tau_i].$

2. **Setting external validity:** Setting external validity asks whether the result applies across institutional, geographic, cultural, or economic contexts. A labor market program may work in a city with strong employer demand but fail in a depressed region. A policing reform may work in one legal system but not another. A healthcare intervention may depend on insurance institutions, provider capacity, and baseline access. Economic effects often depend on institutions.

3. **Treatment-version external validity:** Many treatments have multiple versions. For example, "job training" could mean:
    - classroom training
    - apprenticeships
    - online modules
    - employer-based training
    - certification
    - job search assistance
    - wage subsidies
    - counseling

    An estimate from one version does not necessarily generalize to another. This relates to SUTVA and the problem of hidden treatment versions. If treatment is not well defined, external validity is unclear.

4. **Time external validity:** Effects may change over time. A policy effect estimated in 1995 may not apply in 2026. Labor markets, technology, demographics, institutions, and norms change. Examples:
    - returns to computer training may differ before and after widespread digital adoption
    - minimum wage effects may differ in tight versus weak labor markets
    - online education effects may change as technology improves
    - immigration effects may depend on current industry composition

    Time is not just a background variable. It can alter mechanisms.

5. **Scale external validity:** A program may work at small scale but not at large scale. Small programs often benefit from:
    - highly motivated implementers
    - close monitoring
    - selected participants
    - limited competition for resources
    - high-quality staff
    - novelty effects

    When scaled, the program may face:
    - lower implementation quality
    - capacity constraints
    - general equilibrium effects
    - political resistance
    - participant dilution
    - labor market saturation
    - changes in incentives

    For example, a job training program may raise earnings for a small group by helping them obtain available jobs. But if the program is expanded to all unemployed workers, it may not create enough new jobs for everyone.

6. **Outcome external validity:** A study may estimate effects on one outcome but not others. For example, a schooling intervention may raise test scores but not long-term earnings. A policing intervention may reduce reported crime but harm trust in institutions. A health program may improve short-run biomarkers but not long-run mortality. Policy decisions often require a broader outcome set than the study measures.

## 15.8 Transportability
Transportability refers to the problem of using evidence from one setting to predict effects in another. Suppose a study estimates:
$ATE_A = \mathbb{E}_A[Y_i(1)-Y_i(0)],$ where $A$ is the original study population. A policymaker wants to know:
$ATE_B = \mathbb{E}_B[Y_i(1)-Y_i(0)],$
where $B$ is a new target population. The original estimate transports directly only if the treatment effect is the same across the two populations, or if differences in treatment effects can be explained and adjusted for. If treatment effects depend on covariates $X_i$, then one possible transport formula is:
$ATE_B = \int \mathbb{E}[Y_i(1)-Y_i(0) \mid X_i=x] \, dF_B(x),$ where $F_B(x)$ is the distribution of covariates in the target population. In plain English:

> To generalize from one population to another, we need to know how effects vary across characteristics and how common those characteristics are in the new population.

Transportability requires knowledge of mechanisms and effect heterogeneity.

## 15.9 Internal validity versus external validity: tradeoffs and tensions
Researchers sometimes face a tradeoff between internal and external validity. A tightly controlled RCT may have strong internal validity but involve a narrow population, artificial setting, or small-scale implementation. A large observational study may cover a broad population but have weaker internal validity because treatment is not randomly assigned. A regression discontinuity design may be internally credible near the cutoff but estimate an effect only for marginal units. An IV design may solve endogeneity but estimate a LATE for compliers rather than the full population. The tradeoff is not inevitable, but it is common. Examples:
- RD estimates are local to the cutoff
- IV estimates are local to compliers
- RCTs estimate effects of specific implemented treatment versions
- DiD estimates may depend on treated units and treatment timing
- Fixed effects estimates use within-unit variation and may not generalize to between-unit policy changes

A rigorous study should state not only whether it is internally valid, but also what population and margin the estimate represents.

## 15.10 Construct validity
Construct validity asks:

> Are we measuring the concept we claim to measure?

This is distinct from internal and external validity. A study may have a credible causal design but measure the wrong thing. Examples:
- Test scores may not fully measure learning
- Income may not fully measure welfare
- Arrests may not measure crime if policing intensity changes reporting or enforcement
- Hospital visits may not measure health if access to care changes
- Employment may not measure job quality
- GDP may not measure well-being
- Surveyed happiness may not capture long-term life satisfaction

Construct validity is especially important when outcomes are proxies. Suppose a policing intervention increases arrests. Does that mean crime increased, enforcement increased, reporting increased, or detection improved? Suppose a school reform increases test scores. Does that mean students learned more, teachers taught to the test, or the test became easier? A valid causal estimate of a poorly measured construct can still mislead.

## 15.11 Statistical conclusion validity
Statistical conclusion validity asks:

> Are the statistical inferences sound?

Even if the design is conceptually valid, statistical errors can lead to wrong conclusions. Threats include:
- small sample size
- low statistical power
- incorrect standard errors
- serial correlation
- clustering ignored
- multiple hypothesis testing
- p-hacking
- selective reporting
- outliers
- model misspecification
- weak instruments
- overfitting
- inappropriate functional form

For example, in a difference-in-differences study with state-level policies, observations within states over time are correlated. If standard errors are not clustered at the appropriate level, the study may overstate precision. In an RCT with many outcomes, some significant estimates may appear by chance unless multiple testing is addressed. Statistical conclusion validity is about whether the evidence is statistically reliable, not just whether the research design is causally credible.

## 15.12 Ecological validity
Ecological validity asks:

> Does the study environment resemble the real-world environment where the conclusion will be applied?

This is especially relevant for lab experiments, survey experiments, and artificial tasks. For example, a lab experiment may show that people behave generously in a controlled game with small stakes. But does that behavior generalize to real charitable giving, workplace cooperation, or political behavior? A resume audit study may estimate discrimination in callback rates for fictional applicants. That is informative, but it may not capture later stages of hiring, wage offers, promotions, or workplace treatment. Ecological validity is related to external validity, but it focuses specifically on whether the study context resembles the real-world decision environment.

## 15.13 Policy validity
Policy validity asks:

> Does the evidence answer the policy question that decision-makers actually face?

A study may estimate a causal effect correctly but still not answer the relevant policy question. Examples:
- A study estimates the effect of being offered job training, but policymakers need the effect of mandatory participation
- A study estimates short-run test score gains, but policymakers care about long-run earnings
- A study estimates the effect of a pilot program, but policymakers care about national scale-up
- A study estimates average effects, but policymakers care about disadvantaged subgroups
- A study estimates private benefits, but policy requires social benefits and costs

Policy validity requires aligning the estimand with the decision. A useful policy evaluation should specify:
1. the policy option,
2. the relevant counterfactual,
3. the affected population,
4. the time horizon,
5. the outcome set,
6. distributional effects,
7. costs,
8. implementation constraints,
9. scalability,
10. uncertainty.

## 15.14 Validity and mechanisms
Mechanisms help connect internal and external validity. An internally valid study estimates whether a treatment works in a particular context. Mechanisms help explain why it works. Knowing the mechanism helps determine whether the effect will generalize. Example: suppose a tutoring program raises test scores. Possible mechanisms include:
$Tutoring \rightarrow More\ instructional\ time \rightarrow Higher\ test\ scores,$
$Tutoring \rightarrow Mentoring \rightarrow Motivation \rightarrow Higher\ test\ scores,$ or:
$Tutoring \rightarrow Test\ preparation \rightarrow Higher\ test\ scores.$
Each mechanism has different implications for external validity. If the effect works through instructional time, similar programs may generalize where students lack instructional support. If the effect works through unusually talented tutors, scale-up may be difficult. If the effect works mainly through test preparation, test score gains may not translate into long-term learning. Mechanisms do not replace identification, but they help interpret and transport results.

## 15.15 Validity and heterogeneous treatment effects
External validity is closely connected to heterogeneous treatment effects. If treatment effects are constant, generalization is easier. If every unit has the same treatment effect:
$Y_i(1)-Y_i(0)=\tau$ for all $i$, then an internally valid estimate from one sample may apply broadly. But treatment effects are rarely constant. If:
$Y_i(1)-Y_i(0)=\tau_i,$
and $\tau_i$ differs across people, places, or time periods, then the average effect depends on the composition of the sample. For example, a training program may have large effects for workers with low baseline skills but small effects for highly educated workers. If the original study sample contains mostly low-skill workers, the estimated average effect may not generalize to a more educated population. This is why subgroup analysis, CATE estimation, and mechanism analysis are important for external validity. However, subgroup analysis introduces its own risks, especially multiple testing and low power. Researchers should distinguish pre-specified heterogeneity analysis from exploratory data mining.

## 15.16 Validity and equilibrium effects
Many economic interventions generate equilibrium responses. A small-scale intervention may estimate a partial equilibrium effect, holding the broader environment fixed. A large-scale policy may produce general equilibrium effects by changing prices, wages, behavior, competition, or market structure. Example: a job training program for a small group may raise participants' earnings by helping them get jobs. But if expanded to all workers, it may increase the supply of trained labor and reduce the wage premium. Example: a housing voucher program may help recipients move to better neighborhoods when few people receive vouchers. But if expanded widely, rents may rise, neighborhood composition may change, or housing supply may respond. Example: a tax incentive may increase investment for treated firms, but if all firms receive it, input prices, interest rates, and competitive dynamics may change. Equilibrium effects are a major external validity issue in economics.

## 15.17 Practical example: tutoring RCT
Suppose researchers conduct an RCT of a tutoring program in one city. Students are randomly assigned to receive tutoring or not. At the end of the year, treated students score $0.25$ standard deviations higher on a math test. The internal validity question is:

> Is the $0.25$ standard deviation estimate a credible causal effect for students in this experiment?

Threats include:
- Was randomization implemented correctly?
- Did control students receive tutoring elsewhere?
- Did treated students actually attend tutoring?
- Were outcome data missing for some students?
- Were missing outcomes related to treatment?
- Did teachers treat students differently because they knew assignment status?
- Were multiple outcomes tested?
- Were standard errors appropriate?

If these threats are handled well, the study may have high internal validity. The external validity question is:

> Would this effect apply elsewhere?

Questions include:
- Were the students representative of other students?
- Were the tutors unusually skilled?
- Was implementation unusually intensive?
- Would effects persist beyond one year?
- Would the program work in rural schools?
- Would it work at scale?
- Would it improve long-run outcomes, not just test scores?
- Would costs be reasonable?

The same estimate can be internally credible and externally uncertain.

## 15.18 Practical example: minimum wage DiD
Suppose a state raises its minimum wage, and a researcher uses difference-in-differences to compare employment changes in that state to neighboring states. The internal validity question is:

> Do neighboring states provide a credible counterfactual for what would have happened in the treated state without the minimum wage increase?

Threats include:
- treated and control states had different pre-trends
- another policy changed at the same time
- firms anticipated the policy
- workers crossed borders
- industry composition changed
- treated and control states faced different economic shocks
- standard errors were not clustered properly

The external validity question is:

> Does this estimate generalize to other minimum wage changes?

Questions include:
- Was the increase small or large?
- Was the labor market strong or weak?
- What industries were affected?
- What was the initial wage distribution?
- Did firms have market power?
- Was enforcement strong?
- Would effects differ nationally?
- Would long-run effects differ from short-run effects?

Minimum wage effects may vary across contexts, so external validity must be argued carefully.

## 15.19 Practical example: college returns using IV
Suppose researchers use distance to college as an instrument for college attendance and estimate that college increases earnings. The internal validity question is:

> Is distance to college a valid instrument?

Threats include:
- distance to college may be correlated with urbanization
- urbanization may affect earnings directly
- families may choose where to live based on preferences or resources
- local labor markets may differ
- distance may affect networks, internships, or migration directly
- the instrument may be weak

The external validity question is:

> For whom does the IV estimate apply?

If the estimate is a LATE, it applies to compliers: people whose college attendance changed because of distance. These may be students on the margin of attending college, not all students. The estimated return may not apply to:
- students who would attend college regardless of distance
- students who would never attend college
- elite college students
- older adults
- future cohorts
- different labor markets

IV estimates often trade broad external validity for stronger internal validity on a particular margin.

**Common mistakes.**
1. **Thinking internal validity implies external validity:** A causal effect can be credible in one setting and still fail to generalize. An RCT is not automatically policy-universal.
2. **Thinking external validity can rescue weak internal validity:** A large, representative dataset does not solve confounding by itself. If the estimate is not internally valid, broad coverage does not make it causal.
3. **Ignoring the estimand:** A study may estimate ATE, ATT, LATE, or a local cutoff effect. These are not interchangeable. External validity depends on knowing whose effect was estimated.
4. **Confusing statistical significance with validity:** A statistically significant estimate can be biased. Validity concerns design and assumptions, not only p-values.
5. **Ignoring implementation:** A policy is not just an abstract treatment. Effects depend on who implements it, how well, at what scale, with what compliance, and under what institutional constraints.
6. **Ignoring outcome scope:** A study may show effects on one outcome while missing other important benefits or harms. Policy decisions often require multiple outcomes and cost-benefit analysis.
7. **Overgeneralizing from local estimates:** RD and IV often estimate local effects. Applying them to broad populations requires additional assumptions.
8. **Treating diagnostics as proof:** Balance tests, pre-trend tests, and placebo tests are useful, but they do not prove assumptions. They provide evidence that may support or weaken the design argument.

**Application checklist.**
When evaluating validity, use the following checklist.
1. **Define the causal claim:** What effect is being claimed? What is the treatment? What is the outcome? What is the target population?
2. **Identify the estimand:** Is the study estimating ATE, ATT, ATU, CATE, LATE, a local cutoff effect, an intent-to-treat effect, or something else?
3. **Evaluate internal validity:** What comparison group represents the missing counterfactual? Why is that comparison credible? What assumptions are required?
4. **Identify internal validity threats:** Consider:
    - confounding
    - selection
    - omitted variables
    - reverse causality
    - simultaneity
    - attrition
    - noncompliance
    - spillovers
    - anticipation
    - measurement error
    - regression to the mean
    - simultaneous shocks
5. **Examine diagnostic evidence:** Look for:
    - balance tests
    - pre-trends
    - placebo tests
    - falsification tests
    - robustness checks
    - manipulation tests
    - attrition analysis
    - sensitivity analysis
6. **Evaluate statistical conclusion validity:** Are standard errors appropriate? Is the sample large enough? Was clustering handled correctly? Were multiple hypotheses tested? Are results robust to outliers and specification choices?
7. **Evaluate construct validity:** Does the measured treatment correspond to the intended intervention? Does the measured outcome correspond to the concept of interest? Are there important unmeasured outcomes?
8. **Evaluate external validity:** Would the effect generalize to different:
    - populations
    - places
    - institutions
    - time periods
    - treatment versions
    - scales
    - implementation conditions
    - outcome horizons?
9. **Consider mechanisms:** Why did the treatment work or not work? Would that mechanism operate in the target setting?
10. **State limitations clearly:** What can the study support? What can it not support? What additional evidence would improve confidence?

## 15.20 Summary
Validity determines whether empirical evidence supports the conclusions drawn from it. Internal validity asks whether the estimated effect is credible in the study setting. It depends on whether the research design provides a valid counterfactual and avoids threats such as confounding, selection bias, omitted variables, reverse causality, attrition, noncompliance, spillovers, anticipation, and measurement error. External validity asks whether the estimated effect generalizes beyond the study setting. It depends on population differences, institutional context, treatment versions, timing, implementation, scale, mechanisms, equilibrium responses, and heterogeneous treatment effects. Other validity concepts also matter. Construct validity asks whether the study measures the concepts it claims to measure. Statistical conclusion validity asks whether the statistical inference is sound. Ecological validity asks whether the study environment resembles the real-world environment of interest. Policy validity asks whether the evidence answers the decision-maker's actual question. A strong empirical study is not one that simply produces a significant coefficient. A strong empirical study clearly defines the estimand, uses a credible design, states assumptions, probes threats, quantifies uncertainty, explains mechanisms, and carefully limits its conclusions. The central lesson is:

> Internal validity tells us whether we should believe the causal estimate in the study context. External validity tells us where else, and under what conditions, that estimate should be expected to apply.

# 16. Heterogeneous Treatment Effects
## 16.1 Why treatment effects are rarely the same for everyone
A treatment effect is heterogeneous when the effect of a treatment differs across people, firms, schools, neighborhoods, markets, regions, time periods, or institutional settings. This is not a special case. In economics and social science, treatment effect heterogeneity is usually the rule rather than the exception. A job training program may help workers with weak labor market attachment more than workers who already have strong employment prospects. A tutoring program may help students near proficiency more than students far below grade level. A minimum wage increase may affect teenagers differently from prime-age workers. A tax change may affect liquidity-constrained households differently from wealthy households. A medical treatment may work differently by age, baseline health, or disease severity. The idea that a policy has one single effect can be useful as a simplification, but it is often incomplete. The central question is not only:

> Does the treatment work?

It is also:

> For whom does it work, by how much, under what conditions, and at what cost?

Heterogeneous treatment effects matter for at least five reasons. First, they affect interpretation. An average effect can hide large gains for some groups and losses for others. Second, they affect policy targeting. A program may be worth expanding for one population but not another. Third, they affect external validity. A result from one setting may not generalize if the new setting has a different population mix. Fourth, they affect equity. A policy may improve average outcomes while worsening outcomes for disadvantaged groups, or vice versa. Fifth, they affect welfare analysis. Cost-benefit conclusions can change when effects vary across groups with different needs, costs, or social weights. A rigorous empirical analysis should therefore distinguish between the average effect being estimated and the distribution of effects behind that average.

---

## 16.2 Individual treatment effects
In the potential outcomes framework, each unit has two potential outcomes under binary treatment:
$Y_i(1)$ and:
$Y_i(0)$ where $Y_i(1)$ is the outcome unit $i$ would have under treatment and $Y_i(0)$ is the outcome unit $i$ would have without treatment. The individual treatment effect is:
$\tau_i = Y_i(1)-Y_i(0)$ This is the causal effect of treatment for unit $i$. If $\tau_i$ is the same for every unit, treatment effects are homogeneous. In that case:
$\tau_i = \tau$ for all $i$. But if treatment effects vary across units, then:
$\tau_i \neq \tau_j$ for at least some units $i$ and $j$. For example, suppose a job training program changes annual earnings as follows:

| Worker | Earnings without training | Earnings with training | Individual effect |
|---:|---:|---:|---:|
| A | \$20,000 | \$28,000 | \$8,000 |
| B | \$30,000 | \$34,000 | \$4,000 |
| C | \$45,000 | \$45,000 | \$0 |
| D | \$60,000 | \$58,000 | -\$2,000 |

The program helps some workers, has no effect on one worker, and harms another worker. The average effect may be positive, but the average does not describe everyone. The fundamental problem is that individual treatment effects are usually not observed. For each unit, we observe only one potential outcome. A treated worker reveals $Y_i(1)$ but not $Y_i(0)$. An untreated worker reveals $Y_i(0)$ but not $Y_i(1)$. Therefore, empirical work usually estimates average treatment effects rather than individual treatment effects.

---

## 16.3 Average Treatment Effect, or ATE
The average treatment effect, or ATE, is:
$ATE = \mathbb{E}[Y_i(1)-Y_i(0)]$ Using linearity of expectation:
$ATE = \mathbb{E}[Y_i(1)] - \mathbb{E}[Y_i(0)]$ The ATE answers:

> What is the average effect if everyone in the target population were treated compared with if no one in the target population were treated?

For a job training program, the ATE asks:

> How much would average earnings change if everyone in the population received job training rather than no one receiving it?

For a tutoring program, the ATE asks:

> How much would average test scores change if all students received tutoring rather than no students receiving it?

The ATE is often the natural estimand when policymakers are considering universal treatment or population-wide exposure. However, the ATE can be misleading if effects differ sharply across groups. Suppose a program has the following effects:

| Group | Share of population | Treatment effect |
|---|---:|---:|
| Low-income workers | 50% | \$4,000 |
| High-income workers | 50% | -\$1,000 |

The ATE is:
$ATE = 0.5(4{,}000) + 0.5(-1{,}000) = 1{,}500$
The average effect is positive, but the program helps one group and harms another. A policy decision based only on the ATE would miss this distributional structure. The ATE is useful, but it is not always sufficient.

---

## 16.4 Average Treatment Effect on the Treated, or ATT
The average treatment effect on the treated, or ATT, is:
$ATT = \mathbb{E}[Y_i(1)-Y_i(0) \mid D_i=1]$ The ATT answers:

> What is the average effect of treatment for the units that actually received treatment?

This estimand is especially important when treatment is voluntary, targeted, or already implemented. For a voluntary job training program, the ATT asks:

> How much did training increase earnings for the workers who actually participated?

For a college scholarship program, the ATT asks:

> How much did the scholarship affect the students who actually received it?

For a medical treatment, the ATT asks:

> How much did treatment affect the patients who actually took it?

The ATT can differ from the ATE when treated units are not representative of the broader population. For example, if motivated workers are more likely to enroll in training and also benefit more from training, then:
$ATT > ATE$ But if the program targets the most disadvantaged workers, who face many barriers even after training, then:
$ATT < ATE$
The ATT is often the most relevant estimand for evaluating an existing program. If a program has already been implemented for a specific group, policymakers may first want to know whether it helped that group. But the ATT does not automatically answer whether the program should be expanded. The effect for current participants may differ from the effect for nonparticipants.

---

## 16.5 Average Treatment Effect on the Untreated, or ATU
The average treatment effect on the untreated, or ATU, is:
$ATU = \mathbb{E}[Y_i(1)-Y_i(0) \mid D_i=0]$ The ATU answers:

> What would the average treatment effect be for units that did not receive treatment?

This is often important for policy expansion. Suppose a job training program currently serves motivated unemployed workers who actively apply. The ATT may be large. But if policymakers expand the program to all unemployed workers, the new participants may differ from the original participants. They may have different skills, barriers, motivation, health constraints, childcare constraints, or local labor market opportunities. In that case, the relevant question is not only:
$ATT = \mathbb{E}[Y_i(1)-Y_i(0) \mid D_i=1]$ but also:
$ATU = \mathbb{E}[Y_i(1)-Y_i(0) \mid D_i=0]$
The ATU can be larger or smaller than the ATT. It may be larger if untreated units have more room to improve. It may be smaller if untreated units face barriers that make the treatment less effective. The distinction between ATT and ATU is crucial for scaling policy. A program that works well for current participants may not work equally well for people who did not originally participate.

---

## 16.6 Conditional Average Treatment Effects, or CATEs
The conditional average treatment effect, or CATE, is:
$CATE(x) = \mathbb{E}[Y_i(1)-Y_i(0) \mid X_i=x]$ The CATE answers:

> What is the average treatment effect for units with characteristics $X_i=x$?

For example:
$\mathbb{E}[Y_i(1)-Y_i(0) \mid Age_i < 25]$ is the average effect for young workers. Or:
$\mathbb{E}[Y_i(1)-Y_i(0) \mid BaselineScore_i < 50]$
is the average effect for students with low baseline test scores. CATEs are central to understanding who benefits from treatment. For example, a tutoring program may have different effects by baseline achievement:

| Baseline achievement group | Average treatment effect |
|---|---:|
| Far below grade level | 0.05 SD |
| Slightly below grade level | 0.25 SD |
| At grade level | 0.10 SD |
| Above grade level | 0.00 SD |

The overall average may be positive, but the program is especially effective for students slightly below grade level. CATEs can be defined using many types of covariates:
- age
- gender
- income
- baseline outcome
- prior exposure
- location
- school type
- firm size
- industry
- local labor market conditions
- political institutions
- health status
- risk level
- treatment intensity

CATEs are useful for targeting, but they must be estimated carefully. Searching across many subgroups can produce false discoveries. Subgroup analysis should be guided by theory, pre-specified hypotheses, and appropriate multiple-testing adjustments when necessary.

---

## 16.7 Local Average Treatment Effect, or LATE
The local average treatment effect, or LATE, appears most often in instrumental variables research. Suppose treatment $D_i$ is endogenous, and an instrument $Z_i$ shifts the probability of treatment. Under the standard IV assumptions, including relevance, independence, exclusion, and monotonicity, IV identifies the average treatment effect for compliers. Compliers are units whose treatment status changes because of the instrument. The LATE is:
$LATE = \mathbb{E}[Y_i(1)-Y_i(0) \mid \text{complier}]$
For example, suppose distance to college is used as an instrument for college attendance. The instrument compares people who attend college because they live near a college with people who would not attend if they lived farther away. The IV estimate does not necessarily identify the effect of college for everyone. It identifies the effect for people whose college attendance is changed by distance. These people are compliers. Similarly, if a draft lottery is used as an instrument for military service, the IV estimate identifies the effect of military service for people whose service status was changed by the lottery. The LATE can differ from the ATE, ATT, and ATU. This is not a flaw by itself. A local effect can be highly valuable if the complier group is policy-relevant. But researchers must be clear about what group the estimate applies to. A common mistake is to interpret an IV estimate as the average effect for everyone. Unless treatment effects are homogeneous, this is usually not justified.

---

## 16.8 Treatment effect heterogeneity and selection into treatment
Selection into treatment and treatment effect heterogeneity are closely related. People may select into treatment partly because they expect to benefit from it. For example, workers may enroll in job training if they believe it will improve their employment prospects. Students may apply to college if they expect a high return. Firms may adopt technology if they expect productivity gains. Patients may choose a treatment if they expect it to work for their condition. This means treatment status may be related not only to potential outcome levels but also to treatment effects. Formally, selection into treatment may depend on:
$Y_i(1)-Y_i(0)$ If individuals select into treatment based on expected gains, then treated units may have larger treatment effects than untreated units:
$ATT > ATU$
This is sometimes called selection on gains. For example, suppose college attendance is voluntary. Students who expect high returns to college may be more likely to attend. In that case, the average return to college among college attendees may be larger than the average return among non-attendees. Alternatively, treatment may be targeted toward those with the greatest need but not necessarily the highest gains. For example, a remedial education program may target students with low baseline performance. If those students face many barriers, their treatment effects may be smaller or larger depending on the intervention. Selection on gains matters because it affects external validity and policy expansion. If those who choose treatment are those who benefit most, expanding treatment to nonparticipants may yield smaller effects.

---

## 16.9 Heterogeneous effects and regression models
A standard linear regression often estimates an average relationship:
$Y_i = \alpha + \beta D_i + u_i$
If $D_i$ is randomly assigned, then $\beta$ estimates the average treatment effect in the sample. But if treatment effects are heterogeneous, the regression coefficient is an average of different individual or group effects. Suppose the true model is:
$Y_i = \alpha + \tau_i D_i + u_i$
where $\tau_i$ varies across units. A regression that estimates one coefficient $\beta$ summarizes these heterogeneous effects with a single number. To study heterogeneity, researchers often include interactions:
$Y_i = \alpha + \beta D_i + \gamma X_i + \delta(D_i \times X_i) + u_i$ Here, the treatment effect depends on $X_i$:
$\frac{\partial Y_i}{\partial D_i} = \beta + \delta X_i$ If $X_i$ is binary, such as an indicator for young workers, then:
- $\beta$ is the treatment effect for the reference group
- $\beta + \delta$ is the treatment effect for the group with $X_i=1$
- $\delta$ is the difference in treatment effects between groups

For example:
$Earnings_i = \alpha + \beta Training_i + \gamma Young_i + \delta(Training_i \times Young_i) + u_i$ If $Young_i=0$, the effect of training is:
$\beta$ If $Young_i=1$, the effect of training is:
$\beta + \delta$
The interaction coefficient $\delta$ measures whether the treatment effect differs for young workers relative to older workers. Interactions are useful, but they must be interpreted carefully. A statistically insignificant interaction does not prove effects are homogeneous. The study may simply lack power to detect heterogeneity.

---

## 16.10 Subgroup analysis
Subgroup analysis estimates treatment effects separately for different groups. For example, a researcher might estimate the effect of tutoring separately for:
- students with low baseline test scores
- students with medium baseline test scores
- students with high baseline test scores

Or a researcher might estimate the effect of job training separately by:
- age
- gender
- prior earnings
- education level
- local unemployment rate

Subgroup analysis can be valuable when the subgroups are theoretically motivated and policy-relevant. However, subgroup analysis has several dangers. First, it reduces sample size within each group. Smaller samples produce less precise estimates. Second, testing many subgroups increases the risk of false positives. If researchers search across enough groups, some differences will appear statistically significant by chance. Third, subgroup definitions can be arbitrary. Different cutoffs may produce different conclusions. Fourth, observed subgroup differences may reflect multiple correlated characteristics. For example, differences by neighborhood may reflect income, race, school quality, pollution, policing, and labor market access. Fifth, subgroup effects may not generalize if they are discovered after looking at the data. Good subgroup analysis should therefore be guided by:
1. theory,
2. prior evidence,
3. pre-analysis plans when possible,
4. transparent reporting of all tested subgroups,
5. adjustment for multiple testing when appropriate,
6. humility about exploratory findings.

Exploratory subgroup analysis can generate hypotheses, but confirmatory claims require stronger evidence.

---

## 16.11 Distributional treatment effects
Average effects summarize mean changes. But policies may affect the entire distribution of outcomes. For example, a minimum wage increase may have little effect on average earnings but large effects at the bottom of the wage distribution. A tutoring program may raise low-performing students more than high-performing students. A tax credit may affect low-income households differently from middle-income households. Distributional effects ask how treatment changes the distribution of $Y$, not just its mean. One object of interest is the cumulative distribution function under treatment:
$F_1(y) = P(Y_i(1) \leq y)$ and without treatment:
$F_0(y) = P(Y_i(0) \leq y)$ Comparing $F_1(y)$ and $F_0(y)$ shows how treatment shifts the full outcome distribution. Researchers may also study quantile treatment effects. The $q$th quantile treatment effect is:
$QTE(q) = Q_{Y(1)}(q) - Q_{Y(0)}(q)$ where $Q_{Y(1)}(q)$ is the $q$th quantile of the treated potential outcome distribution and $Q_{Y(0)}(q)$ is the $q$th quantile of the untreated potential outcome distribution. For example:
- the 10th percentile effect shows how treatment affects the lower tail
- the median effect shows how treatment affects the middle
- the 90th percentile effect shows how treatment affects the upper tail

Distributional effects are important when researchers care about inequality, poverty, risk, downside outcomes, or dispersion. A policy can have the same average effect in two settings but very different distributional consequences. For example:

| Policy | Mean effect | Distributional pattern |
|---|---:|---|
| A | \$1,000 | Everyone gains \$1,000 |
| B | \$1,000 | Half gain \$4,000, half lose \$2,000 |
| C | \$1,000 | Low-income people gain, high-income people lose |
| D | \$1,000 | High-income people gain, low-income people lose |

The mean effect is the same, but the policy implications differ sharply.

---

## 16.12 Dynamic treatment effects
Treatment effects may vary over time. A program may have small short-run effects and large long-run effects. Another intervention may have immediate effects that fade. Some policies may generate anticipation effects before treatment formally begins. Let $t$ index time relative to treatment. A dynamic treatment effect can be written as:
$\tau_t = \mathbb{E}[Y_{i,t}(1)-Y_{i,t}(0)]$ where $t=0$ might be the treatment period, $t=1$ one period after treatment, and so on. Examples:
- A preschool program may have modest test score effects in the short run but large effects on graduation, earnings, and crime decades later
- A job training program may reduce earnings while participants are in training but increase earnings later
- A tax rebate may increase consumption immediately but have little long-term effect
- A health intervention may improve outcomes gradually over time
- A technology adoption policy may produce learning costs first and productivity gains later

Dynamic effects matter because the timing of measurement can change conclusions. If a job training program is evaluated during the training period, it may appear to reduce earnings because participants spend time in class rather than working. If evaluated two years later, it may appear beneficial. Therefore, researchers should specify:
1. when treatment occurs,
2. when outcomes are measured,
3. whether effects are expected to be immediate or delayed,
4. whether effects persist, fade, or grow,
5. whether anticipation effects are possible.

Event-study designs are often used to study dynamic treatment effects.

---

## 16.13 Mechanisms and heterogeneous effects
Treatment effects may vary because mechanisms differ across groups. For example, job training may affect earnings through several channels:
$Training \rightarrow Skills \rightarrow Earnings$
$Training \rightarrow Credential \rightarrow Employer\ Beliefs \rightarrow Earnings$
$Training \rightarrow Job\ Search\ Network \rightarrow Employment \rightarrow Earnings$
Different workers may benefit through different mechanisms. Young workers may benefit because they acquire basic skills. Experienced workers may benefit less from basic training but more from credentialing. Workers in strong labor markets may benefit from job placement, while workers in weak labor markets may not. Understanding mechanisms helps explain heterogeneity. However, mechanism analysis requires caution. If a researcher controls for a mediator, the estimated treatment effect changes meaning. Suppose:
$D \rightarrow M \rightarrow Y$
where $D$ is treatment, $M$ is a mediator, and $Y$ is the outcome. A regression that controls for $M$ may estimate a direct effect of $D$ holding $M$ fixed, not the total effect of $D$. If the goal is to estimate the total effect, controlling for mediators can be a bad control problem. Mechanisms are useful for interpreting heterogeneity, but they should be analyzed with a clear causal model.

---

## 16.14 Heterogeneity and external validity
External validity depends heavily on treatment effect heterogeneity. Suppose a tutoring program is tested in one city and produces an average effect of 0.25 standard deviations. Whether that effect generalizes to another city depends on whether the new city has similar students, teachers, schools, implementation quality, baseline achievement, and institutional conditions. If treatment effects are homogeneous, generalization is easier. But if treatment effects vary by context, then the original estimate may not transport directly. Let the effect in setting $s$ be:
$\tau_s = \mathbb{E}[Y_i(1)-Y_i(0) \mid S_i=s]$ An estimate from setting $s=1$ may not equal the effect in setting $s=2$:
$\tau_1 \neq \tau_2$ This can happen because of differences in:
- population composition
- baseline risk
- institutions
- prices
- labor markets
- implementation quality
- treatment intensity
- compliance
- spillovers
- scale
- political context
- complementary inputs

External validity is therefore not just about whether a study was internally valid. A perfectly credible estimate in one setting may not apply elsewhere. To assess external validity, ask:
1. What population generated the original estimate?
2. What treatment version was studied?
3. What mechanisms produced the effect?
4. Are those mechanisms present in the new setting?
5. Is the distribution of effect modifiers similar?
6. Would implementation quality change?
7. Would scaling alter behavior or equilibrium conditions?

Heterogeneous treatment effects are the bridge between internal validity and external validity.

---

## 16.15 Heterogeneity and policy targeting

If treatment effects vary, policymakers may want to target treatment toward groups with the largest benefits. Suppose a program costs \$2,000 per participant. Estimated treatment effects differ by group:

| Group | Treatment effect on earnings | Program cost | Net gain |
|---|---:|---:|---:|
| Group A | \$5,000 | \$2,000 | \$3,000 |
| Group B | \$2,500 | \$2,000 | \$500 |
| Group C | \$500 | \$2,000 | -\$1,500 |


A universal program may have positive average effects but waste resources on groups with low benefits. A targeted program may produce higher net benefits. However, targeting raises practical and ethical issues. First, treatment effects must be estimated accurately. Noisy subgroup estimates can lead to bad targeting decisions. Second, targeting variables must be observable before treatment. A policymaker cannot target based on post-treatment outcomes. Third, targeting rules may create incentives for manipulation. If eligibility depends on income, test scores, or employment status, people may change behavior to qualify. Fourth, targeting can create stigma or political resistance. Fifth, equity may justify serving groups with smaller measured effects if those groups are more disadvantaged. A purely efficiency-based targeting rule might allocate treatment to those with the highest predicted treatment effects:

$Treat_i = 1 \quad \text{if} \quad \widehat{\tau}_i > Cost_i$ But a social planner may care about distributional weights:
$Treat_i = 1 \quad \text{if} \quad w_i \widehat{\tau}_i > Cost_i$ where $w_i$ is a social weight placed on benefits to unit $i$. Policy targeting therefore requires both causal evidence and normative judgment.

## 16.16 Predicting outcomes versus predicting treatment effects

A common mistake is to confuse predicting outcomes with predicting treatment effects. A model that predicts $Y_i$ well does not necessarily identify who benefits most from treatment. For example, suppose high-achieving students have high test scores whether or not they receive tutoring. A prediction model may identify them as likely to have high outcomes. But that does not mean they have the largest treatment effects. Treatment targeting requires predicting:
$Y_i(1)-Y_i(0)$ not just:
$Y_i$
A student with low predicted achievement may have a large treatment effect if tutoring substantially improves their performance. A student with high predicted achievement may have a small treatment effect if they would do well anyway. This distinction matters for machine learning applications in policy. Supervised learning models are often good at predicting observed outcomes. But treatment effects are counterfactual objects. Estimating heterogeneous treatment effects requires causal identification, not only predictive accuracy. In randomized experiments, machine learning can help estimate CATEs because treatment assignment is independent of potential outcomes. In observational studies, machine learning does not solve confounding by itself. The identifying assumptions still matter. The key rule is:

> A good prediction model is not automatically a good causal model.

---

## 16.17 Machine learning and heterogeneous treatment effects
Modern empirical work increasingly uses machine learning to estimate heterogeneous treatment effects. Methods include:
- causal trees
- causal forests
- Bayesian additive regression trees
- double machine learning
- meta-learners such as S-learners, T-learners, X-learners, and R-learners
- uplift modeling
- policy learning algorithms

The goal is often to estimate CATEs:
$\tau(x) = \mathbb{E}[Y_i(1)-Y_i(0) \mid X_i=x]$
These methods can be useful when there are many covariates and complex interactions. However, machine learning does not remove the need for causal identification. If treatment is randomized, machine learning can search for effect heterogeneity with fewer concerns about confounding. Even then, researchers must be careful about overfitting, multiple testing, and honest sample splitting. If treatment is observational, machine learning can flexibly adjust for observed confounders, but it cannot adjust for unobserved confounders unless the research design addresses them. A causal forest applied to badly confounded observational data may produce sophisticated but biased estimates. Good practice usually requires:
1. a credible identification strategy,
2. pre-treatment covariates,
3. honest sample splitting or cross-fitting,
4. validation of overlap,
5. sensitivity analysis,
6. clear interpretation of the target population,
7. caution about exploratory findings.

Machine learning can improve estimation of heterogeneity, but it does not replace research design.

---

## 16.18 Heterogeneity in common research designs
Different research designs estimate different kinds of treatment effects when effects are heterogeneous.
- **Randomized controlled trials.**
In an RCT, a simple difference in means estimates the ATE for the experimental sample if assignment is random and compliance is perfect. If compliance is imperfect, assignment identifies the intent-to-treat effect:
$ITT = \mathbb{E}[Y_i \mid Z_i=1] - \mathbb{E}[Y_i \mid Z_i=0]$ where $Z_i$ is assignment. If assignment is used as an instrument for treatment received, the IV estimate may identify a LATE for compliers.
- **Instrumental variables.**
With heterogeneous treatment effects, IV usually identifies a LATE, not the ATE. The estimate applies to compliers whose treatment status is shifted by the instrument.
- **Difference-in-differences.**
With heterogeneous treatment effects, DiD estimates an average effect for treated units over the relevant post-treatment periods under the parallel trends assumption. In staggered adoption settings, traditional two-way fixed effects can combine effects using problematic weights if treatment effects vary across cohorts or time. Modern DiD methods estimate cohort-time-specific effects, such as:
$ATT(g,t)$ where $g$ is the group first treated in period $g$ and $t$ is the time period.
- **Regression discontinuity.**
RD estimates a local treatment effect at the cutoff:
$\tau_{RD} = \lim_{x \downarrow c}\mathbb{E}[Y_i \mid X_i=x] - \lim_{x \uparrow c}\mathbb{E}[Y_i \mid X_i=x]$ This effect applies to units near the cutoff, not necessarily to units far away.
- **Matching and weighting.**
Matching and weighting may estimate ATE, ATT, or ATU depending on how weights are constructed. For example, matching untreated units to treated units often targets the ATT. Weighting the full sample to represent the whole population may target the ATE. The main lesson is:

> When treatment effects are heterogeneous, the research design determines not only whether an estimate is causal but also whose effect it estimates.

---

**Common mistakes.**
1. **Saying “the effect” without specifying the estimand:** A study should state whether it estimates ATE, ATT, ATU, CATE, LATE, a quantile effect, or another estimand. Different estimands answer different questions.
2. **Treating a local effect as universal:** An RD estimate near a cutoff or an IV estimate for compliers may not apply to the full population. Local estimates can be valuable, but their scope must be clear.
3. **Ignoring negative or zero effects for subgroups:** A positive average effect can hide harm for some groups. Policy evaluation should examine whether benefits and harms are distributed unevenly.
4. **Overinterpreting exploratory subgroup findings:** If many subgroups are tested, some differences will appear by chance. Subgroup findings should be interpreted in light of theory, pre-specification, and multiple testing concerns.
5. **Confusing baseline risk with treatment effect:** High-risk units are not necessarily high-benefit units. A person may have a bad predicted outcome without treatment but still not benefit much from treatment. Another person may have a moderate baseline risk but a large treatment effect.
6. **Using post-treatment variables to define subgroups:** Subgroups should usually be defined using pre-treatment variables. If subgroup membership is affected by treatment, subgroup analysis can introduce post-treatment bias.
7. **Forgetting costs:** The group with the largest treatment effect may not be the group with the largest net benefit if costs differ across groups. Policy targeting should consider both benefits and costs.

---

**Application checklist.**
When analyzing heterogeneous treatment effects, ask the following questions.
1. **Define the main estimand:** Are you estimating ATE, ATT, ATU, CATE, LATE, a quantile effect, or a dynamic effect?
2. **Identify the target population:** Who does the estimate apply to? The full population? Treated units? Untreated units? Compliers? Units near a cutoff? A specific cohort?
3. **Ask whether heterogeneity is theoretically expected:** What mechanisms suggest effects may differ? Examples: age, baseline risk, income, prior achievement, market conditions, institutions, treatment intensity.
4. **Define subgroups before looking at outcomes when possible:** Pre-specification reduces the risk of data mining.
5. **Use pre-treatment covariates:** Do not define heterogeneity using variables caused by treatment unless you are explicitly studying mediation or post-treatment processes.
6. **Estimate subgroup or conditional effects:** Use interactions, stratification, CATE methods, quantile methods, or design-specific heterogeneity analysis.
7. **Quantify uncertainty:** Report standard errors, confidence intervals, or other uncertainty measures for subgroup effects and differences between effects.
8. **Account for multiple testing:** If many subgroups are tested, consider false discovery risk and report the full set of analyses.
9. **Interpret local effects carefully:** For IV, ask who the compliers are. For RD, ask who is near the cutoff. For DiD, ask which treated groups and time periods drive the estimate.
10. **Connect heterogeneity to policy:** Which groups benefit most? Which groups are harmed? How do costs vary? Would targeting improve welfare? Are there equity concerns?
11. **Assess external validity:** Would the same effects appear in another population, setting, or scale? Are the relevant effect modifiers similar?

---

## 16.19 Summary
Treatment effects are heterogeneous when the effect of treatment differs across units, groups, contexts, or time. The individual treatment effect is:
$\tau_i = Y_i(1)-Y_i(0)$ Because individual treatment effects are usually unobserved, researchers estimate average effects. Important estimands include:
$ATE = \mathbb{E}[Y_i(1)-Y_i(0)]$
$ATT = \mathbb{E}[Y_i(1)-Y_i(0) \mid D_i=1]$
$ATU = \mathbb{E}[Y_i(1)-Y_i(0) \mid D_i=0]$
$CATE(x) = \mathbb{E}[Y_i(1)-Y_i(0) \mid X_i=x]$
$LATE = \mathbb{E}[Y_i(1)-Y_i(0) \mid \text{complier}]$
These estimands answer different questions. ATE describes the average effect in a population. ATT describes the effect for treated units. ATU describes the effect for untreated units. CATE describes subgroup or conditional effects. LATE describes effects for compliers whose treatment status is changed by an instrument. Heterogeneity matters for interpretation, targeting, external validity, equity, and cost-benefit analysis. A positive average effect does not mean everyone benefits. A zero average effect does not mean no one benefits. A local effect does not necessarily generalize to the whole population. The central lesson is:

> Empirical research should not only ask whether a treatment works on average. It should ask for whom it works, under what conditions, through what mechanisms, over what time horizon, and at what cost.

# 17. Effect Size, Economic Significance, and Uncertainty
## 17.1 Why effect size matters
A causal estimate is not complete once we know whether the effect is positive, negative, or statistically significant. We also need to know how large the effect is, how uncertain it is, whether it is meaningful in real-world terms, and whether it matters for the decision being considered. An estimated effect answers a question of magnitude:

> How much does the outcome change when the treatment changes?

For example:
- A job training program increases annual earnings by \$2,000
- A tutoring program raises test scores by $0.20$ standard deviations
- A minimum wage increase reduces employment by $1.5$ percentage points
- A pollution regulation reduces hospital admissions by $4$ admissions per $10,000$ residents
- A tax credit increases labor force participation by $3$ percentage points
- A vaccine campaign reduces infection risk by $40\%$

These are effect sizes. Effect size is central because policy decisions require more than knowing whether an effect exists. A policy with a real but tiny effect may not be worth implementing. A policy with a large but uncertain effect may deserve further study. A statistically insignificant estimate may still be economically important if the confidence interval includes large positive or negative effects. A rigorous empirical interpretation asks:
1. What is the estimated effect?
2. What are the units?
3. What is the baseline level of the outcome?
4. Is the effect large relative to the baseline?
5. Is the effect statistically precise?
6. Is the effect practically or economically meaningful?
7. What range of effects is compatible with the data?
8. Does the effect justify the cost, risk, or tradeoff?
9. For whom does the effect apply?
10. Does the magnitude generalize to other settings?

The main lesson of this section is:

> Statistical significance tells us whether an estimate is distinguishable from a benchmark under a statistical model. Effect size tells us whether the estimate matters.

Both are necessary. Neither is sufficient alone.

---

## 17.2 Point estimates
A point estimate is a single numerical estimate of a parameter. Suppose the causal estimand is the average treatment effect:
$ATE = \mathbb{E}[Y_i(1)-Y_i(0)]$ An estimator produces a sample-based estimate:
$\widehat{ATE}$ For example, if a randomized job training program produces:
$\widehat{ATE} = 2{,}000$
then the estimated effect is a \$2,000 increase in annual earnings. A point estimate is useful because it gives a best estimate of the effect based on the model, design, and data. But a point estimate by itself is incomplete. We also need to know the uncertainty around it. The same point estimate can have very different interpretations depending on precision. Example 1:
$\widehat{ATE} = 2{,}000$ with a 95 percent confidence interval:
$[1{,}500,\ 2{,}500]$ This is a fairly precise positive estimate. Example 2:
$\widehat{ATE} = 2{,}000$ with a 95 percent confidence interval:
$[-3{,}000,\ 7{,}000]$
This is a much less precise estimate. The data are consistent with a negative effect, a small positive effect, or a large positive effect. The point estimate is the same in both examples, but the evidence is much stronger in the first. A point estimate should almost never be interpreted without its uncertainty.

---

## 17.3 Units of measurement
Effect size depends on the units in which the outcome and treatment are measured. Suppose a coefficient is:
$\hat{\beta}=0.05$ This number is meaningless until we know the units. It could mean:
- wages increase by $0.05$ dollars
- wages increase by $5\%$
- employment increases by $5$ percentage points
- test scores increase by $0.05$ standard deviations
- mortality increases by $0.05$ deaths per $1,000$ people
- log earnings increase by approximately $5\%$

The same numerical value can represent very different substantive effects. Whenever interpreting an estimate, identify:
1. the unit of the outcome,
2. the unit of the treatment,
3. whether the treatment is binary, continuous, or categorical,
4. whether variables are in levels, logs, percentages, or standardized units,
5. whether the coefficient is a marginal effect, average effect, elasticity, or semi-elasticity.

For example, consider the regression:
$Wage_i = \alpha + \beta Education_i + u_i$
If $Wage_i$ is measured in dollars per hour and $Education_i$ is measured in years, then $\beta$ is interpreted as the dollar change in hourly wage associated with one additional year of education. If instead the outcome is log wages:
$\log(Wage_i) = \alpha + \beta Education_i + u_i$ then $\beta$ is approximately the proportional change in wages associated with one additional year of education. For small values of $\beta$:
$100\beta$ is approximately the percent change in wages. Thus, if:
$\hat{\beta}=0.08$
then one additional year of education is associated with approximately an $8\%$ increase in wages, assuming the estimate is causal. The phrase "assuming the estimate is causal" matters. A coefficient can have a clear unit interpretation without having a causal interpretation.

---

## 17.4 Levels, percentages, percentage points, and logs
Empirical interpretation often goes wrong because people confuse levels, percentages, percentage points, and logs.
- **Levels.**
A level effect is measured in the original unit of the outcome. Example:
$\widehat{ATE}=2{,}000$ If the outcome is annual earnings in dollars, this means the estimated effect is \$2,000 per year.
- **Percent changes.**
A percent change is relative to a baseline. If earnings increase from \$40,000 to \$42,000, the increase is:
$\frac{42{,}000-40{,}000}{40{,}000}=0.05$
or $5\%$. Percent changes are useful when the baseline scale matters. A \$2,000 increase means something different for someone earning \$20,000 than for someone earning \$200,000. For someone earning \$20,000:
$\frac{2{,}000}{20{,}000}=0.10$ or $10\%$. For someone earning \$200,000:
$\frac{2{,}000}{200{,}000}=0.01$ or $1\%$.
- **Percentage points.**
A percentage point change is an absolute change in a rate or probability. If employment rises from $60\%$ to $65\%$, the increase is:
$65\%-60\%=5$ percentage points. The percent increase is:
$\frac{65\%-60\%}{60\%}=8.33\%$ These are not the same. Saying employment increased by $5\%$ is different from saying employment increased by $5$ percentage points.
- **Logs.**
Log outcomes are common in economics, especially for wages, income, prices, firm size, and population. A regression such as:
$\log(Y_i)=\alpha+\beta D_i+u_i$ with binary treatment $D_i$ is often interpreted approximately as a $100\beta$ percent change in $Y$. For larger values of $\beta$, the exact percent change is:
$100\left(e^\beta-1\right)$ For example, if:
$\hat{\beta}=0.20$ then the approximate percent change is $20\%$, but the exact percent change is:
$100(e^{0.20}-1)\approx 22.1\%$ For small coefficients, the approximation is close. For larger coefficients, the exact transformation is better.
---

## 17.5 Elasticities and semi-elasticities
Elasticities are common in applied economics because they express effects in proportional terms. An elasticity measures the percent change in $Y$ associated with a one percent change in $X$. Formally:
$Elasticity = \frac{\partial Y}{\partial X}\frac{X}{Y}$ In a log-log regression:
$\log(Y_i)=\alpha+\beta \log(X_i)+u_i$ the coefficient $\beta$ is an elasticity. It means:

> A 1 percent increase in $X$ is associated with a $\beta$ percent change in $Y$.

For example, if:
$\hat{\beta}=-0.50$
in a regression of log quantity demanded on log price, then a $1\%$ increase in price is associated with a $0.5\%$ decrease in quantity demanded. A semi-elasticity occurs when one variable is logged and the other is not. If the outcome is logged:
$\log(Y_i)=\alpha+\beta X_i+u_i$ then a one-unit increase in $X$ is associated with an approximate $100\beta$ percent change in $Y$. If the explanatory variable is logged:
$Y_i=\alpha+\beta \log(X_i)+u_i$ then a $1\%$ increase in $X$ is associated with an approximate change of:
$\frac{\beta}{100}$
units of $Y$. Elasticities are useful because they are scale-free. They allow comparison across contexts where variables have different units or baseline levels. However, elasticities can hide absolute magnitudes. A large elasticity applied to a small baseline may imply a small absolute effect. A small elasticity applied to a huge baseline may imply a large absolute effect.

---

## 17.6 Standardized effect sizes
Some outcomes do not have intuitive natural units. For example:
- test scores
- psychological scales
- health indices
- neighborhood quality indices
- management quality scores
- cognitive assessments
- composite poverty measures

In such cases, researchers often report standardized effect sizes. A standardized effect expresses the effect in units of the outcome's standard deviation. If the estimated effect is:
$\widehat{ATE}$ and the standard deviation of the outcome is:
$s_Y$ then the standardized effect size is:
$\frac{\widehat{ATE}}{s_Y}$ For example, if a tutoring program increases test scores by $8$ points and the standard deviation of test scores is $40$ points, then the standardized effect is:
$\frac{8}{40}=0.20$
The effect is $0.20$ standard deviations. Standardized effects are useful for comparing effects across studies and outcomes. But they also have limitations. First, standard deviations depend on the population. A $0.20$ standard deviation effect may correspond to different raw score gains in different samples. Second, standardized effects may be less intuitive for policy audiences. Saying a tutoring program raises test scores by $0.20$ standard deviations may be statistically convenient, but policymakers may also want to know what that means in points, grade levels, graduation rates, or earnings. Third, a standardized effect can look small but still be important if the outcome is consequential and the intervention is cheap. Fourth, standardized effects can look large if the outcome has little variation in the sample. Whenever possible, report both natural units and standardized units.

---

## 17.7 Statistical significance
Statistical significance asks whether an estimate is sufficiently far from a null hypothesis relative to its estimated sampling uncertainty. A common null hypothesis is:
$H_0:\theta=0$ where $\theta$ is the parameter of interest. Suppose we estimate:
$\hat{\theta}$ with standard error:
$SE(\hat{\theta})$ A common test statistic is:
$t = \frac{\hat{\theta}-0}{SE(\hat{\theta})}$
If the absolute value of $t$ is large enough, we reject the null hypothesis at a chosen significance level. For example, with large samples, a two-sided test at the $5\%$ significance level often rejects when:
$|t| > 1.96$ Statistical significance means that the estimate is unlikely to be observed if the null hypothesis were true, given the model and assumptions used to compute the standard error. It does not mean:
- the estimate is causal
- the effect is large
- the effect is important
- the estimate is unbiased
- the model is correct
- the finding will replicate
- the policy is worth implementing

A biased estimate can be statistically significant. A trivial effect can be statistically significant. A non-causal association can be statistically significant. Statistical significance is about precision relative to a benchmark. It is not a substitute for research design, interpretation, or judgment.

---

## 17.8 Economic significance and practical significance
Economic significance asks whether an effect is meaningful in economic or policy terms. Practical significance asks whether an effect matters in the real world. These concepts are related but not identical. An effect can be statistically significant but economically small. Example: A massive dataset estimates that a policy increases annual earnings by:
$\hat{\theta}=12$
dollars per year, with a very small standard error. The estimate may be statistically significant, but \$12 per year may be economically trivial. An effect can also be statistically insignificant but economically important. Example: A small randomized trial estimates that a program increases annual earnings by:
$\hat{\theta}=2{,}500$ with a 95 percent confidence interval:
$[-500,\ 5{,}500]$
The estimate may not be statistically significant at the $5\%$ level, but the range includes effects large enough to matter for policy. Economic significance depends on context. A $1$ percentage point increase in employment may be large if applied to millions of workers. A $1$ percentage point reduction in mortality may be enormous. A $0.05$ standard deviation increase in test scores may matter if the intervention is extremely cheap and scalable. To evaluate economic significance, ask:
1. How large is the effect relative to the baseline?
2. How many people are affected?
3. How persistent is the effect?
4. What is the cost of producing the effect?
5. Are there spillovers or indirect effects?
6. Does the effect occur for a high-priority population?
7. Are there distributional consequences?
8. How does the effect compare with alternative policies?

The central point is:

> Statistical significance is not policy significance.

---

## 17.9 Standard errors
A standard error measures the sampling variability of an estimator. If we repeatedly drew samples from the same population and estimated the same parameter, the estimate would vary across samples. The standard error measures the typical size of that variation. For an estimator $\hat{\theta}$, the standard error is:
$SE(\hat{\theta})$ A smaller standard error means the estimate is more precise. A larger standard error means the estimate is less precise. Standard errors depend on:
- sample size
- outcome variability
- treatment variation
- research design
- clustering
- serial correlation
- heteroskedasticity
- model specification
- strength of instruments
- bandwidth choices in RD
- number of treated units
- number of clusters
- effective sample size

In a simple difference in means with independent observations, the standard error is often:

$$
SE(\bar{Y}_1-\bar{Y}_0)
=
\sqrt{
\frac{s_1^2}{n_1}
+
\frac{s_0^2}{n_0}
}
$$

where:
- $s_1^2$ is the sample variance in the treated group
- $s_0^2$ is the sample variance in the control group
- $n_1$ is the number of treated observations
- $n_0$ is the number of control observations

The standard error falls as sample size increases, but it rises when outcomes are more variable. In applied economics, correct standard errors are often as important as point estimates. Incorrect standard errors can make an estimate appear more precise than it really is.

---

## 17.10 Confidence intervals
A confidence interval gives a range of parameter values that are compatible with the data under a statistical procedure. A common approximate 95 percent confidence interval is:
$\hat{\theta} \pm 1.96 \cdot SE(\hat{\theta})$ For example, suppose:
$\hat{\theta}=2{,}000$ and:
$SE(\hat{\theta})=500$ Then an approximate 95 percent confidence interval is:
$2{,}000 \pm 1.96(500)$ or:
$[1{,}020,\ 2{,}980]$
This interval suggests that the data are consistent with effects between about \$1,020 and \$2,980, under the model and assumptions. A confidence interval is often more informative than a p-value because it shows both direction and magnitude. For example, a confidence interval:
$[0.01,\ 0.02]$ may be statistically significant but substantively tiny. A confidence interval:
$[-0.05,\ 0.50]$ may not be statistically significant but includes large positive effects. A confidence interval:
$[-0.50,\ 0.50]$ indicates great uncertainty. A confidence interval:
$[-0.02,\ 0.02]$ suggests the effect is probably small, even if not exactly zero. Confidence intervals help researchers avoid binary thinking. Instead of asking only whether an effect is significant, ask:

> What range of effect sizes is plausible?

---

## 17.11 P-values
A p-value is the probability, under the null hypothesis and statistical model, of obtaining a test statistic at least as extreme as the one observed. If the null hypothesis is:
$H_0:\theta=0$ then the p-value measures how surprising the estimate is if the true effect were zero. A small p-value means the estimate would be unlikely under the null hypothesis. But a p-value is often misinterpreted. A p-value is not:
- the probability that the null hypothesis is true
- the probability that the estimated effect is due to chance
- the probability that the result will replicate
- the probability that the causal claim is valid
- a measure of effect size
- a measure of policy importance

A p-value depends on both effect size and precision. With a huge sample, a tiny effect can produce a small p-value. With a small sample, a large effect can produce a large p-value. For policy analysis, p-values should be interpreted alongside effect sizes, confidence intervals, design credibility, prior evidence, costs, and decision risks.

---

## 17.12 Precision versus bias
A precise estimate is not necessarily a correct estimate. Precision refers to sampling variability. Bias refers to systematic error. An estimator is biased if, on average, it does not equal the target parameter:
$Bias(\hat{\theta}) = \mathbb{E}[\hat{\theta}] - \theta$ An estimate can be:
1. precise and unbiased,
2. imprecise and unbiased,
3. precise and biased,
4. imprecise and biased.

The dangerous case is a precise but biased estimate. For example, suppose a large observational dataset estimates the effect of education on wages with tiny standard errors. If education is endogenous because of ability bias, the estimate may be very precise but not causal. A large sample does not solve confounding. More data can reduce variance, but it does not automatically reduce bias. This distinction is central:

> Standard errors quantify uncertainty from sampling. They do not quantify all uncertainty from identification failure, bad measurement, invalid assumptions, or poor research design.

Researchers often report robustness checks and sensitivity analyses to address uncertainty beyond sampling variability.

---

## 17.13 Sampling uncertainty versus design uncertainty
Statistical uncertainty is usually reported through standard errors and confidence intervals. But empirical economics also involves design uncertainty. Sampling uncertainty asks:

> How much would the estimate vary across repeated samples?

Design uncertainty asks:

> How credible is the research design and identifying assumption?

For example, in difference-in-differences, the standard error may be small. But if the parallel trends assumption is implausible, the estimate may still not be credible. In instrumental variables, the confidence interval may be narrow. But if the exclusion restriction fails, the estimate may be biased. In regression discontinuity, the estimate may be precise near the cutoff. But if units manipulate the running variable, the design may fail. In matching, the estimate may be precise. But if selection on unobservables remains, the estimate may not be causal. Design uncertainty is harder to summarize in a single number. It is addressed through:
- institutional knowledge
- balance tests
- pre-trend checks
- placebo tests
- falsification tests
- sensitivity analysis
- alternative comparison groups
- robustness to specifications
- transparent discussion of threats
- triangulation across designs

A good empirical paper does not only report standard errors. It also argues that the design identifies the intended causal effect.

---

## 17.14 Clustering and dependence
Many datasets contain observations that are not independent. Examples:
- students within schools
- workers within firms
- patients within hospitals
- individuals within neighborhoods
- counties within states
- repeated observations over time
- firms within industries
- households within villages

If observations within a group share shocks, then treating them as independent can understate standard errors. For example, if a policy is assigned at the state level but outcomes are measured for individuals, the relevant independent variation may be at the state level, not the individual level. Suppose a state-level policy affects all individuals in a state. If we have thousands of individuals per state, a naive standard error may act as though there are thousands of independent policy observations. But the policy varies only across states. This can make estimates appear much more precise than they are. Clustered standard errors allow arbitrary correlation of errors within clusters. A typical panel regression might be:
$Y_{it} = \alpha_i + \lambda_t + \beta D_{it} + u_{it}$
If treatment varies at the unit level over time, researchers may cluster by unit to allow serial correlation in $u_{it}$ within units. In difference-in-differences with state-level policy variation, researchers often cluster at the state level. The general rule is:

> Standard errors should reflect the level at which treatment varies and the dependence structure in the data.

Clustering is not only a technical detail. It can change whether estimates appear precise or uncertain.

---

## 17.15 Serial correlation
Serial correlation occurs when errors are correlated over time. In panel or time-series settings, outcomes often persist. A county with high unemployment this year is likely to have high unemployment next year. A firm with high productivity this year is likely to have high productivity next year. If errors are serially correlated, naive standard errors may be too small. Consider:
$Y_{it} = \alpha_i + \lambda_t + \beta D_{it} + u_{it}$ Serial correlation means:
$\operatorname{Cov}(u_{it},u_{is}) \neq 0$
for different time periods $t$ and $s$. This is especially important in difference-in-differences because policies often change at the group level and outcomes are persistent over time. If a policy turns on and stays on, the treatment variable is also serially correlated. Ignoring serial correlation can lead researchers to overstate precision. Common responses include:
- clustering standard errors by unit
- using block bootstrap methods
- aggregating data to the level of treatment variation
- using randomization inference
- modeling serial correlation directly
- conducting placebo policy timing tests

The main idea is that repeated observations over time are not automatically independent.

---

## 17.16 Power and minimum detectable effects
Statistical power is the probability of detecting an effect if the effect truly exists. If $\beta$ denotes the probability of a Type 2 error, then power is:
$1-\beta$ A study with low power may fail to detect meaningful effects. Power depends on:
- sample size
- effect size
- outcome variance
- treatment share
- research design
- clustering
- compliance rates
- significance level
- baseline covariates
- measurement quality

A minimum detectable effect, or MDE, is the smallest effect size a study is likely to detect with a chosen level of power. For example, a study may be designed to have $80\%$ power to detect an earnings effect of at least \$1,500 per year. If the true effect is \$500, the study may be unlikely to detect it. Power matters for both planning and interpretation. Before a study, power analysis helps determine whether the design can answer the question. After a study, power affects how we interpret statistically insignificant results. A statistically insignificant result from a low-powered study does not prove there is no effect. It may simply mean the study was too small or noisy to detect the effect. A useful question is:

> What effect sizes can this study rule out?

If a confidence interval is narrow around zero, the study may rule out large effects. If the confidence interval is wide, the study may be inconclusive.

---

## 17.17 Multiple testing and false discoveries
When researchers test many hypotheses, some statistically significant results will appear by chance. Suppose a program has no true effect on any outcome, but researchers test $100$ independent outcomes at the $5\%$ significance level. Even if all null hypotheses are true, we expect about:
$100 \times 0.05 = 5$ statistically significant results by chance. Multiple testing arises when researchers examine:
- many outcomes
- many subgroups
- many time horizons
- many treatment definitions
- many model specifications
- many samples
- many transformations
- many interaction terms

Multiple testing increases the risk of false positives. Common responses include:
- pre-analysis plans
- preregistration
- distinguishing primary from secondary outcomes
- Bonferroni correction
- Holm correction
- false discovery rate control
- family-wise error rate control
- reporting all tested outcomes
- replication in independent samples

The issue is not that exploratory analysis is forbidden. Exploration can be valuable. But readers should know whether a result was predicted in advance or discovered after searching through many possible results. A finding discovered through extensive specification search is less credible than the same finding predicted before seeing the data.

---

## 17.18 Robustness and sensitivity analysis
Robustness analysis asks whether results change under reasonable alternative choices. Examples include changing:
- control variables
- sample restrictions
- functional forms
- bandwidths in RD
- comparison groups in DiD
- clustering level
- outcome definitions
- treatment definitions
- time windows
- weighting schemes
- fixed effects
- data sources

A robust result is not one that never changes. Some changes are expected. A robust result is one whose core interpretation survives reasonable alternatives. Sensitivity analysis asks how strong a violation of assumptions would need to be to change the conclusion. For example:
- How strong would unobserved confounding need to be to explain away the estimate?
- How much differential attrition would overturn the result?
- How large would spillovers need to be?
- How much manipulation around the RD cutoff would matter?
- How severe would selection on unobservables have to be?

Robustness checks should not be used mechanically. A long list of checks does not guarantee credibility. The checks should target the main threats to the research design. Good robustness analysis is guided by a clear question:

> What would make this estimate wrong?

---

## 17.19 Interpreting zero and near-zero effects
A near-zero estimate can mean several things. It may mean:
1. the true effect is zero,
2. the effect is small,
3. positive and negative effects cancel out,
4. the effect appears only for certain subgroups,
5. the effect occurs later than measured,
6. the treatment was poorly implemented,
7. the treatment contrast was weak,
8. the study was underpowered,
9. measurement error attenuated the estimate,
10. the research design is invalid.

For example, a job training program may have an average effect near zero because it helps young workers but harms older workers. A tutoring program may show no effect after one semester but positive effects after two years. A policy may show no effect because it was not actually enforced. Therefore, a null estimate should be interpreted carefully. Ask:
    - Is the confidence interval narrow enough to rule out meaningful effects?
    - Was treatment actually implemented?
    - Was take-up high?
    - Was the outcome measured at the right time?
    - Could effects be heterogeneous?
    - Could measurement error attenuate the estimate?
    - Is the research design credible?
    - Is the sample large enough?

    "Not statistically significant" does not automatically mean "no effect."

---

## 17.20 Interpreting large effects
Large estimated effects also require scrutiny. A very large estimate may reflect a genuinely large effect. But it may also indicate:
- omitted variable bias
- selection bias
- weak instruments
- small samples
- outliers
- measurement error
- publication bias
- model extrapolation
- functional form problems
- invalid comparison groups
- p-hacking
- bad standard errors

For example, a weak instrument can produce implausibly large IV estimates with wide confidence intervals. A regression discontinuity estimate can be sensitive to outliers near the cutoff. A difference-in-differences estimate can be large because treated and control groups had diverging pre-trends. Large estimates should be compared to:
- baseline outcome levels
- estimates from related studies
- plausible mechanisms
- implementation intensity
- cost of treatment
- known behavioral responses
- historical evidence

An estimate should be large enough to matter but not so large that it is mechanically implausible without explanation.

---

## 17.21 Effect sizes in common empirical designs
Different research designs produce effect sizes with different interpretations.
- **Randomized controlled trials.**
In a simple RCT with full compliance, the difference in means estimates:
$ATE = \mathbb{E}[Y_i(1)-Y_i(0)]$ for the experimental sample. If there is noncompliance, the difference by assignment estimates an intent-to-treat effect:
$ITT = \mathbb{E}[Y_i \mid Z_i=1]-\mathbb{E}[Y_i \mid Z_i=0]$ where $Z_i$ is assignment. The ITT may be smaller than the effect of actually receiving treatment if not everyone assigned to treatment takes it up.
- **Instrumental variables.**
IV often estimates a local average treatment effect:
$LATE = \mathbb{E}[Y_i(1)-Y_i(0) \mid \text{complier}]$
The magnitude applies to compliers, not necessarily to everyone. A large IV estimate may be plausible if compliers benefit more than the average person. But it may also indicate weak instruments or exclusion restriction violations.
- **Difference-in-differences.**
DiD estimates the difference between the treated group's change and the control group's change:

$$
\widehat{\beta}_{DiD}
=
(\bar{Y}_{T,After}-\bar{Y}_{T,Before})
-
(\bar{Y}_{C,After}-\bar{Y}_{C,Before})
$$

The effect is meaningful only under the parallel trends assumption. The magnitude should be interpreted relative to pre-treatment levels, trends, and the timing of treatment.
- **Regression discontinuity.**
RD estimates a local effect at the cutoff:

$$
\tau_{RD}
=
\lim_{x \downarrow c}\mathbb{E}[Y_i \mid X_i=x]
-
\lim_{x \uparrow c}\mathbb{E}[Y_i \mid X_i=x]
$$

The magnitude applies to units near the cutoff. It may not generalize to units far from the cutoff.
- **Fixed effects.**
Fixed effects estimates are identified from within-unit changes:
$Y_{it} = \alpha_i + \lambda_t + \beta D_{it} + u_{it}$ The effect size reflects changes in outcomes when the same unit changes treatment status, net of fixed effects. It may differ from a cross-sectional effect. The key point is:

> The numerical magnitude of an estimate cannot be interpreted separately from the estimand and the source of identifying variation.

---

## 17.22 Communicating effect sizes
Good empirical writing translates estimates into meaningful language. Instead of writing only:

> The coefficient is $0.037$.

write:

> The estimate implies a $3.7$ percentage point increase in employment, relative to a control-group mean of $62\%$. This is about a $6.0\%$ increase relative to baseline.

Instead of writing:

> The treatment effect is $0.18$ standard deviations.

write:

> The program increased test scores by $0.18$ standard deviations, equivalent to about $7$ points on the exam. This is roughly one-third of the achievement gap between low-income and high-income students in the sample.

Instead of writing:

> The log earnings coefficient is $0.09$.

write:

> The estimate implies approximately a $9\%$ increase in earnings. At the control-group mean of \$35,000, this corresponds to about \$3,150 per year.

Good interpretation often includes:
1. the coefficient,
2. the unit,
3. the baseline mean,
4. the percent change relative to baseline,
5. the confidence interval,
6. the relevant population,
7. the time horizon,
8. whether the magnitude is economically meaningful.

Example:

> The estimated effect of the training offer on annual earnings is \$1,200, with a 95 percent confidence interval from \$300 to \$2,100. Relative to the control-group mean of \$30,000, this is a $4\%$ increase. Because the program costs \$900 per participant, the earnings gain is economically meaningful if it persists for more than one year.

This kind of interpretation connects statistical output to substantive meaning.

---

## 17.23 Practical example: tutoring and test scores
Suppose a randomized tutoring program estimates:
$\widehat{ATE}=0.20$ standard deviations on a math test, with standard error:
$SE=0.05$ The t-statistic is:
$t=\frac{0.20}{0.05}=4$ The estimate is statistically significant at conventional levels. A 95 percent confidence interval is approximately:
$0.20 \pm 1.96(0.05)$ or:
$[0.102,\ 0.298]$
This suggests the effect is likely positive and between about $0.10$ and $0.30$ standard deviations. But interpretation should go further. Suppose the test score standard deviation is $50$ points. Then the raw point effect is:
$0.20 \times 50 = 10$ points. If the control-group mean is $300$ points, the effect is:
$\frac{10}{300}=0.033$ or about $3.3\%$ of the baseline mean. If the achievement gap between low-income and high-income students is $40$ points, then the effect closes:
$\frac{10}{40}=0.25$
or $25\%$ of the gap. If the tutoring program costs \$500 per student, the policy interpretation depends on whether a 10-point gain is worth that cost compared with alternatives. The full interpretation requires effect size, uncertainty, baseline context, distributional context, and cost.

---

## 17.24 Practical example: minimum wage and employment
Suppose a difference-in-differences study estimates that a minimum wage increase changes employment by:
$\hat{\beta}=-0.015$ where employment is measured as a share of the working-age population. This is a $1.5$ percentage point decline. If the baseline employment rate is $60\%$, the relative decline is:
$\frac{0.015}{0.60}=0.025$ or $2.5\%$. If the standard error is:
$SE=0.010$ then the t-statistic is:
$t=\frac{-0.015}{0.010}=-1.5$ The estimate is not statistically significant at the conventional $5\%$ level. The approximate 95 percent confidence interval is:
$-0.015 \pm 1.96(0.010)$ or:
$[-0.0346,\ 0.0046]$ This means the data are consistent with an employment decline of up to about $3.5$ percentage points, a very small decline, no effect, or a small increase. A careful interpretation would not say:

> The minimum wage had no effect.

It would say:

> The estimate is negative but imprecise. The confidence interval includes economically meaningful employment losses as well as small positive effects. The study does not provide strong evidence of a precise effect in either direction.

Then one would evaluate whether the DiD design is credible: Are pre-trends parallel? Was there anticipation? Were there other simultaneous policy changes? Are standard errors clustered appropriately? Are effects heterogeneous by sector or worker group?

---

## 17.25 Practical example: job training and earnings
Suppose an RCT estimates that a job training program increases annual earnings by:
$\widehat{ITT}=1{,}000$ with standard error:
$SE=600$ The 95 percent confidence interval is:
$1{,}000 \pm 1.96(600)$ or approximately:
$[-176,\ 2{,}176]$
The result is not statistically significant at the $5\%$ level. But the estimate may still be meaningful. If the program costs \$400 per participant, even an effect of \$1,000 could be economically important. If the effect persists for multiple years, the benefit may exceed the cost. If the effect fades quickly, it may not. Now suppose only half of those assigned to training actually participate. The ITT effect is the effect of being offered training, not the effect of actually receiving training. If assignment increases participation by $0.50$, then a treatment-on-the-treated estimate may be:
$\widehat{TOT} = \frac{\widehat{ITT}}{0.50}$ or:
$\widehat{TOT}=2{,}000$
This estimate applies to the effect of participation under assumptions similar to IV. It may be more relevant for understanding the program's effect on compliers, but it will also be less precise. The interpretation depends on the estimand.

---

**Common mistakes.**
1. **Equating statistical significance with importance:** A result can be statistically significant and practically irrelevant. Always ask whether the magnitude matters.
2. **Treating non-significance as proof of no effect:** Failure to reject the null is not proof that the effect is zero. Look at the confidence interval and power.
3. **Ignoring units:** A coefficient has no meaning without units. Always identify the units of the outcome and treatment.
4. **Confusing percent and percentage points:** A change from $10\%$ to $15\%$ is a $5$ percentage point increase, not a $5\%$ increase. The percent increase is:
$\frac{15-10}{10}=50\%$
5. **Ignoring the baseline:** A \$1,000 increase in earnings means different things depending on whether baseline earnings are \$10,000 or \$100,000.
6. **Ignoring uncertainty:** Point estimates should be interpreted with standard errors, confidence intervals, or other uncertainty measures.
7. **Ignoring identification:** Precise estimates are not useful if the research design is not credible.
8. **Overinterpreting standardized effects:** Standard deviations help comparison, but they can obscure real-world meaning. Translate standardized effects into natural units when possible.
9. **Comparing estimates with different estimands:** An RCT estimate of ATE, an IV estimate of LATE, an RD estimate at a cutoff, and a DiD estimate for treated units may not be directly comparable.
10. **Ignoring multiple testing:** If many outcomes or subgroups were tested, significant findings may be false positives.

---

**Application checklist.**
When interpreting an empirical estimate, use the following checklist.
1. **Identify the estimand:** What causal effect is being estimated? Examples:
    - ATE
    - ATT
    - LATE
    - CATE
    - ITT
    - TOT
    - local RD effect
    - dynamic effect
2. **Identify the units:** What is the unit of the outcome? What is the unit of the treatment? Is the coefficient in levels, logs, percentages, percentage points, or standard deviations?
3. **Translate the coefficient:** Convert the estimate into plain language. If the outcome is logged, convert to percent terms. If the effect is standardized, translate into raw units if possible.
4. **Compare to the baseline:** What is the control-group mean or pre-treatment mean? How large is the effect relative to baseline?
5. **Report uncertainty:** What is the standard error? What is the confidence interval? What range of effects is compatible with the data?
6. **Evaluate statistical significance:** Is the estimate distinguishable from zero or another relevant benchmark? Avoid treating significance as the only criterion.
7. **Evaluate economic significance:** Is the effect large enough to matter? Does it justify the cost? How many people are affected? Does it persist?
8. **Check precision versus bias:** Is the estimate precise? Is the design credible? Could the estimate be precisely wrong?
9. **Check dependence and clustering:** Are standard errors appropriate for the design? At what level does treatment vary? Are observations independent?
10. **Consider heterogeneity:** Does the average effect hide differences across groups? Are subgroup effects credible or exploratory?
11. **Consider multiple testing:** Were many outcomes, groups, or specifications tested? Were primary hypotheses specified in advance?
12. **Interpret in context:** How does the effect compare with other studies? Is the mechanism plausible? Does the estimate generalize? What are the main limitations?

---

## 17.26 Summary
Effect size is about magnitude. It tells us how large an estimated relationship or causal effect is. Statistical significance is about whether an estimate is large relative to its sampling uncertainty. Economic significance is about whether the effect matters in real-world or policy terms. Uncertainty is about the range of values compatible with the data and design. A complete empirical interpretation requires all of these. A point estimate should be interpreted alongside:
- units
- baseline levels
- standard errors
- confidence intervals
- p-values
- research design
- identifying assumptions
- clustering and dependence
- power
- multiple testing concerns
- heterogeneity
- costs and benefits
- external validity

The central lesson is:

> An empirical estimate is not fully understood until we know what it measures, how large it is, how uncertain it is, whether it is causally credible, and whether it matters for the decision at hand.

Good empirical economics does not stop at "significant" or "not significant." It asks:

> How big is the effect, how credible is it, how uncertain is it, who does it apply to, and is it important enough to change what we believe or do?

# 18. Type 1 and Type 2 Errors, Power, Multiple Testing, and Bayesian Evidence
## 18.1 Why hypothesis testing matters in empirical economics
Empirical researchers rarely observe causal effects with certainty. They estimate effects using samples, and samples contain noise. Even if a research design is internally valid, the estimated effect may differ from the true effect because of sampling variation, measurement error, finite sample size, or random assignment imbalance. This means empirical analysis involves uncertainty. A researcher may estimate that a policy increased employment, improved test scores, reduced crime, or raised earnings. But the estimate alone does not answer every relevant question. We also need to ask:
- How much uncertainty surrounds the estimate?
- Could the estimated effect be due to sampling variation?
- What is the probability of detecting an effect if one exists?
- What kinds of mistakes can we make when interpreting the evidence?
- How should we think about many tests conducted at once?
- How should evidence change our beliefs?

Hypothesis testing is one framework for making decisions under uncertainty. The basic idea is that we begin with a null hypothesis, usually representing no effect or no difference, and ask whether the data provide enough evidence against it. For example, suppose we estimate the effect of a job training program on annual earnings:
$Y_i = \alpha + \beta D_i + u_i$ where $Y_i$ is earnings and $D_i$ indicates participation in the program. A common null hypothesis is:
$H_0: \beta = 0$ This says the program has no effect on earnings. The alternative hypothesis may be two-sided:
$H_1: \beta \neq 0$ or one-sided:
$H_1: \beta > 0$
A two-sided alternative asks whether the effect is different from zero in either direction. A one-sided alternative asks whether the effect is positive. The researcher then uses an estimate $\hat{\beta}$ and its standard error to decide whether the data are sufficiently inconsistent with the null hypothesis. This decision can be wrong in two main ways: a Type 1 error or a Type 2 error.

---

## 18.2 The null hypothesis and alternative hypothesis
A hypothesis test begins by defining two competing claims. The **null hypothesis**, denoted $H_0$, is the benchmark claim being tested. In empirical economics, it often says there is no effect:
$H_0: \beta = 0$ The **alternative hypothesis**, denoted $H_1$ or $H_A$, is the claim considered if the null is rejected:
$H_1: \beta \neq 0$
The null and alternative hypotheses should be defined before looking at the results. If researchers choose hypotheses after seeing the data, statistical inference becomes less credible because the test no longer reflects a pre-specified decision rule. Hypotheses can be about regression coefficients, treatment effects, differences in means, distributional changes, or model restrictions. Examples:
- **Minimum wage and employment.**
Null hypothesis:
$H_0: \text{The minimum wage increase has no effect on employment.}$ Alternative hypothesis:
$H_1: \text{The minimum wage increase changes employment.}$
- **Tutoring and test scores.**
Null hypothesis:
$H_0: \text{Tutoring has no effect on test scores.}$ Alternative hypothesis:
$H_1: \text{Tutoring improves test scores.}$
- **Pollution and health.**
Null hypothesis:
$H_0: \text{Pollution exposure has no effect on respiratory illness.}$ Alternative hypothesis:
$H_1: \text{Pollution exposure affects respiratory illness.}$
The null hypothesis is not necessarily what the researcher believes. It is a reference point for evaluating statistical evidence. A failure to reject the null does not prove the null is true. It only means the data did not provide enough evidence to reject it under the chosen test.

---

## 18.3 Type 1 error: false positive
A **Type 1 error** occurs when the researcher rejects the null hypothesis even though the null hypothesis is true. In plain language, it is a false positive. For example:
- A researcher concludes that a job training program increases earnings when it actually has no effect
- A study concludes that a tutoring program improves test scores when the true effect is zero
- A paper finds that a policy reduces crime when the apparent effect is only sampling noise

If the null hypothesis is:
$H_0: \beta = 0$ then a Type 1 error occurs when the researcher concludes:
$\beta \neq 0$ when in reality:
$\beta = 0$ The probability of a Type 1 error is denoted by $\alpha$. Common choices are:
$\alpha = 0.10$
$\alpha = 0.05$
$\alpha = 0.01$
The most common convention is $\alpha = 0.05$. This means that if the null hypothesis is true and the test is repeated many times under the same conditions, the researcher would incorrectly reject the null about 5 percent of the time. It does **not** mean there is a 5 percent probability that the null hypothesis is true. That is a common misunderstanding. The significance level controls the long-run probability of false rejection under the null. It does not directly give the posterior probability that the hypothesis is true or false.

---

## 18.4 Type 2 error: false negative
A **Type 2 error** occurs when the researcher fails to reject the null hypothesis even though the null hypothesis is false. In plain language, it is a false negative. For example:
- A researcher concludes that a job training program has no detectable effect even though it truly raises earnings
- A study fails to find an effect of tutoring even though tutoring genuinely improves learning
- A policy evaluation finds no statistically significant effect of pollution exposure even though pollution harms health

If the null hypothesis is:
$H_0: \beta = 0$ then a Type 2 error occurs when the researcher fails to reject $H_0$ even though:
$\beta \neq 0$
The probability of a Type 2 error is usually denoted by $\beta_{II}$ or simply $\beta$ in hypothesis testing contexts. Because $\beta$ is also commonly used as a regression coefficient, it is useful to be clear from context. The probability of correctly rejecting a false null is called **statistical power**:
$Power = 1 - \beta_{II}$
Power is the probability that a test detects an effect if the effect truly exists. A low-powered study may fail to find statistically significant effects even when effects are substantively important. This is crucial in empirical economics. A statistically insignificant estimate does not necessarily mean there is no effect. It may mean the study lacks enough information to distinguish the effect from noise.

---

## 18.5 The hypothesis testing decision table
The two types of errors can be summarized in a decision table.

| Reality | Researcher rejects $H_0$ | Researcher fails to reject $H_0$ |
|---|---:|---:|
| $H_0$ is true | Type 1 error | Correct non-rejection |
| $H_0$ is false | Correct rejection | Type 2 error |

Equivalently:

| Reality | Test says effect exists | Test does not find effect |
|---|---:|---:|
| No true effect | False positive | True negative |
| True effect | True positive | False negative |

This table makes clear that statistical testing is not about proving truth with certainty. It is about using a rule that has known error properties under repeated sampling. Both types of errors matter. Which error is more costly depends on the context.
- **When Type 1 errors are especially costly.**
Type 1 errors are especially costly when false positives lead to harmful actions. Examples:
- Implementing an expensive policy that does not work
- Approving a treatment that has no benefit and possible side effects
- Scaling an education program that wastes scarce public funds
- Concluding that a company discriminated when the evidence is actually noise
- **When Type 2 errors are especially costly.**
Type 2 errors are especially costly when false negatives prevent beneficial action. Examples:
- Failing to adopt a program that genuinely reduces mortality
- Ignoring a harmful pollutant because the study was underpowered
- Rejecting a tutoring intervention that helps disadvantaged students
- Missing early evidence of a financial risk

There is often a tradeoff. Lowering the probability of Type 1 errors can increase the probability of Type 2 errors, unless the sample size or information quality increases.

---

## 18.6 Significance levels and critical values
A hypothesis test requires a decision rule. For a two-sided test of:
$H_0: \beta = 0$ we often compute a test statistic:
$t = \frac{\hat{\beta} - 0}{SE(\hat{\beta})}$
where $SE(\hat{\beta})$ is the standard error of the estimate. Under suitable conditions, the test statistic follows approximately a standard normal distribution or a $t$ distribution under the null. At the 5 percent significance level in a large sample, a common two-sided critical value is approximately:
$1.96$ The rule is:
$\text{Reject } H_0 \text{ if } |t| > 1.96$ Equivalently, reject if the p-value is less than 0.05. At the 1 percent level, the large-sample two-sided critical value is approximately:
$2.58$ At the 10 percent level, it is approximately:
$1.64$
These thresholds are conventions. They are not laws of nature. A result with $p=0.049$ is not fundamentally different from a result with $p=0.051$. Treating one as a discovery and the other as no evidence is often misleading. Good empirical interpretation should consider the estimate, standard error, confidence interval, research design, prior evidence, and practical importance, not only whether the p-value crosses a threshold.

---

## 18.7 P-values
A **p-value** is the probability, under the null hypothesis, of obtaining a test statistic at least as extreme as the one observed. For a two-sided test, the p-value is:
$p = P(|T| \geq |t_{obs}| \mid H_0)$
where $t_{obs}$ is the observed test statistic. A small p-value means that the observed estimate would be unlikely if the null hypothesis were true, under the assumptions of the test. For example, a p-value of 0.03 means:

> If the null hypothesis were true, a result this extreme or more extreme would occur with probability 0.03 under the test's assumptions.

It does not mean:

> There is a 3 percent probability that the null hypothesis is true.

It also does not mean:

> There is a 97 percent probability that the alternative hypothesis is true.

Those statements require Bayesian reasoning and prior probabilities. Common misinterpretations of p-values include:
1. interpreting the p-value as the probability the null is true,
2. interpreting statistical significance as proof of causality,
3. interpreting non-significance as proof of no effect,
4. treating $p < 0.05$ as a bright line between true and false,
5. ignoring effect size and uncertainty intervals,
6. ignoring the number of tests conducted.

A p-value is one piece of evidence. It should not be the entire empirical argument.

---

## 18.8 Confidence intervals and hypothesis tests
Confidence intervals and hypothesis tests are closely related. A 95 percent confidence interval for $\beta$ is often written as:
$\hat{\beta} \pm 1.96 \times SE(\hat{\beta})$ in large samples. If the 95 percent confidence interval excludes zero, then a two-sided test of:
$H_0: \beta = 0$ will reject at the 5 percent level. If the interval includes zero, the test will not reject at the 5 percent level. For example, suppose:
$\hat{\beta} = 500$ and:
$SE(\hat{\beta}) = 200$ Then the approximate 95 percent confidence interval is:
$500 \pm 1.96(200)$
$500 \pm 392$
$[108, 892]$ This interval excludes zero, so the estimate is statistically significant at the 5 percent level. Now suppose:
$\hat{\beta} = 500$ and:
$SE(\hat{\beta}) = 400$ The approximate 95 percent confidence interval is:
$500 \pm 1.96(400)$
$500 \pm 784$
$[-284, 1284]$
This interval includes zero, so the estimate is not statistically significant at the 5 percent level. But notice that the point estimate is the same in both cases. The difference is uncertainty. This is why confidence intervals are often more informative than binary significant/not-significant labels. They show the range of effect sizes compatible with the data and model.

---

## 18.9 Statistical power
Statistical power is the probability that a test rejects the null hypothesis when the alternative is true. Formally:
$Power = P(\text{Reject } H_0 \mid H_1 \text{ is true})$ If $\beta_{II}$ is the probability of a Type 2 error, then:
$Power = 1 - \beta_{II}$ Power depends on several factors.
- **1. True effect size.**
Larger true effects are easier to detect. A program that raises earnings by \$5{,}000 is easier to detect than a program that raises earnings by \$50, all else equal.
- **2. Sample size.**
Larger samples generally increase power because they reduce standard errors. For many simple estimators:
$SE(\hat{\beta}) \propto \frac{1}{\sqrt{n}}$ where $n$ is sample size. This means that quadrupling the sample size roughly halves the standard error.
- **3. Outcome variability.**
Noisy outcomes reduce power. If earnings vary greatly across workers for reasons unrelated to treatment, it is harder to detect the effect of a job training program.
- **4. Treatment variation.**
More variation in treatment improves precision. In experiments, power is affected by the share assigned to treatment and control. Balanced assignment often improves power for a fixed total sample size.
- **5. Research design.**
Some designs are less statistically powerful than others. Cluster randomized trials often have less power than individual randomized trials because observations within clusters are correlated. Regression discontinuity designs may have less power because identification comes from observations near the cutoff. Instrumental variables estimates may be imprecise when the instrument weakly predicts treatment.
- **6. Significance threshold.**
A stricter significance threshold lowers Type 1 errors but also lowers power. For example, requiring $p < 0.01$ instead of $p < 0.05$ makes it harder to reject the null.

---

## 18.10 Minimum detectable effects
The **minimum detectable effect**, or MDE, is the smallest true effect that a study is likely to detect with a given level of power. Power calculations often ask:

> Given the sample size, outcome variability, and research design, how large must the true effect be for the study to detect it with high probability?

For example, a study might have 80 percent power to detect an earnings effect of \$2{,}000, but only 30 percent power to detect an effect of \$500. If the study finds no statistically significant effect, interpretation depends on the MDE. If the study had enough power to detect even small meaningful effects, then non-significance is more informative. If the study only had enough power to detect very large effects, then non-significance tells us little about moderate or small effects. This distinction matters for policy. A small program evaluation with noisy outcomes might fail to reject the null even if the program is beneficial. Policymakers should not interpret that as proof that the program does not work. A well-powered study with tight confidence intervals around zero provides stronger evidence that large effects are unlikely.

---

## 18.11 Low power and exaggerated significant findings
Low power does not only increase false negatives. It can also make significant estimates unstable and exaggerated. Suppose the true effect is small and the study is noisy. Only estimates that happen to be large in magnitude will cross the statistical significance threshold. As a result, statistically significant estimates from low-powered studies may overstate the true effect. This is sometimes called the **winner's curse** or **exaggeration bias**. For example, suppose a training program truly increases earnings by \$500, but the study has large standard errors. Many samples will produce insignificant estimates. The samples that do produce significant estimates may show effects like \$2{,}000 or \$3{,}000 simply because random noise pushed the estimate upward. Therefore, when a small noisy study reports a large significant effect, researchers should ask:
- Was the study adequately powered?
- Is the estimate plausible given prior evidence?
- Is the confidence interval wide?
- Has the result been replicated?
- Were many outcomes or subgroups tested?

Statistical significance alone is not enough.

---

## 18.12 Multiple testing
Multiple testing occurs when researchers conduct many hypothesis tests. For example, a researcher may test whether a program affects:
- employment
- earnings
- hours worked
- job search
- education
- health
- crime
- savings
- debt
- subjective well-being

If each test uses a 5 percent significance level, then even if the program has no effect on any outcome, some statistically significant results are likely to appear by chance. If 100 independent null hypotheses are true and each is tested at the 5 percent level, the expected number of false positives is:
$100 \times 0.05 = 5$ This is why multiple testing is dangerous. A single significant result is less impressive when it is selected from many tests. Multiple testing can occur across:
- outcomes
- subgroups
- time periods
- model specifications
- treatment definitions
- control groups
- bandwidths
- transformations
- samples

The problem becomes especially severe when researchers report only significant results.

---

## 18.13 Family-wise error rate and Bonferroni correction
The **family-wise error rate**, or FWER, is the probability of making at least one Type 1 error within a family of tests. If we conduct $m$ tests, and each test has significance level $\alpha$, the probability of at least one false positive can become much larger than $\alpha$. A simple correction is the Bonferroni correction. If the desired family-wise error rate is $\alpha$, test each individual hypothesis at:
$\frac{\alpha}{m}$ For example, if:
$\alpha = 0.05$ and:
$m = 10$ then each test is conducted at:
$\frac{0.05}{10} = 0.005$
The Bonferroni correction is simple and conservative. It reduces false positives but can increase false negatives, especially when many tests are conducted. This illustrates a general tradeoff: controlling false discoveries more aggressively often reduces power.

---

## 18.14 False discovery rate
The **false discovery rate**, or FDR, is the expected share of rejected hypotheses that are false positives. In plain language:

> Among the results declared significant, what fraction are expected to be false discoveries?

FDR control is often less conservative than family-wise error control, especially when many hypotheses are tested. This can be useful in settings where researchers test many outcomes or subgroups and want to limit the proportion of false discoveries rather than the probability of any false discovery. For example, if a study examines a large number of educational outcomes, FDR methods can help distinguish robust patterns from chance findings. However, FDR adjustment does not solve all problems. If the set of hypotheses was chosen after seeing the data, or if only significant results are reported, the inference can still be misleading. Good practice includes:
- pre-specifying primary outcomes
- distinguishing primary from secondary analyses
- reporting all tested outcomes
- adjusting for multiple testing when appropriate
- interpreting exploratory results cautiously

---

## 18.15 P-hacking and specification searching
**P-hacking** occurs when researchers search across many analyses until they find statistically significant results. This can happen intentionally or unintentionally. Examples include trying many:
- outcome variables
- subgroups
- time windows
- control variable sets
- functional forms
- sample restrictions
- bandwidths
- clustering choices
- transformations
- treatment definitions

If only the significant specification is reported, the p-value no longer has its usual interpretation. The test did not account for all the hidden searches that occurred before the reported result was selected. For example, if a researcher tries 40 specifications and reports only the one with $p < 0.05$, the reported p-value understates the true risk of false discovery. This is related to the garden of forking paths: even without consciously trying to manipulate results, researchers make many analytic choices. If those choices are influenced by the data, inference becomes less reliable. Good empirical practice includes:
- pre-analysis plans
- preregistration
- transparent reporting of all specifications
- robustness checks motivated by theory
- clear distinction between confirmatory and exploratory analysis
- replication on new data

P-hacking is not merely a statistical issue. It is a research design and credibility issue.

---

## 18.16 Pre-analysis plans and preregistration
A **pre-analysis plan** specifies the main hypotheses, outcomes, sample, empirical strategy, and statistical tests before the researcher analyzes the data. Preregistration records this plan in advance, often in a public or time-stamped registry. Pre-analysis plans are especially common in randomized controlled trials, but the logic can also apply to quasi-experimental studies. A pre-analysis plan may specify:
1. primary outcomes,
2. secondary outcomes,
3. treatment arms,
4. subgroup analyses,
5. regression specifications,
6. control variables,
7. clustering level,
8. multiple testing adjustments,
9. exclusion rules,
10. heterogeneity analyses.

The purpose is not to eliminate researcher judgment. The purpose is to distinguish planned confirmatory analysis from exploratory analysis. Exploratory analysis is valuable. It can reveal unexpected patterns and generate new hypotheses. But it should be labeled as exploratory, not presented as if it were a single pre-specified test. Pre-analysis plans are most useful when:
    - many outcomes are possible
    - treatment effects are uncertain
    - researcher discretion is large
    - policy stakes are high
    - sample sizes are limited
    - publication incentives favor significant results

    They are less useful when research is genuinely exploratory or when the empirical strategy must respond to complex institutional details. Even then, transparency about analytic choices remains important.

---

## 18.17 The base rate problem and false positives
A test with a low Type 1 error rate can still produce many false discoveries if true effects are rare. This is called the base rate problem. Suppose researchers test 1,000 hypotheses. Assume only 100 hypotheses have true effects, and 900 have no true effect. Suppose the test has:
$\alpha = 0.05$ and:
$Power = 0.80$ Among the 100 true effects, expected true positives are:
$100 \times 0.80 = 80$ Among the 900 true nulls, expected false positives are:
$900 \times 0.05 = 45$ So the total number of statistically significant findings is:
$80 + 45 = 125$ The share of significant findings that are false positives is:
$\frac{45}{125} = 0.36$
So even with a 5 percent significance level and 80 percent power, about 36 percent of significant findings may be false in this example. This happens because true effects are relatively rare. The implication is important: the credibility of a significant result depends not only on its p-value, but also on prior plausibility, study design, power, multiple testing, and replication.

---

## 18.18 Statistical significance versus substantive importance
A result can be statistically significant but economically unimportant. For example, suppose a policy increases annual income by:
$\hat{\beta} = 12$ with a very small standard error:
$SE(\hat{\beta}) = 3$ The test statistic is:
$t = \frac{12}{3} = 4$
This is statistically significant. But a \$12 annual income increase may be economically trivial, especially if the policy is expensive. Conversely, a result can be economically important but statistically insignificant. Suppose another policy has:
$\hat{\beta} = 2{,}000$ and:
$SE(\hat{\beta}) = 1{,}500$ The confidence interval is wide, and the estimate may not be statistically significant. But the possible effect sizes may be large enough to matter for policy. Therefore, empirical interpretation should ask:
1. Is the estimate causally identified?
2. What is the point estimate?
3. What are the units?
4. What is the confidence interval?
5. Is the magnitude practically meaningful?
6. What are the costs and benefits?
7. What does prior evidence suggest?
8. How likely are false positives or false negatives?

Statistical significance is not the same as economic significance.

---

## 18.19 Decision theory: errors have costs
Hypothesis testing often treats Type 1 and Type 2 errors symmetrically in form, but their costs may differ greatly. A decision-theoretic approach asks:

> What action should be taken, given the evidence, uncertainty, benefits, costs, and risks of error?

For example, consider a public health intervention. If the intervention is cheap and safe, a policymaker may be willing to act on suggestive evidence because the cost of a false negative is high and the cost of a false positive is low. If the intervention is expensive or harmful if ineffective, the policymaker may require stronger evidence before acting. Similarly, in criminal justice, a false positive may be extremely costly if it leads to wrongful conviction. In early disease screening, a false negative may be extremely costly if it delays treatment. In policy evaluation, the right decision depends on:
- expected benefits
- implementation costs
- uncertainty
- risk tolerance
- distributional consequences
- reversibility
- ethical concerns
- opportunity costs

This means that the same p-value may justify different decisions in different contexts. Statistical testing provides evidence. Decision-making requires values, costs, and institutional judgment.

---

## 18.20 Bayesian thinking
Classical hypothesis testing asks:

> If the null hypothesis were true, how surprising would this data be?

Bayesian inference asks:

> Given the data, what should we believe about the hypothesis or parameter?

Bayesian inference begins with a prior belief about a parameter $\theta$:
$P(\theta)$ The data have likelihood:
$P(Data \mid \theta)$ Bayes' rule combines the prior and likelihood to produce a posterior:
$$
P(\theta \mid Data)
=
\frac{P(Data \mid \theta)P(\theta)}{P(Data)}
$$

The posterior represents updated beliefs after observing the data. For causal inference, Bayesian thinking can be useful because researchers and policymakers often have prior information:
- previous studies
- theory
- institutional knowledge
- expert judgment
- mechanism evidence
- external data

A surprising estimate from a weak design may not change beliefs much. A similar estimate from a strong design may change beliefs substantially. Bayesian reasoning also highlights why a p-value is not the probability that the null hypothesis is true. To evaluate that probability, one needs prior beliefs and a model of how likely the data are under competing hypotheses.

---

## 18.21 Bayes factors
A **Bayes factor** compares how well two hypotheses predict the observed data. For hypotheses $H_0$ and $H_1$, the Bayes factor is:

$$
BF_{10}
=
\frac{P(Data \mid H_1)}{P(Data \mid H_0)}
$$

If:
$BF_{10} > 1$ then the data are more likely under $H_1$ than under $H_0$. If:
$BF_{10} < 1$ then the data are more likely under $H_0$ than under $H_1$. For example, if:
$BF_{10}=5$
then the data are five times as likely under $H_1$ as under $H_0$. Bayes factors are different from p-values. A p-value asks how extreme the data are under the null. A Bayes factor compares the predictive performance of two hypotheses. Bayesian approaches can be especially useful when combining evidence across studies, evaluating policy decisions, or incorporating prior knowledge. However, they require explicit choices about priors and models, which can be controversial. The advantage is transparency: assumptions about prior beliefs are stated directly rather than hidden.

---

## 18.22 Frequentist and Bayesian approaches as complements
Frequentist and Bayesian approaches answer different questions. Frequentist inference emphasizes repeated-sampling properties:
- Type 1 error rates
- Type 2 error rates
- confidence interval coverage
- unbiasedness
- consistency
- power

Bayesian inference emphasizes updating beliefs:
- posterior distributions
- credible intervals
- prior information
- Bayes factors
- posterior decision-making

In practice, empirical economists often use frequentist methods for estimation and inference, while informally using Bayesian reasoning when interpreting results. For example, a researcher may think:

> This estimate is statistically significant, but the design is weak and the result is much larger than prior studies, so I am skeptical.

That is Bayesian-style reasoning, even if not formalized. Or:

> This estimate is only marginally significant, but it comes from a well-powered randomized trial, matches prior evidence, and has a plausible mechanism, so it is fairly persuasive.

Again, the interpretation combines statistical evidence, design credibility, and prior beliefs. Good empirical judgment rarely comes from a single number.

---

## 18.23 Hypothesis testing in causal inference
Hypothesis testing is useful only after the causal estimand is identified or plausibly identified. A statistically significant coefficient is not necessarily a causal effect. Suppose we estimate:
$Wage_i = \alpha + \beta Education_i + u_i$ and find:
$p < 0.01$
This means education is statistically associated with wages, conditional on the model. It does not prove that education causally increases wages. If education is endogenous because of ability, family background, or selection, then $\hat{\beta}$ may be biased. A biased estimate can be highly statistically significant. The correct sequence is:
1. Define the causal question.
2. Define the estimand.
3. Establish an identification strategy.
4. Estimate the effect.
5. Quantify uncertainty.
6. Interpret statistical and economic significance.

Inference cannot rescue a bad research design. Standard errors measure sampling uncertainty around an estimator. They do not measure all sources of uncertainty, such as:
    - omitted variable bias
    - invalid instruments
    - violated parallel trends
    - manipulation around a cutoff
    - measurement error
    - model misspecification
    - external validity concerns

    Therefore, a result can be precisely estimated and still not credible.

---

## 18.24 One-sided versus two-sided tests
A two-sided test considers effects in both directions:
$H_1: \beta \neq 0$ A one-sided test considers effects in one direction:
$H_1: \beta > 0$ or:
$H_1: \beta < 0$
One-sided tests have more power to detect effects in the specified direction, but they ignore effects in the opposite direction. A one-sided test may be appropriate when effects in the opposite direction are impossible or irrelevant. But in many empirical economics settings, effects in both directions are plausible. For example, a job training program might increase earnings by improving skills, but it might reduce earnings in the short run if participants spend less time working. A minimum wage increase might reduce employment, have no effect, or increase employment under some market conditions. Using a one-sided test after seeing the sign of the estimate is inappropriate. The direction must be specified before looking at the data. When in doubt, two-sided tests are usually more transparent.

---

## 18.25 Equivalence testing and non-inferiority
Standard hypothesis testing often uses a null of no effect:
$H_0: \beta = 0$ But sometimes researchers want to test whether an effect is small enough to be practically unimportant. For example, a policymaker may ask:

> Can we rule out employment losses larger than 1 percent?

This is different from asking whether the employment effect is exactly zero. An equivalence test defines a range of effects considered substantively negligible:
$[-\Delta, \Delta]$
where $\Delta$ is the smallest effect size that would matter. The goal is to show that the effect lies within this range. Equivalence testing is useful when researchers want to argue that effects are small, not merely statistically insignificant. A non-significant result does not prove the effect is zero. But a sufficiently tight confidence interval around zero can rule out effects large enough to matter. For example, if a minimum wage study estimates:
$\hat{\beta} = -0.001$ with confidence interval:
$[-0.003, 0.002]$ then the study may rule out large employment effects. But if the confidence interval is:
$[-0.20, 0.18]$ then non-significance tells us little. Equivalence testing forces researchers to define what counts as a meaningful effect.
---

## 18.26 Application example: tutoring program
Suppose a school district evaluates a tutoring program. The estimated effect on standardized test scores is:
$\hat{\beta} = 0.08$ standard deviations, with:
$SE(\hat{\beta}) = 0.04$ The test statistic is:
$t = \frac{0.08}{0.04} = 2$ The result is approximately significant at the 5 percent level for a two-sided test. A naive interpretation might be:

> The tutoring program works.

A more careful interpretation asks:
1. Was treatment randomly assigned or otherwise credibly identified?
2. Is 0.08 standard deviations educationally meaningful?
3. What is the confidence interval?
4. Was this the primary outcome?
5. Were many outcomes tested?
6. Was the study adequately powered?
7. Was there attrition?
8. Were standard errors clustered appropriately?
9. Does the effect persist over time?
10. Does the program justify its cost?

The approximate 95 percent confidence interval is:
$0.08 \pm 1.96(0.04)$
$0.08 \pm 0.0784$
$[0.0016, 0.1584]$
This interval barely excludes zero and includes effects ranging from nearly zero to moderately meaningful. The result is suggestive, but interpretation depends on design quality, multiple testing, prior evidence, and cost-effectiveness.

---

## 18.27 Application example: job training program with low power
Suppose a job training evaluation estimates:
$\hat{\beta} = 1{,}500$ with:
$SE(\hat{\beta}) = 1{,}200$ The test statistic is:
$t = \frac{1{,}500}{1{,}200} = 1.25$ This is not statistically significant at conventional levels. A careless interpretation would be:

> The program has no effect.

But the approximate 95 percent confidence interval is:
$1{,}500 \pm 1.96(1{,}200)$
$1{,}500 \pm 2{,}352$
$[-852, 3{,}852]$ This interval includes zero, but it also includes economically meaningful positive effects. The study is too imprecise to distinguish no effect from a large beneficial effect. A better conclusion is:

> The estimate is positive but imprecise. The data do not provide strong evidence of an effect, but they also do not rule out economically important gains.

This distinction is essential. Failure to reject the null is not proof that the null is true.

---

## 18.28 Application example: multiple outcomes in a policy evaluation
Suppose a researcher evaluates a youth employment program and tests effects on 20 outcomes. The program appears to significantly reduce one outcome: reported anxiety. If anxiety was the only pre-specified primary outcome, this may be meaningful. But if the researcher tested 20 outcomes and only anxiety was significant, the result may be a false positive. At a 5 percent significance level, even if the program has no effect on any outcome, the expected number of significant findings is:
$20 \times 0.05 = 1$ So one significant result among 20 tests is not surprising under the global null. The researcher should report:
- all tested outcomes
- which outcomes were primary
- whether multiple-testing corrections were applied
- whether the anxiety result is consistent with theory
- whether related mental health outcomes also changed
- whether the effect replicates in other samples

Patterns are more persuasive than isolated significant coefficients.

---

**Common mistakes.**
1. **Saying insignificant means no effect:** A statistically insignificant result means the study did not reject the null. It does not prove the effect is zero. Always inspect the confidence interval.
2. **Saying significant means important:** A statistically significant result can be tiny and economically irrelevant. Always inspect the magnitude and units.
3. **Saying significant means causal:** Statistical significance does not solve confounding, selection bias, reverse causality, invalid instruments, or violated identifying assumptions. Causal credibility comes from research design.
4. **Treating $p=0.049$ and $p=0.051$ as fundamentally different:** Thresholds are conventions. Evidence changes continuously.
5. **Ignoring multiple testing:** If many tests were conducted, some significant results may occur by chance.
6. **Ignoring power:** A study with low power may miss meaningful effects.
7. **Reporting only significant outcomes:** Selective reporting makes evidence look stronger than it is.
8. **Ignoring prior evidence:** A surprising result from a weak design should be interpreted differently from a result that matches prior theory and evidence.
9. **Confusing confidence intervals with probability statements:** A frequentist 95 percent confidence interval does not literally mean there is a 95 percent probability that the true parameter lies in that specific interval. It means that the procedure would cover the true parameter 95 percent of the time over repeated samples under the model assumptions.
10. **Forgetting decision costs:** The same evidence may justify different decisions depending on the costs of false positives and false negatives.

---

**Application checklist.**
When interpreting statistical evidence, ask the following questions.
1. **What is the null hypothesis?** Is it clearly stated? Is it a null of no effect, no difference, or some other claim?
2. **What is the alternative hypothesis?** Is it one-sided or two-sided? Was the direction specified before seeing the data?
3. **What is the estimate?** What is the point estimate? What are the units? Is the magnitude meaningful?
4. **What is the uncertainty?** What is the standard error? What is the confidence interval? Are the standard errors appropriate for the design?
5. **Is the result statistically significant?** At what level? Is the threshold pre-specified or chosen after seeing the result?
6. **Is the result economically significant?** Would the effect matter in practice? Is it large relative to costs, baseline levels, or policy goals?
7. **Was the study adequately powered?** Could the study detect meaningful effects? What was the minimum detectable effect?
8. **Were multiple hypotheses tested?** How many outcomes, subgroups, or specifications were examined? Were corrections applied? Which analyses were pre-specified?
9. **Is the estimate causally identified?** What research design supports causal interpretation? What assumptions are required? Could the estimate be biased even if statistically significant?
10. **What are the costs of error?** Is a false positive more costly than a false negative? How should uncertainty affect the decision?
11. **How does the result fit prior evidence?** Is the result consistent with theory, previous studies, and mechanisms? Is replication available?
12. **What conclusion is justified?** Avoid binary claims like "works" or "does not work" when uncertainty is substantial. State what the evidence suggests, what it rules out, and what remains uncertain.

---

## 18.29 Summary
Type 1 and Type 2 errors describe two ways empirical conclusions can be wrong. A Type 1 error is a false positive:
$\text{Reject } H_0 \text{ when } H_0 \text{ is true.}$ A Type 2 error is a false negative:
$\text{Fail to reject } H_0 \text{ when } H_0 \text{ is false.}$ The probability of a Type 1 error is the significance level:
$\alpha$ The probability of a Type 2 error is:
$\beta_{II}$ Statistical power is:
$Power = 1 - \beta_{II}$
P-values measure how surprising the data are under the null hypothesis. They do not give the probability that the null hypothesis is true. Confidence intervals show a range of parameter values compatible with the estimate and uncertainty. They are often more informative than a binary significant/not-significant label. Multiple testing increases the risk of false discoveries. Pre-analysis plans, multiple-testing corrections, transparent reporting, and replication help reduce this risk. Bayesian inference provides a different framework, asking how data update prior beliefs. Bayesian and frequentist approaches answer different questions and can be complementary. The most important lessons are:
1. Statistical significance is not causality.
2. Statistical significance is not practical importance.
3. Non-significance is not proof of no effect.
4. Multiple testing can create false discoveries.
5. Low power can hide meaningful effects.
6. Interpretation should combine effect size, uncertainty, design credibility, prior evidence, and decision costs.

A rigorous empirical conclusion should not say only whether $p < 0.05$. It should explain what was estimated, how credible the design is, how large the effect is, how uncertain it is, what errors are possible, and what decision the evidence supports.

# 19. Cost-Benefit Analysis and Policy Evaluation
## 19.1 Why causal inference is not the end of policy analysis
Causal inference helps answer a central question:

> What happens if we intervene?

Cost-benefit analysis helps answer a different but equally important question:

> Is the intervention worth doing?

A policy may have a positive causal effect and still not be worth implementing if the benefits are small relative to the costs. Conversely, a policy may have modest effects on each person but still be socially valuable if it is inexpensive, scalable, and reaches many people. For example, suppose a job training program increases annual earnings by \$500 per participant. That sounds beneficial. But whether the program is desirable depends on additional questions:
- How much does the program cost per participant?
- How long do the earnings gains last?
- Are the gains caused by higher productivity or by displacing other workers?
- Are participants giving up time they could have spent working?
- Are there administrative costs?
- Are there tax revenue effects?
- Are benefits concentrated among disadvantaged workers?
- Would the effect remain if the program scaled nationally?
- How uncertain is the estimated effect?

A causal estimate is therefore an input into policy evaluation, not a complete policy evaluation by itself. Good empirical policy analysis combines:
1. a credible estimate of causal effects,
2. a clear accounting of costs,
3. a clear accounting of benefits,
4. uncertainty analysis,
5. distributional analysis,
6. external validity assessment,
7. comparison to feasible alternatives.

The main idea is simple:

> A policy should be evaluated relative to what would happen without it and relative to other possible uses of the same resources.

Cost-benefit analysis is the framework for making that comparison explicit.

---

## 19.2 The basic cost-benefit framework
The simplest cost-benefit calculation compares total benefits and total costs:
$Net\ Benefit = Total\ Benefits - Total\ Costs$ A policy has positive net benefits if:
$Total\ Benefits > Total\ Costs$ Equivalently:
$Net\ Benefit > 0$ For example, suppose a training program costs \$2,000 per participant and increases the present value of lifetime earnings by \$5,000 per participant. Ignoring other effects, the net benefit per participant is:
$Net\ Benefit = 5{,}000 - 2{,}000 = 3{,}000$
This suggests the program creates \$3,000 of net value per participant. But this simple calculation hides many important details. The analyst must decide what counts as a benefit, what counts as a cost, whose benefits and costs matter, when they occur, and how uncertain they are. A more careful cost-benefit analysis asks:
1. What is the policy or intervention?
2. What is the counterfactual?
3. What outcomes change because of the policy?
4. Which changes are benefits?
5. Which changes are costs?
6. Who receives the benefits?
7. Who bears the costs?
8. When do benefits and costs occur?
9. How should future values be discounted?
10. How uncertain are the estimates?
11. Do benefits and costs change at scale?
12. What are the relevant alternatives?

The counterfactual remains central. A policy's benefit is not the outcome after the policy. It is the difference between the outcome with the policy and the outcome without the policy. In potential-outcomes language, the benefit of a policy for outcome $Y$ is based on:
$Y_i(1) - Y_i(0)$
where $Y_i(1)$ is the outcome with the policy and $Y_i(0)$ is the outcome without the policy. Cost-benefit analysis therefore depends on causal inference. If the estimated treatment effect is biased, the benefit calculation will also be biased.

---

## 19.3 Benefits, costs, and the policy counterfactual
A benefit is a gain caused by the intervention relative to the counterfactual. A cost is a resource use, loss, or burden caused by the intervention relative to the counterfactual. This means benefits and costs must be measured against the same baseline. Suppose a city implements a tutoring program. After the program, test scores rise. The benefit is not simply the final test score level. The benefit is the improvement relative to what test scores would have been without tutoring. If average test scores rise by 8 points after tutoring, but would have risen by 5 points anyway, the causal gain is:
$8 - 5 = 3$
The benefit calculation should be based on the 3-point causal increase, not the 8-point raw increase. Similarly, suppose a public health program costs \$10 million. If \$2 million would have been spent anyway on existing services, the incremental cost of the new program may be \$8 million rather than \$10 million. The same logic applies to costs:
$Incremental\ Cost = Cost(Policy) - Cost(Counterfactual)$ and benefits:
$Incremental\ Benefit = Benefit(Policy) - Benefit(Counterfactual)$ Cost-benefit analysis is therefore always comparative. The relevant question is not:

> Is this policy good?

The relevant question is:

> Is this policy better than the counterfactual use of resources?

The counterfactual may be doing nothing, continuing the current policy, implementing a smaller version, implementing a different program, or spending the money elsewhere.

---

## 19.4 Private benefits, fiscal benefits, and social benefits
One common mistake is to confuse private benefits, fiscal benefits, and social benefits.
- **Private benefits.**
Private benefits are gains to individuals or firms directly affected by the policy. Examples:
- higher earnings for workers
- higher test scores for students
- better health for patients
- lower energy bills for households
- higher profits for firms

If a job training program increases a participant's annual earnings by \$1,000, that is a private benefit to the participant.
- **Fiscal benefits.**
Fiscal benefits are gains to the government budget. Examples:
- higher tax revenue
- lower unemployment insurance payments
- lower Medicaid spending
- lower incarceration costs
- reduced administrative costs

If higher earnings increase income tax revenue by \$200, that is a fiscal benefit to the government.
- **Social benefits.**
Social benefits include all benefits to society, regardless of whether they appear in private income or government budgets. Examples:
- improved health
- reduced crime victimization
- lower pollution exposure
- increased productivity
- reduced inequality
- improved child well-being
- spillover benefits to peers or neighborhoods

A policy can have positive social benefits even if fiscal benefits are small. For example, a health intervention may improve quality of life substantially without saving much government money. A policy can also have positive private benefits but limited social benefits if gains are mostly transfers rather than new value creation. For example, if a training program helps participants get jobs by displacing nonparticipants, the private benefits to participants may overstate the social benefits. The analyst must be explicit about the perspective of the analysis. Common perspectives include:
1. participant perspective,
2. taxpayer or government budget perspective,
3. firm perspective,
4. local community perspective,
5. national social welfare perspective.

The same policy can look different from each perspective.

---

## 19.5 Transfers versus real resource costs
A transfer moves resources from one group to another. A real resource cost uses up resources that could have been used elsewhere. This distinction matters because not every dollar paid is a social cost. For example, suppose the government gives a \$1,000 cash transfer to a household. From the government's budget perspective, the payment is a cost. From the household's perspective, it is a benefit. From a social perspective, the transfer itself is not necessarily a net resource cost because money moved from taxpayers to the household. However, transfers can still matter for social welfare because society may value dollars differently depending on who receives them. A dollar transferred to a low-income household may have higher social value than a dollar taken from a high-income taxpayer. This is a distributional issue. Real resource costs include:
- staff time
- buildings
- equipment
- administrative labor
- participant time
- transportation costs
- materials
- deadweight loss from taxation
- reduced output elsewhere

Transfers include:
- cash benefits
- tax credits
- unemployment payments
- subsidies
- grants
- benefit payments

Transfers are not irrelevant. They matter for budgets, incentives, and distribution. But analysts should not automatically treat every transfer as a net social cost. For example, consider an unemployment benefit program. Government payments to recipients are fiscal costs, but they are private benefits to recipients. The social cost includes administrative costs, financing distortions, and behavioral responses, while the social benefit includes consumption smoothing, reduced hardship, and insurance value. A rigorous cost-benefit analysis separates:
$Fiscal\ Cost$ from:
$Social\ Resource\ Cost$ and from:
$Distributional\ Transfer$
---

## 19.6 Opportunity cost
Opportunity cost is the value of the best alternative use of a resource. A policy does not only cost the dollars spent on it. It also costs the value of what those dollars, workers, buildings, or time could have produced elsewhere. For example, if a government spends \$100 million on a job training program, the opportunity cost is not merely \$100 million. It is the value of the best alternative use of that \$100 million, such as:
- expanding early childhood education
- reducing taxes
- improving public transit
- increasing healthcare access
- reducing debt
- funding wage subsidies
- doing nothing and leaving resources in private hands

Participant time also has an opportunity cost. If a worker spends 300 hours in training, those hours could have been spent working, searching for jobs, caring for family, or attending another program. Even if the program is free to the participant, participation may still be costly. If the opportunity cost of participant time is \$15 per hour, then 300 hours of training impose a time cost of:
$300 \times 15 = 4{,}500$
Ignoring participant time can make programs look more cost-effective than they really are. Opportunity cost is especially important when comparing policy alternatives. A program with positive net benefits may still be unattractive if another feasible program has larger net benefits. The correct decision rule is not:

> Implement every policy with positive net benefits.

The better decision rule is:

> Choose the feasible policy or portfolio of policies with the highest net social value, subject to constraints.

---

## 19.7 Discounting and present value
Many policies have costs and benefits that occur at different times. For example:
- early childhood education has costs now and benefits decades later
- pollution reduction has upfront costs and long-term health benefits
- infrastructure projects have immediate construction costs and future productivity benefits
- vaccination programs have current costs and future avoided illness
- job training may have immediate time costs and later earnings gains

Because future dollars are usually valued differently from present dollars, cost-benefit analysis converts future values into present value. The present value of a future benefit $B_t$ received $t$ years in the future is:
$PV(B_t) = \frac{B_t}{(1+r)^t}$ where $r$ is the discount rate. If a policy produces benefits $B_1, B_2, \dots, B_T$ over $T$ years, the total present value of benefits is:
$PV(Benefits) = \sum_{t=1}^{T} \frac{B_t}{(1+r)^t}$ Similarly, if costs occur over time:
$PV(Costs) = \sum_{t=0}^{T} \frac{C_t}{(1+r)^t}$ Net present value, or NPV, is:
$NPV = \sum_{t=0}^{T} \frac{B_t - C_t}{(1+r)^t}$ A policy has positive net present value if:
$NPV > 0$
- **Example.**
Suppose a program costs \$2,000 today and increases earnings by \$600 per year for five years. With discount rate $r=0.05$, the present value of benefits is:

$$
PV(Benefits)
=
\frac{600}{1.05}
+
\frac{600}{1.05^2}
+
\frac{600}{1.05^3}
+
\frac{600}{1.05^4}
+
\frac{600}{1.05^5}
$$

This equals approximately \$2,598. The net present value is approximately:
$NPV = 2{,}598 - 2{,}000 = 598$
Under these assumptions, the program has positive net present value. But if the benefits last only two years, the present value is much smaller. If the discount rate is higher, future benefits count less. If the earnings gain is uncertain, the expected value may be lower. Discounting forces the analyst to be explicit about timing.

---

## 19.8 Choosing a discount rate
The discount rate can strongly affect policy conclusions, especially for policies with long-term benefits. A higher discount rate places less value on future benefits. A lower discount rate places more value on future benefits. This matters for policies such as:
- climate change mitigation
- early childhood education
- public health prevention
- infrastructure
- environmental cleanup
- scientific research
- crime prevention
- education reform

For example, a benefit of \$10,000 received 30 years from now has present value:
$PV = \frac{10{,}000}{(1+r)^{30}}$ If $r=0.03$:
$PV \approx 4{,}120$ If $r=0.07$:
$PV \approx 1{,}313$
The same future benefit looks much smaller under a higher discount rate. There is no purely mechanical answer to the correct discount rate. The choice depends on theory, opportunity cost of capital, social time preference, risk, intergenerational ethics, and institutional guidance. Because conclusions may be sensitive to the discount rate, good cost-benefit analysis reports results under multiple rates. For example:
$NPV(r=0.02), \quad NPV(r=0.03), \quad NPV(r=0.05), \quad NPV(r=0.07)$
This is a form of sensitivity analysis. The analyst should not hide the role of discounting. If a policy is valuable only under very low discount rates, that should be made clear. If it remains valuable under a wide range of rates, that strengthens the policy case.

---

## 19.9 Benefit-cost ratio and internal rate of return
Two common summary measures are the benefit-cost ratio and the internal rate of return. The benefit-cost ratio is:
$BCR = \frac{PV(Benefits)}{PV(Costs)}$ If:
$BCR > 1$ then benefits exceed costs. For example, if a program has present-value benefits of \$5,000 and present-value costs of \$2,000, then:
$BCR = \frac{5{,}000}{2{,}000} = 2.5$ This means the program generates \$2.50 in benefits for every \$1 of cost. The internal rate of return, or IRR, is the discount rate that makes net present value equal zero:
$0 = \sum_{t=0}^{T} \frac{B_t - C_t}{(1+IRR)^t}$
The IRR can be interpreted as the rate of return generated by the investment. These measures are useful, but they can be misleading if used carelessly. The net present value is often the most direct measure of social value:
$NPV = PV(Benefits) - PV(Costs)$
A project with a high benefit-cost ratio may be small and produce little total value. A project with a lower benefit-cost ratio may produce much larger total net benefits if it operates at scale. For example:
- Program A costs \$1 million and produces \$3 million in benefits. Its BCR is 3 and its NPV is \$2 million
- Program B costs \$100 million and produces \$180 million in benefits. Its BCR is 1.8 and its NPV is \$80 million

Program A has the higher benefit-cost ratio, but Program B creates more total net value. Therefore, analysts should usually report multiple measures:
1. net present value,
2. benefit-cost ratio,
3. cost per unit of outcome,
4. distribution of benefits and costs,
5. uncertainty around all estimates.

---

## 19.10 Cost-effectiveness analysis
Sometimes benefits are difficult or inappropriate to monetize. In those cases, analysts may use cost-effectiveness analysis rather than full cost-benefit analysis. Cost-effectiveness analysis asks:

> How much does it cost to produce one unit of a desired outcome?

Examples:
- cost per additional student graduating
- cost per life saved
- cost per disability-adjusted life year avoided
- cost per ton of carbon reduced
- cost per crime prevented
- cost per additional worker employed
- cost per standard deviation increase in test scores

The basic formula is:
$Cost\ Effectiveness = \frac{Cost}{Effect}$ For example, if a tutoring program costs \$500,000 and increases the number of students passing an exam by 250, then:
$$
Cost\ per\ Additional\ Passing\ Student
=
\frac{500{,}000}{250}
=
2{,}000
$$

This means the program costs \$2,000 per additional passing student. Cost-effectiveness analysis is especially useful when comparing programs with the same goal. For example, if three programs aim to improve graduation rates, the analyst can compare:

$$
\frac{Cost_A}{Graduates_A}, \quad
\frac{Cost_B}{Graduates_B}, \quad
\frac{Cost_C}{Graduates_C}
$$

The lowest cost per additional graduate may be the most efficient option, assuming the graduates are comparable and the effects are causal. However, cost-effectiveness analysis does not answer whether the outcome is worth its cost in monetary terms. It helps rank alternatives but does not always determine whether any of them should be implemented.

---

## 19.11 Valuing non-market benefits
Many policy benefits are not naturally measured in dollars. Examples include:
- improved health
- reduced mortality risk
- cleaner air
- reduced pain
- improved mental health
- lower crime victimization
- better educational achievement
- social trust
- dignity
- reduced inequality
- environmental preservation

Cost-benefit analysis often requires assigning monetary values to non-market outcomes. This is difficult and sometimes controversial. Common approaches include:
1. revealed preference,
2. stated preference,
3. avoided cost,
4. willingness to pay,
5. quality-adjusted life years,
6. value of a statistical life,
7. shadow pricing.
- **Revealed preference.**
Revealed preference uses observed behavior to infer value. For example, if workers require higher wages to accept riskier jobs, wage-risk tradeoffs can be used to estimate how much people value reductions in mortality risk.
- **Stated preference.**
Stated preference uses surveys to ask people how much they would be willing to pay for a benefit. This can be useful for environmental amenities or public goods, but responses may be sensitive to survey design.
- **Avoided cost.**
Avoided cost values a benefit by the costs it prevents. For example, reducing asthma attacks may save medical expenses, missed workdays, and emergency room visits.
- **Quality-adjusted life years.**
Health economics often measures benefits using quality-adjusted life years, or QALYs. A QALY combines length of life and quality of life into one metric.
- **Value of a statistical life.**
The value of a statistical life, or VSL, is used to value small reductions in mortality risk across a population. It does not value an identified person's life. It values risk reductions. For example, if a policy reduces mortality risk by $1/100{,}000$ for each of 1 million people, the expected number of statistical lives saved is:
$1{,}000{,}000 \times \frac{1}{100{,}000} = 10$ If the VSL is \$10 million, the mortality benefit is:
$10 \times 10{,}000{,}000 = 100{,}000{,}000$ These valuation choices can have large effects on conclusions, so they should be transparent and tested for sensitivity.
---

## 19.12 Spillovers and externalities
A policy may affect people who are not directly treated. These indirect effects are called spillovers or externalities. Examples:
- Vaccination protects unvaccinated people through herd immunity
- Job training may help participants but displace nonparticipants from jobs
- Education may reduce crime and improve civic participation
- Pollution regulation may improve health for nearby communities
- Policing in one neighborhood may displace crime to another
- A school program may affect untreated classmates through peer effects
- Infrastructure may raise nearby property values

Spillovers matter because the private effect on treated units may differ from the social effect. Let the total social benefit be:
$Social\ Benefit = Direct\ Benefit + Spillover\ Benefit$
If spillovers are positive, direct effects understate total benefits. If spillovers are negative, direct effects overstate total benefits. For example, a job training program may increase participants' employment by helping them compete more effectively. If the number of jobs is fixed, some of those gains may come at the expense of nonparticipants. The direct benefit to participants may be positive, while the net social employment effect is smaller. In contrast, a vaccination program may have direct benefits for vaccinated people and positive spillovers to unvaccinated people. Looking only at vaccinated individuals may understate the social benefit. Spillovers also create complications for causal identification. If untreated units are affected by treated units, then the control group may no longer represent the no-treatment counterfactual. A rigorous policy evaluation should ask:
1. Who is directly treated?
2. Who may be indirectly affected?
3. Are spillovers positive or negative?
4. Are control units contaminated?
5. Do effects change when the policy scales up?
6. Are equilibrium responses likely?

---

## 19.13 General equilibrium and scale-up effects
Small-scale program effects may differ from large-scale policy effects. This is especially important in economics because markets adjust. A small job training program may increase participants' employment because trained workers become more attractive to employers. But if the program is expanded to all workers, the relative advantage of training may decline. Wages, vacancies, credentials, and employer expectations may adjust. A small housing voucher program may help recipients move to better neighborhoods. But a large program may raise rents if housing supply is limited. A local minimum wage increase may have different effects from a national minimum wage increase because firms, workers, and consumers can adjust across locations. A small education intervention may improve outcomes when implemented by highly motivated teachers. At scale, implementation quality may fall. These are scale-up concerns. A treatment effect estimated in one setting is often a partial-equilibrium effect. It holds fixed many background conditions. A scaled policy may change those background conditions. We can distinguish:
$Small\ Scale\ Effect$ from:
$Large\ Scale\ Effect$ They may differ because of:
- price changes
- wage changes
- displacement
- congestion
- capacity constraints
- political responses
- behavioral adaptation
- changes in program quality
- changes in participant composition
- changes in employer expectations

External validity and cost-benefit analysis are therefore connected. A policy that passes a small-scale cost-benefit test may fail at scale if effects shrink or costs rise. Good policy analysis asks:

> Would the estimated effect survive implementation at the relevant scale?

---

## 19.14 Distributional analysis
Total net benefits are not the only thing policymakers care about. Distribution matters. A policy with positive total net benefits may hurt disadvantaged groups. A policy with modest aggregate benefits may be attractive if it strongly helps people with low income, poor health, or limited opportunities. Cost-benefit analysis can incorporate distribution in several ways.
- **Incidence analysis.**
Incidence analysis asks who receives benefits and who bears costs. For example:

| Group | Benefits | Costs | Net effect |
|---|---:|---:|---:|
| Low-income households | High | Low | Positive |
| High-income taxpayers | Low | Moderate | Negative |
| Firms | Moderate | High | Negative |
| Government | Moderate | High | Ambiguous |

This table is conceptual, but it illustrates that total net benefits may hide important distributional patterns.
- **Distributional weights.**
Some analyses assign greater weight to benefits received by disadvantaged groups. A weighted social welfare function can be written abstractly as:
$Social\ Welfare = \sum_i w_i \cdot NetBenefit_i$
where $w_i$ is the social weight assigned to person or group $i$. If society places more weight on gains to low-income households, then $w_i$ may be larger for those households. Distributional weights are ethically and politically sensitive. They should be explicit rather than hidden.
- **Heterogeneous treatment effects.**
Distributional analysis also requires knowing whether treatment effects differ across groups. A program may have average effect:
$ATE = 0$ but positive effects for disadvantaged participants and negative effects for advantaged participants. A mean effect alone may mislead policy decisions. The relevant question is not only:

> What is the average net benefit?

but also:

> Who gains, who loses, and by how much?

---

## 19.15 Uncertainty in cost-benefit analysis
Cost-benefit analysis often depends on uncertain inputs:
- estimated treatment effects
- duration of effects
- discount rates
- program costs
- take-up rates
- spillovers
- external validity assumptions
- monetized values of non-market outcomes
- implementation quality
- scale-up effects

A single point estimate of net benefits can create false confidence. A more honest approach treats net benefits as uncertain:
$Net\ Benefit = \widehat{Benefit} - \widehat{Cost}$ where both components may be estimated with error. If the estimated treatment effect is $\hat{\tau}$, and the monetized value per unit of effect is $V$, then estimated benefit may be:
$\widehat{Benefit} = V \cdot \hat{\tau}$ Uncertainty in $\hat{\tau}$ translates into uncertainty in benefits. For example, suppose a program increases earnings by an estimated \$1,000, with a 95% confidence interval of:
$[-200, 2{,}200]$ If the program costs \$800 per person, the point estimate suggests positive net benefits:
$1{,}000 - 800 = 200$ But the confidence interval includes negative effects. The net benefit may plausibly be negative. A rigorous analysis should report uncertainty using tools such as:
- confidence intervals for net benefits
- sensitivity analysis
- scenario analysis
- Monte Carlo simulation
- break-even analysis
- robustness checks
- bounding exercises
- **Break-even analysis.**
Break-even analysis asks how large the effect must be for benefits to equal costs. If a program costs $C$ per participant and each unit of outcome is worth $V$, the break-even effect is:
$\tau^{*} = \frac{C}{V}$
If the estimated effect exceeds $\tau^{*}$, the program may pass the cost-benefit test. For example, if a program costs \$2,000 and each additional employed worker-year is valued at \$10,000, the break-even effect is:
$\tau^{*} = \frac{2{,}000}{10{,}000} = 0.20$ The program must increase employment by at least 0.20 worker-years per participant to break even. Break-even analysis is useful when benefits are uncertain or difficult to value precisely.
---

## 19.16 Sensitivity analysis
Sensitivity analysis asks whether conclusions change when assumptions change. This is essential because cost-benefit analysis often requires assumptions that are not directly testable. Common sensitivity checks include varying:
- the discount rate
- the duration of benefits
- the value of non-market outcomes
- administrative costs
- participant time costs
- spillover effects
- take-up rates
- treatment effect estimates
- scale-up assumptions
- distributional weights

For example, an early childhood education program may appear cost-effective if earnings gains last into adulthood. But if gains fade after a few years, the conclusion may change. A sensitivity table might report:

| Assumption | Low | Baseline | High |
|---|---:|---:|---:|
| Discount rate | 2% | 3% | 7% |
| Earnings gain duration | 5 years | 15 years | 30 years |
| Program cost | \$8,000 | \$10,000 | \$14,000 |
| Effect size | 0.05 SD | 0.15 SD | 0.25 SD |

The purpose is not to create complexity for its own sake. The purpose is to reveal which assumptions drive the conclusion. A strong cost-benefit case is robust across plausible assumptions. A fragile cost-benefit case depends on optimistic assumptions.

---

## 19.17 Program evaluation as a complete framework
Cost-benefit analysis is one part of broader program evaluation. A complete program evaluation usually asks several linked questions.
- **1. Needs assessment.**
What problem is the program trying to solve? Who is affected? Why does the problem exist? What market failure, policy failure, equity concern, or social objective motivates intervention?
- **2. Theory of change.**
How is the program supposed to work? A theory of change links inputs, activities, outputs, outcomes, and impacts. For example:

$$
Training\ Funds
\rightarrow
Courses
\rightarrow
Skills
\rightarrow
Employment
\rightarrow
Earnings
$$

The theory of change helps identify what should be measured.
- **3. Implementation analysis.**
Was the program delivered as intended? Common implementation questions include:
- Did eligible people know about the program?
- Did they enroll?
- Did they complete it?
- Was quality consistent?
- Were services delivered on time?
- Did staff have adequate training?
- Were there bottlenecks?

A program may fail because the theory was wrong or because implementation failed.
- **4. Impact evaluation.**
What causal effect did the program have? This requires a credible identification strategy.
- **5. Cost analysis.**
What resources were used? Costs should include administrative costs, direct service costs, capital costs, overhead, participant time, and opportunity costs.
- **6. Cost-benefit or cost-effectiveness analysis.**
Were the effects worth the costs? How does the program compare to alternatives?
- **7. Distributional analysis.**
Who benefited? Who paid? Were disadvantaged groups helped? Did inequality rise or fall?
- **8. Scalability analysis.**
Would the program work at larger scale? Would costs rise? Would effects shrink? Would general equilibrium responses appear? A strong evaluation does not only estimate an effect. It explains what happened, why it happened, for whom, at what cost, and whether the policy should be continued, expanded, redesigned, or ended.

---

## 19.18 Example: job training program
Suppose a government evaluates a job training program for unemployed workers. An impact evaluation estimates that the program increases annual earnings by:
$\hat{\tau} = 1{,}200$ per participant for three years. The program costs:
$C = 2{,}500$ per participant. Assume the discount rate is 5%. The present value of earnings benefits is:
$$
PV(Benefits)
=
\frac{1{,}200}{1.05}
+
\frac{1{,}200}{1.05^2}
+
\frac{1{,}200}{1.05^3}
$$

This is approximately:
$PV(Benefits) \approx 3{,}269$ The net present value is:
$NPV = 3{,}269 - 2{,}500 = 769$ The benefit-cost ratio is:
$BCR = \frac{3{,}269}{2{,}500} \approx 1.31$ The program appears beneficial. But a careful analysis would ask more questions.
- **Participant time costs.**
If participants spend 200 hours in training and their time is valued at \$10 per hour, participant time costs are:
$200 \times 10 = 2{,}000$ Now total cost is:
$2{,}500 + 2{,}000 = 4{,}500$ Then:
$NPV = 3{,}269 - 4{,}500 = -1{,}231$ The conclusion changes.
- **Fiscal effects.**
If higher earnings generate tax revenue, the government may recover part of the cost. Suppose tax revenue increases by \$300 per year for three years. The fiscal benefit is:

$$
PV(Fiscal\ Benefit)
=
\frac{300}{1.05}
+
\frac{300}{1.05^2}
+
\frac{300}{1.05^3}
\approx 817
$$

From the government budget perspective, the program still costs more than it returns fiscally:
$Fiscal\ NPV = 817 - 2{,}500 = -1{,}683$ A program can have positive social net benefits but negative fiscal net benefits.
- **Displacement.**
If some participants get jobs that would otherwise have gone to nonparticipants, the social benefit is smaller than the private earnings gain. Suppose 25% of earnings gains come from displacement. Then the social earnings benefit is:
$0.75 \times 3{,}269 = 2{,}452$ This may alter the conclusion.
- **Heterogeneity.**
The program may have larger effects for workers without high school degrees and smaller effects for college graduates. In that case, targeting may improve cost-effectiveness. The policy conclusion might be:

> The program should not be expanded universally, but it may be cost-effective for specific groups with high estimated gains and low opportunity costs.

This example shows why cost-benefit analysis must go beyond multiplying a treatment effect by a dollar value.

---

## 19.19 Example: early childhood education
Early childhood education programs often have costs today and benefits far in the future. Potential benefits include:
- improved school readiness
- higher test scores
- reduced special education placement
- higher graduation rates
- higher adult earnings
- lower crime
- better health
- higher tax revenue
- lower welfare use
- improved outcomes for parents

The challenge is that many benefits occur years or decades later. Let the program cost per child be:
$C_0$ and benefits occur over time:
$B_1, B_2, \dots, B_T$ The net present value is:
$NPV = \sum_{t=1}^{T} \frac{B_t}{(1+r)^t} - C_0$ This calculation depends heavily on:
- the persistence of effects
- the discount rate
- the value assigned to crime reduction
- the estimated effect on adult earnings
- the cost of scaling the program
- the quality of implementation
- which children are served

A small early test-score gain may be highly valuable if it predicts large long-term improvements. But if effects fade and do not translate into later outcomes, benefits may be lower. This example illustrates a major theme:

> Long-run cost-benefit analysis requires both credible causal estimates and credible assumptions about how short-run effects translate into long-run outcomes.

---

## 19.20 Example: environmental regulation
Suppose a regulation reduces air pollution. Costs may include:
- compliance costs for firms
- higher consumer prices
- administrative costs
- reduced output in polluting industries
- worker transition costs

Benefits may include:
- lower mortality
- fewer hospitalizations
- fewer asthma attacks
- improved worker productivity
- improved child development
- higher property values
- ecosystem benefits
- climate benefits

The causal effect of pollution on health is central. If pollution reductions causally reduce mortality, the mortality benefit may dominate the cost-benefit calculation. A simplified benefit calculation might be:
$Mortality\ Benefit = Lives\ Saved \times VSL$ If a regulation saves 50 statistical lives and the value of a statistical life is \$10 million, the mortality benefit is:
$50 \times 10{,}000{,}000 = 500{,}000{,}000$ If compliance costs are \$200 million, the regulation appears to have positive net benefits before counting other health and environmental benefits. But the conclusion depends on:
- the causal estimate of lives saved
- the VSL used
- compliance cost estimates
- distribution of costs across firms and consumers
- distribution of benefits across communities
- whether firms relocate pollution elsewhere
- long-run technological adaptation

Environmental policy evaluation often highlights the importance of non-market valuation, long horizons, uncertainty, and distributional justice.

---

**Common mistakes in cost-benefit analysis.**
1. **Treating causal effects as benefits without monetization or context:** An effect estimate is not yet a benefit estimate. A test-score gain, crime reduction, employment increase, or health improvement must be interpreted, valued, and compared to costs.
2. **Ignoring costs borne by participants:** Programs often require time, effort, transportation, compliance, paperwork, or risk. These costs matter even when the program is free.
3. **Ignoring opportunity cost:** Public funds, staff time, and participant time could have been used elsewhere. A policy should be compared to realistic alternatives.
4. **Confusing transfers with social costs:** A government payment is a budget cost, but it may also be a benefit to recipients. Social analysis should distinguish transfers from real resource costs.
5. **Ignoring spillovers:** Direct effects on participants may overstate or understate social benefits if untreated people are affected.
6. **Ignoring scale-up:** Small pilot programs may have effects or costs that differ from large programs.
7. **Using one optimistic scenario:** A single favorable cost-benefit estimate can be misleading. Analysts should report sensitivity to key assumptions.
8. **Ignoring distribution:** A policy with positive average net benefits may impose costs on vulnerable groups. Distribution should be explicit.
9. **Double-counting benefits:** Some benefits overlap. For example, higher earnings, higher tax revenue, and reduced welfare use are related. Counting all incorrectly can overstate benefits.
10. **Ignoring uncertainty in causal estimates:** If the treatment effect is uncertain, the benefits are uncertain. Cost-benefit analysis should reflect that uncertainty.

---

**Application checklist.**
When evaluating a policy using cost-benefit analysis, use the following checklist.
1. **Define the policy:** What exactly is being evaluated? Who is eligible? What services, rules, transfers, or requirements are included? What is the scale of implementation?
2. **Define the counterfactual:** What would happen without the policy? Is the comparison doing nothing, current practice, a smaller program, or another intervention?
3. **Identify causal effects:** What outcomes does the policy affect? Are the estimated effects causally credible? What identification strategy supports them?
4. **Choose the perspective:** Is the analysis from the perspective of:
    - participants
    - taxpayers
    - government budget
    - firms
    - local community
    - society as a whole?

    Different perspectives imply different benefits and costs.
5. **Measure benefits:** What benefits are included? Are they private, fiscal, or social? Are they monetized? Are non-market benefits valued transparently?
6. **Measure costs:** What resources are used? Are administrative costs included? Are participant time costs included? Are opportunity costs included? Are capital costs annualized appropriately?
7. **Account for timing:** When do benefits and costs occur? What discount rate is used? How sensitive are results to the discount rate?
8. **Account for spillovers:** Does the policy affect untreated people? Are spillovers positive or negative? Do control groups become contaminated?
9. **Account for scale-up:** Would effects or costs change if the program expanded? Are there capacity constraints? Would prices, wages, rents, or behavior adjust?
10. **Account for distribution:** Who gains? Who loses? Are benefits concentrated among disadvantaged groups? Should distributional weights be considered?
11. **Quantify uncertainty:** How uncertain are the treatment effects, costs, and valuations? Are confidence intervals, sensitivity checks, or scenarios reported?
12. **Compare alternatives:** Is this policy better than other feasible uses of resources? What is the opportunity cost? What is the marginal value of expanding or reducing the program?
13. **State the policy conclusion carefully:** A careful conclusion should state:
    - the estimated benefits
    - the estimated costs
    - the net benefits
    - the main assumptions
    - the uncertainty
    - the distributional consequences
    - the scale-up concerns
    - the comparison policy

    A good conclusion is not simply:

    > The program works.

    It is closer to:

    > Under the maintained assumptions, the program appears to generate positive net social benefits for the target population, mainly through increased earnings, but the conclusion is sensitive to participant time costs and persistence of effects. The evidence supports targeted expansion rather than universal scaling.

---

## 19.21 Summary
Causal inference estimates what happens when we intervene. Cost-benefit analysis asks whether the intervention is worth doing. The basic framework is:
$Net\ Benefit = Total\ Benefits - Total\ Costs$ When benefits and costs occur over time, analysts use present values:
$NPV = \sum_{t=0}^{T} \frac{B_t - C_t}{(1+r)^t}$
A policy is attractive if it generates positive net benefits relative to feasible alternatives, but that conclusion depends on many assumptions. A rigorous cost-benefit analysis must distinguish:
- causal effects from raw outcomes
- private benefits from fiscal and social benefits
- transfers from real resource costs
- direct effects from spillovers
- small-scale effects from scale-up effects
- average effects from distributional effects
- point estimates from uncertain estimates

Cost-benefit analysis also requires attention to opportunity cost, discounting, non-market valuation, distribution, uncertainty, and external validity. The central lesson is:

> A credible causal estimate tells us what a policy changes. A credible cost-benefit analysis tells us whether those changes justify the resources used, relative to the best alternative.
