In the first two posts, we discussed criteria for "good explanations" in general; with particular emphasis on mechanism and causal structures. In this post, I want to turn to a specific type of explanation. 

It’s often correctly asserted that microeconomic theory often fails to explain economic behavior, for a variety of reasons: incorrect unit of analysis, incorrect assumptions about structure, unrealistic assumptions about human rationality etc. But from an economists perspective, this is not necessarily a failure. The standard microeconomic model serves as a benchmark for comparison, we understand that it doesn’t capture important aspects of reality and adjust the model accordingly. But this has got me thinking about explanation and the relationship between explanation and modeling more generally. In economics, we often relax assumptions of the standard model, then take a game theoretic approach when considering strategic interaction (something the benchmark doesnt account for). This is seen as a step in the right direction, an improvement on the base model, but it’s still a model with limitations. Model simplicity is traded off for model complexity and tractability in situations where the standard model fails to explain the phenomena. 

On the empirical side of the discipline, econometricians are primarily concerned with causal identification strategies (especially after the credibility revolution). They are often meticulous when qualifying their causal claims and vigorously vet eachothers identification strategy. But it seems like questions about "the effect of policy X on Y" are vetted more carefully than some of the theoretical models. It seems as if empirical methods closer to the consequences of being mistaken are more closely scrutinized then theoretical models. This is a bit of a simplification; after all, the empirical methods are often determined by the theory. But it could be just a general fact about expanation importance relative to a question. I guess what I am circling in onare a few questions:

- What kind of thing is an economic model, epistemically?
- When does a model count as an explanation, versus a benchmark, a heuristic, a discipline of thought, or a device for counterfactual reasoning?
- Why do theory and econometrics feel like they have different kinds of explanatory authority, and how should we evaluate them?

## Explanation vs model

A **model** is a representational artifact. It can serve multiple scientific aims:

* *explanation* (why/how),
* *prediction*,
* *counterfactual policy analysis*,
* *conceptual clarification*,
* *benchmarking*,
* *measurement/identification assistance*,
* *mechanism articulation*.

An **explanation** is a success term: it’s what you have **when** a representation successfully answers the relevant why/how question under appropriate standards. So it’s totally coherent that a model can be **useful** without being literally true, and a model can be **explanatory** even when false in many details, but also some models are primarily *disciplinary benchmarks* rather than direct explanations.

This is extremely close to Angela Potochnik’s line: explanations often work by capturing **causal patterns** with the right scope, and idealization can be legitimate if it helps depict that pattern—*but* you still need adequacy constraints so you’re not ignoring major causal influences that dominate the phenomenon. (That’s exactly why economists can accept “false but useful.”)

Economists slide between at least **four** senses of “explain,” and critiques often conflate them.

1. Benchmark explanation (disciplining comparison) - **Perfect competition / full rationality** models explain by giving a **baseline** and locating deviations as effects of particular frictions. This is explanation in a *contrastive* sense. Why is the world not like the competitive benchmark? Because of frictions A, B, C. It’s not a claim that the benchmark is descriptively true. It’s a **reference class** that makes deviation intelligible.

2. Mechanism/possibility explanation (“how this could happen”) - Many theory models are **how-possibly** explanations: they show an internally coherent causal/strategic pathway by which an outcome can arise. Game theory here is a prime example: you “relax assumptions” to add strategic interaction; the model shows a *possible* mechanism (incentives, information, equilibrium selection) that could generate observed regularities. This is scientifically valuable even before it’s pinned to the world.

3. Pattern explanation (capturing robust qualitative dependence) - Some theory is explanatory because it captures a **robust comparative statics pattern** such as direction of change, existence of multiple equilibria, threshold effects, strategic complementarity, or selection effects.

4. World-anchored causal explanation (identification-backed) - This is the econometric “credibility revolution” explanatory style: Under assumptions X (and design Y), policy A causes outcome B by Δ. It’s explanatory in a **difference-making** sense: it supports counterfactual intervention reasoning. But it often tells you less about the *how* (mediators, transmission) unless you deliberately pursue mechanisms. So when you say you trust econometric claims more as “explanations” than a general economic theory, you’re implicitly prioritizing **difference-making causal explanation** over “how-possibly” or “pattern” explanation.

Many critiques treat a benchmark model as if it were a literal hypothesis about the world. Economists treat it as a **controlled counterfactual world** used to isolate the role of frictions. So “unrealistic assumptions” are not automatically a failure; they can be a representational strategy. But there *is* a real philosophical risk here, and it maps to themes discussed earlier. A model becomes pseudo-explanatory when it provides the *feeling* of understanding without having the right dependence relation to the target phenomenon. Concretely, micro theory fails explanatorily when it omits causal factors that dominate the phenomenon, or it gets the **unit of analysis** wrong (e.g., household vs network vs institution), or it imposes structural assumptions that eliminate the very dynamics you need (e.g., strategic manipulation, institutional constraints, non-stationarity). This is basically Potochnik’s adequacy worry applied to economics. Idealize, yes, but don’t idealize away what the phenomenon is *most sensitive to*. And it also echoes Ross. Sometimes the right causal structure isn’t “mechanism within a bounded system,” but **cascade dynamics** (contagion, bank runs, diffusion) or **structural constraints** (institutions, market design, regulation, power structures).

Theory is often strong on *structure* and weak on *world anchoring*. It tells you what could generate the pattern, what the transmission could be, where incentives bite—but may not tell you whether this is *the* operative structure in the data.

The best explanatory practice in economics is the combination of theory and empirics. The identification establishes **that** a causal effect exists (difference-making), theory maps the space of possible structures and generates **discriminating predictions**, and additional empirical tests (heterogeneity, mediation, equilibrium comparative statics, natural experiments affecting specific channels) help you decide which structure is actually operative. Explanation is a package, not a single technique.

Still, fundamental questions remain:

- When does an idealized model count as an explanation of real economic phenomena, as opposed to a benchmark or heuristic?
- What standards justify treating a theoretical model as explaining, if it lacks direct empirical anchoring?
- What should we expect from econometric identification vs micro theory vs structural modeling in a mature explanation of an economic phenomenon?

When you ask “does this model explain?”, score it on three axes:

1. Pattern capture

    * Does it reveal a stable qualitative dependence (comparative statics, thresholds, strategic complements)?
    * Does it specify scope/boundary conditions?

2. World anchoring

    * Are key dependencies supported by credible identification or robust observational constraints?
    * Does it survive alternative explanations / sensitivity?

3. Structure adequacy

    * Is the causal structure it assumes plausibly the right kind for this phenomenon? Equilibrium mechanism vs cascade contagion vs structural constraints vs network diffusion.
    * Does it give intervention handles at the right level?

A model can “pass” as explanatory in different ways depending on the question. For **policy counterfactuals**, B is crucial. For **why recurring patterns happen**, A and C may matter more. For **mechanism/transmission**, C plus targeted evidence matters. This explains why economists aren’t bothered by unrealistic assumptions *if* the model is serving A or C and is explicitly a benchmark.

## Economists vs The Public

There is often a wide chasm between what the general public takes to be a sufficient explanation about economic phenomena versus how economists think about good explanations. I am honestly quite baffled at times when people think certain explanations are satisfactory. There is acadenmic research on this. It ties back into the psychology of explanation and social epistemology we identified earlier. 

There is work on folk economic beliefs that seeks to explain this systematic disconnect between how economists view economic phenomena versus how economic beliefs formed and held by the public. There is actually research into modeling economics as a system of actors with these folk beliefs. The idea is to computationally represent these primitive intuitions, determine decision rules based on these, then simulate market outcomes and properties of those outcomes. 

But this idea of a “good explanation” for an economist (in terms of a well defined theory, model, and identification strategy) vs “good explanation” for a non economist is interesting to me because “good” for the non economist often means identity preservation; it's connected to social epistemology and group think in interesting ways.

**Laypeople’s “explanations” of the economy often function more like intuitive social stories and identity signals**, while economists (especially empiricists post–credibility revolution) treat “good explanation” as something like **a well-specified causal claim with clear counterfactual content and vetted identification**. The interesting part is that *both* are doing work—but often **different kinds of work**, under different standards.

The problem is that two different explanatory jobs get collapsed into one word: “explain”. A lot of professional explanation is constrained by norms like having a **clear estimand** (“effect of X on Y for whom/when”), **identification credibility** (design-based causal inference), **scope conditions** (external validity and boundary conditions), and a **mechanism/transmission (optional but valued)** when the goal is theory-building or policy design. This is the world where “theory” can be a disciplined benchmark, but the *explanatory authority* often lives with causal designs and transparent assumptions.

For non-specialists, an explanation frequently functions as **uncertainty reduction** (“now it makes sense”), **normative positioning** (“who’s to blame / what should be done”), **identity signaling** (“my group sees it this way”), and **agency-centered storytelling** (clear actors, motives, villains, victims). That isn’t “irrational”; it’s often **adaptive** for social life. But it can diverge dramatically from economists’ standards because it optimizes different objectives. This is exactly the kind of distinction Angela Potochnik is trying to foreground: explanation isn’t only about the dependence relation in the world; it also has communicative, representational, psychological, and social dimensions (and those can dominate in public discourse).

There’s a substantial literature on “folk-economic beliefs”: stable, widespread intuitions about markets, trade, prices, wages, immigration, inequality, and so on. Pascal Boyer explicitly frames this as a domain like folk physics/folk biology: ordinary cognition produces *default* economic beliefs that are not best seen merely as “errors” relative to Econ 101. A parallel economics-side tradition documents systematic gaps between economists and the public using survey evidence. Bryan Caplan’s analysis of the “Survey of Americans and Economists on the Economy” argues the public’s positive economic beliefs differ systematically from economists’ in patterned ways, and that these differences aren’t well explained simply by self-serving bias. The public’s “bad explanations” aren’t just ad hoc stories; they are often **products of stable inference heuristics** applied to complex, opaque systems.

Why do these folk beliefs arise? Boyer (with colleagues like Petersen) argues folk-economic beliefs are shaped by cognitive defaults that worked well in small-scale social environments—e.g., intuitions about fairness, cheating, reciprocity, and zero-sum competition—then get overgeneralized to impersonal market systems. So the gap isn’t simply “ignorant public vs informed economist.” It’s **different cognitive toolkits** optimized for different environments.

Many public “explanations” are **identity-laden**, not truth tracking. There’s strong evidence that people’s evaluations of evidence on contested policy topics are influenced by **identity-protective cognition** and motivated reasoning—i.e., people process information in ways that protect their standing in valued groups. Dan M. Kahan has influential work describing this dynamic in policy-relevant risk and science controversies. If you combine this with the psychology of explanation: Explanations are attractive when they produce **clarity** and **closure**. Closure is not just epistemic; it can be social: it ends the discomfort of ambiguity and aligns you with your group. "Good” for the non-economist can mean self-preserving and group-stabilizing. And it also connects to the *“seductions of clarity”* theme: explanations can **feel** clarifying while being epistemically shallow, especially in hostile or polarized environments.

Economics has features that systematically invite narrative-style, identity-friendly explanations:

1. **High causal opacity:** Many mechanisms are indirect, delayed, and multi-step.
2. **Confounded everyday observation:** People “see” prices rising and infer causes using everyday moral psychology (“greed,” “bad people”), because structural inference is hard.
3. **Moral entanglement:** Claims about inflation, redistribution, and trade are never just descriptive; they’re tied to fairness and deservingness.
4. **Scale mismatch:** Folk cognition handles small-group exchange well; economies are networked, institutionally mediated, and emergent.

So the public’s favored explanations often optimize for agentic blame, moral legibility, and quick closure, instead of causal structure, scope conditions, and counterfactual support.

Modeling economies *with* folk beliefs is pretty much intersection of folk economics (as cognitive content), behavioral rules (decision heuristics), and agent-based modeling (ABM) to see emergent macro outcomes. ABM is explicitly used to relax standard assumptions (represent heterogeneous agents with bounded rationality, local interaction, networks, institutions) and study emergent macro patterns. Robert L. Axtell’s overview emphasizes precisely this motivation: ABM as a way to relax conventional assumptions in economics/finance and explore macro patterns from micro rules. And there are broad reviews describing how modern ABM increasingly incorporates heuristics and empirically informed behavioral rules.

I've actually constructed a model like this. A typical pipeline looks like:

1. **Elicit folk beliefs** (survey/experiment): e.g., zero-sum intuitions about trade, price controls, immigration, “profits cause inflation,” etc. (Boyer/Caplan/Rubin-style topics).
2. **Encode belief-based decision rules**: voting/policy preferences, wage demands, consumption/saving responses to inflation narratives, expectations formation (adaptive, narrative-driven, identity-aligned)
3. **Simulate interaction + institutions**: markets, firms, central bank rules, information networks, media
4. **Observe emergent properties**: persistence of inflation expectations, policy volatility, boom-bust dynamics, polarization, regulatory cycles, etc.

**Folk explanations become state variables** in the model. This is definitely a heterodox approach to economic modeling. Model explainability clearly takes a hit, but realism can improve predictions. 

Economists’ best explanations often aim at **causal patterns**. They are selective, abstract, and idealized—*but disciplined*—because they aim to depict a stable dependence relation with defined scope. Public explanations often aim at **psychological and social functions**. They reduce uncertainty, allocate blame, defend identity, and coordinate group action. I find that computationally modeling economic behavior with folk beliefs rather than rational actors leads to quite surprising insights. Public discourse rewards explanations that are simple, agentic, moralized, and group-confirming.

If you’re trying to communicate economics without triggering identity defenses, one thing that often helps is to present explanations in **layers** that respect both functions:

1. **Narrative hook** (meets the audience’s need for coherence)
2. **Structure/cascade layer** (how incentives + institutions + feedback loops constrain outcomes)
3. **Counterfactual layer** (what would happen if we changed X; what evidence supports it)
4. **Scope and humility** (where it applies, where it doesn’t; what is uncertain)

This is basically taking seriously Potochnik’s “other questions” (psychology, communication, representation) while retaining the economist’s demand for causal discipline.

- ["Folk-economic beliefs: An evolutionary cognitive model"](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/folkeconomic-beliefs-an-evolutionary-cognitive-model/7D84E452710ACCC6A35D49B8590B614F?) 
- ["Systematically Biased Beliefs about Economics"](https://econfaculty.gmu.edu/bcaplan/pdfs/systematicallybiased.pdf?)
- ["Ideology, motivated reasoning, and cognitive reflection"](https://ndg.asc.upenn.edu/wp-content/uploads/2017/08/Ideology-motivated-reasoning.pdf?)
- ["Agent-Based Modeling in Economics and Finance"](https://oms-inet.files.svdcdn.com/staging/files/JEL-v2.0.pdf?)
- ["Advances in the agent-based modeling of economic and ..."](https://pmc.ncbi.nlm.nih.gov/articles/PMC8262124/?)

## Systems and Complexity Explanations

Certainly. Here is the passage rewritten in essay style, with the conceptual and informational content preserved. 

Complexity economics should not be understood as hostile to abstraction. Much of scientific explanation works by reducing complexity through abstraction, modeling, simplifying assumptions, and simplified representations of target systems. In that sense, complexity economics is not anti-abstraction so much as committed to a different style of abstraction. Rather than idealizing away heterogeneity, interaction structure, and out-of-equilibrium dynamics in order to achieve analytic tractability, it is more willing to represent those features explicitly, even when doing so makes closed-form solutions difficult or impossible. At its core, complexity economics poses a challenge to standard economics by insisting that many economic phenomena cannot be adequately explained within the traditional framework and that standard models often fail to answer the questions most relevant to economic life.

A useful way to frame the contrast is this: standard microeconomics often abstracts by stripping away interaction structure through devices such as the representative agent, equilibrium assumptions, complete markets, and rational expectations, thereby producing tractable and general theoretical results. Complexity approaches, by contrast, typically abstract by explicitly representing interaction structure, including networks, adaptive learning, agent heterogeneity, and institutions, and then using simulation or computation to study the macro-patterns that emerge from these interactions. The disagreement, then, is not over whether abstraction is legitimate, but over which features of the economic world should be simplified and which should be preserved.

In this sense, complexity approaches depart from more traditional forms of explanation primarily in what they take to be explanatorily fundamental. Standard theoretical explanation often treats explanation as a matter of showing that an observed pattern is an equilibrium of some game or economy. Complexity and generative approaches argue that this is frequently insufficient. To explain a pattern well, one must also show how it could arise through decentralized interaction over relevant time scales. This is why Joshua M. Epstein’s generative maxim, “If you didn’t grow it, you didn’t explain it,” has become so influential: it captures a major shift from static characterization to dynamic formation.

Relatedly, complexity economics moves from an emphasis on closed-form dependence to an emphasis on emergent pattern dependence. Macro regularities are treated as emerging from network topology, feedback loops, adaptation, nonlinearity, threshold effects, and path dependence. Such explanations can appear non-traditional only if one identifies explanation exclusively with formal derivation in closed form. On a broader view, such as Potochnik’s understanding of explanation as depicting causal patterns, complexity explanation is continuous with more familiar scientific practices. It still aims to represent a dependence pattern and its scope, but it does so through simulation and structural modeling rather than analytic derivation alone.

At the same time, complexity economics should not be mistaken for an attempt to embrace complexity without simplification. Complexity models simplify extensively. The difference is that they simplify other things. They may use stylized institutions, bounded rationality heuristics, simplified environments, or reduced decision rules in order to retain interaction structure and system dynamics. Complexity is therefore not anti-simplification; it is selective simplification organized around different explanatory priorities.

What, then, makes a good complexity explanation? First, it must exhibit generative adequacy. A strong complexity explanation can generate the phenomenon to be explained—whether bubbles and crashes, heavy-tailed returns, volatility clustering, diffusion cascades, segregation, or bank runs—from plausible micro-level rules and interaction structures. Yet, as Epstein himself emphasizes, generation is necessary but not sufficient. A model can reproduce a phenomenon in a patently absurd way. Reproducing stylized facts is therefore only the first step.

Second, a good complexity explanation requires non-absurd microfoundations and interpretability. The rules governing agents should be behaviorally or empirically defensible, whether in the form of bounded rationality, learning, or heuristics, and the model should be transparent enough to show what mechanisms are actually doing the explanatory work. This is one area in which agent-based models often fail in practice, even if not in principle: they may contain too many adjustable elements, making causal responsibility difficult to identify.

Third, a good complexity explanation must identify causal structure within the model itself. This involves what might be called internal identification: ablation tests that remove a mechanism to see what changes, sensitivity analyses, robustness checks, and parameter sweeps that reveal thresholds or phase transitions. These procedures function as the complexity analogue of mechanistic intervention, helping determine which parts of the model are essential to the result.

Fourth, good explanation requires attention to scope and invariance. A strong complexity account should specify the conditions under which it applies, distinguish essential from incidental features, and clarify its boundary conditions. Fifth, it should be empirically anchored through calibration and validation. Complexity explanations become genuinely competitive when they are tied to data: calibrated to micro-level distributions, validated against multiple macro-level stylized facts, and capable of predicting new qualitative patterns or comparative statics. One of the central methodological challenges in complexity economics has long been the empirical validation of agent-based models, but recent work has become increasingly explicit about calibration and validation rather than treating simulation as unconstrained exploratory play.

Sixth, complexity explanations are often especially valuable when they reveal policy-relevant leverage points. Systems thinking emphasizes interventions that can dramatically alter system behavior by changing network structures, increasing friction, modifying feedback loops, adjusting adaptation rules, or altering institutional constraints. In this respect, complexity explanation aligns closely with ideas about causal constraints and cascades, but applies them specifically to economic systems. A good explanation does not merely reproduce a phenomenon; it identifies the structural levers through which that phenomenon might be altered.

Complexity explanations tend to outperform standard microeconomic models when the phenomenon to be explained depends crucially on features that standard micro tends to idealize away. One such case is out-of-equilibrium dynamics and continual adaptation. W. Brian Arthur explicitly contrasts the standard equilibrium or steady-state picture with a view of the economy as perpetually in process, with agents continuously adapting. For inherently transitional phenomena such as crises, waves of technological adoption, or shifts in expectations, complexity models may therefore be better aligned with the causal structure of the explanandum.

A second case involves network effects and topology. When outcomes depend on who interacts with whom—as in financial contagion, supply chains, trade networks, or information diffusion—representing network structure is not a form of vague holism, but an appropriate unit of causal analysis. Standard models can incorporate networks, but complexity approaches usually make them central and dynamic rather than peripheral constraints.

A third case concerns heterogeneity and distributional dynamics. Representative-agent models often miss feedback effects generated by differences among agents, such as wealth concentration affecting demand, heterogeneous leverage producing systemic fragility, or firm size distributions shaping aggregate volatility. Complexity models can treat such heterogeneity as explanatorily central rather than as a nuisance to be averaged away.

A fourth case arises when there are multiple equilibria, path dependence, and strong historical effects. In such settings, the mere fact that an equilibrium exists does not explain why this equilibrium rather than another was realized. Complexity approaches address precisely this gap by emphasizing formation dynamics and historical trajectories. A fifth case concerns macro-behavior without stable micro-level rationality. If agents rely on rules of thumb, imitation, learning, or evolutionary adaptation rather than full optimization, complexity models can still generate macro-regularities. In such circumstances, they may offer a better explanation if the goal is to explain observed patterns under plausible cognitive conditions rather than under idealized rationality.

In one broad sense, then, complexity economics and standard microeconomics are engaged in the same general explanatory project. Both use abstract representations to answer why and how questions. Yet to say they are the same kind of explanation can conceal an important difference in explanatory form. Standard micro often explains by characterizing equilibria and tracing comparative statics under strong optimizing assumptions. Complexity economics, by contrast, often explains through generative sufficiency and structural dynamics, showing how decentralized, adaptive interaction can produce emergent macro-patterns. This is not best described as holism. Rather, it reflects the idea that different sciences may legitimately rely on different causal structures, including mechanisms, cascades, and constraints. Complexity economics is especially concerned with cascade-like amplification, constraint regimes, and network-mediated propagation, all of which are difficult to capture in highly stripped-down benchmark models.

Still, complexity models are not automatically superior. They have characteristic weaknesses. They may overfit by using too many degrees of freedom, becoming capable of generating almost any outcome. They may be opaque, making it difficult to identify causal responsibility within a simulation. They may suffer from weak empirical discipline if calibration and validation are insufficient. And they may have limited portability, since a model tailored to one market or historical period may not generalize elsewhere. For these reasons, a good complexity explanation must earn trust through robustness, interpretability, and empirical anchoring. Without these, it risks becoming little more than a sophisticated story-generating device. Epstein’s caution is instructive here: merely generating a phenomenon does not by itself amount to explaining it well.

Viewed in this light, the question of whether economics is simply examining aspects of systems that were traditionally difficult to analyze can often be answered in the affirmative. But that is precisely why complexity can yield better explanations for certain kinds of explananda. It treats as central what standard microeconomics often relegates to the residual category: interaction structure, adaptation, dynamics far from equilibrium, and macro-regularities emerging from heterogeneous agents. A complexity explanation is better than a standard microeconomic one when it captures the relevant causal structure—networks, cascades, feedback, and constraints—when it generates the phenomenon rather than merely showing its equilibrium possibility, when it reveals leverage points for intervention and offers robustness insights, and when it is sufficiently empirically anchored to count as more than a plausible narrative.

Ultimately, the criterion for a good explanation here is the same broader one that applies across scientific inquiry: an explanation is strong when it fits the relevant causal structure, has an appropriate scope, is adequate to the phenomenon, and presents its claims with enough clarity and discipline to avoid becoming exploitative or merely impressionistic. Complexity economics is most compelling not because it rejects simplification, but because it rearranges explanatory priorities in ways that can make certain economic phenomena more intelligible than standard microeconomic models allow.

- ["Foundations of complexity economics"](https://sites.santafe.edu/~wbarthur/Papers/Nature_Phys_Revs.pdf?)
- ["remarks on the foundations of agent-based generative ..."](https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/RemarksFoundationsABM.JEpstein2006.pdf?)
- ["Agent-based computational models and generative social ..."](https://cdanfort.w3.uvm.edu/csc-reading-group/epstein-complexity-1999.pdf? )
- ["Reconstructing Economics: Agent Based Models and ..."](https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/RethinkingEconomicsABM.Gallegati2012.pdf?)
- ["Epstein - Agent-based Generative Social Science"](https://wiki.santafe.edu/images/3/3b/Epstein_-_Agent-based_Generative_Social_Science.pdf?)
- ["Inverse Generative Social Science: Backward to the Future"](https://www.jasss.org/26/2/9.html?)
- ["Empirical Validation and Verification of Agent-Based Models"](https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/EmpValid.htm?)
- ["Leverage Points: Places to Intervene in a System"](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/?)
- ["Complexity Economics"](https://sites.santafe.edu/~wbarthur/complexityeconomics.htm?)


## Summarizing the Explanation Series

### What philosophers mean by “explanation” and how it relates to what is explained

In our discussion, explanation was treated not as a mere statement of fact, but as a relation between two elements: the **explanans**, or the body of information doing the explaining, and the **explanandum**, or the phenomenon to be explained. The explanans may consist of causes, mechanisms, constraints, patterns, or models, and its task is to render the explanandum intelligible in a way that supports inference. This means that explanation is valuable not simply because it states something true, but because it enables counterfactual reasoning, prediction, intervention, unification, or understanding.

A recurring theme was that explanations are best understood as structured answers to questions. Often those questions are implicitly contrastive, taking the form “Why P rather than Q?” In that sense, explanation is not just about attaching one proposition to another, but about identifying the dependence relations that matter for the question being asked.

### Explanation is distinct from description, labeling, and pseudo-explanation

We repeatedly emphasized that explanation must actually do explanatory work. It is not enough to rename a phenomenon by invoking broad or prestigious terms such as neoliberalism, entropy, genes, or vibes. Nor is it enough to restate the phenomenon in different words, as when one says that inflation is high because prices are rising. Similarly, merely gesturing toward an explanatory category, such as calling something a mechanism, does not yet amount to a genuine explanation.

What distinguishes pseudo-explanation is that it produces the feeling of understanding without supporting the right inferences. It may be too elastic, able to fit almost any case, or it may conceal the absence of serious alternatives. It can also borrow the authority of causal language without accepting the accountability that genuine causal claims require. In that way, pseudo-explanation simulates explanatory success while failing to provide it.

### Evaluation: what makes a “good” explanation?

Rather than adopting one universal checklist, we developed a multi-dimensional account of explanatory quality. Some criteria were epistemic or ontic, having to do with whether the explanation tracks reality. A good explanation captures a genuine dependence relation, often causal. It cites factors that are relevant to the specific question or contrast at issue. It makes clear its scope and boundary conditions, showing where it applies and where it fails. It must also be robust or adequate, meaning that it cannot leave out major factors that would alter the explanatory story. Finally, it should discriminate among plausible alternatives, not merely coexist with them untested.

Other criteria were representational. A good explanation involves the right abstraction or idealization for the task at hand. Simplification is often necessary, but it must be legitimate relative to the explanatory aim. Likewise, level matters: sometimes the right explanation is micro-level, sometimes macro-level, sometimes structural. There is no universally privileged level apart from the question being asked.

We also considered pragmatic and social criteria. A good explanation should be comprehensible, but it must avoid seductive clarity, where the mere feeling of clarity masks explanatory weakness. It should also be actionable, offering handles for intervention rather than just an attractive story. This was especially important in our discussion of mechanisms, cascades, constraints, and patterns, because different causal structures require different standards of explanatory excellence.

### Indeterminacy and pluralism: can there be multiple equally good explanations?

We concluded that there can indeed be multiple equally good explanations, but only in principled ways. One reason is that different explanatory questions bring different contrasts into view. Asking “Why P rather than Q?” can shift what counts as relevant. Another reason is that explanations can operate at different levels: a proximate explanation and an ultimate explanation, or a micro-mechanistic one and a macro-structural one, may both be correct without competing. A third reason is that explanatory aims vary. An explanation designed for prediction, one designed for control, one designed for unification, and one designed for policy design may all emphasize different aspects of the same phenomenon.

This is not a license for “anything goes.” It is a structured pluralism according to which multiple explanations may be valid because they capture different causal patterns or answer different explanatory tasks.

### The psychology of explanation: why bad explanations feel good

A major theme in our discussion was that human beings are often drawn to explanations for psychological reasons that are not themselves epistemically reliable. People seek closure, order, narrative coherence, and relief from uncertainty. We connected this tendency to the need for cognitive closure, where people seize on a quick explanation and then freeze on it, as well as to intolerance of ambiguity and premature convergence on the first satisfactory-sounding account.

We also discussed the illusion of explanatory depth. People often overestimate their understanding of complex systems because they confuse recognition, verbal fluency, or narrative coherence with genuine mechanistic knowledge. The larger lesson is that felt understanding is not a dependable sign of explanatory quality, especially in complicated domains where true understanding requires much more than a smooth or familiar narrative.

### Narrative vs explanation: what’s the difference and why it matters?

We distinguished narrative from explanation by noting that narratives are often organized around agents, motives, conflict, and moral legibility. They are typically strong at producing coherence and persuasion. Explanations, by contrast, in the more rigorous epistemic sense, are structured to support counterfactual discrimination and evidential assessment.

Narratives can still be explanatorily useful, especially as scaffolds for communication. However, their persuasiveness can become epistemically dangerous when narrative coherence substitutes for causal discrimination, adequacy constraints, and the testing of alternatives. A story may feel satisfying, but that alone does not make it an explanation in the stronger sense.

### Identity protection, anecdotes, and “anchored narratives”

We explored how narrative explanation is often entangled with identity protection, group membership, and social epistemic environments. In this context, anecdotes frequently function not just as bits of evidence, but as tools of identity reinforcement, trust signaling, and group alignment. They can serve as persuasive rhetorical anchors that stabilize a preferred interpretation.

At the same time, anecdotes need not be epistemically worthless. They can legitimately contribute to explanation if they are treated as data points within a broader evidential structure rather than as proof in themselves. They may help generate hypotheses that are later tested and triangulated. This connected to our discussion of anchored narratives and legal argumentation theory, where structured stories help make sense of evidence but must be firmly tied to facts and evaluated against alternatives if they are not to become mere just-so rationalizations.

### Social epistemology: “clarity” can be weaponized

Our discussion also developed a social-epistemic dimension. Explanations are not evaluated only in terms of their internal coherence or truth-tracking properties; they are also shaped by the environments and incentives in which they circulate. In hostile or pernicious epistemic environments, cognitive vulnerabilities can be exploited. The feeling of clarity can itself become an instrument of manipulation.

We examined how narrow source environments and in-group confirmation can trap groups inside self-reinforcing explanatory loops. In this sense, explanations can become socially satisfying and identity-stabilizing while remaining epistemically poor. This sharpened the broader concern that explanatory success in a social setting may diverge sharply from explanatory quality in an epistemic one.

### Contrastive explanation

A particularly important point was that explanation is often contrastive, and not merely a matter of binary counterfactual dependence. Good explanations frequently answer not just “Why did this happen?” but “Why did this happen rather than that alternative?” Their quality therefore depends in part on selecting the appropriate contrast class.

This idea helped bridge more abstract philosophical theories of explanation with everyday disputes about real-world explanation. Many disagreements that appear to be about causes are in fact disagreements about what contrast is being asked about. Clarifying that contrast can therefore clarify what would count as a good explanation.

### Mechanistic explanation: what it is, and how to evaluate it

We then turned to mechanistic explanation more specifically. Mechanisms were understood as organized entities and activities that produce a phenomenon. We considered their hierarchical and multi-level character, clarified what mechanisms are not, and examined how mechanistic explanations work.

A good mechanistic explanation, on our account, requires more than naming components. It must specify non-vacuous parts and activities, show how they are organized in space, time, and control relations, and provide evidence supporting the causal or constitutive claims involved. It must also give the right level of detail for the question being asked. Too little detail yields emptiness; too much can obscure what matters.

### “Yes, but what’s the mechanism?” (Bullock & Green)

We also considered Bullock and Green’s discussion of mechanism, especially in disciplinary contexts where “mechanism” is often used to mean mediators or transmission paths. This helped show why merely running mediation regressions can be misleading unless strong identification assumptions are satisfied.

The larger lesson for our discussion was that mechanism talk can easily become rhetorical rather than substantive. To claim a mechanism responsibly, one must earn the claim through methodological discipline, design, and defensible assumptions. Labeling something a mechanism is not enough.

### Ross’s causal pluralism: pathways, cascades, constraints, and structures

Ross became a key resource for demonstrating that mechanisms are not the only causal structures with explanatory power. We distinguished pathways from mechanisms by noting that pathways often track sequences, flows, and connectivity while abstracting away from fine-grained productive detail. Even without full mechanistic completeness, pathway explanations can still be genuinely explanatory.

Cascades were treated as another important explanatory form. They are characterized by triggers, sequential amplification, and stable propagation, often across levels and across systems. A cascade explanation can be excellent even if the underlying mechanisms vary, because what matters explanatorily is the topology of amplification and the dynamics of propagation.

We also examined structural and constraint-based explanations. These work by shaping the space of feasible trajectories, guiding outcomes rather than directly triggering them, and functioning as stable external conditions. This line of thought proved especially useful later in our discussion of misinformation, where structure influences diffusion pathways without necessarily acting as a direct push on each individual case.

### Misinformation: why cascade/structural explanations fit better than mechanistic ones

Misinformation provided a concrete case study for comparing explanatory forms. At the micro-level, mechanisms involving cognition, persuasion, or algorithmic ranking internals can explain local steps in the process. But cascade explanations are often better suited to explaining how a small trigger becomes large-scale diffusion. Structural constraint explanations, meanwhile, show why the environment systematically enables certain trajectories by means of low-friction sharing, incentive gradients, and network topology.

From this, we developed comparative rubrics for evaluating explanatory fit. The standards one should demand from a mechanism explanation differ from those appropriate to a cascade explanation or a structural explanation. Explanatory quality depends in part on matching the phenomenon to the right causal form.

### Potochnik: causal patterns, adequacy, and “eight other questions”

Potochnik supplied an important meta-framework for tying these threads together. One of her main contributions was the emphasis on **causal patterns**. Explanations, on this view, often succeed not by presenting complete causal histories but by depicting patterns of dependence together with their scope.

Her notion of an adequacy constraint was equally important. Abstraction is permissible, but only up to a point: one cannot abstract away from features to which the phenomenon is highly sensitive. This provides a minimum bar that guards against cherry-picked causes passing themselves off as explanations.

We also used her “eight other questions” as an audit tool for thinking about explanation more broadly. These questions concern communication, understanding, psychology, representation, abstraction and idealization, the relationship between explanation and prediction, ontological priority, and levels. They helped us show how public narratives about misinformation can be psychologically compelling and communicatively effective while still being explanatorily weak.

### Economics: why “false but useful” models aren’t necessarily failures

You introduced the economist’s perspective, which helped clarify that explanatory success is often task-dependent. We discussed benchmark models as reference points, the relaxation of assumptions as a controlled strategy for exploring frictions and strategic interaction, and econometrics as a credibility-driven way of identifying difference-making causes.

This led us to reframe the issue in terms of different explanatory jobs. Some models serve benchmark or contrastive explanation. Others provide structural how-possibly explanation. Still others aim at causal-pattern explanation or identification-backed counterfactual explanation. The contrast between economists and the broader public also connected back to our psychological and social-epistemic themes: for the public, a “good explanation” often means identity-stabilizing closure, whereas for economists it often means disciplined causal claims with explicit scope conditions and robustness checks.

### Complexity economics and systems thinking

We ended by situating complexity approaches within this broader framework. Complexity economics and systems thinking are not anti-abstraction; rather, they practice selective abstraction that foregrounds interactions, networks, heterogeneity, and out-of-equilibrium dynamics. These approaches are often evaluated in terms of generative adequacy, robustness and interpretability, empirical anchoring, and leverage-point insight.

This fit well with both Ross and Potochnik. Different causal structures, such as networks, cascades, and constraints, call for different explanatory standards. Explanatory quality therefore depends not on whether an account is micro-level or reducible to closed-form expression, but on whether it has the right scope and adequacy for the phenomenon in question.

# The unifying thesis of the series

The unifying conclusion of the discussion is that explanations are tools for making dependence intelligible, but they are also psychological and social artifacts. Because of this, a good explanation cannot be identified simply with coherence, plausibility, or even the mere truth of a causal claim.

A genuinely good explanation is one that matches the appropriate causal structure of the phenomenon, whether that structure is mechanistic, cascading, constraining, or patterned. It supports the right inferences, including counterfactuals, interventions, and discrimination among alternatives. It is abstracted appropriately, with clear scope and boundary conditions. It resists the seductions of clarity and the pressures of identity-driven closure. And it remains credible in light of the social-epistemic environment and the incentives that shape how explanations are produced, circulated, and accepted.