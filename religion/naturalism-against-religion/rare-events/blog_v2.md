# Table of Contents

- [Introduction: What Are the Odds?](#introduction)
- [I. A World Full of Improbable Events](#i-world-full-of-improbable-events)
  - [Littlewood and the Ordinary Extraordinary](#littlewood-ordinary-extraordinary)
  - [Dyson, Diaconis, and the Law of Truly Large Numbers](#dyson-diaconis-truly-large-numbers)
  - [From Local Rarity to Global Expectation](#local-rarity-global-expectation)
- [II. From Improbability to Significance](#ii-improbability-to-significance)
  - [Exact Outcomes and Meaningful Patterns](#exact-outcomes-meaningful-patterns)
  - [Events, Descriptions, and Hidden Multiplicity](#events-descriptions-hidden-multiplicity)
  - [Searching for Significance: The Look-Elsewhere Effect](#look-elsewhere-effect)
  - [Event Selection, Description Selection, and Meaning](#event-description-selection-meaning)
- [III. From Improbability to Divine Agency](#iii-improbability-to-divine-agency)
  - [Surprise, Evidence, and the Bayesian Structure](#surprise-evidence-bayesian-structure)
  - [Divine Psychology: Capability, Propensity, and the Action Space](#divine-psychology-action-space)
  - [Post-Hoc Intention and the Prediction–Accommodation Distinction](#post-hoc-intention-prediction-accommodation)
  - [Inscrutable Intentions and the Non Sequitur](#inscrutable-intentions-non-sequitur)
- [IV. Accommodation, Prediction, and Model Overfitting](#iv-accommodation-prediction-overfitting)
  - [The Overfitting Analogy and Bayesian Complexity](#overfitting-bayesian-complexity)
  - [Retrospective Precision and Predictive Weakness](#retrospective-precision-predictive-weakness)
  - [A Theory That Explains Everything](#theory-that-explains-everything)
  - [Searching the Intention Space](#searching-intention-space)
- [V. Miracle Attribution in Practice](#v-miracle-attribution-in-practice)
  - [Theological Pluralism and Model-Relative Interpretation](#theological-pluralism-model-relative)
  - [The Plane-Crash Survivor and Survivorship Bias](#plane-crash-survivorship-bias)
  - [Prayer, Asymmetric Interpretation, and One-Sided Updating](#prayer-asymmetric-updating)
- [VI. From Interpretation to Evidence: The Probabilistic Anatomy of a Miracle](#vi-interpretation-to-evidence)
  - [Three Inferential Steps](#three-inferential-steps)
  - [A Better Standard for Miracle Claims](#better-standard-miracle-claims)
  - [What a Strong Case Might Look Like](#strong-case)
  - [Limits, Unknowns, and What the Argument Does Not Show](#limits-unknowns)
  - [Evidence at the Level of the Process](#evidence-process-level)
  - [A General Epistemic Principle](#general-epistemic-principle)
  - [A More Careful Vocabulary](#careful-vocabulary)
- [Conclusion: From Anomaly to Intention](#conclusion)

---

<a id="introduction"></a>
# Introduction: What Are the Odds?

One of the most persistent sources of confusion about improbable events is the tendency to treat rarity as though it were an intrinsic property of an event. We say that something was “one in a million,” “astronomically unlikely,” or “almost impossible,” as though those descriptions alone settled how surprising the event should be. But probability does not work that way. An event is rare only relative to a probability model, a description of what counts as the event, and a set of opportunities in which it might occur.

That distinction matters because an event can be extraordinarily improbable on any one occasion while being entirely expected somewhere across a sufficiently large collection of occasions. The probability that a particular person wins a lottery may be vanishingly small, while the probability that *someone* wins may be close to certainty. There is no paradox. These are simply different events embedded in different reference classes.

The same principle applies far beyond lotteries. A coincidence that would be astonishing if there were only one opportunity for it to occur may become routine when there are millions of opportunities. A statistical outlier that would be alarming in a single experiment may be expected somewhere among millions of experiments. A sequence of events that seems almost impossibly specific when described afterward may be only one of an enormous number of equally improbable sequences that could have occurred. The probability of an event considered in isolation therefore tells us less than it first appears to. We also need to know the size and structure of the event space in which it occurs.

This becomes especially important when improbable events are described as miracles. The central question is not whether extraordinary events occur; probability theory virtually guarantees that they will. The harder questions concern **which events we notice, how we describe them, and what we infer from them**. An event may be rare without being globally unexpected, globally unexpected without being intentional, and intentional without being divine. The argument developed here moves through those distinctions in sequence: first from local rarity to large event spaces, then from events to descriptions and selection effects, and finally from improbability to Bayesian evidence and divine intention.

<a id="i-world-full-of-improbable-events"></a>
# I. A World Full of Improbable Events

<a id="littlewood-ordinary-extraordinary"></a>
## Littlewood and the Ordinary Extraordinary

This general intuition is associated with what has come to be called Littlewood's law. J. E. Littlewood observed that extremely improbable events should not astonish us as much as they ordinarily do once we take into account the sheer number of events available across a human lifetime. His memorable point was that, with “a lifetime to choose from,” odds of a million to one are not especially formidable.

The phrase *to choose from* is doing important work. A human life does not present us with one predetermined probabilistic trial. It presents an enormous sequence of experiences: conversations, encounters, illnesses, journeys, thoughts, dreams, accidents, phone calls, deaths, recoveries, names, numbers, dates, memories, and coincidences. Each of these can participate in countless possible relationships with others. We are not asking whether one narrowly specified extraordinary event will happen once; we are living through an immense collection of opportunities for something extraordinary to happen.

Suppose some type of event has probability

$$
p=10^{-6}
$$

on any particular opportunity. Calling it a “one-in-a-million event” sounds impressive. But now suppose there are a million opportunities for such an event to occur. The expected number of occurrences is

$$
\mathbb{E}[X]=Np,
$$

where $$N$$ is the number of opportunities. If

$$
N=10^6
$$

and

$$
p=10^{-6},
$$

then

$$
\mathbb{E}[X]=1.
$$

Nothing about the event itself has become more probable on any individual trial; it remains a one-in-a-million event. What changes is the number of opportunities available for one such event to appear. This gives us a distinction that will matter throughout the discussion:

$$
\text{local improbability}\neq\text{global rarity}.
$$

An event can remain highly improbable at the level of any particular opportunity while becoming common at the level of an entire population of opportunities.

<a id="dyson-diaconis-truly-large-numbers"></a>
## Dyson, Diaconis, and the Law of Truly Large Numbers

Freeman Dyson later gave this intuition a more quantitative and memorable formulation. He imagined that a person encounters roughly one experientially significant event per second while awake. Over a sufficiently long period, this produces on the order of a million events. If a “miracle” is defined, somewhat playfully, as an event with probability around one in a million, then a person should expect such a miracle with some regularity.

Dyson's calculation is heuristic rather than literal. There is no precise psychological unit called an “event,” and human experiences are not independent, identically distributed trials. Its purpose is to expose a mistake in intuition. We often move from the statement

> This event had only a one-in-a-million chance of happening.

straight to the conclusion

> Something extraordinarily unusual has therefore occurred.

But that conclusion does not follow until we know how many opportunities existed. With one opportunity, a one-in-a-million result is astonishing. With a million opportunities, one such result is roughly what we should expect. With a billion opportunities, many such results should occur.

The relevant quantity is therefore not simply $$p$$, but the relationship between probability and the number of opportunities. For a rare event with probability $$p$$ occurring across $$N$$ independent opportunities, the probability that it occurs at least once is

$$
P(\text{at least one occurrence})
=
1-(1-p)^N.
$$

When $$p$$ is small and $$N$$ is large, this is well approximated by

$$
P(\text{at least one occurrence})
\approx
1-e^{-Np}.
$$

The product $$Np$$ therefore gives us a useful scale. If

$$
Np\ll1,
$$

the event remains genuinely unusual even across all the available opportunities. If

$$
Np\approx1,
$$

we should expect it occasionally. And if

$$
Np\gg1,
$$

we should expect it repeatedly. The counterintuitive result is that an event can be individually spectacular and collectively mundane at the same time.

Persi Diaconis and Frederick Mosteller developed this general insight in their work on coincidences. Their formulation is often summarized as the **law of truly large numbers**: with a sufficiently large sample, almost any outrageous event is likely to occur. This should not be confused with the ordinary law of large numbers, which concerns the tendency of sample averages to converge toward expected values as the number of observations increases. The law of truly large numbers is an informal principle about rare events: if the number of opportunities becomes sufficiently enormous, events with very small individual probabilities should eventually occur.

Suppose, for example, that an event has probability

$$
p=10^{-6}.
$$

With only one opportunity, its occurrence would be highly surprising. With one million independent opportunities,

$$
P(\text{at least one occurrence})
=
1-(1-10^{-6})^{10^6},
$$

which is approximately

$$
1-e^{-1}\approx0.632.
$$

So a one-in-a-million event has roughly a 63 percent chance of occurring at least once across a million opportunities. With ten million opportunities,

$$
Np=10,
$$

and therefore

$$
P(\text{at least one occurrence})
\approx
1-e^{-10},
$$

which is effectively certainty. Again, there is no contradiction. The event remains one in a million on each individual opportunity, but the world has supplied so many opportunities that its appearance somewhere becomes unsurprising.

This produces one of the most important conceptual reversals in thinking about extraordinary events. The intuitive question is often:

> How unlikely was this event?

But the more relevant question may be:

> How unlikely was it that no event of this general kind would happen anywhere among all the available opportunities?

Those are very different questions.

There is also a useful distinction between an **expected count** and a **guaranteed occurrence**. When $$N=10^6$$ and $$p=10^{-6}$$, the expected number of occurrences is one, but the probability of seeing at least one is only about 63 percent. The expected value tells us the long-run average number of rare events across repeated collections of opportunities; it does not promise that each collection will contain exactly one. This is worth emphasizing because Dyson's heuristic is best understood as a statement about rates of occurrence, not as a schedule according to which a person should literally experience one miracle at fixed intervals.

Real life also departs from the simple model in another way: opportunities are neither perfectly independent nor identically distributed. Some events cluster, some people have more opportunities than others, and the probability of a particular kind of coincidence may change with context. Those complications matter for precise calculation, but they do not overturn the underlying point. Once a process supplies a very large number of opportunities, the relevant probability is determined by the entire opportunity structure, not by the small probability attached to one isolated trial.

This is where the law of truly large numbers begins to connect with the later problem of selection. Counting opportunities already requires us to decide what would have counted as a relevant occurrence. A million opportunities for *this exact event* is not necessarily the same thing as a million opportunities for *something we would have found equally remarkable*. The first question concerns repetition of a specified event; the second concerns a family of possible events. That distinction becomes increasingly important once the event is identified only after it has happened.

<a id="local-rarity-global-expectation"></a>
## From Local Rarity to Global Expectation

The same reasoning applies to statistical extremes. Suppose an observation lies six standard deviations from the mean under a normal distribution. In the context of one carefully specified observation, such an event would be extraordinarily unusual. But if an enormous number of observations are being generated across the world, extreme deviations become inevitable somewhere. “Six sigma” can sound like an absolute description of extraordinariness, but it is not. It is a statement relative to a distribution, a specified observation, and a set of opportunities.

This is true at every scale. Financial markets generate millions of price movements; hospitals observe millions of patients; billions of people dream, think about friends and relatives, receive medical treatments, survive accidents, miss accidents, have conversations, pray, and encounter countless combinations of names, dates, places, and personal histories. Even before we consider any special human tendency to notice patterns, the opportunity space is immense. A world containing billions of observers will continuously generate events that are fantastically improbable from the perspective of any one observer.

The lottery provides perhaps the cleanest illustration. Suppose a lottery gives each ticket holder a one-in-300-million chance of winning. For any particular person,

$$
P(\text{that person wins})
=
\frac{1}{300,000,000}.
$$

That probability is extraordinarily small. Yet if hundreds of millions of tickets are sold, the probability that *someone* wins may be substantial or overwhelming, depending on the structure of the lottery. When the winner appears on television, two statements can therefore be true at once:

> It was extraordinarily unlikely that this particular person would win.

and

> It was entirely unsurprising that someone would eventually occupy the role of winner.

The first statement does not contradict the second. The person who experiences an extraordinary coincidence occupies an analogous position. From inside the event, it can feel almost impossibly specific: *Why me? Why this event? Why now?* But somebody had to occupy one of the tails of the distribution. Once the population of opportunities becomes sufficiently large, the existence of someone asking “Why me?” may itself be expected.

This suggests a deeper principle: there is no meaningful probability of an event until we define what counts as the event. Compare

$$
P(\text{I win this lottery})
$$

with

$$
P(\text{someone wins this lottery}),
$$

or

$$
P(\text{this patient experiences an extraordinary recovery})
$$

with

$$
P(\text{some patient somewhere experiences an extraordinary recovery}).
$$

Likewise, compare

$$
P(\text{I think of this particular friend five minutes before they call})
$$

with

$$
P(\text{some personally meaningful coincidence occurs somewhere in my lifetime}).
$$

The first probability in each pair can be minuscule while the second is much larger. So describing an event as “one in a million” is incomplete. One in a million *what*—people, attempts, days, descriptions, or opportunities? Without specifying the relevant event space, statements about improbability can create an illusion of explanatory depth.

None of this yet tells us whether any event called a miracle is or is not miraculous. The more basic conclusion is that a rare event does not require a special explanation merely because it is rare. In sufficiently large event spaces, rare events are exactly what probability theory predicts. Indeed, a world in which no extremely improbable events ever occurred would itself be statistically peculiar. The first lesson can therefore be stated simply:

$$
\text{improbable on one trial}
\neq
\text{unexpected somewhere across many trials}.
$$

If we want to know whether an extraordinary event genuinely requires an extraordinary explanation, it is not enough to calculate the probability of that event in isolation. We must also ask how many opportunities existed for something comparably extraordinary to occur. Once we do that, however, a second problem appears: **which event are we calculating the probability of?** An exact outcome may be extraordinarily improbable while remaining completely unremarkable, whereas another outcome with precisely the same probability may strike us as astonishing because it possesses a recognizable pattern or personal significance. The next question, then, is not merely why improbable events occur, but why certain improbable events become *meaningful*.

<a id="ii-improbability-to-significance"></a>
# II. From Improbability to Significance

The previous section established that rare events should occur frequently whenever the number of opportunities becomes sufficiently large. But that leaves another problem unresolved. Even if improbable events are inevitable, why do some of them strike us as extraordinary while others pass unnoticed? The answer cannot simply be that the events we notice are less probable. In fact, almost every sufficiently specific event is extraordinarily improbable. What distinguishes a meaningful coincidence from an ordinary occurrence is usually not its exact probability, but the way we describe it.

This matters because many arguments from extraordinary events begin by calculating the probability of a highly specific description after the event has already occurred. The resulting number may indeed be tiny. But a tiny number is not yet an explanation of why the event should surprise us. Before we can interpret the probability, we have to ask how the description itself was selected.

<a id="exact-outcomes-meaningful-patterns"></a>
## Exact Outcomes and Meaningful Patterns

Consider a thoroughly shuffled deck of fifty-two cards. There are

$$
52!
$$

possible arrangements of the deck, so the probability of any particular ordering is

$$
P(E)=\frac{1}{52!},
$$

or approximately

$$
1.24\times10^{-68}.
$$

That is an unimaginably small probability. Suppose I shuffle the deck and obtain some unremarkable-looking arrangement:

> 8 of clubs, queen of hearts, 3 of diamonds, jack of spades, and so on.

The exact sequence I obtained had probability on the order of

$$
10^{-68}.
$$

Yet nobody would regard the shuffle as miraculous, because some arrangement had to occur. Every possible ordering is individually fantastically improbable, while the probability that *some ordering* occurs is simply

$$
1.
$$

The lesson is basic but easy to miss:

> **An event can have an extraordinarily small probability as an exact outcome without being surprising in any meaningful sense.**

Now imagine that I shuffle the same deck and produce ace through king of spades, followed by ace through king of hearts, then diamonds, then clubs. The exact probability of that sequence is still

$$
\frac{1}{52!}.
$$

It is no more or less probable than the random-looking ordering. And yet virtually everyone would regard the perfectly ordered deck as requiring explanation. The difference is not mathematical probability at the level of the exact sequence. The difference is that the ordered sequence belongs to a **simple, recognizable category** that was available to us independently of the shuffle. We can describe it succinctly: “the deck is perfectly sorted by suit and rank.” The random-looking sequence, by contrast, generally has no comparably simple description beyond listing the sequence itself.

So two events can have identical exact probabilities while differing enormously in perceived significance. When we judge an event extraordinary, we are rarely responding to its microscopic exactness. We are responding to a pattern or description instantiated by the event. That distinction is crucial for coincidences and miracles, because it means that the probability of the physical outcome and the probability of the *salient description* are not automatically the same problem.

<a id="events-descriptions-hidden-multiplicity"></a>
## Events, Descriptions, and Hidden Multiplicity

An event is not identical to the description under which we notice it. Suppose I encounter a person at an airport. That single physical occurrence can be described in countless ways: the person is wearing a blue shirt; they were born in the same state as me; their first name matches my grandfather's; their birthday is two days after mine; they attended the same university as an old friend; they once lived on a street with the same name as the street where I grew up; or I met them exactly ten years after some other memorable event. Many of these descriptions could be true simultaneously.

Let the event be $$E$$, and let

$$
f_1(E), f_2(E), \ldots, f_k(E)
$$

represent different possible descriptions of it. After observing $$E$$, we can search among these descriptions and notice whichever one produces an interesting relationship. Perhaps

$$
f_{417}(E)
$$

turns out to have a remarkable connection to something personally meaningful. We then experience that relation as though it were simply *the event*: “What were the odds that this would happen?”

But the relevant probabilistic process was not necessarily

$$
P(f_{417}(E)).
$$

That description may have been selected only because it happened to generate an interesting result. Before the event occurred, we might have been impressed by hundreds or thousands of other relationships. A more relevant question may therefore resemble

$$
P\left(
\bigcup_{i=1}^{k}
\{f_i(E)\text{ produces a salient pattern}\}
\right),
$$

which can be much larger than the probability of the single description eventually selected.

A familiar coincidence makes the problem intuitive. You suddenly think about an old friend whom you have not spoken to in years, and five minutes later the friend calls. The experience can feel astonishing, and one might ask: “What were the odds that this specific person would call within five minutes of my thinking about them?” Perhaps those odds are indeed very small. But that calculation silently assumes that this exact coincidence was the target all along.

Usually it was not. You might also have been impressed if the friend had called later that day, sent an email, appeared unexpectedly, or been mentioned by someone else. You might have dreamed about another person and heard from them the next morning, thought of a song just before hearing it, mentioned a city and then received news from someone there, or remembered an old teacher and then encountered a former classmate. If any of those outcomes would have prompted the same “What are the odds?” reaction, then they belong, in some sense, to the relevant opportunity space.

The relevant comparison is therefore not merely

$$
P(\text{this specific friend calls within five minutes}),
$$

but something closer to

$$
P(\text{some personally striking coincidence occurs among all such opportunities}).
$$

Those quantities may differ by orders of magnitude. This adds another dimension to the law of truly large numbers. It is not only that there are many events; there are also many ways to describe each event. If a person experiences $$N$$ events and each event admits many potentially salient descriptions, the effective space in which coincidences can be discovered becomes much larger than $$N$$ alone. We should not take a crude product such as

$$
NK
$$

as a literal count in most real-world cases—the descriptions overlap and are not independent—but it captures the conceptual point. A large event space becomes an even larger **event-description space**.

Our intuitions about rarity often ignore this hidden multiplicity. We imagine that “this extraordinarily specific coincidence happened,” when a more faithful description may be: “Among a huge number of events, one event possessed one of a huge number of properties that I found interesting.” Those are very different probabilistic statements.

The deeper issue is that probability depends on how the outcome space is **partitioned**. The same physical outcome can be placed into a very narrow category or a much broader one. “This exact sequence of fifty-two cards” defines an extraordinarily narrow class; “a deck perfectly ordered by suit and rank” defines a recognizable structural class; “some conspicuously non-random-looking arrangement” defines a broader class still. The probability changes because the event being measured changes. There is therefore no contradiction in saying that an outcome is astronomically improbable under one description and much less surprising under another.

That matters especially when the description is chosen after observation. Suppose $$D_1, D_2, \ldots, D_k$$ are different descriptions that would each have struck us as remarkable, and after seeing the data we report only $$D_j$$, the one that happened to fit. The probability relevant to the search process is not generally just

$$
P(D_j).
$$

It is closer to the probability that **at least one** member of the family would have been realized:

$$
P\left(\bigcup_{i=1}^{k}D_i\right).
$$

The descriptions need not be independent, so we cannot usually obtain that probability by simply adding their individual probabilities. The important point is more basic: selecting $$D_j$$ after the fact hides the multiplicity of the search. A post-hoc probability can therefore be mathematically correct as a statement about the selected description while still being evidentially misleading as a statement about the process that generated our surprise.

<a id="look-elsewhere-effect"></a>
## Searching for Significance: The Look-Elsewhere Effect

Statistics has a formal analogue of this problem: the **look-elsewhere effect**. Suppose a scientist performs one hypothesis test with a false-positive rate of

$$
\alpha=0.05.
$$

Under the null hypothesis, there is a 5 percent chance of obtaining a nominally significant result. But suppose the scientist performs one hundred independent tests. The probability of obtaining at least one false positive becomes

$$
P(\text{at least one})
=
1-(1-\alpha)^{100}.
$$

Substituting $$\alpha=0.05$$ gives

$$
P(\text{at least one})
=
1-(0.95)^{100}
\approx
0.994.
$$

Even though any particular test has only a 5 percent false-positive rate, it is nearly certain that *some* apparently significant result will appear if enough tests are conducted. This is why statistical analysis cannot simply report the most interesting result from a large search as though that result had been the only hypothesis tested. The number of places one looked matters.

Human cognition performs an informal version of this search constantly. We notice relationships among names, birthdays, dates, memories, dreams, conversations, locations, illnesses, prayers, deaths, recoveries, songs, numbers, anniversaries, family histories, and chance encounters. The search is not necessarily deliberate. We are simply very good at recognizing patterns when they appear. But probabilistically the structure is similar: if we search enough possible relationships, some will be striking.

The Texas sharpshooter fallacy captures the same idea. Imagine someone firing a large number of bullets randomly at the side of a barn. Afterward, the shooter finds the densest cluster of bullet holes and paints a target around it. The cluster may genuinely be tight, and if the target had been painted there *before* the shooting, the result would be impressive. But because the target was drawn afterward, the probability calculation changes completely. The shooter was effectively allowed to search the entire barn for whichever region happened to contain the best cluster.

The relevant event was not

$$
\text{“the bullets cluster around this predetermined point.”}
$$

It was closer to

$$
\text{“some region of the barn contains an unusually tight cluster.”}
$$

The latter event is much more probable. This is precisely why post-hoc specification matters. A pattern discovered after the data are observed cannot ordinarily be assigned the same evidential significance as a pattern specified before the data were generated.

Many extraordinary coincidences have this structure. Reality generates an outcome; we inspect it; we discover an interesting description; and only then do we calculate the improbability of that description. The resulting probability need not be mathematically wrong. It may be perfectly correct that

$$
P(D)=10^{-9}
$$

for some narrowly defined description $$D$$. The evidential difficulty is that $$D$$ was selected from a large family of descriptions only after the outcome was known. The calculation answers the question “How often would this particular description occur?” when the phenomenon requiring explanation may instead be “How often would some sufficiently striking description be found?” Those are not the same question.

<a id="event-description-selection-meaning"></a>
## Event Selection, Description Selection, and Meaning

Description selection is only part of the story. Before we ever choose a description, we have already selected which events deserve attention. We do not analyze every event that happens to us. Most disappear from memory almost immediately: ordinary conversations, unremarkable journeys, thoughts that lead nowhere, people we think about who never call, prayers followed by nothing memorable, illnesses that proceed normally, and coincidences that almost line up but do not. These events generally do not become stories. The exceptional case does.

The first filtering process is therefore **event selection**:

$$
\text{all events}
\rightarrow
\text{salient events}
\rightarrow
\text{events remembered and reported}.
$$

The set of events we hear about is consequently highly filtered. We disproportionately encounter the strange coincidence rather than the millions of non-coincidences surrounding it, the improbable recovery rather than the enormous number of ordinary recoveries, and the thought immediately followed by a phone call rather than the thousands of thoughts followed by nothing relevant. The extraordinary event is selected from a much larger background that is psychologically invisible.

Once an event has been selected, **description selection** begins. We identify whichever properties make the event interesting:

$$
\text{selected event}
\rightarrow
\text{many possible descriptions}
\rightarrow
\text{salient description}.
$$

These two processes reinforce one another. First we select unusual events; then, within those events, we select unusual descriptions. By the time the event reaches conscious reflection or becomes a story told to others, the object being analyzed may already have passed through several layers of filtering. It can therefore look far more probabilistically exceptional than the underlying generative process really was.

None of this requires us to say that the event lacks personal meaning. A coincidence can be genuinely moving; an unlikely recovery can transform someone's life; an unexpected encounter can carry tremendous emotional significance. Probability theory does not dictate what an event is allowed to mean to a person. The distinction is between **personal significance** and **evidential significance**. An event may matter enormously without its subjective importance telling us why it occurred.

That distinction becomes especially important once the event is interpreted not merely as meaningful, but as intentional. At this point the structure is beginning to emerge: an enormous world produces vast numbers of improbable events; one unusual event is selected; one meaningful description of it is selected; and the resulting event now appears extraordinarily unlikely under a very specific description. A miracle claim commonly goes one step further. The observer concludes not merely that the event was extraordinary, but that it happened for a reason—that someone intended it.

That inference introduces an entirely new probabilistic problem. An unlikely event and an intentionally produced event are not the same category. The fact that an event appears improbable under one selected description does not, by itself, establish that an agent selected the outcome. The argument has moved from probability to agency. Once divine agency is proposed, the relevant question becomes unavoidable:

> Even if this event was extraordinarily unlikely under ordinary natural processes, how likely was it under the hypothesis of divine intention?

That is where the analysis must become Bayesian.

<a id="iii-improbability-to-divine-agency"></a>
# III. From Improbability to Divine Agency

Once an event has been selected as extraordinary and described in a way that makes its improbability salient, a common next step is to infer agency. The reasoning often takes roughly this form:

1. Event $$E$$ occurred.
2. The event $$E$$ was extremely improbable under ordinary natural processes.
3. Therefore ordinary natural processes are an inadequate explanation.
4. Therefore $$E$$ was probably intentional.
5. Therefore divine intervention is a plausible or likely explanation.

The intuitive force of the argument comes from the first two steps. If something appears too improbable to have happened naturally, it is tempting to conclude that some intelligence must have intended it. But the inference moves too quickly. The fact that an event is improbable under one hypothesis does not establish that another hypothesis is probable. At minimum, we must ask whether the alternative hypothesis actually made the event more likely.

That is a Bayesian question.

<a id="surprise-evidence-bayesian-structure"></a>
## Surprise, Evidence, and the Bayesian Structure

Let

$$
N=\text{the event arose through non-divine natural processes}
$$

and

$$
D=\text{the event resulted from divine intervention}.
$$

After observing event $$E$$, the posterior odds are

$$
\frac{P(D\mid E)}{P(N\mid E)}
=
\frac{P(D)}{P(N)}
\times
\frac{P(E\mid D)}{P(E\mid N)}.
$$

The equation separates prior belief from evidential discrimination. The first term,

$$
\frac{P(D)}{P(N)},
$$

is the prior odds. The second,

$$
\frac{P(E\mid D)}{P(E\mid N)},
$$

is the **Bayes factor**: the degree to which the observed event favors one hypothesis over the other.

A useful way to keep the relevant quantities distinct is the following:

| Question | Quantity | What it tells us |
|---|---|---|
| How surprising is the event under natural processes? | $$P(E\mid N)$$ | Natural improbability |
| How expected is the event under divine intervention? | $$P(E\mid D)$$ | Predictive content of the divine hypothesis |
| Which hypothesis does the event favor? | $$\frac{P(E\mid D)}{P(E\mid N)}$$ | Evidential discrimination, or the Bayes factor |
| How probable is divine intervention after observing the event? | $$P(D\mid E)$$ | Posterior belief after priors and evidence are combined |

This immediately reveals the weakness in the common miracle inference. The relevant question is not merely “How improbable was $$E$$ under natural processes?” but “How much more probable was $$E$$ under divine intervention than under natural processes?”

Suppose

$$
P(E\mid N)=10^{-9}.
$$

That is an extraordinarily small probability. If we stop there, the event sounds overwhelmingly mysterious. But now suppose

$$
P(E\mid D)=10^{-9}.
$$

Then the Bayes factor is

$$
BF=
\frac{10^{-9}}{10^{-9}}
=1.
$$

The event is highly surprising under both hypotheses and therefore provides no evidence favoring one over the other. If instead

$$
P(E\mid D)=10^{-12},
$$

then

$$
BF=
\frac{10^{-12}}{10^{-9}}
=
10^{-3}.
$$

The event would actually favor the natural hypothesis over the divine one. Only if

$$
P(E\mid D)\gg P(E\mid N)
$$

does the observation provide substantial evidence for divine intervention. Thus the statement “This event was extraordinarily unlikely naturally” does not, by itself, establish “This event was probably divinely caused.” What is missing is a comparative likelihood.

Information theory makes the same distinction especially clear. The surprisal of an event under hypothesis $$H$$ is

$$
I(E\mid H)
=
-\log_2P(E\mid H).
$$

If

$$
P(E\mid N)=2^{-30},
$$

then the event contains thirty bits of surprise under the natural hypothesis. But evidence for $$D$$ over $$N$$ depends on

$$
\log_2
\frac{P(E\mid D)}{P(E\mid N)}.
$$

If

$$
P(E\mid D)=2^{-30},
$$

then

$$
\log_2BF
=
\log_2
\frac{2^{-30}}{2^{-30}}
=
0.
$$

The event contains thirty bits of surprise but zero bits of evidence favoring divine intervention. The distinction is fundamental:

> **Surprise measures how unexpected an event is under a hypothesis. Evidence measures how differently competing hypotheses expected it.**

A miracle argument that focuses only on natural improbability confuses these two quantities.

<a id="divine-psychology-action-space"></a>
## Divine Psychology: Capability, Propensity, and the Action Space

At this point a deeper problem emerges. Suppose the proposed explanation is simply, “God caused $$E$$.” What exactly does that tell us about

$$
P(E\mid D)?
$$

Not very much by itself. A divine being may be capable of producing $$E$$, but capability is not the same as likelihood. The statement “God could have done this” establishes, at most, that the event is compatible with divine agency. It does not tell us whether God would be likely to choose that event rather than any of the alternatives.

Bayesian analysis therefore forces a question that miracle arguments often leave implicit: **why would this being choose this particular action, at this particular time, involving this particular person, rather than one of the enormous number of other actions available?** This is the problem of divine psychology.

Suppose an agent is capable of actions

$$
A_1,A_2,\ldots,A_k.
$$

If the agent is divine, the action space may be enormous. The probability of observing $$E$$ under divine intervention can be represented schematically as

$$
P(E\mid D)
=
\sum_i
P(E\mid A_i,D)P(A_i\mid D).
$$

Even if there is some action $$A_E$$ such that

$$
P(E\mid A_E,D)=1,
$$

we still need to know

$$
P(A_E\mid D).
$$

In other words, how likely is the deity to choose the action that produces $$E$$? Without an independent theory of divine preferences, motivations, goals, constraints, or intentions, that probability may be difficult or impossible to establish. A miracle argument often treats divine agency as though it automatically assigns high probability to the observed event, but merely saying “God wanted this to happen” after the event occurred does not show that the event was probable under a divine hypothesis beforehand.

We can make the same point by introducing an explicit variable for intention. Let $$I_i$$ represent a possible divine intention. Then a broad divine hypothesis has a predictive distribution of the form

$$
P(E\mid D)
=
\sum_i P(E\mid I_i,D)P(I_i\mid D).
$$

The first factor asks what outcome would follow if a particular intention were present; the second asks how much probability the theological hypothesis assigns to that intention in the first place. Miracle reasoning often supplies the first factor retrospectively—*if God intended this recovery, then of course the recovery is likely*—while leaving the second almost entirely unspecified. Yet it is the second factor that determines whether the specific intention was genuinely expected before the event.

This exposes an important feature of very broad divine hypotheses. Greater power does not automatically mean greater predictive specificity. An omnipotent agent may be capable of producing an enormous range of mutually incompatible outcomes. Unless the hypothesis also tells us something about the agent's preferences, purposes, or regularities of action, that expanded capacity can enlarge the action space without concentrating predictive probability on the event actually observed. **Omnipotence establishes possibility; a theory of divine psychology would be needed to establish propensity.**

A more specific theological hypothesis can, in principle, do better. If a tradition independently claims that a deity reliably intervenes in a particular class of circumstances for a specified purpose, that claim gives some structure to $$P(I_i\mid D)$$ and therefore makes empirical discrimination more possible. But the gain in predictive content comes with a corresponding risk: outcomes outside that predicted class can now count against the hypothesis. The theological content must constrain the action space *before* the event if it is to generate evidential leverage afterward.

The plane-crash example makes the size of this action space vivid. Imagine that one person survives a crash in which many others die, and afterward the survivor says, “God saved me.” Perhaps God could have saved that person. But if divine intervention is the explanation, many alternatives were also available: God could have prevented the crash, saved everyone, saved someone else, saved no one, changed the way the crash occurred, prevented the flight from departing, intervened elsewhere, or performed an unmistakable public miracle instead.

The divine hypothesis therefore does not initially specify one outcome. It contains a potentially vast action space, and the probability of the observed outcome depends on how probability is distributed across that space. If the hypothesis permits almost anything, the fact that the observed outcome is compatible with it is not especially informative.

> **Compatibility is cheap. Prediction is harder.**

<a id="post-hoc-intention-prediction-accommodation"></a>
## Post-Hoc Intention and the Prediction–Accommodation Distinction

The problem becomes especially clear when divine intention is specified only after the event. Suppose event $$E$$ occurs and we then define

$$
D_E=
\text{“God specifically intended to cause }E\text{.”}
$$

Under this newly constructed hypothesis,

$$
P(E\mid D_E)\approx1.
$$

That appears impressive. If

$$
P(E\mid N)=10^{-9},
$$

one might be tempted to conclude that the Bayes factor overwhelmingly favors the divine hypothesis. But the comparison is misleading because $$D_E$$ was tailored to the observation. Before $$E$$ occurred, there might have been many possible divine-intention hypotheses,

$$
D_1,D_2,\ldots,D_k,
$$

each corresponding to a different thing God might have chosen to do. If there was no independent reason beforehand to privilege $$D_E$$ over those alternatives, its apparent predictive success is illusory. It did not predict the event; it was constructed around it.

This reveals a broader epistemic distinction. Prediction has the structure

$$
\text{hypothesis}
\rightarrow
\text{specific expectation}
\rightarrow
\text{observation},
$$

whereas accommodation has the structure

$$
\text{observation}
\rightarrow
\text{interpretation}
\rightarrow
\text{hypothesis fitted to observation}.
$$

Both can produce explanations, but they are not evidentially equivalent. If someone says before an event, “At noon tomorrow, person $$X$$ will experience event $$E$$ because of divine intervention,” and the event occurs under controlled conditions, the theological hypothesis has constrained the outcome space before the observation. That can constitute strong evidence. By contrast, if the event occurs first and the explanation afterward becomes “God must have intended this outcome,” the explanation has accommodated the evidence rather than predicted it.

The distinction becomes even more important when an explanatory system can accommodate many outcomes. A model cannot simply assign high probability to whichever event happens after seeing the result. Suppose a divine hypothesis permits

$$
E_1,E_2,\ldots,E_k.
$$

Before observation, its predictive probability must be distributed across those possibilities. It cannot coherently say

$$
P(E_i\mid D)\approx1
$$

for whichever $$E_i$$ happens to occur; the probabilities would sum to far more than one. A serious predictive model must therefore say something about which outcomes are more likely than others. If it does not, then its predictive content is weak. At that point, post-hoc attribution and model overfitting become two descriptions of the same underlying problem: the explanation gains specificity only after the outcome is known.

<a id="inscrutable-intentions-non-sequitur"></a>
## Inscrutable Intentions and the Non Sequitur

A common response is that divine intentions are beyond human understanding. Perhaps that is true. But epistemically it creates a tradeoff. If God's reasons are inscrutable, then it becomes difficult to assign

$$
P(E\mid D)
$$

with any confidence. The same move that protects the hypothesis from disconfirmation also limits its capacity to receive confirmation. If almost any outcome can be reconciled with divine intention, then no particular outcome strongly favors the hypothesis.

The tradeoff can be stated directly:

> **The less constrained divine intention is, the harder the hypothesis is to falsify—but the weaker any particular event becomes as evidence for it.**

A model that can explain everything may therefore predict very little.

This also exposes an important asymmetry in miracle reasoning. The argument often begins by asking, “How could this particular event have happened naturally?” But once divine agency is proposed, the corresponding question becomes, “Why would this particular divine agent choose this particular event?” The improbability problem has not necessarily disappeared. It may simply have been relocated. Under the natural model, the question is

$$
P(E\mid N).
$$

Under the divine model, the question becomes

$$
P(E\mid D),
$$

which itself depends on something like

$$
P(\text{divine choice of }E\mid D).
$$

If that quantity is unknown, the divine explanation has not automatically gained an advantage.

The common inference can now be stated precisely. It moves from

$$
P(E\mid N)\ll1
$$

toward

$$
P(D\mid E)\gg1.
$$

But Bayes' theorem shows that the conclusion does not follow without additional premises. We need to know $$P(E\mid D)$$, the prior odds

$$
\frac{P(D)}{P(N)},
$$

and whether the event was specified before or after observation. We also need to know how many alternative events would have counted as miraculous, how many opportunities existed, how many descriptions were available, how many divine intentions could have been attributed, and whether the divine hypothesis placed substantial probability on this particular outcome beforehand.

Without that information, the inference from improbability to divine agency is incomplete. This does not mean that no event could ever provide evidence for divine intervention. It means that a compelling case would have to do more than show that the event was unlikely naturally. A theological hypothesis would need to give us some independent reason to expect the event—to say, in effect, not merely “God could have caused this,” but “Given what this hypothesis says about divine intentions, this is the kind of event we should actually expect.” Only then can the observation discriminate between competing explanations.

<a id="iv-accommodation-prediction-overfitting"></a>
# IV. Accommodation, Prediction, and Model Overfitting

The Bayesian problem becomes more severe when a theological system is flexible enough to accommodate many different outcomes after they occur. At that point, the question is no longer merely whether the system can explain the observed event. The more important question is whether the explanation reflects genuine predictive power or whether the model has been fitted to the data after the fact.

The analogy with model overfitting makes that distinction especially clear.

<a id="overfitting-bayesian-complexity"></a>
## The Overfitting Analogy and Bayesian Complexity

In statistics and machine learning, a model is overfit when it captures the peculiarities of the data it has already seen so closely that its apparent explanatory success does not generalize well to new data. It may fit the training set almost perfectly while performing poorly on observations that were not used to construct it.

Something structurally similar can happen in the interpretation of miracles. A theological system may explain an extraordinary event extremely well after it occurs. It can identify the relevant feature, assign a divine intention, connect the outcome to a doctrine, and produce a narrative that makes the event appear almost inevitable in retrospect. But that retrospective precision does not by itself tell us whether the model predicted the event.

The analogy can be made fairly precise:

- **training data** are the events already observed;
- **feature selection** is the process of deciding which properties of those events matter;
- **model selection** is the choice of explanatory framework;
- **parameter fitting** is the adjustment of the model to account for the data;
- **overfitting** occurs when the model explains the observed data extremely well while generalizing poorly;
- **out-of-sample testing** asks whether the model successfully predicts new observations that were not used to construct it.

A miracle interpretation can follow a similar sequence. First, the event occurs. Then the features that appear significant are selected. The event is interpreted through a theological framework, and a particular divine purpose is assigned. The result is a highly specific explanation of the observed outcome:

$$
\text{observed event}
\rightarrow
\text{feature selection}
\rightarrow
\text{theological interpretation}
\rightarrow
\text{divine intention}
\rightarrow
\text{retrospective explanatory fit}.
$$

The danger is not the existence of a retrospective explanation; it is treating that explanation as though it had predictive force before the event occurred.

Bayesian model comparison gives us a formal way to understand why flexible explanations should be treated cautiously. Suppose a theological model $$M$$ contains interpretive parameters $$\theta$$. These might represent divine motives, theological categories, symbolic interpretations, relevant doctrines, possible forms of intervention, or possible reasons for allowing or preventing some event. After observing event $$E$$, one can search the parameter space for the setting that fits the observation best:

$$
\hat{\theta}
=
\arg\max_\theta P(E\mid M,\theta).
$$

Perhaps the best-fitting interpretation gives

$$
P(E\mid M,\hat{\theta})\approx1.
$$

That can look impressive. But Bayesian model comparison does not evaluate a model only at the parameter value that fits the observation best. It asks for the model's predictive probability before the evidence is used to choose the interpretation:

$$
P(E\mid M)
=
\int
P(E\mid M,\theta)
P(\theta\mid M)
\,d\theta.
$$

The model must average over the possibilities it allowed beforehand. If many different theological intentions were possible, the model does not receive the full evidential credit of whichever one happens to fit the observed outcome. This is the Bayesian version of a complexity penalty. Flexibility makes accommodation easier, but that same flexibility can disperse predictive probability across more possibilities.

The distinction between **best fit** and **average predictive fit** is essential here. A flexible model may contain a tiny region of parameter space in which the observed event is almost certain. If that region had very little probability assigned to it beforehand, however, the model's overall predictive probability can remain small. Bayesian marginalization asks not merely whether the model *contains* an explanation that fits, but how much of the model's prior predictive weight was already concentrated near explanations that fit.

A simple discrete example makes the point. Suppose a theological model allows one thousand intentions that were treated as roughly equally plausible beforehand. Imagine that one of them predicts $$E$$ with probability one while the other 999 do not predict it. Then, ignoring other routes to $$E$$ for simplicity, the model's prior predictive probability is approximately

$$
P(E\mid M)\approx\frac{1}{1000},
$$

not one. After observing $$E$$ we can identify the successful intention and say that, *conditional on that intention*, the event was perfectly expected. But the model as a whole did not assign certainty to that intention before the observation. The post-hoc move from “one allowed intention predicts this perfectly” to “the model predicted this perfectly” is exactly what marginal likelihood prevents.

None of this implies the crude rule that every flexible model is automatically bad. A complex model can predict extremely well if its prior probability is concentrated on the parts of parameter space that generate the data. The Bayesian penalty arises when flexibility is purchased by spreading probability over many possibilities and only a small subset fits what was observed. What matters is not complexity by itself, but **how much predictive probability the model committed to the successful explanation before the result was known**.

<a id="retrospective-precision-predictive-weakness"></a>
## Retrospective Precision and Predictive Weakness

Consider an extraordinary recovery. Afterward, someone says, “God preserved this person because they still had an important purpose to fulfill.” The explanation is specific: it identifies the event, the beneficiary, the divine intention, and the significance of the outcome. But the direction of construction matters. The person survived first; the purpose was inferred afterward.

Had the person died, another interpretation might have been available: “God called them home.” Had they recovered gradually through ordinary medicine, one might say, “God worked through the doctors.” Had their condition persisted, one might conclude, “God has a purpose in their suffering.” The theological framework therefore need not predict one specific outcome. It may contain a family of explanations capable of accommodating many possible outcomes, with the precise explanation selected only after the data are known.

This is exactly the kind of situation in which an overfit model can appear more powerful than it is. A model becomes predictively informative by excluding possibilities. If a theory says, “Under these conditions, outcome $$E$$ is substantially more likely than outcomes $$F$$, $$G$$, and $$H$$,” then observing $$E$$ can confirm the theory. But if the theory says that $$E$$ would be consistent with divine purpose while $$F$$, $$G$$, and $$H$$ would be as well, then the occurrence of $$E$$ carries much less evidential weight.

The evidential consequence is straightforward:

> **The more outcomes a hypothesis can absorb without difficulty, the less strongly any one outcome confirms it.**

This does not mean that flexible explanations are false. It means that explanatory flexibility and evidential strength should not be confused.

<a id="theory-that-explains-everything"></a>
## A Theory That Explains Everything

The point becomes clearer if we imagine a theory that can accommodate survival and death, recovery and illness, success and failure, answered and unanswered prayer, visible intervention and hidden intervention. Such a theory may appear extraordinarily powerful because nothing falls outside its explanatory reach. Yet there is an important difference between a theory that can explain every outcome after it occurs and a theory that tells us which outcome to expect before it occurs.

The first is **explanatory flexibility**. The second is **predictive power**. A theory can have nearly perfect retrospective explanatory coverage and very little prospective constraint. That is precisely the pattern associated with overfitting.

The machine-learning analogy makes the contrast vivid. Observed miracle reports function like training data: the interpretive system is repeatedly applied or adjusted so that the observations make sense. But genuine predictive success requires something like a test set—events not used to construct the explanation. The crucial question becomes: **What did the model say before the next event occurred?**

If a theological hypothesis repeatedly made narrow, risky predictions and those predictions succeeded, that would be evidence of generalization. If instead the interpretive framework changes after each outcome so that the result always becomes meaningful, the model may fit the past while predicting little about the future. In machine-learning terms:

> **A model that memorizes the training data has not demonstrated that it understands the underlying process.**

<a id="searching-intention-space"></a>
## Searching the Intention Space

The overfitting problem becomes even stronger once divine intentions are included. Suppose an event can be associated with many possible purposes: to protect someone, teach someone, punish someone, inspire faith, reveal providence, preserve free will, produce spiritual growth, test belief, remain hidden, or fulfill some unknown plan. After almost any outcome, one can search through this intention space until a plausible purpose is found.

The result is another form of the look-elsewhere effect. We are no longer searching only over events and descriptions; we are also searching over possible intentions. The full interpretive space can therefore be represented schematically as

$$
\text{event space}
\times
\text{description space}
\times
\text{intention space}.
$$

That combined space can be enormous. A meaningful explanation discovered somewhere within it may feel highly specific even though the search process itself made such a fit likely.

This lets us summarize miracle attribution as three nested selection processes. First, **which event?** Out of an enormous number of occurrences, some event is selected because it is unusual or emotionally salient. Second, **which description?** Out of many ways to characterize the event, one makes it appear especially meaningful or improbable. Third, **which intention?** Out of many possible divine purposes, one is selected that makes the outcome appear purposeful.

Thus:

$$
\text{event selection}
\rightarrow
\text{description selection}
\rightarrow
\text{intention selection}.
$$

Each stage narrows the story after the fact. By the end, the explanation can appear remarkably precise, even though its precision is retrospective rather than predictive.

The deeper lesson of the analogy is therefore not that theological explanations fail to explain extraordinary events. Quite the opposite: they may be capable of explaining too many of them, in too many different ways, after the outcome is already known. A narrative may fit an event beautifully, make the timing seem meaningful, supply a motive, and connect the event to a larger theological story. None of those features, by themselves, establish that the model assigned substantial probability to the event beforehand.

The distinction can be stated compactly:

$$
\text{retrospective explanatory fit}
\neq
\text{prospective predictive success}.
$$

At this point the earlier pieces of the argument begin to converge. The law of truly large numbers explains why extraordinary events continually occur. Selection effects explain why some become salient. Description selection explains why they can appear uniquely meaningful. Intention selection explains why they can appear purposeful. Model flexibility explains why the resulting theological story can fit so well. But none of these facts alone establishes that the event was actually predicted by the theological hypothesis.

The final question is therefore not simply, “Can this event be interpreted as a miracle?” With enough flexibility, many events can. The more important question is:

> **Did the miracle hypothesis make this event substantially more expected before it occurred than competing explanations did?**

That is the difference between a model that accommodates the world and a model that successfully predicts it. The framework also generates concrete expectations about how miracle attribution should behave when the evidential signal is weak and the interpretive model is flexible. Different communities should be able to fit similar extraordinary events into different doctrinal schemes; favorable outcomes should become more narratively visible than unfavorable ones; and retrospective purposes should proliferate wherever the theology permits many possible motives. The cases that follow are therefore best understood not as unrelated objections, but as observable consequences of the selection-and-accommodation machinery already described.

<a id="v-miracle-attribution-in-practice"></a>
# V. Miracle Attribution in Practice

The abstract structure becomes especially visible when we compare how different religious communities interpret extraordinary events. Once the analysis moves from a bare occurrence to a theological description of it, the background model begins to matter: different traditions bring different expectations, doctrines, and categories to the same kinds of phenomena. The resulting disagreements are therefore not incidental to the argument. They show how much of a miracle's apparent evidential content can depend on the framework used to describe it.

<a id="theological-pluralism-model-relative"></a>
## Theological Pluralism and Model-Relative Interpretation

Within Christianity alone, traditions differ substantially over what sorts of events should count as miracles, what forms of supernatural action remain possible, and what theological significance should be attached to particular phenomena. One tradition may interpret an event through saintly intercession, Marian devotion, sacramental theology, charismatic gifts, prophecy, or healing. Another may reject some of those categories entirely and describe the same phenomenon as coincidence, mistaken attribution, psychological suggestion, ordinary providence, or theological error.

The event itself has not changed. What changes is the interpretive framework. The result is an important principle:

> **Theological significance is partly model-relative.**

An event does not arrive already classified as a Catholic miracle, a Pentecostal healing, or a Protestant act of providence. The theological model contributes the categories through which the event is understood. In that sense, the framework can shape not merely the explanation of the event but the description of what the event *is*.

The problem becomes even clearer across religions. Different traditions report extraordinary events and interpret them as confirmation of incompatible theological systems. Schematically,

$$
E_C\rightarrow T_C,
$$

$$
E_M\rightarrow T_M,
$$

and

$$
E_H\rightarrow T_H.
$$

The notation is deliberately generic because the same form of reasoning can support mutually incompatible conclusions. A striking recovery may be interpreted as evidence of one deity in one culture and another deity in another; a vision may be understood through incompatible doctrinal frameworks; a coincidence may be experienced as providential confirmation of very different theological commitments depending on who experiences it.

The resulting problem is one of discrimination. If the same kind of evidence can be assimilated equally well into competing models, the evidence may not strongly distinguish among those models. A hypothesis does not gain much support merely because it can explain an observation that its rivals can explain equally well.

The Bayesian form of the problem is straightforward. If two theological models, $$T_1$$ and $$T_2$$, compete to explain the same event, then the event's discriminating force between them depends on

$$
BF_{12}
=
\frac{P(E\mid T_1)}{P(E\mid T_2)}.
$$

If both traditions can readily accommodate the event, then this ratio may be close to one even if both regard the event as extraordinary. In that case the event may be psychologically important within each tradition while doing little to decide between them. To support a *specific* theology, the evidence must therefore do more than look unusual under a non-theological baseline; it must be more expected under that theology than under its religious competitors as well.

None of this implies that all theological interpretations have equal evidential standing. They may differ substantially in prior commitments, specificity, documentation, or genuine predictive success. Those differences, however, must be supplied independently. The raw fact that a tradition possesses a coherent story into which $$E$$ can be placed does not itself establish a favorable likelihood ratio against rival traditions.

A useful way to expose this problem is a **symmetry test**:

> Would I regard the same kind of reasoning as equally compelling if a member of a rival religious tradition used it to confirm their theology?

If the answer is no, we should ask what distinguishes the cases. Perhaps there is a genuine asymmetry: one event may be better documented, one tradition may have made a prior prediction, or one hypothesis may assign a much higher likelihood to the event. But if no independent difference can be established, the evidential force may be coming partly from prior theological commitment rather than from the event itself. The symmetry test does not show that all miracle claims are equally weak; it asks whether the inferential standard is being applied consistently.

The same point can be expressed through model-relative descriptions. A recovery might be described as spontaneous remission, an answer to prayer, intercession by a saint, evidence of charismatic healing, or simply an unexplained medical event. These are not merely interchangeable labels. They carve the observation into different explanatory categories, emphasizing some features while ignoring others. The structure is therefore something like

$$
\text{same observation}
\rightarrow
\text{different model}
\rightarrow
\text{different salient features}
\rightarrow
\text{different explanation}.
$$

The event is never interpreted in a vacuum.

<a id="plane-crash-survivorship-bias"></a>
## The Plane-Crash Survivor and Survivorship Bias

The plane-crash example reveals another important form of selection. Suppose a plane carrying two hundred people crashes. One person survives; one hundred and ninety-nine die. The survivor says, “God saved me for a reason.” The selected datum is

$$
E=\text{this person survived}.
$$

But the complete outcome is

$$
D=
\{199\text{ deaths},1\text{ survival}\}.
$$

If divine agency is being proposed to explain the event, the entire pattern should matter. Why did the intervention take the form

$$
199\text{ deaths}+1\text{ survival}?
$$

Why this survivor? Why not prevent the crash? Why not save everyone? Why not intervene in some different way? The miracle narrative usually focuses on the one salient success and treats the remaining outcomes as background. That is a form of event selection.

The example also illustrates a reporting asymmetry. Survivors can tell their stories, interpret their survival, describe meaningful coincidences, give testimony, publish memoirs, and speak about providence. The dead cannot generate symmetrical accounts of divine non-intervention. Miracle testimony can therefore become disproportionately populated by the favorable tail of the outcome distribution—not because the survivors are dishonest, but because the available evidence has itself been selected by the outcome.

Here survivorship bias is almost literal. The very people capable of producing narratives of extraordinary survival are the people who survived. If we listen only to those narratives, the background distribution of outcomes disappears from view.

<a id="prayer-asymmetric-updating"></a>
## Prayer, Asymmetric Interpretation, and One-Sided Updating

The same asymmetry appears in interpretations of prayer. Consider several possible outcomes after someone prays for recovery. If the person recovers unexpectedly, the event may be called a miracle. If they recover through medical treatment, one may say that God worked through the doctors. If recovery is slow, God answered in his own time. If the illness persists, God may have a purpose in the suffering. If the person dies, God called them home. If nothing apparent happens, God's answer may be described as “no” or “not yet.”

No particular interpretation must therefore be false. The evidential difficulty is that the system can accommodate nearly every possible outcome. If

$$
E_1,E_2,E_3,E_4,E_5
$$

can all be readily incorporated into the same theological framework, then observing $$E_1$$ may provide little confirmation of that framework. The model survived the observation because it was flexible enough to survive nearly any observation.

A well-calibrated evidential system should specify what counts in favor of a hypothesis, what counts against it, and what is neutral. But some miracle reasoning operates asymmetrically. A favorable outcome increases confidence:

$$
\text{unexpected recovery}\rightarrow\text{evidence for intervention},
$$

while an unfavorable outcome does not decrease confidence:

$$
\text{death}\rightarrow\text{mysterious divine purpose}.
$$

The result is a form of one-sided updating. The hypothesis receives evidential credit when events appear to support it, while contrary outcomes are absorbed without a corresponding evidential penalty. That is not ordinary Bayesian reasoning. Bayesian updating requires that evidence be capable of moving probabilities in both directions.

The more general lesson is not that theology must reduce every religious claim to a laboratory experiment. It is that an evidential claim should expose itself to evidential loss. If no possible observation can count significantly against a hypothesis, then the hypothesis may be difficult to falsify—but for the same reason, it becomes difficult to confirm. The protection comes at a price.

<a id="vi-interpretation-to-evidence"></a>
# VI. From Interpretation to Evidence: The Probabilistic Anatomy of a Miracle

The preceding analysis can now be assembled into a single picture. A miracle claim often begins not with a prediction but with an observation: something unusual happens, attracts attention because it is rare or narratively striking, and is then described in a way that makes its improbability or significance especially salient. The event is placed within a theological framework, a divine intention is assigned, and the explanation becomes increasingly specific: *this happened to this person, at this time, for this reason, because God intended this outcome*.

The full sequence can be represented as

$$
\text{enormous event space}
\rightarrow
\text{rare events inevitably occur}
\rightarrow
\text{salient event selected}
\rightarrow
\text{meaningful description selected}
\rightarrow
\text{natural improbability emphasized}
\rightarrow
\text{theological framework applied}
\rightarrow
\text{divine intention attributed}
\rightarrow
\text{retrospective fit experienced as confirmation}.
$$

That sequence captures the probabilistic anatomy of many miracle claims. No individual step is necessarily illegitimate; the difficulty arises when the specificity of the final explanation is treated as though it had existed before the observation rather than being generated gradually through selection and interpretation.

<a id="three-inferential-steps"></a>
## Three Inferential Steps

Miracle discussions often collapse several distinct questions into one: Was the event improbable? Was it intentional? Was the intention divine? These are separate inferential steps, and each requires its own evidence.

The first transition is from **improbability to intention**. The fact that an event is unlikely does not imply that it was selected by an agent. Every shuffled deck produces an exact sequence with probability

$$
\frac{1}{52!},
$$

every lottery winner experiences an outcome that was extraordinarily unlikely for that particular person, and every sufficiently large population generates extreme outliers. The world constantly produces outcomes that would have been difficult to predict beforehand. Therefore

$$
P(E\mid N)\ll1
$$

does not imply

$$
P(\text{intentional causation}\mid E)\gg1.
$$

To infer intention, we need evidence that the observed structure is more likely under intentional production than under the relevant alternatives. That is why prior specification matters so much. If an agent announces a target before acting and repeatedly hits it, intention is plausible because the target was fixed independently of the outcome. If the target is drawn around the result afterward, the inference is weaker.

The second transition is from **intention to divinity**. Even if intentional causation were established, the identity of the agent would remain open. Depending on the case, one might still have to distinguish among human action, fraud, hidden technological intervention, unknown natural processes, non-divine agency, and divine intervention. The structure

$$
\text{chance seems unlikely}
\rightarrow
\text{therefore God}
$$

omits a potentially large hypothesis space between those two points.

A third distinction concerns **compatibility and confirmation**. An event may be compatible with a hypothesis without providing significant evidence for it. If hypothesis $$H$$ permits event $$E$$, then

$$
P(E\mid H)>0,
$$

but this tells us little about whether $$E$$ confirms $$H$$. For confirmation, the event must be comparatively more likely under $$H$$ than under relevant competitors. What matters is a ratio such as

$$
\frac{P(E\mid H)}{P(E\mid H')}.
$$

The distinction matters especially for theological claims because a broad divine hypothesis may be compatible with an enormous range of outcomes. “God could have done this” is therefore much weaker than “If this theological hypothesis were true, we would have had strong reason to expect this event rather than its alternatives.”

These distinctions can be summarized compactly:

$$
\text{improbable}
\not\Rightarrow
\text{intentional},
$$

$$
\text{intentional}
\not\Rightarrow
\text{divine},
$$

and

$$
\text{compatible with a hypothesis}
\not\Rightarrow
\text{evidence for that hypothesis}.
$$

<a id="better-standard-miracle-claims"></a>
## A Better Standard for Miracle Claims

Nothing in the preceding analysis requires miracle claims to be dismissed automatically. It instead suggests a more demanding evidential standard, designed to minimize the same forms of flexibility that make post-hoc explanations easy.

**Antecedent specification.** The relevant event should be identified before it occurs. Fixing the target in advance transforms

$$
\text{outcome}\rightarrow\text{description}
$$

into

$$
\text{description}\rightarrow\text{outcome}.
$$

That reversal matters because it prevents the target from being selected to fit the result.

**Narrow prediction.** The hypothesis should constrain what is expected. A theory that predicts one narrow class of outcomes is more informative than a theory compatible with almost anything. If a theological hypothesis predicts $$E$$ rather than

$$
E\lor F\lor G\lor H\lor\cdots,
$$

then observing $$E$$ carries greater evidential weight. Prediction gains force by excluding alternatives.

**Low probability under plausible natural alternatives.** The event should genuinely be unlikely under the relevant non-divine hypotheses. That requires more than showing that the exact outcome was improbable. The calculation should account for the total number of opportunities, the look-elsewhere effect, alternative descriptions, selection effects, and realistic natural mechanisms.

**High probability under the divine hypothesis.** This is the requirement most often neglected. A small value of

$$
P(E\mid N)
$$

does not establish a miracle unless there is also some independent basis for thinking

$$
P(E\mid D)
$$

is comparatively large. Without that, the Bayes factor remains unknown.

**Independent reasons about divine intention.** The predicted action should not be inferred solely from the fact that the action occurred. There should be some prior theological reason to expect this kind of intervention, for this kind of purpose, under these circumstances. Otherwise divine psychology is being reconstructed from the outcome.

**Correction for multiple opportunities.** The calculation should include the full opportunity space. If millions of events could have generated a miracle narrative, the selected case cannot be treated as though it were the only relevant opportunity. Likewise, if many descriptions would have counted as meaningful, that multiplicity belongs in the analysis.

**Symmetrical treatment of success and failure.** A serious evidential framework must allow observations to count against the hypothesis. If successful outcomes confirm the model while failures are automatically reinterpreted as hidden purpose, the updating procedure becomes one-sided. A meaningful prediction must risk being wrong.

**Discrimination among competing theological hypotheses.** If an event is being used to support a particular religion, denomination, or doctrine, then it should distinguish that hypothesis not merely from naturalism but from rival theological interpretations. Otherwise the evidence may support, at most, some broad claim about agency rather than the specific theology being asserted.

Taken together, these criteria ask a miracle claim to do something much more demanding than fit an event after it occurs. They ask it to expose itself to comparison, error, and failed expectation.

<a id="strong-case"></a>
## What a Strong Case Might Look Like

Consider an intentionally exaggerated example. Suppose a religious community publicly announces in advance that a specific person, at a specific location and time, will experience a specific physically extraordinary event under clearly stated theological conditions. The prediction is recorded before the event. Independent observers are present. The event occurs as specified. The phenomenon is difficult to explain under known natural processes, and the theological hypothesis had a clear prior reason to predict precisely that outcome. Failed predictions from the same system are recorded rather than ignored.

This would be epistemically different from a spontaneous recovery interpreted retrospectively. The important difference would not merely be that the event was more dramatic; it would be that the hypothesis constrained the outcome space beforehand. Its success would resemble genuine out-of-sample prediction, and the relevant Bayes factor could plausibly become large:

$$
BF=
\frac{P(E\mid D)}{P(E\mid N)}.
$$

That is the kind of evidential structure a strong miracle claim would have to approximate.

<a id="limits-unknowns"></a>
## Limits, Unknowns, and What the Argument Does Not Show

It is important that the method not assume its conclusion. If one begins by declaring miracles impossible, then no evidence could ever count; the argument would be circular. The probabilistic approach does something different. It leaves open the possibility that

$$
P(D\mid E)
$$

could become large, but insists that the increase come through ordinary evidential reasoning. The miracle hypothesis must outperform relevant alternatives, make sufficiently constrained predictions, and remain exposed to failed opportunities. In that sense, the method is neutral with respect to the metaphysical possibility of miracles. It asks whether the evidence actually favors the hypothesis.

The argument therefore does not establish

$$
P(D)=0.
$$

It does not prove that divine intervention never occurs, that every miracle testimony is fraudulent, that personally meaningful coincidences are psychologically trivial, or that unusual recoveries and survivals are uninteresting. Nor does it require that every unexplained event eventually receive a conventional natural explanation. The conclusion is narrower: **the natural improbability of a retrospectively selected event is insufficient, by itself, to establish intentional divine causation.**

The same framework clarifies what follows when an event remains unexplained. Sometimes our best conclusion really is that we do not know why something happened. But an explanatory gap does not automatically transfer probability to whichever alternative hypothesis is culturally or emotionally available. If the natural explanation is unknown and the divine explanation also lacks a clear predictive distribution, uncertainty remains on both sides. “Unexplained” is a description of our epistemic position, not a causal mechanism.

<a id="evidence-process-level"></a>
## Evidence at the Level of the Process

The same logic also changes how selective evidence should be handled. Suppose one person recovers unexpectedly from a disease after prayer. The event may be remarkable, but if the claim concerns the efficacy of divine intervention, the relevant evidence includes not only that recovery but all comparable cases: prayers followed by recovery, prayers followed by no recovery, no prayer followed by recovery, and no prayer followed by no recovery.

The probability model should therefore be conditioned on the complete evidence rather than the most memorable case. In simplified form, the relevant comparison is not merely

$$
P(\text{this recovery}),
$$

but something more like

$$
P(\text{observed pattern of recoveries and failures}\mid H).
$$

Conceptually, the evidential object is a table of outcomes rather than a single success story:

| | Recovery | No recovery |
|---|---:|---:|
| **Prayer / proposed intervention present** | $$a$$ | $$b$$ |
| **Prayer / proposed intervention absent** | $$c$$ | $$d$$ |

A real causal analysis would require much more than these four counts—cases may differ in prognosis, treatment, selection into prayer, reporting, and many other respects. The table is not offered as a ready-made experiment. Its purpose is to show the change in evidential perspective. Once the claim is about a process such as prayer or intervention, the relevant question is no longer whether one memorable case occurred, but whether the overall distribution of outcomes differs in the way the hypothesis predicts.

The same logic extends to survival, prophecy, visions, coincidences, and other miracle claims: once a claim concerns a recurring process or source of intervention, the evidence should be evaluated at the level of that process rather than at the level of the most memorable anecdote.

It also helps separate a **story** from a **model**. Miracle narratives are often compelling because stories naturally emphasize coherence. They select relevant characters and events, highlight meaningful timing, construct causal relationships, and produce resolution. That structure is precisely what makes stories intelligible. Probability models operate differently. A model must account not only for the events that complete the narrative, but also for the enormous background of events that did not.

The story asks, “Why did this happen?” The model asks, “How often would this kind of outcome arise under each competing hypothesis?” The first seeks meaning; the second seeks discrimination. Confusing the two can make a meaningful narrative appear more evidentially powerful than it is.

The distinction also allows a more charitable treatment of religious experience. An event can have profound personal meaning without its causal interpretation being established. Someone may survive an accident and experience that survival as a moral turning point; someone may recover from illness and understand the experience through prayer; someone may encounter a coincidence that reorganizes how they think about their life. The significance of those experiences does not depend on our treating the corresponding causal interpretation as statistically established.

In short,

$$
\text{meaningful to an observer}
$$

does not entail

$$
\text{intentionally produced for that meaning}.
$$

A psychological, existential, or theological interpretation and a causal inference are different kinds of claims.

<a id="general-epistemic-principle"></a>
## A General Epistemic Principle

Although the discussion has focused on religion, the underlying structure is much broader. It appears whenever humans infer agency, design, or hidden significance from unusual events—whether in conspiracy reasoning, paranormal claims, financial pattern detection, prophecy, pseudoscientific prediction, retrospective historical explanation, or ordinary coincidence.

Two general lessons follow:

> **A pattern discovered after searching a large space of possibilities should not be evaluated as though that pattern had been uniquely specified beforehand.**

and

> **An explanation capable of accommodating many outcomes should not receive the evidential credit of a model that specifically predicted the observed one.**

Miracle reasoning is one instance of this broader problem in human inference.

There is also a question of evidential symmetry. Natural explanations are often required to specify exact probabilities, mechanisms, frequencies, causal pathways, and alternative outcomes, while the divine explanation may be allowed to remain simply “God wanted this.” But if the natural hypothesis is penalized for failing to make the event highly probable, the divine hypothesis should be held to the same standard. It must also confront the questions: Why this outcome? Why this person? Why this time? Why this form of intervention? Why not the alternatives?

If those questions cannot be answered, the divine hypothesis may remain possible, but its comparative likelihood has not been established. The evidential standards should be symmetrical.

The common miracle inference can therefore be reconstructed as a gap between

$$
P(E\mid N)\ll1
$$

and

$$
P(D\mid E)\gg1.
$$

Between those statements lie all the unresolved questions developed throughout this essay: How large was the relevant event space? How many opportunities existed? How many possible descriptions would have counted as significant? Was the event specified before or after observation? How many divine intentions were available? Which observations would have counted against the divine hypothesis? Would the same reasoning be accepted when used by a competing religion? And, above all, what is

$$
P(E\mid D)?
$$

Until those questions are addressed, the inference remains incomplete. The event may be astonishing, unexplained, or deeply meaningful without those facts alone establishing divine intention.

<a id="careful-vocabulary"></a>
## A More Careful Vocabulary

Much of the confusion surrounding miracles comes from collapsing several distinct categories. It is useful to keep them separate:

| Category | Meaning |
|---|---|
| **rare** | It has low probability under some specified model. |
| **surprising** | It was not strongly expected by an observer. |
| **salient** | It attracts attention because of its emotional or structural features. |
| **meaningful** | It is integrated into a person's narrative or worldview. |
| **unexplained** | No currently accepted causal account adequately explains it. |
| **intentional** | It was deliberately selected by an agent. |
| **divine** | The relevant agent is a deity. |

None of these categories automatically entails the next; movement from one to another requires additional evidence. Keeping them separate is perhaps the simplest way to understand the entire argument.

A probability-based understanding of miracle claims therefore begins not by asking whether miracles are possible, but by asking how extraordinary events arise and how they acquire interpretation. The law of truly large numbers explains why rare events should occur. Selection effects explain why some become memorable. Description selection explains why they can appear exquisitely specific. Bayesian reasoning shows that natural improbability alone does not favor divine intervention. The analysis of divine psychology shows that an agent's capability does not establish its propensity to act. Model overfitting explains how theological systems can achieve excellent retrospective fit, and theological pluralism shows why similar events can support incompatible interpretations.

Taken together, these ideas do not eliminate the category of miracle. They make the evidential threshold clearer. A miracle, if it is to function as evidence rather than simply as a theological interpretation of an unusual event, must do more than surprise us.

It must discriminate.

<a id="conclusion"></a>
# Conclusion: From Anomaly to Intention

The question “What are the odds?” can feel like the beginning and end of an argument about miracles. In reality, it is only the beginning. Before the number means anything, we must specify the event, the relevant reference class, the number of opportunities, the alternative outcomes, and the descriptions under which the result could have appeared significant. Above all, we must distinguish the probability of one exact outcome from the probability that *some* comparably striking outcome would occur somewhere in a vast event space.

Once those distinctions are made, the apparent mystery surrounding rare events changes character. A one-in-a-million event is extraordinary when there is one opportunity for it to occur and expected when there are millions. A fantastically improbable card sequence is unremarkable if some sequence had to occur. A coincidence can be genuinely rare under the description selected after the fact while remaining unsurprising as one member of a much larger family of possible coincidences. The world does not need to suspend probability in order to generate extraordinary events; it needs only enough opportunities.

That is the basic lesson of Littlewood's intuition, Dyson's formulation, and the law of truly large numbers. Yet humans are not passive statistical instruments: we select. From the enormous number of events that occur, we remember unusual ones; from the many ways those events can be described, we notice the descriptions that make them meaningful; and from the interpretations available to us, we may favor those that fit an existing worldview. The process can be summarized as

$$
\text{event selection}
\rightarrow
\text{description selection}
\rightarrow
\text{intention selection}.
$$

At each stage, the event becomes more narratively specific. By the end, an occurrence that began as one outcome among countless others can acquire a remarkably precise interpretation: *this happened to me, at this moment, for this reason, because it was intended*. The central epistemic danger is to mistake that retrospective precision for predictive precision.

Bayesian reasoning makes the distinction explicit. The fact that an event is improbable under natural processes does not by itself imply that divine intervention is probable. What matters is not merely

$$
P(E\mid N),
$$

but the comparative likelihood

$$
\frac{P(E\mid D)}{P(E\mid N)}.
$$

An event favors divine intervention only to the extent that the divine hypothesis made that event more expected than its alternatives did. A rare event can therefore be highly surprising while providing little evidence for a particular explanation. It can be unexplained without being divinely explained, meaningful without being intentional, and intentional without being divine. In compact form,

$$
\text{improbable}
\not\Rightarrow
\text{intentional},
$$

$$
\text{intentional}
\not\Rightarrow
\text{divine},
$$

and

$$
\text{compatible with a hypothesis}
\not\Rightarrow
\text{evidence for that hypothesis}.
$$

The same logic explains why flexibility is both attractive and dangerous. A theological model may accommodate an event beautifully after it occurs, but if it could have accommodated many incompatible outcomes just as easily, the fit carries less evidential weight. Predictive power comes from constraint: a model becomes informative when it tells us that some outcomes are more likely than others, risks being wrong, and allows future observations to count against it. The model-overfitting analogy is useful precisely because it captures the gap between fitting observations already in hand and successfully predicting observations not yet seen.

Religious pluralism and asymmetric miracle attribution make this problem visible in practice. Different theological communities can interpret similar recoveries, coincidences, visions, and apparent answers to prayer through incompatible doctrinal frameworks. Favorable outcomes can become prominent evidence while failures or tragedies are accommodated through different appeals to divine purpose. These facts do not establish that every theological interpretation is false. They show that the raw event does not carry a unique theological interpretation on its surface, and that a hypothesis which receives credit for successes must also specify how contrary outcomes affect its evidential standing.

A stronger miracle claim would therefore have a different structure. It would narrow the outcome space *before* the event, specify what should happen, expose itself to failure, establish that the result is genuinely improbable under plausible alternatives, and provide independent reasons for thinking that the proposed divine hypothesis assigns comparatively high probability to it. In other words, it would move away from

$$
\text{observation}
\rightarrow
\text{interpretation}
$$

and toward

$$
\text{hypothesis}
\rightarrow
\text{prediction}
\rightarrow
\text{observation}.
$$

Nothing in probability theory requires that

$$
P(D)=0.
$$

The argument is not that miracles cannot happen. It is that rarity alone does not make an event miraculous, personal meaning alone does not establish intention, and an explanatory gap does not become evidence of divine agency merely because a divine explanation can be supplied afterward. The evidential question begins only once we ask what the relevant event space was, how many opportunities existed, whether the outcome was specified in advance, which alternative outcomes would also have seemed miraculous, why the proposed agent would choose this outcome rather than another, what would have counted against the hypothesis, and whether the proposed divine explanation actually made the event more expected than competing explanations did.

Once the problem is framed in this way, “miracle” separates into several phenomena that are easy to conflate: the improbable event, the human recognition of significance, the attribution of intention, and the further theological claim about the identity of the agent. Those are not one inference. They are several.

Probability theory cannot tell us what events are allowed to mean to us, nor can it rule out every form of divine action. What it can do is tell us when astonishment has outrun evidence. In a sufficiently large world, extraordinary events are not exceptions to probability. They are consequences of it.

The world supplies the anomaly. Selection makes it salient. Interpretation makes it meaningful. Overfitting can make it look predicted.

The remaining question is whether anything actually predicted it.
