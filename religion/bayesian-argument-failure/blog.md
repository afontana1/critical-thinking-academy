# The Probability Was Never Established
*A Methodological Critique of Bayesian Arguments for God*

## Part I — The Methodological Asymmetry

### 1. Probability in Practice Versus Probability in Philosophical Argument

There is a peculiar asymmetry between the treatment of probability in applied disciplines and its use in contemporary philosophical arguments for the existence of God. In fields such as statistics, reliability engineering, risk analysis, and systems engineering, probabilistic assessments are subject to extensive methodological scrutiny. The construction of a probability model requires careful attention to the system under investigation, the assumptions governing its representation, the evidence available, the sources of uncertainty, and the conditions under which its conclusions can reasonably be applied. Yet in philosophical arguments for theism, probabilistic judgments of extraordinary metaphysical significance are frequently advanced without anything approaching this level of methodological accountability.

Consider a relatively ordinary problem in reliability engineering. An analyst is tasked with estimating the probability of catastrophic failure in a complex infrastructure system. The system may consist of numerous interacting components, operating under variable environmental conditions, subject to maintenance interventions, human decisions, organizational constraints, and dependencies that introduce the possibility of cascading or common-cause failures. The analyst's objective is not merely to identify conceivable configurations in which the system might fail. It is to construct a defensible assessment of failure risk within a specified operating context.

Doing so requires considerably more than assigning probabilities to a collection of imagined outcomes.

The analyst must first establish the boundaries of the system and specify what constitutes failure. Different definitions of failure may produce different assessments, and those definitions must correspond to the questions the analysis is intended to answer. The analyst must then identify relevant failure mechanisms, component dependencies, operating conditions, and sources of variation. Historical observations may provide useful information, but their applicability depends on how they were collected, whether they are representative of the conditions being modeled, and whether the system has changed in ways that undermine their relevance.

Uncertainty must also be characterized. Some uncertainty may arise from variability in the system's operating environment or component behavior. Other uncertainty may arise from incomplete measurements, insufficient data, unknown dependencies, uncertain model structure, or an inadequate understanding of the mechanisms producing failure. These uncertainties cannot simply be collapsed into an undifferentiated judgment of plausibility. They have different implications for model construction, inference, validation, and the interpretation of results.

Even after a mathematical model has been specified, the analyst must determine whether its assumptions are defensible. Are the assumed distributions appropriate? Are component failures independent, or does the model neglect shared vulnerabilities? Does the model adequately represent rare events? Is the system sufficiently stationary for historical observations to inform future predictions? How sensitive are the results to choices of parameters, model structure, or assumptions that cannot be independently verified?

These are not optional refinements that become relevant only after an otherwise complete probabilistic analysis has been performed. They are part of what makes the analysis credible in the first place.

Now imagine that the analyst instead presents the following reasoning: the system could conceivably occupy an enormous number of configurations; only a small subset of those configurations results in catastrophic failure; therefore, catastrophic failure is extraordinarily improbable.

No competent evaluation should accept that inference on its own. The size of a subset within an arbitrarily constructed configuration space does not establish the probability of the system entering that subset. The analyst would need to justify why those configurations constitute the relevant alternatives, how the system could actually occupy them, and what warrants the distribution used to evaluate their relative probabilities. Merely identifying possibilities, or intuitively judging their relative abundance, would not establish a defensible probability of failure.

Nor would the situation be rescued by expressing the argument in Bayesian notation. A formally coherent probability assignment does not automatically provide a credible representation of a system. The analyst could specify priors, construct likelihoods, perform mathematically correct updates, and produce a precise posterior estimate while having little justification for the assumptions determining the result. The calculation might be internally consistent while remaining epistemically inadequate for the purpose to which it is being applied.

This distinction between mathematical coherence and methodological justification is fundamental to applied probabilistic reasoning. Probability models are not evaluated solely by whether they satisfy the axioms of probability theory. They are also evaluated by whether their assumptions, representations, and inferential procedures are appropriate to the phenomena under investigation. A formally valid calculation can yield an unwarranted conclusion when the model on which it depends has not been adequately justified.

Against this background, the character of many probabilistic arguments for theism is striking.

Consider the familiar fine-tuning argument. The observation that certain physical constants fall within ranges compatible with life is treated as evidence that a life-permitting universe is extraordinarily improbable under naturalism. Or consider the argument from psychophysical harmony, according to which the apparent coordination between conscious experiences, physical states, and adaptive behavior is improbable because numerous alternative psychophysical relationships are supposedly conceivable. In both cases, a space of hypothetical alternatives is introduced, the observed outcome is characterized as occupying an unusually restricted portion of that space, and a judgment of improbability is used to motivate an inference favoring theism.

But what licenses these probabilistic judgments? What establishes the relevant alternatives? What justifies their purported probabilistic relationships? What independently supports the likelihood of the observations under the competing hypotheses? And what warrants treating the resulting comparison as informative about the actual world?

These questions are often left unresolved precisely where they are most important. The mathematical language of Bayesian confirmation may be employed without adequate justification for the probabilistic models that give the formalism substantive content. Appeals to what could have been otherwise may substitute for an account of what is genuinely possible. Assertions of improbability may rest on the apparent numerical predominance of hypothetical alternatives rather than a defensible probability measure. Likelihood comparisons may depend on speculative assumptions about the expectations of naturalism or the intentions of a divine creator.

The difficulty is not merely that these arguments lack numerical precision. Nor is it that every legitimate probability assessment must be derived from observed frequencies, repeatable experiments, or a known physical randomizing mechanism. Probabilistic reasoning can legitimately concern unique events, epistemic uncertainty, and hypotheses for which direct empirical calibration is unavailable. The methodological requirement is more general: an argument that purports to establish an evidential relationship through probability must justify the assumptions and inferential structure on which that relationship depends.

The absence of empirical data does not grant unrestricted license to substitute intuition for probabilistic justification. Nor does the fact that a question is philosophical exempt its probabilistic treatment from scrutiny. If anything, circumstances involving severe uncertainty, poorly constrained hypotheses, and limited opportunities for validation should make us more cautious about the conclusions that a probabilistic model can support.

This is the central methodological asymmetry. In applied disciplines, a probabilistic assessment that lacks adequate justification for its model, distributions, and relationship to the target system would be treated as methodologically deficient. Yet in philosophical arguments for theism, analogous deficiencies can be obscured by the formal appearance of Bayesian reasoning or by appeals to explanatory plausibility.

The issue is not whether philosophers are permitted to reason probabilistically. Of course they are. The issue is whether the probabilistic reasoning offered actually warrants the substantive conclusions drawn from it.

A probability assignment is not an evidential achievement merely because it is mathematically permissible. A likelihood comparison is not justified merely because it can be expressed using Bayes' theorem. And the identification of conceivable alternatives is not sufficient to establish that an observed state of affairs was improbable.

**The central distinction is between the formal availability of probability and the epistemic legitimacy of its application.** Much of the argumentative force of probabilistic theistic reasoning depends on treating the former as though it establishes the latter. The sections that follow will examine why that transition is unwarranted and how the failure to justify it undermines the purported evidential conclusions of these arguments.

## 2. The Significance of Consequential Reasoning and Decision Theory

The methodological asymmetry becomes even more striking when we consider the relationship between probability and decision-making. In applied disciplines, probabilistic assessments are rarely treated as isolated mathematical exercises. They are frequently constructed to inform decisions under uncertainty, where the adequacy of an assessment must be understood in relation to the decisions it is intended to support. This relationship is central to statistical decision theory, risk analysis, and the broader practice of evaluating complex systems.

Probability provides a formal framework for representing uncertainty, but the practical significance of a probabilistic assessment often emerges through its connection to possible actions and their consequences. In statistical decision theory, a decision-maker selects among available actions while facing uncertainty about the state of the world. Each action may produce different consequences depending on which state obtains, and these consequences can be represented through a loss or utility function. Under an established probabilistic model, the objective may be to select an action that minimizes expected loss.

A conventional Bayesian decision rule can be expressed as:

$$
a^*=\arg\min_{a\in A}\int_{\Theta}L(a,\theta)\,P(d\theta\mid D)
$$

Here, $$A$$ represents the set of available actions, $$\Theta$$ the space of uncertain states, $$L(a,\theta)$$ the loss associated with taking action $$a$$ when state $$\theta$$ obtains, and $$P(d\theta\mid D)$$ the posterior probability measure conditional on available evidence $$D$$.

The mathematical structure is straightforward. Its application, however, depends on a substantial collection of assumptions. The analyst must specify the relevant actions, characterize the possible states of the system, justify the probability model, and establish how the consequences of different actions should be evaluated. The resulting decision rule is optimal only relative to those specifications. If the probability model inadequately represents the system, or if important consequences have been excluded from the loss function, the formal optimality of the selected action offers little assurance that the decision is appropriate.

This illustrates an important feature of statistical decision theory: the formal calculation does not independently establish the adequacy of the decision. It specifies what follows conditional on a particular representation of uncertainty and consequences. The credibility of the decision therefore depends partly on the credibility of that representation.

In practical applications, this distinction receives considerable attention. Consider an engineering organization deciding whether to deploy a safety-critical system. A probabilistic reliability assessment might indicate that the probability of catastrophic failure lies below an established acceptance threshold. But the organization should not treat the result as decisive merely because the estimated probability is numerically small. It must consider how that estimate was obtained, whether the relevant failure mechanisms were adequately represented, and whether the conclusion remains defensible under uncertainty about the model itself.

A failure probability derived under assumptions of independent component behavior, for example, may be seriously misleading if important common-cause failures have been neglected. An estimate based on historical observations may lose relevance when operating conditions change. A model calibrated under ordinary circumstances may provide inadequate information about rare or unprecedented events. In such cases, the reported probability may be mathematically consistent with the model while failing to provide a sufficiently reliable basis for action.

The appropriate response is not always to produce a more elaborate probabilistic calculation. Depending on the available information, the analyst might investigate alternative models, conduct sensitivity analyses, establish uncertainty bounds, evaluate worst-case scenarios, or determine whether additional information would materially improve the decision. Where uncertainty is sufficiently severe, the analyst may conclude that the available evidence does not support a defensible probability estimate at all.

This is an important methodological outcome, not an analytical failure. Recognizing that a probability cannot presently be justified may be more informative than producing a precise estimate whose apparent authority exceeds its evidential foundations.

The connection to philosophical arguments for God's existence is direct, although it requires an important distinction. Accepting a proposition as true is not identical to choosing an engineering intervention, and philosophical belief cannot simply be reduced to an ordinary decision problem. Beliefs are not always under voluntary control, and the standards governing rational belief are not identical to those governing practical action. Nevertheless, probabilistic arguments for theism are explicitly concerned with what an individual should regard as rationally supported by the available evidence. They seek to establish that certain observations warrant an increase in confidence in the existence of God, sometimes to a degree intended to make theistic belief rationally preferable to its alternatives.

The implications of such a conclusion are substantial. Accepting the existence of a divine creator may involve a fundamental revision of one's ontology: the introduction of an intentional agent whose existence is not reducible to the physical structures ordinarily invoked in scientific explanation, and whose alleged purposes or activities may be used to account for features of the universe. Depending on the particular conception of God, this commitment may also affect views concerning causation, consciousness, morality, human purpose, and the ultimate structure of reality.

These are not trivial implications. A probabilistic argument that purports to establish significant evidential support for such a conclusion is therefore making a claim with potentially far-reaching intellectual and practical consequences.

Yet the probabilistic foundations of these arguments often receive less scrutiny than those employed in comparatively ordinary applied decisions. In the fine-tuning argument, a judgment about the improbability of life-permitting physical constants may depend on an inadequately justified distribution over hypothetical physical possibilities. In the argument from psychophysical harmony, a judgment about the improbability of harmonious relationships between consciousness and physical states may depend on speculative assumptions about conceivable alternative mappings. In both cases, further likelihood judgments are introduced to establish that the observations favor theism over naturalism.

The resulting claims are not merely that certain observations are compatible with a theistic worldview. They purport to establish a comparative evidential relationship between competing accounts of reality. This is precisely where the methodological burden becomes substantial. If the likelihoods have not been adequately justified, if the relevant alternatives have not been established, or if the probabilistic conclusions depend critically on arbitrary auxiliary assumptions, the argument cannot claim evidential authority simply by appealing to the formal legitimacy of Bayesian inference.

The contrast with applied decision-making raises an obvious question: why should probabilistic assessments supporting major ontological commitments be permitted to proceed on assumptions that would be considered inadequate when evaluating the reliability of a physical or organizational system?

This question should not be misunderstood as proposing that the truth of a metaphysical proposition depends on the consequences of believing it. The existence or nonexistence of God is not determined by the practical significance of the belief. Nor do high stakes automatically alter the evidential likelihood of an observation under a hypothesis. The distinction between evidential support and the consequences of accepting or acting upon a proposition must be preserved.

Rather, the point concerns the responsible use of uncertain information. The greater the significance of a conclusion, the more consequential it becomes to distinguish what has actually been established from what is merely assumed, conjectured, or represented within a hypothetical model. Where the conclusion rests on uncertain or unvalidated probabilistic assumptions, responsible reasoning requires that those limitations be made explicit rather than concealed beneath the apparent precision of the resulting inference.

Decision theory also illustrates why the failure to justify a probability assessment cannot simply be resolved by proceeding as though the uncertainty were negligible. A decision made under a single probabilistic model may appear optimal, while a different but comparably defensible model may recommend another action. If the conclusion changes substantially across plausible model specifications, its apparent decisiveness may be an artifact of the chosen assumptions. Recognizing this problem is central to robust decision-making: one should distinguish conclusions that remain defensible across relevant uncertainties from conclusions that depend on a narrow and poorly supported specification of the problem.

An analogous concern arises in Bayesian arguments for theism. If the conclusion that some observation favors theism depends on a particular prior, a speculative account of divine preferences, or an arbitrary distribution over hypothetical alternatives, then the argument must justify those assumptions. It is not enough to demonstrate that the conclusion follows once they have been adopted. What requires justification is precisely why those assumptions should govern our assessment of the evidence.

Importantly, this does not mean that a philosophical argument must satisfy every technical requirement of engineering reliability analysis. Metaphysical hypotheses are not physical components whose failure frequencies can ordinarily be measured, and philosophical inquiry need not reproduce the empirical methods of reliability engineering. Statistical decision theory itself permits subjective probabilities, and coherent reasoning under uncertainty is possible even where objective chances or repeated observations are unavailable.

But these differences do not eliminate the more general requirement of methodological accountability. They do not establish that arbitrary priors, unconstrained likelihoods, or inadequately specified hypothesis spaces can support substantive evidential conclusions. If the available information does not determine a defensible comparative assessment, the appropriate epistemic response may be to acknowledge that limitation rather than manufacture a conclusion through the selection of convenient assumptions.

There is also an important difference between showing that a conclusion follows within a stipulated probabilistic framework and establishing that the framework provides reasons for anyone to accept that conclusion about reality. The former is a conditional mathematical result. The latter is a substantive epistemic achievement. Confusing these two accomplishments is especially problematic when the conclusion is presented as a reason to adopt an entirely different ontological account of the world.

The lesson from statistical decision theory is therefore not that metaphysical beliefs must be evaluated according to engineering acceptance thresholds, nor that probability is legitimate only when it directly informs an observable practical action. It is that probabilistic conclusions derive their authority from more than their formal coherence. Their relevance to rational judgment depends on the assumptions supporting them, the uncertainties they neglect or represent, and the extent to which their conclusions remain defensible when those assumptions are scrutinized.

This returns us to the central asymmetry. In applied probabilistic reasoning, consequential decisions invite extensive scrutiny of model adequacy, uncertainty, and robustness. In probabilistic arguments for theism, similarly consequential conclusions can be presented despite profound uncertainty about the construction and justification of the relevant probability models.

The significance of the conclusion cannot compensate for weakness in the inference. If anything, it makes the distinction between justified evidence and speculative probabilistic representation more important.

**Before a probabilistic argument can reasonably support a major ontological commitment, it must first establish that its probabilistic comparison is epistemically warranted. Without that foundation, the apparent evidential force of the argument remains conditional on assumptions whose legitimacy has yet to be demonstrated.**

# Part II — The Foundations of Probabilistic Inference

## 3. The Conflation of Conceivability, Possibility, Plausibility, and Probability

One of the most pervasive methodological problems in probabilistic arguments for theism is the insufficiently justified movement between conceivability, metaphysical possibility, epistemic possibility, plausibility, and probability. These concepts are frequently employed as though they form a natural inferential progression: an alternative can be conceived, it is therefore regarded as possible, its apparent possibility is treated as grounds for assessing its plausibility, and that plausibility is subsequently incorporated into an argument about probability. Yet each transition introduces substantive assumptions that require independent justification. Without those justifications, the resulting probabilistic claims lack the foundations necessary to support the evidential conclusions drawn from them.

The problem begins with conceivability. In its ordinary sense, conceivability concerns our capacity to imagine, describe, or entertain a state of affairs without immediately recognizing a contradiction. We may conceive of a universe governed by different physical laws, alternative relationships between consciousness and physical states, or a world in which certain familiar properties are associated with different objects or processes. But the ability to formulate such descriptions does not establish that they represent genuine metaphysical possibilities.

This distinction matters because our capacities for conceiving alternatives are constrained by our knowledge, conceptual resources, and understanding of the phenomena involved. A description may appear coherent because it omits precisely those features that would reveal its incoherence under a more complete account of the relevant system. What appears possible under an incomplete description may turn out to be impossible once the dependencies, identities, or necessary relationships governing the phenomenon are understood.

Consider a mathematical analogy. Someone unfamiliar with the relevant mathematical constraints might conceive of an object satisfying a collection of properties that cannot, in fact, be jointly instantiated. The apparent conceivability of the object would reflect a limitation in their understanding rather than a genuine possibility within the mathematical structure. The absence of an immediately recognizable contradiction would not establish that the proposed object could exist.

Something similar can occur when reasoning about physical or metaphysical alternatives. We might imagine physical constants taking different values while holding the remaining structure of physical theory fixed. But this imagined variation does not establish that those constants are independently variable within a more complete physical theory. Nor does imagining conscious experiences associated with different physical processes establish that phenomenal and physical properties can genuinely be recombined in the proposed manner. In both cases, the apparent coherence of the alternative may depend on an incomplete understanding of the relationships governing the actual phenomenon.

This is not to claim that conceivability is always irrelevant to metaphysical possibility. Philosophical theories of modality differ over the circumstances in which conceivability can provide evidence of possibility. Some sophisticated accounts attempt to distinguish forms of conceivability that are more or less reliable indicators of metaphysical possibility. But those accounts themselves require philosophical justification. The crucial point is that conceivability does not automatically establish the modal status of what is conceived, particularly when the proposed alternative concerns phenomena whose underlying nature remains poorly understood.

A probabilistic argument that relies on the metaphysical possibility of imagined alternatives must therefore defend the relevant modal assumptions. It cannot simply take the absence of an obvious contradiction as sufficient evidence that the alternatives belong to the space of genuine possibilities.

A further distinction must be drawn between metaphysical possibility and epistemic possibility. Metaphysical possibility concerns what could obtain given the nature of reality, including whatever necessary relationships hold among its properties. Epistemic possibility concerns what remains open relative to some specified body of knowledge or information. Something can remain epistemically possible because we do not know enough to rule it out, even if it is metaphysically impossible.

For example, before learning the relevant mathematical facts, someone might regard two mutually incompatible mathematical claims as epistemically open. Their uncertainty would not make both claims mathematically possible. It would reflect the limits of what they knew.

Likewise, our present inability to establish whether certain psychophysical relationships are necessary does not imply that they are metaphysically contingent. We may be unable to rule out alternative relationships from our current epistemic position, but this establishes something about the limitations of our knowledge, not necessarily about the modal structure of reality.

The distinction becomes especially important when epistemic possibility is used to justify probabilistic reasoning. A defender of a philosophical probability argument might concede that the imagined alternatives are not known to be metaphysically possible while maintaining that they remain epistemically possible and can therefore receive epistemic probabilities.

This response does not resolve the underlying difficulty. The fact that a proposition has not been excluded by our knowledge does not establish any particular probability for it. Epistemic openness is not a probability measure. A collection of alternatives that remain compatible with incomplete information does not come equipped with a distribution of rational credences merely because we have not determined which alternatives are actually realizable.

This brings us to the distinction between possibility and probability.

In formal probability theory, probabilities are assigned relative to a probability space consisting of a sample space, a collection of measurable events, and a probability measure:

$$
(\Omega,\mathcal{F},P)
$$

The set $$\Omega$$ identifies the elementary outcomes represented by the model, $$\mathcal{F}$$ identifies the events to which probabilities are assigned, and $$P$$ specifies the probability measure.

The identification of possible outcomes does not independently determine the measure. Even if we granted that some collection of alternatives constitutes a legitimate space of possibilities, nothing about that fact alone establishes how probability should be distributed across the alternatives.

Suppose we identify a collection of hypothetical configurations and designate a subset as exhibiting some property of interest. The mere fact that this subset occupies a small portion of the described space does not demonstrate that the property is improbable. Such a conclusion requires additional assumptions about how probabilities are assigned across the space.

For a finite set of alternatives, one might be tempted to reason that if only $$k$$ of $$n$$ possible configurations exhibit a property, then the probability of observing that property is:

$$
P(H)=\frac{k}{n}
$$

But this expression follows only under an appropriate equiprobability assumption. The existence of $$n$$ alternatives does not establish that each alternative has probability $$1/n$$, nor does it establish that this manner of counting alternatives is privileged.

The problem becomes even more substantial when the alternatives are continuous, multidimensional, incompletely specified, or dependent on an arbitrary choice of representation. In such circumstances, probability cannot generally be inferred from a simple enumeration of alternatives, and even the notion of relative size depends on how the space is constructed and measured.

An additional difficulty arises when the relevant alternatives have been generated through unconstrained imagination. The number of alternatives someone can describe may depend on the language used, the distinctions they choose to introduce, the granularity of their descriptions, and the assumptions under which they permit alternatives to vary. There is no reason to think that the relative abundance of such descriptions tracks the relative probability of the states of affairs they purport to represent.

This reveals a deeper methodological concern. A philosophical argument may construct an expansive set of hypothetical alternatives and then characterize the observed state of affairs as exceptional within that set. But unless the construction of the space and the assignment of probabilities are independently justified, the apparent exceptionalism may be an artifact of the representation rather than an evidential fact about reality.

The distinction between plausibility and probability introduces another source of confusion.

Plausibility is often used to express an informal judgment concerning how credible, reasonable, or intellectually attractive a proposition appears. Such judgments may be informed by evidence, theoretical commitments, familiarity, explanatory considerations, or background expectations. However, plausibility is not itself a uniquely specified probabilistic quantity. Different individuals may regard the same hypothesis as plausible for different reasons, and those judgments need not correspond to a common or defensible probability assignment.

This does not mean that qualitative judgments are inherently illegitimate or that every rational assessment must be numerical. Informal plausibility assessments can play an important role in scientific reasoning, philosophical inquiry, and the development of hypotheses. The problem arises when such assessments are treated as though they independently establish probabilistic relationships.

For example, someone might argue that it is plausible that a benevolent deity would create a universe containing conscious beings capable of flourishing. Even if that claim were granted as an intelligible philosophical intuition, it would not establish a particular likelihood for such a universe under theism. Nor would it independently show that the observed universe is more probable under theism than under naturalism.

To establish that comparative conclusion, one must explain why the observation should be expected to a greater degree under one hypothesis than the other. Merely finding an observation compatible with a hypothesis, or constructing a narrative under which the observation appears unsurprising, does not establish the required evidential relationship.

These distinctions are especially important because philosophical arguments for theism frequently concern domains in which the conditions necessary for probabilistic inference are unusually difficult to establish. We do not have independent access to a population of universes from which observed physical constants have been sampled. We do not possess a settled account of the metaphysical relationship between consciousness and physical states that would independently establish which psychophysical alternatives are genuinely available. Nor do broad ontological hypotheses such as theism and naturalism automatically determine distributions over the phenomena they are invoked to explain.

Under these circumstances, the construction of hypothetical alternatives requires exceptional care. The fact that we can formulate different descriptions of reality does not establish their physical or metaphysical realizability. The fact that we cannot exclude those descriptions does not establish their relative epistemic probabilities. And the fact that one description appears more intuitively plausible than another does not establish a justified likelihood ordering.

A crucial distinction must also be maintained between uncertainty about the truth of a proposition and evidence that the proposition was unlikely to be true. Our ignorance of why some phenomenon obtains is not itself evidence that the phenomenon was improbable. A lack of explanatory understanding may justify uncertainty, but uncertainty about a phenomenon's explanation is not equivalent to a probability distribution over alternative explanations or outcomes.

This point is central to both the fine-tuning and psychophysical harmony arguments. The observation that we do not presently know why certain physical constants have their observed values does not establish that those values were improbable under naturalism. Similarly, the observation that we do not fully understand why conscious experiences correspond to particular physical or functional states does not establish that the observed correspondence is unlikely.

In either case, the argument requires an additional inferential step from the limits of our explanatory knowledge to a substantive claim about probability. That step cannot be supplied merely by appealing to the abundance of imagined alternatives.

It is therefore important to distinguish between using a possibility space as a heuristic device and using it as the foundation of an evidential inference. Hypothetical alternatives can be useful for conceptual exploration. They may clarify the commitments of a theory, expose dependencies, or help formulate questions for further investigation. But their heuristic usefulness does not confer probabilistic authority. A conceptual exercise does not become evidence of improbability simply because it describes many ways in which things might have been different.

The methodological failure occurs when these distinctions are collapsed. Conceivability is treated as sufficient grounds for possibility; possibility is treated as though it supplies a probability space with a privileged measure; intuitive plausibility is treated as a defensible likelihood; and the resulting probabilistic comparison is presented as evidence for a substantive metaphysical conclusion.

None of these transitions is automatic, and each requires justification appropriate to the claim being made.

This does not imply that probabilistic reasoning about metaphysical hypotheses is impossible in principle. It implies that the legitimacy of such reasoning cannot be assumed merely because the hypotheses can be entertained or because a probability function can be formally defined over them. If a probabilistic argument is to establish that some observation favors one metaphysical hypothesis over another, it must justify how the relevant alternatives have been identified, why the probabilistic representation is appropriate, and what warrants the particular comparative judgment.

The burden is especially significant when the alleged improbability of an observation depends almost entirely on a constructed space of counterfactual alternatives. If that space lacks independent justification, or if the probability measure over it is arbitrary, then the apparent improbability has not been established. The argument has supplied a representation of uncertainty, but it has not demonstrated that the representation provides evidence about the world.

**Conceivability is not a demonstration of possibility. Possibility is not a probability distribution. Plausibility is not a likelihood. And none of these distinctions can be bypassed merely by expressing the resulting judgment in Bayesian notation.**

The next section examines the mathematical and methodological consequences of this problem more closely. Even when a domain of alternatives is granted for the sake of argument, the construction of a defensible probability measure remains an independent and frequently unresolved task. This is where the difference between identifying possible outcomes and establishing their probabilities becomes especially consequential.

## 4. The Arbitrary Construction of Probability Spaces

The distinction between possibility and probability introduces a more fundamental mathematical problem: even when a domain of alternatives has been identified, there is no general principle by which its mere existence determines a probability distribution. A collection of conceivable or possible states of affairs is not, by itself, a probabilistic model. The construction of such a model requires additional mathematical structure, and the selection of that structure introduces substantive assumptions that must be justified independently of the conclusions derived from it.

This distinction is elementary in probability theory but frequently obscured in philosophical arguments that attempt to infer improbability from the apparent abundance of hypothetical alternatives. The underlying assumption is often that if some observed condition occupies a sufficiently restricted portion of a space of possibilities, the observation must be improbable. Yet the conclusion does not follow unless a suitable probability measure has been established over that space. The relative size of a region under some chosen representation is not intrinsically equivalent to its probability, and the identification of numerous alternatives does not independently tell us how credence or chance should be distributed among them.

The formal structure of probability makes this clear. A probability space is conventionally represented by the triple:

$$
(\Omega,\mathcal{F},P)
$$

Here, $$\Omega$$ denotes the sample space of elementary outcomes, $$\mathcal{F}$$ is a sigma-algebra identifying the events to which probabilities may be assigned, and $$P$$ is a probability measure satisfying the relevant axioms, including nonnegativity, normalization, and countable additivity.

These components serve different functions. The sample space identifies the outcomes represented within the model. The sigma-algebra specifies which collections of outcomes are treated as measurable events. The probability measure assigns probabilities to those events.

The crucial point is that specifying the first component does not determine the third.

For a given measurable space, numerous probability measures may be mathematically admissible. Those measures can assign radically different probabilities to the same event while satisfying precisely the same probability axioms. Nothing about mathematical consistency alone establishes which measure, if any, should govern an inference about the world.

Suppose a set of hypothetical outcomes has been specified, and let $$H$$ denote the subset exhibiting some property of interest. Its probability is given by:

$$
P(H)=\int_{\Omega}\mathbf{1}_H(\omega)\,P(d\omega)
$$

The value of this expression depends on the measure $$P$$. It cannot be recovered merely by identifying the subset $$H$$ or describing its apparent size.

In applied probabilistic modeling, this distinction is indispensable. When estimating a system's reliability, an analyst does not ordinarily infer the probability of failure by counting the number of conceivable configurations in which failure occurs. The analyst must establish a probability model that adequately represents the mechanisms, conditions, dependencies, and uncertainties relevant to the system. The probability measure is not supplied by the conceptual availability of alternative configurations. It must be justified in relation to the question being investigated.

The same requirement cannot simply be suspended when the subject matter shifts from engineered systems to metaphysical hypotheses.

### The principle of indifference and the illusion of equiprobability

A common response to the absence of an established distribution is to invoke some version of the principle of indifference: where there is no reason to prefer one alternative over another, the alternatives should receive equal probabilities.

In certain well-specified circumstances, symmetry considerations can justify equiprobability. For example, if a physical system possesses relevant symmetries and there are defensible reasons to treat its outcomes as exchangeable, a uniform distribution may be appropriate. Similarly, particular mathematical models may assign equal probability to elementary outcomes by construction.

But the absence of a known reason to distinguish alternatives is not itself evidence that the alternatives are equally probable.

Ignorance about the probability structure of a phenomenon does not establish a uniform probability structure. Treating all alternatives as equally probable introduces an additional assumption about their relative weighting. Unless that assumption is independently justified, the resulting probabilities reflect the selected modeling convention rather than an established feature of the phenomenon.

Consider a finite space containing $$n$$ elementary outcomes, of which $$k$$ satisfy some condition $$H$$. Under an equiprobability assumption, we obtain:

$$
P(H)=\frac{k}{n}
$$

But this follows only if the elementary outcomes have been appropriately specified and each has been assigned probability $$1/n$$. If the outcomes are not equiprobable, the probability instead depends on their individual weights:

$$
P(H)=\sum_{\omega_i\in H}P(\{\omega_i\})
$$

The distinction is decisive. Counting outcomes provides a probability only when the assumptions linking the count to the measure have already been established.

A further difficulty is that equiprobability can depend on how the alternatives are individuated.

Imagine a model that initially distinguishes two outcomes, labeled A and B. If we apply indifference directly, we assign each probability one-half. But suppose B is subsequently divided into nine more specific alternatives, while A remains undivided. Applying indifference to the resulting ten descriptions assigns A a probability of one-tenth.

Nothing about the underlying phenomenon has necessarily changed. What has changed is the partition over which indifference is imposed.

Of course, refining a partition does not alter probabilities when a previously established measure is preserved. The inconsistency arises when uniform probability is independently imposed upon whichever partition happens to be selected.

The example illustrates why an arbitrary enumeration of possibilities cannot generate an objective or uniquely rational probability distribution. Without principled constraints on the identification and weighting of alternatives, the resulting probabilities can depend on descriptive choices that have no demonstrated connection to the phenomenon being investigated.

This problem is especially serious in arguments involving hypothetical universes or psychophysical mappings. What counts as an elementary alternative? Which differences warrant separate outcomes? How finely should alternatives be distinguished? Why should the resulting descriptions be treated as equiprobable, or even as having comparable probabilistic weight?

If these questions have not been answered, the apparent numerical dominance of one class of alternatives has no established probabilistic significance.

### Parameterization dependence and the absence of a privileged measure

The problem becomes more pronounced when the alternatives are represented by continuously varying parameters.

Suppose an uncertain quantity can take values within the interval from zero to one. One modeling choice is to assign a uniform distribution directly to that quantity. Under this assumption, the probability that its value is less than some threshold is proportional to the threshold itself.

Let the quantity be denoted by $$X$$, and suppose:

$$
X\sim\operatorname{Uniform}(0,1)
$$

Then, for a threshold $$0<\varepsilon<1$$:

$$
P(X<\varepsilon)=\varepsilon
$$

Now consider a different parameterization:

$$
Y=X^2
$$

Suppose someone independently assumes that $$Y$$, rather than $$X$$, should be uniformly distributed over the interval from zero to one:

$$
Y\sim\operatorname{Uniform}(0,1)
$$

Since the event that $$X$$ is less than $$\varepsilon$$ corresponds to the event that $$Y$$ is less than $$\varepsilon^2$$, the second assumption yields:

$$
P(X<\varepsilon)=\varepsilon^2
$$

The two models therefore assign different probabilities to the same event.

Importantly, this is not a failure of probability theory to preserve probabilities under transformations. If a probability measure is properly transformed from one coordinate system to another, the probability of a given event remains unchanged. The discrepancy arises because assuming uniformity in each parameterization independently defines different probability measures.

That is precisely the methodological issue.

If no independent principle privileges uniformity in $$X$$ over uniformity in $$Y$$, then neither distribution can claim authority merely because it appears mathematically natural in its chosen coordinates.

The choice of parameterization has introduced a substantive assumption about the underlying probability measure.

More generally, a probability density changes under a differentiable, invertible transformation according to the relevant Jacobian. If:

$$
Y=g(X)
$$

then the transformed density satisfies:

$$
f_Y(y)
=
f_X(g^{-1}(y))
\left|
\frac{d}{dy}g^{-1}(y)
\right|
$$

A density that is constant in one parameterization will not generally remain constant in another. Consequently, the instruction to assign a uniform prior is incomplete unless the relevant parameterization and the justification for privileging it have been established.

The problem is not merely technical. When philosophical arguments describe certain physical constants, psychophysical relationships, or hypothetical configurations as occupying an extraordinarily small region of a possibility space, their conclusions may depend heavily on the coordinates and measures used to represent those alternatives.

In continuous spaces, the numerical width or volume of a region is not an invariant indication of probability. Relative volume acquires probabilistic significance only after a measure has been specified, and the choice of measure requires justification.

The appeal to uniformity becomes still more difficult in unbounded parameter spaces, where a normalized uniform probability distribution may not exist. An improper prior can sometimes be employed within a justified statistical procedure, but it cannot automatically be treated as a probability distribution over possible outcomes. Its legitimacy depends on additional conditions, including the propriety of the resulting posterior when Bayesian inference is performed.

These complications demonstrate the inadequacy of moving directly from the apparent narrowness of an outcome to its alleged improbability.

A region can be mathematically narrow under some description without being improbable under a justified probability model. Conversely, a broad region need not receive high probability. Geometric size and probability are distinct quantities, and their relationship is determined by the measure being employed.

### The distinction between a mathematical representation and a model of reality

There is a broader epistemological problem underlying these examples. Mathematical probability spaces are extraordinarily flexible. We can construct sample spaces and assign probability measures to virtually any suitably defined collection of hypothetical outcomes.

But the fact that a probability model can be constructed does not establish that it adequately represents the phenomenon to which it is applied.

A model can be mathematically well-defined while lacking substantive justification. It can satisfy every probability axiom while employing arbitrary distributions, omitting relevant dependencies, or representing alternatives that have no established relationship to the actual system.

In applied statistics, this distinction appears in questions concerning model specification, identifiability, validation, and the relationship between mathematical assumptions and empirical observations. Probabilities acquire substantive relevance through the interpretation and justification of the model, not merely through the formal consistency of its construction.

A stochastic model of component failures, for example, may be justified through knowledge of degradation mechanisms, empirical failure data, physical constraints, and operational experience. Even when such information is incomplete, the analyst can distinguish assumptions supported by available evidence from assumptions introduced for tractability or exploratory purposes.

A philosophical model need not possess precisely the same empirical basis to be meaningful. Probabilities can represent rational credences rather than objective physical chances, and some epistemic judgments concern events that are not generated by repeatable stochastic mechanisms.

Nevertheless, an epistemic interpretation does not eliminate the question of justification.

If a probability measure represents rational credence, one must explain why the particular distribution is rationally warranted. If it represents objective chance, one must explain what makes it appropriate to the physical process. If it is introduced as a hypothetical modeling convention, one must distinguish conclusions conditional on that convention from conclusions purporting to establish evidence about reality.

These interpretations differ, but none permits the mere construction of a probability measure to establish its own epistemic authority.

Probability theory imposes coherence constraints on the mathematical representation of uncertainty. It does not, by itself, determine which representation is appropriate to an incompletely understood phenomenon.

This difference between mathematical admissibility and substantive adequacy is central to the present critique.

### The problem of physically and metaphysically unconstrained alternatives

In fine-tuning arguments, the relevant alternatives are commonly represented as different possible values of physical constants or parameters. The observed values are then compared with hypothetical values that would allegedly prevent the emergence of life.

But constructing such a space already involves substantive assumptions.

It assumes that the selected quantities can meaningfully vary in the proposed manner. It assumes that their values can be considered within specified ranges. It may assume that some parameters can vary independently while others remain fixed. It also presupposes a theoretical framework within which the consequences of those variations can be evaluated.

None of these assumptions follows from the fact that physical theories contain numerical parameters.

A parameter appearing as freely specifiable within an effective physical theory need not be independently variable within a more fundamental theory. What appears contingent at one level of theoretical description may be constrained by relationships not represented at that level. Likewise, a procedure that varies one constant while holding others fixed may explore a mathematically defined family of models without demonstrating that the family corresponds to physically realizable alternatives.

Such exercises can be scientifically informative. They may reveal dependencies within a theory or identify conditions required for particular physical structures. But the exploration of theoretical alternatives is not equivalent to demonstrating a probability distribution over possible universes.

The same distinction applies to the selection of parameter ranges. Why should the relevant range have one set of endpoints rather than another? Why should probability be uniform over the chosen range? Why should one measure or parameterization be treated as privileged? And how are dependencies between parameters incorporated?

Without answers, any resulting numerical improbability remains conditional on the stipulated model.

The argument from psychophysical harmony faces an even earlier problem. Its proposed sample space consists of alternative relationships between conscious experiences and physical or functional states. Yet the legitimacy of treating these relationships as independently recombinable is itself a controversial metaphysical assumption.

Before a probability measure can be justified, the argument must explain why the proposed domain constitutes an appropriate space of alternatives. The sheer number of imagined disharmonious mappings cannot establish their relative probability, particularly when the coherence and metaphysical status of those mappings remain unresolved.

This exposes two distinct levels of underdetermination.

First, the space of alternatives may lack adequate justification. Second, even if that space is granted, the probability measure over it remains unspecified.

A probability assignment cannot resolve the first problem merely by supplying mathematical structure for the second.

### Selection effects and the conditions of observation

The interpretation of an observed outcome can also depend on the conditions under which that outcome becomes observable.

In applied statistical analysis, sampling and selection mechanisms can substantially alter the relationship between observed data and the underlying process. An observation obtained through a selective procedure cannot necessarily be interpreted as though it were drawn without selection from a broader population.

The same general concern arises in cosmological arguments.

Observers capable of investigating physical constants necessarily exist under conditions compatible with their existence. This does not, by itself, establish that life-permitting conditions are common, probable, or unsurprising under any particular cosmological model. Nor does it settle the fine-tuning argument.

It does mean that the evidential interpretation of the observation cannot ignore the relationship between the existence of observers and the conditions they observe.

A probabilistic argument must distinguish the probability that certain conditions obtain from the probability of observing those conditions given the relevant observational circumstances. The appropriate treatment depends on the hypotheses being compared, the proposed reference class, and the selection mechanism.

These details are not incidental to the evidential calculation. They are part of specifying what the evidence is and how its probability should be evaluated.

Without such specification, there is a risk of treating an observation made under particular selection conditions as though it had arisen through a different probabilistic process.

### From conditional calculations to unsupported evidential conclusions

The methodological problem can now be stated more precisely.

Suppose a philosophical argument identifies a set of hypothetical alternatives, chooses a measure over those alternatives, and establishes that a particular observation has low probability under the selected measure.

For the sake of argument, assume that the mathematics is correct.

What has been established?

At most, the argument has demonstrated that the observation is improbable relative to the stipulated probability model.

That is a legitimate conditional mathematical result. But it is not yet a justified claim that the observation was improbable under the metaphysical hypothesis being evaluated.

To make that further inference, the argument must establish why the selected probability model is appropriate to the hypothesis and the phenomenon.

If the model is supported only by an appeal to imagined alternatives, intuitive symmetry, arbitrary ranges, or a convenient parameterization, the evidential conclusion has not been independently established.

This is especially consequential when an argument compares broad metaphysical hypotheses. Theism and naturalism are not themselves uniquely specified probability measures over physical constants, conscious experiences, or possible universes. Deriving likelihoods from them requires auxiliary assumptions about what those hypotheses imply or lead us to expect.

The justification of those assumptions cannot be bypassed by presenting the resulting probabilities as though they belonged intrinsically to the hypotheses.

Nor does introducing a new label, such as *intrinsic probability*, resolve the issue. A proposed concept of intrinsic probability may be meaningful within a philosophical theory, but the theory must still explain what determines that probability, why the proposed assignments are warranted, and how they support the relevant evidential inference.

Naming a probability does not establish its measure. Characterizing a distribution as natural does not establish its appropriateness. And invoking epistemic uncertainty does not determine how that uncertainty should be distributed.

The same considerations apply to claims that a probability need only be approximately low rather than numerically precise. It is true that many legitimate arguments require only an inequality or a qualitative ordering. But even such claims depend on assumptions about the relevant probability measures. If those assumptions remain unconstrained, the argument may be unable to establish even the direction of the proposed evidential comparison.

The failure is therefore not necessarily one of numerical accuracy. It is more fundamental: the argument has not justified the probabilistic structure required to make its asserted numerical or qualitative conclusion evidentially authoritative.

This is why the distinction between constructing a probability model and justifying its application must remain central.

A mathematical model can be useful for exploring what follows from particular assumptions. But the inferential significance of its conclusions depends on whether those assumptions are defensible. Where the model is only one among numerous admissible representations, and no principled reason is provided for privileging it, its conclusions cannot simply be promoted from conditional results to claims about the actual likelihood of the observed world.

**The existence of a possibility space does not determine a probability measure. The existence of a probability measure does not establish its appropriateness. And the mathematical correctness of a result does not demonstrate that its underlying model provides justified evidence about reality.**

These are distinct methodological obligations. Probabilistic arguments for theism frequently depend on moving through them without supplying the necessary justifications.

The resulting problem cannot be repaired by increasingly elaborate mathematics. Greater formal sophistication may make the conditional structure of an argument clearer, but it cannot independently establish the legitimacy of the assumptions on which that structure depends.

What is missing is not merely a better calculation. It is a defensible account of why the probability being calculated is the probability relevant to the evidential conclusion.

This problem carries directly into Bayesian confirmation, where speculative priors and likelihoods can be combined into apparently precise posterior assessments. The next section examines why Bayesian coherence, subjective probability, and appeals to theoretical virtues do not independently resolve the foundational problem of probabilistic justification.

## 5. Bayesian Formalism, Unjustified Prior Specification, and Unsupported Likelihoods

The preceding discussion established that the construction of a probability space and the assignment of a probability measure are distinct methodological tasks. Even when a set of alternatives has been defined, its existence does not determine how probability should be distributed across those alternatives. Nor does the mathematical admissibility of a particular distribution establish that it provides an appropriate representation of the phenomenon under investigation. These difficulties become especially consequential when probability assignments are incorporated into Bayesian arguments, where the formal structure of conditional probability can give speculative assumptions the appearance of rigorous evidential conclusions.

Bayesian reasoning provides a powerful framework for updating probabilities in light of evidence. Its mathematical legitimacy is not in dispute. The problem arises when the validity of the formal updating procedure is treated as though it independently justifies the probabilities supplied to that procedure. Bayes' theorem specifies relationships among conditional probabilities, but it does not establish which hypotheses should be considered, how their prior probabilities should be determined, or which likelihood functions adequately represent the evidence under investigation. These are substantive modeling questions, and the evidential significance of a Bayesian calculation depends on how they are answered.

Consider a standard Bayesian comparison between theism and naturalism. Let $$T$$ represent theism, $$N$$ represent naturalism, and $$E$$ represent some observation alleged to support theism. Their posterior odds can be expressed as:

$$
\frac{P(T\mid E)}{P(N\mid E)}
=
\frac{P(E\mid T)}{P(E\mid N)}
\cdot
\frac{P(T)}{P(N)}
$$

The equation decomposes posterior odds into a likelihood ratio and prior odds. The likelihood ratio, often called the Bayes factor, measures the relative evidential support provided by $$E$$ under the specified probabilistic models:

$$
BF_{T,N}=\frac{P(E\mid T)}{P(E\mid N)}
$$

When the relevant likelihoods are well-defined, a Bayes factor greater than one indicates that the evidence favors theism over naturalism in the Bayesian likelihood-ratio sense. A value below one indicates the reverse. A value equal to one indicates that the evidence does not discriminate between the hypotheses under the specified models.

But the algebra does not tell us what values these likelihoods should take, or whether the proposed hypotheses determine them at all.

This is where the methodological burden begins. To claim that some observation favors theism, it is not sufficient to display Bayes' theorem or describe the observation as surprising under naturalism. The argument must establish why the observation is more probable under theism than under naturalism. That requires a defensible account of the likelihoods being compared.

The distinction is fundamental. A valid mathematical relationship among probabilities does not justify the probability assignments themselves. The relationship tells us what follows if the specified assignments are accepted. It does not establish that those assignments ought to be accepted.

### The distinction between Bayesian coherence and evidential justification

One possible response is to invoke a subjective interpretation of probability. On this view, probabilities represent degrees of belief rather than objective physical chances or observed relative frequencies. Their legitimacy therefore need not depend on the existence of a repeatable experiment or an identifiable stochastic mechanism. A person may assign a probability to a unique event, a historical proposition, or a metaphysical hypothesis without claiming that the proposition belongs to a population of independently sampled outcomes.

This is correct as far as it goes. Bayesian probability need not be interpreted as physical frequency, and subjective probabilistic reasoning is not illegitimate merely because its subject matter lacks a conventional data-generating process.

But this observation does not resolve the methodological problem. It changes the interpretation of the probability assignments without independently establishing their evidential justification.

Subjective Bayesian coherence requires probabilistic judgments to satisfy certain formal constraints. These constraints help prevent internally inconsistent combinations of beliefs. They do not, by themselves, establish that any particular coherent assignment is appropriate to the subject matter.

For a proposition $$H$$, a coherent agent may assign one prior probability while another coherent agent assigns a substantially different prior. Both assignments can satisfy the axioms of probability theory. Their mathematical coherence does not establish that either assignment is uniquely rational or evidentially supported.

The same point applies to conditional probabilities. An agent may coherently judge that a particular observation is highly likely under a metaphysical hypothesis. Another agent may assign a substantially lower likelihood while remaining equally consistent with the probability axioms. Unless additional constraints justify one judgment over the other, the formalism alone cannot resolve the disagreement.

This is not an objection to the logical permissibility of subjective credences. It is an objection to treating those credences as though their coherence establishes a substantive evidential relationship that others are rationally obligated to accept.

A distinction must therefore be maintained between the internal consistency of a person's probabilistic beliefs and the public justification of an argument purporting to demonstrate that some evidence supports a particular hypothesis.

The former concerns whether the assignments satisfy formal probabilistic constraints. The latter concerns whether there are adequate reasons to accept those assignments as appropriate to the evidential question.

Bayesian arguments for theism typically aspire to more than a description of an individual's coherent beliefs. They seek to demonstrate that observations concerning the universe, consciousness, or other phenomena provide genuine evidential support for the existence of God. Their conclusions are presented as reasons for revising one's understanding of reality, not merely as statements about what follows from one person's chosen credences.

That ambition creates an additional burden. The argument must provide reasons for accepting the relevant likelihoods and prior assumptions rather than merely demonstrating that they can be consistently entertained.

**Coherence is a constraint on probabilistic reasoning, not a substitute for the justification of its substantive assumptions.**

### The problem of unjustified prior specification

The specification of prior probabilities is one of the most conspicuous sources of uncertainty in Bayesian arguments concerning broad metaphysical hypotheses.

A prior probability represents the probability assigned to a hypothesis before conditioning on the particular evidence under consideration. In applied Bayesian statistics, prior distributions may be informed by previous research, background knowledge, physical constraints, empirical measurements, or explicitly defended modeling assumptions. In other circumstances, analysts may use weakly informative priors, reference priors, or other formal approaches intended to represent limited prior information or satisfy specific methodological objectives.

None of these strategies renders prior selection universally automatic. Priors remain part of the model specification, and the implications of alternative prior choices may require investigation.

In philosophical arguments for theism, the problem is substantially more difficult because the hypotheses under consideration are exceptionally broad. Theism and naturalism are not narrowly specified statistical models for which a common empirical basis straightforwardly determines prior probabilities. They are families of metaphysical positions encompassing numerous possible accounts of reality.

Nevertheless, arguments may proceed by assigning non-negligible prior probability to theism on the basis of alleged simplicity, explanatory scope, coherence, or what is sometimes described as intrinsic probability.

These considerations may have legitimate roles within particular theories of rational belief or explanation. But their invocation does not independently establish a probability measure over metaphysical hypotheses.

For example, simplicity is not a uniquely defined numerical property. Different measures of simplicity can privilege different representations, explanatory structures, or theoretical commitments. A hypothesis may be simple with respect to the number of fundamental entities it postulates while introducing substantial complexity in the specification of their properties, dispositions, or causal relationships. Another hypothesis may require more mathematical structure while offering greater constraints on observable outcomes.

Without an adequately specified criterion of simplicity and a defensible account of its relationship to prior probability, the assertion that one hypothesis deserves a favorable prior remains underdetermined.

Similarly, appealing to the intrinsic probability of a hypothesis does not settle how that probability is established. The term may receive a technical definition within a particular philosophical framework, but its introduction does not eliminate the need to justify the framework, the criteria governing the probability assignment, and the applicability of those criteria to the hypotheses being compared.

The methodological issue is not that philosophers are prohibited from introducing technical concepts. It is that the introduction of a concept does not constitute a justification of the values or inferential relationships subsequently attributed to it.

A prior assignment can be mathematically coherent, philosophically motivated, and still insufficiently justified to support the evidential conclusion being drawn.

The problem becomes especially significant when the posterior conclusion is sensitive to the prior odds.

From Bayes' theorem:

$$
\frac{P(T\mid E)}{P(N\mid E)}
=
BF_{T,N}
\cdot
\frac{P(T)}{P(N)}
$$

If the prior odds are weakly constrained, the posterior odds may remain correspondingly dependent on assumptions that the argument has not established.

This is the familiar problem of prior sensitivity. Its presence does not automatically invalidate a Bayesian analysis. In legitimate applications, sensitivity to prior choices can be examined, characterized, and communicated. The analyst may investigate whether the substantive conclusion remains stable across a defensible range of priors.

But when a philosophical argument relies on an insufficiently justified prior while presenting its posterior conclusion as substantively established, the prior dependence of that conclusion is an unresolved methodological problem.

Even here, however, the objection should not be restricted to the possibility that the prior has been chosen incorrectly.

The deeper concern is whether the argument has provided adequate grounds for treating its prior specification as epistemically authoritative at all.

### Unspecified likelihoods and the problem of comparative confirmation

Although prior specification receives considerable attention in philosophical discussions of Bayesian reasoning, the likelihood problem is arguably more fundamental to probabilistic arguments for theism.

A Bayes factor purports to characterize how strongly an observation discriminates between competing hypotheses. Unlike posterior odds, it does not directly depend on the prior odds assigned to those hypotheses. Nevertheless, it depends entirely on the likelihoods of the evidence under the models being compared.

For an observation $$E$$, the assertion that the evidence favors theism requires:

$$
P(E\mid T)>P(E\mid N)
$$

This inequality is not established by the observation that theism could explain $$E$$. Nor is it established by the claim that naturalism does not currently provide a satisfactory explanation for $$E$$.

To justify the inequality, one must establish why the evidence should be expected to a greater degree under theism than under naturalism.

The distinction between explanatory compatibility and probabilistic expectation is crucial.

A hypothesis may be compatible with an observation without making that observation particularly likely. Likewise, a hypothesis may be unable to provide a presently satisfactory explanation of an observation without thereby assigning that observation a low probability. Explanatory incompleteness is not itself a likelihood function.

Consider the claim that a benevolent God would have reason to create a universe containing conscious beings capable of flourishing. Even if this claim is granted as a possible explanation, it does not independently establish the probability of such a universe under theism.

Theism, considered in the abstract, does not uniquely specify divine preferences, the relative importance of possible divine purposes, the constraints governing divine action, or the range of worlds a deity might choose to create.

A theistic likelihood therefore requires additional assumptions about what a deity would desire, value, or actualize.

Similarly, naturalism does not uniquely specify the laws of physics, the determination of physical constants, or the relationship between consciousness and physical processes. An argument that treats the absence of a complete naturalistic explanation as evidence of a low naturalistic likelihood is conflating uncertainty about a hypothesis's implications with evidence that the relevant observation would be improbable under that hypothesis.

Ignorance concerning the determination of an outcome does not supply a numerical probability for that outcome.

This difficulty applies to both sides of the proposed comparison. Theism does not automatically entail a high likelihood for an observed phenomenon, and naturalism does not automatically entail a low likelihood merely because the phenomenon remains incompletely understood.

Without independently justified likelihoods, the Bayes factor has not been established.

To see the problem, suppose an argument assigns:

$$
P(E\mid T)=0.8
$$

and:

$$
P(E\mid N)=0.02
$$

The resulting Bayes factor is:

$$
BF_{T,N}=\frac{0.8}{0.02}=40
$$

The observation would then strongly favor theism relative to the stipulated likelihoods.

But the mathematical result tells us nothing about whether the assignments themselves are defensible. If those values were selected through intuition, speculative explanatory expectations, or arbitrary assumptions, the Bayes factor merely reproduces the consequences of those choices.

A different pair of assignments could produce a much smaller likelihood ratio, no discrimination between the hypotheses, or a result favoring naturalism.

The point is not that alternative values can always be substituted without consequence. In a sufficiently constrained model, relevant evidence and theoretical assumptions can rule out many assignments. The problem arises where those constraints have not been established.

In that case, the argument has not demonstrated that the evidence favors theism. It has demonstrated that the evidence favors theism conditional on a set of likelihood assignments whose evidential legitimacy remains unresolved.

This is a fundamental difference.

**A Bayesian calculation cannot establish comparative evidential support when the comparative likelihoods supplying that support have themselves been introduced without adequate justification.**

### Broad hypotheses, auxiliary assumptions, and the problem of model specification

The difficulty of specifying likelihoods becomes clearer when we recognize that theism and naturalism are not single, fully specified predictive models.

Each encompasses a broad family of possible accounts of reality. A naturalistic theory may include specific assumptions about fundamental physics, cosmological dynamics, consciousness, and the relationships governing physical processes. A theistic theory may include assumptions concerning divine intentions, preferences, creative actions, and the relationship between divine agency and the natural order.

These auxiliary assumptions can substantially alter the predicted likelihood of an observation.

Formally, suppose $$\theta$$ represents the additional assumptions necessary to specify a predictive model under theism. A marginal likelihood would then take a form such as:

$$
P(E\mid T)
=
\int_{\Theta_T}
P(E\mid T,\theta)\,
P(d\theta\mid T)
$$

A corresponding expression would be required under naturalism:

$$
P(E\mid N)
=
\int_{\Theta_N}
P(E\mid N,\phi)\,
P(d\phi\mid N)
$$

Here, $$\theta$$ and $$\phi$$ represent the relevant auxiliary parameters, model structures, or subsidiary hypotheses within the respective frameworks.

The significance of these expressions is not that philosophical arguments must always produce explicit multidimensional integrals. It is that a likelihood attributed to a broad hypothesis generally depends on how the different models compatible with that hypothesis are weighted.

The likelihood of evidence under theism is not automatically identical to its likelihood under one conveniently selected conception of divine intentions. Likewise, the likelihood under naturalism is not automatically identical to its likelihood under an arbitrarily selected naturalistic model.

To derive marginal likelihoods, the argument needs an account of how the relevant auxiliary possibilities are represented and weighted.

This introduces another level of prior specification, now occurring within each overarching hypothesis. Even if the prior odds between theism and naturalism were agreed upon, the resulting Bayes factor could remain highly sensitive to the distributions assigned to their respective auxiliary models.

Consequently, the likelihood comparison cannot be insulated from questions of prior justification simply by focusing on the Bayes factor rather than the posterior odds.

The calculation of a Bayes factor between composite hypotheses can itself depend heavily on prior assumptions over the models contained within those hypotheses.

This is particularly relevant when the underlying metaphysical categories are sufficiently broad to accommodate multiple, substantially different expectations about the same observation.

An argument cannot simply select a favorable auxiliary model under theism, an unfavorable auxiliary model under naturalism, and treat the resulting likelihood ratio as an established comparison between the overarching hypotheses.

Such a procedure would establish, at most, a conditional comparison between the specific subsidiary models selected.

The additional step from those subsidiary models to the broad metaphysical hypotheses requires independent justification.

### Ad hoc assumptions and explanatory flexibility

A related problem concerns the use of auxiliary assumptions that are introduced primarily to explain the observation under consideration.

In Bayesian reasoning, explanatory flexibility is not inherently illegitimate. Complex hypotheses can be evaluated probabilistically, and introducing additional parameters or subsidiary hypotheses is a normal part of statistical modeling.

The methodological difficulty arises when those additions are insufficiently constrained and their selection is driven by the very evidence they are subsequently claimed to explain.

For example, suppose an argument begins with the broad hypothesis that a divine creator exists. The observed universe contains conscious beings, and the argument proposes that a divine creator would desire such beings. The resulting assumption is then used to argue that the observation is highly probable under theism.

But why should that particular divine preference be assigned substantial probability conditional on theism?

The mere fact that the assumed preference would explain the observation does not establish that the preference was probable independently of the observation.

A creator might be imagined as preferring embodied conscious life, disembodied minds, entirely different forms of existence, or purposes unrelated to the emergence of conscious beings. Theism considered by itself does not obviously establish how probability should be distributed across these proposed preferences.

The problem is not solved by asserting that one divine intention is intuitively reasonable. Reasonableness or conceptual compatibility does not independently determine its conditional probability.

A properly specified Bayesian model can account for alternative auxiliary hypotheses by assigning them probabilities and marginalizing over them. It can also accommodate genuine learning about model parameters. But the justification of those assignments and the treatment of model flexibility remain essential.

When a favorable auxiliary assumption is selected after considering the evidence and then treated as though it had been independently established, the apparent predictive success of the hypothesis may be overstated.

This is one reason why distinguishing explanation after observing an outcome from independently warranted expectations about that outcome is methodologically important.

A hypothesis capable of accommodating many possible observations is not necessarily worthless. But its ability to explain an observation does not, by itself, establish that it assigned that observation a high probability before the explanatory assumptions were selected.

The relevant question is not simply whether a theistic account can be constructed that makes the observation intelligible. It is whether there are adequate reasons, independent of that construction's explanatory convenience, to assign the observation a greater likelihood under theism than under the competing hypothesis.

Without such reasons, the likelihood advantage remains asserted rather than demonstrated.

### The problem of evidential asymmetry

The inadequacy of these likelihood comparisons is especially visible when different standards of justification are applied to the competing hypotheses.

Naturalism may be treated as explanatorily deficient because it does not currently determine why physical constants have their observed values or why conscious experiences possess particular relationships to physical processes. This explanatory limitation is then converted into a judgment of low likelihood.

Theism, by contrast, may receive a favorable likelihood because some divine intention could make the observation intelligible.

The two sides are not being evaluated according to the same inferential standard.

In one case, an absence of explanatory determination is treated as evidence of improbability. In the other, the availability of a compatible explanatory narrative is treated as evidence of probability.

Neither transition is automatic.

A lack of knowledge about the mechanism determining an observation does not establish that the observation is improbable. And the ability to formulate an intention that would make an observation unsurprising does not establish that the intention should have been expected.

The comparison becomes methodologically unstable when ignorance on one side is penalized while unconstrained explanatory flexibility on the other is rewarded.

This is not an argument that naturalism must receive a favorable likelihood, or that theism necessarily receives a low likelihood. It is an objection to drawing a comparative conclusion from asymmetrically applied assumptions.

The relevant methodological standard must be applied to both hypotheses: what do the hypotheses, together with independently defensible auxiliary assumptions, actually warrant us in expecting?

If that question cannot be answered, then the claimed likelihood ordering has not been established.

### Qualitative likelihoods do not escape the problem

A defender of Bayesian arguments for theism might respond that precise numerical probabilities are unnecessary. The argument may require only the qualitative conclusion that the observation is more probable under theism than under naturalism.

On this view, the precise magnitude of the Bayes factor is secondary. What matters is the direction of the evidential relationship.

This response correctly identifies an important feature of Bayesian confirmation. Evidence can favor one hypothesis over another even when the likelihood ratio is not estimated numerically. In some circumstances, theoretical relationships may justify a qualitative inequality without determining exact probabilities.

But the absence of numerical precision does not eliminate the need to justify the inequality.

The claim:

$$
P(E\mid T)>P(E\mid N)
$$

is still a substantive probabilistic claim.

It asserts an ordering between two conditional probabilities. Establishing that ordering requires reasons to believe that the relevant observation is more likely under one hypothesis than under the other.

If the hypotheses do not determine sufficiently constrained expectations, or if the ordering changes under alternative defensible auxiliary assumptions, then the qualitative conclusion may be no better established than a speculative numerical estimate.

This matters because a qualitative formulation can conceal the same methodological deficiencies that would be more visible in an explicit calculation.

A philosopher may avoid assigning numerical likelihoods while continuing to assert that some phenomenon is much more expected under theism. But unless there is a defensible basis for this comparative expectation, the argument has not escaped the problem of likelihood specification.

The requirement is not numerical precision for its own sake. It is justification for the inferential relationship being asserted.

### Prior sensitivity, likelihood sensitivity, and robustness

In applied Bayesian analysis, the consequences of uncertain assumptions can be investigated through sensitivity analysis. Rather than treating a single model specification as authoritative, an analyst may examine how conclusions change when priors, likelihood functions, structural assumptions, or other components of the model are varied within defensible ranges.

The importance of this practice is straightforward. If a substantive conclusion remains stable across relevant alternative specifications, the conclusion may possess a form of robustness that strengthens confidence in its inferential significance. If the conclusion changes dramatically under modest adjustments to poorly constrained assumptions, the analysis must communicate that dependence.

The same concern arises in probabilistic arguments for theism.

Suppose that alternative assumptions about divine preferences yield different values of $$P(E\mid T)$$, while alternative naturalistic models yield different values of $$P(E\mid N)$$. If those assumptions are not sufficiently constrained, the Bayes factor may vary across a wide range of possible values.

To express this formally, let $$\mathcal{M}_T$$ and $$\mathcal{M}_N$$ denote families of admissible model specifications under theism and naturalism. The possible likelihood ratios could be represented by:

$$
\mathcal{B}
=
\left\{
\frac{P(E\mid M_T)}{P(E\mid M_N)}
:
M_T\in\mathcal{M}_T,\,
M_N\in\mathcal{M}_N
\right\}
$$

This set represents the range of likelihood ratios generated by the model specifications under consideration. It is not itself a probability distribution over those specifications.

If the admissible model families are sufficiently broad that the resulting likelihood ratios include values above and below one, the specified family alone does not establish a stable direction of evidential support.

The argument would then need additional grounds for privileging some models, restricting the admissible family, or assigning weights across its members.

Merely selecting the model specifications that produce a favorable comparison would not establish that those specifications are justified.

This does not mean that every philosophical argument must conduct a numerical sensitivity analysis. The point is methodological: when the conclusion depends on uncertain assumptions, the argument must explain why those assumptions are defensible and whether the claimed result survives relevant alternatives.

In engineering and statistical modeling, this distinction is essential because apparent certainty can be generated by a narrow specification of assumptions rather than by the strength of the available evidence.

A similar danger exists in speculative Bayesian reasoning. The introduction of a precise probability assignment may create the impression that uncertainty has been resolved when it has merely been relocated into unexamined modeling choices.

The resulting posterior may be precise conditional on the model while the model itself remains profoundly underdetermined.

### What Bayesian reasoning can and cannot establish

The criticism developed here does not challenge Bayes' theorem or deny that probabilities can represent subjective uncertainty. Nor does it assert that probabilistic reasoning is categorically inapplicable to metaphysical hypotheses.

Instead, it distinguishes three different achievements that are too often conflated.

The first is the construction of a mathematically coherent probabilistic model.

The second is the derivation of a conditional result within that model.

The third is the justification of using that result to support a substantive conclusion about reality.

The first two do not automatically establish the third.

A philosopher may construct a coherent Bayesian model in which fine-tuning or psychophysical harmony favors theism. Within that model, the relevant likelihood ratio may indeed be greater than one. The posterior odds may then follow correctly from the selected prior odds.

But none of this independently demonstrates that the model's probability assignments are warranted.

If the relevant likelihoods depend on speculative distributions over physical constants, unsupported assumptions about psychophysical alternatives, or unconstrained judgments about divine intentions, the formal inference merely transmits those assumptions into the conclusion.

The validity of the calculation does not establish the epistemic authority of its inputs.

This distinction also clarifies the burden faced by critics of these arguments. One need not demonstrate that naturalism is more probable than theism. Nor must one provide an alternative set of priors or likelihoods. The criticism can be directed at the failure to justify the evidential comparison offered.

If an argument claims that an observation favors theism, it bears the burden of establishing the relevant likelihood ordering. Where its assumptions do not adequately support that ordering, the advertised evidential conclusion has not been demonstrated.

It would be a mistake to infer from this failure that the evidence must be neutral, that the hypotheses are equally probable, or that the observation cannot possibly favor theism under some defensible future model. Those conclusions do not follow.

The appropriate conclusion is narrower and more methodologically disciplined: the proposed argument has not established the probabilistic relationship required for its claim.

This is precisely the distinction between uncertainty within a justified model and the failure to justify a model's applicability.

The former can often be represented and investigated using Bayesian methods. The latter cannot be resolved merely by applying those methods to assumptions whose legitimacy remains in question.

Bayesian formalism is therefore not a solution to the foundational difficulties identified in the preceding sections. It is a framework whose evidential usefulness depends on whether those difficulties have been adequately addressed.

**An unsupported likelihood does not become evidence because it appears in a Bayes factor. An arbitrary prior does not become epistemically authoritative because it satisfies the probability axioms. And a posterior conclusion does not acquire substantive legitimacy merely because it follows from mathematically coherent assumptions.**

The central problem is not that Bayesian arguments for theism necessarily produce incorrect numerical conclusions. It is that they often fail to establish the probabilistic inputs required to warrant any particular evidential conclusion.

Where the hypotheses are insufficiently specified, the auxiliary assumptions are unconstrained, the priors lack adequate justification, and the likelihoods are asserted rather than derived, the resulting comparison has not demonstrated that the evidence favors theism.

The probability calculus may be perfectly valid. The evidential claim remains unestablished.

The next section extends this criticism beyond individual prior and likelihood assignments to the broader problem of model uncertainty and underdetermination. In particular, it examines why uncertainty about the appropriate probabilistic representation cannot simply be treated as ordinary uncertainty within a settled model, and why the distinction is essential when evaluating philosophical arguments that purport to draw conclusions from deeply speculative descriptions of reality.

## 6. Model Uncertainty, Underdetermination, and the Failure to Establish an Inference

The preceding sections have examined the difficulties involved in constructing probability spaces, specifying prior distributions, and establishing likelihoods for broad metaphysical hypotheses. These difficulties point toward a more general methodological problem: probabilistic arguments for theism frequently proceed as though the relevant models have already been adequately specified and the remaining task is simply to reason about uncertainty within them. Yet the most consequential uncertainties often concern the models themselves. The relevant alternatives may be incompletely understood, their relationships may be misrepresented, and the assumptions required to connect abstract hypotheses to observable phenomena may be insufficiently constrained.

This distinction between uncertainty within a model and uncertainty about the model is fundamental to applied probabilistic reasoning. It is also essential to understanding why the deficiencies identified in Bayesian arguments for theism cannot be resolved simply by acknowledging that the relevant probabilities are uncertain or imprecise.

The issue is not merely that we lack sufficiently accurate estimates of otherwise well-defined quantities. It is that the justification for treating those quantities as meaningful representations of the evidential relationship under investigation may itself be absent.

### Parameter uncertainty and structural model uncertainty

In statistical modeling, uncertainty can arise at several different levels. A model may contain unknown parameters whose values must be estimated from observations or background information. Even when its mathematical structure is fixed, uncertainty about those parameters can substantially affect its predictions.

Consider a simplified reliability model in which component failures are represented through an exponential survival distribution. If the failure rate is denoted by $$\lambda$$, the probability that a component fails within a time interval of length $$t$$ is:

$$
P(T_f\leq t\mid\lambda)
=
1-e^{-\lambda t}
$$

Here, the mathematical structure of the model is taken as given, while the failure rate remains uncertain. An analyst might estimate the parameter from historical observations, engineering information, or a combination of available evidence and prior assumptions.

If uncertainty concerns only the value of $$\lambda$$, a Bayesian analysis can represent it through a posterior distribution and propagate that uncertainty into the predicted probability of failure.

But suppose the component's failure behavior is not adequately represented by an exponential distribution. Its hazard rate may change with age, operating conditions, accumulated damage, or maintenance interventions. Alternatively, component failure may depend on common-cause events, organizational decisions, or interactions with other components that are not represented by the model.

In such circumstances, uncertainty is no longer confined to the value of a parameter. It concerns whether the model's structure adequately represents the process being investigated.

A highly precise posterior estimate of $$\lambda$$ would not resolve this problem. The posterior could be sharply concentrated while the underlying model remained misspecified.

The distinction can be expressed in general terms. Let $$M$$ denote a specified model, $$\theta$$ its parameters, and $$D$$ the available data. A conventional Bayesian parameter inference concerns:

$$
P(\theta\mid D,M)
$$

This distribution describes uncertainty about the parameters conditional on the assumed model.

It does not independently establish that $$M$$ is the appropriate representation of the system.

Uncertainty concerning the model itself raises a different question:

$$
P(M\mid D)
$$

But even this expression presupposes a framework within which alternative models can be specified, assigned probabilities, and evaluated against the evidence.

The important point is that uncertainty about the correct parameters and uncertainty about the appropriate model are not interchangeable. A probabilistic assessment can represent the former while neglecting the latter entirely.

In applied analysis, this distinction motivates model checking, comparison of alternative specifications, investigation of structural uncertainty, and examination of whether the intended application falls within the model's domain of validity.

The problem becomes especially serious when the models under consideration are not merely imperfect approximations of a well-studied system, but speculative representations of phenomena whose fundamental structure remains unresolved.

This is precisely the situation encountered in many Bayesian arguments for theism.

### Broad metaphysical hypotheses do not uniquely determine predictive models

Theism and naturalism are commonly treated as opposing hypotheses in probabilistic arguments. Yet neither, considered at the level of generality normally employed in these discussions, constitutes a fully specified predictive model.

Naturalism encompasses a wide range of possible accounts of fundamental physics, cosmology, consciousness, and the relationships among physical phenomena. Different naturalistic theories may imply substantially different expectations concerning the same observation.

Similarly, theism encompasses numerous possible accounts of divine intentions, divine action, creation, and the relationship between a deity and the natural order. Even when the argument specifies classical theism or a deity possessing particular attributes, substantial uncertainty may remain concerning what such a being would create or which possible outcomes it would prefer.

These are not minor differences between parameter values within otherwise fixed models. They can involve distinct causal structures, explanatory assumptions, metaphysical commitments, and predictions.

The problem arises when a philosophical argument moves directly from a broad ontological hypothesis to a conditional probability without adequately specifying the intermediary model.

For example, the claim that life-permitting physical constants are improbable under naturalism is not an immediate consequence of naturalism itself. It depends on further assumptions concerning the determination of physical constants, the relationships among them, and the relevant distribution over alternative values.

Likewise, the claim that life-permitting constants are probable under theism depends on assumptions concerning divine preferences, the purposes of creation, and the likelihood that a deity possessing those preferences would actualize a universe with the observed properties.

If these auxiliary assumptions are not independently constrained, the broad metaphysical hypotheses do not determine the likelihoods attributed to them.

This means that the apparent Bayesian comparison may conceal an unacknowledged process of model selection. The argument effectively chooses particular interpretations or subsidiary models within each metaphysical framework and treats their implications as though they were implications of the frameworks themselves.

But a comparison between selectively specified subsidiary models is not automatically a justified comparison between the overarching hypotheses.

The distinction matters because the result may depend entirely on which subsidiary models are selected.

An argument that compares a theistic model in which God strongly prefers conscious life against a naturalistic model in which life-permitting conditions are assigned very low probability may produce a favorable likelihood ratio for theism. Yet the same broad ontological categories could accommodate other subsidiary models yielding radically different likelihoods.

Unless the selection or weighting of those models is justified, the inference does not establish a likelihood ordering between the broader hypotheses.

### Underdetermination and the absence of discriminating predictions

The problem can also be understood through the concept of underdetermination.

In scientific methodology, a model is underdetermined by available evidence when multiple competing explanations or model structures remain compatible with the observations. In statistical settings, related issues arise when available data do not adequately identify model parameters or discriminate between competing probability distributions.

These concepts are not identical. Statistical identifiability has a specific formal meaning, while philosophical underdetermination may concern broader explanatory or theoretical relationships. Nevertheless, both draw attention to a common methodological difficulty: an observation may be compatible with multiple accounts without providing sufficient information to distinguish among them.

Bayesian confirmation requires more than compatibility.

Suppose some observation $$E$$ is compatible with both theism and naturalism. To establish that it comparatively favors theism, the argument must justify:

$$
P(E\mid T)>P(E\mid N)
$$

If the available theoretical information fails to constrain either likelihood sufficiently, the mere existence of the observation does not resolve the comparison.

One might object that probability theory permits conditional probabilities to be assigned even where the underlying theories are incomplete. That is true as a matter of mathematical representation. But mathematical permissibility is not the issue.

The question is whether the information supplied by the hypotheses and background assumptions warrants the particular likelihood ordering.

If a broad hypothesis is compatible with many subsidiary models that imply substantially different likelihoods, then selecting a single likelihood requires an additional modeling decision.

If the evidence does not constrain that decision, the claimed likelihood may reflect the modeler's assumptions more than the evidential implications of the hypothesis.

This is not merely a problem of assigning too much numerical precision to an otherwise justified assessment. It is a problem of whether the available information warrants the direction of the comparison at all.

An observation can be genuinely puzzling, theoretically important, and compatible with multiple explanations without thereby establishing a probabilistic preference among them.

The failure to distinguish among hypotheses is not equivalent to evidence that they are equally probable. It means that the proposed inferential procedure has not established how the observation discriminates between them.

### Why Bayesian model averaging does not automatically resolve the problem

Bayesian methodology contains formal tools for representing model uncertainty. Rather than selecting a single model, an analyst may assign probabilities to a collection of candidate models and average their predictions.

Suppose a hypothesis $$H$$ contains a collection of possible subsidiary models:

$$
\mathcal{M}_H=\{M_1,M_2,\ldots,M_k\}
$$

The likelihood of evidence under the broader hypothesis can be represented as:

$$
P(E\mid H)
=
\sum_{i=1}^{k}
P(E\mid H,M_i)
P(M_i\mid H)
$$

This expression accounts for uncertainty over subsidiary models by weighting their likelihoods according to probabilities assigned conditional on the overarching hypothesis.

The procedure is mathematically legitimate and can be useful when the candidate models and their weights have defensible foundations.

But it does not independently solve the problem of model justification.

The analyst must still determine which models belong in the candidate set, whether relevant alternatives have been omitted, what probability weights should be assigned to them, and whether their likelihood functions adequately represent the observation.

Model averaging propagates the uncertainty represented within the specified framework. It does not establish that the framework exhausts the relevant possibilities or that its weighting assumptions are epistemically appropriate.

This becomes particularly important when the candidate models themselves are speculative and the probabilities assigned to them are largely unconstrained.

Consider an illustrative case in which two subsidiary models are entertained under theism. One assigns high probability to an observation, while the other assigns low probability. Suppose the same is true of two subsidiary models under naturalism.

For simplicity, let the likelihoods within each overarching hypothesis take the values $$0.9$$ and $$0.1$$. Let $$w_T$$ denote the conditional weight assigned to the high-likelihood theistic model, and $$w_N$$ the corresponding weight assigned to the high-likelihood naturalistic model.

The marginal likelihoods become:

$$
P(E\mid T)
=
0.9w_T+0.1(1-w_T)
$$

$$
P(E\mid N)
=
0.9w_N+0.1(1-w_N)
$$

Equivalently:

$$
P(E\mid T)=0.1+0.8w_T
$$

$$
P(E\mid N)=0.1+0.8w_N
$$

The resulting Bayes factor is:

$$
BF_{T,N}
=
\frac{0.1+0.8w_T}{0.1+0.8w_N}
$$

The likelihood comparison favors theism when $$w_T>w_N$$, favors naturalism when $$w_T<w_N$$, and is neutral when the weights are equal.

The example is deliberately schematic. It is not an empirical model of either metaphysical hypothesis. Its purpose is to isolate the methodological problem: when the weights assigned to subsidiary models are not independently constrained, the direction of the likelihood comparison may depend entirely on those weights.

Bayesian model averaging does not remove that dependence. It expresses it mathematically.

A defender of the argument would therefore need to explain why the proposed weights are justified, or why the conclusion remains stable across an appropriately defended range of alternatives.

The existence of a formal procedure for integrating over model uncertainty does not demonstrate that the necessary probabilities can be responsibly specified.

This is an important general lesson. Sophisticated mathematical methods can propagate uncertainty that has already been represented, but they cannot guarantee that all relevant forms of uncertainty have been identified or that the model choices used to represent them are appropriate.

### Model misspecification and false precision

A related difficulty is the possibility of model misspecification.

In applied statistics, a model can be misspecified when its mathematical assumptions fail to adequately represent the process generating the observations. The problem is not necessarily that the calculations are performed incorrectly. It is that the model does not sufficiently correspond to the phenomenon it is intended to describe.

A posterior distribution may become highly concentrated under a misspecified model. Numerical precision can therefore coexist with serious structural inadequacy.

For a sufficiently constrained statistical model, additional observations may reduce uncertainty about its parameters without resolving the discrepancy between the model and the actual data-generating process.

The resulting precision is conditional on assumptions that may be false or inappropriate.

The same distinction applies to philosophical Bayesian arguments.

Suppose a probability distribution is assigned over hypothetical physical constants, or over proposed relationships between conscious experiences and physical states. The argument then performs a mathematically valid calculation and concludes that the observed configuration is extremely improbable.

Even if the numerical result is precise, its evidential significance depends on whether the selected model provides an appropriate representation of the relevant alternatives and their probabilities.

If those assumptions are not justified, greater numerical precision does not improve the epistemic standing of the inference.

Indeed, precision can obscure the underlying uncertainty by directing attention toward the calculated result rather than the assumptions required to produce it.

A claim that some observation has a probability of one in a billion can sound substantially more informative than a claim that its probability is unknown. But if the numerical estimate depends on an arbitrary sample space or unjustified measure, the appearance of informativeness may be illusory.

The fundamental question is not how many decimal places the model produces. It is whether the model warrants the interpretation assigned to those numbers.

This is especially relevant to arguments in which extreme improbability is rhetorically central. The force of such arguments may depend on the impression that the improbability has been mathematically established, when it is actually conditional on a series of unvalidated modeling choices.

### Robustness and the stability of evidential conclusions

One way to investigate the consequences of model uncertainty is to examine whether a conclusion remains stable across alternative defensible specifications.

In applied modeling, robustness analysis can reveal whether an assessment depends heavily on particular modeling choices or whether its substantive implications survive variations in assumptions.

The idea can be extended to Bayesian comparisons.

Let $$\mathcal{C}$$ denote a specified collection of admissible probabilistic model pairs. Each pair contains a theistic model and a naturalistic model, together with the assumptions required to evaluate the likelihood of the evidence.

For a model pair $$c\in\mathcal{C}$$, define:

$$
BF(c)
=
\frac{P(E\mid T,c)}{P(E\mid N,c)}
$$

Assume the denominator is positive for the comparisons considered.

If the argument seeks to establish that the evidence favors theism across the entire admissible class, it would require:

$$
\inf_{c\in\mathcal{C}}BF(c)>1
$$

This is a strong robustness criterion, not a universal requirement for every legitimate Bayesian inference. Its significance is that it makes explicit what would be needed to establish a likelihood advantage uniformly across the specified model class.

A weaker argument might instead identify particular assumptions under which the likelihood ratio exceeds one and justify why those assumptions should be preferred.

But if the model class contains defensible specifications yielding likelihood ratios on both sides of one, then the mere specification of that class does not establish a robust direction of evidential support.

The argument would need further reasons to privilege some models over others.

This distinction matters because the existence of a favorable Bayesian model is not equivalent to the establishment of a favorable Bayesian comparison.

If one can construct a model in which theism predicts the observation with high probability, that demonstrates what follows under that model. It does not establish that the model is the appropriate basis for evaluating theism.

Likewise, constructing a naturalistic model that assigns the observation a low probability does not establish that naturalism itself makes the observation improbable.

The comparison requires justified restrictions on the model families or justified weights over their members.

Without such constraints, the claimed evidential relationship may be highly sensitive to assumptions that have no independent basis.

Robustness analysis also depends on the legitimacy of the alternatives included in the analysis. It is not enough to construct an arbitrarily broad collection of models and demand that a conclusion survive every imaginable specification. The model class must itself be justified.

But that qualification reinforces the central point: specifying the relevant alternatives and defending their treatment are substantive methodological tasks.

They cannot be bypassed merely by presenting a favorable result from one selected model.

### The difference between uncertainty and an unestablished probability

At this stage, it is necessary to distinguish two epistemic situations that are frequently conflated.

In the first, a probability model has been specified and adequately justified for a particular purpose, but the available information leaves substantial uncertainty about its parameters or predictions.

The analyst may possess a defensible probability interval, posterior distribution, or range of estimates. The uncertainty is represented within a framework whose relevance has been established to an appropriate degree.

In the second situation, the model's probability assignments, structural assumptions, or applicability have not been adequately justified. The analyst does not merely lack precision concerning a quantity within the model. The analyst lacks sufficient grounds for treating the chosen model as an appropriate basis for the asserted inference.

These are different problems.

An imprecise estimate within a defensible model may still contain meaningful information. For example, a reliability assessment might establish that a failure probability lies within a range under stated and supported assumptions.

By contrast, an arbitrarily selected probability distribution over hypothetical alternatives does not become an informative estimate merely because its uncertainty is described qualitatively or because a wide interval is attached to its results.

In the latter case, the problem concerns the legitimacy of the representation itself.

This distinction is particularly important when philosophers respond to criticism by emphasizing that their probability judgments are approximate, subjective, or intended only to establish a qualitative comparison.

Such qualifications can be appropriate when a valid inferential framework supports a conclusion but does not determine its precise magnitude.

They do not resolve the absence of justification for that framework.

If the available information does not support a particular likelihood ordering, describing the ordering as approximate does not establish it.

If the relevant alternatives have not been adequately specified, assigning imprecise probabilities to them does not independently validate the sample space.

And if broad metaphysical hypotheses do not constrain their subsidiary models sufficiently to generate a comparative prediction, acknowledging uncertainty does not automatically produce evidential discrimination.

The appropriate conclusion may simply be that the proposed probability comparison has not been established.

This is not equivalent to assigning equal probability to the competing hypotheses. Nor does it imply that no possible model could eventually support a discriminating likelihood.

It means that the argument presently offered does not provide sufficient grounds for the evidential conclusion it claims.

### The limits of probabilistic formalization under deep uncertainty

These considerations raise a broader question about the relationship between probability theory and severe epistemic uncertainty.

Probability theory is a general mathematical framework for representing uncertainty, but its applicability to a particular inferential problem is not established merely because a probability function can be defined.

Where the underlying phenomenon is poorly understood, the relevant alternatives are speculative, and the models connecting hypotheses to evidence are weakly constrained, it may be difficult to establish a unique or sufficiently informative probability assessment.

There are formal approaches to uncertainty that permit multiple probability measures, interval-valued assessments, or sets of admissible probabilistic models. Such approaches can make uncertainty about probability assignments explicit rather than disguising it within a single selected distribution.

For example, if $$\mathcal{P}$$ represents a justified class of probability measures, an event may be assigned lower and upper probabilities:

$$
\underline{P}(E)
=
\inf_{P\in\mathcal{P}}P(E)
$$

$$
\overline{P}(E)
=
\sup_{P\in\mathcal{P}}P(E)
$$

These quantities characterize the range of event probabilities permitted by the chosen class.

When the class is sufficiently constrained, such bounds may provide useful information. When the admissible measures remain extremely broad, the bounds may be correspondingly uninformative.

This is not a defect of the formalism. It can accurately reflect the limits of what the assumptions establish.

In some circumstances, a class of models may be too weakly constrained to determine whether the evidence favors one hypothesis or another. The formal analysis may then yield no stable likelihood ordering.

That outcome is methodologically preferable to selecting an arbitrary measure merely to manufacture a determinate result.

The important point is that uncertainty should not be suppressed simply because a philosophical argument requires a particular conclusion.

If the available assumptions fail to establish a comparative probability, the absence of a justified comparison is itself an epistemic result.

Not every question about reality is presently answerable through a sufficiently constrained probabilistic model. The generality of probability theory does not guarantee the availability of informative probability assignments for every conceivable hypothesis.

The ability to construct a formal representation of uncertainty must not be confused with having sufficient information to justify the representation.

### The application problem in probabilistic theistic arguments

The methodological difficulties developed throughout Part II converge on a single question: what justifies the application of the selected probabilistic model to the metaphysical hypotheses and observations being compared?

In the fine-tuning argument, the relevant model may involve distributions over hypothetical physical constants, assumptions about their independent variability, and claims concerning the likelihood of life-permitting conditions under different ontological frameworks.

In the psychophysical harmony argument, the model may involve hypothetical mappings between phenomenal and physical states, assumptions about their possible recombination, and comparative judgments about the expectations of theism and naturalism.

In both cases, the claimed Bayesian inference depends on more than the formal relationship among conditional probabilities.

It depends on the legitimacy of the space of alternatives, the adequacy of the model, the justification of its probability measures, and the appropriateness of the auxiliary assumptions connecting broad metaphysical hypotheses to the observations.

If those elements are not established, the argument has not earned the right to treat its calculated or asserted likelihoods as evidentially authoritative.

A philosopher might respond by insisting that every model requires assumptions and that no probabilistic assessment is free from uncertainty.

That observation is correct but insufficient.

The existence of assumptions in all models does not render all model specifications equally defensible. Nor does the unavoidable presence of uncertainty eliminate the distinction between justified and unjustified inference.

Applied disciplines operate under uncertainty constantly. Their methodological standards exist precisely because uncertainty does not disappear when a mathematical representation is introduced.

A model can be useful despite its limitations when its assumptions are sufficiently understood, its domain of applicability is appropriately characterized, and its conclusions are proportionate to the evidence supporting them.

By contrast, a model whose decisive assumptions are speculative, arbitrary, or unconstrained cannot claim the same epistemic authority merely because it is mathematically coherent.

The burden is not to eliminate uncertainty. It is to justify the inference despite uncertainty and to recognize when the available information does not warrant the conclusion.

### The failure to establish an inference

The central criticism can now be stated with greater precision.

A Bayesian argument for theism purports to establish that some observation provides comparative evidential support for theism over naturalism.

To support that conclusion, it must justify the probabilistic relationship between the evidence and the competing hypotheses.

That relationship depends on models connecting the hypotheses to the observation, together with the assumptions required to specify likelihoods and marginalize over relevant uncertainty.

If the models are inadequately specified, their auxiliary assumptions are unconstrained, or their likelihood orderings are unstable across defensible alternatives, the argument has not established the evidential relationship it purports to demonstrate.

The failure occurs before any posterior conclusion can acquire substantive epistemic significance.

It is therefore inadequate to respond that Bayes' theorem has been applied correctly. Correct application establishes only the mathematical consequences of the selected probability assignments.

It is equally inadequate to respond that the assignments are subjectively coherent. Coherence does not independently justify their relevance to the phenomenon.

Nor does it suffice to acknowledge that the assigned probabilities are approximate. Approximation presupposes some defensible target of estimation or judgment; it does not supply the missing grounds for the comparison.

The criticism is not that naturalism should receive the more favorable probability. It is not that theism must receive a negligible prior, or that every imaginable Bayesian formulation of a theistic argument is logically impossible.

It is that the arguments under examination have not adequately justified the probabilistic comparisons on which their claimed evidential force depends.

And importantly, a critic is under no obligation to replace an unsupported likelihood ratio with a competing one.

If an argument claims that an observation favors theism, the burden is to establish that claim. Demonstrating that its model fails to justify the asserted likelihood ordering is sufficient to show that the proposed argument has not accomplished its stated evidential task.

This is a foundational methodological objection, not a disagreement about the preferred numerical result.

**The existence of a coherent model does not establish its adequacy. The existence of a posterior distribution does not resolve structural uncertainty. And the possibility of constructing a favorable likelihood ratio does not establish that the evidence actually favors the hypothesis.**

Where competing probabilistic representations remain insufficiently constrained, the appropriate conclusion is not to assign whatever probabilities are needed to complete the argument. It is to recognize that the claimed evidential relationship has not been established.

This brings us to the central thesis of the essay.

The problem with the relevant Bayesian arguments for theism is not simply that they involve uncertainty, employ subjective probabilities, or lack the empirical resources available to conventional statistical modeling. Those features, by themselves, do not establish methodological failure.

The problem is that they seek to draw substantive conclusions about reality from probabilistic comparisons whose representational foundations, auxiliary assumptions, and inferential applicability have not been adequately justified.

The resulting formalism may be internally consistent. The philosophical narrative may be intelligible. The observations under discussion may raise genuine explanatory questions.

But none of these facts establishes the claimed likelihood ordering.

**The probability was not merely estimated imprecisely. The argument has not established the grounds on which that probability, or its asserted comparison with an alternative, should be accepted as evidence.**

The next part examines these failures in two prominent applications: the fine-tuning argument and the argument from psychophysical harmony. These cases will demonstrate how the methodological difficulties identified in Part II arise within concrete philosophical arguments, and why their purported evidential conclusions depend on assumptions that have not been independently established.

# Part III — Two Case Studies

## 7. Fine-Tuning: From Narrow Parameter Ranges to Cosmic Improbability

The fine-tuning argument provides a particularly instructive example of the methodological difficulties developed in the preceding sections. It begins with observations concerning the sensitivity of physical systems to certain parameters of fundamental physics and proceeds toward a probabilistic claim about the existence of a life-permitting universe. That claim is subsequently employed in a comparative inference intended to establish that the observed conditions provide evidence favoring theism over naturalism.

The central difficulty lies in the transition between these stages. A physical theory may establish that certain conditions are necessary for the development of complex structures or familiar forms of life. It may also establish that changes to particular parameters, while other theoretical assumptions are held fixed, would substantially alter the behavior of the modeled universe. These can be legitimate results of theoretical physics. But they do not independently establish that the actual parameters were improbable, that they could have varied according to some particular distribution, or that their observed values are more probable under theism than under naturalism.

The philosophical argument requires these additional conclusions, yet the methodological foundations necessary to support them are often insufficiently established.

This distinction is critical because the credibility of the fine-tuning argument frequently depends on its association with quantitative physical reasoning. Discussions of the cosmological constant, the strengths of fundamental interactions, particle masses, and early-universe conditions can involve sophisticated mathematical modeling. The resulting sensitivity analyses may be technically demanding and scientifically informative. But mathematical sophistication in the physical analysis does not automatically transfer to the probabilistic interpretation imposed upon it.

A physical calculation concerning how a modeled universe would behave under altered parameters is not the same thing as an estimate of the probability that those parameters would take particular values.

The former may be supported by established equations and theoretical constraints. The latter requires an additional probability model, along with a justification for treating that model as relevant to the determination of the observed universe.

Failing to distinguish these tasks allows the authority of the physical calculation to obscure the speculative assumptions introduced during the subsequent philosophical inference.

### Reconstructing the probabilistic argument

The contemporary fine-tuning argument is frequently presented as a likelihood comparison. The relevant evidence is that the fundamental features of our universe permit the existence of life, while the competing hypotheses are theism and some specified non-theistic alternative.

Robin Collins, for example, argues that fine-tuning provides strong evidence for theism over an atheistic single-universe hypothesis because life-permitting conditions are comparatively unsurprising under theism but highly improbable under the alternative. His argument invokes a principle of confirmation according to which an observation favors the hypothesis under which it is more probable.

The important point is that the conclusion does not necessarily claim that theism has a high posterior probability after all available evidence is considered. It claims that fine-tuning provides comparative confirmation of theism.

That distinction should be preserved. The present criticism does not depend on attributing a stronger conclusion to the argument than its proponents intend. It challenges whether the comparative confirmation itself has been established.

Let $$L$$ represent the proposition that the universe possesses conditions compatible with life, $$T$$ represent theism, and $$N$$ represent the relevant naturalistic hypothesis.

The argument requires the likelihood inequality:

$$
P(L\mid T)>P(L\mid N)
$$

The corresponding Bayes factor is:

$$
BF_{T,N}
=
\frac{P(L\mid T)}{P(L\mid N)}
$$

If the ratio is greater than one, fine-tuning favors theism relative to the specified probabilistic models. If it is substantially greater than one, the observation may provide correspondingly stronger comparative confirmation.

But the formal validity of this relationship is not controversial. The entire dispute concerns whether the likelihoods can be adequately justified.

The familiar argumentative progression is roughly as follows.

First, certain physical parameters are identified as necessary for the emergence of life or the structures believed to support it. Second, the observed values of those parameters are characterized as occupying an exceptionally small region of a much larger space of hypothetical values. Third, the restricted size of that region is interpreted as evidence that life-permitting conditions are extraordinarily improbable under naturalism. Finally, the existence of a divine creator is claimed to render those conditions more probable, thereby establishing comparative evidence favoring theism.

The decisive transitions occur between the second and third stages and again between the third and fourth.

The scientific identification of a restricted life-permitting region does not independently establish a probability for that region. Even if its probability were somehow established under a particular model, the comparison with theism would require further assumptions concerning what a deity would create.

The argument therefore depends on two distinct probabilistic judgments, neither of which follows merely from the physical sensitivity of the system.

### Physical sensitivity is not a probability distribution

It is important to begin by separating the legitimate physical content of fine-tuning discussions from the probabilistic interpretation often attached to that content.

Suppose a physical model contains a parameter $$\theta$$, and some phenomenon of interest occurs only when that parameter lies within a restricted interval:

$$
\theta\in[\theta_{\min},\theta_{\max}]
$$

Theoretical analysis might demonstrate that outside this interval, some physical structure becomes unstable, a required process cannot occur, or the modeled system behaves in a way incompatible with the phenomenon being investigated.

Such a result establishes a conditional relationship within the model.

It tells us that the phenomenon depends sensitively on the parameter, subject to the assumptions of the relevant physical theory.

But it does not establish how probable it is that $$\theta$$ would fall within the specified interval.

That requires a probability distribution.

If $$f(\theta\mid N)$$ denotes a density justified under the naturalistic model, then the probability associated with the life-permitting interval would be:

$$
P(L\mid N)
=
\int_{\theta_{\min}}^{\theta_{\max}}
f(\theta\mid N)\,d\theta
$$

This expression assumes, for simplicity, that the parameter's membership in the interval is equivalent to the condition for life within the model.

The physical sensitivity analysis may help determine the interval. It does not independently determine the density.

And without a justified density, the probability cannot be inferred from the interval alone.

The distinction remains even when the interval is exceptionally narrow.

A restricted range may indicate that the relevant phenomenon is highly sensitive to parameter variation. It does not establish that the realized parameter value was unlikely under the process, theory, or epistemic model being considered.

In engineering, this distinction would be entirely familiar. A complex system might function reliably only within a narrow temperature range. That fact does not establish the probability that the system will operate within that range. The answer depends on its actual operating environment, control systems, exposure conditions, and the probability distribution of relevant temperatures.

A narrow tolerance is not equivalent to a low probability of satisfying that tolerance.

The same logical distinction applies to cosmological fine-tuning.

The observation that certain physical constants appear restricted by the requirements of life does not establish the probability of their taking life-permitting values. That probability requires additional structure that the sensitivity analysis itself does not supply.

### The arbitrary reference range

A common way of translating a narrow interval into a small probability is to compare its width with a much larger reference range.

Suppose a dimensionless physical parameter $$\theta$$ is represented as lying within some interval from zero to $$R$$, while the life-permitting region occupies the interval from zero to $$\delta$$, where $$\delta<R$$.

If a uniform distribution is assumed, the probability becomes:

$$
P(L\mid N)
=
\frac{\delta}{R}
$$

For sufficiently large $$R$$ relative to $$\delta$$, this probability can be made extremely small.

But the calculation depends on at least two additional assumptions: that the reference range is appropriate and that the distribution over that range is uniform.

The sensitivity of the physical phenomenon to $$\theta$$ establishes neither assumption.

Why should the upper bound be $$R$$ rather than some other value? Why should the parameter be uniformly distributed? Why should the distribution be uniform in this particular parameterization? And what features of the underlying hypothesis justify treating the parameter as a variable governed by that distribution?

If these questions remain unanswered, the resulting probability is conditional on an arbitrary modeling choice.

The problem is not resolved by emphasizing how small $$\delta$$ is. The mathematical narrowness of the life-permitting interval does not independently establish the legitimacy of the reference range or the distribution used to evaluate it.

A probability can be made arbitrarily small by choosing a sufficiently expansive reference domain under a uniform measure. Conversely, a distribution concentrated near the life-permitting region can assign that region substantial probability.

Neither assignment becomes epistemically authoritative simply because it can be expressed mathematically.

The actual task is to justify the distribution relevant to the hypothesis being evaluated.

The principle of indifference is sometimes invoked to address this difficulty. If there is supposedly no reason to favor one interval over another, equal intervals are assigned equal probabilities.

But the inference from a lack of information to a uniform distribution is precisely what requires justification.

Ignorance does not establish equiprobability. Nor does a lack of known physical constraints imply that the parameter values were selected from a uniform distribution over a chosen domain.

Moreover, as discussed in Section 4, uniformity is not generally preserved when one independently imposes uniform distributions under different parameterizations.

A uniform prior over a physical quantity can differ substantially from a uniform prior over a nonlinear transformation of that quantity. Unless the argument provides some principled reason for privileging one measure, the resulting probabilities may depend on arbitrary representational choices.

The objection is not that every choice of measure is inherently illegitimate. Defensible measures can arise from symmetries, physical theories, statistical modeling objectives, or other independently supported considerations.

The objection is that the argument must establish the relevant justification rather than treating the measure as an automatic consequence of the space of possibilities.

### Are the physical constants independently variable?

The construction of a hypothetical parameter space introduces a further difficulty: it may assume that physical parameters can vary independently when their actual relationships are unknown or constrained.

A model of the universe may contain numerous constants whose values are treated as free parameters within the present theoretical framework. But this does not establish that those constants are metaphysically or physically independent.

A parameter may be freely specified within an effective theory while being constrained by a more fundamental theory. Likewise, multiple parameters that appear independent within one mathematical representation may be connected through relationships not yet understood.

The distinction is particularly important when considering simultaneous variation.

Let the relevant physical parameters be represented by:

$$
\boldsymbol{\theta}
=
(\theta_1,\theta_2,\ldots,\theta_n)
$$

Suppose the life-permitting region is denoted by:

$$
\mathcal{L}\subseteq\Theta
$$

The relevant probability would require a joint distribution:

$$
P(L\mid N)
=
\int_{\mathcal{L}}
f(\boldsymbol{\theta}\mid N)
\,d\boldsymbol{\theta}
$$

The joint distribution must account for any dependencies among the parameters.

One cannot simply multiply independently assigned probabilities unless an appropriate independence assumption is justified.

Even where varying one parameter while holding the others fixed produces drastic consequences, those results do not automatically establish what would happen under coordinated variations.

Some combinations of parameters may compensate for changes that would be catastrophic when considered individually. Other combinations may introduce additional constraints that make the life-permitting region smaller.

The methodological point is not that such compensating relationships necessarily exist, or that fine-tuning disappears when multiple parameters are varied. The point is that the relevant joint structure must be investigated rather than assumed.

A collection of individually narrow parameter tolerances does not automatically determine the probability mass associated with the joint life-permitting region.

Furthermore, the domain $$\Theta$$ must itself be justified.

Does it represent values permitted by a particular effective theory? Values compatible with mathematical consistency? Values realizable under a more fundamental physical theory? Or merely values that can be inserted into familiar equations while holding other assumptions fixed?

These are different domains.

The identification of mathematically describable alternatives does not demonstrate that those alternatives are physically realizable, much less that they carry comparable probabilities.

The philosophical inference frequently depends on treating an exploratory parameter space as though it were an established probability space describing how the universe could have been realized.

That transition is not warranted merely by the existence of the mathematical model.

### The distinction between physical possibility and model variation

At this point, a defender might argue that fine-tuning does not require a physical process that randomly selects constants. The relevant probabilities can instead represent rational expectations concerning how the universe might have been.

This is a legitimate distinction between physical chance and epistemic probability. The existence of a repeated stochastic process is not a general prerequisite for Bayesian reasoning.

But replacing a physical probability interpretation with an epistemic one does not remove the need to justify the relevant alternatives and their relative weighting.

There is a difference between constructing mathematical models in which physical constants possess different values and establishing that those models represent alternatives to which rational credence should be assigned in some particular manner.

In theoretical physics, varying parameters can be useful for understanding how a model behaves. Such variations may reveal sensitivities, stability conditions, or relationships among physical quantities.

They do not necessarily describe a process through which the actual universe might have been selected, nor do they independently establish a rational probability distribution over the alternatives.

If the argument appeals to epistemic probability, it must explain what background information is being used, which possibilities remain open relative to that information, and why some distribution over those possibilities is warranted.

If the argument instead appeals to objective physical probability, it must provide an account of the relevant chance structure or other physically justified probabilistic mechanism.

Neither interpretation can be established merely by referring to the mathematical space of parameter values.

A further complication concerns our knowledge of physical necessity.

We may not presently know whether certain fundamental constants could have possessed different values. A deeper physical theory might constrain them, relate them to other parameters, or explain their observed values through mechanisms not represented in our current theories.

The existence of such a theory cannot simply be assumed. But neither can its absence be converted into evidence that the constants were freely variable or randomly distributed.

Our uncertainty about the determination of physical constants is not itself evidence that their observed values were improbable.

This is an instance of the broader error identified throughout Part II: treating incomplete explanatory knowledge as though it supplied a substantive probability assignment.

The correct distinction is between not knowing why the constants have their values and having established that those values were unlikely under a particular hypothesis.

The former does not entail the latter.

### The probability of life and the definition of the evidence

Even if an appropriate distribution over physical parameters could be justified, another question remains: what exactly constitutes a life-permitting universe?

Fine-tuning arguments often appeal to conditions necessary for complex chemistry, stable atomic structures, long-lived stars, or other physical systems associated with familiar forms of life.

These investigations can provide meaningful constraints. Nevertheless, the definition of the relevant event must be carefully specified.

There is an important difference between showing that a parameter variation would prevent life as we understand it and showing that the variation would prevent every possible form of life.

The latter is a substantially stronger claim.

An investigation might establish that certain parameters are incompatible with carbon-based chemistry, stable nuclei, or familiar biological processes. But extending that result to all physically possible forms of organized complexity would require additional theoretical justification.

This does not mean that any imagined form of life should automatically be considered physically possible. Speculative alternatives are no more justified when introduced to defend naturalism than when introduced to defend theism.

Rather, the argument must be explicit about what its calculations establish and where their scope ends.

If the available physical analysis concerns known or theoretically modeled forms of life, then its conclusions should be stated at that level.

If the argument claims that the universe would be entirely incapable of supporting any form of conscious or complex organization, it must defend the stronger characterization.

The precise definition of the evidence matters because the probability of an event depends on what the event includes.

Let $$\mathcal{L}_K$$ denote the region supporting known or specifically modeled forms of life, and $$\mathcal{L}_A$$ the region supporting all forms of life admissible under a stated theoretical framework.

If the former is a subset of the latter, then under any fixed probability measure:

$$
P(\mathcal{L}_K)
\leq
P(\mathcal{L}_A)
$$

A calculation concerning a restricted class of life-permitting conditions cannot automatically establish the probability of the broader event.

The argument must therefore avoid moving between different definitions of life-permitting conditions without accounting for the consequences.

The same issue arises when the evidence is characterized more broadly as the existence of conscious observers, embodied moral agents, or intelligent life.

These are not identical observational propositions. They may impose different physical requirements and carry different implications under the competing hypotheses.

Consequently, the specification of the event is itself a substantive part of the probabilistic model.

### Observation selection and anthropic conditioning

A further complication concerns the relationship between the conditions necessary for observation and the fact that we are observing them.

We necessarily find ourselves in circumstances compatible with our existence as observers. This introduces an observation selection effect that must be considered when evaluating the evidential significance of life-permitting conditions.

In applied statistics, selection effects arise when the probability of an observation entering the available data depends on features of the underlying phenomenon.

Ignoring such effects can produce misleading inferences about the process being investigated.

The cosmological case has a structurally similar difficulty.

An observer cannot find themselves observing a universe that does not permit the existence of that observer. The available observation is therefore conditioned by the circumstances under which observation is possible.

This does not imply that life-permitting conditions are objectively probable. Nor does it imply that anthropic selection automatically defeats every fine-tuning argument.

The relevant point is that the observation process must be represented correctly.

Let $$O$$ denote the event that an observer capable of making the relevant observation exists, and $$L$$ the event that the observed universe permits that observer's existence.

If the model specifies that $$O$$ entails $$L$$, then:

$$
P(L\mid O,H)=1
$$

for any hypothesis $$H$$ under which the conditioning event has positive probability.

This identity does not establish that:

$$
P(O\mid T)=P(O\mid N)
$$

Nor does it show that the existence of observers cannot discriminate between metaphysical hypotheses.

Rather, it demonstrates that different choices of evidence and background information produce different conditional questions.

The probability that life-permitting conditions arise under a specified model is not the same as the probability that an existing observer will observe life-permitting conditions.

Likewise, the probability that observers exist under a hypothesis is not automatically identical to the probability of their observations conditional on their existence.

A defensible inference must specify which proposition constitutes the evidence, what background information is being conditioned upon, and how the observational selection mechanism enters the model.

Otherwise, the argument risks moving between distinct probabilities while treating them as interchangeable.

This is not a technical complication that can simply be dismissed by noting that the universe must permit life for us to observe it. The selection effect does not settle the comparative evidential question. It determines part of the structure that an adequate assessment of that question must address.

If the argument seeks to infer theism from the existence of observers, it must justify the probability of observer existence under the competing hypotheses.

If it seeks to infer theism from the particular life-permitting conditions we observe, it must justify the relevant conditional likelihoods while accounting for the circumstances under which those observations are available.

In either case, observation selection adds methodological requirements rather than removing them.

### The naturalistic likelihood has not been established

The preceding difficulties converge on a central probabilistic claim:

$$
P(L\mid N)\ll 1
$$

Fine-tuning arguments often depend on treating life-permitting conditions as extremely improbable under naturalism or under a more narrowly specified atheistic single-universe hypothesis.

But naturalism, considered as a broad metaphysical position, does not itself specify a distribution over possible physical constants.

Naturalism does not necessarily entail that physical parameters are selected independently, uniformly, randomly, or from any particular reference range. It does not require that the universe be generated by a chance process in which every mathematically describable configuration receives comparable probability.

These assumptions must be introduced through additional theoretical commitments.

A specific naturalistic cosmological model may generate testable predictions concerning parameters, initial conditions, or the distribution of physical outcomes. If so, those predictions can be assessed according to the model and the evidence supporting it.

But this is importantly different from attributing an arbitrary probability distribution to naturalism itself.

The absence of an established naturalistic explanation for the observed values does not independently establish that those values were improbable under naturalism.

It establishes an explanatory limitation.

To move from that limitation to a claim of low probability, the argument must supply an additional account of why the values should have been expected to fall elsewhere.

The distinction becomes especially clear when considering the hypothesis that there is a single universe whose fundamental parameters are not presently explained by a deeper physical theory.

Such a hypothesis may leave the parameter values as unexplained features of the world. But leaving a quantity unexplained does not entail assigning it a uniform distribution across a range of imagined alternatives.

An unexplained fact and a randomly selected fact are not equivalent.

If the argument treats the naturalistic hypothesis as involving a random selection process, it must justify why that process belongs to the hypothesis being evaluated.

If it instead treats the relevant probability as epistemic, it must explain why rational uncertainty about the values should be represented by the proposed distribution.

Simply describing the values as contingent, unexplained, or not necessitated by known laws does not establish the relevant likelihood.

The naturalistic likelihood is therefore not supplied by the observation of physical fine-tuning. It depends on an additional probabilistic model whose legitimacy must be independently defended.

### The theistic likelihood is equally in need of justification

Suppose, for the sake of argument, that the naturalistic likelihood could be shown to be very small under an adequately specified model.

The fine-tuning argument would still need to establish the corresponding likelihood under theism.

The fact that life-permitting conditions are improbable under one hypothesis does not independently demonstrate that they are more probable under another.

Theism does not automatically determine what kind of universe a divine creator would produce.

A theistic argument may propose that a benevolent God would value conscious beings, rational agents, moral development, or the flourishing of life. These considerations are then used to suggest that a life-permitting universe would be unsurprising under theism.

But the availability of such a theological explanation does not establish a particular conditional probability.

Why should a deity possessing the relevant attributes be expected to create embodied life rather than disembodied minds? Why should the existence of conscious beings require a universe governed by physical laws of the sort we observe? Why should a deity prefer a universe containing the particular mixture of life-permitting conditions, apparent indifference to life, and extensive physical regions unsuitable for known biological organisms?

These questions are not intended to establish that a deity would prefer some alternative universe. The point is that the proposed divine preferences are insufficiently constrained to justify a particular likelihood.

A broad hypothesis asserting the existence of an intentional creator is compatible with many possible creative purposes.

The conditional probability of life-permitting conditions therefore depends on how those purposes are represented and weighted.

Let $$\psi$$ represent the relevant subsidiary assumptions concerning divine intentions, creative preferences, or the manner in which divine agency relates to physical reality.

Then a marginal likelihood under theism would require a structure such as:

$$
P(L\mid T)
=
\int_{\Psi}
P(L\mid T,\psi)
\,P(d\psi\mid T)
$$

The mathematical expression does not require that divine intentions be objectively random. It represents the need to account for uncertainty over the subsidiary assumptions used to generate the likelihood.

The argument must still explain why the relevant assumptions deserve the probability weights assigned to them.

Selecting the proposition that God wishes to create embodied conscious life and treating it as though it followed directly from theism does not resolve this requirement.

It narrows the hypothesis to a particular theological model.

That model may be philosophically interesting, and it may be compatible with the observed universe. But compatibility is not comparative confirmation.

Nor can the likelihood be established simply by claiming that God could create life-permitting conditions. Divine ability to produce an outcome is distinct from the probability that the outcome would be produced.

Without a justified account of divine preferences and the weighting of possible creative outcomes, the theistic likelihood remains underdetermined.

### The problem of asymmetrical explanatory standards

At this point, the central asymmetry within the fine-tuning argument becomes apparent.

The naturalistic hypothesis is frequently penalized for failing to determine or explain the observed physical constants. This lack of determination is converted into a judgment of extreme improbability.

The theistic hypothesis, by contrast, is credited with a favorable likelihood because a plausible divine intention can be constructed that would make the observation intelligible.

But these are not equivalent inferential standards.

The absence of a known naturalistic explanation does not establish that the observation was improbable. Likewise, the existence of a compatible theistic explanation does not establish that the observation was likely.

The argument effectively converts uncertainty on one side into improbability, while converting explanatory flexibility on the other into probability.

That comparison has not been justified.

A methodologically consistent analysis would require defensible accounts of the relevant likelihoods under both hypotheses. Neither hypothesis should be assigned a favorable or unfavorable probability merely because its explanatory resources are more or less convenient for the purposes of the argument.

This becomes particularly important when theism and naturalism are treated as broad metaphysical categories rather than specifically defined predictive models.

An argument that selects one naturalistic model assigning life-permitting conditions a low probability and one theistic model assigning those conditions a high probability may establish a conditional comparison between those selected models.

It does not automatically establish the same likelihood ordering between naturalism and theism generally.

The inference to the broader ontological conclusion requires additional justification.

This is precisely the kind of model specification problem discussed in Section 6.

The relevant issue is not whether one can formulate a theistic model under which fine-tuning is expected.

It is whether the argument has established that this model, rather than other models compatible with theism, should govern the likelihood of the evidence.

The same demand applies to the naturalistic alternative.

### The problem is not solved by a multiverse

The possibility of a multiverse frequently enters discussions of fine-tuning as a proposed naturalistic explanation.

Under some multiverse models, physical conditions may vary across distinct regions or universes, and observers would necessarily arise only in regions compatible with their existence.

Such models can provide a framework within which the observed life-permitting conditions might be understood through variation and selection.

But invoking a multiverse does not automatically establish a probability distribution over universes, nor does it guarantee that the relevant observation selection effects have been modeled appropriately.

The evidential implications depend on the specific cosmological theory, its mechanism of variation, the distribution of physical parameters, the relevant measure, and the procedure by which observations are associated with observers.

In cosmology, these issues can become technically difficult, particularly in models involving very large or infinite ensembles of possible observational domains.

The important point is that a multiverse hypothesis requires its own methodological justification.

It would be inconsistent to criticize speculative theistic likelihoods while treating speculative multiverse probabilities as automatically legitimate.

But the converse is equally important.

The inability to establish a defensible multiverse probability model does not validate the fine-tuning argument for theism.

Nor does it establish that a life-permitting universe must be extraordinarily improbable under every naturalistic hypothesis.

The failure of one proposed explanation is not evidence for a competing explanation unless the relevant comparative relationship has been independently established.

The present critique therefore does not depend on the existence of a multiverse, the truth of some particular cosmological theory, or the successful construction of a competing naturalistic explanation.

It concerns whether the fine-tuning argument has established its own claimed likelihood comparison.

### Scientific naturalness and theological improbability

Another distinction is important here. In theoretical physics, fine-tuning can refer to problems of naturalness, parameter sensitivity, or the need for delicate cancellations among quantities within a model.

Such problems can motivate the search for deeper theories, new symmetries, or additional physical mechanisms.

But the technical use of fine-tuning in physics does not always imply the existence of a justified probability distribution over possible universes.

A parameter may appear unnatural within a theoretical framework because its observed magnitude requires substantial cancellation or is sensitive to assumptions about underlying scales. This may provide a legitimate reason to investigate whether the theory is incomplete.

It does not automatically establish that the parameter's observed value was improbable under naturalism.

The distinction matters because the philosophical argument can borrow the terminology and apparent quantitative force of physical fine-tuning without establishing the additional probabilistic claims necessary for theistic confirmation.

A technical naturalness problem may be scientifically substantive even if no probability over possible universes has been established.

Conversely, the existence of a small life-permitting region within a parameter model does not establish the probability of occupying that region under a metaphysical hypothesis.

These are related but distinct questions.

Conflating them risks converting a legitimate problem in theoretical physics into an unsupported probabilistic conclusion about ultimate reality.

### Why the evidential comparison cannot be inferred from the available premises

The general structure of the difficulty can now be stated formally.

Let $$\boldsymbol{\theta}$$ represent the relevant physical parameters, $$\mathcal{L}$$ the region compatible with the specified form of life, and $$M_N$$ a particular naturalistic model.

The physical analysis may establish a conditional relationship of the form:

$$
\boldsymbol{\theta}\in\mathcal{L}
\Longrightarrow
\text{life-permitting conditions}
$$

Or it may establish that values outside some specified region are incompatible with the physical structures necessary for the life under investigation.

These are substantive claims about the behavior of the theoretical model.

But the naturalistic likelihood requires:

$$
P(L\mid M_N)
=
\int_{\mathcal{L}}
P(d\boldsymbol{\theta}\mid M_N)
$$

The relevant measure must be supplied and justified.

The broader naturalistic likelihood may then require marginalization over multiple possible naturalistic models:

$$
P(L\mid N)
=
\int_{\mathcal{M}_N}
P(L\mid M_N)
\,P(dM_N\mid N)
$$

A comparable problem arises under theism, where the probability of life-permitting conditions depends on assumptions concerning divine intentions and the manner in which those intentions relate to the realized universe.

The desired comparison remains:

$$
BF_{T,N}
=
\frac{P(L\mid T)}{P(L\mid N)}
$$

But neither the numerator nor the denominator follows merely from the observation that the actual physical parameters permit life.

The numerator requires a justified predictive account under theism.

The denominator requires a justified predictive account under naturalism.

The mathematical analysis of fine-tuning, considered by itself, supplies neither.

The argument therefore needs more than a demonstration that life is sensitive to physical parameters. It needs an independently defensible bridge from those sensitivities to the relevant conditional probabilities.

Without that bridge, the Bayes factor is not established.

And if the Bayes factor is not established, the claimed comparative confirmation does not follow.

### Why a narrower claim of improbability is insufficient

A defender of the argument may concede that exact likelihoods are unavailable while maintaining that the relevant conclusion is obvious at a qualitative level.

Perhaps it is not necessary to calculate the precise probability of life-permitting conditions. Perhaps it is enough to recognize that the life-permitting region is extremely restricted and that its realization would therefore be extraordinarily surprising under naturalism.

But this response returns to the same unsupported transition.

The apparent restriction of a life-permitting region does not independently determine its probability.

Nor does the absence of a known explanation for the observed parameters establish that their realization should have been unexpected under a properly specified naturalistic model.

The claim:

$$
P(L\mid N)\ll 1
$$

is still a substantive probabilistic claim, even when no numerical value is supplied.

And the comparative claim:

$$
P(L\mid T)>P(L\mid N)
$$

requires additional justification beyond the supposed improbability of life under naturalism.

A qualitative likelihood ordering is not exempt from the methodological requirements governing probability assignments.

If those requirements have not been met, replacing precise numbers with the language of surprise or plausibility does not establish the missing inference.

The problem is not that the argument has failed to determine the exact magnitude of the Bayes factor.

It is that the assumptions presented have not justified its asserted direction.

### The methodological conclusion

The fine-tuning argument illustrates how a scientifically legitimate investigation can be transformed into an inadequately justified probabilistic inference.

The physical observation may be real. The sensitivity of modeled physical systems to changes in fundamental parameters may be substantial. The fact that familiar forms of life depend on numerous physical conditions may pose interesting questions for theoretical physics and cosmology.

None of these concessions establishes the probabilistic conclusion the philosophical argument requires.

The transition from a restricted life-permitting region to a low naturalistic likelihood depends on assumptions about the relevant parameter space, its probability measure, the dependencies among parameters, the determination of physical constants, and the appropriate treatment of observational selection.

The transition from that purported improbability to comparative support for theism introduces further assumptions concerning divine intentions, creative preferences, and the relationship between a broad theological hypothesis and the observed physical universe.

These are not minor uncertainties surrounding an otherwise established result. They constitute the inferential foundations of the argument itself.

The criticism therefore does not require denying the physical observations, rejecting Bayesian confirmation, or defending an alternative cosmological explanation.

Nor does it require assigning a higher probability to naturalism or insisting that the observed universe was likely to exist.

It requires only recognizing that the probabilistic claims used to establish comparative confirmation have not been adequately justified by the premises offered.

A defender might construct a more fully specified probabilistic model, supported by independent theoretical considerations, under which life-permitting conditions genuinely favor some form of theism over a specified alternative. Such an argument would have to be assessed on its own assumptions and evidential merits.

But the mere possibility of constructing such a model does not vindicate the existing inference.

The fact that an observation is compatible with a theistic explanation does not establish a favorable likelihood ratio. The fact that naturalism has not yet provided a complete account of the observed physical constants does not establish a low naturalistic likelihood. And the fact that a life-permitting region is narrow within a theoretical parameter space does not establish its improbability.

**The fine-tuning argument's central methodological failure is the conversion of physical sensitivity into probabilistic improbability, followed by the conversion of that alleged improbability into comparative confirmation of theism, without independently justifying the probabilistic assumptions required at either stage.**

The resulting Bayesian structure may be formally correct. Its likelihood comparison, however, has not been established merely by the physical facts invoked in its support.

This is the distinction between identifying a phenomenon worthy of scientific investigation and demonstrating that the phenomenon provides evidence for a particular metaphysical explanation.

The former may be justified. The latter requires an inferential foundation that the argument has not adequately supplied.

The argument has not demonstrated that the observed physical universe was improbable under naturalism, nor that its life-permitting conditions were more probable under theism. It has demonstrated, at most, that familiar physical structures and life depend on certain features of the universe within specified theoretical models.

That is not the same conclusion.

**The relevant probabilities have not been established, and therefore the advertised probabilistic confirmation of theism has not been demonstrated.**

## 8. Psychophysical Harmony: The Manufacture of Probabilistic Significance from Modal Speculation

The argument from psychophysical harmony provides an even more revealing example of the methodological failures examined throughout this essay. Whereas cosmological fine-tuning arguments begin with physical models whose parameters can be varied and whose consequences can, at least in some circumstances, be investigated through established theoretical methods, psychophysical harmony arguments begin with a far more controversial construction: a space of hypothetical relationships between conscious experiences and physical or functional states.

The argument then treats the apparent abundance of disharmonious relationships within that constructed space as grounds for concluding that the actual relationship between consciousness and physical processes is extraordinarily improbable under naturalism. This alleged improbability is subsequently compared with the supposed expectations of theism, yielding the conclusion that psychophysical harmony constitutes powerful evidence for the existence of God.

The methodological problems arise at virtually every stage of this inference. The space of hypothetical alternatives is not independently established. The metaphysical coherence of the proposed alternatives remains controversial. Their epistemic availability does not determine their relative probabilities. The probability measure used to evaluate the alleged alternatives lacks adequate justification. And the proposed likelihood advantage under theism depends on speculative assumptions concerning divine intentions and the normative significance of conscious experience.

These difficulties are not merely technical omissions in an otherwise adequate probabilistic argument. They undermine the foundations necessary for the argument to establish its claimed evidential conclusion.

The criticism is not that psychophysical harmony is necessarily uninteresting, nor that the relationship between consciousness and physical processes raises no philosophical questions. The problem is the attempt to transform uncertainty about those relationships into a substantive likelihood comparison between competing metaphysical hypotheses.

The argument proceeds as though the capacity to imagine alternative psychophysical relationships establishes a domain over which rational probability can be distributed, and as though the numerical predominance of imagined disharmonious alternatives establishes that the actual relationship was improbable.

Neither inference has been justified.

### The argument from psychophysical harmony

A prominent formulation of the argument appears in Brian Cutter and Dustin Crummett's *Psychophysical Harmony: A New Argument for Theism* (2025).

The authors identify what they regard as strikingly fortunate relationships between conscious experiences, physical states, and the functional organization of conscious organisms. They distinguish several forms of harmony, with particular emphasis on normative harmony and semantic harmony.

Normative harmony concerns the apparent correspondence between the normative significance of conscious experiences and the functional or behavioral roles associated with them.

Pain, for example, is ordinarily experienced as unpleasant or aversive, while the physical and behavioral systems associated with pain tend to promote avoidance of damaging stimuli. Pleasure, by contrast, is generally associated with experiences that are positively valued and with dispositions toward certain forms of approach or continued engagement.

The alleged harmony consists in the correspondence between what conscious experiences provide reasons for doing and what the associated physical or functional systems are disposed to do.

Semantic harmony concerns the correspondence between conscious experiences and our reports or judgments about those experiences.

When someone reports that they are experiencing pain, their report ordinarily corresponds to their actual experience. Likewise, judgments concerning the similarity, structure, or character of conscious experiences frequently correspond to the experiences they purport to describe.

The authors maintain that these correspondences would be remarkable if conscious experiences and physical states were related through fundamental laws that could have connected them in numerous alternative ways.

Under an initially assumed dualist framework, phenomenal states are taken to be ontologically distinct from physical states, with their relationships governed by fundamental psychophysical laws. If physical events are also causally complete, the physical mechanisms producing behavior and verbal reports can be specified without appealing to phenomenal states as additional causes.

Within that framework, it appears possible to imagine physical processes proceeding much as they actually do while conscious experiences are associated with them differently.

A physical state ordinarily associated with pain might instead be associated with pleasure. A physical system that produces avoidance behavior might be accompanied by an experience lacking any aversive character. A person's verbal reports about consciousness might fail to correspond to the experiences actually occurring.

The argument maintains that most conceivable psychophysical mappings would produce such disharmony.

By contrast, the actual relationships between conscious experiences and physical or functional states exhibit the kinds of correspondences that appear normatively and semantically appropriate.

The authors then argue that this pattern is extraordinarily improbable under ordinary naturalistic atheism, while being considerably more likely under theism because a benevolent creator would have reasons to realize the values associated with psychophysical harmony.

Let $$H$$ represent the observation of psychophysical harmony, $$T$$ represent theism, and $$N$$ represent the relevant naturalistic alternative.

The central likelihood claim is:

$$
P(H\mid T)\gg P(H\mid N)
$$

Under Bayesian confirmation theory, this inequality would imply that harmony favors theism, potentially by a substantial margin.

But the mathematical relationship is not what requires examination. The decisive issue is whether the argument has established the likelihoods appearing on either side of the comparison.

To assess that question, we must begin with something more fundamental than probability: the construction of the alleged space of alternative psychophysical relationships.

### The unestablished space of psychophysical alternatives

The argument begins by treating conscious experiences and physical or functional states as though their relationships can be systematically varied.

But what justifies that treatment?

Consider the suggestion that pain could have been associated with physical states ordinarily associated with pleasure, or that painful experiences could have been linked to behavioral systems promoting approach rather than avoidance.

The ability to describe such a scenario does not establish that it represents a coherent alternative to the actual relationship between consciousness and physical processes.

Whether these associations could have been different depends on substantive questions concerning the nature of phenomenal properties, physical realization, functional organization, metaphysical grounding, and the identity conditions of conscious states.

Suppose, for example, that the phenomenal character of pain is necessarily related to some feature of its physical realization or functional organization. In that case, the proposed recombination of pain with an arbitrarily different physical or functional state might not represent a genuine metaphysical possibility.

Alternatively, suppose that conscious experiences are related to physical states through metaphysically contingent psychophysical laws. Under that assumption, some alternative associations may be possible.

But the latter possibility cannot simply be taken as the neutral starting point of the argument.

It introduces a substantive metaphysical framework governing the relationships under investigation.

The argument therefore risks treating a controversial theory of consciousness as though it were an independently established description of the possible alternatives.

This matters because the alleged abundance of disharmonious relationships is not an incidental feature of the argument. It is the primary basis for asserting that the observed harmony was improbable.

If the proposed alternatives have not been justified, then neither has the domain from which the alleged improbability is derived.

The problem becomes clearer when we ask what exactly is being varied.

Are we holding the complete physical structure of the universe fixed while changing the phenomenal properties associated with particular states?

Are we altering fundamental psychophysical laws?

Are we changing the identity relations between phenomenal and physical properties?

Are we modifying relations of metaphysical grounding?

Or are we considering different functional organizations that might give rise to different phenomenal experiences?

These are not interchangeable operations.

Each presupposes a different account of the relationship between the physical and the phenomenal. Each may impose different constraints on which alternatives are coherent. Each may also yield a different domain of possible or epistemically open outcomes.

The construction of a single undifferentiated space of psychophysical mappings can conceal these distinctions.

Moreover, there is no established principle according to which phenomenal properties constitute a collection of independently assignable elements that can be freely distributed among physical or functional states.

Treating them in this manner already imposes a particular structure upon the problem.

That structure is not derived from an established theory of consciousness. It is introduced as part of the philosophical exercise.

The argument therefore has not demonstrated that its proposed sample space accurately represents the relevant metaphysical alternatives. It has constructed a collection of hypothetical descriptions and treated them as though they provide a suitable basis for probabilistic inference.

This is a foundational methodological deficiency.

### Conceivability does not establish metaphysical possibility

The appeal to alternative psychophysical mappings depends heavily on conceivability.

We can apparently imagine pain being associated with different functional roles. We can describe experiences occurring without corresponding reports. We can entertain scenarios involving inverted experiences, absent experiences, or mismatches between phenomenal and behavioral properties.

But, as established in Section 3, conceivability and metaphysical possibility are distinct.

Our ability to formulate a description does not demonstrate that the described arrangement could genuinely obtain.

This distinction is especially important in the philosophy of consciousness, where the relationships under investigation remain deeply contested.

The fact that physical descriptions do not transparently reveal the phenomenal character of consciousness may indicate an explanatory or conceptual limitation. It does not, by itself, demonstrate that phenomenal properties are metaphysically independent of physical properties.

A physicalist may hold that consciousness is identical to, realized by, or necessarily grounded in certain physical structures, even if those relationships are not discoverable through conceptual analysis alone.

An apparently conceivable separation between a phenomenal state and its physical realization may therefore arise because the relevant identity or grounding relationship is not apparent from the concepts being employed.

An analogy can be drawn with a posteriori identities.

Before discovering that water is constituted by H₂O, someone might have regarded water as capable of possessing a different chemical constitution. But once the identity is understood in the relevant metaphysical framework, the apparent possibility of water not being H₂O may be reinterpreted as a possibility concerning something that merely resembles water.

The epistemic ability to entertain the description does not establish that water itself could have possessed a different chemical identity.

The analogy does not prove that phenomenal and physical properties are identical. It illustrates why conceptual separability cannot automatically establish metaphysical separability.

An argument relying on independently variable phenomenal properties must therefore defend the metaphysical assumptions licensing that variation.

The burden is particularly substantial when the alleged alternatives are used to establish extreme improbability.

The argument does not merely claim that different psychophysical relationships can be entertained as conceptual exercises. It relies on their apparent abundance to characterize the actual relationship as exceptional.

But if the alternatives are not established as metaphysically coherent, then their abundance provides no direct information about the modal structure of reality.

And without further justification, that abundance certainly provides no information about probability.

### The retreat to epistemic possibility does not establish probability

A defender of the argument can acknowledge this objection without abandoning the proposed Bayesian inference.

Cutter and Crummett explicitly attempt to do so.

They argue that their reasoning need not depend on the metaphysical possibility of alternative psychophysical mappings. Even if physicalism is true and phenomenal properties are necessarily related to physical or functional properties, alternative relationships may remain epistemically possible.

An epistemic gap may persist between a complete physical description and what can be determined a priori about phenomenal experience.

On this approach, the relevant probability measure is understood as assigning epistemic probabilities to alternatives compatible with a specified state of knowledge, rather than objective chances to metaphysically possible worlds.

This is an important qualification. It would be inaccurate to characterize the argument as depending exclusively on the assertion that all conceivable psychophysical mappings are metaphysically possible.

But the qualification does not resolve the methodological problem.

The fact that multiple alternatives remain epistemically open does not establish a probability distribution over them.

Suppose we lack sufficient information to determine which physical property, if any, is identical to the phenomenal property of pain.

Several identity claims may therefore remain epistemically possible.

But what follows about their relative probabilities?

Nothing determinate follows merely from their epistemic availability.

An agent may be unable to exclude several hypotheses without possessing adequate grounds for treating them as equally probable, approximately equally probable, or distributed according to any particular measure.

The move from metaphysical possibility to epistemic possibility therefore changes the interpretation of the alternatives, but it does not establish the probabilistic structure required by the argument.

Indeed, it introduces additional questions.

What constitutes the relevant body of background knowledge?

Which alternative psychophysical descriptions are distinguishable relative to that knowledge?

How should uncertainty be distributed across the resulting alternatives?

What principles determine the relative epistemic probabilities of competing identity, grounding, or nomological hypotheses?

And why should those principles produce the particular distribution necessary to make psychophysical harmony extraordinarily improbable under naturalism?

These are precisely the questions that the argument needs to answer.

It is not enough to respond that epistemic probabilities can be assigned to epistemic possibilities.

The possibility of making an assignment does not demonstrate that any particular assignment is rationally warranted.

A coherent probability function can be constructed over hypothetical alternatives even when those alternatives are metaphysically impossible. But that mathematical construction does not establish that the resulting function represents the evidential support supplied by our actual knowledge.

**Epistemic openness does not determine epistemic probability.**

The distinction is elementary, yet the argument's central claim depends on moving between these concepts.

The argument treats the existence of numerous epistemically open psychophysical mappings as though it established that the actual harmonious relationship had a very small epistemic probability.

That conclusion does not follow without additional assumptions governing the probabilities of the alternatives.

The modal problem has not been eliminated. It has been replaced by a problem concerning the construction and justification of epistemic probability.

### The combinatorial illusion of improbability

The central probabilistic intuition behind psychophysical harmony is that there are vastly more ways for phenomenal properties to be associated disharmoniously with physical states than harmoniously.

This can be illustrated through a simplified mathematical model.

Suppose we define a finite collection of physical or functional states:

$$
F=\{f_1,f_2,\ldots,f_n\}
$$

And suppose we separately define a collection of phenomenal states:

$$
C=\{c_1,c_2,\ldots,c_n\}
$$

Now imagine that every phenomenal state can be paired with every functional state, subject only to the requirement that each element is paired exactly once.

The number of possible bijective mappings is:

$$
|\Omega|=n!
$$

Suppose, for simplicity, that only one of these mappings is classified as harmonious.

Under a uniform distribution over all mappings:

$$
P(H)=\frac{1}{n!}
$$

As the number of states increases, this probability becomes extremely small.

The mathematical result is straightforward. But its evidential significance depends entirely on the assumptions used to construct it.

First, the model assumes that phenomenal and functional states can be individuated independently.

Second, it assumes that every permutation constitutes an admissible alternative.

Third, it assumes that the relevant alternatives are appropriately represented by bijections.

Fourth, it assumes that harmony corresponds to the selected subset.

Fifth, and most importantly, it assumes a uniform probability distribution over the mappings.

None of these assumptions follows from the mere observation that conscious experiences correspond to physical and functional states.

The calculation therefore establishes only a conditional proposition: if the proposed state spaces, mapping structure, harmony criterion, and uniform measure are accepted, then the harmonious subset has the resulting probability.

It does not demonstrate that the actual psychophysical relationships were improbable.

And if the assumptions are not justified, the apparent improbability is an artifact of the constructed model.

The problem persists even without assuming a uniform distribution explicitly.

One might instead assert that harmonious mappings are not intrinsically more probable than sufficiently similar disharmonious mappings, or that the simplest mappings are more likely to be disharmonious.

But these claims also require justification.

What determines the intrinsic probability of a psychophysical mapping?

What makes one mapping simpler than another?

Which language or representation is being used to assess simplicity?

And why should that criterion determine rational credence concerning the actual relationship between consciousness and physical states?

A mapping that appears simple when phenomenal and functional states are represented independently may look very different under a theory in which their structures are necessarily connected.

Likewise, an apparently complicated mapping may be generated by a simple underlying relationship that is not captured by the chosen representation.

The problem is not merely that the number of mappings is large. It is that the enumeration, classification, and weighting of those mappings depend on substantive assumptions that have not been established.

A different measure over the same formal space could assign substantial probability to harmonious mappings. A different metaphysical theory might exclude the supposedly disharmonious alternatives entirely. A different representation might alter which mappings are counted as distinct or simple.

The sheer numerical abundance of imagined alternatives does not resolve any of these questions.

This is the combinatorial illusion at the heart of the argument: the mathematical proliferation of hypothetical alternatives creates the appearance of improbability without establishing an evidentially justified probability measure.

### The problem of individuation and representation

The difficulty is more fundamental than the absence of a uniform distribution.

Before counting psychophysical mappings, one must establish what counts as a distinct mapping.

Phenomenal experience is not obviously a collection of discrete, independently assignable properties. Experiences exhibit complex relationships involving similarity, intensity, temporality, intentional content, affective character, and integration with other experiences.

Likewise, physical and functional states are not naturally given as an arbitrary list of interchangeable slots. Functional states are individuated partly through their relationships to inputs, outputs, other internal states, and the organization of the system.

Treating these domains as separate collections of independently permutable elements risks ignoring precisely the structure that may be relevant to their relationship.

Consider two descriptions of a psychophysical association.

One representation may individuate physical states according to highly specific neural configurations. Another may individuate them according to higher-level functional organization.

A single functional state may be realized by numerous physically distinct configurations. Conversely, a physical state described at one level may participate in several higher-level functional roles.

The number and structure of possible mappings will depend on which level of description is chosen.

The same issue arises on the phenomenal side. A description that treats every distinguishable experience as a separate elementary state will yield a different mapping space from one that models experiences through a structured collection of phenomenal dimensions.

There is no reason to assume that these representational choices are probabilistically neutral.

Consequently, statements about the overwhelming numerical predominance of disharmonious mappings require an account of how the mappings are individuated and why the resulting structure is appropriate to the underlying phenomenon.

This is not an objection to the use of mathematical abstraction. Abstraction is indispensable in modeling.

The objection is that an abstraction cannot be treated as evidentially authoritative merely because it permits a dramatic counting argument.

In an applied setting, the choice of state representation would be scrutinized for its relationship to the actual system. A failure analysis based on arbitrarily partitioned system configurations would not acquire credibility simply because the resulting configuration space was mathematically large.

The corresponding methodological burden remains when the subject is consciousness.

### Physicalism and the assumptions behind the alleged surprise

The problem becomes especially apparent when the argument attempts to extend its conclusions beyond dualism.

Under some forms of dualism, fundamental psychophysical laws are treated as contingent connections between ontologically distinct physical and phenomenal properties.

Within that framework, it may be intelligible to ask why those laws associate particular phenomenal properties with particular physical states.

But physicalism does not generally accept that the relationship between consciousness and physical processes consists of two independent domains subsequently connected by contingent laws.

A physicalist may instead hold that phenomenal states are identical to physical states, necessarily realized by them, or metaphysically grounded in their organization.

If some version of such an account is correct, the language of freely permutable psychophysical mappings may misrepresent the relationship being investigated.

Cutter and Crummett recognize this difficulty. Their response is that, even if psychophysical identities are metaphysically necessary, multiple identity hypotheses may remain epistemically possible.

They argue that the actual harmonious identity is only one among numerous epistemically conceivable alternatives, and that its apparent specialness can therefore retain probabilistic significance.

But this response still requires a justified distribution over the competing identity hypotheses.

Consider a functionalist view on which pain is identical to a particular functional state associated with aversive processing.

If that identity is true, then the relationship between pain and the relevant functional organization is not an accidental association between independently existing properties.

The relationship follows from the identity itself.

A defender of psychophysical harmony may respond that there are numerous alternative functional states with which pain could have turned out to be identical, at least from an a priori epistemic standpoint.

But why should those alternative identity hypotheses receive comparable probabilities?

The existence of multiple descriptions does not establish their relative evidential support.

Nor is it obvious that the appropriate alternatives can be specified independently of our developing understanding of consciousness, functional organization, and phenomenal character.

The argument may appeal to the claim that we possess no a priori guarantee of a harmonious relationship. But the absence of an a priori guarantee does not establish that the harmonious relationship was improbable.

A posteriori identities are not rendered improbable merely because they cannot be established through conceptual analysis.

The discovery of an identity may resolve an apparent explanatory gap without requiring that the identity have been selected from a distribution over independently interchangeable properties.

Of course, a physicalist account must still defend its claims concerning consciousness. Identity, realization, and grounding are not explanatory achievements merely because they are asserted.

But the burden of developing a complete physicalist theory is distinct from the burden of establishing that the observed relationships are improbable under naturalism.

The failure of physicalism to provide a complete explanation would not automatically validate the probabilistic assumptions of the harmony argument.

That is the central methodological distinction.

Even if physicalism remains incomplete or controversial, its incompleteness does not provide a probability measure over alternative psychophysical identities.

And even if we grant the epistemic possibility of many alternative identities, the argument must still establish why the actual one should receive low probability.

Without that justification, the extension of the argument to physicalism reproduces rather than resolves the foundational problem.

### Normative harmony and the independence of phenomenal value

The notion of normative harmony introduces additional assumptions that require scrutiny.

The argument characterizes certain phenomenal experiences as possessing normative significance independently of their physical or functional roles.

Pain is presented as intrinsically aversive or bad, while pleasure is associated with positive experiential value. The alleged harmony arises because the functional roles of the corresponding physical states align with these normative properties.

But the precise relationship between phenomenal character, valence, functional organization, and normative significance is itself philosophically contested.

One might accept that painful experiences possess intrinsic negative value while remaining uncertain whether their phenomenal nature can be separated from every relevant physical or functional feature.

Alternatively, one might hold that certain aspects of affective experience are partly constituted by functional organization, motivational structure, or dispositions toward action.

These possibilities are relevant because the argument's apparent improbability depends on treating the normative character of experiences as capable of being reassigned independently of the functional roles with which it actually corresponds.

To regard the actual relationship as an unlikely alignment, the argument must justify the independence of the properties being aligned, at least in the probabilistic sense relevant to its inference.

Otherwise, the apparent coincidence may arise from representing as separate quantities features that are necessarily or structurally related.

This is analogous to a modeling error in which correlated variables are treated as independent, thereby making an observed joint configuration appear much less probable than it actually is under the appropriate model.

The analogy should not be mistaken for a demonstration that the relevant phenomenal and functional properties are necessarily connected.

The point is that their relationship cannot be assumed to be probabilistically unconstrained.

That question is part of the metaphysical problem under investigation.

A probabilistic argument cannot simply proceed as though the required independence had already been established.

### Semantic harmony and the problem of fixing content

Semantic harmony presents a related difficulty.

The argument emphasizes that our reports and judgments about conscious experience frequently correspond to the experiences they describe.

But the relationship between experience, judgment, linguistic meaning, and physical behavior is not straightforwardly represented by holding the contents of reports fixed while arbitrarily varying phenomenal experience.

The meaning of an introspective expression may itself depend on the subject's experiences, conceptual capacities, and the causal or functional relationships through which the expression is acquired and used.

If those relationships were different, the content of the associated reports might also differ.

Cutter and Crummett recognize that some apparent mismatches can be dissolved by considering how phenomenal character influences reference and meaning. They maintain, however, that other examples of semantic harmony remain significant.

Even granting that some correspondences require explanation, the probabilistic conclusion remains unestablished.

A formal model must specify what is held fixed when phenomenal states are varied, how the contents of introspective judgments are determined, and which relationships between experiences and reports are allowed to change.

If linguistic content and phenomenal reference are partly dependent on the same underlying structures, arbitrarily varying one while holding the other fixed may generate descriptions that do not preserve the relevant semantic relationships.

The resulting disharmony might then be a feature of the counterfactual construction rather than a genuine alternative outcome whose probability can be meaningfully assessed.

Furthermore, the mere possibility of constructing semantically mismatched descriptions does not establish that those descriptions have greater cumulative epistemic probability than the observed correspondence.

The same foundational problem reappears.

The argument must move from an account of the structure of possible semantic relationships to a justified probability distribution over those relationships.

Without that transition, the assertion of semantic improbability remains unsupported.

### Naturalism does not entail a random assignment of conscious experiences

Perhaps the most consequential problem with the naturalistic likelihood is the implicit treatment of psychophysical relationships as though they were drawn from an unconstrained space of alternative mappings.

Naturalism does not entail that conscious experiences are randomly assigned to physical states.

It does not entail that phenomenal properties and physical structures are independently variable.

Nor does it entail that their relationship is governed by a uniform or otherwise arbitrary distribution over conceivable associations.

A particular naturalistic theory might posit contingent psychophysical laws. Another might posit identity, realization, grounding, or constitutive relationships between consciousness and physical organization.

Other theories may differ substantially concerning the fundamental nature of experience.

These possibilities cannot simply be collapsed into a single naturalistic model that distributes probability over arbitrary psychophysical mappings.

A hypothesis that the physical and phenomenal domains are independent and connected through randomly selected laws is a much more specific model than naturalism itself.

If the argument wishes to evaluate that model, it must identify and defend it.

But the resulting probability would be conditional on that particular model, not automatically on naturalism generally.

The point becomes clear when considering the likelihood:

$$
P(H\mid N)
$$

This quantity cannot be derived simply from the claim that naturalism contains no divine designer.

The absence of a designer does not imply a uniform distribution over conceivable psychophysical relationships.

Nor does it establish that the actual relationships were generated without structural constraints.

Even if one assumes that naturalism offers no ultimate teleological explanation of psychophysical harmony, the absence of teleology does not establish a particular probability measure.

A non-teleological system need not behave like a random permutation of independently specified properties.

Physical systems regularly exhibit highly structured relationships without being modeled as random assignments over every conceivable configuration.

The structure may arise from identity relations, dynamical constraints, physical organization, or other mechanisms.

The existence and adequacy of such mechanisms in the case of consciousness remain open questions. But the argument cannot infer a low naturalistic likelihood merely by excluding divine intentionality and appealing to hypothetical alternatives.

That would conflate the absence of a particular kind of explanation with the presence of a particular stochastic or epistemic model.

**Naturalism is not a random mapping hypothesis.**

This distinction alone substantially undermines the transition from the abundance of imagined disharmonious relationships to the claimed improbability of harmony under naturalism.

### Evolutionary explanation and the limits of the argument

A related concern involves the possible explanatory role of biological evolution.

The correspondence between aversive experiences, bodily damage, learning, and avoidance behavior is closely connected to the functional organization of organisms.

Natural selection can, in principle, favor mechanisms that produce adaptive responses to environmental conditions.

An adequate naturalistic account of consciousness might therefore connect the functional organization of conscious organisms with the character and role of their experiences.

This does not automatically solve the philosophical problem.

Under a dualist view in which conscious experiences exert no influence on physical behavior, an evolutionary explanation of adaptive neural and behavioral mechanisms might leave unanswered why the phenomenal experiences associated with those mechanisms possess the particular normative character they do.

That residual problem deserves to be distinguished from the more general evolutionary explanation of behavior.

But identifying such an explanatory gap does not establish the probability of the psychophysical relationship.

An argument may demonstrate that a particular evolutionary explanation is incomplete under a stipulated metaphysical framework. It does not follow that harmony was improbable under naturalism.

To establish that conclusion, the argument still requires a justified probability model.

Moreover, naturalism does not require acceptance of the precise dualist framework under which the explanatory gap has been generated.

If the relationship between experience and functional organization is constitutive or metaphysically necessary, the relevant explanatory task may differ substantially.

The argument therefore cannot use the incompleteness of one naturalistic explanation to establish a general probabilistic disadvantage for naturalism.

Explanatory insufficiency is not a likelihood.

### The theistic likelihood and speculative divine preferences

Even if a low naturalistic likelihood were established, the argument would still require justification for the claim that psychophysical harmony is substantially more probable under theism.

The proposed explanation appeals to the value of psychophysical harmony.

A benevolent creator would allegedly have reason to establish relationships between conscious experiences and physical processes that promote rational agency, meaningful action, epistemic reliability, and the flourishing of conscious beings.

These considerations may form an intelligible theological narrative. But the availability of a possible divine reason does not establish the probability that a deity would act upon that reason in the manner proposed.

Theism, even when understood as the existence of an omniscient, omnipotent, and perfectly good creator, does not uniquely determine the structure of the created world.

A deity might have reasons to create embodied conscious agents. But a deity might also create disembodied minds, different forms of consciousness, substantially different physical systems, or worlds in which the relationship between conscious experience and behavior is organized according to principles unlike those observed.

The argument requires some account of how these possible creative outcomes should be weighted.

It is not enough to assert that psychophysical harmony is valuable.

Numerous possible features of reality may be valuable. The existence of value does not independently determine the probability that an agent possessing perfect goodness would instantiate a particular configuration.

Nor does the availability of a reason for producing an outcome establish how strongly that reason would determine the agent's action relative to other possible considerations.

The difficulty can be represented schematically.

Let $$\psi$$ denote the auxiliary assumptions concerning divine intentions, creative preferences, and their implications for psychophysical organization.

Then:

$$
P(H\mid T)
=
\int_{\Psi}
P(H\mid T,\psi)\,
P(d\psi\mid T)
$$

The likelihood depends on the assumptions determining what a deity would be expected to create and on how uncertainty concerning those assumptions is represented.

The mathematical expression does not imply that divine intentions are governed by objective randomness. It makes explicit the need for a justified treatment of uncertainty when deriving a likelihood from a broad hypothesis.

If the argument selects the assumption that God strongly values psychophysical harmony, and then uses that assumption to conclude that harmony is highly probable under theism, it has introduced a substantive subsidiary hypothesis.

The inferential burden is to justify that hypothesis and its probabilistic significance.

The observed harmony cannot itself supply the entire justification for the divine preference subsequently used to explain it without raising concerns about explanatory flexibility and the assessment of likelihoods.

This is particularly relevant because a sufficiently flexible appeal to divine purposes can make many different outcomes appear intelligible after they have been observed.

A world characterized by harmonious consciousness might be explained by a benevolent creator who values rational agency.

But a world with radically different psychophysical relationships might also be assigned some divine purpose, perhaps involving different kinds of conscious goods or forms of experience.

The relevant question is not whether some purpose can be associated with the actual outcome.

It is whether theism, together with independently defensible assumptions, assigns that outcome a higher likelihood than the competing hypothesis.

Without a constrained account of divine preferences, that comparison remains unsupported.

### The apparent likelihood advantage is an artifact of asymmetrical assumptions

The central Bayesian comparison now contains two unsupported elements.

Under naturalism, the argument appeals to a vast collection of hypothetical psychophysical mappings, treats harmonious mappings as exceptional within that collection, and infers that harmony possesses very low epistemic probability.

Under theism, the argument appeals to the value of psychophysical harmony and infers that a benevolent creator would have reasons to establish it.

The first inference treats the absence of divine design as grounds for distributing uncertainty across numerous disharmonious possibilities.

The second treats the availability of a compatible divine intention as grounds for assigning the observed outcome a comparatively favorable likelihood.

These procedures are not symmetrical applications of a common methodological standard.

Naturalism is burdened with an unconstrained domain of alternatives whose probabilities have not been justified. Theism is credited with a favorable explanatory assumption concerning divine preferences whose probability has likewise not been established.

The resulting likelihood inequality may therefore reflect the construction of the competing models rather than any demonstrated evidential discrimination supplied by the observation.

This problem is especially evident when numerical illustrations are introduced.

Cutter and Crummett illustrate their Bayesian argument using a likelihood ratio of fifty, which they describe as conservative while presenting the numerical example as hypothetical.

There is nothing mathematically objectionable about illustrating Bayes' theorem with stipulated numbers.

But the claim that a likelihood ratio of that magnitude would be conservative requires a substantive evidential basis.

What establishes that psychophysical harmony is at least fifty times more probable under theism?

What constrains the naturalistic likelihood?

What constrains the theistic likelihood?

And what justifies the confidence that the likelihood ratio favors theism by such a substantial margin?

The formal calculation cannot answer these questions.

Even if the illustrative numbers are discarded, the qualitative comparison requires the same foundational justification.

The central assertion remains:

$$
P(H\mid T)>P(H\mid N)
$$

The argument has not established that inequality merely by describing numerous hypothetical disharmonious mappings and proposing that God would value harmony.

An unsupported qualitative likelihood ordering is not rendered legitimate by avoiding precise numerical assignments.

The issue is not the number fifty. It is the absence of a defensible basis for the advertised direction and strength of confirmation.

### The explanatory gap is not evidence of improbability

The argument's deeper error can be seen in its treatment of explanatory uncertainty.

We do not possess a universally accepted account of why conscious experiences have the phenomenal character they do or how those experiences relate to physical processes.

This is a legitimate philosophical and scientific problem.

But the existence of an unresolved explanatory problem does not establish that the observed phenomenon was improbable.

The distinction is crucial.

A phenomenon may lack a satisfactory explanation because our theories are incomplete, because its underlying mechanisms are poorly understood, because its metaphysical structure is disputed, or because the relevant explanatory framework has not yet been developed.

None of these circumstances independently establishes a probability distribution over alternative outcomes.

In particular, the absence of an a priori derivation of phenomenal facts from physical facts does not entail that those phenomenal facts were probabilistically unexpected.

The argument from psychophysical harmony repeatedly risks treating an epistemic limitation as though it were evidence of an improbable realization.

We do not know why certain phenomenal states correspond to certain physical states.

Therefore, alternative correspondences appear epistemically open.

Because numerous alternatives can be described, the actual correspondence is treated as one among many.

Because most described alternatives are characterized as disharmonious, the observed harmony is treated as improbable.

But every transition introduces assumptions that require independent justification.

The final claim of improbability is not a consequence of the initial explanatory gap. It is a consequence of the modeling decisions introduced along the way.

Those decisions do not become epistemically warranted simply because the original philosophical question remains unanswered.

**An explanatory gap is not a probability distribution.**

And the existence of many imaginable explanations or alternative configurations does not demonstrate that the actual explanation or configuration was unlikely.

### Observation selection and the specification of harmony

An additional issue concerns the precise characterization of the evidence.

What level of psychophysical harmony is being assessed?

Is the evidence that conscious organisms possess experiences sufficiently coordinated with their functional organization to survive and reproduce?

Is it that conscious experiences generally correspond to introspective reports?

Is it that the particular relationship between experience, valence, rational agency, and behavior exhibits a high degree of normative appropriateness?

These are different claims, and their probabilistic significance need not be identical.

Cutter and Crummett argue that the observed degree of harmony goes beyond what would be required merely for conscious observers to exist. They therefore maintain that observation selection does not remove the apparent surprise.

But establishing that a phenomenon exceeds some minimum threshold does not independently establish its probability.

The argument must still specify the relevant measure and explain why the observed degree of harmony occupies a low-probability region under naturalism.

Moreover, the definition of the event must be sufficiently clear to distinguish genuine evidential features from properties used retrospectively to characterize the observed outcome as special.

If harmony is defined broadly, the class of harmonious relationships may be correspondingly large. If it is defined narrowly, the event may become more specific, but its specificity does not automatically provide comparative confirmation.

Any sufficiently detailed description of the actual world may occupy a small region of a constructed possibility space.

What matters is not simply its descriptive specificity, but whether the observation is more probable under one hypothesis than another.

The definition of psychophysical harmony must therefore be connected to a defensible probabilistic model.

Observation selection, the existence of conscious observers, and the particular criteria used to characterize harmony cannot be ignored merely because the argument focuses on an apparently exceptional feature of experience.

### Why psychophysical harmony is methodologically more problematic than fine-tuning

The comparison with cosmological fine-tuning is instructive.

In the physical case, at least some proposed parameter variations can be examined within established mathematical theories. Researchers can investigate how a physical model behaves under altered values, identify stability conditions, and characterize sensitivity to particular parameters.

These exercises do not establish probabilities over possible universes, but they can provide substantive information about the conditional behavior of physical systems.

In psychophysical harmony, the corresponding domain of alternatives lacks even this comparatively firm theoretical foundation.

There is no comparably established mathematical theory defining a space of independently permutable phenomenal properties and physical states, identifying the constraints governing their relationships, and determining which mappings constitute coherent alternatives.

Nor is there an independently justified probability measure over that space.

The argument instead relies on contested metaphysical assumptions, conceptual exercises, and intuitions about the relative abundance or simplicity of alternative associations.

It then attempts to translate those considerations into a claim of extreme epistemic improbability.

The difficulty is therefore not merely analogous to the measure problem in fine-tuning. It arises earlier.

Before asking how probability should be distributed over psychophysical mappings, the argument must establish why the proposed mappings form an appropriate domain for probabilistic inference.

Before appealing to their numerical predominance, it must justify how the alternatives are individuated.

Before claiming that the actual mapping is exceptional, it must establish the criteria governing the comparison.

Before interpreting that exceptionalism probabilistically, it must justify the measure.

And before claiming comparative confirmation of theism, it must justify the likelihoods under both metaphysical hypotheses.

These are cumulative methodological burdens.

A failure at any one of them can undermine the advertised inference. The argument, however, proceeds through all of them without establishing the probabilistic foundations required for its conclusion.

### What the argument actually establishes

The strongest defensible conclusion from the observations invoked by psychophysical harmony is substantially more modest than the claimed Bayesian confirmation of theism.

Conscious experiences exhibit relationships with physical organization, behavior, and introspective reports that raise important questions about the nature of consciousness.

Those relationships may be difficult to explain under some metaphysical theories.

Certain dualist frameworks may face a challenge concerning why their contingent psychophysical laws produce experiences with apparently appropriate normative and semantic roles.

These are legitimate subjects for philosophical investigation.

But none of these claims establishes that psychophysical harmony was improbable under naturalism.

Nor do they demonstrate that harmony was more probable under theism.

The argument attempts to derive those conclusions from a speculative space of alternatives whose coherence, individuation, and probability structure have not been adequately justified.

Theistic explanations introduce further assumptions about divine intentions and creative preferences, but those assumptions do not independently establish the likelihood of the observed relationships.

Consequently, the proposed Bayesian comparison has not been shown to possess the evidential force attributed to it.

This criticism does not require proving physicalism, denying phenomenal consciousness, or constructing a complete naturalistic explanation of subjective experience.

It does not require demonstrating that alternative psychophysical relationships are metaphysically impossible.

It does not even require denying that epistemic probabilities can, in principle, be assigned to epistemically possible hypotheses.

The objection is more fundamental.

The argument has not established that the relevant alternatives and their relative probabilities are justified, nor that they support the proposed comparison between theism and naturalism.

A critic does not need to replace the alleged probability of harmony with a different number.

The burden belongs to the argument claiming that harmony provides comparative evidential support for theism.

And the argument has not discharged that burden merely by describing conceivable alternatives, invoking epistemic probability, or appealing to the value of harmonious consciousness.

The resulting inference remains conditional on assumptions that have not been independently established.

### The methodological conclusion

The argument from psychophysical harmony exemplifies a particularly severe form of probabilistic overreach.

It begins with a genuine philosophical problem concerning consciousness and the relationship between phenomenal experience and physical organization.

It constructs an expansive domain of imagined alternative relationships.

It treats the apparent abundance of disharmonious alternatives as grounds for an extremely low naturalistic likelihood.

It then invokes a possible divine preference for valuable conscious experiences to establish a supposedly favorable theistic likelihood.

Finally, it presents the resulting comparison as strong evidence for a substantive metaphysical conclusion.

But the inferential foundations required for that conclusion have not been justified.

The construction of the possibility space depends on controversial assumptions about the nature of consciousness. The transition from conceivability to metaphysical possibility is disputed. The retreat to epistemic possibility does not supply a probability measure. The counting or intuitive weighting of hypothetical mappings does not establish their relative probabilities. And the alleged theistic likelihood depends on auxiliary assumptions concerning divine intentions that remain insufficiently constrained.

The argument therefore does not merely suffer from uncertain numerical estimates.

Its basic probabilistic representation has not been adequately established.

Even the qualitative claim that harmony is more probable under theism than under naturalism depends on inferential assumptions that the argument has not justified.

The central difficulty can be stated succinctly:

**The argument manufactures probabilistic significance from modal speculation. It treats the capacity to describe alternative psychophysical relationships as though it establishes an appropriate domain of probabilistic alternatives, treats the apparent abundance of disharmonious descriptions as evidence of improbability, and then converts that alleged improbability into comparative confirmation of theism.**

None of these transitions is warranted simply by the formal availability of Bayesian reasoning.

The failure to explain consciousness completely is not evidence that the actual relationships between conscious experiences and physical states were improbable. The ability to imagine disharmonious alternatives is not evidence that those alternatives possess significant cumulative probability. And the availability of a divine explanation is not evidence that the observed harmony was comparatively likely under theism.

The argument has identified a philosophical question. It has not established the probability comparison required to answer that question in favor of God.

**The probability was never established because the alleged probabilistic alternatives, their weighting, and their comparative relationship to the competing hypotheses were never adequately justified.**

This failure is more fundamental than disagreement over the precise value of a prior or the magnitude of a Bayes factor. It concerns whether the proposed Bayesian comparison has been given a defensible epistemic foundation at all.

The next section extends this criticism beyond explicitly Bayesian arguments. The same methodological pattern appears when philosophical arguments appeal to inference to the best explanation, explanatory virtues, or the alleged superiority of a theistic explanation without establishing the connection between explanatory compatibility and comparative evidential support.

# Part IV — Beyond Bayesianism: The Problem with Inference to the Best Explanation

## 9. Explanatory Possibility Is Not Evidential Confirmation

The methodological problems examined in the preceding sections are not confined to arguments that explicitly employ Bayesian probability theory. Similar difficulties arise when philosophers appeal to inference to the best explanation, explanatory virtues, or the supposed superiority of theistic explanations over their naturalistic alternatives. In these arguments, the formal apparatus of Bayesian confirmation may be absent, but the underlying inferential ambition remains substantially the same: to establish that certain features of reality provide reasons for accepting theism rather than naturalism.

The difficulty is that the ability to construct an explanation of an observation does not independently establish that the explanation is true, probable, or evidentially superior to its competitors. Nor does the absence of a satisfactory alternative explanation establish that the proposed explanation is comparatively well supported. Explanatory compatibility, explanatory quality, and evidential confirmation are distinct concepts, and moving between them requires justification.

This distinction is particularly important in philosophical arguments for God because the hypotheses under consideration are exceptionally broad, their explanatory implications frequently depend on unconstrained auxiliary assumptions, and the phenomena they are invoked to explain often lie at the boundaries of existing theoretical understanding.

Theism may be offered as an explanation for the existence of the universe, the life-permitting character of physical laws, the emergence of consciousness, or the apparent normative structure of human experience. In each case, the argument may proceed by suggesting that the phenomenon becomes intelligible if a divine creator exists, while naturalism allegedly leaves the phenomenon unexplained or insufficiently understood.

But the existence of an explanatory narrative does not settle the evidential comparison.

An explanation can be internally coherent without being independently supported. It can accommodate an observation without having generated a defensible expectation of that observation. It can possess qualities we find intellectually attractive without those qualities being sufficient to establish its truth. And it can be preferable to the alternatives currently under consideration without being an adequate explanation of the phenomenon.

These are not merely abstract philosophical possibilities. They represent familiar methodological problems in scientific modeling, causal inference, and the evaluation of competing hypotheses.

The central question is therefore not simply whether theism can be presented as an explanation of some phenomenon. It is whether the proposed explanation possesses a justified evidential advantage over its alternatives.

Without an adequate account of that advantage, inference to the best explanation risks reproducing the same methodological failures previously identified in Bayesian arguments, but without the formal structure that would make its assumptions explicit.

### The structure of inference to the best explanation

Inference to the best explanation, commonly abbreviated IBE, is a form of ampliative reasoning in which a hypothesis is supported or provisionally accepted because it provides the best explanation of some body of evidence.

The modern philosophical formulation is commonly associated with Gilbert Harman and subsequently developed by philosophers including Peter Lipton. The details vary across different accounts, but the basic idea is that explanatory superiority can provide a reason for accepting a hypothesis.

The general structure can be expressed as follows.

An observation or collection of observations requires explanation. Several competing hypotheses are considered. Those hypotheses are evaluated according to their explanatory qualities. One hypothesis is judged superior to the others. That superiority is then used to justify some level of belief in the hypothesis.

Unlike deductive reasoning, the conclusion does not follow necessarily from the premises. The existence of a superior explanation does not logically entail its truth. IBE is therefore generally understood as a form of non-deductive inference whose epistemic legitimacy depends on the connection between explanatory quality and truth or rational acceptance.

Different philosophical accounts understand that connection differently.

Some treat IBE as an independent rule of rational inference. Others regard explanatory virtues as useful heuristics for approximating Bayesian confirmation. Still others emphasize the role of explanatory reasoning in generating hypotheses without granting that explanatory superiority alone establishes their truth.

These distinctions matter.

The present critique does not assume that every legitimate explanatory inference must be reducible to Bayes' theorem. Nor does it deny that explanatory considerations can play important roles in scientific and philosophical reasoning.

Its target is more specific: the assumption that explanatory attractiveness, compatibility, or apparent superiority can support substantive metaphysical conclusions without an adequate account of why those features are evidentially significant.

An explanation must do more than provide a description under which an observation appears intelligible.

It must establish some defensible connection between the explanatory hypothesis and the phenomenon being explained.

In many scientific contexts, that connection can be investigated through mechanisms, theoretical constraints, empirical predictions, interventions, or independent lines of evidence. Not every explanatory success requires all these features, and legitimate scientific explanations vary substantially in their structure.

Nevertheless, explanatory claims are not made credible simply by describing how a phenomenon could arise if a preferred hypothesis were true.

The explanation must have an adequate basis for its application to the phenomenon.

This is the methodological standard that becomes especially important when IBE is used to support the existence of God.

### Explanatory compatibility is not evidential confirmation

The most elementary problem is the distinction between a hypothesis being compatible with an observation and the observation providing evidence for that hypothesis.

Suppose we observe some phenomenon and identify a hypothesis under which the phenomenon could occur.

At most, this establishes that the hypothesis is not excluded by that observation, assuming that the proposed compatibility has been correctly characterized.

It does not establish that the hypothesis is likely to be true.

Nor does it demonstrate that the observation favors the hypothesis over competing explanations.

The distinction is readily expressed in probabilistic terms, although it does not depend on accepting Bayesianism as the only legitimate theory of confirmation.

Let $$E$$ represent an observation and $$H$$ a proposed hypothesis.

The observation's compatibility with the hypothesis may be represented, in a suitably specified probabilistic model, by:

$$
P(E\mid H)>0
$$

But this does not establish:

$$
P(H\mid E)>P(H)
$$

Nor does it establish that the evidence comparatively favors $$H$$ over some alternative hypothesis $$A$$:

$$
P(E\mid H)>P(E\mid A)
$$

Compatibility and confirmation are different relationships.

Indeed, an observation may be compatible with a hypothesis while providing evidence against it, if the observation is even more expected under competing hypotheses.

A theory's capacity to accommodate an observation therefore cannot independently establish the evidential relevance of that observation.

This is especially important in theistic explanation.

A philosopher may argue that a benevolent creator could have reasons to produce a universe containing conscious life. Or that a divine intelligence could establish fundamental physical laws exhibiting mathematical order. Or that God could organize psychophysical relationships so that conscious experiences possess appropriate functional and normative roles.

Even if all these explanatory proposals are granted as coherent possibilities, their mere availability does not establish that the corresponding observations favor theism.

The proposed explanation must demonstrate some connection between the hypothesis and the observation that goes beyond compatibility.

If theism accommodates the existence of conscious beings but also accommodates their absence, their radically different organization, or entirely different kinds of created reality, then the observation of conscious beings does not automatically possess the discriminatory force attributed to it.

The question is not whether theism permits the observed phenomenon.

It is whether theism provides a sufficiently constrained explanatory account that warrants treating the phenomenon as evidence for the hypothesis.

Without that distinction, virtually any observation that can be incorporated into a theological narrative becomes a potential source of confirmation.

That is not an adequate basis for comparative inference.

### The absence of a naturalistic explanation does not establish theism

A related problem arises when theistic explanations are defended by appealing to alleged deficiencies in naturalistic explanations.

The structure often takes a familiar form.

Some phenomenon is identified as difficult to explain under current naturalistic theories. A theistic explanation is then proposed. The absence of a satisfactory naturalistic explanation is treated as a reason to regard the theistic explanation as superior.

But the absence of an explanation and the improbability of the phenomenon under a hypothesis are not equivalent.

Nor does a failure to construct an adequate explanation under one hypothesis establish that some competing explanation is correct.

A hypothesis may leave an observation unexplained because its theoretical development is incomplete. The relevant mechanisms may be unknown, the available evidence may be insufficient, or the phenomenon may not yet be adequately characterized.

These limitations do not automatically imply that the hypothesis conflicts with the observation.

There is an important difference between a theory predicting that a phenomenon should not occur and a theory failing to explain why the phenomenon occurs.

The former may constitute substantive evidence against the theory. The latter may identify an explanatory limitation without establishing the direction or magnitude of evidential support.

Consider psychophysical harmony.

Suppose a philosopher argues that contemporary naturalistic theories do not adequately explain why conscious experiences exhibit their particular relationships with physical and functional states.

This may identify a genuine explanatory problem.

But it does not establish that the observed relationships are improbable under naturalism.

Nor does it establish that theism provides a better explanation merely because a divine creator could intend to produce harmonious experiences.

The naturalistic explanatory gap and the proposed theistic explanation must each be evaluated according to their own substantive merits.

The inadequacy of one explanation cannot supply the missing justification for another.

The same issue arises in cosmological fine-tuning.

The inability to provide a complete naturalistic explanation for the observed values of fundamental physical constants does not establish that those values were unlikely under naturalism.

A proposed divine explanation does not become evidentially successful simply because the physical determination of those constants remains unresolved.

To conclude otherwise would be to convert the incompleteness of current knowledge into positive support for a particular metaphysical hypothesis.

This is precisely the type of inferential transition that requires justification.

The problem is not that appeals to explanatory gaps are always illegitimate. A genuine inconsistency between a theory and an observation, or a demonstrated inability of a specified model to generate an observed phenomenon, can be important evidence against that model.

But such conclusions depend on establishing the relevant theoretical constraints.

A failure to explain something is not automatically equivalent to a demonstration that the phenomenon could not have occurred, or was improbable, under the hypothesis.

And without that distinction, the comparative superiority attributed to theism may reflect differences in explanatory expectations rather than differences in evidential support.

### The problem of explanatory flexibility

A hypothesis can appear explanatorily powerful because it is compatible with a large variety of possible observations.

But the capacity to accommodate many possible outcomes is not necessarily a mark of evidential strength.

In some circumstances, it can indicate that the hypothesis is insufficiently constrained to discriminate among alternatives.

This problem is especially relevant to explanations invoking the intentions of an agent.

Intentional explanations can be informative when the agent's goals, abilities, constraints, preferences, and circumstances are independently understood.

For example, the behavior of an organization may be explained by reference to its established objectives, institutional rules, available resources, and documented decision processes.

The explanation gains credibility because the relevant intentional structure is independently constrained.

We may possess records of the organization's decisions, evidence of its incentives, observations of its past behavior, or well-supported models of its operating environment.

These constraints allow us to distinguish what the organization would reasonably be expected to do from what it merely could do.

But suppose we introduce a hypothetical agent whose goals and preferences are largely unspecified.

We observe some outcome and then propose that the agent desired that outcome.

The explanation is immediately available.

Yet its availability provides little evidential discrimination unless there are independent reasons to believe that the agent possessed the relevant preference.

The explanatory hypothesis risks becoming adaptable to whatever outcome happens to occur.

This distinction matters for theistic explanations.

If a universe contains conscious embodied organisms, one may suggest that God values embodied consciousness.

If a universe contains radically different forms of conscious existence, one might instead suggest that God values those forms.

If the universe exhibits simple physical laws, simplicity might be attributed to divine preference.

If the universe exhibits profound complexity, complexity might be attributed to divine purposes.

The point is not that theism logically permits every conceivable outcome or that theological explanations are necessarily devoid of constraints.

Particular theologies may impose substantive restrictions on divine action. Those restrictions may deserve philosophical consideration.

The problem arises when the explanatory assumptions are selected primarily because they accommodate the observation, while their independent justification remains unclear.

Under those circumstances, the apparent explanatory success may be generated by the flexibility of the hypothesis rather than by its capacity to identify or anticipate the relevant features of reality.

The existence of an explanation for the observed outcome is not enough.

One must also explain why the hypothesis should be preferred over alternatives and why the assumptions used to generate the explanation are independently warranted.

Otherwise, explanatory flexibility can be mistaken for explanatory power.

### Explanatory virtues and their evidential significance

Defenders of IBE frequently appeal to explanatory virtues such as simplicity, coherence, explanatory scope, unification, and theoretical elegance.

These considerations can be valuable.

Scientific theories are routinely assessed in relation to their ability to explain multiple phenomena through common principles, avoid unnecessary assumptions, integrate with established knowledge, and generate fruitful research programs.

But the methodological significance of these virtues is not uniform across contexts, and their relationship to evidential support requires careful examination.

An explanation can be simpler without being true.

It can be more elegant without possessing greater empirical adequacy.

It can unify multiple observations under a common description while failing to identify the mechanisms responsible for those observations.

And it can be intuitively satisfying because it resembles familiar forms of explanation rather than because it accurately represents reality.

These possibilities do not render explanatory virtues worthless. They establish that the virtues cannot be treated as self-justifying indicators of truth.

Consider simplicity.

A hypothesis may be simple in terms of the number of entities it postulates while being complex in terms of the properties or dispositions attributed to those entities.

A single explanatory agent may appear ontologically economical, but the specification of that agent's preferences, abilities, intentions, and relationship to the phenomenon may introduce substantial additional structure.

Likewise, a mathematical theory containing several interacting entities may nevertheless generate a highly constrained and unified account of observations.

Without an adequately specified criterion, simplicity comparisons can become ambiguous.

The problem is amplified when simplicity is invoked to justify an ontological conclusion.

Suppose theism is described as a simple explanation because it attributes the relevant phenomena to a single divine mind.

This description does not establish that the resulting hypothesis is simpler under every relevant measure of complexity.

Nor does it demonstrate that the alleged simplicity provides sufficient evidence for the existence of the proposed entity.

A further argument is needed connecting the relevant notion of simplicity to rational belief.

Similar difficulties arise with explanatory scope.

A broad hypothesis may be capable of explaining many observations because its subsidiary assumptions can be adjusted to accommodate them.

But the number of observations that can be incorporated into an explanatory narrative is not necessarily equivalent to the number of observations that the hypothesis independently constrains.

There is a difference between a theory that derives multiple phenomena from a common, independently specified structure and a theory that invokes additional explanatory assumptions whenever a new phenomenon is introduced.

Both may appear to possess substantial explanatory scope, but their methodological significance can differ considerably.

The relevant question is not simply how many observations can be explained after the fact.

It is what substantive constraints the explanation supplies, how its assumptions are justified, and whether its purported explanatory virtues provide an adequate reason for treating the hypothesis as true or comparatively well supported.

An IBE argument cannot bypass these questions by treating explanatory virtues as inherently evidentially authoritative.

### The distinction between explanatory unification and empirical constraint

Unification deserves particular attention because it frequently plays a central role in philosophical arguments for God.

A single metaphysical principle capable of accounting for several seemingly unrelated features of reality may appear intellectually attractive.

For example, a divine creator might be invoked to explain the existence of the universe, its physical order, its life-permitting character, and the presence of conscious beings.

The resulting worldview appears to unify disparate phenomena under a common explanatory source.

But there is a crucial distinction between unification through a constrained theory and unification through the repeated application of an unrestricted explanatory category.

A physical theory can achieve explanatory unification by deriving multiple phenomena from a shared mathematical structure whose consequences are sufficiently constrained to be investigated.

The explanatory achievement depends partly on the fact that the theory does not simply accommodate arbitrary outcomes.

Its structure restricts what can occur under specified conditions.

By contrast, a broad metaphysical explanation may unify phenomena by attributing them to the decisions or intentions of an agent whose preferences remain unspecified.

The same explanatory source can then be applied to numerous observations without necessarily determining why those observations, rather than alternatives, should obtain.

The distinction is not between physical and nonphysical explanations as such.

It is between explanatory structures whose relationships to the phenomena are adequately constrained and those whose apparent scope arises primarily from their flexibility.

An explanation can be general without being informative.

Likewise, an explanation can be unified at the level of vocabulary without possessing the independent constraints necessary to establish a substantive account of the phenomena.

A theistic explanation may identify a single proposed source for multiple features of reality, but the mere identification of that source does not demonstrate why the particular features should follow from it.

If additional assumptions about divine purposes are required for each phenomenon, the explanatory achievement depends on the legitimacy of those assumptions.

And if those assumptions are selected after the observations are known, the apparent unification may not possess the evidential significance attributed to it.

This is not a demand that every explanation produce exact quantitative predictions.

It is a demand that the explanation establish some defensible relationship between its assumptions and the phenomena it purports to explain.

Without that relationship, unification may amount to a common label attached to otherwise unresolved explanatory problems.

### The problem of the best available explanation

Another difficulty concerns the comparative structure of IBE.

Even if one explanation is genuinely superior to the alternatives currently under consideration, it does not follow that the explanation is true or sufficiently well supported to justify belief.

The best available explanation may still be inadequate.

This problem is familiar in the philosophy of science and is commonly associated with Bas van Fraassen's objection that IBE may select the best explanation from an inadequate collection of candidates.

The point is straightforward.

Suppose an investigator considers three possible explanations of a complex system failure.

One explanation accounts for more observations than the other two. It is more coherent, requires fewer unsupported assumptions, and better fits the available evidence.

The investigator may reasonably regard it as the leading hypothesis.

But if the actual failure resulted from a mechanism that none of the three explanations represents, the best available explanation may still be incorrect.

Its relative superiority would not establish its absolute adequacy.

In practical investigation, this possibility motivates the search for overlooked mechanisms, additional observations, alternative model structures, and independent tests.

The same methodological concern applies to philosophical arguments.

Suppose theism is judged superior to several naturalistic explanations of consciousness.

What establishes that the alternatives under consideration adequately represent the relevant explanatory possibilities?

What establishes that the evaluation criteria capture the features most relevant to truth?

And what establishes that the best explanation among those considered is sufficiently well supported to warrant the ontological conclusion?

The existence of a preferred explanation does not answer these questions.

This problem becomes especially serious when the competing hypotheses are extremely broad and the underlying phenomenon is poorly understood.

Our present explanatory options may be incomplete. The relevant theoretical framework may require substantial revision. The correct explanation may involve distinctions that are not represented within the currently available hypotheses.

The possibility of unconceived alternatives does not imply that all explanatory reasoning must be suspended.

But it limits what can legitimately be inferred from relative explanatory superiority.

The fact that one explanation appears better than another does not automatically establish that it is an adequate explanation of reality.

The burden is to justify both the comparison and the epistemic significance attributed to the outcome of that comparison.

### The selection of explanatory alternatives

IBE also depends on the construction of the set of explanations being compared.

This issue parallels the problem of specifying a sample space in probabilistic modeling.

A comparison can only evaluate the alternatives that have been included, and its conclusion may depend heavily on how those alternatives are characterized.

Consider a contrast between theism and naturalism.

Theism may be presented as a unified hypothesis involving an omnipotent, omniscient, and benevolent creator.

Naturalism, by contrast, may be represented as the absence of a divine creator, supplemented by the claim that some phenomenon remains unexplained.

But these are not necessarily comparable explanatory specifications.

Theism has been supplemented with a positive account of agency and purpose, while naturalism has been characterized primarily through the absence of that agency.

The resulting comparison may favor theism partly because one side has been provided with an explanatory narrative while the other has not been developed into a corresponding theory.

Yet naturalism is not itself a single complete explanation of every phenomenon.

It is a broad metaphysical framework under which numerous subsidiary theories may be proposed.

A fair comparison requires attention to the explanatory structure actually available under each hypothesis, not merely the contrast between a particular developed theistic narrative and the absence of a presently complete naturalistic account.

The same issue arises in the opposite direction.

A defender of naturalism cannot automatically establish its superiority by comparing a sophisticated physical theory against an undeveloped or arbitrarily restricted conception of theism.

The methodological standard must remain consistent.

The alternatives must be specified at a comparable level of explanatory detail, and the conclusions must be limited to what the comparison establishes.

Otherwise, the apparent superiority of one hypothesis may be generated by the manner in which its competitors were constructed.

This is particularly relevant when a broad metaphysical position is treated as though it were equivalent to one narrowly defined explanatory model.

An argument that shows the superiority of a specific model over another specific model does not automatically establish the superiority of the metaphysical frameworks to which those models belong.

That further inference requires justification.

### Why scientific uses of IBE do not automatically vindicate theistic IBE

A common response is to observe that inference to the best explanation is widely employed in science.

Scientists infer the existence of unobserved entities, mechanisms, and processes because they provide compelling explanations of available evidence.

Why, then, should philosophers be prohibited from making an analogous inference to God?

The objection is misplaced.

The criticism does not depend on a general prohibition against explanatory inference, nor does it establish a categorical restriction against metaphysical hypotheses.

The issue is the methodological basis supporting a particular inference.

In many scientific applications, explanatory hypotheses are constrained by established theory, independent observations, known mechanisms, and the consequences of the proposed explanation.

These constraints help distinguish the proposed explanation from alternative accounts.

For example, an engineering failure investigation may identify a common-cause mechanism that explains several otherwise puzzling component failures.

The explanatory hypothesis becomes credible not merely because it provides a coherent story, but because it is connected to the system's architecture, operating conditions, physical dependencies, maintenance records, and other relevant evidence.

The mechanism may generate implications that can be investigated independently of the observations that initially motivated the hypothesis.

Those independent constraints contribute to the explanatory inference's credibility.

Not all scientific explanations possess the same level of empirical support. Some are provisional, speculative, or weakly constrained. Scientific practice is not immune to the methodological failures criticized here.

But the legitimacy of successful explanatory inference cannot be transferred wholesale to a different context simply by employing the same terminology.

To claim that a theistic explanation is justified because science uses IBE is to overlook the substantive conditions under which particular scientific inferences become credible.

The explanatory inference must be evaluated according to its own assumptions, evidence, constraints, and domain of application.

A philosophical hypothesis does not become evidentially well supported merely because it is presented in the form of an inference commonly used in scientific reasoning.

This is the same distinction developed earlier concerning Bayesian mathematics.

The existence of a legitimate inferential method does not establish the legitimacy of every application of that method.

### When IBE is treated as a Bayesian heuristic

Some defenders of IBE maintain that explanatory virtues function as heuristics for probabilistic confirmation.

On this approach, simplicity, unification, and explanatory power may guide judgments about which hypotheses have greater posterior probability or which observations should be expected under competing theories.

This interpretation connects IBE directly to the issues examined in Sections 3 through 6.

If explanatory superiority is intended to approximate Bayesian confirmation, the argument must explain why the explanatory criteria reliably track the relevant probabilistic relationships.

The problem can be represented schematically.

Let $$Q(H,E)$$ denote a measure of the explanatory quality of hypothesis $$H$$ with respect to evidence $$E$$.

An IBE argument may establish:

$$
Q(T,E)>Q(N,E)
$$

But this does not automatically establish:

$$
P(T\mid E)>P(N\mid E)
$$

Nor does it establish:

$$
P(E\mid T)>P(E\mid N)
$$

The relationship between explanatory quality and probabilistic confirmation must itself be defended.

A hypothesis may possess greater explanatory elegance while having a lower posterior probability because of other relevant evidence or prior considerations.

Likewise, an explanation can exhibit considerable scope while remaining insufficiently constrained to support the observation with a favorable likelihood.

The proposed explanatory virtues may be relevant to probability in some circumstances, but their relevance cannot be assumed independently of the modeling context.

If the argument's claim of explanatory superiority relies on a judgment that the observation is more expected under theism, then the likelihood problem reappears immediately.

If it relies instead on simplicity or unification as guides to prior probability, the problem of prior justification reappears.

If it relies on the existence of a compatible divine intention, the problem of unconstrained auxiliary assumptions reappears.

The move from Bayesian reasoning to IBE therefore does not automatically remove the foundational difficulties.

It may simply relocate them into qualitative judgments concerning explanatory attractiveness.

### When IBE is defended as an independent form of inference

A more substantial response is to deny that explanatory inference needs to be justified through Bayesian probability at all.

On this view, IBE may be a distinct form of rational reasoning whose legitimacy does not depend on assigning priors, specifying likelihood functions, or deriving numerical posterior probabilities.

The present critique must take this possibility seriously.

It would be mistaken to demand Bayesian likelihoods from every explanatory argument while simultaneously acknowledging that IBE may possess an independent epistemic structure.

But rejecting Bayesian reduction does not eliminate the need to justify the inference.

It changes the form that justification must take.

If explanatory superiority independently supports rational belief, we must ask what makes that superiority epistemically significant.

Why should a theory's elegance, simplicity, coherence, or unifying power provide reason to believe that it accurately represents reality?

Under what conditions are these virtues indicators of truth rather than merely pragmatic advantages?

How should competing virtues be weighted when they conflict?

And how do we determine whether a proposed explanation is sufficiently good to warrant belief rather than merely deserving further investigation?

These questions do not require numerical probabilities.

They require a substantive account of the relationship between explanation and epistemic justification.

An IBE defender may attempt to provide that account through broader philosophical considerations concerning rationality, explanatory success, or the reliability of certain inferential practices.

Such defenses must be evaluated on their merits.

But simply invoking IBE does not establish that the necessary justification has been supplied.

The point is especially important for theistic arguments.

If the conclusion is that God exists because theism provides the best explanation of some phenomenon, the argument must establish more than the claim that a theistic explanation is available or intellectually attractive.

It must defend the criteria by which explanatory superiority is assessed and explain why satisfying those criteria warrants the ontological commitment being proposed.

Without that further justification, the appeal to IBE does not resolve the methodological problem.

It merely gives the unsupported inferential transition a different name.

### Explanatory success and ontological commitment

The stakes of this distinction become clearer when we consider the ontological implications of the proposed conclusion.

An explanatory hypothesis can serve several different intellectual purposes.

It may organize existing observations. It may identify a possible mechanism. It may guide future investigation. It may provide a conceptual framework for understanding otherwise disconnected phenomena.

These achievements can be valuable without establishing the literal existence of every entity or process invoked by the explanation.

The move from explanatory usefulness to ontological commitment therefore requires additional justification.

This is especially important when the proposed entity has properties far beyond those directly implicated by the phenomenon.

Suppose, for the sake of argument, that some observation provided evidence favoring intentional design over a specified non-design hypothesis.

Even then, the conclusion that a designer exists would not automatically establish the existence of the God of classical theism.

Additional arguments would be required to connect the alleged designer to attributes such as omnipotence, omniscience, perfect goodness, necessity, or any other substantive theological commitments.

This is not a trivial distinction.

The explanatory properties required to account for an observation may be considerably narrower than the properties attributed to the proposed metaphysical entity.

If an argument establishes only that some form of agency could explain a phenomenon, it cannot simply infer the existence of an agent possessing every attribute associated with a particular religious tradition.

The additional ontological commitments must be independently justified.

The same concern applies more generally to IBE arguments that move from explanatory compatibility to assertions about the ultimate structure of reality.

A hypothesis can possess conceptual or explanatory usefulness without the available evidence warranting its full metaphysical interpretation.

The adequacy of the ontological conclusion depends on the inferential support supplied for the actual attributes being asserted.

This requirement becomes increasingly important as the hypothesis becomes more expansive.

The explanatory reach of a metaphysical account should not be confused with evidence for the full ontology it introduces.

### The absence of a complete alternative does not reverse the burden of justification

A recurring response to methodological criticism is to demand that the critic provide a better explanation.

If the theistic explanation is rejected, what naturalistic explanation should replace it?

But this misunderstands the nature of the objection.

The criticism is not that naturalism has already provided a complete explanation of the phenomenon.

It is that the argument has failed to establish the evidential superiority it claims for theism.

Those are different propositions.

A person can identify a failure in an explanatory inference without possessing a complete alternative explanation.

An engineer who demonstrates that a proposed failure mechanism is unsupported does not thereby become obligated to establish the true mechanism before the original explanation can be rejected as unproven.

Likewise, a statistician who identifies an inadequately specified likelihood model need not provide the correct model to demonstrate that the original inference lacks sufficient justification.

The burden belongs to the claim being advanced.

If an argument asserts that theism is the best explanation of some phenomenon, it must justify the relevant explanatory comparison and the epistemic significance attributed to it.

If it claims that the observation supports the existence of God, it must establish why the proposed explanation warrants that conclusion.

The inability of a critic to provide a complete naturalistic explanation does not supply the missing justification.

Nor should the recognition of explanatory uncertainty be regarded as a failure to reason constructively.

There are circumstances in which the most defensible conclusion is that the available explanatory options are incomplete or insufficiently constrained.

Recognizing that limitation is not equivalent to asserting that all explanations are equally plausible.

It is simply an acknowledgment that the evidence has not established the proposed comparison.

An argument does not become successful because its critic declines to manufacture an alternative answer.

### The methodological conclusion

The preceding analysis reveals a common structure underlying both Bayesian and IBE-based arguments for theism.

A phenomenon is identified as striking, surprising, or insufficiently explained.

A theistic explanation is proposed that renders the phenomenon intelligible under some set of assumptions concerning divine agency or intentions.

Naturalistic explanations are characterized as incomplete, inadequate, or lacking comparable explanatory resources.

The resulting contrast is then used to support a conclusion that the phenomenon provides evidence favoring theism.

But the crucial inferential connections frequently remain unestablished.

The existence of an explanatory gap under naturalism does not establish the improbability of the observation under naturalism.

The availability of a theistic explanation does not establish that the observation was expected under theism.

The apparent simplicity or unity of a hypothesis does not independently establish its truth.

And the superiority of one explanation over a restricted or inadequate collection of alternatives does not demonstrate that the explanation is sufficiently supported to warrant a substantive ontological commitment.

These problems cannot be resolved simply by avoiding numerical probabilities.

The absence of Bayesian notation does not eliminate the burden of justifying the relationship between explanatory considerations and evidential conclusions.

If IBE is understood as a probabilistic heuristic, its application must establish why the relevant explanatory virtues provide reliable guidance concerning the probabilistic relationships at issue.

If IBE is defended as an independent form of inference, it must explain why explanatory superiority warrants rational belief and demonstrate that the proposed explanation satisfies the relevant standards.

In either case, the central question remains the same: what justifies the transition from the availability or attractiveness of an explanation to a substantive conclusion about reality?

For the arguments examined here, that transition has not been adequately established.

The criticism is not that explanatory reasoning is inherently illegitimate, that metaphysical hypotheses can never possess evidential support, or that a complete naturalistic explanation must already be available.

It is that the arguments under consideration frequently treat explanatory possibilities as though they possess evidential authority without independently justifying the criteria and inferential relationships necessary for that conclusion.

This is the same foundational error identified in their explicitly Bayesian counterparts.

The formal vocabulary differs, but the methodological deficiency persists.

**Explanatory compatibility is not evidential confirmation. Explanatory attractiveness is not a substitute for inferential justification. And the absence of a competing explanation does not establish the truth or comparative superiority of the explanation that happens to be available.**

The argument must do more than make theism an intelligible response to an unresolved philosophical problem.

It must demonstrate why the proposed explanation supplies a warranted reason to regard theism as true or comparatively better supported by the evidence.

Where that justification is absent, the claimed evidential conclusion does not follow.

This completes the extension of the methodological critique beyond Bayesian formalism.

The difficulties identified throughout this essay are not peculiar to probability calculations, nor are they resolved by replacing numerical likelihoods with qualitative judgments of explanatory superiority.

They concern the broader requirements of justified inference: the adequacy of the representations employed, the independent support for explanatory assumptions, the treatment of competing hypotheses, and the legitimacy of moving from the explanatory framework to conclusions about reality.

These requirements are not optional conventions peculiar to statistics or engineering. They are part of what distinguishes a disciplined inferential assessment from a speculative explanation whose evidential significance has not been established.

**The ability to formulate an explanation is not the same as having evidence for it. And the capacity to accommodate an observation is not sufficient to establish that the observation favors the hypothesis.**

The final part of this essay will consolidate the methodological critique into a general argument, clarify the precise scope of its conclusion, and address the principal objections that might be raised against it.

The resulting position does not require assigning any probability to theism or naturalism. It does not require demonstrating that either metaphysical framework is true. It requires only that arguments claiming evidential support meet the methodological burden necessary to establish that support.

Where the burden has not been met, the purported inference has not been established.

That is the central failure shared by the arguments examined here.

# Part V — The General Methodological Challenge

## 10. The Failure Occurs Before the Probability Calculation

The preceding analysis has identified a recurring methodological failure in probabilistic and explanatory arguments for the existence of God. Across cosmological fine-tuning, psychophysical harmony, and inference to the best explanation, the same general pattern emerges: a phenomenon is identified as striking or insufficiently explained, a set of hypothetical alternatives is constructed, and the resulting contrast is used to support a substantive evidential conclusion favoring theism. Bayesian arguments express that conclusion through prior probabilities, likelihood ratios, and posterior updates. IBE arguments typically appeal to explanatory virtues, comparative plausibility, or the apparent superiority of a theistic explanation.

Despite these differences in formal presentation, the central difficulty remains substantially the same. The inferential relationships required to establish the advertised evidential conclusions have not been adequately justified.

The problem is not that the arguments necessarily violate the axioms of probability theory. Nor is it that their conclusions are logically impossible, or that every probabilistic comparison involving metaphysical hypotheses must be illegitimate. The difficulty is more fundamental: the arguments frequently assume the validity of the probabilistic or explanatory relationships that they are supposed to establish.

The construction of a possibility space is treated as though it establishes a domain of probabilistic alternatives. The numerical predominance of hypothetical outcomes is treated as though it establishes relative probability. The absence of a complete naturalistic explanation is treated as though it establishes improbability under naturalism. The availability of a theistic explanation is treated as though it establishes a favorable likelihood under theism.

These transitions are not licensed by the concepts or observations from which they begin.

A probability model can be mathematically coherent without being epistemically justified. An explanatory narrative can be intelligible without being evidentially discriminating. And a comparison can produce a determinate result within a stipulated framework without establishing that the framework provides an appropriate basis for conclusions about reality.

The fundamental failure therefore precedes the calculation.

Before a likelihood ratio can establish comparative confirmation, the likelihoods must be justified. Before a probability measure can support a substantive inference, its relationship to the relevant alternatives must be defended. Before explanatory superiority can warrant ontological commitment, the standards governing that superiority and its epistemic implications must be established.

These requirements are not additional demands imposed after an argument has already succeeded. They concern the conditions under which the argument could succeed in the first place.

### Formal validity is not inferential adequacy

The most important distinction developed throughout this essay is between formal validity within a model and the epistemic adequacy of applying that model to a particular phenomenon.

In Bayesian reasoning, the posterior odds between two hypotheses can be expressed as:

$$
\frac{P(T\mid E)}{P(N\mid E)}
=
\frac{P(E\mid T)}{P(E\mid N)}
\cdot
\frac{P(T)}{P(N)}
$$

Assuming the relevant probabilities and ratios are well-defined, this relationship follows from the probability calculus.

Its mathematical correctness does not depend on whether the hypotheses concern component failures, medical diagnoses, cosmological theories, or the existence of God.

But the equation does not specify its own inputs.

It does not determine which hypotheses constitute the appropriate alternatives, which observations should be included in the evidence, which background assumptions are relevant, or what probability distributions should be assigned to the phenomena under consideration.

These are separate methodological questions.

In a well-supported application, the probabilistic model is constrained by information relevant to the target phenomenon. That information may include empirical observations, theoretical relationships, mechanistic knowledge, established symmetries, independently justified background assumptions, or other defensible sources of epistemic constraint.

The precise requirements vary across applications. A Bayesian assessment of a historical proposition need not resemble a reliability analysis of a mechanical component. A philosophical assessment of rational credence need not presuppose an objectively random physical process.

Nevertheless, substantive probability assignments require some account of why those assignments are appropriate to the inferential question.

Without that account, Bayes' theorem supplies only a conditional relationship among stipulated quantities.

This distinction is particularly important when the mathematical apparatus generates a dramatic result.

Suppose an argument assigns a very low likelihood to some observation under naturalism and a comparatively high likelihood under theism. The resulting Bayes factor may strongly favor theism.

But the strength of that conclusion derives entirely from the assigned likelihoods.

If their values are speculative, their comparison is speculative.

If their ordering is unsupported, the direction of the purported confirmation is unsupported.

And if the models generating those likelihoods have not been adequately specified, the calculation cannot independently establish their applicability.

A formally valid Bayesian update transmits the assumptions of the probabilistic model into its conclusion. It does not validate those assumptions.

This is why criticisms focused exclusively on the numerical magnitude of the proposed probabilities can miss the more fundamental issue.

The difficulty is not necessarily that the likelihood ratio should be ten rather than one hundred, or that a prior probability should be somewhat larger or smaller.

The question is whether the argument has established a defensible basis for assigning any particular likelihood ordering to the competing hypotheses.

Where it has not, the apparent precision or decisiveness of the calculation is not an evidential achievement.

### The central methodological argument

The criticism can be consolidated into an explicit argument.

**Premise 1 — Evidential claims require justified inferential relationships.**

An argument that claims an observation provides comparative evidence for one hypothesis over another must establish an adequate basis for that comparative relationship.

The precise form of justification depends on the inferential framework employed. For a Bayesian argument, this involves the relevant probabilistic models and likelihood comparisons. For an independently defended form of IBE, it involves the explanatory criteria and the epistemic relationship between explanatory superiority and rational acceptance.

In either case, merely asserting that an observation supports a hypothesis does not establish that support.

**Premise 2 — Mathematical coherence is insufficient for substantive probabilistic justification.**

The satisfaction of probability axioms and the correct application of conditional probability rules do not independently establish that a selected probability model adequately represents the phenomenon or epistemic uncertainty under investigation.

A substantive probabilistic inference requires defensible assumptions concerning its hypotheses, relevant alternatives, probability assignments, and domain of application.

**Premise 3 — Constructed possibility spaces do not determine probability measures.**

The identification of conceivable, metaphysically possible, or epistemically open alternatives does not independently establish their relative probabilities.

The individuation of alternatives, the selection of a measure, and the interpretation of that measure introduce additional assumptions that require justification.

The apparent abundance of hypothetical alternatives cannot substitute for this justification.

**Premise 4 — Explanatory compatibility does not independently establish comparative confirmation.**

A hypothesis may accommodate or render intelligible an observation without making that observation more probable than competing hypotheses do.

Likewise, the absence of an adequate explanation under a competing hypothesis does not independently establish that the observation was improbable under that hypothesis.

Comparative evidential support requires additional justification beyond explanatory availability or incompleteness.

**Premise 5 — The arguments examined rely on inadequately justified transitions of precisely these kinds.**

In fine-tuning arguments, physical sensitivity and restricted parameter ranges are used to motivate claims of extreme improbability without adequately establishing the relevant probability measures and their applicability.

In psychophysical harmony arguments, speculative spaces of alternative phenomenal and physical relationships are used to motivate epistemic probability judgments without adequately establishing the coherence, individuation, or relative weighting of those alternatives.

In both cases, favorable theistic likelihoods depend on additional assumptions concerning divine intentions and creative preferences whose probabilistic significance has not been independently established.

Related IBE arguments frequently rely on explanatory compatibility or the absence of competing explanations without adequately defending the inferential relationship between those considerations and the claimed evidential conclusion.

**Premise 6 — An unsupported probabilistic or explanatory comparison cannot establish the evidential conclusion that depends on it.**

If the decisive comparative relationship has not been justified, the conclusion that the evidence favors the proposed hypothesis has not been demonstrated by that argument.

This remains true even when the formal reasoning is internally coherent or the proposed explanation is conceptually intelligible.

**Conclusion — The arguments examined have not established their advertised comparative evidential support for theism.**

Their failure is not primarily a matter of numerical inaccuracy. It concerns the absence of adequate justification for the probabilistic or explanatory relationships on which the proposed inference depends.

The conclusion is deliberately methodological.

It does not assign a competing probability to naturalism. It does not establish that theism is false. It does not claim that the observed phenomena are explanatorily insignificant.

It establishes that the arguments under examination have not justified the evidential conclusions they purport to demonstrate.

### The burden of proof belongs to the claimed inference

A significant consequence of this methodological critique concerns the burden of justification.

Defenders of probabilistic theistic arguments may respond to objections by asking critics to provide alternative probability estimates.

If the critic rejects the claimed improbability of fine-tuning under naturalism, what probability should be assigned instead?

If the critic disputes the alleged improbability of psychophysical harmony, what distribution over psychophysical mappings would be more appropriate?

If the critic rejects the explanatory superiority of theism, what complete naturalistic explanation should replace it?

These questions may be relevant to a separate project of developing competing explanations or probability models. They are not necessary for evaluating whether the original argument has established its conclusion.

An inference can fail without a competing inference being available.

Consider an engineering analyst who presents a risk assessment based on an unjustified failure distribution. A reviewer demonstrates that the model neglects relevant dependencies, employs an arbitrary reference class, or assumes a failure mechanism that has not been established.

The reviewer does not need to determine the true probability of failure before concluding that the presented assessment lacks adequate justification.

The methodological criticism concerns the relationship between the analysis and the conclusion it claims to support.

The same principle applies to Bayesian arguments for God.

If an argument asserts:

$$
P(E\mid T)>P(E\mid N)
$$

then the argument bears the burden of justifying that inequality.

A critic who demonstrates that the proposed assumptions do not warrant the inequality has identified a deficiency in the argument.

The critic is not subsequently obligated to establish:

$$
P(E\mid N)>P(E\mid T)
$$

Nor must the critic demonstrate:

$$
P(E\mid T)=P(E\mid N)
$$

These are different claims, each requiring its own justification.

The failure to establish a favorable likelihood ordering for theism does not establish an unfavorable ordering. It establishes that the proposed inference has not been supported.

This distinction is essential because probabilistic criticism is sometimes incorrectly interpreted as a competing probabilistic thesis.

To reject an unsupported likelihood is not to endorse its opposite.

To challenge an arbitrary probability measure is not to assert a different measure.

To recognize the incompleteness of current explanatory knowledge is not to claim that the relevant phenomenon has no explanation.

The present argument does none of these things.

It concerns the evidential burden attached to a specific inference.

A proponent cannot discharge that burden by demanding that critics answer a different question.

### The distinction between an unestablished probability and an unfavorable probability

The conclusion that a probability has not been established must also be distinguished from the conclusion that the probability is low, high, or indeterminate in some formally specified sense.

In a probabilistic model, an event may possess a well-defined probability even when an analyst does not know its value. In other cases, multiple probability measures may be admissible because the model is underdetermined. Still other cases may involve uncertainty concerning which model is applicable or whether the event has been adequately specified.

These situations should not be conflated.

When the present critique states that the relevant probability has not been established, it does not necessarily assert that the probability is mathematically undefined.

One can construct coherent probability spaces over the relevant hypotheses. A subjective Bayesian can assign degrees of belief to theism, naturalism, fine-tuning, or psychophysical harmony. A philosophical model can introduce stipulated likelihoods and determine what follows from them.

But the existence of such assignments does not independently establish their epistemic appropriateness.

The criticism concerns the absence of adequate justification for treating a particular assignment as informative about the evidential relationship under examination.

This distinction prevents an important misunderstanding.

The claim is not that probability theory cannot formally represent metaphysical uncertainty.

It is that the specific probabilistic representations employed in the arguments examined have not been sufficiently justified to establish the conclusions attributed to them.

Likewise, the failure to establish comparative confirmation does not demonstrate evidential neutrality.

Within Bayesian confirmation theory, evidential neutrality has a particular meaning. Under suitable conditions, evidence is neutral between two hypotheses when their likelihoods are equal:

$$
P(E\mid T)=P(E\mid N)
$$

But if the likelihoods have not been established, their equality has not thereby been demonstrated.

The absence of a justified comparison is not itself a comparison.

It is a recognition that the required evidential relationship remains unsupported.

This is why the criticism can be maintained without adopting a particular alternative metaphysical position.

One may remain uncertain about theism, naturalism, or the ultimate explanation of consciousness while rejecting an argument that purports to settle their comparative evidential standing through unjustified probability assignments.

There is no inconsistency in doing so.

### The failure of model construction cannot be repaired by formal sophistication

A recurring temptation in philosophical probabilistic reasoning is to regard increasing mathematical sophistication as a response to concerns about rigor.

A simple argument based on intuitive probabilities may be reformulated using conditional probability. Its probabilities may then be incorporated into a Bayesian network, a hierarchical model, or a more elaborate framework involving distributions over auxiliary hypotheses.

Such developments can make the assumptions and relationships within an argument more explicit.

They may also reveal previously unrecognized dependencies or identify conditions under which the conclusion would hold.

These are genuine benefits of formalization.

But greater formal complexity does not independently justify the model's relationship to reality.

A sophisticated mathematical model can be constructed over an arbitrarily defined possibility space.

It can contain internally coherent distributions whose relationship to the underlying phenomenon remains unestablished.

It can incorporate uncertainty over hypothetical subsidiary models without justifying the selection or weighting of those models.

And it can produce a precise posterior conclusion whose substantive implications depend entirely on unsupported assumptions.

The problem is not resolved by making the calculation more elaborate.

It is resolved, if at all, by providing the missing justification for the model.

This is a central lesson from applied probabilistic methodology.

Statistical sophistication is not equivalent to model adequacy.

A complex reliability model may be less credible than a simpler model if the former introduces unsupported dependencies or assumptions that cannot be defended.

A Bayesian analysis may be mathematically elegant while remaining highly sensitive to arbitrary prior choices.

And a model can be internally consistent while failing to represent the mechanisms or uncertainties relevant to the decision under consideration.

The corresponding criticism of probabilistic theistic arguments is therefore not a complaint that philosophers need to learn more advanced mathematics.

It is a complaint that the mathematical formalism is being asked to perform a justificatory function it cannot perform.

Probability theory can determine what follows from a model.

It cannot, by itself, establish that the model's assumptions are an adequate representation of reality.

**Formal sophistication cannot compensate for the absence of methodological justification.**

The inferential burden remains at the level of model construction, specification, and application.

### Why the criticism is not an argument against subjective Bayesianism

Another possible misunderstanding is that the critique depends on treating probability exclusively as objective physical chance.

This would make the criticism unnecessarily narrow.

Subjective Bayesianism permits probabilities to represent rational or personal degrees of belief rather than frequencies or objective propensities. It therefore allows probabilistic reasoning about propositions for which no repeatable physical experiment is available.

That framework is not inherently incompatible with the methodological demands developed here.

A subjective Bayesian may legitimately investigate the coherence of credences, update beliefs in response to evidence, and examine the implications of particular prior commitments.

The methodological problem arises when the outputs of a subjective probability model are presented as publicly justified evidential conclusions without an adequate defense of the assignments determining those outputs.

A coherent belief is not necessarily a well-supported belief.

Likewise, a conditional probability can be coherent without the underlying conditional judgment being adequately justified.

There are circumstances in which multiple agents may assign different coherent probabilities to the same proposition because their background information, inferential commitments, or permitted credence functions differ.

The existence of such disagreement does not automatically invalidate subjective Bayesianism.

But it does limit what follows from a particular probabilistic argument.

If a theistic likelihood advantage depends on a subjective judgment that is not independently constrained, then the argument may demonstrate only that the observation favors theism relative to that judgment.

To establish the stronger conclusion that the observation provides generally defensible evidential support for theism, further justification is required.

The distinction is between expressing a coherent probabilistic perspective and demonstrating that others have adequate epistemic reasons to adopt it.

The latter cannot be established simply by invoking the formal legitimacy of the former.

A defender might respond that substantive prior and likelihood judgments can be rational without being uniquely determined by evidence.

That is correct.

The present criticism does not require every rational probability assignment to be uniquely determined.

It requires the argument to establish enough justification for its claimed conclusion.

If a range of defensible probability assignments supports the same qualitative inference, that may provide a basis for a robust evidential claim.

If the available information fails to constrain the relevant assignments sufficiently to establish even the direction of the comparison, then the claimed likelihood advantage remains unsupported.

The issue is not whether subjective probability is legitimate.

It is whether the specific subjective judgments employed can bear the evidential weight placed upon them.

### Why ignorance does not generate a likelihood

One of the most important lessons of the preceding case studies concerns the treatment of explanatory ignorance.

In both fine-tuning and psychophysical harmony, the argument begins with phenomena whose ultimate explanation is disputed or incomplete.

We do not possess a universally accepted account of why the fundamental physical constants have their observed values.

We do not possess a settled account of the metaphysical relationship between phenomenal consciousness and physical organization.

These limitations are genuine features of our current explanatory situation.

But the absence of complete knowledge does not itself determine a probability distribution over alternative explanations or possible outcomes.

The transition from ignorance to improbability requires additional assumptions.

In fine-tuning, these assumptions may concern the independent variability of physical constants, the selection of parameter ranges, and the probability measure over those ranges.

In psychophysical harmony, they concern the independent individuation of phenomenal and physical states, the coherence of alternative mappings, and their relative epistemic probabilities.

In both cases, the alleged surprise depends on more than the existence of unexplained facts.

It depends on a constructed representation of what might have occurred instead.

The relevant question is whether that representation is justified.

Without an adequate answer, the argument risks treating our ignorance of the actual explanation as evidence that the observed phenomenon was unlikely.

But these are different epistemic states.

Not knowing why something occurs is not equivalent to knowing that it was improbable.

A missing explanation does not supply a probability measure.

And an unexplained regularity does not become evidence of design merely because one can imagine many alternative arrangements in which the regularity would be absent.

The alleged improbability must be established independently of the explanatory gap.

Otherwise, the inference derives its apparent evidential force from the very ignorance it claims to resolve.

### The epistemic cost of unconstrained explanatory hypotheses

The preceding analysis also reveals why unconstrained explanatory flexibility is not automatically an evidential advantage.

A broad metaphysical hypothesis may accommodate numerous possible outcomes by invoking different subsidiary assumptions.

In the case of theism, these may concern divine intentions, creative preferences, moral purposes, or the means through which a deity actualizes particular states of affairs.

Such assumptions can make a wide range of observations intelligible.

But their evidential significance depends on whether they are independently supported and appropriately incorporated into the hypothesis.

Without such constraints, a favorable explanation can be selected after the observation is known.

This raises an important methodological problem.

The fact that an agent could have intended an observed result does not establish that the agent would probably have intended it.

Nor does it establish that the agent existed.

A hypothetical intentional explanation may be compatible with the data while possessing little capacity to distinguish between alternative possible observations.

This does not mean that intentional explanations are inherently weak.

In ordinary scientific and social inquiry, intentional explanations can be highly informative when agents, preferences, incentives, capabilities, and circumstances are sufficiently constrained by independent information.

The problem arises when the agent's existence and relevant preferences are themselves part of the disputed explanatory hypothesis.

Under those circumstances, the explanatory model can become underdetermined at multiple levels.

The phenomenon is explained by reference to an intention, but the intention is inferred primarily from the phenomenon, and the agent possessing the intention is then inferred from the apparent explanatory success.

Without additional constraints, this chain of reasoning risks presenting explanatory accommodation as evidential confirmation.

The issue is not that the conclusion must be false.

It is that the explanation has not established the discriminating relationship necessary to support the conclusion.

### The methodological asymmetry revisited

We can now return to the practical asymmetry that motivated the essay.

In applied probabilistic modeling, the analyst is expected to justify the representation of the system, the assumptions governing uncertainty, the data and theoretical information used, and the conditions under which the resulting assessment may reasonably inform decisions.

The standards are not always satisfied perfectly.

Models can be misspecified, data can be inadequate, and analysts can place excessive confidence in conclusions unsupported by their assumptions.

Applied statistics and engineering are not immune to methodological error.

But these possibilities reinforce rather than undermine the distinction between formal calculation and justified inference.

The purpose of methodological scrutiny is to identify precisely such failures.

Suppose a reliability analyst presents a catastrophic failure probability derived from an arbitrary space of imagined system configurations.

The analyst has not established how those configurations relate to the system's actual operation.

The probabilities have been selected through intuition.

Relevant dependencies and uncertainty about the model remain unaddressed.

The analyst nevertheless maintains that the result is meaningful because the probability assignments are coherent and the calculations are mathematically correct.

The methodological criticism would be immediate.

Correct arithmetic cannot establish that the assessment represents the system's actual risk.

Now consider a philosophical argument that constructs a speculative space of alternative universes or psychophysical mappings, assigns relative probabilities through intuition or contested theoretical assumptions, and then claims that the observed outcome provides strong evidence for God.

The epistemic problem is structurally similar.

The mathematical calculation may be correct.

The hypothetical alternatives may be conceptually interesting.

The explanatory narrative may be intelligible.

But the relationship between the probabilistic representation and the phenomenon remains insufficiently justified.

The argument cannot derive substantive evidential authority merely from the formal legitimacy of its procedure.

The standards of applied reasoning need not be transplanted mechanically into metaphysics. There are important differences in the available evidence, the nature of the hypotheses, and the appropriate methods of inquiry.

Nevertheless, the general requirement of methodological accountability persists.

The legitimacy of an inference depends on more than its logical or mathematical form.

It also depends on whether the assumptions used to connect that form to the target phenomenon are defensible.

That is the fundamental asymmetry this essay has sought to expose.

### What the critique establishes—and what it does not

The scope of the conclusion must be stated precisely.

The argument developed here does not demonstrate that God does not exist.

It does not establish that naturalism is true, or that naturalism possesses greater prior or posterior probability than theism.

It does not show that all metaphysical hypotheses are inherently unsuitable for probabilistic analysis.

Nor does it establish that explanatory reasoning is illegitimate whenever complete empirical validation is unavailable.

Those conclusions would require additional arguments.

The present criticism is directed at a specific class of inferential procedures and the evidential claims made on their behalf.

The arguments examined purport to show that observations such as fine-tuning and psychophysical harmony favor theism over naturalistic alternatives.

They do so by relying on speculative alternatives, inadequately justified probability measures, unconstrained likelihoods, or explanatory comparisons whose epistemic significance has not been established.

The conclusion is that these arguments have not demonstrated the comparative evidential support they claim.

This is a substantive result.

An argument whose purpose is to establish confirmation has not achieved that purpose if the relation of confirmation remains unsupported.

The fact that its conclusion might ultimately be true does not vindicate the inference.

Likewise, the fact that some future theory might establish a defensible likelihood comparison does not supply the missing justification for the argument presently offered.

An argument must be evaluated according to the premises and inferential relationships it actually establishes, not according to hypothetical improvements that have yet to be provided.

This distinction also prevents the critique from becoming an argument from ignorance in the opposite direction.

We should not infer that theism is improbable simply because theistic likelihoods have not been established.

We should not infer that naturalism is probable merely because theism has not received the claimed evidential support.

And we should not infer that a phenomenon has no explanation because presently proposed explanations are inadequate.

The appropriate response to insufficient justification is to recognize the limits of the inference.

There is no methodological obligation to replace an unsupported conclusion with another unsupported conclusion.

### The general principle of epistemic accountability

The critique ultimately rests on a principle that extends far beyond philosophy of religion.

When a mathematical or explanatory framework is used to support a substantive conclusion about reality, the inferential relationship between the framework and the phenomenon must be justified.

The requirements of justification will vary according to the inquiry.

An engineering model may rely on empirical measurements, physical mechanisms, and established reliability methods.

A scientific theory may rely on mathematical structure, explanatory constraints, observational consistency, and independent empirical predictions.

A philosophical argument may rely on conceptual analysis, background knowledge, modal reasoning, theoretical virtues, or principles concerning rational credence.

These methods are not interchangeable.

But none is exempt from the requirement to explain why its inferential procedure warrants the conclusion drawn from it.

The mere availability of a mathematical representation does not establish its evidential significance.

The mere coherence of a probability assignment does not establish its epistemic appropriateness.

The mere existence of an explanatory narrative does not establish its superiority.

And the absence of a complete alternative does not establish that the preferred explanation is true.

These are not unusual or excessively demanding standards.

They are general principles of responsible inference.

The problem with the probabilistic arguments for theism examined here is that the decisive inferential transitions repeatedly fail to satisfy them.

The existence of hypothetical alternatives is treated as though it establishes probability.

The existence of an explanatory gap is treated as though it establishes improbability.

The existence of a compatible divine purpose is treated as though it establishes an expectation under theism.

And the formal combination of these assumptions is presented as though it demonstrates comparative evidence for the existence of God.

But the assumptions do not acquire epistemic authority through their inclusion in a formal argument.

What is required is an independent justification for the relationships on which the inference depends.

Where that justification is absent, the resulting conclusion is not established.

### Conclusion: the inference was never earned

The central failure of these arguments is therefore not located in the final step of the Bayesian calculation.

It occurs earlier, during the construction of the alternatives, the selection of probability measures, the specification of likelihoods, and the interpretation of explanatory relationships.

The argument may eventually arrive at a mathematically coherent result. But the coherence of that result does not establish the legitimacy of the assumptions required to obtain it.

A life-permitting universe may occupy a restricted region of some theoretical parameter space. That does not establish its probability under naturalism.

A harmonious relationship between consciousness and physical organization may appear exceptional relative to a collection of imagined alternative mappings. That does not establish that the actual relationship was improbable.

A divine creator may be imagined as possessing reasons to produce the observed phenomena. That does not establish the likelihood of those phenomena under theism.

And the apparent explanatory superiority of a theistic narrative does not independently establish the evidential significance of that superiority.

Each inference requires justification that cannot be supplied merely by repeating the original observation, expanding the space of hypothetical alternatives, or expressing the conclusion through Bayesian notation.

The arguments examined have not demonstrated that the evidence favors theism. They have constructed frameworks under which the evidence can be made to favor theism, without adequately establishing why those frameworks should be accepted as evidentially authoritative.

That distinction is decisive.

It is the difference between showing what follows from stipulated assumptions and demonstrating what the available evidence warrants us in believing.

The former can be mathematically legitimate while the latter remains unsupported.

The entire methodological critique can therefore be summarized in a single principle:

**The right to employ a probabilistic or explanatory framework is not the same as having established that the framework warrants a substantive conclusion about reality.**

This principle does not prohibit philosophical probabilistic reasoning.

It requires that such reasoning satisfy the justificatory burden created by its own evidential ambitions.

If a philosopher claims that some observation provides comparative evidence for God, then the inferential relationship supporting that claim must be established.

If that relationship depends on a probability measure, the measure must be justified.

If it depends on a likelihood ordering, the ordering must be defended.

If it depends on explanatory superiority, the criteria and epistemic significance of that superiority must be established.

And if the relevant assumptions remain too weakly constrained to determine the proposed comparison, the appropriate conclusion is that the comparison has not been established.

The critic need not demonstrate that the opposite conclusion is true.

The critic need only identify the failure of the proposed argument to support its own conclusion.

This is the central methodological result of the analysis.

**The problem with these arguments is not that they calculate the wrong probability. It is that they have not established the grounds on which the probability they invoke should be accepted as evidence.**

The probability was never established.

And without that probability—or another independently justified inferential basis—the advertised evidential conclusion does not follow.

# Part VI — Anticipating Objections

The methodological criticism developed throughout this essay is likely to encounter several objections. Some concern the interpretation of probability, particularly the legitimacy of subjective Bayesian credences and epistemic probabilities. Others concern the applicability of statistical and engineering standards to philosophical inquiry. Still others challenge whether numerical probability assignments are necessary, whether conceivability can support probabilistic reasoning, or whether inference to the best explanation provides an independent route to theistic confirmation.

These objections deserve careful examination because several identify legitimate distinctions. Probability need not always represent objective physical chance. Bayesian reasoning can be applied to unique events. Rational credences need not be precisely determined by available evidence. Philosophical explanations need not always generate quantitative predictions. And explanatory inference cannot automatically be reduced to the methods of reliability engineering.

But acknowledging these points does not establish that the probabilistic and explanatory arguments examined in this essay are methodologically adequate.

The distinction is between defending the general legitimacy of an inferential framework and justifying a particular application of that framework.

Demonstrating that Bayesian probability can represent rational uncertainty does not establish that a proposed likelihood ratio between theism and naturalism is warranted. Demonstrating that epistemic possibilities can receive probability assignments does not justify a distribution over imagined psychophysical mappings. And demonstrating that explanatory virtues can be epistemically relevant does not establish that a particular theological explanation possesses the evidential significance attributed to it.

The following objections therefore need to be assessed according to whether they actually supply the missing inferential justification.

## Objection 1: Bayesian probability represents subjective degrees of belief, not objective physical frequencies

A defender may argue that the criticism mistakenly imposes requirements appropriate to objective chance or empirical frequency estimation upon subjective Bayesian reasoning.

Bayesian probabilities need not correspond to frequencies in repeated trials. They can represent degrees of belief concerning unique events, historical claims, scientific hypotheses, and metaphysical propositions. An individual can assign a probability to the existence of God without supposing that universes have been repeatedly sampled or that divine existence is the outcome of a physical randomizing mechanism.

Under subjective Bayesianism, the relevant requirement is that credences satisfy appropriate coherence constraints and be updated consistently in response to evidence.

Consequently, the objection continues, philosophical arguments for theism need not identify a physical probability distribution governing the selection of universes or psychophysical mappings. They need only identify rationally permissible epistemic probabilities.

### Response: Coherence does not establish evidential authority

The objection correctly distinguishes subjective probability from objective physical chance, but it does not address the central methodological criticism.

The present argument does not require every probability judgment to be grounded in observed frequencies or an identifiable stochastic process. It does not deny that coherent credences can be assigned to metaphysical propositions.

The issue is whether a particular set of credences has been adequately justified as a basis for the evidential conclusion being asserted.

Coherence constrains relationships among probabilities. It does not, by itself, establish which coherent probability assignments an individual ought to adopt.

Consider two agents who possess the same relevant evidence but assign different conditional probabilities to an observation under theism and naturalism.

One judges that the observation strongly favors theism. Another judges that it is evidentially neutral. A third judges that it favors naturalism.

Depending on their underlying assignments, all three may satisfy the probability axioms.

The existence of a coherent assignment favoring theism therefore does not demonstrate that the evidence favors theism in a sense that others have adequate reason to accept.

To establish that stronger conclusion, the argument must supply reasons for the relevant probability assignments.

This is especially important because Bayesian arguments for theism are ordinarily presented as more than descriptions of the author's personal credences. They purport to demonstrate that observations concerning fine-tuning, consciousness, or other features of reality provide genuine evidential support for the existence of God.

Such a claim requires an account of why the observation possesses the asserted likelihood relationship to the competing hypotheses.

If the proposed likelihoods depend on unconstrained judgments about divine intentions or arbitrary distributions over hypothetical alternatives, their subjective coherence does not resolve the problem.

The distinction can be expressed as follows:

A coherent credence assignment establishes what an agent can consistently believe.

An adequately justified evidential argument must establish why the relevant probability assignments should be accepted for the inferential purpose at hand.

These are different achievements.

Nor does this criticism demand unique rational credences. It is possible that more than one probability assignment is defensible given the available information. Nevertheless, an argument claiming a particular direction of evidential support must justify that direction.

If defensible assignments yield conflicting likelihood orderings, the argument cannot simply select the ordering favorable to theism and treat it as established.

**Subjective probability changes the interpretation of the probability assignment. It does not eliminate the responsibility to justify the assignment when using it to support a substantive conclusion about reality.**

## Objection 2: A probability model does not require a physical data-generating process

A closely related objection concerns the role of data-generating processes and physical mechanisms.

In statistics and reliability engineering, probability models frequently represent physical processes whose outcomes vary according to identifiable mechanisms. But not every legitimate application of probability involves such a process.

Probabilistic reasoning can concern uncertainty about a fixed but unknown quantity, the truth of a proposition, or the outcome of a unique historical event.

Consequently, a defender may argue that it is inappropriate to demand a mechanism generating universes or psychophysical relationships before assigning epistemic probabilities to them.

### Response: A generating mechanism is one possible source of justification, not a universal requirement

This objection also identifies a legitimate distinction, but it addresses a requirement the present critique does not impose.

A physical data-generating mechanism is not a universal prerequisite for meaningful probability.

In some applications, empirical frequencies provide important constraints. In others, probabilities may be informed by theoretical symmetries, background knowledge, established relationships, or defensible principles governing rational uncertainty.

The methodological requirement is not that every probabilistic assessment identify a physical randomizing mechanism.

It is that the selected probabilistic representation be justified in relation to its intended interpretation and application.

A probability model can be constructed without reference to a physical chance process. But the absence of such a process does not itself justify any particular distribution.

Suppose an argument defines a collection of hypothetical universes and assigns a uniform distribution over their physical parameters.

The objection that no physical universe-generating mechanism has been identified may be inapplicable if the distribution is intended to represent epistemic uncertainty.

But a different question remains: why should epistemic uncertainty be represented by that uniform distribution?

What principles establish its relevance?

What background assumptions justify its domain, parameterization, and weighting?

Similarly, the assignment of epistemic probabilities to alternative psychophysical mappings does not require those mappings to have been generated by an objective lottery.

Nevertheless, the argument must explain why the specified mappings constitute the appropriate alternatives and why their assigned probabilities are rationally warranted.

The distinction between physical and epistemic probability does not erase the distinction between justified and arbitrary epistemic probability.

An analyst can legitimately represent uncertainty about an unknown fixed quantity. But the mathematical possibility of doing so does not make every prior distribution equally defensible.

The proper question is therefore not whether a physical randomizing process exists.

It is whether the probability model has an adequate epistemic foundation.

**The absence of a required physical chance mechanism does not entail the absence of any requirement to justify the probability measure.**

## Objection 3: Epistemic possibility is sufficient; metaphysical possibility need not be established

Defenders of psychophysical harmony may respond that the argument does not require alternative psychophysical mappings to be metaphysically possible.

Even if consciousness is necessarily related to physical states, multiple accounts of those relationships may remain compatible with our present knowledge.

The argument may therefore employ a space of epistemically possible alternatives rather than metaphysically possible worlds.

Within that space, epistemic probabilities can be assigned to different proposed relationships between phenomenal and physical properties.

The argument's purported surprise arises from the observation that the actual harmonious relationship appears exceptional among the alternatives that remain epistemically open.

### Response: Epistemic openness does not supply a probability distribution

This response correctly identifies a distinction between metaphysical and epistemic possibility.

But that distinction does not establish the claimed improbability.

Suppose several psychophysical identity hypotheses remain compatible with our current knowledge. We may be unable to determine which, if any, is correct.

The existence of that uncertainty does not determine how credence should be distributed among the hypotheses.

In particular, it does not establish that each hypothesis deserves equal probability, that the simplest hypotheses are necessarily more probable, or that harmonious relationships deserve substantially less probability than disharmonious alternatives.

Those are additional claims.

The response also leaves unresolved the individuation of the relevant epistemic possibilities.

What counts as a distinct psychophysical identity hypothesis?

Why should phenomenal and physical properties be represented through the selected collection of states?

Which alternative descriptions are genuinely compatible with the relevant background knowledge?

How should hypotheses differing in theoretical structure, explanatory commitments, or relationships among properties be weighted?

These questions are not resolved by classifying the alternatives as epistemically possible.

An epistemic possibility space is defined relative to a body of information. Its structure therefore depends on what information is included and how alternative descriptions are represented.

The mere availability of multiple descriptions does not establish a privileged distribution over them.

This becomes especially important when the argument depends on their numerical abundance.

Suppose the harmonious relationship is represented as one mapping among an enormous number of disharmonious permutations.

The resulting counting argument may appear powerful.

But the relevant probability depends on whether the permutations represent appropriate elementary alternatives and whether there is a justified measure over them.

A different representation of the epistemic alternatives may yield a different counting structure.

A different theory of consciousness may constrain the alternatives in different ways.

A different epistemic probability model may assign substantial weight to harmonious relationships.

The argument must provide reasons for preferring its representation and measure.

There is an additional distinction concerning a posteriori necessity.

Something may be metaphysically necessary while remaining epistemically uncertain because its necessity is not discoverable through conceptual analysis alone.

The fact that we cannot derive a psychophysical identity a priori does not demonstrate that the identity was probabilistically unlikely.

Our ignorance of a necessary relationship is not equivalent to evidence that the relationship could easily have been otherwise.

Nor does it establish that the correct identity should have received low prior credence.

The latter claim requires independent epistemic principles.

Consequently, the appeal to epistemic possibility preserves the formal possibility of constructing a Bayesian model, but it does not establish that the model is appropriate.

**The distinction between epistemic and metaphysical possibility prevents one objection only by leaving the central probabilistic objection unanswered.**

The question remains why the proposed alternatives and their relative probabilities should be accepted as the basis for a likelihood comparison.

## Objection 4: Precise probabilities are unnecessary; qualitative likelihood comparisons are sufficient

A defender may argue that the criticism demands an inappropriate level of numerical precision.

Probabilistic arguments for theism need not determine exact prior probabilities or likelihood ratios.

They may require only the qualitative judgment that some observation is more probable under theism than under naturalism.

For example, an argument from fine-tuning might claim that life-permitting conditions are substantially more expected under theism, without attempting to calculate their precise probabilities.

Likewise, the argument from psychophysical harmony may claim only that harmony would be far more surprising under naturalism than under theism.

The exact magnitude of the difference may be irrelevant.

### Response: The direction of a probability comparison still requires justification

This objection is correct that numerical precision is not always necessary for an evidential argument.

A qualitative likelihood comparison can be meaningful and informative.

In some scientific and statistical settings, theoretical constraints may justify an ordering between conditional probabilities even when their exact numerical values remain unknown.

But the absence of a requirement for precision does not eliminate the requirement to justify the ordering.

The claim:

$$
P(E\mid T)>P(E\mid N)
$$

is still a substantive probabilistic claim.

It asserts that the evidence is more probable under theism than under naturalism.

That assertion cannot be established merely by observing that theism is compatible with the evidence or that naturalism lacks a complete explanation.

Nor can it be established by describing numerous hypothetical alternatives without a defensible account of their probabilities.

The problem becomes especially clear when the relevant hypotheses encompass multiple subsidiary models.

Suppose one theistic model assigns an observation high probability while another assigns it low probability.

Suppose the same is true of different naturalistic models.

Without an adequate basis for selecting or weighting these models, the broader hypotheses may not determine a stable likelihood ordering.

It may be possible to construct models in which the evidence favors theism.

It may also be possible to construct models in which the evidence favors naturalism or provides no discrimination.

The existence of one favorable construction does not establish the qualitative comparison.

Moreover, the use of words such as *likely*, *surprising*, *expected*, or *plausible* can obscure rather than resolve the problem.

If these terms are intended probabilistically, their inferential content requires justification.

If they are intended non-probabilistically, the argument must explain what evidential relationship they express and why that relationship supports the conclusion.

The distinction is not between precise and imprecise reasoning.

It is between justified and unjustified comparison.

An approximate likelihood ratio may be defensible when sufficient constraints establish its approximate magnitude.

A qualitative ordering may be defensible when sufficient constraints establish its direction.

But an ungrounded judgment does not become an adequate inference merely because it avoids numerical specificity.

**The problem is not that the arguments fail to identify how much the evidence favors theism. It is that they have not established why the evidence favors theism at all.**

## Objection 5: Simplicity, indifference, and rational credence can justify the probabilities

A defender might argue that probability assignments need not be arbitrary simply because they are not empirically calibrated.

Philosophical principles may provide rational grounds for assigning probabilities.

The principle of indifference, for example, may recommend assigning equal credence to alternatives when no relevant distinction favors one over another.

Simplicity may favor hypotheses requiring fewer independent assumptions or possessing less descriptive complexity.

Other principles of rational belief may justify particular prior assignments or constraints on likelihoods.

Consequently, the absence of empirical calibration does not demonstrate that the proposed probability measures lack justification.

### Response: The relevant principles must be specified and shown to apply

This objection correctly identifies that probabilities can be justified through considerations other than empirical frequency estimation.

It does not, however, establish that the principles invoked in theistic arguments successfully justify their assignments.

Consider the principle of indifference.

In a sufficiently constrained model, symmetry can provide a defensible reason for treating alternatives equally.

But the inference from ignorance to equiprobability is not generally valid.

To justify equal probabilities, one must establish why the alternatives are appropriately individuated and why they should be treated symmetrically.

An arbitrary partition of a possibility space does not acquire a uniform probability measure merely because its elements can be enumerated.

Nor is uniformity generally preserved when one independently imposes uniform distributions under different parameterizations.

The principle therefore cannot be invoked without addressing the construction of the relevant alternatives and the basis for treating them as equiprobable.

The same issue arises with simplicity.

Simplicity may be epistemically relevant, but the relevant notion must be specified.

Does simplicity concern the number of entities, the length of a description, the number of independent parameters, the complexity of the mathematical structure, or the extent of auxiliary assumptions required?

These criteria need not produce the same ordering.

A hypothesis involving one fundamental entity may be descriptively simple while containing poorly constrained preferences or capacities.

A theory involving numerous mathematical structures may nevertheless possess highly constrained explanatory relationships.

The assertion that one hypothesis is simpler therefore does not automatically determine its prior probability.

A further argument is needed connecting the chosen measure of simplicity to the probability assignment.

Even when such a connection is available, its applicability to metaphysical hypotheses must be defended.

The same criticism applies to claims of intrinsic probability.

A philosophical framework may define intrinsic probability through simplicity, explanatory virtues, or other theoretical considerations.

But the terminology does not independently establish the legitimacy of those considerations or the values assigned through them.

The framework must provide a defensible account of its probability judgments.

And the argument must show that the resulting assignments support the claimed conclusion rather than merely restating a preference for the hypothesis.

There is an important distinction between offering a philosophical rationale for a probability assignment and demonstrating that the rationale is adequate.

A principle may provide a reason to investigate a model without establishing that its probabilities accurately represent the relevant evidential relationships.

The present critique does not deny that nonempirical considerations can constrain rational credence.

It requires that their constraining role be established rather than assumed.

**Appeals to simplicity, symmetry, or intrinsic probability do not eliminate the problem of justification. They identify additional principles whose relevance and application must themselves be defended.**

## Objection 6: Theism supplies a genuine likelihood because God would have reasons to create the observed goods

A more substantive response concerns the alleged likelihood under theism.

A defender may argue that theism is not an unconstrained hypothesis.

Traditional theism attributes substantive properties to God, including perfect goodness, omniscience, and omnipotence.

These attributes may provide reasons to expect the creation of valuable realities.

A perfectly good creator might have reason to actualize worlds containing conscious beings, rational agency, moral significance, or harmonious relationships between experience and behavior.

Consequently, the argument need not assume arbitrary divine preferences. It can appeal to the attributes of God and their implications for the kinds of worlds a divine creator would have reason to create.

### Response: The existence of a reason does not establish its probabilistic weight

The objection identifies a potentially substantive constraint on divine intentions.

But the inference from a divine attribute to a likelihood of a particular observation remains incomplete.

The existence of a reason for producing an outcome is not equivalent to the probability of producing that outcome.

Even if perfect goodness implies that certain states of affairs possess value, it does not automatically follow that a perfectly good creator would actualize every valuable state of affairs.

Nor does it follow that one valuable outcome would be preferred over all alternatives.

Different possible worlds may realize different goods, involve different tradeoffs, or instantiate values through radically different structures.

An argument claiming that God would have reason to produce conscious agents must therefore explain why this reason provides a sufficiently strong expectation of the observed outcome.

The task becomes more difficult when the evidence is narrowly specified.

The existence of some form of conscious life is not identical to the existence of embodied organisms governed by the particular physical laws of our universe.

The existence of valuable experiences is not identical to the precise psychophysical relationships observed in terrestrial organisms.

And the value of rational agency does not automatically determine the structure of the physical and phenomenal processes through which rational agency is realized.

The argument must therefore distinguish the general claim that God may have reasons to create valuable realities from the much more specific claim that the observed reality is comparatively probable under theism.

The latter does not follow automatically from the former.

This is especially important when the observation itself is used to identify the divine purpose.

If the world contains a particular form of harmony, the argument may propose that God values that harmony.

But the relevant evidential question is whether the divine preference was independently justified, rather than introduced because it makes the observed outcome intelligible.

Otherwise, the explanation risks becoming adaptable to the observed evidence.

A properly constrained theistic model might support substantive expectations. The present critique does not rule out that possibility.

But the argument must establish those constraints and show how they warrant the claimed likelihood.

Merely identifying a morally intelligible divine reason does not complete the inference.

Furthermore, the comparative argument still requires the corresponding likelihood under naturalism.

Even if a high theistic likelihood were justified, that would not independently establish that the evidence favors theism unless the naturalistic likelihood were sufficiently lower.

**A reason God might have for creating the observed world is not, without further argument, a probability that God would create it.**

## Objection 7: Philosophical inquiry cannot be held to the standards of engineering and statistics

One of the strongest general objections concerns the methodological analogy that motivates this essay.

Engineering, statistics, and reliability analysis often investigate systems for which empirical measurements, physical mechanisms, repeated observations, and operational validation are available.

Philosophical arguments for theism concern ultimate reality, metaphysical explanation, and hypotheses whose empirical implications may be difficult to specify.

It may therefore be unreasonable to demand the same forms of methodological validation in both contexts.

Perhaps philosophical arguments must rely more heavily on conceptual analysis, rational intuition, metaphysical principles, and qualitative explanatory judgments.

If so, the apparent asymmetry may simply reflect differences in the subject matter rather than a methodological deficiency.

### Response: Different methods do not imply the absence of common justificatory standards

The objection is correct that philosophical inquiry and reliability engineering are not methodologically identical.

The present argument does not require them to be.

A metaphysical hypothesis cannot ordinarily be evaluated through the same procedures used to estimate component failure rates. The existence of God is not a parameter that can simply be measured through repeated trials. Nor must every philosophical argument be translated into an empirically calibrated statistical model.

But these differences do not eliminate the requirement that substantive inferences be justified.

The engineering analogy concerns a general methodological distinction, not the wholesale transplantation of one discipline's techniques into another.

In applied modeling, a mathematical result is not regarded as evidentially authoritative merely because it follows from stipulated assumptions. Its use requires an account of the model's adequacy and its relationship to the phenomenon.

The same general distinction applies to philosophical inference.

A metaphysical argument must justify the assumptions connecting its premises to its conclusion.

If it claims a probability comparison, it must justify that comparison.

If it invokes a possibility space, it must explain the relevance of that space.

If it relies on explanatory superiority, it must establish why the alleged superiority warrants the proposed epistemic conclusion.

These are not uniquely engineering requirements.

They are basic conditions of justified inference.

The absence of the empirical resources available in applied disciplines may make philosophical probabilistic modeling more difficult.

But difficulty does not justify substituting arbitrary assumptions for evidence.

Indeed, where uncertainty is severe and the available information provides limited constraints on competing models, caution concerning probabilistic conclusions becomes especially important.

An engineering analyst facing insufficient information may acknowledge that a risk cannot presently be estimated with defensible precision.

A philosopher confronting deeply underdetermined metaphysical hypotheses may likewise need to acknowledge that a proposed likelihood comparison cannot presently be justified.

Such acknowledgment is not a failure of philosophical reasoning.

It is an appropriate recognition of its limits.

The alternative would be to allow the absence of empirical constraints to function as permission for unconstrained probabilistic speculation.

That would invert the relationship between uncertainty and epistemic confidence.

The less information available to justify the model, the greater the freedom to assign whatever probabilities seem intuitively attractive.

But greater freedom in model construction does not imply stronger evidential support.

It generally makes the problem of justification more demanding.

**The point is not that philosophy must become engineering. It is that philosophical arguments cannot claim evidential authority while exempting their decisive assumptions from methodological scrutiny.**

## Objection 8: IBE is independent of Bayesian probability and therefore avoids these objections

A defender of inference to the best explanation may reject the probabilistic framing entirely.

Perhaps explanations can support rational belief without being reducible to likelihood ratios or posterior probabilities.

Theistic arguments may therefore succeed by showing that God provides the simplest, most coherent, or most comprehensive explanation of certain observations.

If IBE possesses independent epistemic legitimacy, criticisms of Bayesian model construction may not apply.

### Response: Independent explanatory inference requires independent justification

This objection identifies a legitimate philosophical position.

IBE need not be treated as a disguised Bayesian calculation.

But independence from Bayesian probability does not establish that every purported explanatory inference is warranted.

If IBE is defended as an independent form of inference, it must provide an account of why explanatory superiority supplies a reason for belief.

It must also establish that the hypothesis under consideration genuinely possesses the relevant explanatory advantages.

The distinction between explanatory compatibility and explanatory confirmation remains essential.

A hypothesis may explain an observation in the sense of making it intelligible without being comparatively well supported by that observation.

Likewise, a hypothesis may possess greater explanatory scope or simplicity under some criteria while remaining unsupported by independent evidence.

The IBE defender must therefore explain why the selected explanatory virtues are epistemically relevant, how they are applied, and whether the resulting comparison warrants the conclusion.

This task is particularly difficult when the explanation invokes an agent whose preferences and intentions are not independently constrained.

Theism may be presented as a unified explanation of physical order, consciousness, moral experience, and the existence of life.

But if the explanatory connection between divine agency and each phenomenon depends on separately selected assumptions about divine purposes, the apparent unification may not establish the evidential advantage claimed for it.

Nor does a comparison with incomplete naturalistic explanations demonstrate that theism is the best explanation in a truth-conducive sense.

The best explanation among those considered may still be inadequate.

The set of available alternatives may be incomplete.

And the criteria of explanatory superiority may not be sufficient to establish the ontological conclusion.

None of these concerns requires assigning numerical probabilities.

They concern the relationship between explanation and justified belief.

Consequently, the move from Bayesian confirmation to IBE does not automatically escape the critique.

It changes the form in which the inferential burden must be discharged.

**If explanatory superiority is invoked as evidence for theism, the argument must justify why the proposed explanatory qualities establish that superiority and why the superiority warrants belief.**

Simply invoking IBE does not supply that justification.

## Objection 9: All probabilistic models depend on assumptions, so the criticism demands an impossible standard

Another objection challenges the feasibility of the methodological demands themselves.

Every model involves idealization, abstraction, and assumptions that cannot be conclusively established.

Even highly successful scientific theories contain uncertain parameters, approximations, and unresolved structural questions.

No probability model is free from uncertainty.

If philosophical arguments for theism are rejected because their assumptions are not fully justified, perhaps the same standard would undermine probabilistic reasoning throughout science and ordinary life.

### Response: The criticism concerns adequate justification, not certainty

This objection confuses the requirement for defensible assumptions with a demand for infallible knowledge.

The present critique does not require that every model assumption be proven with certainty.

Nor does it require exhaustive enumeration of every possible source of uncertainty.

The requirement is that the assumptions supporting a substantive conclusion possess sufficient justification for the inference being made.

In applied statistics, models routinely employ approximations and idealizations.

These are not automatically illegitimate.

Their adequacy depends on whether they are appropriate to the purpose of the analysis, whether their limitations are understood, and whether the conclusions remain defensible under relevant uncertainties.

A model may be useful even when its assumptions are imperfect.

But the fact that all models involve assumptions does not make arbitrary and well-supported assumptions epistemically equivalent.

There is a meaningful distinction between a probability distribution justified by relevant physical knowledge and a distribution selected because it produces an attractive result.

There is a meaningful distinction between a sensitivity analysis grounded in a developed theoretical model and a counting argument over unconstrained hypothetical alternatives.

And there is a meaningful distinction between an independently supported explanatory mechanism and an explanatory narrative constructed primarily to accommodate the observed phenomenon.

These distinctions remain even though no model is perfectly certain.

The issue is whether the assumptions are adequate to support the claimed conclusion.

Moreover, the strength of an evidential claim should be proportionate to the support for its premises and inferential relationships.

A model with substantial unresolved uncertainty may still justify a limited conclusion.

A model whose decisive assumptions are effectively unconstrained may fail to justify even the direction of a proposed comparison.

This is not an impossibly demanding standard.

It is the ordinary distinction between an inference that has been sufficiently supported and one that has not.

To insist otherwise would make methodological criticism almost impossible.

Any challenge to an assumption could be dismissed by observing that all reasoning requires assumptions.

But the general inevitability of assumptions does not justify any particular assumption.

**The fact that no model is perfect does not imply that every model is equally defensible.**

## Objection 10: The criticism is excessively skeptical because it permits no conclusion under deep uncertainty

A final objection concerns the consequences of the critique.

If fine-tuning and psychophysical harmony cannot support theistic confirmation without independently justified likelihoods, perhaps the resulting standard is so demanding that little philosophical progress remains possible.

Many metaphysical questions lack decisive empirical tests.

Their competing hypotheses may be incompletely specified.

Their explanatory relationships may remain underdetermined.

If we cannot assign probabilities or establish explanatory comparisons under such circumstances, are we simply forced into permanent suspension of judgment?

### Response: Recognizing inferential limits is not the abandonment of inquiry

The objection assumes that philosophical progress requires a determinate probabilistic or explanatory conclusion.

That assumption is unwarranted.

An inquiry can make progress by clarifying concepts, identifying hidden assumptions, distinguishing competing theories, discovering inconsistencies, developing new explanatory models, or determining which questions remain underconstrained.

The recognition that a particular inference lacks adequate justification is itself an intellectual achievement.

It prevents speculative assumptions from being mistaken for established evidence.

It can also reveal what additional work would be required to develop a stronger argument.

In the case of fine-tuning, this might involve more precise physical theories, better-motivated probability measures, or clearer accounts of the relationship between theoretical parameter variation and genuine physical alternatives.

In psychophysical harmony, it might involve more developed theories of consciousness, greater clarity concerning the metaphysical relationships between phenomenal and physical properties, and principled accounts of which alternative psychophysical structures are genuinely relevant.

For IBE, it might involve stronger explanatory constraints, independently supported auxiliary assumptions, or a more rigorous account of how explanatory virtues bear on rational belief.

None of these avenues is foreclosed by the present critique.

What is rejected is the premature conversion of explanatory uncertainty into probabilistic confirmation.

There is no requirement that every unresolved question be supplied with a numerical answer.

Nor is there a requirement that every philosophical disagreement admit an immediately defensible comparative likelihood.

Sometimes the available evidence does not establish the proposed relationship.

Recognizing that limitation is not excessive skepticism.

It is an appropriate refusal to claim more than the argument warrants.

Moreover, the criticism does not entail that all evidence concerning theism and naturalism is uninformative.

It concerns the specific inferential structures examined here.

Other arguments may possess different evidential foundations. They would need to be assessed independently.

The failure of one argument does not establish the impossibility of every argument with a similar conclusion.

But neither does the mere possibility of a future successful argument vindicate the inadequately justified arguments currently offered.

**The recognition that a proposed inference has failed is not equivalent to the claim that its subject matter is beyond rational investigation.**

It establishes only that the inference has not earned its conclusion.

---

## The cumulative significance of the objections

The objections considered in this section identify several genuine philosophical distinctions.

Subjective probabilities need not represent physical frequencies. Epistemic possibilities can receive coherent probability assignments. Qualitative likelihood comparisons can sometimes be justified without exact numbers. Simplicity and explanatory virtues may possess legitimate epistemic roles. IBE may be defensible independently of Bayesian confirmation. And philosophical inquiry need not reproduce every methodological feature of applied engineering.

But none of these general observations establishes that the particular probabilistic and explanatory comparisons examined in this essay are warranted.

Their relevance depends on what they actually justify.

The legitimacy of subjective Bayesianism does not justify an arbitrary likelihood.

The legitimacy of epistemic probability does not determine a distribution over hypothetical mappings.

The legitimacy of qualitative comparison does not establish the direction of an unsupported likelihood inequality.

The legitimacy of simplicity as a theoretical virtue does not establish a particular prior probability.

The legitimacy of intentional explanation does not determine the probability of a hypothetical agent choosing a particular outcome.

And the legitimacy of IBE does not make every available explanation evidentially superior.

The recurring error is to treat a defense of an inferential method as though it were a defense of a particular inference.

But the existence of a legitimate method does not demonstrate that its requirements have been satisfied in a specific application.

This is the methodological distinction on which the entire critique depends.

A probability assignment may be mathematically admissible without being epistemically justified.

An explanation may be intelligible without being evidentially discriminating.

And an argument may possess a valid conditional structure without establishing that the conditions supporting its conclusion are satisfied.

These possibilities are not unusual exceptions to otherwise reliable inferential methods.

They are precisely the reasons methodological scrutiny is necessary.

### The unresolved burden

After considering these objections, the burden faced by probabilistic arguments for theism remains substantially unchanged.

If the argument claims that fine-tuning is improbable under naturalism, it must justify the relevant probability model.

If it claims that psychophysical harmony was extraordinarily unlikely, it must justify the proposed alternatives, their individuation, and their relative probabilities.

If it claims that either observation is more probable under theism, it must justify the assumptions concerning divine intentions and the resulting likelihood comparison.

If it relies on explanatory superiority rather than explicit Bayesian confirmation, it must defend the criteria and inferential principles connecting that superiority to the claimed ontological conclusion.

A defender may employ subjective probabilities, epistemic possibility spaces, qualitative judgments, or non-Bayesian explanatory principles.

None of these choices is inherently illegitimate.

But none relieves the argument of its central justificatory burden.

The existence of a coherent framework in which an observation favors theism is not equivalent to a demonstration that the observation provides justified evidence for theism.

The difference is decisive.

In the arguments examined, the favorable evidential relationship is frequently produced by assumptions about the alternatives, their probabilities, or the explanatory expectations of the competing hypotheses.

Yet those assumptions are precisely what the argument has not adequately established.

The resulting conclusion therefore remains conditional on a speculative representation whose evidential authority has not been demonstrated.

That is not a minor limitation concerning the magnitude of the claimed confirmation.

It concerns whether the argument has established confirmation at all.

**The central methodological objection survives because none of these defenses establishes the missing inferential relationship. They demonstrate, at most, that such a relationship might be constructed within a suitable philosophical framework. They do not establish that the particular frameworks employed warrant the conclusions drawn from them.**

This leaves the critique's central conclusion intact.

The fine-tuning and psychophysical harmony arguments examined have not established the probability comparisons required for their claimed evidential force. Related IBE arguments have not established that explanatory availability or attractiveness warrants the proposed comparative conclusions.

The failure is not repaired by appealing to the general legitimacy of Bayesian probability, subjective credence, epistemic possibility, or explanatory inference.

The problem lies in the unjustified application of those methods to the phenomena being investigated.

And where the inferential foundations remain unestablished, the advertised evidential conclusion remains unsupported.

# Conclusion — The Probability Was Never Established

There is something deeply revealing about the contrast between how probability is treated in applied disciplines and how it is frequently employed in philosophical arguments for the existence of God. In reliability engineering, statistical modeling, and decision theory, the legitimacy of a probabilistic assessment depends on far more than the formal correctness of its calculations. The analyst must establish an appropriate representation of the system, identify the relevant uncertainties, justify the probability distributions employed, examine the assumptions connecting the model to the phenomenon, and determine what conclusions the available information actually warrants. A probabilistic assessment that fails to satisfy these requirements cannot claim evidential authority merely because its mathematical operations are internally consistent.

Yet in arguments for theism, probability is often treated with a remarkable degree of methodological permissiveness. Hypothetical alternatives are constructed through conceptual speculation, their relative abundance is presented as evidence of improbability, and unsupported judgments about the expectations of competing metaphysical hypotheses are incorporated into Bayesian comparisons. The resulting arguments may possess the formal appearance of statistical reasoning while lacking the methodological foundations necessary to justify their application.

The contrast is not a superficial difference between disciplines. It exposes a fundamental distinction between the mathematical representation of uncertainty and the epistemic justification of probabilistic inference.

Probability theory provides a formal language for reasoning under uncertainty. It does not independently establish which uncertainties are relevant, which alternative states of affairs should be represented, how probability should be distributed across them, or whether the resulting model adequately describes the phenomenon under investigation. Those are substantive questions whose answers determine the evidential significance of the calculation.

To overlook this distinction is to mistake the availability of a mathematical framework for the legitimacy of its application.

This mistake is particularly consequential when probabilistic reasoning is used to support major metaphysical conclusions. The claim that the universe provides evidence for the existence of God is not an ordinary descriptive judgment. It is a proposed inference concerning the fundamental structure of reality. Depending on the conception of God being defended, accepting the conclusion may involve substantial commitments concerning agency, causation, consciousness, morality, and the ultimate explanation of the physical world.

The significance of these commitments does not determine whether theism is true. Nor does it alter the evidential probabilities of the observations invoked in its support. But it makes the responsible treatment of inferential uncertainty especially important. A conclusion of such ontological significance should not rest on probabilistic assumptions whose legitimacy would be questioned in far less ambitious applications.

The preceding analysis has shown that the problems arise before the relevant Bayesian calculations can acquire substantive evidential force.

In the fine-tuning argument, physical sensitivity is converted into probabilistic improbability. The observation that life-permitting conditions occupy restricted regions of theoretical parameter spaces is treated as though it establishes that those conditions were unlikely under naturalism. But the probability does not follow from the narrowness of the region. It depends on the specification of the relevant alternatives, the justification of a probability measure, the relationships among physical parameters, and the theoretical assumptions governing their possible values.

These are not peripheral details. They determine whether the alleged improbability has been established at all.

Even if an appropriately specified naturalistic model assigned life-permitting conditions a low probability, comparative confirmation of theism would require additional justification. The argument would need to establish that the observed conditions are more probable under theism, rather than merely compatible with some proposed divine intention. The existence of a possible theological explanation does not independently establish the likelihood of the observation.

The fine-tuning argument therefore moves through two inferential transitions that require separate justification: from physical sensitivity to probabilistic improbability, and from alleged improbability to comparative confirmation of theism.

Neither transition is established simply by the scientific observation with which the argument begins.

The argument from psychophysical harmony displays an even more fundamental problem.

Here, the proposed domain of alternatives is itself highly speculative. The argument treats phenomenal experiences and physical or functional states as though their relationships can be varied across an enormous space of alternative mappings. It then characterizes the actual harmonious associations as exceptional within that space and infers that they were extraordinarily improbable under naturalism.

But the construction of this space depends on controversial assumptions about the metaphysical nature of consciousness. The ability to describe alternative psychophysical relationships does not demonstrate their coherence or metaphysical possibility. And retreating to epistemic possibility does not establish a probability distribution over the alternatives.

The argument has not justified the individuation of the mappings, their relative weighting, or the principles governing their probability assignments. Consequently, the apparent numerical predominance of disharmonious alternatives does not establish that psychophysical harmony was improbable.

Nor does the availability of a possible divine preference for harmonious consciousness establish that harmony was more likely under theism.

The resulting Bayesian comparison therefore lacks the foundations required for its advertised evidential conclusion.

What makes this case especially revealing is that the argument's apparent improbability arises largely from its own speculative construction. The enormous space of disharmonious alternatives is not an independently established feature of a known physical or metaphysical process. It is produced through assumptions about the recombinability of phenomenal and physical properties, the structure of the alternative mappings, and the manner in which epistemic probability should be distributed across them.

The argument then treats the output of this construction as though it were evidence about the actual relationship between consciousness and reality.

But mathematical abundance within a constructed possibility space is not evidence of probabilistic improbability.

The wider problem extends beyond Bayesian reasoning.

Inference-to-the-best-explanation arguments frequently rely on similar transitions. A phenomenon is identified as difficult to explain under naturalism. A theistic explanation is proposed. The proposed explanation is then characterized as superior because it renders the phenomenon intelligible, offers a unified account, or invokes a divine purpose under which the observation appears reasonable.

Yet the availability of an explanation is not the same as evidential confirmation.

An explanation may accommodate an observation without establishing that the observation was expected. A broad hypothesis may unify phenomena through flexible auxiliary assumptions without genuinely constraining the outcomes it purports to explain. And the absence of a complete alternative explanation does not establish the truth or comparative superiority of the explanation that happens to be available.

If explanatory virtues are intended to support probabilistic confirmation, their relationship to the relevant probabilities requires justification. If IBE is defended as an independent form of inference, the criteria governing explanatory superiority and their connection to rational belief must be established.

Neither approach permits explanatory compatibility to substitute for evidential support.

Across these arguments, the same methodological pattern repeatedly emerges. An unresolved explanatory question is treated as though it establishes that the observed phenomenon was improbable. A collection of imagined alternatives is treated as though it supplies a probability distribution. An intuitively attractive explanation is treated as though it establishes a favorable likelihood. And a formal or qualitative comparison is used to support a conclusion whose decisive assumptions have not been adequately defended.

This is the central failure.

The probability was not merely estimated imprecisely. The relevant probabilistic comparison was not established by the premises offered.

Recognizing this failure does not require a competing Bayesian argument for naturalism. It does not require demonstrating that life-permitting conditions or psychophysical harmony were probable under naturalism. Nor does it require assigning a low prior probability to theism.

Those would be additional claims, each requiring independent justification.

The present criticism is directed at the proposed inference itself.

If an argument claims that an observation favors theism over naturalism, it must establish the relationship on which that comparison depends. If its likelihoods are unsupported, its probability measures arbitrary, or its explanatory assumptions insufficiently constrained, then the claimed evidential conclusion has not been demonstrated.

The critic is not obligated to replace an unsupported probability with another unsupported probability. The failure of the proposed assessment is sufficient to establish that the assessment has not achieved its stated purpose.

This distinction is essential because it prevents the methodological criticism from being misunderstood as a competing metaphysical doctrine.

To reject an unjustified likelihood comparison is not to assert that its reverse is true.

To recognize that a probability has not been established is not to assign equal probability to the competing hypotheses.

And to acknowledge that a phenomenon remains unexplained is not to deny that an explanation exists.

The appropriate epistemic conclusion is proportionate to the analysis: the arguments examined have not demonstrated the comparative evidential support they claim for theism.

This is not excessive skepticism. It is an ordinary requirement of responsible inference.

There are circumstances in which the available information is insufficient to establish a determinate probability or a defensible likelihood ordering. Recognizing that limitation may be the most informative conclusion the inquiry can support.

In applied disciplines, such recognition is not necessarily considered a methodological failure. An analyst who determines that the available evidence cannot justify a particular risk estimate may have prevented a much more serious error: the use of an unsupported probability as though it were a reliable basis for judgment.

The same principle should apply to philosophical reasoning.

Where the relevant alternatives cannot be adequately specified, the probability measures cannot be justified, or the competing hypotheses do not sufficiently constrain their expected observations, the responsible conclusion may be that the proposed comparison cannot presently be established.

The inability to produce a defensible likelihood ratio does not create permission to invent one.

Nor does the extraordinary significance of a philosophical question entitle its proposed answers to weaker standards of justification.

If anything, questions concerning the fundamental structure of reality demand particular attention to the limits of what our models and arguments can establish.

None of this entails that probability has no place in metaphysics or philosophy of religion. Bayesian reasoning can legitimately represent uncertainty concerning propositions that are not generated by repeatable physical processes. Subjective credences can be coherent and philosophically informative. Explanatory virtues can contribute to rational inquiry. And metaphysical hypotheses can, in principle, possess evidential relationships to observations.

But the legitimacy of these methods in general does not establish the legitimacy of any particular application.

A coherent probability assignment may be inadequate for the conclusion it is intended to support. An explanatory hypothesis may be intelligible without being evidentially superior. And a mathematically valid update may transmit assumptions whose justification remains entirely unresolved.

The methodological burden is not satisfied by demonstrating that an argument can be formulated.

It is satisfied by establishing that the inferential relationships on which the argument depends are warranted.

That is the principle that should govern both applied probabilistic reasoning and philosophical argumentation.

In engineering, we would not accept an unsupported estimate of catastrophic failure merely because an analyst could construct a coherent probability distribution producing it. We would ask what the model represents, how its assumptions were justified, whether its uncertainties were appropriately characterized, and what conclusions could responsibly be drawn from it.

Those questions do not become irrelevant when the proposed conclusion concerns the existence of God.

The subject matter may differ. The available methods may differ. The forms of evidence may differ. But the distinction between a mathematically permissible representation and an epistemically justified inference remains.

The arguments examined in this essay repeatedly fail to establish that distinction.

Their probabilistic conclusions depend on assumptions whose evidential authority has not been demonstrated. Their explanatory conclusions depend on relationships between hypothesis and observation that remain insufficiently constrained. And their apparent inferential force frequently arises from the conversion of conceptual possibilities, explanatory gaps, and speculative intuitions into claims of probability or confirmation.

The resulting formalism may be coherent. The philosophical questions may be important. The proposed explanations may be conceptually interesting.

But none of these considerations establishes the likelihood comparisons required for the claimed evidential conclusions.

The deeper lesson extends beyond philosophy of religion. Whenever probabilistic or explanatory reasoning is applied to complex, poorly understood, or weakly constrained phenomena, there is a danger that the formal structure of the analysis will be mistaken for evidence of its adequacy.

A model can be made precise without becoming accurate. A probability can be made coherent without becoming justified. And an explanation can be made intellectually satisfying without becoming evidentially compelling.

The task of disciplined inquiry is to distinguish these achievements rather than conflate them.

**The legitimacy of an inference depends not merely on what follows from its assumptions, but on whether those assumptions provide a defensible basis for reasoning about the phenomenon under investigation.**

That requirement is not suspended when the conclusion is metaphysical, the evidence is difficult to interpret, or the available explanations are incomplete.

It is precisely under such circumstances that methodological accountability becomes most important.

The fundamental objection to the Bayesian and explanatory arguments for theism examined here is therefore not that their conclusions are necessarily false, nor that their calculations necessarily contain mathematical errors.

It is that they have not established the evidential relationships on which their conclusions depend.

They have demonstrated what follows when certain speculative probability assignments and explanatory assumptions are accepted. They have not adequately demonstrated why those assignments and assumptions should be accepted as justified representations of reality.

And without that justification, the purported confirmation remains unestablished.

**The probability was never established. The likelihood advantage was never demonstrated. And the ontological conclusion was never earned by the inference offered in its support.**