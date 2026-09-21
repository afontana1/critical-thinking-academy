# Counting Possibilities, Reifying Mind

### A Critique of Joshua Rasmussen’s Counting Argument

## 1. Introduction: When Mathematics Becomes Metaphysics

Can a mathematical fact about the number of possible representations tell us what reality is fundamentally made of? In his [counting argument for mind-first metaphysics](https://worldviewdesign.substack.com/p/a-new-counting-argument-for-mind), philosopher Joshua Rasmussen suggests that mind is metaphysically prior to matter because it encompasses a greater range of possible realities. Drawing on Cantor’s theorem, he argues that possible mental realities outnumber possible nonmental realities, and that this numerical abundance provides a reason to regard mind as the fundamental basis of existence.

The argument is intriguing because it appears to transform a contentious metaphysical question into a mathematical problem. Yet the mathematical relationship itself does not establish the metaphysical conclusion. Rasmussen must additionally show that arbitrary collections of physical properties correspond to distinct conceivable mental properties, that mental and physical possibilities can be meaningfully compared, and that the cardinality of a possibility space bears upon ontological fundamentality.

This essay challenges those assumptions by drawing on mathematical modeling, cognitive science, and complexity theory. It argues that mental representation is characteristically selective: cognition makes complex realities tractable through abstraction and the allocation of limited cognitive resources, rather than by exhaustively reproducing their possible configurations. Moreover, even if Rasmussen’s proposed numerical correspondence were established, it would not follow that mind is ontologically prior to matter. The argument risks reifying mathematical and representational abstractions into claims about the fundamental structure of reality.

The issue, then, is not the validity of Cantor’s theorem, but whether its application to metaphysics can bear the philosophical weight Rasmussen places upon it.

## 2. Rasmussen’s Argument: From Cantor to the Priority of Mind

Rasmussen’s argument develops in two stages. In his 2015 paper, *Building Thoughts from Dust: A Cantorian Puzzle*, he advances a counting argument against a particular form of reductive physicalism. He begins with the premise that, for any plurality of physical properties, there is a corresponding conceivable mental property: the property of thinking that those properties are physical. Distinct pluralities, he maintains, determine distinct mental properties.

The mathematical component follows from Cantor’s theorem. Let \(P\) denote the set of physical properties, and let \(\mathcal{P}(P)\) denote its power set, comprising all subsets of \(P\). Cantor’s theorem establishes that:

$$
|\mathcal{P}(P)|>|P|
$$

If every subset of physical properties corresponds to a distinct conceivable mental property, then mental properties must outnumber physical properties. Rasmussen concludes that not every mental property can be identical to a physical property. His original argument therefore challenges a particular reductive identity theory without establishing that mind is metaphysically fundamental.

In his 2024 essay, *Mind Makes More*, Rasmussen extends this reasoning into a stronger metaphysical argument. He proposes that the most fundamental reality is the basis of the greatest range of possible realities. Mind, he argues, satisfies this condition because any possible nonmental reality can be mentally represented, while mental representations can also be combined through conceptual relations to generate additional possibilities. He therefore concludes that mind, rather than something mindless, constitutes the fundamental basis of reality.

This extension introduces two distinct philosophical commitments. First, arbitrary collections of physical properties must correspond to genuinely distinct conceivable mental properties. Second, the number of possibilities associated with a domain must provide some indication of its metaphysical fundamentality. Cantor’s theorem establishes neither proposition. The first concerns the nature and individuation of mental representations; the second concerns the relationship between possibility and ontological priority.

The argument’s mathematical validity is therefore not the central issue. What requires examination is whether these additional premises can support the metaphysical conclusion Rasmussen draws from them.

## 3. The Representation Problem: Cognition as Selective Modeling

Rasmussen’s counting argument depends upon the premise that arbitrary collections of physical properties correspond to distinct conceivable mental properties. Yet this raises a fundamental question: what does it mean for a mind to represent a physical reality? The answer is far from straightforward. Both scientific modeling and cognitive science suggest that representation is typically selective, preserving certain distinctions while disregarding others. This presents a significant challenge to Rasmussen’s account of mental representation.

Consider an NVIDIA A100 GPU. Even restricting our attention to its computational architecture, the device admits an enormous range of possible configurations involving memory contents, processing states, instruction sequences, and interactions between components. If we represent a simplified system as consisting of \(n\) independently variable components, its configuration space is given by:

$$
|\Omega|=\prod_{i=1}^{n}|X_i|
$$

where \(X_i\) denotes the possible states of component \(i\). Now extend this example to a computing cluster, introducing network configurations, communication delays, synchronization, and interactions between devices. The resulting configuration space becomes extraordinarily complex. An engineer cannot mentally enumerate every possible configuration, much less anticipate every possible interaction. Instead, engineers construct mathematical models, simulations, and abstractions that isolate particular aspects of the system.

This observation suggests something more fundamental than a limitation of human computational capacity. Mathematical models do not ordinarily reproduce their target systems in exhaustive detail. They represent those systems by selecting properties and relationships relevant to particular explanatory or practical purposes. As discussed in the *Stanford Encyclopedia of Philosophy’s* [entry on scientific models](https://plato.stanford.edu/entries/models-science/), abstraction and idealization are central features of scientific modeling, allowing otherwise intractable systems to become understandable.

A simplified model of GPU performance, for example, might map its physical configurations onto a smaller set of descriptions involving throughput, power consumption, and temperature:

$$
f:\Omega\rightarrow Z
$$

Two physically distinct configurations may produce the same model description:

$$
x_1\ne x_2
\qquad\text{while}\qquad
f(x_1)=f(x_2)
$$

The model has discarded certain physical distinctions without thereby ceasing to represent the system. Indeed, this selective abstraction may be precisely what makes the model useful.

A similar picture emerges from cognitive science. Herbert Simon’s theory of [bounded rationality](https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf) emphasizes that human agents must contend with limited capacities for comprehension and computation. Rather than exhaustively evaluating every possibility, they employ tractable procedures and simplified representations. John Vervaeke, Timothy Lillicrap, and Blake Richards develop the related problem of [relevance realization](https://contrastiveconvergence.net/~timothylillicrap/files/articles/relevance%20realization%20as%20an%20emerging%20framework%20in%20cogsci.pdf): how cognitive systems determine which features and relationships matter amid an overwhelming range of possibilities.

Other approaches reinforce the importance of selectivity. Dan Sperber and Deirdre Wilson’s [relevance theory](https://www.dan.sperber.fr/?p=93) connects the cognitive value of information to its effects and processing costs, while Falk Lieder and Thomas Griffiths’ [resource-rational analysis](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/resourcerational-analysis-understanding-human-cognition-as-the-optimal-use-of-limited-computational-resources/586866D9AD1D1EA7A1EECE217D392F4A) examines cognitive strategies in terms of the benefits and costs of computation. Although these approaches differ in scope and theoretical commitments, they converge on the importance of selective information processing. Cognition succeeds not by reproducing every available distinction, but by allocating representational and computational resources to those distinctions relevant to its purposes.

Admittedly, these empirical observations do not establish that every logically possible mind must possess the same limitations as human cognition. Nor does representing a large possibility space require enumerating its individual members: a compact mathematical expression can describe an infinite collection. Nevertheless, representing a collection as a whole is not equivalent to possessing a distinct conceivable mental property corresponding to every arbitrary subset of that collection.

This distinction exposes an ambiguity in Rasmussen’s premise. A mind can refer to the exact physical configuration of a GPU without encoding that configuration or distinguishing it from every alternative. If Rasmussen's mental properties require sufficiently detailed representations to discriminate between arbitrary physical pluralities, their unrestricted possibility demands independent justification. If, instead, they require only that thoughts refer to different pluralities, their distinctness may arise from differences in their referents rather than from any corresponding richness of cognitive representation.

The issue is therefore not simply whether minds possess sufficient computational resources. It is whether the capacity to refer to arbitrary physical possibilities establishes the distinct mental properties upon which Rasmussen’s counting argument depends. The existence of mathematical modeling and selective cognition gives us reason to question that inference. The next question is whether the resulting mental and physical properties can meaningfully be counted on comparable terms.

## 4. What Are We Counting? The Problem of Individuation

Even if every arbitrary plurality of physical properties could be mentally represented, Rasmussen must still establish that these representations correspond to distinct mental properties. Cantor’s theorem guarantees that the power set of a set is larger than the set itself, but it does not determine how mental or physical properties should be individuated. The cardinality comparison therefore depends upon philosophical assumptions about what counts as one property.

An initial difficulty concerns the apparent asymmetry between the domains being compared. Rasmussen counts physical properties on one side and mental properties constructed through arbitrary pluralities of physical properties on the other. Yet physical reality can also be described through configurations, relations, and higher-order structures. Rasmussen anticipates a related objection in his [2015 paper](https://joshualrasmussen.com/articles/building-thoughts-from-dust.pdf), arguing that unrestricted conjunctions of physical properties generate Russellian difficulties. This response, however, does not establish that the original comparison employs equivalent criteria of individuation. A physicalist need not endorse unrestricted conjunctions to maintain that physical configurations and relational structures deserve consideration. The question is whether the relevant domains have been specified on comparable terms.

A second difficulty concerns definability. Rasmussen maintains that physical realizability is unnecessary for his argument: what matters is that the relevant mental properties can be coherently defined. Yet a distinction exists between all mathematical subsets of a collection and those individually definable within a particular language. A countable formal language with finite expressions can define at most countably many objects through those expressions, whereas Cantor’s theorem establishes that:

$$
|\mathcal{P}(\mathbb{N})|=2^{\aleph_0}>\aleph_0
$$

This does not prove that conceivable mental properties are countable. Rather, it raises a question about whether a general definitional procedure establishes the existence of a distinct conceivable mental property for every arbitrary plurality.

Rasmussen might respond that mental properties are individuated by their intentional contents rather than by the internal resources required to represent them. Different physical pluralities would then determine different mental properties simply because the thoughts concern different things. But this response introduces a further difficulty: the alleged abundance of mental properties would depend upon the physical pluralities used to distinguish their contents. It would not independently demonstrate a greater richness of mental representation.

The counting argument thus requires more than Cantor’s theorem. It requires a defensible account of mental individuation and a justification for comparing mental and physical properties under the proposed criteria. Without these, the purported numerical superiority of mind remains philosophically underdetermined.

## 5. Possibility, Complexity, and the Reification of Mathematical Abstractions

Even if Rasmussen successfully established that possible mental properties outnumber physical properties, a more fundamental question would remain: why should numerical abundance establish metaphysical priority? In *Mind Makes More*, Rasmussen proposes that the most fundamental reality is the basis of the greatest range of possible realities. Yet this principle requires independent justification. The size of a possibility space does not, by itself, establish what grounds the realities it describes.

Consider the distinction between possibility and actuality in systems engineering. Engineers may begin with a broad possibility space of conceivable configurations, progressively restrict it through physical and practical constraints, evaluate alternatives within a trade space, and ultimately implement a particular design. The initial possibility space may vastly exceed the range of realizable configurations, while the actual system represents only one outcome among many alternatives. Nevertheless, the size of the possibility space tells us nothing directly about the ontological constitution of the implemented system. A mathematical description of every conceivable aircraft configuration does not establish that the aircraft is fundamentally constituted by its possibility space.

The distinction can be expressed as:

$$
\text{Modal abundance}\not\Rightarrow\text{Ontological priority}
$$

Rasmussen’s principle consequently risks conflating the logical scope of what can be conceived with the metaphysical basis of what exists. Even if mind were capable of representing every logically possible physical configuration, it would not follow that physical reality depends upon mind for its existence.

Complexity science provides a further reason to question the intuition underlying this principle. Relatively simple components and generative rules can produce extraordinarily large spaces of possible configurations. A system consisting of \(n\) independent binary components, for example, admits:

$$
|\Omega|=2^n
$$

possible configurations. The number of configurations grows exponentially despite the simplicity of the underlying components. More generally, interactions among elementary components can generate elaborate higher-order structures and behaviors without requiring the fundamental components themselves to exhibit comparable complexity.

This does not establish that Rasmussen’s metaphysical principle is false. His notion of fundamentality may differ from the relationships examined in complexity science. Nevertheless, generative systems demonstrate that numerical abundance at a higher level is entirely compatible with a comparatively simple underlying basis. There is no evident general principle requiring the number of fundamental properties to equal or exceed the number of configurations they can generate.

A final difficulty concerns the relationship between representation and grounding. A mathematical model can represent a physical system without constituting its ontological foundation. Likewise, a computer simulation can represent a hurricane without the hurricane depending upon that simulation for its existence. Representation and metaphysical grounding are different relations, and the existence of the former does not establish the latter.

This is where Rasmussen’s argument risks reification. An abstract mathematical correspondence between physical possibilities and conceivable mental properties is treated as evidence of a substantive hierarchy of reality. Yet the transition from mathematical construction to mental representation, and subsequently from representation to ontological fundamentality, requires justification at each stage. Cantor’s theorem cannot supply these missing connections.

The decisive philosophical work is therefore performed not by the counting argument itself, but by Rasmussen’s additional metaphysical principle. Unless the relationship between possibility, representation, and grounding can be independently established, the numerical abundance of conceivable mental properties provides no sufficient basis for concluding that mind is metaphysically prior to matter.

## 6. Conclusion: A Quasi-Logical Argument for Mind?

Joshua Rasmussen’s counting argument can be understood through Chaïm Perelman and Lucie Olbrechts-Tyteca’s concept of *quasi-logical argumentation*. In *The New Rhetoric*, they examine arguments that derive persuasive force from their resemblance to formal logical or mathematical demonstrations, while depending upon substantive assumptions that permit those formal structures to be applied to particular subjects.

Rasmussen’s argument exhibits this tension. Cantor’s theorem establishes a rigorous mathematical relationship, but its application to mental properties depends upon an independently justified account of representation and individuation. Mathematical modeling and cognitive science suggest that cognition operates through selective abstraction rather than exhaustive reproduction of physical possibilities. Moreover, even if the proposed numerical correspondence were established, the inference from a larger possibility space to greater metaphysical fundamentality would remain unsupported.

The argument’s difficulty, therefore, is not mathematical but philosophical. It risks treating the abstract possibilities generated through representation as evidence of an ontological hierarchy, without establishing the relationship between representation and grounding. Its apparent deductive force depends upon metaphysical commitments that the counting procedure itself cannot justify.

None of this demonstrates that idealism is false or that physicalism is true. It establishes a narrower conclusion: the cardinality of conceivable mental properties does not, by itself, establish the metaphysical priority of mind. If mind is fundamental, that conclusion requires an argument that counting alone cannot provide.
