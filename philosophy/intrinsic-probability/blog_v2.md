# Against Intrinsic Probability

## Table of Contents

1. [What “Intrinsic Probability” Would Have to Mean](#1-what-intrinsic-probability-would-have-to-mean)
2. [Preference Is Not Probability](#2-preference-is-not-probability)
   - [From Theoretical Virtues to a Partial Order](#from-theoretical-virtues-to-a-partial-order)
   - [The Operationalization Problem](#the-operationalization-problem)
   - [From Ordinal Preference to Cardinal Probability](#from-ordinal-preference-to-cardinal-probability)
3. [The Strongest Case: Formal Simplicity and Kolmogorov Complexity](#3-the-strongest-case-formal-simplicity-and-kolmogorov-complexity)
4. [Why the Resulting Prior Is Still Not Intrinsic](#4-why-the-resulting-prior-is-still-not-intrinsic)
   - [The Hidden Meta-Theory](#the-hidden-meta-theory)
   - [Representation and Background Dependence](#representation-and-background-dependence)
   - [Dependence on the Hypothesis Space](#dependence-on-the-hypothesis-space)
5. [Objection: Bayesian Reasoning Requires Priors](#5-objection-bayesian-reasoning-requires-priors)
6. [A Better Alternative](#6-a-better-alternative)
7. [Conclusion: There Is No Probability Inside the Hypothesis](#7-conclusion-there-is-no-probability-inside-the-hypothesis)

---

## 1. What “Intrinsic Probability” Would Have to Mean

Philosophers sometimes speak of the “intrinsic probability” of a hypothesis: the probability a hypothesis possesses prior to the consideration of some body of empirical evidence. The idea is often connected to familiar theoretical virtues such as simplicity, elegance, explanatory scope, coherence, modesty, or unification. A hypothesis that is simpler, more elegant, or less ad hoc may therefore be said to possess a greater intrinsic probability than a more complicated rival, even before the relevant evidence is considered.

The terminology is tempting because it appears to fit naturally into Bayesian reasoning. If $$H$$ is a hypothesis, $$E$$ is some body of evidence, and $$K$$ represents background knowledge or assumptions, then Bayesian updating may be written as

$$
P(H\mid E,K)=\frac{P(E\mid H,K)P(H\mid K)}{P(E\mid K)}.
$$

The likelihood $$P(E\mid H,K)$$ represents how expected the evidence would be if the hypothesis were true, while the prior $$P(H\mid K)$$ represents the probability assigned to the hypothesis before the new evidence $$E$$ is incorporated. It is therefore natural to ask what determines that prior. One answer is that at least part of it is determined by features of the hypothesis itself: simpler, more coherent, or more elegant hypotheses are assigned greater prior probability because they are, in some sense, antecedently more plausible.

The difficulty is that this answer moves too quickly between several fundamentally different concepts. Simplicity is not probability. Elegance is not probability. Coherence is not probability. Nor does a preference for one theory over another, however rational that preference may be, by itself constitute a probability assignment. Theoretical virtues may provide reasons for ranking, preferring, pursuing, or provisionally adopting hypotheses, but an additional argument is needed before any such ranking can be interpreted as a measure of the probability that a hypothesis is true.

The criticism developed here is therefore deliberately narrower than a rejection of Bayesian inference or prior probabilities. It does not deny that priors may be useful, necessary, or rationally constrained, nor does it deny that theoretical virtues can play legitimate roles in scientific reasoning. The target is the stronger claim that a hypothesis possesses a determinate pre-evidential probability *in virtue of its own content or intrinsic theoretical features*.

| This essay accepts | This essay rejects |
|---|---|
| Priors can be legitimate and useful. | A prior follows from the content of $$H$$ alone. |
| Simplicity and other virtues can guide theory choice. | Simplicity or elegance is itself probabilistic. |
| Complexity-sensitive priors can be explicitly constructed. | Constructing such a prior shows that it is intrinsic to $$H$$. |
| Theoretical virtues may constrain a family of reasonable priors. | A virtue ranking automatically determines a unique credence. |

The distinction matters because probability is not simply a generic numerical expression of epistemic approval. In the standard Kolmogorov formulation, a probability space is given by

$$
(\Omega,\mathcal{F},P),
$$

where $$\Omega$$ is a space of possible outcomes, $$\mathcal{F}$$ is a collection of measurable events, and $$P$$ is a probability measure satisfying non-negativity, normalization, and countable additivity. These axioms constrain what a probability measure must be like once it has been specified. They do not tell us which admissible measure ought to be chosen.

That distinction is easy to overlook because, after a measure has been fixed, probability calculations can proceed mechanically. Yet many different measures can satisfy the same axioms over the same space. Nothing in the formalism alone determines whether a particular hypothesis should receive probability $$0.7$$, $$0.2$$, or $$10^{-6}$$. Probability theory can constrain a measure; it does not extract a unique measure from the semantic content of a proposition.

Suppose we have a space of possible hypotheses $$\mathcal{H}=\{H_1,H_2,\ldots\}$$. Assigning probabilities to those hypotheses requires a probability measure over an appropriate algebra of alternatives. The proposition $$H_i$$ does not itself supply that measure. In other words, there is no general probability-theoretic implication of the form

$$
H\Longrightarrow P(H).
$$

What is required is something more like

$$
(H,\mathcal{H},M)\longmapsto P_M(H),
$$

where $$M$$ represents whatever modeling assumptions determine the measure. Those assumptions may concern the structure of the hypothesis space, the distribution from which hypotheses are imagined to arise, the language in which they are represented, previous information, or methodological rules governing how hypotheses are weighted.

An ordinary die illustrates the point. When we write $$P(X=4)=1/6$$, the number does not arise from the proposition “the die lands on four.” It follows from a model in which the six outcomes are assigned equal probability. If the die is weighted, the event remains the same while the model changes, and so does its probability. The probability belongs to the event *under a model*, not to the linguistic or semantic content of the event in isolation.

The same point applies more strongly to hypotheses. If $$H$$ is the claim that some physical theory correctly describes a domain, what feature of that proposition determines whether its probability should be $$0.1$$ rather than $$0.01$$? Its syntax does not determine the number, nor do its truth conditions or logical form. A numerical assignment requires some additional rule connecting the hypothesis, or information about it, to a probability measure.

This is why the notation $$P(H)$$ can obscure more than it reveals in epistemic contexts. It is often more informative to write $$P(H\mid K)$$, where $$K$$ represents background knowledge and assumptions. Likewise, posterior probability is more fully written as $$P(H\mid E,K)$$. A prior is therefore prior relative to the new evidence $$E$$; it need not be prior to all assumptions whatsoever. The term $$P(H\mid K)$$ may already encode substantial commitments.

Once this is made explicit, the central question becomes clearer. If a philosopher claims that a simpler or more elegant hypothesis should receive greater prior probability, then the relevant probability is not being supplied by the hypothesis alone. It is being supplied by a methodological principle contained in $$K$$ or in some additional framework $$M$$. The more transparent expression is therefore $$P(H\mid K,M)$$. If the assignment depends on such a framework, the burden falls on the defender of intrinsic probability to explain in what meaningful sense the result remains intrinsic to $$H$$.

The thesis of this essay is that this burden cannot be met. Theoretical virtues may guide methodological evaluation, and explicit formal rules may convert such evaluations into priors. But once the machinery required to produce the prior is made visible, the resulting probability is better understood as $$P_M(H)$$: a model-relative assignment. It is not a probability contained within the proposition itself.

---

## 2. Preference Is Not Probability

Suppose hypotheses can be evaluated according to a catalogue of theoretical virtues. Let $$V=\{v_1,v_2,\ldots,v_n\}$$ represent criteria such as simplicity, coherence, explanatory scope, unification, elegance, conservatism, or absence of ad hoc assumptions. There is nothing obviously objectionable about claiming that these features provide rational grounds for preferring one hypothesis to another even before some particular body of evidence is considered. Scientific reasoning routinely includes judgments that are not reducible to direct empirical fit.

The difficulty begins when such preference is redescribed as probability. If $$H_1$$ is methodologically preferable to $$H_2$$ according to the virtue catalogue, we can represent this as $$H_1\succeq_V H_2$$. The relation may mean that $$H_1$$ is simpler, more coherent, more economical, or more attractive according to the relevant criteria. But it does not by itself entail $$P(H_1)>P(H_2)$$. The first statement expresses an evaluative relation; the second expresses an ordering induced by a probability measure.

Decision theory makes the distinction familiar. Two actions may be compared according to cost, convenience, benefit, risk, and other criteria, yielding a preference $$a_1\succ a_2$$ or perhaps a utility representation $$U(a_1)>U(a_2)$$. It would be a category mistake to infer from this that $$P(a_1)>P(a_2)$$. Utility and probability play different roles: one evaluates outcomes or choices, while the other represents uncertainty. The same conceptual separation should be preserved when hypotheses are evaluated according to theoretical virtues.

This does not mean that methodological preference can never influence credence. It means that an additional bridge principle is required. Something must justify the transition

$$
H_1\succeq_V H_2\quad\Longrightarrow\quad P(H_1)>P(H_2).
$$

That bridge is neither a theorem of probability theory nor a consequence of the concept of theoretical virtue. It is a substantive epistemological claim about why methodological attractiveness should track probability of truth.

### From Theoretical Virtues to a Partial Order

The problem becomes sharper once theoretical virtues are treated as genuinely multidimensional. Let a hypothesis be represented by a vector

$$
V(H)=\begin{pmatrix}S(H)\\U(H)\\C(H)\\E(H)\end{pmatrix},
$$

where $$S$$ represents simplicity, $$U$$ unification, $$C$$ coherence with existing knowledge, and $$E$$ elegance. One hypothesis may perform better on simplicity and coherence while another performs better on unification and elegance. In such a case, the virtues themselves do not determine which theory is better overall. The natural relation may be incomparability, $$H_1\parallel H_2$$, rather than a complete ranking.

A Pareto-style relation makes this clear. If $$H_1$$ is at least as good as $$H_2$$ on every agreed criterion and strictly better on at least one, then there is a straightforward methodological sense in which $$H_1$$ dominates $$H_2$$. But many interesting comparisons will not have this structure. If $$v_i(H_1)>v_i(H_2)$$ for some virtues while $$v_j(H_1)<v_j(H_2)$$ for others, neither hypothesis dominates. The result is a partial order rather than a total ordering.

This matters because probability imposes substantially more structure than a partial order. If one assigns $$P(H_1)=0.6$$ and $$P(H_2)=0.3$$, the hypotheses have been decisively and cardinally ranked. Yet the original virtue structure may have said only that $$H_1$$ is better in some respects and $$H_2$$ in others. Moving from that state of incomparability to a numerical ordering introduces information that was not present in the initial evaluation.

One can, of course, eliminate incomparability by assigning weights. Suppose an overall score is defined as

$$
S_M(H)=w_1v_1(H)+w_2v_2(H)+\cdots+w_nv_n(H).
$$

A complete ranking may now emerge, but only because a new layer of structure has been imposed. The weights encode tradeoffs: how much simplicity is worth relative to unification, how much coherence compensates for reduced explanatory scope, or how much elegance offsets complexity. Nothing in the virtues themselves supplies these exchange rates. The weighting scheme is a methodological decision.

This is structurally similar to multi-criteria decision analysis. Alternatives evaluated along several dimensions can often be totally ordered only after a utility function, aggregation rule, or weighting system is introduced. That procedure may be legitimate, but it should not be mistaken for discovering a scalar ordering already latent in the alternatives. The same is true of hypotheses.

A more honest representation of the structure is therefore

$$
V(H)\longrightarrow \text{partial order},
$$

followed, if one wishes to impose additional structure, by

$$
V(H)+w\longrightarrow S_M(H).
$$

Only after that does a further question arise: how, if at all, should the scalar score be related to probability? Each step adds assumptions that were not contained in the original virtue catalogue.

Even a complete ordinal ranking remains insufficient. Suppose the virtues somehow yield $$H_1\succ H_2\succ H_3$$. The distributions $$(0.6,0.3,0.1)$$, $$(0.4,0.35,0.25)$$, and $$(0.98,0.015,0.005)$$ all preserve the same ranking. The ordinal information tells us which hypothesis is ranked above another; it does not tell us how much prior mass each should receive. Probability requires cardinal structure that an ordinary preference relation does not supply.

This is why assigning a precise value such as $$P(H_1)=0.72$$ can create an appearance of measurement that the underlying methodological judgment does not warrant. If the underlying information says only that $$H_1$$ is somewhat simpler or more unified than $$H_2$$, the decimal precision may come entirely from the chosen transformation rather than from any equally precise epistemic fact.

### The Operationalization Problem

The difficulty deepens because the virtues themselves are often vague, heterogeneous, and context-dependent. Terms such as simplicity, elegance, coherence, explanatory scope, and unification are frequently invoked as though they referred to well-defined quantities, yet each admits several importantly different interpretations. Before a virtue can play a quantitative role in assigning prior probability, one must first explain what is being measured.

Simplicity is the clearest case. A theory may be called simple because it has few free parameters, posits few entities, relies on few auxiliary assumptions, has a short mathematical description, has low computational complexity, or integrates smoothly with an existing body of knowledge. These notions need not agree.

| Sense of simplicity | What it measures | Why it can conflict with other senses |
|---|---|---|
| Parameter simplicity | Number of free parameters | Few parameters can encode complicated structures. |
| Syntactic simplicity | Length or compactness of an expression | Depends on language, notation, and chosen primitives. |
| Ontological simplicity | Number or kinds of entities posited | A sparse ontology may require complicated laws or auxiliaries. |
| Computational simplicity | Resources needed to generate predictions | A short description may still be computationally intractable. |
| Background-relative simplicity | How much new structure is needed relative to $$K$$ | Explicitly depends on existing knowledge and commitments. |

A theory with a compact equation may be computationally intractable. Another may contain many parameters but derive them from a highly unified mechanism. A third may be ontologically sparse yet require numerous auxiliary assumptions before generating observable predictions. The statement that one theory is “intrinsically simpler” is therefore ambiguous unless a decision has already been made about which notion of simplicity is relevant.

The dependence becomes especially obvious when simplicity is understood in terms of how naturally a theory fits into existing knowledge. One theory may require only minor adjustments to the current framework while another requires extensive revision. This sort of simplicity is plainly relational: it is not merely $$S(H)$$ but $$S(H\mid K)$$. A hypothesis can fit naturally within one background theory and disrupt another, so that $$S(H\mid K_1)\neq S(H\mid K_2)$$. The hypothesis itself has not changed; the epistemic environment has.

There is a further methodological issue here. A preference for theories that require minimal revision of existing knowledge may express epistemic conservatism rather than a truth-directed probabilistic principle. Conservatism can be rational, but compatibility with what is currently believed does not by itself imply greater probability of truth. Existing knowledge can be incomplete or mistaken, and genuinely successful theories can demand substantial conceptual revision. To reward minimal revision is therefore to adopt a substantive methodological norm, not to uncover an intrinsic property of the hypothesis.

Elegance is even more difficult to operationalize. Scientists and philosophers often use the term meaningfully, but it may refer to mathematical symmetry, economy of expression, explanatory unification, conceptual economy, elimination of arbitrary constants, or some combination of these. A formal representation might therefore take the form $$E(H)=F(S(H),U(H),Y(H),N(H),\ldots)$$, where the components represent simplicity, unification, symmetry, non-arbitrariness, and other features. Yet this merely moves the problem down one level. One must still decide how those components are measured, whether they are commensurable, and how conflicts among them are resolved.

The same problem applies to explanatory scope, coherence, and unification. Broad scope can conflict with precision. Coherence can mean logical consistency, compatibility with established theories, inferential integration, or conceptual unity. Unification can mean deriving many phenomena from a common mechanism, reducing independent assumptions, or embedding several theories within a common formal structure. The alleged virtues are often not single variables at all, but families of related evaluative criteria.

If these virtues are to enter a quantitative model, one eventually needs functions such as $$v_i:H\rightarrow\mathbb{R}$$ or, where background information matters, $$v_i:(H,K)\rightarrow\mathbb{R}$$. Constructing those functions requires decisions about representation, scale, comparison class, and measurement procedure. Different operationalizations can rank the same hypotheses differently. A researcher using parameter count may obtain $$S_A(H_1)>S_A(H_2)$$ while a researcher using description length obtains $$S_B(H_1)<S_B(H_2)$$. Any subsequent disagreement in prior probability has therefore been inherited from the methodological choice of metric.

The important sequence is consequently not simply $$H\rightarrow P(H)$$. It is closer to

$$
H\longrightarrow \text{representation}\longrightarrow V_M(H)\longrightarrow \succeq_M\longrightarrow S_M(H)\longrightarrow P_M(H).
$$

Each arrow requires justification. One must decide what the virtues are, how they are operationalized, whether they are commensurable, how they are aggregated, and finally why the resulting evaluation should be interpreted probabilistically at all.

### From Ordinal Preference to Cardinal Probability

Even if all of the preceding problems were solved and a scalar methodological score $$S_M(H)$$ were produced, that score would still not yet be a probability. A further transformation is required. One might, for example, define

$$
P_M(H_i)=\frac{\exp(S_M(H_i))}{\sum_j\exp(S_M(H_j))}.
$$

The resulting numbers are non-negative and sum to one, so they have the formal structure of a probability distribution. But normalization does not, by itself, justify interpreting those numbers as probabilities that the hypotheses are true. A softmax can be applied to utilities to generate a stochastic-choice model; in that context, the resulting probabilities represent the probability of choosing an option under the behavioral model. They do not thereby become probabilities that the options are true. The semantics comes from the model, not from normalization.

This distinction can be stated succinctly:

$$
\boxed{\text{having the mathematical form of a probability distribution}\neq\text{being justified as a probability of truth}.}
$$

The defender of intrinsic probability therefore needs more than a method for producing normalized weights. The missing step is a bridge principle connecting theoretical virtue to truth probability. Until that principle is independently justified, theoretical preference and probability should remain conceptually distinct.

The underdetermination also suggests a more cautious probabilistic possibility. If methodological considerations constrain but do not determine credence, the mathematically honest result may be a *set* of admissible priors rather than a unique precise one. Instead of claiming a privileged $$P^*$$, one might have

$$
P\in\mathcal{P},
$$

where $$\mathcal{P}$$ is a family of priors compatible with the available methodological constraints. This possibility does not establish intrinsic probability; it strengthens the opposite point. Even if theoretical virtues legitimately constrain rational credence, they may still fail to determine a unique numerical probability. The leap from methodological guidance to a single intrinsic prior remains unjustified.

---
## 3. The Strongest Case: Formal Simplicity and Kolmogorov Complexity

A defender of intrinsic probability might object that the preceding discussion relies too heavily on vague notions such as elegance or explanatory simplicity. Perhaps some theoretical virtues are difficult to operationalize, but simplicity need not always remain informal. Algorithmic information theory provides a precise notion of complexity and therefore appears to offer a stronger foundation for assigning prior probabilities to hypotheses.

The most obvious candidate is Kolmogorov complexity. Relative to a universal Turing machine $$U$$, the Kolmogorov complexity of an object $$x$$ is the length of the shortest program that causes $$U$$ to output $$x$$:

$$
K_U(x)=\min_{p:U(p)=x}|p|.
$$

If a hypothesis $$H$$ can be represented as a finite object, hypotheses can in principle be compared according to the lengths of their shortest descriptions. A hypothesis requiring a shorter program is, in this technical sense, simpler than one requiring a longer program. Unlike ordinary appeals to elegance or conceptual economy, this notion of simplicity is formally defined.

It is then natural to construct a prior that penalizes complexity. A familiar form is

$$
P(H)\propto 2^{-K_U(H)}.
$$

Under such a rule, hypotheses with shorter minimal descriptions receive greater prior weight. If $$K_U(H_1)=K_U(H_2)+10$$, then the prior odds satisfy approximately

$$
\frac{P(H_1)}{P(H_2)}=2^{-10}.
$$

The hypothesis requiring ten additional bits of description receives roughly one-thousandth the prior weight of its shorter rival. Unlike vague talk of elegance, there is now an explicit mapping from a formal property to a numerical weight.

This is a much stronger case. It should be conceded that formal simplicity can be used to construct a genuine prior. Yet this still does not establish the existence of an intrinsic probability.

The first reason is that Kolmogorov complexity is relative to a reference machine. The correct notation is $$K_U(H)$$ rather than an unqualified $$K(H)$$. For universal machines $$U$$ and $$V$$, the invariance theorem guarantees that

$$
|K_U(H)-K_V(H)|\leq c_{UV},
$$

where $$c_{UV}$$ is a machine-dependent additive constant. This theorem is extremely important, but it does not give every finite hypothesis a unique, representation-independent complexity. For concrete hypotheses, the additive constant can matter, and when complexity is exponentiated into prior weight, even a fixed additive difference can correspond to a substantial multiplicative difference in prior odds.

If the prior is $$P_U(H)\propto 2^{-K_U(H)}$$, changing the reference machine can therefore alter the prior weight assigned to the same hypothesis. The proposition has not changed; the coding framework has. That fact already pushes us toward notation such as $$P(H\mid U,M)$$, where $$M$$ includes the rule connecting complexity to prior weight.

There is a second issue. Even if the reference machine is fixed and $$K_U(H)$$ is accepted as the relevant complexity measure, it does not follow from complexity alone that probability must be assigned according to $$2^{-K_U(H)}$$. One could define $$P(H)\propto e^{-\lambda K_U(H)}$$ for some $$\lambda>0$$, or use a weaker penalty such as $$P(H)\propto(1+K_U(H))^{-\alpha}$$. Each construction favors simpler hypotheses, but they induce different quantitative distributions. The existence of a complexity measure does not by itself select the mapping from complexity to probability.

The standard exponential form does have a deeper motivation than an arbitrary penalty. For prefix-free binary programs, a program of length $$n$$ naturally receives weight $$2^{-n}$$, and Kraft's inequality guarantees

$$
\sum_p2^{-|p|}\leq1.
$$

This supports an algorithmic probability construction in which one sums over all programs producing an output. Schematically,

$$
M(x)=\sum_{p:U(p)=x*}2^{-|p|},
$$

where the sum ranges over programs whose output begins with $$x$$. If programs are generated from random binary input, shorter descriptions receive more probability mass because fewer specific bits must be supplied.

This is a legitimate probabilistic construction, but notice what has happened. The direction of explanation is no longer

$$
\text{simplicity}\longrightarrow\text{probability}.
$$

It is instead

$$
\text{specified random program-generation process}\longrightarrow\text{probability measure}\longrightarrow\text{greater mass on short descriptions}.
$$

The probability comes from a generative process, not from simplicity alone. This raises the philosophical question that probability theory itself cannot answer: why should a process in which random bits are fed into a particular universal machine represent our uncertainty about which hypotheses are true of the world?

A generative process can define a measure without thereby justifying that measure as a probability of truth. Conditional on the generative setup, one may obtain something like $$P(H\mid U,G)$$, where $$G$$ is the chosen process. What has not been established is $$P_{\text{intrinsic}}(H)$$. The former is explicitly conditional on a model; the latter suggests that the probability belongs to the hypothesis independently of that model.

An analogy helps. A random procedure that generates English sentences will assign different probabilities to different sentences. Those probabilities are properties of the sentences *relative to the generator*. A different generative mechanism produces a different distribution over the same sentences. No one would conclude that the sentence itself possesses the probability independently of the mechanism that generated it. Algorithmic probability should be understood in the same way.

The role of background knowledge reinforces the point. A hypothesis can be complex in isolation but simple relative to a rich theoretical background. In algorithmic terms, one might therefore consider conditional complexity $$K_U(H\mid K)$$: the length of the shortest program needed to produce $$H$$ given background information $$K$$. This captures one formal sense in which a hypothesis may fit naturally with existing knowledge. But it also makes the dependence explicit. Any prior derived from this quantity is correspondingly conditional on the reference machine, background information, and prior-construction rule: $$P(H\mid U,K,M)$$.

Kolmogorov complexity is therefore a useful limiting case because it shows exactly where the issue lies. The objection is not that theoretical virtues can never be formalized or used in prior construction. They can. The objection is that successful formalization reveals the external structure on which the resulting prior depends. The correct schema is

$$
(U,K,M,H)\longrightarrow P_{U,K,M}(H),
$$

not

$$
H\longrightarrow P_{\text{intrinsic}}(H).
$$

Formal simplicity can generate a principled prior under a specified model. It does not show that a probability was already present inside the hypothesis waiting to be recovered.

---

## 4. Why the Resulting Prior Is Still Not Intrinsic

The preceding sections point toward a common conclusion. Whenever theoretical virtues are used to construct prior probabilities, the construction depends on a body of assumptions about how hypotheses are represented, evaluated, compared, and weighted. Once those assumptions are made explicit, the resulting probability no longer looks intrinsic to the hypothesis. It looks like the output of a methodological model.

### The Hidden Meta-Theory

Suppose a hypothesis is evaluated according to a methodological cost $$C_M(H)$$ and a prior is constructed as

$$
P(H\mid M)=\frac{\exp[-C_M(H)]}{\sum_{H'}\exp[-C_M(H')]}.
$$

The notation $$M$$ represents a collection of assumptions about theory choice: which virtues are relevant, what they mean, how they are operationalized, how conflicts are resolved, how weights are assigned, how the hypothesis space is partitioned, and how the resulting score is transformed into probability mass.

The resulting prior is therefore not simply a function of $$H$$. If one wished to expose every dependency, one might write something cumbersome such as

$$
P(H\mid M,K,L,V,w,f,\mathcal{H}),
$$

where $$K$$ denotes background knowledge, $$L$$ a representational language or coding scheme, $$V$$ the selected catalogue of virtues, $$w$$ a set of weights, $$f$$ an aggregation or transformation rule, and $$\mathcal{H}$$ the relevant hypothesis space. This notation is intentionally ugly. Its purpose is to show how much structure disappears when the same quantity is abbreviated as $$P(H)$$.

The central point is that the probability assignment is generated by a meta-theory. The object-level hypothesis $$H$$ makes a claim about the world; the methodological framework $$M$$ makes claims about how hypotheses like $$H$$ ought to be assessed. The framework decides whether simplicity should count in favor of a hypothesis, whether compatibility with existing knowledge should be rewarded, whether complexity should be penalized exponentially or linearly, and how explanatory scope should trade off against elegance or coherence.

The structure is therefore better represented as

$$
M\longrightarrow P_M\longrightarrow P_M(H)
$$

than as

$$
H\longrightarrow P_{\text{intrinsic}}(H).
$$

This distinction matters even if one believes that some methodological framework is objectively correct. Objectivity and intrinsicness are not the same. A quantity can be objectively determined by a relation without being intrinsic to either relatum. Distance, for example, may be objectively determined between two points while not being an intrinsic property of either point alone. Likewise, even if there were a uniquely rational methodology $$M^*$$, the resulting prior would still be $$P(H\mid M^*)$$: objective relative to a methodological structure, not intrinsic to $$H$$ in isolation.

This generates a hierarchy of justification. If $$P(H)$$ depends on $$M$$, one may ask why $$M$$ should be accepted. Perhaps $$M$$ is defended because it is simple, coherent, elegant, or successful. But if the same virtues are used to justify the framework that assigns virtue-based probabilities, the reasoning risks becoming circular. If simplicity is epistemically privileged because simpler methodological principles are themselves said to be more plausible, then simplicity has been presupposed in the justification of its own privilege.

This need not produce an infinite regress. A theorist may simply treat some methodological principles as primitive. But then the resulting probabilities should be described accordingly: they are priors generated under primitive methodological commitments. They are not probabilities intrinsic to the hypotheses themselves.

This also clarifies a recurrent confusion about priors. Ordinary updating is written as $$P(H\mid E,K)$$. The appeal to intrinsic probability attempts to identify a probability prior to $$E$$. Yet once methodological assumptions are made explicit, the prior is more accurately $$P(H\mid K,M)$$. It is prior to the specified evidence, but it is not prior to assumptions. The slide from “prior to $$E$$” to “intrinsic to $$H$$” is unwarranted.

### Representation and Background Dependence

The same conclusion follows from representation dependence. If a probability is genuinely intrinsic to a hypothesis, then it should not vary merely because the same substantive proposition is represented in a different language. Yet many of the virtues invoked to motivate intrinsic probability are sensitive to precisely such choices.

A theory may be concise in one formal language and cumbersome in another. Its apparent economy can depend on which concepts are treated as primitive, which operations are built into the language, and which background results are assumed rather than explicitly derived. What appears to be a property $$S(H)$$ may therefore be more accurately represented as $$S(H\mid L)$$, where $$L$$ is a language, coding system, or representational framework. If $$S(H\mid L_1)\neq S(H\mid L_2)$$, a simplicity-sensitive prior may inherit that dependence even though the truth conditions of $$H$$ have not changed.

Background knowledge creates a similar dependence. A hypothesis that initially looks complex may become simple once the relevant theoretical framework is assumed, while a hypothesis that looks compact in isolation may require substantial auxiliary machinery when embedded in a wider system. This is why conditional complexity $$K_U(H\mid K)$$ can be more informative than unconditioned complexity. But the same observation undermines the language of intrinsicness: the virtue is a property of the hypothesis relative to a background, not of the hypothesis alone.

Many alleged intrinsic virtues are therefore relational. Coherence is coherence *with something*. Conservatism is conservatism relative to an existing body of belief. Explanatory integration is integration with an already structured theoretical system. Simplicity itself may be simplicity relative to a language, coding scheme, or stock of accepted primitives.

Equivalent formulations of a theory make the problem vivid. Suppose $$H$$ and $$H'$$ express the same substantive theory but differ sharply in syntactic complexity. A prior that rewards description length may assign different weights to the two formulations. If they express the same proposition, however, it is difficult to interpret the difference as a difference in probability of truth. At most, it is a difference in probability assigned to two representations. A defender can respond that the relevant unit is the proposition rather than the sentence, but then a representation-independent measure of simplicity at the propositional level must be supplied. That is precisely the difficult part.

The point is not that representation-sensitive quantities are illegitimate. Many useful scientific quantities depend on conventions, coordinates, parameterizations, or modeling choices. The issue is conceptual: a convention-dependent or model-relative quantity should be described as such. If a prior is defined relative to $$L$$, $$K$$, and $$M$$, then notation such as $$P(H\mid L,K,M)$$ is more informative than $$P_{\text{intrinsic}}(H)$$.

### Dependence on the Hypothesis Space

A prior is also defined over a structured space of alternatives rather than attached to isolated propositions in a vacuum. This introduces another potential source of dependence: how hypotheses are individuated and partitioned.

Suppose one prior-construction rule is defined over $$\mathcal{H}_1=\{H_1,H_2\}$$, while another representation refines $$H_2$$ into subhypotheses, yielding $$\mathcal{H}_2=\{H_1,H_{2,1},\ldots,H_{2,n}\}$$. A coherent probability measure *can* preserve the marginal probability of $$H_1$$ under such a refinement; probability theory itself does not require that its mass change. The point is narrower. Many procedures for *generating* priors allocate mass according to the number, description, or structure of represented alternatives, and those procedures can be sensitive to how the hypothesis space is carved up.

That sensitivity matters for claims of intrinsic probability. If a proposed prior-generation rule changes the weight of unchanged $$H_1$$ merely because rival possibilities are redescribed, subdivided, or grouped differently, then the resulting number cannot plausibly be attributed to $$H_1$$ alone. It is a property of the whole modeled space and the allocation rule used on that space.

This is entirely familiar in probabilistic modeling. A probability measure is defined across a structured domain. The problem arises only when a model-relative assignment is rhetorically presented as if it were a unary property intrinsic to a proposition.

The hidden meta-theory, representation dependence, background dependence, and hypothesis-space dependence all point in the same direction. Theoretical virtues do not reveal a pre-existing probability contained in $$H$$. They contribute to an evaluative framework that may, after further assumptions, generate a prior. The resulting quantity is therefore

$$
P_M(H),
$$

not

$$
P_{\text{intrinsic}}(H).
$$

---
## 5. Objection: Bayesian Reasoning Requires Priors

A natural objection is that Bayesian reasoning cannot proceed without prior probabilities. If inference requires a prior over hypotheses, and if theoretical virtues are among the considerations used to construct that prior, then perhaps intrinsic probability is simply a name for a necessary feature of rational inference. On this view, the criticism developed so far may seem to demand an impossible neutrality: evidence alone cannot determine a posterior, so some pre-evidential structure must enter the analysis, and theoretical virtues may be what supply it.

There is an important truth in this objection, but it does not establish intrinsic probability. The need for priors does not imply that hypotheses possess probabilities independently of the models under which those priors are assigned. A Bayesian framework may require a prior distribution, but that is a claim about the structure of the inferential model, not about an intrinsic property of the hypotheses.

Three claims must therefore be kept separate:

$$
\text{Bayesian inference requires a prior}
$$

$$
\not\Rightarrow
$$

$$
\text{theoretical virtues uniquely determine that prior}
$$

$$
\not\Rightarrow
$$

$$
\text{the resulting prior is intrinsic to }H.
$$

Within a Bayesian framework, the posterior is determined by both likelihood and prior, $$P(H\mid E,K)\propto P(E\mid H,K)P(H\mid K)$$. But the fact that $$P(H\mid K)$$ must be specified does not tell us how it should be specified. Priors may be motivated by symmetry arguments, previous data, hierarchical models, domain knowledge, regularization, reference constructions, or other principles. Theoretical virtues may enter among these considerations, but when they do, they enter as part of the model-building procedure.

The most that follows is that some methodological framework $$M$$ helps determine a prior $$P_M(H)$$. That is entirely compatible with the criticism of intrinsic probability. Indeed, it reinforces it: the prior is now explicitly relative to a model of rational or methodological judgment.

A defender might insist that some priors are nevertheless more rational than others and that theoretical virtues supply objective constraints. Perhaps simpler hypotheses deserve greater initial probability because simplicity is truth-conducive; perhaps more unified theories deserve greater weight because unification has historically correlated with successful scientific theories. If these claims can be defended, then they may justify a structured prior. But the justification itself relies on further premises.

If simplicity is regarded as truth-conducive because simpler theories have historically generalized better, that historical pattern is evidence. It becomes part of the background information $$K$$. The prior is then informed by empirical facts about the performance of classes of hypotheses. What one has is $$P(H\mid K)$$, not an evidence-independent probability intrinsic to $$H$$. Likewise, if simplicity is justified by statistical learning theory, predictive performance, coding efficiency, or regularization, the justification depends on assumptions about the data-generating process, loss function, hypothesis class, or inferential goal. These may be excellent assumptions, but they remain assumptions in the surrounding model.

The distinction is therefore not between having a prior and having no prior. It is between recognizing a prior as an explicitly modeled component of inference and reifying that prior into a property of the hypothesis itself. Compare the following claims:

> Under methodological framework $$M$$, hypothesis $$H_1$$ receives greater prior weight than $$H_2$$ because $$M$$ penalizes complexity.

and

> Hypothesis $$H_1$$ is intrinsically more probable than $$H_2$$ because it is simpler.

The first is transparent about the rule generating the probability assignment. The second suppresses that rule and makes the conclusion appear to follow from the hypothesis itself.

This distinction also prevents a conflation between epistemic rationality and probabilistic representation. Even if one accepts the Bayesian position that rational degrees of belief should satisfy the probability axioms, it does not follow that every consideration relevant to theory choice must be encoded directly into a prior. Some considerations may guide the construction of the hypothesis space, determine which models are worth investigating, influence the loss function, or operate as external methodological norms.

Decision theory provides a useful comparison. Expected utility combines probability and utility without identifying them:

$$
EU(a)=\sum_sP(s\mid K)U(a,s).
$$

Probability represents uncertainty concerning possible states; utility represents value or preference. The usefulness of the framework depends on preserving those distinct roles. The same conceptual discipline should apply to theoretical virtues. Simplicity, elegance, or coherence may influence methodological preference without being absorbed into a probability measure merely because Bayesian inference contains a prior term.

The defender might reply that this leaves an incomplete epistemology: if theoretical virtues influence rational belief, they must somehow affect rational credence. Even if that is granted, the strongest conclusion available is still that theoretical virtues constrain or influence prior assignment *under some epistemic theory*. What follows is something like

$$
V(H),M,K\longrightarrow P(H\mid M,K),
$$

not an intrinsic probability belonging to $$H$$ independently of those assumptions.

The non-uniqueness of reasonable prior constructions makes the point especially clear. One framework might use a strong complexity penalty $$P_{M_1}(H)\propto e^{-\lambda_1C(H)}$$ while another uses a weaker one $$P_{M_2}(H)\propto e^{-\lambda_2C(H)}$$, with $$\lambda_1\neq\lambda_2$$. Both may be valid probability distributions and both may be defensible under different modeling commitments. The mere requirement for a prior therefore does not uniquely determine its form.

So-called objective priors do not alter the fundamental point. Methods based on invariance, maximum entropy, or reference behavior may be principled and useful, but they still rely on choices about parameterization, constraints, information structure, and inferential goals. Their objectivity, insofar as it is achieved, is methodological rather than intrinsic.

The relevant distinction can be summarized as

$$
\boxed{\text{necessity of a prior}\neq\text{uniqueness of a prior}\neq\text{intrinsicness of a prior}.}
$$

Bayesian reasoning therefore does not rescue intrinsic probability. It provides a formal location in which prior assumptions must be represented. The burden remains to justify those assumptions and to avoid mistaking their output for a property belonging to the hypothesis independently of them.

---

## 6. A Better Alternative

Rejecting intrinsic probability does not make theoretical virtues irrelevant. A more coherent framework is to preserve a distinction between different kinds of epistemic structure. Probability can represent uncertainty, theoretical virtues can guide methodological preference, and decision-theoretic quantities can represent the value of actions or outcomes. These structures may interact without being collapsed into one another.

For probabilistic uncertainty, the relevant object is something like $$P(H\mid E,K)$$. For methodological comparison, one may instead use a relation $$H_1\succeq_V H_2$$, meaning that $$H_1$$ is at least as attractive as $$H_2$$ according to a chosen catalogue of theoretical virtues. The second relation need not imply any unique probabilistic relation between the hypotheses.

A researcher may therefore judge that two hypotheses fit the available evidence similarly while one is methodologically preferable because it is simpler or more unified. This can be represented as

$$
P(E\mid H_1,K)\approx P(E\mid H_2,K)
$$

while

$$
H_1\succ_V H_2.
$$

There is no inconsistency here. The first statement concerns empirical fit under a probabilistic model; the second concerns methodological evaluation. A theory can be preferable for purposes of explanation, tractability, robustness, or research strategy without a determinate numerical claim that it is more likely to be true.

This framework also allows the multidimensional structure of theory evaluation to remain visible. Instead of forcing all virtues into a scalar, one may retain a vector such as $$V(H)=(S(H),U(H),C(H),E(H))$$ and accept that the resulting comparison is sometimes partial. Some hypotheses may dominate others; in other cases the virtues may conflict and no unique overall ranking may be justified. That incompleteness may accurately represent the epistemic situation rather than a defect requiring immediate numerical repair.

None of this prevents theoretical virtues from entering probabilistic modeling when there is a reason to make them do so. A researcher may construct a prior such as

$$
P_M(H)\propto e^{-\lambda C(H)},
$$

where $$C(H)$$ is a specified complexity measure and $$\lambda$$ controls the strength of the penalty. Such a prior may be useful for regularization, model selection, prediction, or compression. The important point is that it should be described transparently as a prior under a methodological model $$M$$.

The same applies to minimum-description-length methods, information criteria, and algorithmic priors. These approaches may encode principled preferences for simpler models, and their procedures may have desirable predictive, asymptotic, or compression properties. Those properties can provide strong reasons to use the methods. They do not imply that the favored hypotheses possess greater probabilities independently of the procedures that favor them.

The positive alternative is therefore not hostile to formalization. It asks for more transparency about what is being formalized. If a complexity penalty is used, its form should be stated. If multiple virtues are aggregated, the weighting scheme should be explicit. If a prior depends on a representational language, background theory, or hypothesis class, those dependencies should be acknowledged rather than hidden behind the label “intrinsic.”

A clean inferential architecture would distinguish at least four roles:

$$
\text{evidence}\longrightarrow\text{likelihood structure},
$$

$$
\text{background assumptions}\longrightarrow\text{prior model},
$$

$$
\text{theoretical virtues}\longrightarrow\text{methodological preference},
$$

$$
\text{preferences and consequences}\longrightarrow\text{decision criteria}.
$$

These components can interact without being identified. Theoretical virtues may influence which hypotheses are formulated, which are tested first, which explanations are considered satisfactory, and which prior models are worth adopting. What they do not automatically provide is a probability of truth.

This also leaves room for imprecise or set-valued probabilistic representations. If methodological considerations genuinely constrain credence but do not uniquely determine it, one can represent the admissible possibilities as a family $$\mathcal{P}$$ of priors rather than manufacturing a precise scalar. This is conceptually preferable to treating underdetermined methodological judgments as if they already contained exact probabilities.

The conceptual picture is therefore better represented by keeping

$$
P(H\mid E,K)
$$

and

$$
H_1\succeq_V H_2
$$

as distinct structures. Where a probability is required, it should be supplied by an explicit probabilistic model. Where a methodological preference is being expressed, it should be represented as such. This preserves what is valuable in appeals to theoretical virtue while avoiding the stronger and more problematic claim that those virtues reveal a probability intrinsic to the hypothesis.

---

## 7. Conclusion: There Is No Probability Inside the Hypothesis

The case against intrinsic probability does not depend on denying Bayesian inference, rejecting priors, or dismissing theoretical virtues. It depends on keeping distinct several kinds of structure that are too easily conflated. A hypothesis may be simpler, more elegant, more coherent, or more unified than a rival. Those features may rationally influence how the theory is evaluated, which hypotheses are investigated, or even how a prior model is constructed. But none of those facts, taken by itself, supplies a probability measure.

The argument can be summarized in one sequence. Theoretical virtues first require definition and operationalization. When several virtues are present, they may produce only a partial preference relation. Turning that relation into a scalar requires additional assumptions about weighting and tradeoffs. Turning the scalar into a probability distribution requires still another mapping and an account of why the resulting numbers should represent probability of truth. Formal approaches such as Kolmogorov complexity improve the precision of these steps, but they do not eliminate their dependence on reference machines, representations, background knowledge, generative assumptions, or methodological rules.

The relevant structure is therefore

$$
H\longrightarrow V_M(H)\longrightarrow\succeq_M\longrightarrow S_M(H)\longrightarrow P_M(H),
$$

not

$$
H\longrightarrow P_{\text{intrinsic}}(H).
$$

The first chain is intelligible because every transition makes explicit the methodological machinery responsible for the result. The second suppresses that machinery and makes a model-relative assignment appear to be a property of the proposition itself.

A prior may be prior to some evidence without being prior to all assumptions. It may be objective under a specified methodology without being intrinsic to the hypothesis. It may be highly useful without being uniquely determined. And theoretical virtues may constrain rational inquiry without themselves becoming probabilities.

The central conclusion is therefore straightforward:

$$
\boxed{P_M(H)\neq P_{\text{intrinsic}}(H).}
$$

The former is intelligible: it is the probability assigned to a hypothesis under a specified model. The latter suggests a probability residing within the hypothesis itself, independently of the methodological, representational, and probabilistic assumptions required to generate it. Once those assumptions are made explicit, there is no reason to think such a quantity exists.
