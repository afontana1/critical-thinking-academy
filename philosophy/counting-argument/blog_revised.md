# Counting Possibilities, Reifying Mind

### A Critique of Joshua Rasmussen’s Counting Argument

## 1. Introduction: When Mathematics Becomes Metaphysics

Can a mathematical fact about the number of possible representations tell us what reality is fundamentally made of? In his [counting argument for mind-first metaphysics](https://worldviewdesign.substack.com/p/a-new-counting-argument-for-mind), philosopher Joshua Rasmussen suggests that mind is metaphysically prior to matter because it encompasses a greater range of possible realities. Drawing on Cantor’s theorem, he argues that possible mental realities outnumber possible nonmental realities, and that this numerical abundance provides a reason to regard mind as the fundamental basis of existence.

The argument is intriguing because it appears to transform a contentious metaphysical question into a mathematical problem. Yet the mathematical relationship itself does not establish the metaphysical conclusion. Rasmussen must additionally show that arbitrary collections of physical properties correspond to distinct conceivable mental properties, that mental and physical possibilities can be meaningfully compared, and that the cardinality of a possibility space bears upon ontological fundamentality.

This essay challenges those assumptions by drawing on mathematical modeling, cognitive science, and complexity theory. It argues that mental representation is characteristically selective: cognition makes complex realities tractable through abstraction and the allocation of limited cognitive resources, rather than by exhaustively reproducing their possible configurations. Moreover, even if Rasmussen’s proposed numerical correspondence were established, it would not follow that mind is ontologically prior to matter. The argument risks reifying mathematical and representational abstractions into claims about the fundamental structure of reality.

The issue, then, is not the validity of Cantor’s theorem, but whether its application to metaphysics can bear the philosophical weight Rasmussen places upon it.

## 2. Rasmussen’s Argument: From Cantor to the Priority of Mind

Rasmussen’s argument develops in two stages. In his [2015 paper, *Building Thoughts from Dust: A Cantorian Puzzle*](https://joshualrasmussen.com/articles/building-thoughts-from-dust.pdf), he advances a counting argument against a particular form of reductive physicalism. He begins with the premise that, for any plurality of physical properties, there is a corresponding conceivable mental property: thinking that those properties are physical. Distinct pluralities, he proposes, determine distinct mental properties.

Let $$P$$ denote a set of physical properties, and let $$\mathcal{P}(P)$$ denote its power set, comprising all subsets of $$P$$. Cantor’s theorem establishes that:

$$
|\mathcal{P}(P)|>|P|
$$

If every subset of physical properties determines a *different* conceivable mental property, then the mental properties so identified outnumber the members of $$P$$. Rasmussen concludes that not every mental property can be identical with a physical property. His 2015 argument targets a particular reductive identity theory; it does not by itself establish that mind is metaphysically fundamental. The correspondence between subsets and distinct mental properties is a philosophical premise, not a consequence of Cantor’s theorem.

In his [2024 essay, *Mind Makes More*](https://worldviewdesign.substack.com/p/a-new-counting-argument-for-mind), Rasmussen proposes a stronger, preliminary argument. He describes fundamental reality as the basis of the greatest amount of “stuff,” using that term in connection with a domain’s possible divisions or states. He argues that a possible nonmental reality can be mentally represented and that conceptual combinations yield further possible mental realities. On this basis he concludes that mind has the wider range of possibilities and is therefore fundamental.

Two questions must be kept distinct. **First**, does every relevant physical plurality determine a distinct conceivable mental property, allowing the cardinality comparison? **Second**, even if mental possibilities outnumber physical ones, why should the larger range identify what grounds reality? A third question—whether the domains are counted on comparable terms—concerns the move between them. The mathematics settles none of these questions on its own.

## 3. The Representation Problem: Cognition as Selective Modeling

Rasmussen’s counting argument relies on a possible mental property for each arbitrary plurality of physical properties. What, however, does it mean for a mind to represent a physical reality? Scientific modeling and cognitive science give us reason to distinguish *referring to* something, *modeling* selected aspects of it, and *encoding* enough detail to discriminate it from alternatives.

Consider an NVIDIA A100 GPU. Its possible configurations involve memory contents, processing states, instruction sequences, and interactions between components. For a simplified system with $$n$$ independently variable components, its configuration space is:

$$
|\Omega|=\prod_{i=1}^{n}|X_i|
$$

where $$X_i$$ is the set of states available to component $$i$$. A cluster of GPUs introduces additional network, scheduling, and synchronization possibilities. Engineers do not mentally enumerate every configuration; they use simulations, specifications, and models that isolate the dimensions relevant to a task.

This is more than a complaint about insufficient human brainpower. Mathematical models often succeed *by omitting detail*. The [*Stanford Encyclopedia of Philosophy*’s discussion of scientific models](https://plato.stanford.edu/entries/models-science/) describes abstraction and idealization as ways of making complex systems tractable. A GPU-performance model might map physical configurations onto descriptions involving throughput, power, and temperature:

$$
f:\Omega\rightarrow Z
$$

Distinct configurations can share a modeled description:

$$
x_1\ne x_2\qquad\text{while}\qquad f(x_1)=f(x_2)
$$

The model has not ceased to represent the GPU because it fails to preserve every physical distinction. Its selectivity is part of what makes it useful.

A parallel insight appears in cognitive science. Herbert Simon’s [account of bounded rationality](https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf) explains why agents adopt tractable procedures instead of evaluating every alternative. John Vervaeke, Timothy Lillicrap, and Blake Richards’ work on [relevance realization](https://contrastiveconvergence.net/~timothylillicrap/files/articles/relevance%20realization%20as%20an%20emerging%20framework%20in%20cogsci.pdf) addresses how a cognitive system determines which features and relations matter. Dan Sperber and Deirdre Wilson’s [relevance theory](https://www.dan.sperber.fr/?p=93) relates cognitive effects to processing effort, while Falk Lieder and Thomas Griffiths’ [resource-rational analysis](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/resourcerational-analysis-understanding-human-cognition-as-the-optimal-use-of-limited-computational-resources/586866D9AD1D1EA7A1EECE217D392F4A) examines the allocation of limited computational resources. These are distinct theories, not a single account of representation, but each makes selection or computational constraint philosophically salient.

Rasmussen has an important reply available. His [2015 paper](https://joshualrasmussen.com/articles/building-thoughts-from-dust.pdf) expressly separates *conceivability* from *physical realizability*: he need not claim that any human brain could instantiate a thought about every physical property. Cognitive science cannot show that every logically possible mind is bounded as we are. Nor must a mind enumerate an infinite set to describe it compactly. The GPU example therefore does **not** disprove his premise by exhibiting human limitations.

Its force is more precise. Our familiar capacities for reference and modeling do not justify the unrestricted claim that each arbitrary plurality determines its own conceivable mental property. I can refer to “the GPU’s exact state at noon” without encoding that state, and I can describe a state space without possessing a separately specified thought about each of its subsets. Rasmussen may individuate thoughts by what they are *about*, rather than by how much information they internally carry. But then the differences being counted may be supplied by the physical referents used to classify the thoughts, not by an independently demonstrated richness of cognitive representation. That is a problem for the proposed correspondence, distinct from the empirical question of what actual brains can do.

## 4. What Are We Counting? The Problem of Individuation

Even granting that arbitrary pluralities can figure in thought, Rasmussen needs distinct pluralities to determine **distinct mental properties**. Cantor’s theorem tells us that a set has more subsets than members; it does not tell us what counts as one mental or physical property. In the [2015 paper](https://joshualrasmussen.com/articles/building-thoughts-from-dust.pdf), Rasmussen explicitly treats thoughts about different pluralities as different mental properties. That principle requires defense, not merely mathematical notation.

One concern is asymmetry. Physical properties are counted on one side, while mental properties are distinguished through arbitrary collections of those properties on the other. Physical systems also admit configurations, relations, and higher-order descriptions. Rasmussen anticipates a parallel construction using unrestricted physical conjunctions and argues that it runs into a Russell-style contradiction. His reply blocks that *particular* parody; it does not settle which physical and mental domains should be compared, or whether appropriately restricted higher-order physical descriptions deserve consideration.

A second concern is **definability**. Rasmussen proposes a systematic procedure: given physical properties, define the mental property of thinking about them. But a schema using an arbitrary plurality as a parameter is not the same as an individual definition of every plurality. In a fixed countable formal language with finite expressions, there are only countably many such expressions. By contrast:

$$
|\mathcal{P}(\mathbb{N})|=2^{\aleph_0}>\aleph_0
$$

Most subsets of the natural numbers are thus not individually definable in that language. The point is conditional: it neither proves that mental properties are countable nor rules out richer languages, semantic reference, or possible thoughts that are not finitely expressible. It asks what licenses the move from a *uniform description with a parameter* to a distinct intelligible mental property for **every** value of that parameter. Saying “thinking about $$S$$” leaves the question of how $$S$$ is picked out—and how a distinct thought is secured—unanswered.

A defender might instead regard intentional contents as distinct whenever their referents differ, whether or not we can specify them individually. That is a substantive theory of content, and the counting argument may be conditional upon it. But even if it supplies the requisite numerical result, it need not show that minds have greater representational capacities, still less that their referents depend on mind for their existence. The correspondence, the cardinality result, and the metaphysical inference are three separate claims.

## 5. Possibility, Complexity, and the Reification of Mathematical Abstractions

Suppose, for the sake of argument, that Rasmussen’s counting succeeds: possible mental properties really do outnumber physical properties. Why should a greater *number* of possibilities indicate metaphysical priority? In [*Mind Makes More*](https://worldviewdesign.substack.com/p/a-new-counting-argument-for-mind), Rasmussen offers two considerations for his foundational principle. A reality explainable through a single fundamental kind seems theoretically simpler than one requiring several basic kinds; and it may seem strange for “more stuff” to arise from “less stuff.” He describes the latter idea as intuitive and acknowledges that it needs further development. These are reasons to consider the principle, but neither establishes that grounding must preserve or maximize cardinality.

Simplicity of *fundamental kinds* and size of a *possibility space* are different measures. One underlying kind might support many configurations without there being correspondingly many fundamental kinds. Likewise, the intuition that more cannot come from less needs an account of what is being counted: fundamental properties, divisions, configurations, or possible experiences? Without a fixed measure and a rule connecting it to grounding, the ordering principle remains uncertain.

Systems engineering makes the modal distinction vivid. Engineers can distinguish conceivable configurations, feasible designs constrained by physical requirements, alternatives in a trade study, and the system eventually built. The largest possibility space may exceed the realizable and actual spaces by orders of magnitude. Yet a mathematical description of every conceivable aircraft does not establish that the actual aircraft is constituted by that description. Rasmussen specifies *logical* possibility; logical describability must still be connected by argument to what exists and what grounds it.

$$
\text{Modal abundance}\not\Rightarrow\text{ontological priority}
$$

Complexity provides a second check on the intuition, though not a decisive counterexample to his precise metaphysical principle. A system of $$n$$ independent binary components has:

$$
|\Omega|=2^n
$$

possible configurations. This compares elementary component states with configurations, **not** the total number of fundamental properties with the total number of grounded properties. It therefore does not refute Rasmussen by itself. It does show why we should resist inferring that a basis must already contain, as separate fundamentals, every distinction generated through combination. His principle needs an additional argument explaining why his chosen measure of “stuff” behaves differently.

Finally, a representation is not a ground. A model represents a GPU without constituting the GPU; a computer simulation represents a hurricane without making that hurricane depend on the simulation for its existence. Even an injection from physical possibilities to possible thoughts would establish a correspondence, not an ontological dependence relation. Rasmussen needs to explain why *being representable by mind* entails *being based in mind*.

This is the essay’s reification concern, stated carefully rather than as an automatic fallacy verdict. **First**, the ability to construct expressions of the form “a thought about $$S$$” risks being treated as sufficient evidence for a fully populated domain of distinct conceivable mental properties. **Second**, the cardinality of that proposed domain risks being treated as evidence that mind grounds the realities it represents. The first transition raises questions about definition and individuation; the second raises questions about grounding. Neither is supplied by Cantor’s theorem, even if the formal counting conditional is impeccable.

## 6. Conclusion: A Quasi-Logical Argument for Mind?

Rasmussen’s argument can be read through Chaïm Perelman and Lucie Olbrechts-Tyteca’s concept of *quasi-logical argumentation*. In [*The New Rhetoric*](https://undpress.nd.edu/9780268001919/the-new-rhetoric/), they examine forms of argument that gain persuasive force from their resemblance to formal demonstration while requiring substantive interpretive choices to apply those forms to a subject. Calling Rasmussen’s argument quasi-logical is not a claim that Cantor’s theorem is invalid or that his premises cannot form a valid conditional deduction. It locates the dispute over what the mathematical terms are taken to mean and what follows from their application.

Three steps remain distinct: establishing a conceivable mental property for every physical plurality, showing that these properties outnumber the appropriately specified physical domain, and explaining why a larger modal range identifies what is metaphysically fundamental. Mathematical modeling and cognitive science challenge an easy inference to the first; questions of individuation complicate the second; neither the mathematical result nor the appeal to simplicity establishes the third.

None of this demonstrates that idealism is false or physicalism true. It supports the narrower conclusion that the counting argument, as presented, does not yet establish the metaphysical priority of mind. If mind is fundamental, the case requires an independently defended account of representation, possibility, and grounding. Counting alone cannot provide it.
