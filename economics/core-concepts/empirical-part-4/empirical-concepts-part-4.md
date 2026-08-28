# Core Concepts in Empirical Economics and Causal Inference — Part 4

*Empirical Macroeconomics: Time Series, Dynamic Effects, and Structural Identification*

## Reader's Roadmap

Part 4 develops one cumulative argument: dynamic data can describe how economic variables evolve, but causal interpretation requires a separate identification argument. The chapters are organized into four conceptual acts.

| Act | Chapters | Reader's question |
| --- | --- | --- |
| **A. The Dynamic Empirical Problem** | 1–3 | What changes when causal questions unfold through time and the statistical environment may itself change? |
| **B. Modeling Dynamic Responses** | 4–5 | How can a dynamic system be represented, and how do we trace a disturbance through that system? |
| **C. From Statistical Innovation to Causal Shock** | 6–7 | When can an unexpected movement be interpreted as an economically meaningful structural shock? |
| **D. Extensions and Synthesis** | 8–9 | What changes with multiple units, common shocks, heterogeneity, spillovers, and a complete empirical design? |

The recurring logic is:

$$
\boxed{
\text{Dynamic Question}
\rightarrow
\text{Time-Series Properties}
\rightarrow
\text{Dynamic System}
\rightarrow
\text{Reduced-Form Innovation}
\rightarrow
\text{Structural Identification}
\rightarrow
\text{Dynamic Response}
\rightarrow
\text{Interpretation}
}
$$

The roadmap is deliberately repeated in compressed form near the end of Part 4. At the beginning it is a map of the argument; at the end it becomes a memory device.

> **ACT A — THE DYNAMIC EMPIRICAL PROBLEM**
> Chapters 1–3 establish the dynamic causal problem, the time-series properties of the data, and the possibility that the economic environment itself changes.

## 1. Dynamic Questions in Empirical Macroeconomics

### 1.1 Why Dynamics Change the Empirical Problem

Many empirical questions in economics can be framed as comparisons between different states of the world. For example:

* What happens to earnings if a worker receives job training?
* What happens to employment if the minimum wage increases?
* What happens to health if a patient receives a treatment?

In each case, the central causal problem is the same: we would like to compare the observed outcome with the outcome that would have occurred under an alternative treatment state. Macroeconomic questions share this same counterfactual logic, but they introduce an additional complication:

> **Economic outcomes evolve through time.**

Inflation today may depend on inflation last quarter. Output growth may depend on previous financial conditions. Interest rates may respond to current inflation while also affecting future inflation and economic activity. The timing of these relationships matters. Consider a simple dynamic model:

$$
y_t = \alpha + \phi y_{t-1} + \varepsilon_t
$$

where:

* $y_t$ is the value of an economic variable at time $t$,
* $y_{t-1}$ is its value in the previous period,
* $\phi$ measures persistence,
* $\varepsilon_t$ represents new information or an unexpected innovation.

Unlike a cross-sectional setting, observations at different dates cannot generally be treated as unrelated. The value observed today may contain information inherited from previous periods. This creates several new empirical questions:

1. How persistent are economic outcomes?
2. How quickly do shocks disappear?
3. Do shocks have temporary or permanent effects?
4. How long does it take for a policy change to affect the economy?
5. Do multiple variables respond to one another over time?
6. Can an observed change be interpreted as a causal shock?
7. Are the relationships themselves stable across different historical periods?

These questions form the basis of empirical macroeconomics.

### 1.2 Time-Series Data

A **time series** is a sequence of observations for the same variable ordered through time:

$$
y_1,y_2,\dots,y_T
$$

Examples include:

* quarterly GDP growth,
* monthly inflation,
* monthly unemployment,
* daily exchange rates,
* quarterly investment,
* interest rates,
* stock-market returns.

The defining feature is not simply that many observations exist. It is that their **ordering through time contains economic information**. For example, quarterly inflation might be represented as:

$$
\pi_1,\pi_2,\pi_3,\dots,\pi_T
$$

where $\pi_t$ represents inflation in quarter $t$. If current inflation depends partly on past inflation, we might write:

$$
\pi_t = \alpha + \phi \pi_{t-1} + \varepsilon_t
$$

If $\phi$ is large, inflation is persistent: high inflation today tends to be followed by relatively high inflation tomorrow. If $\phi$ is small, deviations from normal inflation disappear more quickly. This distinction between temporally ordered observations and a genuinely dynamic process is fundamental: past values may help explain current values. This means time-series data require us to think not only about **levels and relationships**, but also about:

* timing,
* persistence,
* trends,
* lagged effects,
* expectations,
* structural changes,
* and the propagation of shocks.

### 1.3 From One Time Series to a Dynamic System

Macroeconomists are rarely interested in only one variable. Economic variables usually evolve together. For example, consider:

$$
\mathbf{y}_t =
\begin{bmatrix}
\text{Output Growth}_t \\
\text{Inflation}_t \\
\text{Policy Rate}_t
\end{bmatrix}
$$

This is a **multivariate time series**: several variables are observed repeatedly for the same economic system. The distinction matters because these variables may influence one another. For example:

* stronger economic activity may increase inflationary pressure,
* higher inflation may lead the central bank to raise interest rates,
* higher interest rates may reduce future consumption and investment,
* weaker demand may subsequently reduce inflation,
* expectations about future policy may affect activity before policy actually changes.

This is the natural setting for models such as vector autoregressions, in which several variables are modeled jointly over time. A simple representation might therefore be:

$$
\mathbf{y}_t
=

A\mathbf{y}_{t-1}
+
\mathbf{u}_t
$$

where:

* $\mathbf{y}_t$ is a vector of economic variables,
* $A$ describes how past values are related to current values,
* $\mathbf{u}_t$ contains new movements not predicted by the variables' histories.

We will develop this model formally later. For now, the important idea is that empirical macroeconomics often studies **systems rather than isolated variables**.

### 1.4 Timing, Feedback, and Endogeneity

Dynamic systems make causal interpretation difficult because economic variables frequently respond to one another. Suppose we observe that periods with high interest rates also tend to have high inflation. A naive interpretation might be:

> Higher interest rates cause higher inflation.

But there is an obvious alternative explanation. Central banks often **raise interest rates because inflation is already high or because they expect inflation to increase**. The relationship may therefore run in both directions:

$$
\text{Inflation}
\rightarrow
\text{Interest Rates}
$$

while economic theory may also suggest:

$$
\text{Interest Rates}
\rightarrow
\text{Future Inflation}
$$

This is a dynamic form of the endogeneity problem introduced earlier in the series. The observed interest rate is not randomly assigned. It reflects policy choices made in response to economic conditions. Consequently, a regression such as

$$
\pi_t
=

\alpha
+
\beta i_t
+
\varepsilon_t
$$

does not automatically identify the causal effect of monetary policy on inflation. The coefficient $\beta$ may combine:

* the effect of interest rates on inflation,
* the central bank's response to inflation,
* responses to expected future inflation,
* changes in economic activity,
* financial shocks,
* and other omitted macroeconomic developments.

The basic causal lesson therefore remains unchanged:

> **Observed relationships do not become causal merely because they are observed through time.**

If anything, dynamic feedback often makes the identification problem more difficult.

### 1.5 Predictability Is Not Causality

Time-series analysis often asks whether one variable helps predict another. Suppose past interest rates help predict future output:

$$
E[Y_{t+1}\mid i_t]
\neq
E[Y_{t+1}]
$$

This may be useful for forecasting. But predictive information does not by itself tell us what would happen if policymakers **intervened** and changed the interest rate. These are different questions.

#### Predictive question

> Given the interest rate observed today, what should we expect output to look like tomorrow?

#### Causal question

> If the central bank unexpectedly increased the interest rate today, how would future output change relative to what would otherwise have happened?

The second question requires a counterfactual. Conceptually, we still want something like:

$$
Y_{t+h}(1)-Y_{t+h}(0)
$$

where:

* $Y_{t+h}(1)$ is the outcome at horizon $h$ following the relevant policy shock,
* $Y_{t+h}(0)$ is the outcome that would have occurred without that shock.

The difference from many earlier examples is that the causal effect is now indexed by **time horizon**. Instead of asking for one effect,

$$
\tau
$$

we may care about an entire sequence:

$$
\tau_0,\tau_1,\tau_2,\dots,\tau_H
$$

A macroeconomic intervention can therefore have:

* an immediate effect,
* a delayed effect,
* a peak effect,
* a persistent effect,
* or an effect that eventually disappears.

This is why dynamic causal analysis frequently focuses on the **path of responses through time**, rather than a single regression coefficient.

#### Terminology: Granger causality is predictive, not automatically structural

Time-series work often uses the phrase **Granger causality** for a predictive concept: $X$ Granger-causes $Y$ if past values of $X$ contain information that improves prediction of $Y$ conditional on the information already included in the model. The terminology can be misleading because this is not, by itself, an intervention claim. A variable can improve forecasts because it reacts earlier to common information, proxies for omitted forces, or belongs to a feedback system.

Accordingly, evidence that $X$ Granger-causes $Y$ should normally be read as evidence of **incremental predictive content**. A structural causal interpretation still requires an argument explaining what exogenous variation in $X$ represents and why that variation isolates the intervention or shock of interest.

#### Not every empirical macro model needs structural identification

Reduced-form models remain valuable when the objective is forecasting, description, monitoring, or summarizing dynamic comovement. Structural identification becomes necessary when the claim changes from “what tends to happen next?” to “what would happen if an economically meaningful intervention or shock occurred?” This distinction prevents the causal standard from being imposed where it is unnecessary while keeping causal claims appropriately demanding.

### 1.6 Shocks and Expected Changes

Another central distinction in empirical macroeconomics is between an ordinary change in an economic variable and an **unexpected shock**. Suppose the central bank raises the policy rate from 4% to 4.25%. That observed increase is not necessarily a monetary-policy shock. If financial markets fully expected the increase, households, firms, and investors may already have adjusted their behavior before the announcement. By contrast, suppose markets expected the rate to remain at 4%, but the central bank unexpectedly raises it to 4.25%.

The unexpected component is much closer to the object economists often want to study. We can think schematically of:

$$
\text{Observed Policy Change}
=

\text{Expected Component}
+
\text{Unexpected Component}
$$

The empirical challenge is that the unexpected component must itself be interpreted carefully. An unexpected increase in interest rates could occur because:

* the central bank unexpectedly became more hawkish,
* inflation news was worse than expected,
* economic activity was unexpectedly strong,
* policymakers received information that markets did not possess.

So even an **unexpected movement** is not automatically an **exogenous structural shock**. That distinction will become central when we later separate **reduced-form innovations** from **structural shocks**.

### 1.7 Running Application: Monetary Policy, Output, and Inflation

Throughout Part 4, we will use one recurring empirical question:

> **What happens to inflation and economic activity after an unexpected monetary-policy tightening?**

Suppose we observe quarterly data on:

$$
\mathbf{y}_t
=

\begin{bmatrix}
GDPGrowth_t \\
Inflation_t \\
PolicyRate_t
\end{bmatrix}
$$

Our ultimate objective is not merely to document whether these variables move together. We want to estimate something closer to:

$$
IRF_{GDP}(h)
$$

and

$$
IRF_{\pi}(h)
$$

where $h$ represents the number of quarters following a monetary-policy shock. In plain language:

* What happens to output immediately?
* What happens one quarter later?
* When is the largest effect?
* What happens to inflation?
* How long do the effects persist?
* Do they eventually disappear?
* Would the estimated response be different in a recession or a high-inflation period?

Before answering any of these questions, however, we will need to solve several intermediate problems. We need to understand:

1. whether the variables are stable through time,
2. whether shocks are temporary or persistent,
3. whether the economy behaves differently across regimes,
4. how several macroeconomic variables can be modeled jointly,
5. how dynamic responses are estimated,
6. what a statistical innovation represents,
7. and, most importantly, **what makes a monetary-policy shock causally identifiable**.

The monetary-policy example will therefore serve as an integrated application rather than a separate case study. Each section will add another piece of the empirical argument.

### 1.8 Common Mistakes

**Mistake 1 — Treating time-series observations as independent**

Quarterly inflation in one period is usually related to inflation in surrounding periods. Time ordering is part of the data-generating process.

**Mistake 2 — Treating temporal precedence as causality**

If $X_t$ occurs before $Y_{t+1}$, this does not imply:

$$
X_t\rightarrow Y_{t+1}
$$

Both variables may respond to earlier conditions or expectations.

**Mistake 3 — Confusing predictability with intervention**

A variable may be useful for forecasting another variable without having a causal effect on it.

**Mistake 4 — Treating every unexpected movement as an exogenous shock**

Unexpected movements can still reflect endogenous responses to other unexpected information.

**Mistake 5 — Ignoring feedback**

Macroeconomic variables frequently affect one another simultaneously and over multiple periods.

**Mistake 6 — Ignoring anticipation**

Economic agents may respond before a policy change formally occurs if they expect it in advance.

**Mistake 7 — Focusing only on contemporaneous effects**

Many macroeconomic effects emerge gradually. The relevant causal object may be an entire response path rather than the effect within the period of the intervention.

### 1.9 Application and Evaluation Checklist

When approaching a dynamic empirical question, ask:

#### Data

1. What economic variables are observed?
2. At what frequency are they measured?
3. How long is the historical sample?
4. Are observations ordered meaningfully through time?

#### Dynamics

5. Could current values depend on past values?
6. How persistent are the variables likely to be?
7. Could effects occur with delays?
8. Could economic agents anticipate the event?

#### Economic relationships

9. Can the variables affect one another?
10. Could policy respond endogenously to the outcome being studied?
11. Are there common shocks affecting several variables simultaneously?

#### Causal interpretation

12. What is the intervention or economic shock of interest?
13. Is the question predictive or causal?
14. What is the relevant counterfactual?
15. Over what horizons should the causal response be measured?
16. What variation could eventually identify the shock?

### 1.10 Summary

Empirical macroeconomics extends the causal-inference framework into settings where economic variables evolve jointly through time. The fundamental causal problem has not disappeared. We still want to understand:

$$
\text{Observed Outcome}
-
\text{Relevant Counterfactual Outcome}
$$

But the counterfactual is now dynamic. A shock today may change outcomes tomorrow, next quarter, and several years into the future. Time therefore introduces additional complications:

* persistence,
* lagged relationships,
* feedback,
* anticipation,
* joint determination,
* and dynamic propagation.

The first task is not yet to estimate a VAR or calculate an impulse response. It is to understand the structure of the dynamic empirical problem.

> **Central Lesson:**
> **Macroeconomic data add timing, persistence, feedback, and propagation to the causal-inference problem. Observing that variables move together through time does not tell us what would happen following an exogenous economic intervention.**

## 2. Stationarity, Persistence, and Non-Stationarity

### 2.1 Why Stability Matters

Before studying how economic variables respond to shocks, we need to understand how those variables behave through time. A central question is:

> **Are the statistical properties of the process sufficiently stable for observations from different periods to be meaningfully compared?**

Consider quarterly inflation. If inflation fluctuates around a relatively stable long-run average, with similar volatility and similar dependence on past inflation throughout the sample, then observations from different periods may provide information about a common underlying process. But suppose instead that inflation:

* follows a persistent upward trend,
* experiences permanent shifts in its average level,
* becomes substantially more volatile,
* or behaves according to completely different dynamics during different historical periods.

Then treating the entire sample as if it were generated by one stable process may be misleading. This is the motivation for the concept of **stationarity**. A stationary process does not need to remain constant. It can rise and fall substantially. The key idea is that the statistical rules governing those fluctuations remain stable through time.

### 2.2 Weak Stationarity

A commonly used concept is **weak stationarity**, sometimes called covariance stationarity. A weakly stationary process typically satisfies three conditions. First, the expected value is constant through time:

$$
E[y_t] = \mu
$$

Second, the variance is constant:

$$
Var(y_t) = \sigma^2
$$

Third, the covariance between observations depends on the distance between them rather than on the specific calendar dates:

$$
Cov(y_t,y_{t-k}) = \gamma_k
$$

where $k$ is the lag between the observations. This means that the relationship between $y_t$ and $y_{t-1}$ should be governed by the same covariance structure whether we examine observations early or late in the sample. In short, stationarity concerns stability in the mean, variance, and lag-dependent covariance structure of the process. A stationary process can therefore fluctuate substantially:

$$
y_t = \mu + \varepsilon_t
$$

where:

$$
E[\varepsilon_t]=0
$$

and the statistical properties of $\varepsilon_t$ remain stable. The observations vary. The **rules generating the variation** remain stable.

### 2.3 Stationarity Does Not Mean No Movement

A common misunderstanding is to interpret stationarity as meaning that a variable hardly changes. That is incorrect. Suppose a series follows:

$$
y_t = 2 + 0.6y_{t-1} + \varepsilon_t
$$

The series may experience large positive and negative shocks. But because:

$$
|0.6|<1
$$

the effect of a temporary shock gradually diminishes. The process tends to return toward its long-run behavior. This property is called **mean reversion**. To see why, suppose a shock $\varepsilon_t$ raises $y_t$ by one unit. One period later, the remaining effect is approximately:

$$
0.6
$$

Two periods later:

$$
0.6^2 = 0.36
$$

Three periods later:

$$
0.6^3 = 0.216
$$

More generally, after $h$ periods, the effect is proportional to:

$$
\phi^h
$$

for an autoregressive process of the form:

$$
y_t = \alpha + \phi y_{t-1} + \varepsilon_t
$$

when:

$$
|\phi|<1
$$

As $h$ becomes large:

$$
\phi^h \rightarrow 0
$$

The shock eventually dies out. This simple idea will become extremely important when we later study **impulse response functions**.

### 2.4 Persistence

Stationarity and persistence are related, but they are not the same concept. A process can be stationary and still be highly persistent. Consider:

$$
y_t = \alpha + 0.95y_{t-1}+\varepsilon_t
$$

Because $|0.95|<1$, the process can still be stationary. But the effect of a shock disappears slowly. For example:

$$
0.95^{10}\approx0.60
$$

so a substantial part of the original shock may remain even ten periods later. Now compare this with:

$$
y_t = \alpha + 0.2y_{t-1}+\varepsilon_t
$$

where:

$$
0.2^{10}
$$

is extremely close to zero. Both processes may be stationary. But their economic behavior is very different. The first is highly persistent. The second reverts toward its long-run behavior rapidly.

This distinction matters in macroeconomics because many substantive questions concern not only whether a shock has an effect, but **how long that effect lasts**.

### 2.5 Non-Stationarity

A process is **non-stationary** when important statistical properties change through time. Common sources include:

* changing means,
* changing variances,
* trends,
* unit roots,
* structural breaks,
* regime changes,
* and changing relationships among variables.

Non-stationarity therefore describes a broad class of problems rather than one specific model. A variable can be non-stationary because it trends steadily upward. Another variable may be non-stationary because shocks permanently alter its level. A third may behave differently before and after a major structural change. These cases have different economic interpretations and may require different empirical treatments.


#### Time-series behavior at a glance

The distinctions introduced in this chapter are easier to retain when they are compared directly. The table is a guide to interpretation rather than a mechanical classification rule.

| Process | What is stable or unstable? | Effect of a one-time shock | Typical empirical implication |
| --- | --- | --- | --- |
| Stationary autoregression | Mean, variance, and lag-covariance structure are stable | Temporary; the effect decays | Model the level if the level is the relevant economic object |
| Highly persistent stationary process | Same statistical structure, but slow mean reversion | Temporary but long-lived | Do not confuse slow decay with a unit root |
| Trend-stationary process | Mean follows a deterministic trend; deviations can be stationary | Shocks to deviations are temporary | Detrending may preserve the long-run deterministic path |
| Unit-root / random-walk process | The level does not revert to a fixed mean | Permanent; shocks accumulate | Differencing may be appropriate if changes are the relevant object |
| Structural-break or regime process | Parameters change discretely across periods or states | Depends on the local regime | Model the break or regime rather than forcing one relationship over the full sample |

### 2.6 Trend Non-Stationarity

Consider:

$$
y_t = \alpha + \beta t + \varepsilon_t
$$

where $t$ represents time. Then:

$$
E[y_t]=\alpha+\beta t
$$

The expected value changes systematically over time. If $\beta>0$, the series has an upward trend. Because the mean is not constant, the process is not stationary around a fixed level. However, suppose we subtract the deterministic trend:

$$
\tilde y_t = y_t-(\alpha+\beta t)
$$

If $\tilde y_t$, is stationary, then the original process can be described as **trend-stationary**. A deterministic trend therefore creates a changing mean even when deviations around that trend form a stationary process. This distinction is important because a trending variable can create the appearance of strong relationships with other trending variables even when no meaningful economic relationship exists between them.

### 2.7 Random Walks and Unit-Root Behavior

A different form of non-stationarity occurs when shocks have permanent effects. The classic example is a random walk:

$$
y_t = y_{t-1}+\varepsilon_t
$$

Suppose:

$$
\varepsilon_t=1
$$

in one period. Then $y_t$ rises by one unit. But because future observations build on the new level, that increase remains part of the series indefinitely. The effect does not decay. We can see this recursively:

$$
y_t = y_{t-1}+\varepsilon_t
$$

$$
y_{t+1}=y_t+\varepsilon_{t+1}
$$

Substituting:

$$
y_{t+1}
=

y_{t-1}
+
\varepsilon_t
+
\varepsilon_{t+1}
$$

and more generally:

$$
y_t
=

y_0
+
\sum_{s=1}^{t}\varepsilon_s
$$

Past shocks accumulate. This contrasts sharply with a stationary autoregressive process:

$$
y_t = \phi y_{t-1}+\varepsilon_t,
\qquad |\phi|<1
$$

where the influence of shocks eventually disappears. This difference leads to an important economic distinction:

> **Are shocks temporary deviations from a stable path, or do they permanently change the level of the variable?**

That question has major implications for how macroeconomic shocks are interpreted.

### 2.8 Levels, Growth Rates, and Differences

Many macroeconomic variables look very different depending on how they are expressed. Consider real GDP. The **level** of GDP may grow over long periods:

$$
GDP_t
$$

while the **growth rate** measures the rate of change:

$$
g_t
=

\frac{GDP_t-GDP_{t-1}}{GDP_{t-1}}
$$

or approximately:

$$
g_t
\approx
\Delta \log(GDP_t)
$$

Similarly, the price level may trend upward:

$$
P_t
$$

while inflation measures its rate of change:

$$
\pi_t
=

\frac{P_t-P_{t-1}}{P_{t-1}}
$$

or approximately:

$$
\pi_t
\approx
\Delta \log(P_t)
$$

This means the statement:

> “GDP is non-stationary”

does not automatically imply:

> “GDP growth is non-stationary.”

Likewise, the price level and inflation are not the same time-series object. The transformation used in empirical analysis therefore affects both the statistical properties of the data and the economic interpretation of the model.

### 2.9 Differencing

One common way to transform a persistent or non-stationary series is to examine its first difference:

$$
\Delta y_t = y_t-y_{t-1}
$$

Consider the random walk:

$$
y_t=y_{t-1}+\varepsilon_t
$$

Taking first differences gives:

$$
\Delta y_t=\varepsilon_t
$$

If $\varepsilon_t$ is stationary, then the change in $y_t$ is stationary even though the level of $y_t$ is not. This illustrates why economists often analyze:

* GDP growth rather than GDP levels,
* changes in interest rates rather than interest-rate levels in some applications,
* returns rather than asset prices.

But differencing should not be mechanical. Taking differences changes the economic question. A model of:

$$
GDP_t
$$

concerns the level of economic activity. A model of:

$$
\Delta GDP_t
$$

concerns changes in economic activity. Those are related but distinct objects.

#### Cointegration and error correction: when differencing can discard long-run information

Differencing can convert some non-stationary series into stationary changes, but it is not always innocuous. Two variables can each contain a unit root while a particular linear combination of them is stationary. In that case the variables are **cointegrated**: they may drift individually while remaining tied by a stable long-run relationship. For example, if $y_t$ and $x_t$ are individually non-stationary but

$$
y_t-\beta x_t
$$

is stationary, then $\beta$ describes a long-run equilibrium relation. Modeling only $\Delta y_t$ and $\Delta x_t$ can obscure that information. An error-correction representation instead allows short-run changes to depend on the previous period's deviation from the long-run relation. The practical lesson is the same as elsewhere in this chapter: transformations should follow from both the statistical properties of the series and the economic question, not from a mechanical rule to difference every persistent variable.

### 2.10 Changing Volatility

Non-stationarity does not need to come from a changing mean. The variance of a process may also change over time. For example:

$$
r_t = \sigma_t\varepsilon_t
$$

where:

$$
Var(r_t)=\sigma_t^2
$$

If $\sigma_t$ changes substantially, then the volatility of the process changes even if its mean remains stable. Financial markets provide an intuitive example. Returns may fluctuate around approximately the same mean during both normal and crisis periods, while the magnitude of those fluctuations becomes dramatically larger during crises. Stable averages therefore do not imply stable volatility. This matters because periods of unusually high volatility may:

* affect statistical uncertainty,
* alter the behavior of economic agents,
* change relationships among variables,
* or signal a transition into a different economic regime.

We will return to this idea in the next section.

### 2.11 Stationarity and the Meaning of a Shock

Stationarity also changes how we should interpret an economic shock. Suppose:

$$
y_t=\phi y_{t-1}+\varepsilon_t
$$

with:

$$
|\phi|<1
$$

A one-time shock has a temporary effect. Its influence at horizon $h$ is proportional to:

$$
\phi^h
$$

and therefore:

$$
\lim_{h\rightarrow\infty}\phi^h=0
$$

Now compare:

$$
y_t=y_{t-1}+\varepsilon_t
$$

A one-time shock permanently shifts the path of $y_t$. So before asking:

> What happens after a monetary-policy shock?

we also need to ask:

> What kind of process is being shocked?

The answer determines whether the dynamic response should eventually return toward zero or whether the shock may permanently change the path of the variable. This is why stationarity is not merely a technical preprocessing issue. It affects the substantive interpretation of dynamic effects.

### 2.12 Ergodicity: Can One Historical Path Teach Us About the Process?

Macroeconomics has another unusual feature. For many important variables, we observe only one realized history. We have:

* one realized history of US inflation,
* one realized path of US monetary policy,
* one sequence of global recessions,
* one realized history of the world economy.

This motivates the concept of **ergodicity**. Informally:

> **An ergodic process is one for which a sufficiently long realization can reveal the underlying statistical properties of the process.**

Consider the time average:

$$
\frac{1}{T}\sum_{t=1}^{T}y_t
$$

and the population expectation:

$$
E[y_t]
$$

Under suitable ergodic conditions:

$$
\frac{1}{T}\sum_{t=1}^{T}y_t
\rightarrow
E[y_t]
$$

as:

$$
T\rightarrow\infty
$$

The idea is that observing one process for long enough allows us to learn about its distribution. The distinction can be summarized as:

* **stationarity:** the distributional rules do not change through time,
* **ergodicity:** one sufficiently long observed path reveals those rules.

These concepts are related but not identical.

### 2.13 Stationarity Does Not Guarantee Ergodicity

Consider:

$$
y_t=X
$$

where $X$ is randomly chosen once:

$$
X=
\begin{cases}
0 & \text{with probability }0.5\\
1 & \text{with probability }0.5
\end{cases}
$$

and then remains fixed forever. Across hypothetical realizations:

$$
E[y_t]=0.5
$$

for every period. The distribution is therefore stable through time. But suppose the realized value is:

$$
X=1
$$

Then every observation in our historical sample is:

$$
1,1,1,1,\dots
$$

and:

$$
\frac{1}{T}\sum_{t=1}^{T}y_t=1
$$

regardless of how large $T$ becomes. One realized path does not reveal the population mean of $0.5$. The process may therefore be stationary without being ergodic. The example shows why **a long time series is not automatically equivalent to many independent realizations of an economic system**.

### 2.14 Why This Matters for Empirical Macroeconomics

The concepts introduced so far affect almost every dynamic model we will use later.

#### Historical comparability

If the underlying process changes substantially, observations from the 1970s may not be directly comparable to observations from the 2010s.

#### Persistence

If macroeconomic variables are highly persistent, shocks can affect outcomes many periods into the future.

#### Model specification

A model appropriate for a stationary growth rate may not be appropriate for a trending level.

#### Dynamic responses

Whether an impulse response eventually returns toward zero depends partly on the stability of the underlying system.

#### Statistical inference

Serial dependence means that observations cannot generally be treated as independent draws.

#### Structural interpretation

If economic relationships themselves change over time, a single parameter estimated over the entire sample may represent no stable structural relationship at all. Stationarity is therefore not simply something to test before running a model. It asks whether the historical observations can reasonably be interpreted as realizations of a sufficiently stable economic process.

### 2.15 Running Application: Monetary Policy, Inflation, and Output

Return to our running system:

$$
\mathbf{y}_t=
\begin{bmatrix}
GDPGrowth_t\\
Inflation_t\\
PolicyRate_t
\end{bmatrix}
$$

Before estimating how the system responds to a monetary-policy shock, we should ask how each variable behaves through time.

#### Output

The level of real GDP generally behaves differently from GDP growth. If GDP contains a strong trend, modeling:

$$
GDP_t
$$

and modeling:

$$
GDPGrowth_t
$$

are not equivalent empirical choices.

#### Prices and inflation

The price level:

$$
P_t
$$

and inflation:

$$
\pi_t
$$

also represent different objects. A permanent increase in the price level does not necessarily imply permanently higher inflation.

#### Interest rates

Interest rates may display substantial persistence:

$$
i_t
=

\alpha
+
\phi i_{t-1}
+
\varepsilon_t
$$

A high value of $\phi$ would imply that changes in monetary conditions tend to persist.

#### The causal question

Ultimately, we want to estimate what happens after a monetary-policy shock. But the expected shape of that response depends partly on the dynamics of the system. If output growth is mean-reverting, we might expect the effect of a temporary shock eventually to disappear. If a variable contains a unit root, the effect may instead be permanent. The statistical properties of the variables therefore influence the economic meaning of the impulse responses we will later estimate.

### 2.16 Common Mistakes

**Mistake 1 — Interpreting stationarity as constancy**

A stationary variable can fluctuate considerably. The issue is whether its statistical properties are stable.

**Mistake 2 — Assuming all persistent variables are non-stationary**

A stationary process can be extremely persistent when:

$$
|\phi|
$$

is close to one. Persistence and unit-root behavior are not identical.

**Mistake 3 — Assuming a long sample solves instability**

More observations do not solve the problem if the economic process itself changes. A longer sample may simply combine different historical regimes.

**Mistake 4 — Treating levels and growth rates as interchangeable**

Transforming:

$$
y_t
$$

into:

$$
\Delta y_t
$$

changes the empirical object being studied.

**Mistake 5 — Differencing automatically**

Differencing may help address some forms of non-stationarity, but it should follow from the properties of the series and the economic question rather than from a mechanical rule.

**Mistake 6 — Ignoring changing variance**

A process may have a stable mean but experience major changes in volatility.

**Mistake 7 — Ignoring persistence when interpreting shocks**

A statistically significant effect today tells us little about the full economic consequence unless we know how the effect propagates through time.

**Mistake 8 — Treating one historical realization as unlimited independent evidence**

A long macroeconomic history is still one realized path of an interconnected economic system.

### 2.17 Application and Evaluation Checklist

When evaluating the time-series properties of an economic variable, ask:

#### Stability

1. Does the series appear to fluctuate around a stable level?
2. Does its mean change systematically over time?
3. Does its variance appear stable?
4. Are there obvious trends?

#### Persistence

5. How strongly does the current value depend on past values?
6. Do shocks disappear quickly or slowly?
7. Could shocks have permanent effects?

#### Transformation

8. Is the relevant economic object a level, growth rate, return, or change?
9. Would differencing change the substantive question?
10. Are trends economically meaningful or statistical nuisances?

#### Historical comparability

11. Are early and late observations plausibly generated by similar economic relationships?
12. Are there major institutional or policy changes in the sample?
13. Could the apparent non-stationarity reflect structural breaks or different regimes?

#### Causal interpretation

14. Should a structural shock have temporary or permanent consequences?
15. Over what horizon should its effects be evaluated?
16. Would instability in the underlying process make one average response misleading?

### 2.18 Summary

Dynamic empirical analysis requires more than observing how variables move through time. We need to understand the statistical process generating those movements. A stationary process has stable statistical properties such as its mean, variance, and lag-dependent covariance structure. A persistent stationary process may respond slowly to shocks while still eventually returning toward its long-run behavior. By contrast, non-stationary processes may contain:

* trends,
* unit roots,
* changing volatility,
* structural breaks,
* or other changes in their statistical properties.

A random walk illustrates the central distinction:

$$
y_t=y_{t-1}+\varepsilon_t
$$

Shocks accumulate and permanently affect the path of the variable. In a stable autoregressive process:

$$
y_t=\phi y_{t-1}+\varepsilon_t,
\qquad |\phi|<1
$$

the effect of a shock eventually disappears. Ergodicity adds another consideration: even when a process is statistically stable, we need conditions under which one sufficiently long historical realization can reveal its underlying properties. These ideas prepare us for a more difficult possibility:

> What if the economic process is not governed by the same relationships throughout the sample?

The next section considers **structural breaks, regimes, and state-dependent economic relationships**.

> **Central Lesson:**
> **Before interpreting dynamic relationships or responses to shocks, we must understand whether the economic process is stable, how persistent its movements are, and whether shocks have temporary or permanent effects. Stationarity is therefore part of the economic interpretation of a dynamic model, not merely a technical prerequisite.**

## 3. Structural Breaks, Regimes, and State Dependence

### 3.1 What If the Economic Rules Change?

The previous section assumed that we could meaningfully ask whether a time series is generated by a stable statistical process. But macroeconomic history often contains periods in which the economy appears to behave differently. For example:

* inflation dynamics may differ between low- and high-inflation periods,
* monetary policy may operate differently near the zero lower bound,
* financial relationships may change during crises,
* fiscal policy may have different effects in recessions than in expansions,
* exchange-rate dynamics may change after a country adopts a new monetary regime.

This raises a deeper question:

> **What if the relationship among economic variables is not constant throughout the sample?**

Suppose we estimate:

$$
y_t = \alpha + \beta x_t + \varepsilon_t
$$

The standard interpretation assumes that the same coefficient:

$$
\beta
$$

meaningfully describes the relationship between $x_t$ and $y_t$ throughout the sample. But suppose instead that:

$$
\beta = \beta_1
$$

during one historical period and:

$$
\beta = \beta_2
$$

during another. Then estimating a single coefficient over the entire sample may produce an average that describes neither period particularly well. The problem is no longer simply that the variables are persistent or trending. The **economic relationship itself may have changed**. This motivates the concepts of:

* structural breaks,
* regimes,
* regime switching,
* and state-dependent effects.

A regime is therefore a persistent state of the world in which the data-generating process follows a particular rule set, such as expansion versus recession, low versus high inflation, or calm versus high-volatility financial conditions.

### 3.2 Structural Breaks

A **structural break** occurs when some important feature of the data-generating process changes. For example, suppose:

$$
y_t = \alpha_1 + \beta_1 x_t + \varepsilon_t
$$

before some date $T^*$, but:

$$
y_t = \alpha_2 + \beta_2 x_t + \varepsilon_t
$$

after that date. Then:

$$
(\alpha_1,\beta_1)
\neq
(\alpha_2,\beta_2)
$$

The relationship has changed. The break might affect:

* the mean,
* the variance,
* the persistence of the process,
* the relationship between variables,
* the response to shocks,
* or several of these at once.

A simple break in the mean could be represented as:

$$
y_t =
\begin{cases}
\mu_1 + \varepsilon_t, & t < T^* \\
\mu_2 + \varepsilon_t, & t \geq T^*
\end{cases}
$$

with:

$$
\mu_1 \neq \mu_2
$$

A break in the relationship between two variables could instead be represented as:

$$
y_t =
\begin{cases}
\alpha_1+\beta_1x_t+\varepsilon_t, & t<T^* \\
\alpha_2+\beta_2x_t+\varepsilon_t, & t\geq T^*
\end{cases}
$$

The key point is that the same model no longer governs the entire historical sample.

### 3.3 Why Structural Breaks Matter

Structural breaks create several problems for empirical analysis. Suppose monetary policy had a relatively strong effect on output during one historical period and a weaker effect during another. If we estimate:

$$
Y_t = \alpha+\beta Shock_t+\varepsilon_t
$$

over the combined sample, the resulting:

$$
\hat\beta
$$

may be some weighted average of different underlying effects. That average may be statistically correct for the pooled sample but economically misleading. The researcher might conclude:

> “The effect of monetary policy is moderate.”

when the more informative conclusion is:

> “The effect is large in one environment and small in another.”

Structural breaks can therefore affect:

* parameter interpretation,
* forecasts,
* impulse responses,
* long-run relationships,
* and causal conclusions.

They can also make earlier historical observations less informative about current economic behavior.

### 3.4 What Can Cause a Structural Break?

A structural break can arise for many reasons.

#### Policy changes

A central bank may adopt a new operating framework. For example, the relationship between inflation and interest rates may change after a change in the monetary-policy regime.

#### Institutional changes

Financial regulation, labor-market institutions, fiscal rules, or exchange-rate arrangements may change.

#### Technological changes

New technologies can alter production, productivity, pricing, and financial transmission.

#### Major crises

Financial crises, pandemics, wars, or other large disruptions can alter behavior.

#### Changes in expectations

If households and firms begin to form expectations differently, historical relationships may change even if formal institutions remain the same.

#### Changes in market structure

Greater financial integration, globalization, or changes in competition can alter transmission mechanisms. The important point is that a structural break is not merely a statistical curiosity. It may reflect a genuine change in the economic environment.

#### Policy invariance and the Lucas-critique intuition

Structural instability can arise even without a dramatic institutional break. If households and firms understand a change in the policy rule, they may alter expectations and behavior, causing historically estimated relationships to change. A coefficient that summarized behavior under one policy regime may therefore fail to predict outcomes under a different regime.

This is the intuition behind the **Lucas critique**: reduced-form historical relationships need not be invariant to policy changes. The implication here is not that every reduced-form model is useless, but that policy counterfactuals require particular caution when the intervention itself may change the behavioral rules generating the data.

### 3.5 Structural Breaks Versus Non-Stationarity

Structural breaks can produce patterns that look like more general non-stationarity. Suppose:

$$
y_t=
\begin{cases}
2+\varepsilon_t, & t<T^* \\
5+\varepsilon_t, & t\geq T^*
\end{cases}
$$

Within each period, the process may be stationary around a stable mean. But over the full sample, the mean is not constant. The overall series therefore looks non-stationary. This distinction is important. The process may not be drifting continuously.

Instead, it may contain two locally stable periods separated by a break. So when a series appears unstable, one question is:

> Is the process continuously non-stationary, or is it stable within separate historical regimes?

These interpretations imply different empirical models.

### 3.6 Regimes

A **regime** is a persistent economic state in which the system follows a particular set of relationships. Examples include:

| Economic setting     | Regime 1       | Regime 2        |
| -------------------- | -------------- | --------------- |
| Business cycle       | Expansion      | Recession       |
| Inflation            | Low inflation  | High inflation  |
| Financial conditions | Calm           | Crisis          |
| Monetary policy      | Conventional   | Constrained     |
| Volatility           | Low volatility | High volatility |

A simple regime-dependent model is:

$$
y_t=\mu_{S_t}+\varepsilon_t
$$

where:

$$
S_t \in \{1,2,\dots,K\}
$$

indexes the regime. If $S_t=1$, the process might have mean:

$$
\mu_1
$$

while under:

$$
S_t=2
$$

the mean becomes:

$$
\mu_2
$$

The variance can also depend on the regime:

$$
\varepsilon_t
\sim
N(0,\sigma_{S_t}^2)
$$

so that:

$$
\sigma_1^2 \neq \sigma_2^2
$$

A crisis regime, for example, may have both different average behavior and much higher volatility. Both the mean and the variance may therefore depend on the regime.

### 3.7 Structural Breaks Versus Regime Switching

Structural breaks and regime switching are related, but they are not the same thing. A **structural break** usually refers to a one-time or relatively rare change. A **regime-switching process** allows the economy to move repeatedly among different states. For example:

#### Structural break

A central bank adopts a new inflation-targeting framework in 1995 and continues using it thereafter. We might represent this as:

$$
S_t=
\begin{cases}
1, & t<1995 \\
2, & t\geq1995
\end{cases}
$$

#### Regime switching

The economy repeatedly moves between expansion and recession. Then:

$$
S_t
$$

can move:

$$
1\rightarrow2\rightarrow1\rightarrow2
$$

over time. The distinction is that structural breaks represent one-time or rare persistent changes, while regime switching allows repeated movement among states.


#### Structural break, regime switching, and state dependence compared

These ideas are related but answer different questions.

| Concept | What changes? | Does the state recur? | Main empirical question |
| --- | --- | --- | --- |
| **Structural break** | A parameter or data-generating relationship changes at a date or over a transition | Usually rare or persistent | Can one model describe the entire sample? |
| **Regime switching** | The economy moves among distinct rule sets | Yes, potentially many times | Which state is the economy in, and how persistent is that state? |
| **State-dependent effect** | The response to a shock varies with the state | The state may be observed or latent | Is the causal response different in recessions, crises, high-inflation periods, or other environments? |

A regime model can describe changing statistical behavior without identifying why the regime exists, and a state-dependent response can document heterogeneity without identifying the causal mechanism behind that heterogeneity.

### 3.8 Observed and Unobserved Regimes

Sometimes the economic state can be directly observed. For example, a researcher might define:

$$
HighInflation_t=
\begin{cases}
1, & \pi_t>5% \\
0, & \pi_t\leq5%
\end{cases}
$$

The researcher has explicitly classified the observations. Similarly, a recession indicator may be supplied by an external dating procedure. These are **observed regimes**. But sometimes the regime itself is not directly observed. Suppose financial markets alternate between:

* a normal-liquidity state,
* and a stressed-liquidity state.

We may observe asset prices, credit spreads, volatility, and lending, but not the regime itself. Then the regime can be treated as a **latent state**:

$$
S_t
$$

that must be inferred from the data. This motivates regime-switching models.

### 3.9 Markov Regime Switching

One important approach assumes that regimes evolve according to a **Markov process**. The Markov property states:

$$
P(S_{t+1}\mid S_t,S_{t-1},S_{t-2},\dots)
=

P(S_{t+1}\mid S_t)
$$

In words:

> **Conditional on the current regime, earlier regimes do not provide additional information about the next regime.**

This is the Markov property used here. For a two-regime model, the transition matrix is:

$$
P=
\begin{bmatrix}
p_{11} & p_{12} \\
p_{21} & p_{22}
\end{bmatrix}
$$

where:

* $p_{11}$ is the probability of remaining in regime 1,
* $p_{12}$ is the probability of moving from regime 1 to regime 2,
* $p_{21}$ is the probability of moving from regime 2 to regime 1,
* $p_{22}$ is the probability of remaining in regime 2.

Because each row contains all possible next-period states:

$$
p_{11}+p_{12}=1
$$

and:

$$
p_{21}+p_{22}=1
$$

Suppose:

$$
P=
\begin{bmatrix}
0.95 & 0.05 \\
0.20 & 0.80
\end{bmatrix}
$$

Then regime 1 is very persistent:

$$
P(S_{t+1}=1\mid S_t=1)=0.95
$$

while regime 2 has an 80% probability of continuing:

$$
P(S_{t+1}=2\mid S_t=2)=0.80
$$

This allows the model to describe states that are persistent but not permanent. The example illustrates persistent but nonpermanent states.

### 3.10 Regime-Switching Models

A basic Markov-switching model might be:

$$
y_t=\mu_{S_t}+\varepsilon_t
$$

where:

$$
S_t\in\{1,2\}
$$

and the state evolves according to the transition probabilities. A richer model could allow autoregressive dynamics to differ:

$$
y_t
=

\alpha_{S_t}
+
\phi_{S_t}y_{t-1}
+
\varepsilon_t
$$

Then both the intercept and persistence can depend on the regime. For example:

#### Regime 1

$$
y_t
=

\alpha_1
+
0.3y_{t-1}
+
\varepsilon_t
$$

#### Regime 2

$$
y_t
=

\alpha_2
+
0.9y_{t-1}
+
\varepsilon_t
$$

The second regime is much more persistent. The economy may therefore exhibit very different shock propagation depending on the current state.

### 3.11 Local Stability and Overall Instability

An important implication of regime models is that a series can appear unstable when viewed over the entire sample even if it is relatively stable within each regime. Suppose:

$$
y_t\mid S_t=1
$$

is stationary around:

$$
\mu_1
$$

and:

$$
y_t\mid S_t=2
$$

is stationary around:

$$
\mu_2
$$

with:

$$
\mu_1\neq\mu_2
$$

The unconditional series can look highly unstable because it switches between the two local processes. A series may therefore look non-stationary overall because it moves among several locally stable regimes. This creates an important diagnostic question:

> Is the economy governed by one unstable process, or by several more stable processes between which it switches?

### 3.12 State-Dependent Effects

Regimes matter not only because the level or volatility of an economic variable may change. The **effect of a shock itself may depend on the state of the economy**. Suppose the effect of a policy shock is:

$$
\beta_1
$$

during normal periods but:

$$
\beta_2
$$

during recessions. We could write:

$$
Y_t
=

\alpha
+
\beta_1 Shock_t
+
\beta_2(Shock_t\times Recession_t)
+
\varepsilon_t
$$

When:

$$
Recession_t=0
$$

the effect of the shock is:

$$
\beta_1
$$

When:

$$
Recession_t=1
$$

the effect becomes:

$$
\beta_1+\beta_2
$$

This is a dynamic analogue of **heterogeneous treatment effects**. Earlier in the series, treatment effects could differ across:

* individuals,
* firms,
* demographic groups,
* regions.

In empirical macroeconomics, effects may also differ across:

* recessions and expansions,
* high- and low-inflation periods,
* financial crises and normal conditions,
* different monetary regimes.

The heterogeneity is now associated with the **state of the economic system**.

### 3.13 Regime Dependence Versus Treatment Heterogeneity

It is useful to make the connection explicit. Suppose the effect of treatment for individual $i$ is:

$$
\tau_i
$$

In a state-dependent macro model, we might instead write:

$$
\tau(S_t)
$$

or:

$$
\tau_s
$$

where the effect depends on the regime. For example:

$$
\tau_{recession}
\neq
\tau_{expansion}
$$

This means an average effect:

$$
E[\tau]
$$

may conceal economically important variation. A policy could have:

* a large effect during recessions,
* a small effect during expansions,
* and therefore a moderate average effect.

The average is not necessarily wrong. It may simply be incomplete.

### 3.14 Running Application: Does Monetary Policy Have the Same Effect in Every State?

Return to our running question:

> **What happens to inflation and output after an unexpected monetary-policy tightening?**

So far, we have implicitly treated the effect as stable. But suppose monetary transmission differs across economic states. For example:

#### Low-inflation regime

$$
S_t=1
$$

#### High-inflation regime

$$
S_t=2
$$

We might represent the output response as:

$$
GDPGrowth_{t+h}
=

\alpha_h
+
\beta_{1,h}MPShock_t
+
\beta_{2,h}
(MPShock_t\times HighInflation_t)
+
\varepsilon_{t+h}
$$

The effect during low-inflation periods is:

$$
\beta_{1,h}
$$

The effect during high-inflation periods is:

$$
\beta_{1,h}+\beta_{2,h}
$$

for each horizon:

$$
h=0,1,2,\dots,H
$$

This means state dependence can affect the **entire dynamic response path**, not merely the contemporaneous coefficient.

### 3.15 Why Monetary Transmission Might Be State-Dependent

There are several economic reasons why an identical policy shock might have different consequences in different environments.

#### Expectations

If inflation expectations are already unstable, a policy tightening may affect expectations more strongly.

#### Financial conditions

When households and firms are highly indebted, changes in interest rates may have larger effects on spending.

#### Economic slack

A tightening during a strong expansion may operate differently from the same tightening during a recession.

#### Policy credibility

A central bank with highly credible inflation objectives may influence expectations differently from one whose commitments are less credible.

#### Interest-rate constraints

When policy rates are near their effective lower bound, conventional monetary-policy dynamics may differ from normal periods. The point is not that any one of these mechanisms must be true. It is that **economic theory can provide reasons to expect state dependence**, which can then motivate empirical tests.

### 3.16 Regime Classification Does Not Create Causality

A very important warning is required here. Suppose we estimate that monetary-policy shocks have larger effects during recessions than expansions. That finding does not automatically mean that recession status has been causally identified as the reason for the difference. Regime classification and causal identification are separate problems. For example, recession periods may also differ systematically in:

* financial stress,
* fiscal policy,
* uncertainty,
* credit conditions,
* external demand,
* asset prices.

So an interaction such as:

$$
Shock_t\times Recession_t
$$

can reveal **conditional heterogeneity** without necessarily identifying the causal mechanism responsible for it. This reflects the same lesson from earlier parts of the series:

> **Describing heterogeneity is not the same as identifying why the heterogeneity exists.**

### 3.17 Endogenous Regimes

Another complication is that the regime itself may be influenced by the same forces we are trying to study. Suppose we classify periods as:

$$
HighInflation_t=1
$$

when inflation is high. But monetary policy itself affects inflation. Then regime status is not necessarily an externally determined characteristic. Similarly, recessions may partly result from earlier policy decisions or shocks. This creates a potential endogeneity problem. A state-dependent relationship such as:

$$
Y_t
=

\alpha
+
\beta_1 Shock_t
+
\beta_2 Shock_t\times S_t
+
\varepsilon_t
$$

may therefore be more difficult to interpret when:

$$
S_t
$$

is itself endogenous. The appropriate interpretation depends on:

* how the regime is defined,
* when it is measured,
* whether the regime can respond to the shock,
* and what causal question is being asked.

### 3.18 Ex Ante Versus Ex Post States

Timing becomes particularly important when defining regimes. Suppose we ask whether monetary policy has different effects during recessions. One possibility is to classify the state using information known **before the shock**:

$$
S_{t-1}
$$

Then we ask:

> Does the effect of a shock at time $t$ depend on the economic state that existed immediately before the shock?

This is conceptually different from defining the state using an outcome that occurs after the shock. If $S_{t+h}$, is partly caused by the policy shock, conditioning on it may create serious interpretational problems. A useful practical rule is:

> **Whenever state dependence is studied, ask whether the state is defined using information that precedes the shock or information that may itself be affected by it.**

### 3.19 Regime Models and Structural Interpretation

A regime-switching model can tell us that the data behave differently across states. For example, it may find:

$$
\phi_1\neq\phi_2
$$

or:

$$
\sigma_1^2\neq\sigma_2^2
$$

But this does not by itself tell us **why** the regimes exist. A latent regime might statistically resemble:

* recession versus expansion,
* high versus low financial stress,
* tight versus loose monetary conditions.

But giving the state an economic label requires additional evidence. This is analogous to the distinction we will later make between:

* reduced-form shocks,
* and structural shocks.

A statistical state is not automatically an economically identified state.

### 3.20 How Regimes Affect Forecasting and Causal Analysis

Regime changes matter for both forecasting and causal inference, but in different ways.

#### Forecasting

If the economy is currently in regime 2, the relevant forecasting relationship may be:

$$
E[y_{t+1}\mid S_t=2]
$$

rather than an unconditional historical average.

#### Causal analysis

For causal questions, we may instead want:

$$
E[Y_{t+h}(1)-Y_{t+h}(0)\mid S_t=s]
$$

The causal effect itself is conditional on the state. This is a more demanding question. It requires us to identify both:

1. the relevant shock or intervention,
2. and how its effect varies across economic states.

Thus, state-dependent causal analysis combines the identification problems from earlier parts of the series with the dynamic complications introduced in Part 4.

### 3.21 Common Mistakes

**Mistake 1 — Assuming one relationship governs the entire sample**

A single coefficient may conceal major changes across historical periods.

**Mistake 2 — Calling every unusual observation a structural break**

A large shock is not necessarily evidence that the underlying economic relationship has permanently changed.

**Mistake 3 — Confusing a structural break with a regime switch**

A structural break is typically a rare or persistent change. A regime-switching process allows repeated movement among states.

**Mistake 4 — Treating regimes as automatically observed**

Some regimes are directly classified, while others are latent and inferred from the data.

**Mistake 5 — Giving latent regimes economic labels too quickly**

A statistically estimated “regime 1” is not automatically a recession, crisis, or high-inflation state. Economic interpretation requires additional evidence.

**Mistake 6 — Assuming state dependence proves a causal mechanism**

Finding different effects across states does not explain why the states generate different effects.

**Mistake 7 — Ignoring the timing of regime classification**

A state defined after the shock may itself be affected by the shock.

**Mistake 8 — Pooling very different periods without justification**

Adding more historical observations does not necessarily improve inference if those observations come from different data-generating processes.

### 3.22 Application and Evaluation Checklist

When evaluating possible structural change or regime dependence, ask:

#### Structural stability

1. Is there reason to believe the economic relationship is stable throughout the sample?
2. Did important institutions or policy frameworks change?
3. Are there obvious breaks in means, variances, or persistence?
4. Could one parameter reasonably describe the entire historical period?

#### Regimes

5. Are there economically meaningful states of the world?
6. Are those states directly observed or latent?
7. Are transitions rare and permanent, or repeated?
8. If the regime is latent, what features of the data identify it?

#### State-dependent effects

9. Could the treatment or shock have different effects across states?
10. What economic mechanism would predict that heterogeneity?
11. Is the state measured before the shock?
12. Could the shock itself change the regime?

#### Interpretation

13. Does an estimated regime correspond to a clear economic concept?
14. Could another factor explain the apparent state dependence?
15. Is the estimated average effect hiding economically important heterogeneity?
16. Would conclusions change if separate periods were analyzed?

### 3.23 Summary

Economic relationships need not remain constant through time. A **structural break** occurs when the data-generating process experiences a relatively persistent change. A **regime** is a state of the world in which the economy follows a particular set of statistical or economic relationships. Regime-switching models allow the economy to move repeatedly among those states. Under a Markov structure:

$$
P(S_{t+1}\mid S_t,S_{t-1},\dots)
=

P(S_{t+1}\mid S_t)
$$

so the current state summarizes the information used to determine transition probabilities. Regime dependence also introduces a form of treatment-effect heterogeneity. Instead of one constant effect:

$$
\tau
$$

we may have:

$$
\tau_s
$$

or more generally:

$$
\tau(h,s)
$$

where the effect varies both by the horizon and by the state of the economy. For our monetary-policy application, this means that an unexpected interest-rate increase may have different consequences during:

* recessions and expansions,
* low- and high-inflation environments,
* calm and stressed financial conditions.

But identifying regimes does not solve the causal problem. A regime-switching model may describe different statistical states without explaining why those states exist, and a state-dependent correlation does not automatically identify a state-dependent causal effect. The next step is therefore to construct a framework capable of representing several macroeconomic variables that evolve and respond to one another simultaneously. That leads to **vector autoregressions and dynamic economic systems**.

> **Central Lesson:**
> **Macroeconomic relationships may change across historical periods and states of the economy. Structural breaks and regimes help describe that instability, while state dependence allows dynamic effects to vary across economic environments. But identifying different regimes does not, by itself, identify causal effects or their mechanisms.**

> **ACT B — MODELING DYNAMIC RESPONSES**
> Chapters 4–5 move from properties of individual series to models of interacting systems and the response paths generated by shocks.

## 4. Vector Autoregressions and Dynamic Economic Systems

### 4.1 Why Macroeconomic Variables Are Often Modeled as a System

Many macroeconomic variables do not evolve independently. Inflation may influence monetary policy. Monetary policy may influence output. Output may influence inflation. Financial conditions may affect all three.

This means that the empirical problem is often not well represented by a single equation in which one variable is treated as purely explanatory and another as purely dependent. Consider our running application:

$$
\mathbf{y}_t
=

\begin{bmatrix}
GDPGrowth_t \\
Inflation_t \\
PolicyRate_t
\end{bmatrix}
$$

A conventional regression might attempt to model inflation as:

$$
Inflation_t
=

\alpha
+
\beta PolicyRate_t
+
\varepsilon_t
$$

But this representation ignores several important possibilities:

* inflation may depend on its own past,
* the policy rate may depend on past inflation,
* output may affect both inflation and policy,
* the policy rate may affect output with a delay,
* all three variables may respond to common shocks.

A more natural approach is therefore to model the variables **jointly as a dynamic system**. One widely used framework for doing this is the **vector autoregression**, or VAR.

### 4.2 From an Autoregression to a Vector Autoregression

We previously considered a simple autoregressive model:

$$
y_t
=

\alpha
+
\phi y_{t-1}
+
\varepsilon_t
$$

Current values depend on past values of the same variable. A VAR extends this idea to several variables. Suppose we have two variables:

$$
y_t
$$

and:

$$
x_t
$$

Instead of allowing each variable to depend only on its own past, we allow each to depend on the past values of **both variables**:

$$
y_t
=

\alpha_y
+
a_{11}y_{t-1}
+
a_{12}x_{t-1}
+
u_{y,t}
$$

and:

$$
x_t
=

\alpha_x
+
a_{21}y_{t-1}
+
a_{22}x_{t-1}
+
u_{x,t}
$$

The first equation says that current $y_t$ may depend on:

* past $y$,
* past $x$.

The second says that current $x_t$ may also depend on:

* past $y$,
* past $x$.

The two variables are therefore treated as part of one dynamic system.

### 4.3 Matrix Representation

The same system can be written more compactly as:

$$
\mathbf{y}_t
=

\mathbf{c}
+
A\mathbf{y}_{t-1}
+
\mathbf{u}_t
$$

where:

$$
\mathbf{y}_t
=

\begin{bmatrix}
y_t \\
x_t
\end{bmatrix}
$$

$$
\mathbf{c}
=

\begin{bmatrix}
\alpha_y \\
\alpha_x
\end{bmatrix}
$$

$$
A
=

\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
$$

and:

$$
\mathbf{u}_t
=

\begin{bmatrix}
u_{y,t} \\
u_{x,t}
\end{bmatrix}
$$

The matrix:

$$
A
$$

contains the dynamic relationships among the variables. For example:

$$
a_{12}
$$

describes how the previous value of $x$ is associated with the current value of $y$, holding the other lagged variables in the system fixed. Similarly:

$$
a_{21}
$$

describes how past $y$ is associated with current $x$. This is the basic structure of a VAR with one lag, usually called a **VAR(1)**. The coefficient matrices summarize how the vector of variables depends on its own lags and therefore capture dynamic interaction within the system.

### 4.4 VARs with Multiple Lags

Economic effects often take more than one period to appear. A VAR can therefore include several lags:

$$
\mathbf{y}_t
=

\mathbf{c}
+
A_1\mathbf{y}_{t-1}
+
A_2\mathbf{y}_{t-2}
+
\cdots
+
A_p\mathbf{y}_{t-p}
+
\mathbf{u}_t
$$

where:

$$
p
$$

is the number of lags. A VAR with two lags is:

$$
\mathbf{y}_t
=

\mathbf{c}
+
A_1\mathbf{y}_{t-1}
+
A_2\mathbf{y}_{t-2}
+
\mathbf{u}_t
$$

This allows current outcomes to depend on economic conditions from both the previous period and two periods earlier. For quarterly macroeconomic data, this can matter because many economic mechanisms operate gradually. For example:

* monetary policy may influence financial conditions quickly,
* investment may respond with a delay,
* output may respond later,
* inflation may respond later still.

A lag structure allows the model to capture this gradual propagation.

### 4.5 What Does “Endogenous” Mean Inside a VAR?

In ordinary regression language, researchers often distinguish between:

* dependent variables,
* independent variables.

A standard equation might be written as:

$$
Y_t
=

\alpha
+
\beta X_t
+
\varepsilon_t
$$

where $Y_t$ is the outcome and $X_t$ is the explanatory variable. A VAR is different. The variables inside:

$$
\mathbf{y}_t
$$

are usually treated as **jointly endogenous within the dynamic system**. This means that each variable is modeled as potentially depending on the lagged values of every variable in the system. For example, consider:

$$
\mathbf{y}_t
=

\begin{bmatrix}
GDPGrowth_t \\
Inflation_t \\
PolicyRate_t
\end{bmatrix}
$$

A VAR(1) contains three equations.

#### Output equation

$$
GDPGrowth_t
=

\alpha_1
+
a_{11}GDPGrowth_{t-1}
+
a_{12}Inflation_{t-1}
+
a_{13}PolicyRate_{t-1}
+
u_{1,t}
$$

#### Inflation equation

$$
Inflation_t
=

\alpha_2
+
a_{21}GDPGrowth_{t-1}
+
a_{22}Inflation_{t-1}
+
a_{23}PolicyRate_{t-1}
+
u_{2,t}
$$

#### Policy-rate equation

$$
PolicyRate_t
=

\alpha_3
+
a_{31}GDPGrowth_{t-1}
+
a_{32}Inflation_{t-1}
+
a_{33}PolicyRate_{t-1}
+
u_{3,t}
$$

The model therefore allows feedback in several directions. Past inflation may help explain the policy rate. Past policy may help explain output. Past output may help explain inflation. The system does not require us to declare one of these variables permanently “the treatment” and another permanently “the outcome.”

### 4.6 Reduced-Form VARs

The model:

$$
\mathbf{y}_t
=

\mathbf{c}
+
A_1\mathbf{y}_{t-1}
+
\cdots
+
A_p\mathbf{y}_{t-p}
+
\mathbf{u}_t
$$

is usually called a **reduced-form VAR**. The term “reduced form” matters. The model describes how the variables move together dynamically. It does not yet claim that the residuals:

$$
\mathbf{u}_t
$$

represent economically pure causal shocks. For example:

$$
u_{Policy,t}
$$

represents the part of the policy rate not predicted by the included lagged variables. But this does not automatically mean:

$$
u_{Policy,t}
=

\text{Monetary Policy Shock}_t
$$

The residual might contain several kinds of unexpected information. This distinction will become central in Sections 6 and 7. For now, the important point is:

> **A reduced-form VAR is primarily a statistical representation of dynamic relationships.**

### 4.7 What Information Does a VAR Coefficient Provide?

Suppose the inflation equation contains:

$$
Inflation_t
=

\alpha
+
a_{21}GDPGrowth_{t-1}
+
a_{22}Inflation_{t-1}
+
a_{23}PolicyRate_{t-1}
+
u_t
$$

Then:

$$
a_{23}
$$

describes the relationship between the previous period's policy rate and current inflation, conditional on the other lagged variables in the equation. It may be tempting to interpret:

$$
a_{23}
$$

as:

> the causal effect of monetary policy on inflation.

That interpretation is generally too strong. The coefficient describes one **local lagged relationship inside the system**. But a change in the policy rate may also affect future output, which then affects future inflation, which then affects future policy. The complete effect therefore propagates through many equations and many periods. This yields an important distinction:

> a VAR coefficient represents one local lagged relationship, while an impulse response traces the full dynamic path generated as the shock repeatedly moves through the system.

This is one reason macroeconomists often care more about **impulse responses** than about individual VAR coefficients.

### 4.8 Direct and Indirect Dynamic Effects

To see why, suppose an unexpected policy movement affects output:

$$
PolicyRate_t
\rightarrow
GDPGrowth_{t+1}
$$

Then output affects inflation:

$$
GDPGrowth_{t+1}
\rightarrow
Inflation_{t+2}
$$

Inflation may then affect future policy:

$$
Inflation_{t+2}
\rightarrow
PolicyRate_{t+3}
$$

The original shock therefore continues to propagate through the system. Conceptually:

$$
Shock_t
\rightarrow
Y_{t+1}
\rightarrow
X_{t+2}
\rightarrow
Z_{t+3}
\rightarrow
\cdots
$$

A single regression coefficient does not summarize this full sequence. Dynamic systems create:

* direct effects,
* indirect effects,
* delayed effects,
* feedback effects.

The relevant substantive object may therefore be the **entire response path** generated by the system.

### 4.9 Lag Length

A practical issue in VAR analysis is choosing:

$$
p
$$

the number of lags. If too few lags are included, relevant dynamics may be omitted. For example, suppose output depends on the policy rate from four quarters earlier:

$$
GDPGrowth_t
=

\alpha
+
\beta PolicyRate_{t-4}
+
\varepsilon_t
$$

A model containing only one lag may fail to capture that delayed relationship. But including too many lags also creates problems. Suppose we have:

$$
K
$$

variables and:

$$
p
$$

lags. Each equation contains approximately:

$$
Kp
$$

lag coefficients, before including constants or other deterministic terms. With:

$$
K=5
$$

variables and:

$$
p=8
$$

lags, each equation already contains:

$$
5\times8=40
$$

lagged coefficients. This can consume statistical power quickly, particularly when the time series is short. The lag choice therefore involves a tradeoff:

> **Too few lags may omit important dynamics; too many lags may produce imprecise and unstable estimates.**

In applied work, economists may use:

* economic reasoning,
* information criteria,
* residual diagnostics,
* sensitivity analysis.

The conceptual point is more important than any one mechanical selection rule. The lag structure should be rich enough to represent the plausible economic dynamics without overwhelming the available data.

### 4.10 Stability of a VAR

The stationarity discussion from Section 2 now becomes important. Consider the VAR(1):

$$
\mathbf{y}_t
=

A\mathbf{y}_{t-1}
+
\mathbf{u}_t
$$

Repeated substitution gives:

$$
\mathbf{y}_{t+1}
=

A\mathbf{y}*t
+
\mathbf{u}_{t+1}
$$

so that a shock today propagates through:

$$
A
$$

then:

$$
A^2
$$

then:

$$
A^3
$$

and so on. For a stable VAR, the effect of a temporary shock should eventually disappear. Informally:

$$
A^h\rightarrow0
$$

as:

$$
h\rightarrow\infty
$$

The same intuition underlies VAR stability: shocks die out when the dynamic system is stable. The formal stability condition involves the eigenvalues of the VAR system. For the purposes of this learning guide, the intuition is sufficient:

> **A stable VAR is one in which temporary disturbances do not generate endlessly exploding responses.**

If the system is unstable or contains unit-root behavior, the interpretation of dynamic responses changes substantially.

### 4.11 Why Stationarity Must Be Considered Before Interpretation

Suppose a VAR contains:

$$
GDP_t
$$

and:

$$
PriceLevel_t
$$

both of which trend strongly through time. Estimating relationships among such variables without considering their time-series properties can produce misleading results. By contrast, a system using:

$$
GDPGrowth_t
$$

and:

$$
Inflation_t
$$

may have very different statistical properties. This does not imply that macroeconomists should always difference every variable. It means that the specification of a VAR must be consistent with:

* the properties of the series,
* the economic question,
* and the interpretation of long-run relationships.

As in Section 2, the transformation of a variable is part of the substantive modeling decision.

### 4.12 The Residual Vector

After using past information to predict the current variables, the remaining unexplained movements are collected in:

$$
\mathbf{u}_t
$$

For our three-variable system:

$$
\mathbf{u}_t
=

\begin{bmatrix}
u_{GDP,t} \\
u_{\pi,t} \\
u_{i,t}
\end{bmatrix}
$$

These residuals can be interpreted as **innovations relative to the model's information set**. For example:

$$
u_{\pi,t}>0
$$

means inflation was higher than the VAR predicted using the included lags. Similarly:

$$
u_{i,t}>0
$$

means the policy rate was unexpectedly high relative to the model's forecast. But there is an important complication. These innovations may occur at the same time. An unexpected inflation increase may coincide with an unexpected interest-rate increase. This creates **contemporaneous correlation**.

### 4.13 Contemporaneous Correlation

Suppose:

$$
Cov(u_{\pi,t},u_{i,t})\neq0
$$

This means inflation and interest-rate innovations are correlated within the same period. More generally, the residual covariance matrix is:

$$
\Sigma_u
=

E[\mathbf{u}_t\mathbf{u}_t']
$$

For two variables:

$$
\Sigma_u
=

\begin{bmatrix}
Var(u_{1,t})
&
Cov(u_{1,t},u_{2,t})
\\
Cov(u_{2,t},u_{1,t})
&
Var(u_{2,t})
\end{bmatrix}
$$

If the off-diagonal elements are nonzero:

$$
Cov(u_{1,t},u_{2,t})\neq0
$$

then the residuals are contemporaneously correlated. This is a central complication of VAR analysis because the raw innovations are then statistically entangled.

### 4.14 Why Contemporaneous Correlation Creates an Interpretation Problem

Return to monetary policy. Suppose the VAR estimates:

$$
u_{i,t}>0
$$

meaning the policy rate is unexpectedly high. At the same time:

$$
u_{\pi,t}>0
$$

meaning inflation is unexpectedly high. What happened? One possibility is:

$$
\text{Exogenous Policy Tightening}
\rightarrow
\text{Higher Policy Rate}
$$

But another is:

$$
\text{Unexpected Inflation News}
\rightarrow
\text{Central Bank Raises Rate}
$$

Or both could be responding to a third development. The observed policy-rate residual therefore may not represent a pure policy intervention. The residuals are statistically useful, but their economic meaning remains ambiguous. This creates a central identification problem:

> **How can we separate correlated reduced-form innovations into economically meaningful structural shocks?**

That question will eventually motivate structural VAR identification.

### 4.15 The VAR Does Not Automatically Resolve Simultaneity

One reason VARs are attractive is that they treat several variables as jointly endogenous. But this should not be confused with solving all endogeneity problems. A reduced-form VAR can model:

$$
Inflation_{t-1}
\rightarrow
PolicyRate_t
$$

and:

$$
PolicyRate_{t-1}
\rightarrow
Inflation_t
$$

at the same time. This is useful for representing feedback. But contemporaneous relationships remain unresolved. If $Inflation_t$, and:

$$
PolicyRate_t
$$

move together during the same quarter, the reduced-form model alone may not tell us which structural shock generated those movements. Thus:

> **Modeling endogeneity dynamically is not the same as causally identifying structural shocks.**

This distinction is fundamental to empirical macroeconomics.

### 4.16 Prediction Versus Structural Interpretation

A VAR can be useful even without structural identification. Suppose past:

* output growth,
* inflation,
* and interest rates

contain useful information about future inflation. Then the VAR can be used for forecasting:

$$
E[\mathbf{y}_{t+h}\mid\mathcal{I}_t]
$$

where:

$$
\mathcal{I}_t
$$

represents the information available at time $t$. Forecasting does not necessarily require us to determine whether every innovation has a clean causal interpretation. But a question such as:

> What would happen to output if the central bank exogenously tightened monetary policy?

is fundamentally different. That question requires a structural interpretation. The distinction is:

#### Reduced-form question

> Given the historical relationships in the system, what tends to happen after an unexpected movement in the policy-rate equation?

#### Structural question

> What happens after an exogenous monetary-policy shock?

The second requires additional assumptions.

### 4.17 Running Application: A Three-Variable Monetary VAR

Suppose we estimate:

$$
\mathbf{y}_t
=

\begin{bmatrix}
GDPGrowth_t \\
Inflation_t \\
PolicyRate_t
\end{bmatrix}
$$

using the VAR:

$$
\mathbf{y}_t
=

\mathbf{c}
+
A_1\mathbf{y}_{t-1}
+
A_2\mathbf{y}_{t-2}
+
\mathbf{u}_t
$$

The system can capture several relationships.

#### Output persistence

$$
GDPGrowth_{t-1}
\rightarrow
GDPGrowth_t
$$

#### Inflation persistence

$$
Inflation_{t-1}
\rightarrow
Inflation_t
$$

#### Monetary-policy reaction

$$
Inflation_{t-1}
\rightarrow
PolicyRate_t
$$

#### Delayed policy transmission

$$
PolicyRate_{t-1}
\rightarrow
GDPGrowth_t
$$

#### Output-inflation interaction

$$
GDPGrowth_{t-1}
\rightarrow
Inflation_t
$$

These relationships allow the model to represent macroeconomic feedback. But suppose the estimated residuals during a particular quarter are:

$$
\mathbf{u}_t
=

\begin{bmatrix}
-0.4 \\
0.3 \\
0.5
\end{bmatrix}
$$

This means, relative to the model's predictions:

* output growth was unexpectedly weak,
* inflation was unexpectedly high,
* the policy rate was unexpectedly high.

Can we conclude that the policy-rate innovation caused the other two movements? No. The innovations occurred within the same period, and the reduced-form VAR alone does not identify their causal ordering. That is the next conceptual problem we need to solve.

### 4.18 VAR Coefficients Versus Impulse Responses

Suppose the policy-rate coefficient in the output equation is:

$$
a_{13}=-0.2
$$

This tells us something about the relationship between:

$$
PolicyRate_{t-1}
$$

and:

$$
GDPGrowth_t
$$

conditional on the other lagged variables. But suppose the policy movement also affects inflation, which then affects future policy, which then affects future output. The total dynamic consequence cannot be read from:

$$
a_{13}
$$

alone. We need to trace how an initial disturbance propagates through:

$$
A_1,A_2,\dots,A_p
$$

over several horizons. This motivates the **impulse response function**. Conceptually, an impulse response asks:

> If a particular shock occurs today, what path does each variable in the system follow afterward?

That will be the focus of Section 5.

### 4.19 Common Mistakes

**Mistake 1 — Treating a VAR as automatically causal**

A VAR represents dynamic relationships among variables. It does not automatically identify structural causal effects.

**Mistake 2 — Interpreting one VAR coefficient as the total effect of a shock**

A coefficient captures one local lagged relationship. Dynamic effects propagate through the entire system.

**Mistake 3 — Assuming the variables are independent because they have separate equations**

The equations form one connected system. The variables are jointly modeled.

**Mistake 4 — Ignoring contemporaneous residual correlation**

Unexpected movements can occur together within the same period. This makes raw residuals difficult to interpret structurally.

**Mistake 5 — Calling the policy-rate residual a monetary-policy shock**

A residual is unexpected relative to the model. It is not automatically an exogenous structural intervention.

**Mistake 6 — Including arbitrary numbers of lags**

Lag structure affects both the ability to capture dynamics and the precision of estimates.

**Mistake 7 — Ignoring the time-series properties of the variables**

A VAR estimated on unstable or inappropriate transformations can produce misleading dynamic interpretations.

**Mistake 8 — Assuming “endogenous variables” means the endogeneity problem is solved**

Treating variables jointly allows feedback to be modeled. It does not itself provide causal identification.

### 4.20 Application and Evaluation Checklist

When evaluating a VAR, ask:

#### Variables

1. What variables are included in the system?
2. Why are these variables economically relevant?
3. Are important variables omitted?
4. Are the variables measured at compatible frequencies?

#### Time-series properties

5. Are the variables stationary or otherwise appropriately modeled?
6. Are there trends or structural breaks?
7. Is the system plausibly stable over the sample?

#### Dynamics

8. How many lags are included?
9. Why is that lag structure plausible?
10. Are important delayed effects likely to be omitted?
11. Is the model becoming too parameter-heavy for the sample size?

#### Interpretation

12. What does an individual VAR coefficient represent?
13. Does the researcher mistakenly interpret coefficients as total dynamic effects?
14. What information is contained in the residual vector?

#### Contemporaneous relationships

15. Are residuals correlated within the same period?
16. Could several economic shocks be occurring simultaneously?
17. Can any individual residual be given a structural economic interpretation without additional assumptions?

#### Causal claims

18. Is the VAR being used descriptively, predictively, or structurally?
19. What additional identification argument would be needed for causal interpretation?
20. Is the researcher distinguishing reduced-form dynamics from structural economic mechanisms?

### 4.21 Summary

A **vector autoregression** extends the autoregressive framework to several jointly evolving variables. A VAR with $p$ lags can be written as:

$$
\mathbf{y}_t
=

\mathbf{c}
+
A_1\mathbf{y}_{t-1}
+
A_2\mathbf{y}_{t-2}
+
\cdots
+
A_p\mathbf{y}_{t-p}
+
\mathbf{u}_t
$$

Each variable can depend on:

* its own history,
* and the histories of the other variables in the system.

This makes VARs useful for studying macroeconomic environments characterized by:

* persistence,
* delayed effects,
* feedback,
* and joint determination.

However, the reduced-form residuals:

$$
\mathbf{u}_t
$$

are simply innovations relative to the model's predictions. They may be contemporaneously correlated:

$$
Cov(u_{i,t},u_{j,t})\neq0
$$

and therefore may represent mixtures of several underlying economic shocks. A VAR coefficient tells us about one part of the lagged dynamic system. It does not summarize the full response to a disturbance. To study how a shock propagates through the system, we need to move from individual coefficients to **dynamic response paths**. That is the role of impulse response functions.

> **Central Lesson:**
> **A VAR provides a flexible representation of how macroeconomic variables interact through time, but it does not automatically reveal causal mechanisms. The model describes reduced-form dynamics; structural interpretation requires us to identify what the underlying economic shocks actually are.**

## 5. Impulse Responses and Dynamic Effects

### 5.1 From a Single Effect to a Dynamic Response Path

In many causal settings, we summarize the effect of a treatment using a single parameter:

$$
\tau
$$

For example:

$$
\tau = E[Y(1)-Y(0)]
$$

This is useful when the effect can reasonably be summarized as one difference between treated and untreated outcomes. Macroeconomic effects are often more complicated. A shock that occurs today may affect the economy:

* immediately,
* one quarter later,
* several quarters later,
* and possibly years into the future.

The relevant causal object is therefore not necessarily one number. Instead, we may care about an entire sequence of effects:

$$
\tau_0,\tau_1,\tau_2,\dots,\tau_H
$$

where:

$$
\tau_h
$$

represents the effect at horizon $h$. For example, after a monetary-policy tightening:

* financial markets may react immediately,
* consumption and investment may respond after several months,
* output may weaken later,
* inflation may respond only after an additional delay.

The empirical question is therefore:

> **How does the effect of a shock evolve through time?**

This motivates the concept of an **impulse response function**.

### 5.2 What Is an Impulse Response Function?

An **impulse response function**, or IRF, traces the path of one or more variables after a one-time shock. For a VAR(1):

$$
\mathbf{y}_t
=

A\mathbf{y}_{t-1}
+
\mathbf{u}_t
$$

suppose a shock:

$$
\mathbf{s}
$$

occurs at time $t$. The response at horizon $h$ can be written as:

$$
IRF(h)=A^h\mathbf{s}
$$

The shock occurs once. The dynamic structure of the model then propagates its effects into future periods. An IRF asks how the system responds over future periods after a one-time disturbance. The important distinction is:

> **The impulse occurs once, but the response can continue for many periods.**

### 5.3 A Simple Autoregressive Example

Consider:

$$
y_t=\phi y_{t-1}+\varepsilon_t
$$

Suppose:

$$
\varepsilon_t=1
$$

in the current period. The immediate effect is:

$$
IRF(0)=1
$$

One period later:

$$
IRF(1)=\phi
$$

Two periods later:

$$
IRF(2)=\phi^2
$$

Three periods later:

$$
IRF(3)=\phi^3
$$

and more generally:

$$
IRF(h)=\phi^h
$$

If $|\phi|<1$, then:

$$
\phi^h\rightarrow0
$$

and the effect eventually disappears. For example, if:

$$
\phi=0.5
$$

then:

$$
IRF(0)=1
$$

$$
IRF(1)=0.5
$$

$$
IRF(2)=0.25
$$

$$
IRF(3)=0.125
$$

The effect decays rapidly. If instead:

$$
\phi=0.95
$$

the response disappears much more slowly. This connects impulse responses directly to the persistence concepts introduced in Section 2.

### 5.4 Impulse Responses in a Multivariate System

The idea becomes more useful in a VAR because a shock to one variable can affect several variables. Consider:

$$
\mathbf{y}_t
=

\begin{bmatrix}
GDPGrowth_t\\
Inflation_t\\
PolicyRate_t
\end{bmatrix}
$$

Suppose there is a one-time monetary-policy shock. We may want to trace:

$$
IRF_{Rate}(h)
$$

$$
IRF_{GDP}(h)
$$

and:

$$
IRF_{\pi}(h)
$$

for:

$$
h=0,1,2,\dots,H
$$

The policy-rate response tells us how persistent the initial tightening is. The output response tells us how economic activity changes over time. The inflation response tells us whether prices respond immediately or with a delay. The full set of impulse responses therefore describes how one disturbance propagates throughout the system.

> **Identification checkpoint — which impulse is being applied?** A multivariate IRF is not automatically a structural causal response. Before interpreting impact, delay, persistence, or cumulative effects, ask whether the initial innovation is merely a reduced-form forecast error or has already been mapped into an economically meaningful structural shock. Section 5.13 develops this issue explicitly, and Chapters 6–7 provide the identification framework.

### 5.5 Why Individual VAR Coefficients Are Not Enough

Recall the VAR:

$$
\mathbf{y}_t
=

A\mathbf{y}_{t-1}
+
\mathbf{u}_t
$$

Suppose the policy-rate coefficient in the output equation is negative. That tells us something about the relationship between past policy rates and current output. But suppose an interest-rate movement also changes inflation:

$$
PolicyRate_t
\rightarrow
Inflation_{t+1}
$$

and inflation then changes future monetary policy:

$$
Inflation_{t+1}
\rightarrow
PolicyRate_{t+2}
$$

which then affects future output:

$$
PolicyRate_{t+2}
\rightarrow
GDPGrowth_{t+3}
$$

The initial disturbance therefore propagates repeatedly through the system. A single coefficient captures only one component of this process. The distinction is:

> A VAR coefficient describes a local lagged relationship, while an impulse response represents the dynamic consequence of a shock as it propagates through the system.

This is why impulse responses are often the more economically meaningful object.

### 5.6 Impact Effects

The response at:

$$
h=0
$$

is called the **impact response**. It asks:

> What happens in the same period in which the shock occurs?

For example:

$$
IRF_{GDP}(0)
$$

would describe the immediate output response to the identified shock. Whether an immediate response is economically plausible depends partly on the frequency of the data. With daily financial data, many variables can adjust within the same period. With quarterly macroeconomic data, some variables may plausibly react only with a delay. This is important because assumptions about contemporaneous adjustment will later become part of structural identification.

### 5.7 Delayed Responses

Many economic effects are not immediate. Suppose:

$$
IRF_{GDP}(0)\approx0
$$

but:

$$
IRF_{GDP}(2)<0
$$

and:

$$
IRF_{GDP}(4)
$$

is even more negative. This would suggest that the effect builds gradually. The economic mechanism might involve delays in:

* consumption decisions,
* investment,
* hiring,
* mortgage refinancing,
* credit conditions,
* price adjustment.

The presence of a delayed response does not imply the shock was initially ineffective. It may indicate that the transmission mechanism operates slowly.

### 5.8 Peak Effects

Researchers are often interested in the horizon at which the effect is largest. Suppose:

$$
IRF_{GDP}(1)=-0.1
$$

$$
IRF_{GDP}(2)=-0.4
$$

$$
IRF_{GDP}(4)=-0.7
$$

$$
IRF_{GDP}(8)=-0.2
$$

Then the largest contraction occurs around:

$$
h=4
$$

The **peak effect** is therefore different from the impact effect. This distinction matters because describing only the contemporaneous coefficient could severely understate the total economic importance of the shock.

### 5.9 Persistence and Mean Reversion

An impulse response also tells us how long the effect lasts. Suppose:

$$
IRF(h)\rightarrow0
$$

as:

$$
h\rightarrow\infty
$$

Then the effect eventually disappears. This is typical of a stable stationary system. By contrast, if:

$$
IRF(h)
$$

does not return toward zero, the shock may have a permanent effect on the level of the variable. This connects directly to stationarity: stable VARs generally produce decaying responses, while non-stationary processes may generate permanent effects. This means IRFs cannot be interpreted separately from the time-series properties of the model.

### 5.10 Temporary and Permanent Effects

Consider again:

$$
y_t=\phi y_{t-1}+\varepsilon_t
$$

with:

$$
|\phi|<1
$$

Then:

$$
IRF(h)=\phi^h
$$

and:

$$
\lim_{h\rightarrow\infty}IRF(h)=0
$$

The shock is temporary. Now consider a random walk:

$$
y_t=y_{t-1}+\varepsilon_t
$$

A one-unit shock permanently raises the level of $y_t$. Then:

$$
IRF(h)=1
$$

for every future horizon. So the same phrase:

> “a one-unit shock”

can have very different long-run implications depending on the underlying dynamics. This is why the distinction between stationary and non-stationary processes from Section 2 is economically important.

### 5.11 Cumulative Effects

Sometimes the total effect over several periods is more relevant than the response in any one period. Suppose:

$$
IRF(h)
$$

represents the effect on output growth. A cumulative response over horizons $0$ through $H$ can be written as:

$$
CIRF(H)
=

\sum_{h=0}^{H}IRF(h)
$$

This can help answer questions such as:

> How much cumulative output growth was lost over the first two years after the shock?

The interpretation depends on the outcome variable. A cumulative response in a growth rate is not the same object as the response of the underlying level. Again, the transformation of the variable matters.

### 5.12 Dynamic Effects as Horizon-Specific Treatment Effects

There is a useful connection between IRFs and the causal framework developed earlier in the series. Suppose:

$$
Y_{t+h}(1)
$$

represents the outcome at horizon $h$ if a shock occurs at time $t$, and:

$$
Y_{t+h}(0)
$$

represents the outcome that would have occurred without the shock. Then the horizon-specific causal effect is:

$$
\tau_h
=

E[Y_{t+h}(1)-Y_{t+h}(0)]
$$

for:

$$
h=0,1,\dots,H
$$

Conceptually, an impulse response is attempting to recover this kind of dynamic causal object. Instead of one treatment effect:

$$
\tau
$$

we want a function:

$$
\tau(h)
$$

This is one of the most important bridges between standard causal inference and empirical macroeconomics. The counterfactual logic has not changed. The causal object has simply become **dynamic**.

### 5.13 But Which Shock?

There is an important problem. Suppose the VAR residual in the policy equation is:

$$
u_{i,t}>0
$$

We could calculate what happens after this innovation. But as discussed in Section 4, the raw policy residual may be correlated with:

$$
u_{\pi,t}
$$

and:

$$
u_{GDP,t}
$$

The question:

> What happens after $u_{i,t}$ increases?

is therefore not necessarily the same as:

> What happens after an exogenous monetary-policy tightening?

This creates a distinction between:

#### Reduced-form impulse response

The response to a statistical innovation in the fitted model.

#### Structural impulse response

The response to an economically meaningful identified shock. The mathematics of propagating the shock can be straightforward. The difficult question is often deciding **what shock is being propagated**. That is why impulse-response estimation and structural identification must be kept conceptually separate.

### 5.14 Normalization of the Shock

Impulse responses also depend on how the initial shock is scaled. A researcher might report the response to:

* a one-unit shock,
* a one-standard-deviation shock,
* a 25-basis-point monetary-policy shock,
* a 1-percentage-point shock.

Suppose an interest-rate shock is normalized as:

$$
Shock_t=0.25
$$

percentage points. Then the resulting IRF answers:

> What is the estimated response following a 25-basis-point policy shock?

If another study normalizes the shock to one standard deviation, the numerical responses may differ even if the underlying model is similar. So when comparing impulse responses, always ask:

> **What is the size and unit of the initial shock?**

### 5.15 Uncertainty Around Impulse Responses

Impulse responses are estimated from data. They are therefore uncertain. Suppose the estimated response is:

$$
\widehat{IRF}(h)
$$

The true response is not known exactly. Researchers often report uncertainty bands around the estimated response. Conceptually:

$$
\widehat{IRF}(h)
\pm
\text{uncertainty}
$$

The interpretation is similar to uncertainty elsewhere in empirical economics. A visually large estimated response may still be very imprecise. A near-zero point estimate may also be consistent with economically meaningful positive or negative effects if the uncertainty interval is wide. For dynamic analysis, uncertainty often grows with the horizon because long-horizon responses depend on repeated propagation through estimated parameters.

### 5.16 Pointwise Versus Whole-Path Interpretation

An impulse response produces estimates for many horizons:

$$
h=0,1,2,\dots,H
$$

A common temptation is to inspect each horizon separately and highlight whichever periods appear statistically significant. But the response should also be interpreted as a **dynamic path**. Questions include:

* Is the overall shape economically coherent?
* Does the response persist?
* Is the peak estimate precise?
* Are results sensitive to the horizon chosen?
* Does the response consistently point in one direction?

This connects to the broader lesson from Part 3 on multiple testing and statistical uncertainty. Looking at many horizons creates many opportunities to overinterpret isolated estimates.

#### Pointwise versus simultaneous uncertainty

A confidence interval drawn separately at each horizon answers a pointwise question: how uncertain is the response at this particular horizon? That is not identical to asking whether an entire response path is jointly consistent with a null or with a particular economic shape. Because an IRF contains many related horizon-specific estimates, repeated inspection of pointwise intervals can overstate the evidentiary importance of isolated significant periods.

When the substantive claim concerns the response path as a whole, simultaneous bands or other joint inference procedures can therefore be more informative than a sequence of unrelated pointwise tests. The broader principle is to align the uncertainty statement with the economic claim being made.

### 5.17 Impulse Responses and Regime Dependence

Section 3 introduced the possibility that effects differ across economic states. We can extend the impulse-response notation accordingly. Instead of:

$$
IRF(h)
$$

we may have:

$$
IRF(h\mid S_t=s)
$$

where:

$$
S_t
$$

represents the state of the economy when the shock occurs. For example:

$$
IRF_{GDP}(h\mid Recession)
$$

may differ from:

$$
IRF_{GDP}(h\mid Expansion)
$$

This means state dependence can affect:

* the immediate response,
* the peak effect,
* persistence,
* and the speed of recovery.

The dynamic causal object is therefore potentially:

$$
\tau(h,s)
$$

rather than merely:

$$
\tau(h)
$$

### 5.18 Local Projections

Impulse responses do not have to be estimated through a VAR. An alternative approach is the **local projection**. A simple local-projection equation is:

$$
y_{t+h}
=

\alpha_h
+
\beta_h Shock_t
+
\Gamma_h X_t
+
e_{t+h}
$$

where a separate regression is estimated for each horizon:

$$
h=0,1,2,\dots,H
$$

The coefficient:

$$
\beta_h
$$

is then interpreted as the estimated response at horizon $h$. For example:

#### Horizon 0

$$
y_t
=

\alpha_0
+
\beta_0 Shock_t
+
\Gamma_0X_t
+
e_t
$$

#### Horizon 1

$$
y_{t+1}
=

\alpha_1
+
\beta_1 Shock_t
+
\Gamma_1X_t
+
e_{t+1}
$$

#### Horizon 4

$$
y_{t+4}
=

\alpha_4
+
\beta_4 Shock_t
+
\Gamma_4X_t
+
e_{t+4}
$$

The sequence:

$$
\beta_0,\beta_1,\dots,\beta_H
$$

forms the estimated dynamic response. Local projections estimate dynamic responses directly rather than through the VAR recursion.

### 5.19 VAR-Based IRFs Versus Local Projections

Both approaches can answer similar substantive questions.

#### VAR-based approach

Estimate the dynamic system:

$$
\mathbf{y}_t
=

A_1\mathbf{y}_{t-1}
+
\cdots
+
A_p\mathbf{y}_{t-p}
+
\mathbf{u}_t
$$

and use the estimated system to propagate the identified shock forward.

#### Local-projection approach

Estimate the response at each horizon directly:

$$
y_{t+h}
=

\alpha_h
+
\beta_h Shock_t
+
\Gamma_hX_t
+
e_{t+h}
$$

This means the two approaches differ primarily in **how the dynamic response is estimated**. A VAR imposes a common dynamic structure from which all horizons are generated. Local projections estimate each horizon more directly and can be more flexible. But this flexibility can come with less precision, particularly in smaller samples. The most important conceptual point is that neither method automatically solves the identification problem.

### 5.20 Estimation Is Not Identification

This distinction deserves emphasis. Suppose we estimate:

$$
y_{t+h}
=

\alpha_h
+
\beta_hShock_t
+
e_{t+h}
$$

using local projections. A beautifully estimated sequence of:

$$
\beta_h
$$

does not become causal unless:

$$
Shock_t
$$

has been credibly identified. Similarly, a sophisticated VAR does not produce a causal IRF if the shock itself is not structurally identified. The point is explicit:

> Local projections do not solve identification by themselves; the shock still needs to be causally identified.

This reflects the central philosophy of the entire series:

> **An estimator tells us how to calculate an effect. An identification strategy tells us why the effect deserves a causal interpretation.**

### 5.21 Running Application: Monetary Policy

Return to the question:

> **What happens to output and inflation after an unexpected monetary-policy tightening?**

Suppose an identified shock raises the policy rate by 25 basis points at time:

$$
t=0
$$

We might estimate responses over:

$$
h=0,1,\dots,12
$$

quarters. A hypothetical output response could look conceptually like:

| Horizon | Output Response |
| ------- | --------------: |
| 0       |            0.00 |
| 1       |           -0.10 |
| 2       |           -0.30 |
| 4       |           -0.60 |
| 8       |           -0.25 |
| 12      |            0.00 |

This would suggest:

* little immediate output response,
* gradually increasing contraction,
* a peak decline around four quarters,
* eventual recovery.

Inflation might respond even more slowly. For example:

| Horizon | Inflation Response |
| ------- | -----------------: |
| 0       |               0.00 |
| 1       |              -0.05 |
| 2       |              -0.10 |
| 4       |              -0.25 |
| 8       |              -0.35 |
| 12      |              -0.15 |

The precise numbers are not important here. The point is that the relevant economic object is a **path**, not one coefficient.

### 5.22 Interpreting the Running Application Carefully

Even if the estimated response looks plausible, several questions remain.

#### What exactly was the shock?

Was it:

$$
u_{Policy,t}
$$

from a reduced-form VAR? Or was it an identified monetary-policy shock?

#### How large was the shock?

Was the IRF normalized to:

$$
25
$$

basis points? One standard deviation? One percentage point?

#### Are the responses statistically precise?

Does the uncertainty interval exclude zero? At which horizons?

#### Are the dynamics stable?

Would the same response be expected in:

* a recession,
* a high-inflation period,
* a financial crisis?

#### Are the time-series properties appropriate?

Should the outcome be interpreted as:

$$
GDP_t
$$

or:

$$
GDPGrowth_t
$$

? Should inflation be modeled in levels or differences? These questions show why an IRF is not self-interpreting. The graph or response table is the end product of several earlier modeling and identification decisions.

### 5.23 Reduced-Form Versus Structural IRFs

Suppose we take a raw residual:

$$
u_{i,t}
$$

and calculate the dynamic response associated with it. This gives us information about what tends to happen after an unexpected movement in the policy-rate equation. But suppose:

$$
u_{i,t}
$$

contains both:

* an autonomous policy tightening,
* and the policy response to unexpected inflation news.

Then the resulting IRF combines different economic mechanisms. A **structural IRF** instead attempts to trace the response to a specific economically interpretable shock:

$$
\varepsilon_{MP,t}
$$

such as a monetary-policy shock. The distinction can be represented as:

$$
\mathbf{u}_t
=

B\boldsymbol{\varepsilon}_t
$$

where:

$$
\mathbf{u}_t
$$

contains reduced-form innovations and:

$$
\boldsymbol{\varepsilon}_t
$$

contains structural shocks. The IRF we ultimately care about may therefore be:

$$
IRF(h\mid\varepsilon_{MP,t})
$$

rather than:

$$
IRF(h\mid u_{i,t})
$$

But recovering:

$$
\varepsilon_{MP,t}
$$

from:

$$
\mathbf{u}_t
$$

requires an identification strategy. That will be the focus of the next two sections.


#### Four dynamic objects that should not be conflated

| Object | What it describes | Causal by itself? |
| --- | --- | --- |
| VAR coefficient | One local lagged relationship inside the dynamic system | No |
| Reduced-form innovation | A forecast error relative to the model's information set | No |
| Reduced-form IRF | How the estimated system propagates a particular statistical innovation | No |
| Structural IRF | How the system responds to an economically identified structural shock | Only to the extent that the identification strategy is credible |

Local projections change how the response path is estimated, not the requirement that the initial shock be identified when the intended interpretation is causal.

### 5.24 Common Mistakes

**Mistake 1 — Treating the impact response as the total effect**

Many macroeconomic effects emerge with substantial delays.

**Mistake 2 — Reading one VAR coefficient as an IRF**

An individual coefficient describes one relationship. An IRF traces the full propagation of a shock through the system.

**Mistake 3 — Ignoring shock normalization**

A response to a one-standard-deviation shock is not directly comparable to a response to a 25-basis-point shock unless the scaling is understood.

**Mistake 4 — Ignoring uncertainty**

A visually large IRF may be imprecisely estimated.

**Mistake 5 — Focusing selectively on significant horizons**

A response should be interpreted as a dynamic path rather than as a collection of unrelated significance tests.

**Mistake 6 — Confusing a reduced-form innovation with a structural shock**

The dynamic calculation may be correct while the economic interpretation of the shock is wrong.

**Mistake 7 — Assuming local projections solve causal identification**

Local projections provide another way of estimating dynamic responses. They do not make an endogenous shock exogenous.

**Mistake 8 — Ignoring stationarity and regime dependence**

The persistence and shape of an IRF depend on the underlying dynamics of the process.

### 5.25 Application and Evaluation Checklist

When evaluating an impulse-response analysis, ask:

#### Shock

1. What exactly is being shocked?
2. Is the shock reduced-form or structural?
3. What is its unit?
4. How is it normalized?

#### Dynamic response

5. What is the impact response?
6. When does the effect peak?
7. How persistent is it?
8. Does it return toward zero?
9. Is the effect temporary or permanent?
10. Are cumulative effects relevant?

#### Estimation

11. Is the response estimated through a VAR or local projections?
12. What assumptions does that estimator impose on the dynamics?
13. Are results sensitive to the horizon or lag structure?

#### Uncertainty

14. How precise are the estimated responses?
15. Does uncertainty increase at longer horizons?
16. Is the entire path economically meaningful, or only isolated horizons?

#### Heterogeneity

17. Could the response differ across regimes?
18. Would the effect be different in recessions and expansions?
19. Is a pooled average response masking state dependence?

#### Causal interpretation

20. Why should the initial shock be interpreted causally?
21. What identifying assumptions are required?
22. Would a different identification strategy produce a different response?

### 5.26 Summary

An impulse response function describes how the effect of a one-time shock evolves through time. For a VAR(1):

$$
\mathbf{y}_t
=

A\mathbf{y}_{t-1}
+
\mathbf{u}_t
$$

the response to a shock:

$$
\mathbf{s}
$$

at horizon $h$ can be written as:

$$
IRF(h)=A^h\mathbf{s}
$$

The IRF allows researchers to examine:

* immediate effects,
* delayed effects,
* peak responses,
* persistence,
* cumulative consequences,
* and eventual return toward baseline.

This extends the causal framework from a single treatment effect:

$$
\tau
$$

to a dynamic sequence:

$$
\tau_0,\tau_1,\dots,\tau_H
$$

or:

$$
\tau(h)
$$

Local projections provide an alternative way to estimate these horizon-specific responses:

$$
y_{t+h}
=

\alpha_h
+
\beta_hShock_t
+
\Gamma_hX_t
+
e_{t+h}
$$

But neither VARs nor local projections solve the central causal problem on their own. The crucial question remains:

> **What exactly is the shock whose dynamic response we are estimating?**

A reduced-form residual may mix several simultaneous economic disturbances. Before we can give an impulse response a structural causal interpretation, we therefore need to distinguish **reduced-form innovations from structural economic shocks**. That is the focus of Section 6.

> **Central Lesson:**
> **Dynamic economic effects are response paths rather than single coefficients. Impulse responses and local projections can estimate how effects evolve across horizons, but the causal meaning of those responses depends entirely on whether the underlying shock has been credibly identified.**

> **ACT C — FROM STATISTICAL INNOVATION TO CAUSAL SHOCK**
> Chapters 6–7 separate unexpected statistical movements from economically interpretable shocks and then examine the assumptions that can identify those shocks.

## 6. Reduced-Form and Structural Shocks

### 6.1 Why the Meaning of the Shock Matters

In the previous section, we treated the impulse response as the dynamic response to a shock. But that immediately raises a deeper question:

> **What exactly is the shock?**

This is one of the most important questions in empirical macroeconomics. A VAR may produce an unexpected movement in the policy rate. Inflation may also move unexpectedly. Output may also move unexpectedly. But these residual movements do not automatically correspond to economically meaningful shocks such as:

* a monetary-policy shock,
* a demand shock,
* a supply shock,
* a credit-supply shock,
* a financial-risk shock.

The distinction is between a **reduced-form innovation** and a **structural shock**. A reduced-form innovation is something the statistical model did not predict. A structural shock is an economically interpretable disturbance that we want to treat as a distinct causal force. Reduced-form residuals are generally mixtures of deeper structural disturbances, while structural interpretation requires additional identifying assumptions.

### 6.2 Reduced-Form Innovations

Recall the reduced-form VAR:

$$
\mathbf{y}_t
=

A_1\mathbf{y}_{t-1}
+
\cdots
+
A_p\mathbf{y}_{t-p}
+
\mathbf{u}_t
$$

where:

$$
\mathbf{u}_t
$$

is the vector of residuals. For our running application:

$$
\mathbf{y}_t
=

\begin{bmatrix}
GDPGrowth_t\\
Inflation_t\\
PolicyRate_t
\end{bmatrix}
$$

the residual vector is:

$$
\mathbf{u}_t
=

\begin{bmatrix}
u_{GDP,t}\\
u_{\pi,t}\\
u_{i,t}
\end{bmatrix}
$$

Each component tells us how much the corresponding variable differed from what the VAR predicted using past information. For example:

$$
u_{i,t}>0
$$

means the policy rate was unexpectedly high relative to the model's forecast. Similarly:

$$
u_{\pi,t}>0
$$

means inflation was unexpectedly high. These are useful statistical innovations. But they do not yet have a unique economic interpretation.

### 6.3 Unexpected Does Not Mean Exogenous

This distinction is crucial. Suppose the policy rate rises more than predicted. It is tempting to say:

> “The central bank delivered a positive monetary-policy shock.”

But the surprise could have occurred for several reasons. The central bank may have:

* unexpectedly decided to tighten policy,
* reacted to unexpectedly high inflation,
* reacted to unexpectedly strong output,
* responded to financial-market developments,
* received information about the economy that was not captured in the VAR.

So:

$$
u_{i,t}>0
$$

does not necessarily imply:

$$
\varepsilon_{MP,t}>0
$$

where:

$$
\varepsilon_{MP,t}
$$

denotes a structural monetary-policy shock. A residual is unexpected **conditional on the model**. A structural shock is intended to be unexpected for an economically meaningful reason. Those are not the same thing.

### 6.4 A Simple Example

Suppose the economy experiences unexpectedly high inflation. We could write:

$$
\varepsilon_{\pi,t}>0
$$

The central bank observes this and raises the policy rate within the same period. Then we may observe:

$$
u_{\pi,t}>0
$$

and:

$$
u_{i,t}>0
$$

at the same time. The policy-rate residual is positive. But the underlying causal sequence may be:

$$
\text{Inflation Shock}
\rightarrow
\text{Policy Response}
$$

not:

$$
\text{Monetary Policy Shock}
\rightarrow
\text{Inflation}
$$

If we simply treat:

$$
u_{i,t}
$$

as a monetary-policy shock, we could reverse the causal interpretation. This is exactly why contemporaneous residual correlation from Section 4 matters.

### 6.5 Structural Shocks

A **structural shock** is an economically meaningful disturbance that has been separated from other simultaneous disturbances using some identification argument. Examples include:

* monetary-policy shocks,
* aggregate-demand shocks,
* aggregate-supply shocks,
* productivity shocks,
* fiscal-policy shocks,
* credit-supply shocks,
* financial-risk shocks.

A structural model attempts to distinguish these underlying disturbances from the observed reduced-form innovations. We can write:

$$
\mathbf{u}_t
=

B\boldsymbol{\varepsilon}_t
$$

where:

$$
\mathbf{u}_t
$$

contains the reduced-form residuals,

$$
\boldsymbol{\varepsilon}_t
$$

contains structural shocks, and:

$$
B
$$

is the impact matrix that maps structural shocks into the observed reduced-form innovations. This decomposition separates reduced-form innovations from structural shocks.


#### A hierarchy of increasingly demanding interpretations

| Object | Meaning | What is required to obtain it? |
| --- | --- | --- |
| **Observed change** | The variable moved | Measurement |
| **Unexpected component / surprise** | The movement differed from an expectation or forecast | A clearly specified expectation or information set |
| **Reduced-form innovation** | The movement was not predicted by the estimated dynamic model | A reduced-form statistical model |
| **Structural shock** | The innovation can be interpreted as a particular exogenous economic disturbance | An explicit identification strategy plus defensible assumptions |

Each step adds information. Calling an observed change a “shock” skips the distinctions that the rest of Part 4 is designed to make explicit.

### 6.6 Interpreting the Structural Shock Vector

Suppose:

$$
\boldsymbol{\varepsilon}_t
=

\begin{bmatrix}
\varepsilon_{Demand,t}\\
\varepsilon_{Supply,t}\\
\varepsilon_{MP,t}
\end{bmatrix}
$$

Then:

$$
\varepsilon_{Demand,t}
$$

represents a demand shock,

$$
\varepsilon_{Supply,t}
$$

represents a supply shock, and:

$$
\varepsilon_{MP,t}
$$

represents a monetary-policy shock. These are not simply three residuals from three equations. They are intended to represent **distinct economic disturbances**. The observed residual vector:

$$
\mathbf{u}_t
$$

may contain mixtures of all three. For example:

$$
u_{i,t}
$$

could contain contributions from:

* a monetary-policy shock,
* a demand shock that causes the central bank to respond,
* a supply shock that alters inflation and policy simultaneously.

The structural decomposition attempts to separate these channels.

### 6.7 The Impact Matrix

The matrix:

$$
B
$$

determines how each structural shock affects each observed variable contemporaneously. Suppose:

$$
\mathbf{u}_t
=

B\boldsymbol{\varepsilon}_t
$$

with:

$$
B
=

\begin{bmatrix}
b_{11} & b_{12} & b_{13}\\
b_{21} & b_{22} & b_{23}\\
b_{31} & b_{32} & b_{33}
\end{bmatrix}
$$

Then the output residual can be written as:

$$
u_{GDP,t}
=

b_{11}\varepsilon_{Demand,t}
+
b_{12}\varepsilon_{Supply,t}
+
b_{13}\varepsilon_{MP,t}
$$

The inflation residual is:

$$
u_{\pi,t}
=

b_{21}\varepsilon_{Demand,t}
+
b_{22}\varepsilon_{Supply,t}
+
b_{23}\varepsilon_{MP,t}
$$

and the policy-rate residual is:

$$
u_{i,t}
=

b_{31}\varepsilon_{Demand,t}
+
b_{32}\varepsilon_{Supply,t}
+
b_{33}\varepsilon_{MP,t}
$$

This representation makes the problem clear:

> **One observed residual can reflect several structural shocks.**

### 6.8 Why the Structural Shocks Are Usually Normalized

Structural shocks are commonly normalized so that:

$$
E[
\boldsymbol{\varepsilon}_t
\boldsymbol{\varepsilon}_t'
]
=

I
$$

where:

$$
I
$$

is the identity matrix. This means the structural shocks are normalized to have unit variance and to be mutually uncorrelated. Then:

$$
\Sigma_u
=

BB'
$$

where:

$$
\Sigma_u
$$

is the covariance matrix of the reduced-form residuals. This relationship is useful because:

$$
\Sigma_u
$$

can be estimated from the data. But:

$$
B
$$

is not uniquely determined by:

$$
\Sigma_u
$$

alone. This is the structural identification problem.

### 6.9 The Identification Problem

Suppose we estimate:

$$
\Sigma_u
$$

from the reduced-form VAR. We know:

$$
\Sigma_u=BB'
$$

But there can be many different matrices:

$$
B
$$

that satisfy this equation. Each possible:

$$
B
$$

implies a different mapping from reduced-form residuals to structural shocks. Therefore the data alone generally do not tell us which structural decomposition is correct. This is a classic identification problem. We observe the reduced-form covariance structure. We want to recover economically meaningful shocks.

But multiple structural models can generate the same observed reduced-form relationships. So additional information is required. That information may come from:

* timing assumptions,
* zero restrictions,
* long-run restrictions,
* sign restrictions,
* external instruments,
* historical information,
* changes in volatility,
* economic theory.

These will be the focus of Section 7.

### 6.10 A Concrete Monetary-Policy Example

Suppose the VAR residuals in one quarter are:

$$
\mathbf{u}_t
=

\begin{bmatrix}
-0.4\\
0.3\\
0.5
\end{bmatrix}
$$

This tells us:

* output was unexpectedly weak,
* inflation was unexpectedly high,
* the policy rate was unexpectedly high.

Several structural stories are consistent with this pattern.

#### Story 1: Autonomous monetary tightening

The central bank unexpectedly tightens policy. This could produce:

$$
\varepsilon_{MP,t}>0
$$

and perhaps lead output to weaken.

#### Story 2: Adverse supply shock

A supply shock raises inflation and weakens output. The central bank responds by increasing rates. Then:

$$
\varepsilon_{Supply,t}>0
$$

may be the main structural disturbance.

#### Story 3: Multiple simultaneous shocks

A supply shock and an autonomous monetary-policy shock occur in the same quarter. Then the reduced-form residuals reflect both. The observed vector:

$$
\mathbf{u}_t
$$

does not tell us which story is correct. We need an identifying assumption.

### 6.11 Reduced-Form IRFs Versus Structural IRFs

This distinction carries directly into impulse-response analysis. Suppose we calculate the dynamic response to:

$$
u_{i,t}
$$

This gives a response to an unexpected movement in the policy-rate equation. But if:

$$
u_{i,t}
$$

contains several structural disturbances, then the response mixes those shocks together. A structural IRF instead traces the response to:

$$
\varepsilon_{MP,t}
$$

alone. Conceptually:

#### Reduced-form response

$$
IRF(h\mid u_{i,t})
$$

#### Structural response

$$
IRF(h\mid\varepsilon_{MP,t})
$$

The structural response is usually the object of interest when the research question is causal. For example:

> What happens to output after an exogenous monetary-policy tightening?

requires:

$$
IRF_{GDP}(h\mid\varepsilon_{MP,t})
$$

not merely the response to a raw residual.

### 6.12 Structural Shocks and Counterfactuals

This connects directly back to the causal framework developed earlier in the series. Suppose:

$$
Y_{t+h}(1)
$$

is output at horizon $h$ following a monetary-policy shock, and:

$$
Y_{t+h}(0)
$$

is output at the same horizon in the counterfactual world without that shock. Then the dynamic causal effect is:

$$
\tau_h
=

E[
Y_{t+h}(1)-Y_{t+h}(0)
]
$$

To estimate this effect, we need variation in monetary policy that behaves as if it were separated from the other forces affecting output. That is the role of structural identification. In this sense, empirical macroeconomics is not abandoning the logic of counterfactual causal inference. It is applying that logic to a system of dynamically interacting variables.

### 6.13 Structural Interpretation Is Stronger Than Statistical Orthogonality

Suppose a statistical transformation creates shocks that are mutually uncorrelated:

$$
Cov(\varepsilon_{1,t},\varepsilon_{2,t})=0
$$

That alone does not prove that:

$$
\varepsilon_{1,t}
$$

is a monetary-policy shock and:

$$
\varepsilon_{2,t}
$$

is a demand shock. Statistical orthogonality is not the same as economic interpretation. The shocks need to be linked to economic concepts through restrictions or external evidence. For example, if a shock:

* raises interest rates,
* lowers output,
* lowers inflation,

one might interpret it as contractionary monetary policy. But that interpretation depends on the identifying restrictions used to construct the shock. A mathematically valid decomposition is not automatically an economically valid decomposition.

### 6.14 Statistical Shocks Versus Economic Mechanisms

Another useful distinction is between identifying a shock and identifying the full mechanism through which that shock operates. Suppose we credibly identify:

$$
\varepsilon_{MP,t}
$$

and find:

$$
IRF_{GDP}(h)<0
$$

The result may support the claim:

> Monetary-policy tightening reduces economic activity.

But it does not necessarily tell us whether the effect operates primarily through:

* household borrowing,
* housing,
* business investment,
* bank credit,
* exchange rates,
* expectations.

Shock identification establishes the source of the disturbance. Mechanism identification is an additional empirical question. This is similar to earlier causal-inference settings where identifying a treatment effect does not automatically identify every mediating channel.

### 6.15 Exogeneity in Structural Macroeconomics

The word **exogenous** requires care. A monetary-policy shock is not necessarily exogenous in the sense that monetary policy itself is unrelated to the economy. Ordinary policy decisions are highly endogenous. Central banks respond to:

* inflation,
* output,
* unemployment,
* financial conditions,
* expectations.

The structural shock is intended to isolate the component of policy variation that is not explained by those endogenous responses. Schematically:

$$
Policy_t
=

SystematicResponse_t
+
StructuralShock_t
$$

or:

$$
i_t
=

f(Information_t)
+
\varepsilon_{MP,t}
$$

The object of interest is:

$$
\varepsilon_{MP,t}
$$

not the entire observed policy movement. This distinction is central to empirical monetary economics.

### 6.16 Policy Rules and Policy Shocks

Suppose the central bank follows a simplified policy rule:

$$
i_t
=

\alpha
+
\beta_{\pi}\pi_t
+
\beta_y y_t
+
\varepsilon_{MP,t}
$$

The terms:

$$
\beta_{\pi}\pi_t
$$

and:

$$
\beta_y y_t
$$

represent systematic policy responses to economic conditions. The remaining component:

$$
\varepsilon_{MP,t}
$$

represents an unsystematic policy disturbance. If inflation increases and the central bank raises rates according to its normal reaction function, that policy movement is not necessarily the structural shock we want. The shock is the deviation from that systematic response. Conceptually:

$$
\text{Observed Rate Change}
=

\text{Endogenous Policy Response}
+
\text{Policy Shock}
$$

This decomposition is much closer to the causal object of interest.

### 6.17 Information Sets Matter

Calling something “unexpected” always depends on an information set. Suppose the VAR uses:

$$
\mathcal{I}_{t-1}
$$

the information available through the previous period. Then:

$$
u_{i,t}
$$

is unexpected relative to:

$$
\mathcal{I}_{t-1}
$$

But the central bank may observe information during period $t$ that the model does not include. So what appears to be a policy surprise to the econometric model may actually be a systematic response to contemporaneous information. This means:

> **A model residual can be unpredictable from the econometrician's information set without being exogenous to the economy.**

This is another reason structural identification is needed.

### 6.18 Anticipation and Structural Shocks

Expectations create another complication. Suppose the central bank announces today that interest rates will rise next quarter. Households and firms may react immediately. Then the economic shock may occur at the **announcement date**, not when the policy rate mechanically changes. If researchers identify shocks using the observed policy change alone, they may misdate the intervention. This is one motivation for identification strategies that use:

* announcement surprises,
* financial-market reactions,
* high-frequency event windows.

The empirical object is often the **new information** revealed by the policy action, not the mechanical movement of the policy variable itself. We will return to this in Section 7.

### 6.19 Structural Shocks Can Be Defined in Different Ways

Even when researchers agree that they want a “monetary-policy shock,” they may operationalize that concept differently. One study might define the shock as:

* an unexpected short-term interest-rate increase.

Another might use:

* a surprise in futures prices around central-bank announcements.

Another might identify:

* an innovation to a monetary-policy rule.

Another might impose:

* sign restrictions on several macroeconomic variables.

These approaches may recover different empirical objects. So when reading a structural macroeconomic study, do not ask only:

> “Did they identify a monetary-policy shock?”

Ask:

> **How exactly did they define and identify that shock?**

The label alone is not enough.

### 6.20 Running Application: What Is the Monetary-Policy Shock?

Return to our system:

$$
\mathbf{y}_t
=

\begin{bmatrix}
GDPGrowth_t\\
Inflation_t\\
PolicyRate_t
\end{bmatrix}
$$

Suppose we estimate a reduced-form VAR and recover:

$$
\mathbf{u}_t
$$

We ultimately want:

$$
\varepsilon_{MP,t}
$$

But the raw policy innovation:

$$
u_{i,t}
$$

may contain:

$$
u_{i,t}
=

b_{31}\varepsilon_{Demand,t}
+
b_{32}\varepsilon_{Supply,t}
+
b_{33}\varepsilon_{MP,t}
$$

The central empirical problem is therefore to isolate:

$$
\varepsilon_{MP,t}
$$

from the mixture. If we can do that credibly, then we can estimate:

$$
IRF_{GDP}(h\mid\varepsilon_{MP,t})
$$

and:

$$
IRF_{\pi}(h\mid\varepsilon_{MP,t})
$$

and interpret them structurally. Without that step, the dynamic responses remain primarily reduced-form relationships.

### 6.21 Why This Is an Identification Problem Rather Than an Estimation Problem

Suppose we have an enormous dataset and estimate the reduced-form VAR with almost no sampling uncertainty. We may know:

$$
A_1,\dots,A_p
$$

and:

$$
\Sigma_u
$$

extremely precisely. But the problem:

$$
\Sigma_u=BB'
$$

can still admit multiple possible:

$$
B
$$

matrices. More data may reduce **estimation uncertainty**. It does not necessarily resolve **identification uncertainty**. This is a fundamental distinction.

#### Estimation question

> How precisely can we estimate the reduced-form relationships?

#### Identification question

> Which structural model generated those reduced-form relationships?

The second requires assumptions or additional variation. This mirrors the broader causal-inference principle established throughout the series:

> **More data cannot substitute for a missing identification argument.**

### 6.22 Common Mistakes

**Mistake 1 — Equating a VAR residual with a structural shock**

A residual is an innovation relative to the model. It may contain several structural disturbances.

**Mistake 2 — Treating unexpected variation as automatically exogenous**

A surprise may reflect an endogenous reaction to information omitted from the model.

**Mistake 3 — Assuming uncorrelated shocks are economically identified**

Statistical orthogonalization does not automatically attach meaningful economic labels to the shocks.

**Mistake 4 — Ignoring the central bank's reaction function**

Observed policy changes contain systematic responses to economic conditions as well as policy shocks.

**Mistake 5 — Confusing shock identification with mechanism identification**

Identifying a monetary-policy shock does not automatically reveal the channel through which monetary policy affects output.

**Mistake 6 — Ignoring the information set**

A surprise to the econometrician may not be a surprise to policymakers or private agents.

**Mistake 7 — Ignoring anticipation**

The economically relevant shock may occur when new information is revealed rather than when the policy variable formally changes.

**Mistake 8 — Assuming more data solve structural identification**

Precise reduced-form estimates do not uniquely determine the structural model.

**Mistake 9 — Using structural labels without explaining the restrictions**

Calling something a “demand shock” or “monetary shock” is not an identification argument.

### 6.23 Application and Evaluation Checklist

When evaluating a claimed structural shock, ask:

#### Reduced-form object

1. What is the underlying reduced-form model?
2. What residual or innovation does the model recover?
3. Relative to what information set is that innovation unexpected?
4. Are the residuals contemporaneously correlated?

#### Structural interpretation

5. What economic shock does the researcher want to identify?
6. Why is the reduced-form residual not sufficient?
7. What other structural shocks could contaminate it?
8. How is the structural shock formally defined?

#### Identification

9. What separates the desired shock from the other disturbances?
10. What restrictions are imposed on the impact matrix?
11. Are those restrictions economic, statistical, historical, or external?
12. Could an alternative set of restrictions produce a different shock?

#### Timing and expectations

13. When does the relevant economic information arrive?
14. Could agents anticipate the intervention?
15. Is the shock dated at the policy action or at the information revelation?

#### Causal interpretation

16. Is the identified shock plausibly exogenous to the outcome innovations?
17. Does the identification strategy isolate the shock or merely orthogonalize residuals?
18. Is the researcher identifying the causal effect of the shock, or also claiming to identify the transmission mechanism?

#### Robustness

19. Does the interpretation survive alternative identification schemes?
20. Are conclusions sensitive to how the structural shock is defined?

### 6.24 Summary

A reduced-form VAR produces innovations:

$$
\mathbf{u}_t
$$

that represent movements not predicted by the model's included history. But those innovations generally do not correspond one-to-one with economically meaningful shocks. Instead, we can write:

$$
\mathbf{u}_t
=

B\boldsymbol{\varepsilon}_t
$$

where:

$$
\boldsymbol{\varepsilon}_t
$$

contains structural disturbances such as:

* demand shocks,
* supply shocks,
* monetary-policy shocks.

Under the common normalization:

$$
E[
\boldsymbol{\varepsilon}_t
\boldsymbol{\varepsilon}_t'
]
=

I
$$

we obtain:

$$
\Sigma_u=BB'
$$

But the observed covariance matrix:

$$
\Sigma_u
$$

does not usually identify a unique:

$$
B
$$

Therefore the mapping from reduced-form innovations to structural shocks requires additional assumptions or external information. For our monetary-policy application, the distinction is:

$$
u_{i,t}
$$

is an unexpected movement in the policy-rate equation, while:

$$
\varepsilon_{MP,t}
$$

is the structural monetary-policy shock we actually want to interpret causally. The first is estimated statistically. The second must be identified. This leads directly to the next question:

> **What assumptions or sources of external variation allow economists to recover structural shocks from reduced-form macroeconomic data?**

That is the subject of Section 7: **Structural Identification in Empirical Macroeconomics**.

> **Central Lesson:**
> **Reduced-form innovations are statistical surprises; structural shocks are economically interpretable causal disturbances. The data can reveal the former without uniquely revealing the latter. Structural interpretation therefore requires an explicit identification argument.**

## 7. Structural Identification in Empirical Macroeconomics

> **Identification family 0 — Framing the problem.** Before choosing a method, distinguish what the reduced form reveals from what remains structurally unidentified.

### 7.1 The Central Identification Question

The previous section established the key structural problem. A reduced-form VAR gives us innovations:

$$
\mathbf{u}_t
$$

but the economically meaningful shocks we care about are:

$$
\boldsymbol{\varepsilon}_t
$$

linked through:

$$
\mathbf{u}_t
=

B\boldsymbol{\varepsilon}_t
$$

The empirical challenge is to recover the structural shocks from the reduced-form residuals. This requires answering:

> **What assumptions or external information allow us to interpret one component of the observed variation as a particular economic shock?**

This is the macroeconomic version of the identification problem developed earlier in the series. The fundamental logic has not changed. We still need to ask:

1. What is the causal object?
2. What variation identifies it?
3. Why should that variation be interpreted as exogenous?
4. What assumptions are required?
5. How could those assumptions fail?
6. What evidence could support or weaken the identification argument?

The main difference is that the object being identified is now often a **structural shock inside a dynamic system**.

### 7.2 Why Reduced-Form Information Is Not Enough

Recall:

$$
\Sigma_u=BB'
$$

where:

$$
\Sigma_u
$$

is the covariance matrix of the reduced-form residuals. The data allow us to estimate:

$$
\Sigma_u
$$

But many possible matrices:

$$
B
$$

may satisfy:

$$
\Sigma_u=BB'
$$

Each candidate:

$$
B
$$

implies a different interpretation of the underlying structural shocks. Suppose:

$$
\boldsymbol{\varepsilon}_t
=

\begin{bmatrix}
\varepsilon_{Demand,t}\\
\varepsilon_{Supply,t}\\
\varepsilon_{MP,t}
\end{bmatrix}
$$

The reduced-form data alone do not tell us which combination of residual movements should be labeled:

* demand,
* supply,
* monetary policy.

We must impose additional identifying information. Structural identification is therefore the set of restrictions or external sources of variation that allow reduced-form innovations to be given an economic interpretation.

### 7.3 Identification Is an Economic Argument

It is tempting to think of structural identification as a technical matrix problem. But the deeper question is economic. Suppose a researcher says:

> “This is a monetary-policy shock.”

The correct response is:

> **Why?**

What feature of the research design allows that interpretation? Possible answers include:

* output cannot respond within the same period,
* the shock must increase interest rates and reduce inflation,
* a particular external instrument isolates policy surprises,
* a historically known episode represents an unusually exogenous policy action,
* high-frequency market movements around an announcement isolate unexpected policy news.

Each answer supplies a different identification argument. The quality of the causal interpretation therefore depends on the credibility of that argument. This is exactly analogous to earlier methods in the series. An instrumental-variable estimate is not credible because it uses IV. It is credible if the instrument satisfies a convincing relevance and exclusion argument.

A regression-discontinuity design is not credible because it contains a cutoff. It is credible if treatment changes at the cutoff while other potential determinants evolve smoothly. Likewise:

> **A structural VAR is not causal because it is labeled “structural.”**

It becomes structurally interpretable only through its identifying assumptions.

> **Identification family I — Restrictions on contemporaneous and dynamic responses.** Recursive orderings, short-run restrictions, long-run restrictions, and sign restrictions identify shocks by ruling out particular response patterns.

### 7.4 Recursive Identification

One of the simplest and most common identification strategies is **recursive identification**, often implemented using a Cholesky decomposition. The basic idea is to impose an ordering on the variables that restricts which variables can respond contemporaneously to which shocks. Suppose:

$$
\mathbf{y}_t
=

\begin{bmatrix}
GDPGrowth_t\\
Inflation_t\\
PolicyRate_t
\end{bmatrix}
$$

and we order the variables as:

$$
GDPGrowth_t
\rightarrow
Inflation_t
\rightarrow
PolicyRate_t
$$

A recursive structure may imply that:

* output does not respond contemporaneously to inflation or policy shocks,
* inflation can respond contemporaneously to output shocks but not to policy shocks,
* the policy rate can respond contemporaneously to both output and inflation.

This creates a lower-triangular impact matrix such as:

$$
B=
\begin{bmatrix}
b_{11} & 0 & 0\\
b_{21} & b_{22} & 0\\
b_{31} & b_{32} & b_{33}
\end{bmatrix}
$$

The zeros are identifying restrictions. They say that some structural shocks cannot affect certain variables within the same period. This is a recursive contemporaneous ordering, and its substantive interpretation depends directly on the ordering chosen.

### 7.5 Interpreting a Recursive Ordering

The ordering is not simply a computational convention. It embeds economic assumptions. Suppose:

$$
GDPGrowth_t
$$

is ordered before:

$$
PolicyRate_t
$$

This may imply that the central bank can respond to current output conditions, while output cannot respond to the policy shock within the same measurement period. Whether this is plausible depends partly on data frequency. With quarterly data, one might argue that production and spending decisions adjust only gradually. But with daily or hourly financial data, such a restriction may be much less plausible. Thus, when evaluating recursive identification, ask:

> **What contemporaneous reactions are being ruled out, and is that timing restriction economically credible at the frequency of the data?**

### 7.6 Ordering Matters

Suppose we instead order:

$$
PolicyRate_t
\rightarrow
Inflation_t
\rightarrow
GDPGrowth_t
$$

The implied contemporaneous restrictions change. The identified shocks may therefore change as well. Consequently, the resulting impulse responses can depend substantially on variable ordering. This creates a useful robustness question:

> Do the substantive conclusions survive plausible alternative orderings?

If they do not, then the identification argument may be fragile. This is the principal weakness of recursive identification: it is simple and transparent, but the results can depend heavily on the ordering assumption.

### 7.7 Short-Run Zero Restrictions

Recursive identification is one example of a broader class of **short-run restrictions**. These strategies impose assumptions that certain variables cannot respond immediately to particular structural shocks. For example:

$$
\frac{\partial GDP_t}
{\partial \varepsilon_{MP,t}}
=

0
$$

would mean:

> A monetary-policy shock has no contemporaneous effect on GDP within the period.

The restriction may be motivated by adjustment frictions. Production, investment, and hiring may take time to respond. Likewise, one might impose:

$$
\frac{\partial P_t}
{\partial \varepsilon_{MP,t}}
=

0
$$

if prices are assumed not to adjust fully within the same period. Short-run zero restrictions use theory or institutional timing to rule out immediate responses.

### 7.8 Strength of Short-Run Restrictions

The attraction of short-run restrictions is that they can be economically intuitive. Many macroeconomic variables do not adjust instantly. For example:

* wages may be fixed by contracts,
* prices may adjust infrequently,
* investment projects take time,
* production plans cannot always be changed immediately.

If these frictions are credible, contemporaneous zero restrictions may provide useful identifying information. The empirical argument becomes:

> Because variable $Y$ cannot respond within the current period to shock $\varepsilon$, contemporaneous movement in $Y$ must reflect other shocks.

That restriction helps separate the shocks.

### 7.9 Threats to Short-Run Identification

The main danger is that the assumed timing may be wrong. Suppose the data are quarterly. A quarter is long enough for many economic variables to react. If the model assumes:

$$
\frac{\partial GDP_t}
{\partial \varepsilon_{MP,t}}
=0
$$

but output actually responds within several weeks, the restriction is violated. Likewise, financial markets can often respond within minutes. Thus, the plausibility of a zero restriction depends heavily on:

* data frequency,
* institutional timing,
* information flows,
* adjustment costs.

Short-run restrictions should therefore be defended economically rather than imposed mechanically.

### 7.10 Long-Run Restrictions

Another strategy identifies structural shocks using assumptions about their **long-run effects**. Instead of saying:

> This shock cannot affect output today,

we might say:

> This shock cannot permanently affect output.

For example, suppose economic theory suggests that demand shocks can move output temporarily but do not permanently change the economy's productive capacity. Then we might impose:

$$
\lim_{h\rightarrow\infty}
IRF_{Output,Demand}(h)
=

0
$$

while allowing supply or productivity shocks to have permanent output effects. The demand-versus-supply example illustrates the logic of long-run identification.

### 7.11 Economic Logic of Long-Run Restrictions

The identifying argument may be:

* demand shocks affect utilization and spending temporarily,
* productivity shocks affect productive capacity permanently.

If the data reveal both temporary and permanent components, the long-run restriction helps separate the underlying shocks. Conceptually:

$$
\text{Temporary Output Movement}
\Rightarrow
\text{Demand Shock}
$$

while:

$$
\text{Permanent Output Movement}
\Rightarrow
\text{Supply/Productivity Shock}
$$

The economic theory supplies the distinction.

### 7.12 Threats to Long-Run Restrictions

Long-run restrictions can be powerful, but they require strong assumptions. The estimated long-run response may depend on:

* stationarity,
* cointegration,
* lag length,
* sample size,
* model specification.

And the theoretical neutrality assumption itself may be questionable. For example, a demand shock could have long-lasting effects if it changes:

* capital accumulation,
* labor-force participation,
* firm entry,
* human capital.

The distinction between temporary and permanent effects may therefore be less clean in reality than in theory. Long-run restrictions are therefore sensitive to stationarity assumptions, lag structure, and finite-sample problems.

### 7.13 Sign Restrictions

A different strategy identifies shocks using the **direction of theoretically expected responses**. Suppose we want to identify a contractionary monetary-policy shock. Economic theory might predict:

| Variable    | Expected response |
| ----------- | ----------------- |
| Policy rate | Positive          |
| Output      | Negative          |
| Inflation   | Negative          |

We therefore search for shocks satisfying:

$$
IRF_{Rate}(h)>0
$$

$$
IRF_{Output}(h)<0
$$

$$
IRF_{\pi}(h)<0
$$

over specified horizons. Instead of saying that certain responses must be exactly zero, sign restrictions impose weaker qualitative constraints. This monetary-policy example illustrates the sign-restriction approach.

### 7.14 Why Sign Restrictions Can Be Attractive

Zero restrictions can be highly rigid. For example:

$$
IRF_{GDP}(0)=0
$$

is a strong statement. A sign restriction might instead require only:

$$
IRF_{GDP}(h)\leq0
$$

for several early horizons. This allows the data greater flexibility while still using economic theory to rule out implausible structural interpretations. The identifying logic becomes:

> Among the many decompositions consistent with the reduced-form data, retain those whose responses are qualitatively consistent with the economic shock we want to identify.

### 7.15 Set Identification

Sign restrictions frequently do not produce a single unique structural model. Instead, many structural decompositions may satisfy the same sign restrictions. The shock may therefore be **set identified** rather than point identified. Instead of obtaining one:

$$
B
$$

we may obtain a set:

$$
\mathcal{B}
$$

containing many admissible structural models. This changes how results should be interpreted. Rather than:

> “The impulse response is exactly this.”

the appropriate conclusion may be:

> “The set of models consistent with our identifying restrictions implies responses within this range.”

This is a central limitation of sign restrictions.

### 7.16 Threats to Sign Restrictions

Sign restrictions depend directly on economic theory. Suppose theory predicts:

$$
Inflation\downarrow
$$

after a contractionary monetary-policy shock. But inflation may respond slowly. If the restriction is imposed too aggressively at:

$$
h=0
$$

the researcher may reject plausible models. Likewise, several different structural shocks may generate similar signs. For example, both:

* a monetary tightening,
* and a negative demand shock

might reduce output and inflation. Additional identifying information may therefore be needed to distinguish them.

> **Identification family II — External historical and market information.** Narrative restrictions, external instruments, and high-frequency surprises bring information from outside the reduced-form covariance structure.

### 7.17 Narrative Restrictions

**Narrative identification** uses historical information about particular episodes. Suppose researchers have strong external reasons to believe that a specific date contained an unusually exogenous policy action. They may impose restrictions reflecting that historical knowledge. For example:

> A known monetary-policy episode should contain a large contractionary policy shock.

Or:

> A particular quarter is known to have contained an important financial shock.

Narrative restrictions use outside historical knowledge about specific episodes to help identify structural disturbances.

### 7.18 Why Historical Information Can Help

Reduced-form data may not reveal what caused an innovation. Historical information can sometimes supply that missing interpretation. Researchers may use:

* central-bank records,
* meeting minutes,
* policy announcements,
* institutional histories,
* documented crisis events.

This is a useful reminder that empirical identification does not have to come solely from the statistical properties of the dataset. Institutional knowledge can be part of the identification strategy. That principle is consistent with the earlier parts of the series:

> **Credible causal inference often combines data with theory, institutional knowledge, and research design.**

### 7.19 Threats to Narrative Identification

The classification of episodes may itself be uncertain. Historical accounts can be:

* incomplete,
* subjective,
* revised,
* contaminated by multiple simultaneous events.

Suppose a particular date is labeled a monetary-policy shock. But the same day also contains:

* important inflation news,
* fiscal announcements,
* geopolitical developments.

Then the historical event may not isolate one clean structural disturbance. The identifying credibility depends on the quality of the historical classification.

### 7.20 External Instruments and Proxy SVARs

A particularly important modern strategy uses an **external instrument** to isolate a structural shock. Suppose:

$$
z_t
$$

is an instrument for the monetary-policy shock:

$$
\varepsilon_{MP,t}
$$

The instrument should satisfy two core requirements.

#### Relevance

$$
Cov(z_t,\varepsilon_{MP,t})\neq0
$$

The instrument must contain information about the structural shock of interest.

#### Exogeneity / exclusion

$$
Cov(z_t,\varepsilon_{Other,t})=0
$$

The instrument should not be correlated with the other structural shocks. These are the core conditions for external-instrument or proxy-SVAR identification.

### 7.21 Connection to Instrumental Variables

This should feel familiar from Part 2. The logic is essentially the same as ordinary IV. We want variation in policy that is related to the treatment component we care about but unrelated to other determinants of the outcome. In a conventional IV setting:

$$
Z
\rightarrow
D
\rightarrow
Y
$$

In a proxy-SVAR setting:

$$
z_t
\rightarrow
\varepsilon_{MP,t}
\rightarrow
\mathbf{y}_{t+h}
$$

The instrument helps isolate the structural disturbance. The notation and dynamic system are more complex, but the causal logic remains familiar.

### 7.22 Example: Monetary-Policy Surprises

Suppose:

$$
z_t
$$

measures an unexpected financial-market movement around a central-bank announcement. If $z_t$, is strongly related to genuine monetary-policy surprises, relevance may hold. If the narrow-window movement reflects only the unexpected policy component and not other macroeconomic news, exclusion may also be plausible. Then the instrument can help isolate:

$$
\varepsilon_{MP,t}
$$

from the mixture of reduced-form residuals. The identifying argument becomes much more explicit:

> Variation in the proxy isolates the component of policy news that is plausibly independent of contemporaneous demand, supply, and other macroeconomic disturbances.

### 7.23 Weak Instruments Still Matter

As in ordinary IV, relevance cannot be taken for granted. If $Cov(z_t,\varepsilon_{MP,t})$, is very weak, the instrument contains little useful information about the structural shock. This can produce:

* imprecise estimates,
* unstable inference,
* sensitivity to specification.

A sophisticated structural model does not eliminate familiar IV problems. The basic principles of identification continue to apply.

### 7.24 High-Frequency Identification

**High-frequency identification** attempts to isolate policy shocks using very narrow windows around announcements. Suppose the central bank makes an announcement at:

$$
2:00\text{ PM}
$$

Researchers might examine market movements between:

$$
1:55\text{ PM}
$$

and:

$$
2:30\text{ PM}
$$

The identifying intuition is:

> **Within a sufficiently narrow window, the primary new information affecting financial prices is the policy announcement.**

This is the core identifying logic of high-frequency identification.

### 7.25 Why Narrow Windows Help

Suppose we used daily interest-rate movements. During one full day, financial markets could respond to:

* employment reports,
* inflation releases,
* corporate news,
* geopolitical events,
* central-bank announcements.

A very narrow event window reduces the probability that many unrelated shocks occur simultaneously. This is conceptually similar to a natural experiment. The researcher tries to isolate a short period in which the relevant source of new information is unusually clear.

### 7.26 The Information-Effect Problem

High-frequency identification also has an important complication. Central-bank announcements may reveal information about more than policy. Suppose the central bank unexpectedly raises rates. Markets may infer:

> “The central bank must believe inflationary pressure is stronger than we thought.”

Then a financial-market surprise may contain both:

$$
\text{Policy Shock}
$$

and:

$$
\text{Central Bank Information Shock}
$$

The announcement reveals not only what policymakers are doing but also what they know. Thus:

$$
z_t
$$

may be correlated with information about future economic fundamentals. This threatens the clean interpretation of the instrument as a pure monetary-policy shock. Announcement windows can therefore reveal other information in addition to the policy shock.

> **Identification family III — Statistical and distributional structure.** Heteroskedasticity and non-Gaussianity use changes in variances or distributional shape to help separate shocks.

### 7.27 Identification Through Heteroskedasticity

Another strategy uses changes in the **variance of structural shocks** across periods or regimes. Suppose:

$$
\Sigma_{u,1}
=

BD_1B'
$$

during regime 1 and:

$$
\Sigma_{u,2}
=

BD_2B'
$$

during regime 2. The key assumption is that:

$$
B
$$

the transmission matrix, remains stable, while:

$$
D_1
\neq
D_2
$$

because the variances of the structural shocks change. The differences in observed covariance across regimes can then provide additional information about the underlying structural shocks. This approach is known as heteroskedasticity-based identification.

### 7.28 Intuition for Heteroskedasticity-Based Identification

Suppose monetary-policy shocks become much more volatile during one historical period, while demand and supply shocks do not. Then changes in the covariance structure of the observed residuals may reveal which component corresponds to monetary policy. In other words:

> Changes in how large different shocks are can help distinguish shocks that would otherwise be statistically entangled.

This is particularly relevant in macro-financial data where volatility can vary substantially across historical periods.

### 7.29 Main Threat

The critical assumption is that the transmission matrix remains stable:

$$
B_1=B_2=B
$$

If instead the economic structure changes across regimes:

$$
B_1\neq B_2
$$

then changes in the covariance matrix could reflect:

* different shock variances,
* different transmission mechanisms,
* or both.

This creates a direct connection to Section 3. Ironically, the regime variation that provides identification can also undermine identification if the economic transmission mechanism changes across those regimes.

### 7.30 Non-Gaussian Identification

Some approaches exploit distributional properties of the shocks. Suppose the structural disturbances are:

* statistically independent,
* and non-Gaussian.

Then methods related to statistical source separation may help recover the underlying shocks. Non-Gaussianity can help statistically unmix shocks while relying less heavily on timing restrictions. The appeal is that identification comes partly from features of the shock distributions rather than from a recursive contemporaneous ordering. But an important limitation remains. Even if the statistical procedure recovers independent components:

$$
\varepsilon_{1,t},
\varepsilon_{2,t},
\varepsilon_{3,t}
$$

we still need to determine whether they correspond economically to:

* demand,
* supply,
* monetary policy.

Statistical separation does not automatically produce economic interpretation.

> **Identification family IV — Theory, estimands, and interpretation.** Theory can discipline the admissible structural decompositions, but the resulting interpretation remains only as credible as the restrictions imposed.

### 7.31 Theory-Based Restrictions

Economic theory can provide restrictions on:

* timing,
* signs,
* long-run responses,
* policy rules,
* cross-equation relationships.

For example, a macroeconomic model may imply that a productivity shock:

$$
\varepsilon_{A,t}>0
$$

should:

* increase output,
* reduce marginal costs,
* affect real wages.

Those theoretical restrictions can be used to distinguish the productivity shock from other disturbances. Theory can discipline identification, but the structural interpretation is only as credible as the theory generating the restrictions.

### 7.32 Theory Does Not Eliminate the Need for Empirical Scrutiny

A theoretical model can produce internally coherent restrictions. But that does not prove that those restrictions describe the actual economy. Suppose theory implies:

$$
IRF_{\pi,MP}(0)<0
$$

but actual price adjustment is delayed. An overly rigid theoretical restriction could force the empirical model toward an incorrect structural decomposition. Theory should therefore be used as part of the identification argument, not as a substitute for empirical validation. Researchers should ask whether the restrictions are consistent with:

* institutional timing,
* historical evidence,
* alternative theories,
* observed behavior.

### 7.33 Different Identification Strategies Can Recover Different Shocks

This point is important. Suppose two studies both report:

> “the effect of a monetary-policy shock.”

Study A uses recursive identification. Study B uses high-frequency surprises. Study C uses sign restrictions. Study D uses an external instrument. These studies may not be estimating exactly the same empirical object. For example:

* the recursive shock may reflect residual policy movements after conditioning on lags,
* the high-frequency shock may capture announcement surprises,
* the proxy-SVAR shock may emphasize policy variation correlated with the external instrument.

Even when all are labeled:

$$
\varepsilon_{MP,t}
$$

the identifying variation can differ. Therefore disagreements among studies may reflect not merely sampling noise but differences in **what variation is being used to define the shock**. This is why the question:

> “Which method did they use?”

is less informative than:

> **“What variation identifies the shock under that method?”**

### 7.34 Identification and the Estimand

Different identification strategies can also imply different causal estimands. Suppose one instrument primarily captures large, unexpected announcement surprises. The estimated effect may be most informative about responses to that particular type of policy variation. It may not necessarily identify the effect of every possible monetary-policy adjustment. This is closely related to the IV logic introduced earlier in the series.

The source of exogenous variation determines what causal object is identified. A credible structural estimate should therefore specify:

* what shock is being isolated,
* what variation identifies it,
* and what class of interventions the result should represent.

### 7.35 Structural Identification and Regime Dependence

Section 3 introduced state dependence. Now suppose:

$$
B=B_{S_t}
$$

so the contemporaneous transmission matrix differs by regime. Then:

$$
\mathbf{u}_t
=

B_{S_t}
\boldsymbol{\varepsilon}_t
$$

A monetary-policy shock may therefore generate different immediate effects depending on whether the economy is in:

* recession,
* expansion,
* crisis,
* high-inflation regime.

This creates a more demanding identification problem. Researchers may need to identify:

1. the structural shock,
2. the regime,
3. the regime-specific transmission mechanism.

A single full-sample identification scheme may be misleading if structural relationships change substantially across states.

> **Application and evaluation.** The remaining sections compare the identification strategies, stress-test them, and apply the framework to monetary policy.

### 7.36 Running Application: Identifying a Monetary-Policy Shock

Return to our core question:

> **What happens to inflation and output after an unexpected monetary-policy tightening?**

Suppose the reduced-form VAR gives:

$$
\mathbf{u}_t
=

\begin{bmatrix}
u_{GDP,t}\\
u_{\pi,t}\\
u_{i,t}
\end{bmatrix}
$$

We want to recover:

$$
\varepsilon_{MP,t}
$$

There are several possible strategies.

#### Strategy A: Recursive identification

Order:

$$
GDPGrowth_t
\rightarrow
Inflation_t
\rightarrow
PolicyRate_t
$$

and assume output and inflation do not respond contemporaneously to a policy shock. Then identify the policy shock as the component of the policy-rate innovation orthogonal to the earlier variables in the ordering. The key question is:

> Is it plausible that GDP growth and inflation cannot react within the measurement period?

#### Strategy B: Sign restrictions

Require a contractionary monetary-policy shock to generate:

$$
PolicyRate\uparrow
$$

$$
Output\downarrow
$$

$$
Inflation\downarrow
$$

over selected horizons. The key question becomes:

> Are these response signs theoretically compelling enough to identify the shock?

#### Strategy C: External instrument

Use:

$$
z_t
$$

such as an announcement-based monetary-policy surprise. Require:

$$
Cov(z_t,\varepsilon_{MP,t})\neq0
$$

and:

$$
Cov(z_t,\varepsilon_{Other,t})=0
$$

The key question is:

> Does the instrument isolate policy news without also capturing other economic information?

#### Strategy D: High-frequency identification

Measure financial-market movements in a narrow announcement window. The key question is:

> Is the central-bank announcement really the dominant source of new information in that window?

Each strategy produces a different identification argument. No strategy is made credible merely by being technically sophisticated.

### 7.37 Comparing Identification Strategies

A useful summary is:

| Strategy                      | Main identifying information  | Central assumption                        | Primary threat                   |
| ----------------------------- | ----------------------------- | ----------------------------------------- | -------------------------------- |
| Recursive / Cholesky          | contemporaneous ordering      | some variables cannot respond immediately | incorrect ordering               |
| Short-run restrictions        | zero impact responses         | specific timing restrictions are valid    | faster adjustment than assumed   |
| Long-run restrictions         | permanent effects             | some shocks have no long-run effect       | incorrect neutrality assumptions |
| Sign restrictions             | qualitative response patterns | theory correctly predicts signs           | weak/set identification          |
| Narrative restrictions        | historical information        | episodes are correctly classified         | contamination/misclassification  |
| External instruments          | outside proxy                 | relevance and exclusion                   | weak or contaminated instrument  |
| High-frequency identification | narrow event-window surprises | little unrelated news arrives in window   | information effects              |
| Heteroskedasticity            | variance changes              | transmission matrix remains stable        | structural change across regimes |
| Non-Gaussian methods          | shock distributions           | shocks are independent/non-Gaussian       | difficult economic labeling      |
| Theory-based restrictions     | formal economic model         | theoretical restrictions are valid        | model misspecification           |

Each identification family has its own strengths and weaknesses.

### 7.38 Identification Should Be Stress-Tested

Because structural identification relies on assumptions, applied work should examine sensitivity to plausible alternatives. For example:

#### Alternative orderings

Does changing the recursive ordering materially change the IRF?

#### Alternative horizons

Do sign-restriction results depend on imposing signs for one quarter versus four?

#### Alternative instruments

Do different policy-surprise measures produce similar conclusions?

#### Alternative samples

Do results change before and after major structural breaks?

#### Alternative variable sets

Does adding financial conditions or expectations alter the estimated shock? These are not merely robustness exercises. They reveal how much of the empirical conclusion comes from:

* the data,
* versus the identifying assumptions.

### 7.39 Falsification and Supporting Evidence

Identification assumptions are often not directly testable. But researchers can still look for evidence that would make the identifying story more or less plausible. For a monetary-policy shock, useful questions might include:

* Does the shock predict the policy movement it is supposed to capture?
* Is it correlated with known inflation or output surprises?
* Does it behave differently on policy-announcement dates?
* Does it generate responses consistent with institutional knowledge?
* Is it correlated with variables that should not respond before the shock?
* Does the estimated shock line up with historically recognized policy episodes?

No single test proves validity. But a coherent body of supporting evidence can strengthen the identification argument.

### 7.40 Common Mistakes

**Mistake 1 — Treating identification as a matrix exercise**

The matrix decomposition is technical. The identifying restrictions require economic justification.

**Mistake 2 — Using Cholesky ordering without discussing what the ordering means**

A variable order implies contemporaneous restrictions. The ordering must be defended.

**Mistake 3 — Treating zero restrictions as harmless normalizations**

A restriction such as:

$$
\frac{\partial Y_t}
{\partial \varepsilon_t}
=0
$$

is an economic claim.

**Mistake 4 — Assuming long-run restrictions are automatically more credible**

Long-run effects may be difficult to estimate and may depend heavily on stationarity assumptions.

**Mistake 5 — Treating sign restrictions as point identification**

Multiple structural models may satisfy the same signs.

**Mistake 6 — Assuming an external instrument is valid because it is external to the VAR**

It still requires:

$$
Relevance
$$

and:

$$
Exclusion
$$

**Mistake 7 — Assuming narrow event windows eliminate all confounding**

Policy announcements may reveal information about the economy as well as policy.

**Mistake 8 — Ignoring structural instability**

An identification scheme requiring stable transmission may fail across regimes.

**Mistake 9 — Assuming statistically separated shocks have obvious economic labels**

Independent components are not automatically demand, supply, or monetary-policy shocks.

**Mistake 10 — Comparing structural IRFs without comparing identification schemes**

Two studies using different identifying variation may be estimating different versions of the “same” shock.

**Mistake 11 — Confusing robustness with proof**

Similar findings across specifications strengthen confidence but do not logically prove the identifying assumptions.

### 7.41 Application and Evaluation Checklist

When reading a structurally identified macroeconomic study, ask:

#### Causal object

1. What structural shock is the researcher trying to identify?
2. How is that shock defined economically?
3. What outcome response is the main estimand?
4. Over what horizons?

#### Reduced-form starting point

5. What reduced-form model is estimated?
6. What residual covariance structure must be decomposed?
7. Why can the reduced-form residual not be interpreted directly?

#### Identification

8. What exactly identifies the structural shock?
9. Is the source of identification:

* timing,
   * signs,
   * long-run behavior,
   * historical knowledge,
   * an external instrument,
   * event-window variation,
   * volatility changes,
   * or economic theory?
10. What restrictions are imposed?

#### Credibility

11. Why should those restrictions hold?
12. What institutional knowledge supports them?
13. How could they fail?
14. Are the restrictions plausible at the data frequency being used?

#### External instruments

15. If an instrument is used, is it relevant?
16. Is the exclusion restriction plausible?
17. Could the instrument capture other shocks or information?

#### Dynamic interpretation

18. Is the resulting IRF reduced-form or structural?
19. Is the shock normalization clear?
20. Are responses robust to plausible alternative identification schemes?

#### Stability

21. Could structural relationships differ across periods or regimes?
22. Does the identification strategy require a stable impact matrix?
23. Are results sensitive to sample choice?

#### Scope

24. What type of structural variation does the design identify?
25. Does the estimated effect generalize to all policy changes or only to the particular shocks isolated by the design?

### 7.42 Summary

Structural identification gives economic meaning to the dynamic relationships estimated in macroeconomic models. The reduced-form VAR provides:

$$
\mathbf{u}_t
$$

while structural analysis seeks:

$$
\boldsymbol{\varepsilon}_t
$$

through:

$$
\mathbf{u}_t
=

B\boldsymbol{\varepsilon}_t
$$

Because $\Sigma_u=BB'$, does not usually determine a unique:

$$
B
$$

additional identifying information is required. That information can come from:

* recursive timing assumptions,
* short-run zero restrictions,
* long-run restrictions,
* sign restrictions,
* narrative evidence,
* external instruments,
* high-frequency surprises,
* heteroskedasticity,
* non-Gaussianity,
* economic theory.

Each method solves the identification problem differently. And each method introduces assumptions that must be defended. The relevant question is therefore not:

> “Which structural VAR method did the researcher use?”

It is:

> **What variation or restriction identifies the structural shock, and why should that identifying information isolate the causal disturbance the researcher claims to study?**

For the monetary-policy application, identifying:

$$
\varepsilon_{MP,t}
$$

allows us to move from the reduced-form question:

> What tends to happen after an unexpected movement in the policy-rate equation?

to the structural question:

> What happens to output and inflation after an exogenous monetary-policy tightening?

Once the shock is credibly identified, VARs or local projections can be used to estimate its dynamic effects. But even then, an additional issue arises when macroeconomic evidence comes not from one economy but from **many countries, regions, firms, or financial institutions observed through time**. Those settings combine dynamic models with the panel-data complications introduced in Part 3. That is the focus of Section 8: **Macro Panels, Common Shocks, and Heterogeneous Dynamics**.

> **Central Lesson:**
> **Structural identification is the causal argument that transforms a statistical innovation into an economically meaningful shock. Different identification strategies use different assumptions and sources of variation, so the credibility of a structural impulse response depends not on the sophistication of the model, but on the credibility of the restrictions that identify the shock.**

> **ACT D — EXTENSIONS AND SYNTHESIS**
> Chapters 8–9 extend the framework across units and then assemble the complete empirical-macro reasoning process.

## 8. Macro Panels, Common Shocks, and Heterogeneous Dynamics

> **Panel foundation — what changes when there are many macroeconomic units?** Begin with the panel structure and the fact that more observations do not automatically imply more independent macroeconomic variation.

### 8.1 From One Economy to Many

So far, most of Part 4 has focused on a single dynamic economic system observed through time. For example:

$$
\mathbf{y}_t
=

\begin{bmatrix}
GDPGrowth_t\\
Inflation_t\\
PolicyRate_t
\end{bmatrix}
$$

might describe the macroeconomic dynamics of one country. But many empirical macroeconomic studies observe several economies, regions, sectors, firms, or financial institutions over time. The data then have both a cross-sectional dimension and a time dimension:

$$
\mathbf{y}_{i,t}
$$

where:

* $i$ indexes the unit,
* $t$ indexes time.

Examples include:

* inflation and output across many countries,
* employment and wages across regions,
* credit and lending across banks,
* investment and productivity across industries,
* interest rates and exchange rates across economies.

This creates a **macro panel**. A macro panel combines two sets of empirical complications:

1. the panel-data issues introduced earlier in the series,
2. the dynamic time-series issues developed in Part 4.

The researcher must therefore think simultaneously about:

* unit heterogeneity,
* time dependence,
* common shocks,
* lagged outcomes,
* dynamic responses,
* and cross-sectional dependence.

### 8.2 The Basic Panel Structure

A simple panel outcome can be written as:

$$
y_{i,t}
$$

where:

$$
i=1,\dots,N
$$

and:

$$
t=1,\dots,T
$$

A conventional panel model might be:

$$
y_{i,t}
=

\alpha_i
+
\lambda_t
+
\beta x_{i,t}
+
\varepsilon_{i,t}
$$

where:

* $\alpha_i$ represents unit-specific effects,
* $\lambda_t$ represents common time effects,
* $x_{i,t}$ is a time-varying explanatory variable,
* $\varepsilon_{i,t}$ is the remaining disturbance.

This framework is useful when the main question concerns how changes within units relate to changes in outcomes. But macroeconomic relationships are often dynamic. The current outcome may depend on past outcomes:

$$
y_{i,t}
=

\alpha_i
+
\lambda_t
+
\phi y_{i,t-1}
+
\beta x_{i,t}
+
\varepsilon_{i,t}
$$

Now the model is both:

* a panel model,
* and a dynamic model.

### 8.3 Why Macro Panels Are Not Just Larger Time Series

It might be tempting to think that adding more countries simply provides more observations. But panel dimensions do not automatically produce independent information. Suppose we observe:

$$
N=50
$$

countries during a global recession. All 50 countries may be affected by:

$$
\text{one common global shock}
$$

Their outcomes are therefore not 50 independent realizations of unrelated economic histories. Observing many units during a common global event does not imply that the dataset contains the same number of independent macroeconomic shocks. This is one of the central differences between ordinary micro panels and macro panels. Countries, regions, banks, and markets are often linked by:

* trade,
* finance,
* common monetary conditions,
* commodity prices,
* global risk,
* shared institutions,
* geopolitical events.

The cross-sectional units may therefore move together.

> **Cluster I — Heterogeneity and common shocks.** Units may differ persistently while also moving together because of shared disturbances.

### 8.4 Unit Heterogeneity

The first major issue is that macroeconomic units are different. Countries may differ in:

* institutions,
* income levels,
* financial development,
* monetary-policy frameworks,
* exchange-rate regimes,
* fiscal capacity,
* industrial structure,
* demographics.

We can represent persistent unit differences using:

$$
\alpha_i
$$

A basic model is:

$$
y_{i,t}
=

\alpha_i
+
\beta x_{i,t}
+
\varepsilon_{i,t}
$$

The role of:

$$
\alpha_i
$$

is to capture stable characteristics of unit $i$. This is the familiar fixed-effects logic from Part 3. The current source uses the same structure and emphasizes that unit effects can capture persistent differences among countries or institutions.

### 8.5 Fixed Effects in a Dynamic Macro Panel

Suppose we estimate:

$$
GDPGrowth_{i,t}
=

\alpha_i
+
\beta PolicyRate_{i,t}
+
\varepsilon_{i,t}
$$

Country fixed effects:

$$
\alpha_i
$$

remove stable differences between countries. For example, they may absorb persistent differences in:

* geography,
* legal institutions,
* average productivity,
* financial structure.

The identifying variation then comes from changes **within countries through time**. Conceptually:

> When the policy rate changes within a particular country relative to that country's usual policy environment, how does output change?

But fixed effects do not solve every confounding problem. They do not automatically remove:

* time-varying political conditions,
* financial crises,
* commodity-price shocks,
* changes in expectations,
* global monetary developments.

Dynamic macro panels therefore require additional attention to common time variation.

### 8.6 Time Fixed Effects

A common extension includes:

$$
\lambda_t
$$

so that:

$$
y_{i,t}
=

\alpha_i
+
\lambda_t
+
\beta x_{i,t}
+
\varepsilon_{i,t}
$$

Time fixed effects capture shocks common to all units during period $t$. Examples include:

* global recessions,
* pandemics,
* commodity-price shocks,
* global financial stress,
* worldwide risk-off episodes.

Time fixed effects absorb shocks that affect all units at the same date. In a cross-country monetary-policy study, time fixed effects might absorb:

$$
\text{GlobalShock}_t
$$

that affects many countries simultaneously. But there is an important limitation. Time fixed effects assume that the common shock can be represented as the same additive time effect for every unit. In reality, countries may have different exposures to the same global disturbance.

### 8.7 Common Shocks

Suppose a global financial shock occurs:

$$
f_t
$$

Country $i$ may respond according to its exposure:

$$
\gamma_i
$$

Then a residual structure could be:

$$
u_{i,t}
=

\gamma_i f_t
+
e_{i,t}
$$

where:

* $f_t$ is the common shock,
* $\gamma_i$ measures how strongly country $i$ is exposed,
* $e_{i,t}$ is the unit-specific component.

Two countries exposed to the same shock may therefore have correlated residuals:

$$
Cov(u_{i,t},u_{j,t})\neq0
$$

This dependence across units is called **cross-sectional dependence**. This matters because an apparent country-specific relationship may actually be driven by a common global disturbance.

### 8.8 Cross-Sectional Dependence

In a panel with independent units, we might imagine:

$$
Cov(u_{i,t},u_{j,t})=0
$$

for:

$$
i\neq j
$$

But this assumption is often implausible in macroeconomic data. Instead:

$$
Cov(u_{i,t},u_{j,t})\neq0
$$

may be common. For example, the United States and Canada may both experience weaker growth because of:

* a global oil shock,
* common financial conditions,
* synchronized monetary tightening,
* a global recession.

If we ignore that shared source of variation, we may overstate how much independent evidence the panel provides. Cross-sectional dependence can affect:

* standard errors,
* coefficient interpretation,
* identification,
* dynamic responses.

Common shocks can masquerade as unit-level effects if cross-sectional dependence is ignored.

> **Cluster II — Dynamic panel models and estimation.** PVARs add joint dynamics, but pooling, heterogeneity, fixed effects, and dynamic-panel bias determine what can be estimated reliably.

### 8.9 From Panel Regression to Panel VAR

Suppose each country contains several dynamically interacting variables:

$$
\mathbf{y}_{i,t}
=

\begin{bmatrix}
GDPGrowth_{i,t}\\
Inflation_{i,t}\\
PolicyRate_{i,t}
\end{bmatrix}
$$

We may want each variable to depend on the lagged values of all variables within that country. A **panel vector autoregression**, or PVAR, extends the VAR framework to multiple units. A simple PVAR can be written as:

$$
\mathbf{y}_{i,t}
=

A\mathbf{y}_{i,t-1}
+
\alpha_i
+
\lambda_t
+
\mathbf{u}_{i,t}
$$

where:

* $\mathbf{y}_{i,t}$ is the vector of variables for unit $i$,
* $A$ captures dynamic relationships,
* $\alpha_i$ captures persistent unit heterogeneity,
* $\lambda_t$ captures common time shocks,
* $\mathbf{u}_{i,t}$ contains innovations.

This is the basic panel-VAR formulation used here.

### 8.10 What a PVAR Adds

A conventional panel model might estimate:

$$
y_{i,t}
=

\alpha_i
+
\lambda_t
+
\beta x_{i,t}
+
\varepsilon_{i,t}
$$

A PVAR instead models several variables jointly:

$$
\mathbf{y}_{i,t}
=

A_1\mathbf{y}_{i,t-1}
+
\cdots
+
A_p\mathbf{y}_{i,t-p}
+
\alpha_i
+
\lambda_t
+
\mathbf{u}_{i,t}
$$

This allows:

* output to depend on past inflation,
* inflation to depend on past output,
* monetary policy to respond to both,
* all of these relationships to be estimated across multiple countries.

The PVAR therefore combines:

> **dynamic feedback within units**

with:

> **repeated observations across units.**

### 8.11 Pooled Dynamics

A simple PVAR often assumes that:

$$
A
$$

is the same across all units. For example:

$$
\mathbf{y}_{i,t}
=

A\mathbf{y}_{i,t-1}
+
\alpha_i
+
\mathbf{u}_{i,t}
$$

for every country:

$$
i
$$

This means the dynamic coefficients are pooled. The model assumes that the underlying propagation mechanism is common across countries after accounting for unit-specific intercepts. For example, the effect of past interest rates on current output is governed by the same coefficient in:

* the United States,
* Canada,
* Japan,
* Germany.

This is a pooled PVAR with common dynamic coefficients.

### 8.12 Why Pooling Can Help

Pooling can be attractive because macroeconomic time series are often relatively short. Suppose we observe:

$$
T=80
$$

quarters for each country. Estimating a large VAR separately for every country may provide limited statistical precision. By pooling countries, the researcher uses information from:

$$
N\times T
$$

observations. This can improve precision. But the gain comes from a strong assumption:

> **The relevant dynamic coefficients are sufficiently similar across units that combining them is meaningful.**

If this assumption is badly wrong, the pooled estimate may describe no country particularly well.

### 8.13 Heterogeneous Dynamics

A more flexible model allows:

$$
A_i
$$

to vary by unit:

$$
\mathbf{y}_{i,t}
=

A_i\mathbf{y}_{i,t-1}
+
\alpha_i
+
\mathbf{u}_{i,t}
$$

Now country $i$ can have its own dynamic structure. The distinction is therefore between pooled and heterogeneous PVARs. This allows the effect of a monetary-policy shock to differ because countries may have different:

* mortgage structures,
* credit markets,
* exchange-rate systems,
* central-bank credibility,
* financial institutions.

The tradeoff is familiar:

#### Pooled model

More precision, stronger homogeneity assumptions.

#### Heterogeneous model

Greater flexibility, but more parameters and often less precision.

### 8.14 Heterogeneity in Dynamic Responses

Suppose a structural monetary-policy shock has response:

$$
IRF_i(h)
$$

for country $i$. Then:

$$
IRF_{US}(h)
$$

may differ from:

$$
IRF_{Japan}(h)
$$

or:

$$
IRF_{Canada}(h)
$$

A pooled model instead estimates something closer to an average response:

$$
\overline{IRF}(h)
$$

This raises an important interpretation question:

> **Is the average dynamic response itself economically meaningful?**

Suppose one group of countries has:

$$
IRF_i(h)<0
$$

while another has:

$$
IRF_i(h)\approx0
$$

The pooled estimate may show a moderate negative effect. That estimate is not necessarily incorrect. But it may hide the most economically interesting feature of the data:

**monetary transmission is heterogeneous.**

### 8.15 Group-Specific Responses

One compromise is to estimate different dynamics for meaningful groups. For example:

$$
IRF(h\mid AdvancedEconomy)
$$

versus:

$$
IRF(h\mid EmergingEconomy)
$$

or:

$$
IRF(h\mid FixedExchangeRate)
$$

versus:

$$
IRF(h\mid FloatingExchangeRate)
$$

This connects directly to the treatment-effect heterogeneity framework from earlier sections. Instead of one response:

$$
\tau(h)
$$

we may have:

$$
\tau(h,g)
$$

where:

$$
g
$$

indexes groups. The key challenge is to make the grouping economically meaningful rather than simply dividing the sample until different effects appear.

### 8.16 Regime and Unit Heterogeneity Together

Macro panels can combine several forms of heterogeneity. The response may differ by:

* country,
* group,
* economic regime.

We might therefore write:

$$
IRF_i(h\mid S_t=s)
$$

A monetary-policy tightening could have different effects:

* across countries,
* and within the same country across different macroeconomic states.

For example:

$$
IRF_{i}(h\mid Recession)
\neq
IRF_{i}(h\mid Expansion)
$$

and:

$$
IRF_{i}(h)
\neq
IRF_{j}(h)
$$

This illustrates how quickly the empirical problem can become more complex. A single “average monetary-policy effect” may combine:

* cross-country heterogeneity,
* state dependence,
* different exposure to common shocks.

### 8.17 Dynamic-Panel Bias

Adding lagged dependent variables to a fixed-effects panel creates another technical complication. Consider:

$$
y_{i,t}
=

\alpha_i
+
\phi y_{i,t-1}
+
\varepsilon_{i,t}
$$

The lagged dependent variable:

$$
y_{i,t-1}
$$

is mechanically related to the unit-specific history. After removing fixed effects, the transformed lagged dependent variable can become correlated with the transformed error. In short panels, this can bias standard fixed-effects estimates. This is one reason dynamic panel models often require specialized estimators. Panel VARs are frequently estimated using GMM because lagged dependent variables and fixed effects can create bias in short panels.

### 8.18 GMM in Dynamic Panels

Generalized method of moments, or GMM, can use lagged variables as instruments for endogenous transformed variables. The details can become technical, but the conceptual purpose is straightforward. Suppose:

$$
y_{i,t-1}
$$

is endogenous in the transformed dynamic-panel equation. Earlier lags such as:

$$
y_{i,t-2}
$$

or:

$$
y_{i,t-3}
$$

may provide instruments under appropriate assumptions. This can help estimate the dynamic coefficients. But one distinction is crucial:

> **GMM helps address estimation and endogeneity problems in the dynamic panel equation. It does not automatically identify economically meaningful structural shocks.**

The same warning applies here.

### 8.19 Estimating Dynamic Coefficients Is Not Structural Identification

Suppose GMM allows us to estimate:

$$
A
$$

in:

$$
\mathbf{y}_{i,t}
=

A\mathbf{y}_{i,t-1}
+
\alpha_i
+
\mathbf{u}_{i,t}
$$

We may now have credible estimates of the reduced-form dynamic relationships. But the innovations:

$$
\mathbf{u}_{i,t}
$$

may still contain mixtures of structural shocks. So we still face:

$$
\mathbf{u}_{i,t}
=

B\boldsymbol{\varepsilon}_{i,t}
$$

Structural identification remains a separate problem. This distinction mirrors Section 5:

* VAR versus local projection concerns estimation of dynamic responses,
* structural identification concerns the causal meaning of the shock.

And now:

* GMM concerns estimation of dynamic-panel parameters,
* structural identification still concerns the causal meaning of the shock.

> **Cluster III — Structural identification and cross-unit transmission.** Common shocks, spillovers, and comparable structural interventions must be separated before cross-country responses receive a causal interpretation.

### 8.20 Common Shocks and Structural Identification

The structural identification problem can become more difficult in panels because shocks may have both:

* global components,
* country-specific components.

Suppose:

$$
u_{i,t}
=

\gamma_i f_t
+
e_{i,t}
$$

The common factor:

$$
f_t
$$

could represent:

* global demand,
* global financial risk,
* international monetary conditions.

The unit-specific innovation:

$$
e_{i,t}
$$

contains local movements. Now suppose country $i$ raises interest rates. If many countries simultaneously tighten monetary policy because of a global inflation shock, it would be misleading to interpret country $i$'s rate increase as an isolated structural policy shock. The researcher must distinguish:

$$
\text{Common Global Shock}
$$

from:

$$
\text{Country-Specific Structural Shock}
$$

This is why panel size alone does not solve causal identification.

### 8.21 Spillovers Across Units

Another complication arises when one unit directly affects another. Suppose US monetary policy changes. The effect may not stop at US borders. It may influence:

* foreign interest rates,
* exchange rates,
* capital flows,
* foreign output.

Then:

$$
Shock_{US,t}
\rightarrow
Y_{Canada,t+h}
$$

or:

$$
Shock_{US,t}
\rightarrow
Y_{Mexico,t+h}
$$

The units are not merely exposed to a shared global shock. They may transmit shocks directly to one another. This creates **spillovers**. A standard PVAR is often primarily designed to describe within-unit dynamics, while explicit cross-unit transmission may require richer structures.

### 8.22 A Simple Spillover Model

A model with cross-unit effects might be:

$$
\mathbf{y}_{i,t}
=

A\mathbf{y}_{i,t-1}
+
C\mathbf{y}_{-i,t-1}
+
\alpha_i
+
\mathbf{u}_{i,t}
$$

where:

$$
\mathbf{y}_{-i,t-1}
$$

summarizes relevant variables from other units. The matrix:

$$
C
$$

captures cross-unit dynamic effects. For example:

$$
USRate_t
\rightarrow
CanadianOutput_{t+1}
$$

could appear through the cross-unit component. This structure illustrates why simple PVARs may be insufficient when spillovers are substantively central.

### 8.23 Direct Effects Versus Spillover Effects

Suppose country $i$ experiences a policy shock. We may distinguish:

#### Own-country response

$$
IRF_{i\leftarrow i}(h)
$$

the response of country $i$ to its own shock.

#### Cross-country response

$$
IRF_{j\leftarrow i}(h)
$$

the response of country $j$ to the shock originating in country $i$. The second is a spillover response. This distinction matters because a policy can have:

* domestic consequences,
* international consequences.

A study estimating only the domestic response may therefore miss an important part of the total economic effect.

### 8.24 Common Shocks Versus Spillovers

These concepts are easy to confuse.

#### Common shock

A third factor affects multiple units:

$$
F_t
\rightarrow
Y_{i,t}
$$

and:

$$
F_t
\rightarrow
Y_{j,t}
$$

For example:

$$
GlobalFinancialShock_t
$$

affects both countries.

#### Spillover

A shock originating in one unit affects another:

$$
Shock_{i,t}
\rightarrow
Y_{j,t+h}
$$

These are different causal structures. If countries move together, we therefore need to ask:

> Are they jointly responding to a common shock, or is one country transmitting a shock to another?

Those interpretations can require different empirical models and identification strategies.


#### Common shocks, dependence, and spillovers compared

| Concept | Causal structure | What the data may look like | Main danger |
| --- | --- | --- | --- |
| **Common shock** | One external disturbance affects several units | Units move together at the same time | Mistaking shared exposure for independent unit-level variation |
| **Cross-sectional dependence** | Statistical dependence across units, potentially from common shocks or other links | Residuals or outcomes remain correlated across units | Treating observations as independent when they are not |
| **Spillover** | A shock originating in one unit changes outcomes in another | Unit $j$ responds after a shock in unit $i$ | Confusing transmission from $i$ to $j$ with a third common cause |

The same comovement can therefore admit different causal explanations. The empirical design must distinguish the structure generating the dependence, not merely document that the units move together.

### 8.25 Running Application: Monetary Policy Across Countries

Suppose we now observe:

$$
i=1,\dots,N
$$

countries. For each country:

$$
\mathbf{y}_{i,t}
=

\begin{bmatrix}
GDPGrowth_{i,t}\\
Inflation_{i,t}\\
PolicyRate_{i,t}
\end{bmatrix}
$$

Our original question was:

> What happens to inflation and output after an unexpected monetary-policy tightening?

The panel version becomes:

> **What happens to output and inflation after a monetary-policy shock across different countries, and how much do those responses differ?**

A simple pooled PVAR might be:

$$
\mathbf{y}_{i,t}
=

A\mathbf{y}_{i,t-1}
+
\alpha_i
+
\lambda_t
+
\mathbf{u}_{i,t}
$$

We could then estimate:

$$
IRF_{GDP}(h)
$$

and:

$$
IRF_{\pi}(h)
$$

as average responses across countries. But several new questions immediately arise.

### 8.26 Question 1: Are the Dynamic Coefficients Really Common?

The pooled model assumes:

$$
A_i=A
$$

for all:

$$
i
$$

But suppose monetary transmission depends on mortgage structure. Country A has mostly fixed-rate mortgages. Country B has mostly variable-rate mortgages. An interest-rate shock may affect household cash flow much more quickly in country B. Then:

$$
IRF_A(h)
\neq
IRF_B(h)
$$

Pooling may conceal this difference.

### 8.27 Question 2: Are There Common Global Shocks?

Suppose inflation rises in many countries simultaneously because of a global energy-price shock:

$$
f_t
$$

Central banks then tighten policy. Without adequately accounting for:

$$
f_t
$$

we might falsely attribute common output weakness to independent domestic policy shocks. This is a cross-sectional version of the endogeneity problem.

### 8.28 Question 3: Does Monetary Policy Spill Across Borders?

Suppose the US tightens monetary policy. Capital flows toward US assets. Foreign currencies depreciate. Foreign central banks may respond by raising their own interest rates. Then:

$$
\varepsilon_{MP,US,t}
$$

may affect:

$$
GDPGrowth_{j,t+h}
$$

for:

$$
j\neq US
$$

A model treating each country as an isolated unit may miss this transmission.

### 8.29 Question 4: Is the Structural Shock Comparable Across Countries?

A 25-basis-point interest-rate increase may not represent the same economic intervention everywhere. For example:

* central-bank operating frameworks differ,
* financial-market depth differs,
* policy credibility differs,
* nominal interest-rate environments differ.

Even the interpretation of:

$$
\varepsilon_{MP,i,t}
$$

may vary across countries. Thus, structural comparability is not guaranteed merely because the same variable is observed in each unit.

> **Cluster IV — Generalization, stability, and interpretation.** Average responses are useful only when their population, time-series stability, regime dependence, and identifying variation are clear.

### 8.30 Average Responses and External Validity

Suppose a pooled model estimates:

$$
\overline{IRF}_{GDP}(4)=-0.5
$$

This may represent an average response across the countries in the panel. We should then ask:

> To whom does this average response apply?

Possibilities include:

* the average country in the sample,
* countries similar to the sample,
* a specific subset of economies.

The estimate does not automatically generalize to:

* countries with radically different institutions,
* different monetary regimes,
* different stages of development.

This reconnects the panel VAR discussion to Part 3's distinction between internal and external validity. A well-identified average response in one set of countries may still have limited external validity elsewhere.

### 8.31 Panel Stationarity

The time-series properties from Section 2 also matter in panels. For:

$$
y_{i,t}
$$

stationarity can be considered within units. A simple panel process might be:

$$
y_{i,t}
=

\alpha_i
+
\varepsilon_{i,t}
$$

where each unit has its own stable mean:

$$
\alpha_i
$$

The deviations:

$$
\varepsilon_{i,t}
$$

may still be stationary. Different units may have different average levels while their within-unit deviations remain statistically stable.

### 8.32 Panel Non-Stationarity

Macro panels can be non-stationary in several ways.

#### Unit-specific trends

$$
y_{i,t}
=

\alpha_i
+
\beta_i t
+
\varepsilon_{i,t}
$$

Different countries may follow different trends.

#### Common time trends or shocks

$$
y_{i,t}
=

\alpha_i
+
\lambda_t
+
\varepsilon_{i,t}
$$

All countries may respond to common historical developments.

#### Unit roots

$$
y_{i,t}
=

y_{i,t-1}
+
\varepsilon_{i,t}
$$

#### Regime changes

$$
y_{i,t}
=

\mu_{i,S_t}
+
\varepsilon_{i,t}
$$

These forms of non-stationarity are central complications in macro panels. Thus, moving from one country to many does not eliminate the stationarity problem. It adds another dimension along which instability can occur.

### 8.33 Common Versus Unit-Specific Regimes

Regime dynamics can also operate at multiple levels.

#### Common regime

$$
y_{i,t}
=

\mu_{i,S_t}
+
\varepsilon_{i,t}
$$

All units share the same macroeconomic regime. For example:

$$
S_t=
\text{Global Financial Crisis}
$$

#### Unit-specific regime

$$
y_{i,t}
=

\mu_{i,S_{i,t}}
+
\varepsilon_{i,t}
$$

Each country may be in its own state. For example, one country may be in recession while another is expanding.

#### Mixed regime

$$
y_{i,t}
=

\mu_{i,S_t,S_{i,t}}
+
\varepsilon_{i,t}
$$

Outcomes depend on both global and local states. The relevant distinction is among common, unit-specific, and mixed panel regimes. This adds another layer to heterogeneous dynamic effects.

### 8.34 The Unit of Observation Still Matters

A macro panel may look straightforward in notation:

$$
y_{i,t}
$$

But identifying:

$$
i
$$

correctly is fundamental. Possible units include:

* countries,
* regions,
* industries,
* banks.

The interpretation of:

$$
\alpha_i
$$

and:

$$
\mathbf{u}_{i,t}
$$

depends on what the unit represents. So does the independence assumption. A panel of countries may have strong international dependence. A panel of banks may have shared exposure to the same financial system. A panel of regions may be affected by the same national monetary policy. Before estimating a dynamic panel model, therefore ask:

> **What does one observational unit represent economically?**

### 8.35 What Variation Identifies the Panel Effect?

The guiding identification question from the rest of the series remains useful. Suppose we estimate:

$$
y_{i,t}
=

\alpha_i
+
\lambda_t
+
\beta x_{i,t}
+
\varepsilon_{i,t}
$$

After including:

$$
\alpha_i
$$

and:

$$
\lambda_t
$$

what variation remains in:

$$
x_{i,t}
$$

to identify:

$$
\beta
$$

? For a dynamic panel, the same question applies. For a structural PVAR, it becomes even more demanding:

1. What variation identifies the reduced-form dynamics?
2. What variation or restrictions identify the structural shock?
3. What variation distinguishes common shocks from local shocks?
4. What variation identifies heterogeneous responses across units?

This is the panel version of the same principle used throughout the series:

> **Always ask what variation remains after the model has absorbed the controls and fixed effects.**

### 8.36 Common Mistakes

**Mistake 1 — Treating a large panel as many independent macro histories**

Many units may be exposed to the same global shocks.

**Mistake 2 — Assuming country fixed effects solve macroeconomic confounding**

Fixed effects remove stable country characteristics. They do not remove time-varying global or country-specific confounders.

**Mistake 3 — Assuming time fixed effects solve all common-shock problems**

Countries may have heterogeneous exposure to the same global shock.

**Mistake 4 — Pooling countries without examining dynamic heterogeneity**

A common:

$$
A
$$

matrix imposes common dynamics across units. That assumption should be justified.

**Mistake 5 — Interpreting a pooled IRF as representative of every unit**

An average response may conceal large country-level differences.

**Mistake 6 — Treating PVAR estimation as structural identification**

Estimating dynamic coefficients does not identify structural shocks automatically.

**Mistake 7 — Treating GMM as a causal identification strategy for the shock**

GMM can help estimate dynamic-panel parameters. It does not give an economic interpretation to the residuals.

**Mistake 8 — Ignoring cross-sectional dependence**

Residual correlation across units can invalidate simple independence assumptions.

**Mistake 9 — Confusing common shocks with spillovers**

Joint movement may reflect exposure to the same shock rather than transmission from one unit to another.

**Mistake 10 — Ignoring international or cross-unit transmission**

When spillovers are central, a model that treats units as isolated may be misspecified.

**Mistake 11 — Assuming the same policy variable represents the same structural intervention everywhere**

Institutional differences may change the meaning and transmission of the shock.

**Mistake 12 — Ignoring panel non-stationarity**

More units do not eliminate trends, unit roots, structural breaks, or regime changes.

### 8.37 Application and Evaluation Checklist

When evaluating a dynamic macro panel or PVAR, ask:

#### Panel structure

1. What does the unit index:

$$
i
$$

represent?

2. How many units are observed?
3. How long is the time dimension?
4. Are units plausibly independent?

#### Heterogeneity

5. What persistent differences exist across units?
6. Are unit fixed effects included?
7. Are dynamic coefficients assumed to be common?
8. Is that homogeneity assumption economically plausible?
9. Are group-specific or unit-specific responses important?

#### Common shocks

10. Could the units share global shocks?
11. Are time fixed effects sufficient?
12. Could exposure to common shocks differ across units?
13. Is there evidence of cross-sectional dependence?

#### Dynamics

14. Are lagged dependent variables included?
15. Is dynamic-panel bias a concern?
16. What estimator is used?
17. Why are the instruments or moment conditions valid if GMM is used?

#### Structural identification

18. Does the model identify reduced-form dynamics or structural shocks?
19. How is the structural shock isolated?
20. Is the same structural interpretation valid across all units?

#### Spillovers

21. Can shocks in one unit affect another?
22. Are observed comovements common-shock effects or true spillovers?
23. Does the model explicitly represent cross-unit transmission?

#### Stationarity and regimes

24. Are series stable within units?
25. Are there unit-specific trends?
26. Are there common structural breaks?
27. Do countries move through common or different regimes?

#### Interpretation

28. Does the reported IRF represent:

* an average response,
* a group response,
* or a unit-specific response?

29. How heterogeneous are the responses?
30. To what population of units should the result generalize?

### 8.38 Summary

Macro panels extend dynamic time-series analysis across multiple economic units. A simple dynamic panel may be written as:

$$
y_{i,t}
=

\alpha_i
+
\lambda_t
+
\phi y_{i,t-1}
+
\beta x_{i,t}
+
\varepsilon_{i,t}
$$

while a panel VAR can be written as:

$$
\mathbf{y}_{i,t}
=

A\mathbf{y}_{i,t-1}
+
\alpha_i
+
\lambda_t
+
\mathbf{u}_{i,t}
$$

This combines:

* dynamic dependence,
* unit heterogeneity,
* and common time variation.

The framework can be useful when studying economic relationships across:

* countries,
* regions,
* banks,
* industries.

But increasing the number of units does not automatically solve the empirical problems encountered in a single time series. Macro panels introduce additional challenges:

* cross-sectional dependence,
* common shocks,
* heterogeneous responses,
* dynamic-panel bias,
* spillovers,
* unit-specific regimes.

A pooled PVAR may estimate a representative dynamic response:

$$
\overline{IRF}(h)
$$

while a heterogeneous model allows:

$$
IRF_i(h)
$$

to differ across units. Neither approach automatically identifies structural shocks. Likewise, methods such as GMM can help estimate reduced-form dynamic coefficients without solving the structural identification problem. The central question remains:

> **What variation identifies the effect, what assumptions give the shock a structural interpretation, and how do common shocks, heterogeneity, and spillovers alter that interpretation?**

For our running monetary-policy application, moving from one country to many allows us to ask whether monetary transmission differs across economies. But it also forces us to distinguish:

* domestic shocks from global shocks,
* average responses from heterogeneous responses,
* common exposure from genuine cross-border spillovers.

These are the additional complications introduced by macro panels. The final section will now bring the entire Part 4 framework together through one integrated empirical exercise: starting with a dynamic causal question and moving through the data properties, dynamic model, shock identification, impulse responses, heterogeneity, uncertainty, and final causal interpretation.

> **Central Lesson:**
> **Macro panels provide additional variation across units, but they also introduce dependence, common shocks, heterogeneous dynamics, and spillovers. More observations do not substitute for identification: the researcher must still explain what variation isolates the structural shock and what population or economic environment the estimated dynamic response actually represents.**

## 9. Integrated Empirical Macro Exercise and Final Framework

### 9.1 Bringing the Pieces Together

The previous sections introduced the main building blocks of empirical macroeconomic analysis:

* dynamic causal questions,
* stationarity and persistence,
* structural breaks and regimes,
* vector autoregressions,
* impulse responses,
* reduced-form and structural shocks,
* structural identification,
* and macro panels.

These concepts are most useful when treated as parts of a single empirical argument rather than as isolated techniques. A researcher does not begin with:

> “I want to estimate a VAR.”

The researcher should begin with an economic question. The appropriate data structure, dynamic model, estimator, and identification strategy should follow from that question. We will therefore finish Part 4 by returning to the running application:

> **What happens to inflation and economic activity after an unexpected monetary-policy tightening?**

The objective is to work through the complete reasoning process from the causal question to the final interpretation.

### 9.2 Step 1: Define the Causal Question

Suppose a researcher observes that periods of high interest rates are often followed by weaker economic activity. A naive question might be:

> Are higher interest rates associated with lower output growth?

But this is not yet the causal question we care about. Central banks change interest rates in response to economic conditions. For example:

$$
Inflation_t\uparrow
\rightarrow
PolicyRate_t\uparrow
$$

and:

$$
ExpectedOutput_t\uparrow
\rightarrow
PolicyRate_t\uparrow
$$

Observed interest-rate variation therefore includes endogenous policy responses. The causal question should instead be:

> **What happens to future output and inflation when monetary policy becomes unexpectedly tighter for reasons that are distinct from the central bank's normal response to economic conditions?**

The causal object is a structural monetary-policy shock:

$$
\varepsilon_{MP,t}
$$

not simply the observed policy rate:

$$
i_t
$$

or even the observed change:

$$
\Delta i_t
$$

This distinction is fundamental.

### 9.3 Step 2: Define the Dynamic Estimand

Because the effect unfolds through time, one coefficient is not enough. For output, we may want:

$$
\tau_{GDP}(h)
=

E[GDPGrowth_{t+h}(1)-GDPGrowth_{t+h}(0)]
$$

for:

$$
h=0,1,\dots,H
$$

Similarly, for inflation:

$$
\tau_{\pi}(h)
=

E[Inflation_{t+h}(1)-Inflation_{t+h}(0)]
$$

The relevant estimand is therefore a **dynamic response path**. We want to know:

* the immediate effect,
* the delayed effect,
* the peak effect,
* how persistent the effect is,
* and whether the economy eventually returns toward its previous path.

In structural macroeconomic language, these objects are typically represented by impulse responses:

$$
IRF_{GDP}(h\mid\varepsilon_{MP})
$$

and:

$$
IRF_{\pi}(h\mid\varepsilon_{MP})
$$

The substantive question determines the horizon. For quarterly data, for example, the researcher might study:

$$
h=0,1,\dots,12
$$

quarters.

### 9.4 Step 3: Understand the Data

Suppose the researcher has 30 years of quarterly data on:

$$
GDPGrowth_t
$$

$$
Inflation_t
$$

and:

$$
PolicyRate_t
$$

Before estimating anything, we should understand what these variables represent. Questions include:

* Are the variables levels, growth rates, or changes?
* Are they measured consistently through time?
* Are there missing observations?
* Have definitions changed?
* Is quarterly frequency appropriate for the economic mechanism?

The basic data vector is:

$$
\mathbf{y}_t
=

\begin{bmatrix}
GDPGrowth_t\\
Inflation_t\\
PolicyRate_t
\end{bmatrix}
$$

But specifying the vector is only the beginning. We must understand its time-series properties.

### 9.5 Step 4: Examine Stationarity and Persistence

Before estimating dynamic responses, ask whether the statistical properties of the variables are sufficiently stable. For each variable, consider:

$$
E[y_t]
$$

$$
Var(y_t)
$$

and:

$$
Cov(y_t,y_{t-k})
$$

through time. Suppose GDP growth appears to fluctuate around a relatively stable mean. Inflation may be persistent but mean-reverting. The policy rate may also display substantial persistence. A simple representation might be:

$$
i_t
=

\alpha
+
\phi i_{t-1}
+
\varepsilon_t
$$

with:

$$
|\phi|<1
$$

but:

$$
\phi
$$

close to one. Then monetary conditions may remain elevated for several quarters even after a one-time disturbance. This matters because persistence affects the shape of the eventual impulse response.

### 9.6 Levels Versus Growth Rates

Suppose the researcher instead uses the level of GDP:

$$
GDP_t
$$

The series may display a strong long-run trend. GDP growth:

$$
\Delta\log(GDP_t)
$$

may have very different statistical properties. Similarly:

$$
PriceLevel_t
$$

and:

$$
Inflation_t
$$

are not interchangeable. The empirical specification should reflect both:

1. the time-series properties of the variable,
2. the substantive economic question.

The researcher should not difference variables mechanically simply because differencing is commonly used. Transformation changes the object being studied.

### 9.7 Step 5: Look for Structural Breaks and Regimes

Suppose the sample includes:

* low-inflation periods,
* high-inflation periods,
* recessions,
* financial crises,
* major changes in the monetary-policy framework.

Then it may be unreasonable to assume that one constant relationship governs the entire sample. A simple regime-dependent response could be written as:

$$
\tau(h,S_t)
$$

where:

$$
S_t
$$

represents the macroeconomic state. For example:

$$
IRF_{GDP}(h\mid HighInflation)
$$

may differ from:

$$
IRF_{GDP}(h\mid LowInflation)
$$

This does not mean the researcher must always estimate a regime-switching model. The important point is to ask whether structural stability is plausible. If the transmission mechanism changes across periods, a single full-sample average may hide meaningful heterogeneity.

### 9.8 Step 6: Specify the Dynamic System

Suppose the researcher chooses a VAR with two lags:

$$
\mathbf{y}_t
=

\mathbf{c}
+
A_1\mathbf{y}_{t-1}
+
A_2\mathbf{y}_{t-2}
+
\mathbf{u}_t
$$

where:

$$
\mathbf{y}_t
=

\begin{bmatrix}
GDPGrowth_t\\
Inflation_t\\
PolicyRate_t
\end{bmatrix}
$$

The model allows:

* past output to predict current output,
* past inflation to predict current inflation,
* past policy to influence current output,
* inflation to affect future policy,
* output to affect future inflation.

The VAR captures dynamic feedback. But at this stage the model is still **reduced form**. The residual vector:

$$
\mathbf{u}_t
=

\begin{bmatrix}
u_{GDP,t}\\
u_{\pi,t}\\
u_{i,t}
\end{bmatrix}
$$

contains innovations relative to the model's lagged information. These are not yet structural economic shocks.

### 9.9 Step 7: Interpret the Reduced-Form Innovations Carefully

Suppose in one quarter we observe:

$$
u_{GDP,t}<0
$$

$$
u_{\pi,t}>0
$$

$$
u_{i,t}>0
$$

This tells us that:

* output was weaker than predicted,
* inflation was higher than predicted,
* the policy rate was higher than predicted.

But several structural stories could produce this combination.

#### Possibility 1: Monetary-policy shock

The central bank unexpectedly tightens policy.

#### Possibility 2: Supply shock

A supply disturbance raises inflation and weakens output, causing the central bank to raise rates.

#### Possibility 3: Multiple shocks

A supply shock and an autonomous policy shock occur simultaneously. The reduced-form data alone do not distinguish these stories. This is why:

$$
u_{i,t}
$$

cannot automatically be interpreted as:

$$
\varepsilon_{MP,t}
$$

The central distinction remains essential here: reduced-form residuals can mix deeper structural disturbances.

### 9.10 Step 8: State the Identification Problem Explicitly

The researcher should now be able to express the central identification problem in plain language:

> **The central bank changes interest rates in response to the same economic conditions that also affect inflation and output. We therefore need a source of variation that isolates the unexpected policy component from those endogenous responses.**

Formally:

$$
\mathbf{u}_t
=

B\boldsymbol{\varepsilon}_t
$$

where:

$$
\boldsymbol{\varepsilon}_t
=

\begin{bmatrix}
\varepsilon_{Demand,t}\\
\varepsilon_{Supply,t}\\
\varepsilon_{MP,t}
\end{bmatrix}
$$

and:

$$
\Sigma_u=BB'
$$

The data identify:

$$
\Sigma_u
$$

but not generally a unique:

$$
B
$$

The structural decomposition therefore requires additional identifying information. This is the same identification problem discussed in the source material: a sophisticated model does not itself tell us how to assign economic meaning to the residual shocks.

### 9.11 Step 9: Choose an Identification Strategy

Suppose the researcher considers two possible strategies.

#### Option A: Recursive Identification

Order the variables as:

$$
GDPGrowth_t
\rightarrow
Inflation_t
\rightarrow
PolicyRate_t
$$

This might imply that within the quarter:

* monetary policy can respond to output,
* monetary policy can respond to inflation,
* output and inflation do not respond immediately to the policy shock.

The identifying assumption is therefore partly a **timing assumption**. The researcher should ask:

> Is it plausible that output and inflation cannot respond within the same quarter?

If not, the recursive structure may be inappropriate.

#### Option B: External Instrument

Suppose the researcher has a measure:

$$
z_t
$$

of unexpected financial-market movements around central-bank announcements. To identify the policy shock, the instrument should satisfy:

$$
Cov(z_t,\varepsilon_{MP,t})\neq0
$$

and:

$$
Cov(z_t,\varepsilon_{Other,t})=0
$$

The first is relevance. The second is the exclusion requirement. Now the identification argument becomes:

> The announcement surprise isolates the component of monetary-policy news that is related to the structural policy shock but unrelated to other contemporaneous macroeconomic disturbances.

But the researcher must still consider the possibility that the announcement reveals information about the central bank's economic outlook. That could violate the clean exclusion interpretation.

### 9.12 Step 10: Defend the Identification Strategy

Choosing a method is not enough. The researcher should articulate:

#### What identifies the shock?

For example:

> High-frequency interest-rate surprises around central-bank announcements.

#### Why is the variation relevant?

Because it moves strongly when policy announcements differ from market expectations.

#### Why might it be exogenous?

Because the event window is narrow enough that little unrelated macroeconomic information is expected to arrive.

#### How could the assumption fail?

Because central-bank announcements can reveal private information about economic conditions.

#### What evidence could strengthen the argument?

For example:

* weak correlation with unrelated macro news,
* robustness to narrower windows,
* consistency with historically recognized policy surprises,
* similar findings using alternative policy-surprise measures.

This is the same identification discipline developed throughout the learning series.

### 9.13 Step 11: Estimate the Dynamic Response

Once the shock has been credibly identified, the researcher can estimate the response using a VAR or local projections.

#### VAR approach

Estimate:

$$
\mathbf{y}_t
=

A_1\mathbf{y}_{t-1}
+
\cdots+
A_p\mathbf{y}_{t-p}
+
\mathbf{u}_t
$$

identify:

$$
\varepsilon_{MP,t}
$$

and propagate the shock through the system. The relevant responses are:

$$
IRF_{GDP}(h\mid\varepsilon_{MP})
$$

and:

$$
IRF_{\pi}(h\mid\varepsilon_{MP})
$$

#### Local-projection approach

Estimate for each horizon:

$$
GDPGrowth_{t+h}
=

\alpha_h
+
\beta_h\varepsilon_{MP,t}
+
\Gamma_hX_t
+
e_{t+h}
$$

and:

$$
Inflation_{t+h}
=

\delta_h
+
\theta_h\varepsilon_{MP,t}
+
\Lambda_hX_t
+
v_{t+h}
$$

The coefficients:

$$
\beta_h
$$

and:

$$
\theta_h
$$

trace the dynamic responses. The choice between VARs and local projections concerns how the response path is estimated. It does not replace identification.

### 9.14 Step 12: Interpret the Response Path

Suppose the estimated output response is:

| Horizon     | Estimated Output Response |
| ----------- | ------------------------: |
| 0 quarters  |                      0.00 |
| 1 quarter   |                     -0.10 |
| 2 quarters  |                     -0.30 |
| 4 quarters  |                     -0.55 |
| 8 quarters  |                     -0.25 |
| 12 quarters |                      0.00 |

The interpretation might be:

* little immediate response,
* gradual output contraction,
* peak effect after approximately four quarters,
* eventual return toward baseline.

Suppose inflation responds more slowly:

| Horizon     | Estimated Inflation Response |
| ----------- | ---------------------------: |
| 0 quarters  |                         0.00 |
| 1 quarter   |                        -0.02 |
| 2 quarters  |                        -0.08 |
| 4 quarters  |                        -0.18 |
| 8 quarters  |                        -0.30 |
| 12 quarters |                        -0.15 |

This would suggest slower inflation transmission. Again, the numbers are illustrative. The important lesson is that the effect is a **path through time**, not a single coefficient.

### 9.15 Step 13: Evaluate Statistical Uncertainty

The point estimates are not the full result. Suppose:

$$
\widehat{IRF}_{GDP}(4)=-0.55
$$

but the uncertainty interval is wide. Then the researcher should distinguish:

* the estimated effect,
* from the precision with which it is estimated.

For each horizon:

$$
h
$$

the relevant object is something like:

$$
\widehat{IRF}(h)
\pm
\text{uncertainty}
$$

Long-horizon responses may be especially uncertain. The researcher should therefore avoid focusing only on the most visually dramatic point estimate.

### 9.16 Step 14: Evaluate Economic Significance

Statistical significance does not tell us whether the effect is economically important. Suppose a 25-basis-point monetary-policy shock reduces output growth at its peak by:

$$
0.02
$$

percentage points. Even if this is estimated very precisely, the effect may be economically small. By contrast, an estimated effect of:

$$
-0.8
$$

percentage points may be economically substantial even if the confidence interval is relatively wide. The analysis should therefore consider both:

$$
\text{Statistical Precision}
$$

and:

$$
\text{Economic Magnitude}
$$

This reconnects the dynamic analysis to the interpretation framework developed in Part 3.

### 9.17 Step 15: Check for State Dependence

Suppose the full-sample response suggests:

$$
IRF_{GDP}(4)=-0.4
$$

But the response differs by inflation regime. For example:

$$
IRF_{GDP}(4\mid LowInflation)=-0.2
$$

and:

$$
IRF_{GDP}(4\mid HighInflation)=-0.8
$$

Then the full-sample average hides substantial heterogeneity. The empirical conclusion should not simply be:

> Monetary policy reduces output by 0.4.

A better interpretation is:

> The estimated contractionary effect appears considerably larger during high-inflation environments than during low-inflation environments.

But the researcher should still avoid claiming that high inflation itself causally produces the stronger transmission unless that mechanism has separately been identified.

### 9.18 Step 16: Consider Structural Stability

Suppose the sample covers several monetary-policy regimes. We should ask whether:

$$
B_t=B
$$

and:

$$
A_t=A
$$

are plausible throughout the entire period. If the transmission mechanism changes, then the full-sample IRF may combine different structural relationships. Possible checks include:

* subsample estimation,
* break tests,
* regime-specific responses,
* rolling estimates,
* sensitivity to sample start and end dates.

This is particularly important in macroeconomics because institutions and policy frameworks evolve.

### 9.19 Step 17: Extend the Question to a Panel Only If Needed

Suppose the researcher now observes the same variables for:

$$
N
$$

countries:

$$
\mathbf{y}_{i,t}
=

\begin{bmatrix}
GDPGrowth_{i,t}\\
Inflation_{i,t}\\
PolicyRate_{i,t}
\end{bmatrix}
$$

The question can become:

> Do different countries respond differently to monetary-policy shocks?

A PVAR might be:

$$
\mathbf{y}_{i,t}
=

A\mathbf{y}_{i,t-1}
+
\alpha_i
+
\lambda_t
+
\mathbf{u}_{i,t}
$$

But adding countries does not automatically strengthen identification. We now need to ask:

* Are the same structural shocks comparable across countries?
* Are countries exposed to common global shocks?
* Are responses heterogeneous?
* Are there spillovers?
* Does pooling impose unrealistic common dynamics?

A large panel can still contain relatively little independent macro variation when units share common shocks. The panel extension should therefore follow from the research question rather than from a desire to increase the number of observations.

### 9.20 Step 18: Distinguish Own Effects, Common Shocks, and Spillovers

In a multi-country setting, three different patterns may look similar in the data.

#### Country-specific effect

$$
\varepsilon_{MP,i,t}
\rightarrow
Y_{i,t+h}
$$

#### Common shock

$$
F_t
\rightarrow
Y_{i,t+h}
$$

and:

$$
F_t
\rightarrow
Y_{j,t+h}
$$

#### Spillover

$$
\varepsilon_{MP,i,t}
\rightarrow
Y_{j,t+h}
$$

These are not the same causal structures. A strong macro-panel analysis should distinguish them. Otherwise, comovement across countries could be incorrectly attributed to domestic policy transmission.

### 9.21 Step 19: Stress-Test the Result

A credible empirical conclusion should survive reasonable alternative choices. Possible robustness exercises include:

* alternative lag lengths,
* alternative variable transformations,
* alternative sample periods,
* alternative identification schemes,
* alternative shock measures,
* alternative normalization,
* alternative regime definitions.

For example, if the estimated monetary-policy response appears only under one highly specific Cholesky ordering and disappears under plausible alternatives, confidence in the structural interpretation should be limited. Robustness is not proof. But it helps reveal how much the result depends on specific modeling choices.

### 9.22 Step 20: State the Conclusion at the Correct Level of Strength

Suppose the researcher identifies a contractionary monetary-policy shock using high-frequency announcement surprises. The estimated response shows that output falls gradually over four quarters and inflation declines later. A careless conclusion would be:

> “Higher interest rates cause recessions and reduce inflation.”

This is too broad. The empirical design does not identify the causal effect of every possible increase in interest rates. A more disciplined conclusion is:

> **Using unexpected monetary-policy variation isolated from narrow announcement windows, the estimated dynamic responses suggest that contractionary policy shocks reduce economic activity with a delay and are followed by lower inflation over subsequent quarters.**

This statement tells the reader:

* what variation identifies the effect,
* what type of policy change is being studied,
* and what the estimated dynamic response shows.

That is much closer to the standard of causal interpretation developed throughout this series.

### 9.23 The Complete Empirical Macro Workflow

The worked exercise above contains twenty operational steps. For reuse, those steps can be compressed into a fifteen-stage empirical workflow. The purpose of the compression is not to omit reasoning, but to make the sequence visible at a glance.

| Stage | Task | Core question or decision |
| --- | --- | --- |
| 1 | Define the economic question | What intervention or shock do we want to understand? |
| 2 | Define the dynamic estimand | At which horizons do we care about the effect? The object may be written as $\tau(h)$. |
| 3 | Understand the data | What variables are observed, at what frequency, and in what units? |
| 4 | Examine time-series properties | Are the variables stationary, persistent, trending, or mean-reverting? |
| 5 | Examine structural stability | Are there structural breaks, regime changes, or state-dependent relationships? |
| 6 | Specify the dynamic system | For example, $\mathbf{y}_t=A_1\mathbf{y}_{t-1}+\cdots+A_p\mathbf{y}_{t-p}+\mathbf{u}_t$. |
| 7 | Interpret the reduced-form innovations | What does $\mathbf{u}_t$ actually represent? |
| 8 | Define the structural shock | What economically meaningful disturbance, $\boldsymbol{\varepsilon}_t$, do we want to recover? |
| 9 | State the identification strategy | What variation or restrictions allow $\mathbf{u}_t$ to be mapped into $\boldsymbol{\varepsilon}_t$? |
| 10 | Defend the identifying assumptions | Why should the restrictions be credible, and how could they fail? |
| 11 | Estimate the dynamic response | Use VAR-based IRFs, local projections, or another appropriate dynamic method. |
| 12 | Evaluate uncertainty | How precisely are the responses estimated? |
| 13 | Evaluate heterogeneity | Does $\tau(h)$ vary by regime, country, or historical period? |
| 14 | Consider common shocks and spillovers | If multiple units are observed, are they independent, or do common shocks and cross-unit transmission matter? |
| 15 | Interpret the result within its identified scope | What causal claim does the design actually support? |

The sequence is cumulative: later stages cannot repair an earlier failure to define the causal object, understand the data, or justify the identifying variation.

### 9.24 A Compact Evaluation Framework

When reading any empirical macroeconomic paper, the following questions provide a useful diagnostic framework.

#### The question

1. What economic shock or intervention is being studied?
2. What is the outcome?
3. What is the relevant time horizon?

#### The data

4. What is the unit of observation?
5. What is the frequency?
6. Are variables in levels, differences, growth rates, or returns?

#### Time-series properties

7. Are the variables stationary?
8. How persistent are they?
9. Are there structural breaks?
10. Are relationships stable across the sample?

#### The dynamic model

11. Is the model a VAR, local projection, panel model, or something else?
12. What lag structure is used?
13. What assumptions does the dynamic specification impose?

#### The shock

14. Is the shock an observed change, a reduced-form innovation, or a structural shock?
15. What economic meaning is attached to it?
16. Is that interpretation justified?

#### Identification

17. What identifies the structural shock?
18. What assumptions are required?
19. Why might those assumptions hold?
20. How could they fail?

#### Dynamic effects

21. What is the impact effect?
22. When does the effect peak?
23. How persistent is it?
24. Does it return toward zero?
25. Are cumulative effects relevant?

#### Heterogeneity

26. Do effects differ across regimes?
27. Do effects differ across countries or groups?
28. Is the reported estimate an average that hides important variation?

#### Dependence

29. Are there common shocks?
30. Are there spillovers?
31. Are the observational units genuinely independent?

#### Interpretation

32. Are the responses statistically precise?
33. Are they economically significant?
34. Are results robust to alternative identification schemes?
35. What causal claim is actually justified?

### 9.25 Final Mental Model

The entire empirical-macro framework can be compressed into one chain:

$$
\boxed{
\text{Dynamic Question}
\rightarrow
\text{Time-Series Properties}
\rightarrow
\text{Dynamic System}
\rightarrow
\text{Reduced-Form Innovation}
\rightarrow
\text{Structural Identification}
\rightarrow
\text{Dynamic Response}
\rightarrow
\text{Interpretation}
}
$$

Each step answers a different question.

#### Dynamic question

> What economic intervention or shock do we want to understand?

#### Time-series properties

> How do the variables behave through time?

#### Dynamic system

> How do the variables interact with their own histories and with one another?

#### Reduced-form innovation

> What movements were unexpected relative to the statistical model?

#### Structural identification

> Why should one of those movements be interpreted as the economic shock we care about?

#### Dynamic response

> What happens immediately and at future horizons?

#### Interpretation

> How large, uncertain, heterogeneous, and generalizable is the estimated effect?

### 9.26 How Part 4 Fits Into the Larger Series

The logic of Part 4 is not separate from the causal-inference framework developed in the earlier parts. It extends it. Part 1 established that:

$$
Correlation\neq Causation
$$

and that causal inference requires a credible counterfactual. Part 2 asked:

> **What variation identifies the effect, and why is that variation plausibly exogenous?**

Part 3 expanded the framework to:

* longitudinal and panel data,
* heterogeneity,
* internal and external validity,
* uncertainty,
* economic significance,
* and policy evaluation.

Part 4 adds:

* time-series dependence,
* persistence,
* dynamic systems,
* structural shocks,
* and effects that unfold across multiple horizons.

But the central empirical principle remains unchanged. A causal claim still requires:

$$
\text{Data}
+
\text{Economic Reasoning}
+
\text{Identification}
+
\text{Assumptions}
$$

A VAR does not create causality. An impulse-response graph does not create causality. A structural label does not create causality. A sophisticated estimator does not create causality. The causal interpretation comes from the argument explaining why the relevant variation isolates the economic shock of interest. The principle can be stated compactly:

> **A sophisticated empirical model is only as credible as the variation and assumptions that identify the effect.**

### 9.27 Final Summary

Empirical macroeconomics studies economic systems in which variables evolve through time, depend on their own histories, respond to one another, react to common shocks, and may behave differently across historical regimes. The central challenge is not merely to estimate those dynamic relationships. It is to determine which parts of the observed variation can support an economically meaningful causal interpretation.

A researcher may begin with a reduced-form system,

$$
\mathbf{y}_t
=
A_1\mathbf{y}_{t-1}
+
\cdots+
A_p\mathbf{y}_{t-p}
+
\mathbf{u}_t,
$$

and seek structural shocks satisfying

$$
\mathbf{u}_t
=
B\boldsymbol{\varepsilon}_t.
$$

Once a relevant shock $\varepsilon_t$ has been credibly identified, its effects can be traced across horizons through $IRF(h)$ or estimated directly through local projections. But estimation is only one stage of the argument. A complete interpretation must ask whether the variables are stationary, whether shocks are temporary or persistent, whether structural breaks or regimes alter the relationships, whether responses differ across states or units, what the model residual actually represents, what assumptions identify the structural shock, whether those assumptions are credible, how uncertain the resulting responses are, whether common shocks or spillovers matter, and what causal conclusion the design ultimately supports.

The purpose of the framework is therefore not simply to teach the mechanics of estimating a VAR, constructing an impulse response, or labeling a structural shock. It is to develop a disciplined way of reasoning from a dynamic economic question to a claim whose statistical, structural, and causal scope is explicit.

> **Central Lesson:**  
> **Empirical macroeconomics extends causal inference into dynamic systems. The statistical model tells us how variables evolve and interact; identification tells us which variation can be interpreted as an economic shock; impulse responses tell us how that shock propagates through time. A credible macroeconomic causal claim requires all three.**
