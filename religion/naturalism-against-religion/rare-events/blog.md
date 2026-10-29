# I. A World Full of Improbable Events

One of the most persistent sources of confusion about improbable events is the tendency to treat rarity as though it were an intrinsic property of an event. We say that something was “one in a million,” “astronomically unlikely,” or “almost impossible,” as though those descriptions alone settled how surprising the event should be. But probability does not work that way. An event is only rare relative to a particular probability model, a particular description of the event, and a particular number of opportunities for it to occur.

This matters because an event can be extraordinarily improbable on any one occasion while being entirely expected somewhere across a sufficiently large collection of occasions. The probability that a particular person wins a lottery may be vanishingly small, while the probability that someone wins may be close to certainty. There is no paradox here. These are simply different events embedded in different reference classes.

The same principle applies far beyond lotteries. A coincidence that would be astonishing if there were only one opportunity for it to occur may become routine when there are millions of opportunities. A statistical outlier that would be alarming in a single experiment may be expected somewhere among millions of experiments. A sequence of events that seems almost impossibly specific when described afterward may be one of an enormous number of equally improbable sequences that could have occurred.

The probability of an event, considered in isolation, therefore tells us less than it initially appears to. We also need to know the size of the event space in which it occurs.

## Littlewood and the Ordinary Extraordinary

This general intuition is associated with what has come to be called Littlewood's law. J. E. Littlewood observed that extremely improbable events should not astonish us as much as they ordinarily do once we take into account the sheer number of events available across a human lifetime. His memorable point was that, with “a lifetime to choose from,” odds of a million to one are not especially formidable.

The phrase *to choose from* is important.

A human life does not present us with one predetermined probabilistic trial. It presents us with an enormous sequence of experiences: conversations, encounters, illnesses, journeys, thoughts, dreams, accidents, phone calls, deaths, recoveries, names, numbers, dates, memories, and coincidences. Each of these can participate in countless possible relationships with others. We are not asking whether one narrowly specified extraordinary event will happen once. We are living through an immense collection of opportunities for something extraordinary to happen.

Suppose some type of event has probability

$$
p=10^{-6}
$$

on any particular opportunity. Calling it a “one-in-a-million event” sounds impressive. But now suppose there are a million opportunities for such an event to occur. The expected number of occurrences is

$$
\mathbb{E}[X]=Np,
$$

where $$N$$ is the number of opportunities.

If

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

Nothing about the event itself has become more probable on any individual trial. It remains a one-in-a-million event. What changes is the number of opportunities available for one such event to appear.

This produces a distinction that will matter throughout the discussion:

$$
\text{local improbability}\neq\text{global rarity}.
$$

An event can remain highly improbable at the level of any particular opportunity while becoming common at the level of an entire population of opportunities.

## Freeman Dyson's “Miracles”

Freeman Dyson later gave this intuition a more quantitative and memorable formulation. He imagined that a person encounters roughly one experientially significant event per second while awake. Over a sufficiently long period, this produces on the order of a million events. If a “miracle” is defined, somewhat playfully, as an event with probability around one in a million, then a person should expect such a miracle with some regularity.

The point is not that Dyson had discovered a precise psychological unit called an “event,” nor that all experiences are independent trials with identical probabilities. The calculation is heuristic. Its purpose is to expose a mistake in intuition.

We often reason from:

> This event had only a one-in-a-million chance of happening.

to:

> Something extraordinarily unusual has therefore occurred.

But that conclusion does not follow without knowing how many opportunities existed.

If there was one opportunity, a one-in-a-million result is astonishing. If there were a million opportunities, one such result is roughly what we should expect. If there were a billion opportunities, many such events should occur.

The relevant scale is therefore not simply $$p$$, but the relationship between probability and opportunity count.

For a rare event with probability $$p$$ occurring across $$N$$ independent opportunities, the probability that it occurs at least once is

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

This makes the quantity

$$
Np
$$

especially important.

If

$$
Np\ll1,
$$

then even across all the available opportunities, the event remains genuinely unusual.

If

$$
Np\approx1,
$$

we should expect it occasionally.

If

$$
Np\gg1,
$$

we should expect it repeatedly.

The counterintuitive result is that an event can be individually spectacular and collectively mundane at the same time.

## The Law of Truly Large Numbers

Persi Diaconis and Frederick Mosteller developed this general insight in their work on coincidences. Their formulation is often summarized as the **law of truly large numbers**: with a sufficiently large sample, almost any outrageous event is likely to occur.

This principle should not be confused with the ordinary law of large numbers. The ordinary law of large numbers concerns the tendency of sample averages to converge toward expected values as the number of observations increases. The law of truly large numbers is a more informal principle about rare events: if the number of opportunities becomes sufficiently enormous, even events with very small individual probabilities should eventually occur.

Suppose, for example, that an event has probability

$$
p=10^{-6}.
$$

With only one opportunity, its occurrence would be highly surprising.

With one million independent opportunities,

$$
P(\text{at least one occurrence})
=
1-(1-10^{-6})^{10^6},
$$

which is approximately

$$
1-e^{-1}\approx0.632.
$$

So a one-in-a-million event has roughly a 63 percent chance of occurring at least once across a million opportunities.

With ten million opportunities,

$$
Np=10,
$$

and

$$
P(\text{at least one occurrence})
\approx
1-e^{-10},
$$

which is effectively certainty.

Again, there is no contradiction. The event remains one in a million on each individual opportunity. But the world has supplied so many opportunities that its appearance somewhere becomes unsurprising.

This is one of the most important conceptual reversals in thinking about extraordinary events. The natural intuition asks:

> How unlikely was this event?

The more relevant question is often:

> How unlikely was it that no event of this general kind would happen anywhere among all the available opportunities?

Those are very different questions.

## Six-Sigma Events Happen Somewhere

The same reasoning applies to statistical extremes.

Suppose an observation lies six standard deviations from the mean under a normal distribution. In the context of one carefully specified observation, such an event would be extraordinarily unusual. But if an enormous number of observations are being generated across the world, extreme deviations become inevitable somewhere.

This is easy to overlook because “six sigma” sounds like an absolute description of extraordinariness. It is not. It is a statement relative to a distribution and an observation.

If there are enough observations, the question ceases to be whether a six-sigma event will occur and becomes where and when one will occur.

This is true at every scale. Consider:

- financial markets generating millions of price movements;
- hospitals observing millions of patients;
- billions of people having dreams every night;
- billions of people thinking about friends and relatives;
- enormous numbers of medical treatments and recoveries;
- countless accidents and near misses;
- billions of daily conversations;
- billions of prayers;
- trillions of combinations of dates, names, places, and personal histories.

Even before considering any special human tendency to notice patterns, the opportunity space is immense.

A world containing billions of observers will continuously generate events that are fantastically improbable from the perspective of any one observer.

## The Lottery Intuition

The lottery provides perhaps the cleanest illustration.

Suppose a lottery gives each ticket holder a one-in-300-million chance of winning.

For any particular person,

$$
P(\text{that person wins})
=
\frac{1}{300,000,000}.
$$

That is extraordinarily small.

Yet if hundreds of millions of tickets are sold, the probability that *someone* wins may be substantial or even overwhelming, depending on the lottery structure.

So when a winner appears on television, two statements are simultaneously true:

> It was extraordinarily unlikely that this particular person would win.

and:

> It was entirely unsurprising that someone would eventually occupy the role of winner.

The first statement does not contradict the second.

And this distinction generalizes.

The person who experiences an extraordinary coincidence occupies a position analogous to the lottery winner. From inside the event, it can feel almost impossibly specific:

> Why me? Why this event? Why now?

But somebody had to occupy one of the tails of the distribution. Once the population of opportunities becomes sufficiently large, the existence of someone asking “Why me?” may itself be expected.

## Rarity Is Relative to an Event Space

We can now state the deeper principle.

There is no meaningful probability of an event without first defining what counts as the event.

Consider the difference between:

$$
P(\text{I win this lottery})
$$

and

$$
P(\text{someone wins this lottery}).
$$

Or:

$$
P(\text{this patient experiences an extraordinary recovery})
$$

and

$$
P(\text{some patient somewhere experiences an extraordinary recovery}).
$$

Or:

$$
P(\text{I think of this particular friend five minutes before they call})
$$

and

$$
P(\text{some personally meaningful coincidence occurs somewhere in my lifetime}).
$$

The first probability in each pair can be minuscule while the second is much larger.

So describing an event as “one in a million” is incomplete. We must ask:

> One in a million *what*?

One in a million people?

One in a million attempts?

One in a million days?

One in a million possible descriptions?

One in a million among how many total opportunities?

Without specifying the relevant event space, statements about improbability can create an illusion of explanatory depth.

## The First Lesson for Miracles

This does not yet tell us whether any event called a miracle is or is not miraculous. At this stage, the point is more basic.

A rare event does not require a special explanation merely because it is rare.

In sufficiently large event spaces, rare events are exactly what probability theory predicts.

Indeed, a world in which no extremely improbable events ever occurred would itself be statistically peculiar.

The important distinction is therefore:

$$
\text{improbable on one trial}
\neq
\text{unexpected somewhere across many trials}.
$$

This is the first step toward understanding miracle claims probabilistically.

If we want to know whether an extraordinary event genuinely requires an extraordinary explanation, it is not enough to calculate the probability of that event in isolation. We must also ask how many opportunities existed for something comparably extraordinary to occur.

And that leads to a second problem.

Even after we account for the number of opportunities, we still have to decide **which event we are calculating the probability of**.

An exact outcome may be extraordinarily improbable while being completely unremarkable. Another outcome with precisely the same probability may strike us as astonishing because it possesses some recognizable pattern or personal significance.

The next question, then, is not simply why improbable events occur.

It is why certain improbable events become *meaningful*.

# II. From Improbability to Significance

The previous section established that rare events should occur frequently whenever the number of opportunities becomes sufficiently large. But this leaves another problem unresolved. Even if improbable events are inevitable, why do some of them strike us as extraordinary while others pass unnoticed?

The answer cannot simply be that the events we notice are less probable.

In fact, almost every sufficiently specific event is extraordinarily improbable.

What distinguishes a meaningful coincidence from an ordinary occurrence is usually not its exact probability, but the way we describe it.

This distinction is essential because many arguments from extraordinary events begin by calculating the probability of a highly specific description after the event has already occurred. The resulting number may indeed be tiny. But that alone does not tell us whether something genuinely surprising happened.

## Every Exact Outcome Is Improbable

Consider a thoroughly shuffled deck of fifty-two cards.

There are

$$
52!
$$

possible arrangements of the deck. Assuming each arrangement is equally likely, the probability of any particular ordering is

$$
P(E)=\frac{1}{52!},
$$

or approximately

$$
1.24\times10^{-68}.
$$

That is an unimaginably small probability.

Suppose I shuffle a deck and obtain some unremarkable-looking arrangement:

> 8 of clubs, queen of hearts, 3 of diamonds, jack of spades, and so on.

The exact sequence I obtained had probability roughly

$$
10^{-68}.
$$

Yet nobody would regard the shuffle as miraculous.

Why not?

Because some arrangement had to occur.

Every possible ordering is individually fantastically improbable, but the probability that *some ordering* occurs is:

$$
1.
$$

This gives us a basic but easily overlooked principle:

> **An event can have an extraordinarily small probability as an exact outcome without being surprising in any meaningful sense.**

The rarity of the exact event is therefore insufficient.

Something else must explain why certain outcomes attract our attention.

## The Ordered Deck

Now imagine that I shuffle the deck and produce:

> ace through king of spades, followed by ace through king of hearts, then diamonds, then clubs.

The exact probability of that sequence is still:

$$
\frac{1}{52!}.
$$

It is no less and no more probable than the random-looking ordering.

And yet virtually everyone would regard the perfectly ordered deck as requiring explanation.

The reason is not that the ordered sequence is mathematically less probable than the random one.

The difference is that the ordered sequence belongs to a **simple, recognizable category** that was available to us independently of the shuffle.

We can describe it succinctly:

> “The deck is perfectly sorted by suit and rank.”

The random-looking sequence, by contrast, generally has no similarly simple description beyond listing the entire sequence itself.

So two events can have identical exact probabilities while differing enormously in perceived significance.

This tells us that when humans judge an event extraordinary, we are rarely responding to its exact probability. We are responding to some **pattern** or **description** instantiated by the event.

That distinction becomes crucial when discussing coincidences and miracles.

## Events and Descriptions

An event is not identical to the description under which we notice it.

Suppose I encounter a person at an airport.

That physical event can be described in countless ways:

- I encountered someone wearing a blue shirt.
- I encountered someone born in the same state as me.
- I encountered someone whose first name matches my grandfather's.
- I encountered someone whose birthday is two days after mine.
- I encountered someone who attended the same university as an old friend.
- I encountered someone who once lived on a street with the same name as the street where I grew up.
- I encountered someone exactly ten years after another memorable event.

All of these could be true of the same encounter.

The physical occurrence is one event, but there are potentially thousands of properties through which it can be represented.

Let the event be $$E$$, and let:

$$
f_1(E), f_2(E), \ldots, f_k(E)
$$

represent different possible descriptions of it.

After observing $$E$$, we can search among these descriptions and notice whichever one produces an interesting relationship.

Perhaps:

$$
f_{417}(E)
$$

turns out to have a remarkable connection to something personally meaningful.

We then experience that relation as though it were the event itself:

> “What were the odds that *this* would happen?”

But the relevant probabilistic process was not necessarily:

$$
P(f_{417}(E)).
$$

That description may have been selected only because it happened to produce an interesting result.

Before the event occurred, we might have been impressed by any of hundreds or thousands of other relationships.

The more appropriate question may therefore be something like:

$$
P\left(
\bigcup_{i=1}^{k}
\{f_i(E)\text{ produces a salient pattern}\}
\right).
$$

That probability can be far larger.

## The Hidden Multiplicity of Possible Coincidences

Consider a familiar example.

You suddenly think about an old friend whom you have not spoken to in years. Five minutes later, the friend calls.

The experience can feel astonishing.

One might calculate:

> “What were the odds that this specific person would call within five minutes of my thinking about them?”

Perhaps those odds are very small.

But that calculation implicitly assumes that the remarkable outcome had been specified beforehand.

Usually it had not.

There are many other outcomes that might have generated the same reaction:

- the friend calls later that day;
- the friend sends an email;
- someone else mentions the friend;
- you encounter the friend unexpectedly;
- you see the friend's name somewhere;
- you dream about someone and hear from them the next morning;
- you think of a song and immediately hear it;
- you mention a city and later receive news from someone there;
- you recall an old teacher and encounter a former classmate.

If any of these would have prompted:

> “What are the odds?”

then they belong, in some sense, to the relevant opportunity space.

The relevant question is not merely:

$$
P(\text{this specific friend calls within five minutes}).
$$

It is closer to:

$$
P(\text{some personally striking coincidence occurs among all such opportunities}).
$$

Those probabilities may differ by orders of magnitude.

## The Description Space Is Part of the Event Space

This adds another dimension to the law of truly large numbers.

It is not only that there are many events.

There are also many ways to describe each event.

Suppose a person experiences:

$$
N
$$

events over some period.

And suppose each event admits:

$$
K
$$

potentially salient descriptions.

The effective space in which coincidences can be discovered can then become vastly larger than merely $$N$$.

We should not take the crude product

$$
NK
$$

as a literal count in most real-world cases, because the descriptions will not be independent and many will overlap. But conceptually it illustrates the problem.

A large event space becomes an even larger **event-description space**.

This is important because our intuitions about rarity often count the event but ignore the multiplicity of available descriptions.

We imagine:

> “This extraordinarily specific coincidence happened.”

But what actually happened may be:

> “Among a huge number of events, one event possessed one of a huge number of properties that I found interesting.”

Those are very different probabilistic statements.

## The Look-Elsewhere Effect

Statistics has a formal analogue of this problem: the **look-elsewhere effect**.

Suppose a scientist performs one hypothesis test with a false-positive rate of:

$$
\alpha=0.05.
$$

Then, under the null hypothesis, there is a 5 percent chance of obtaining a nominally significant result.

But suppose the scientist conducts one hundred independent tests.

The probability of obtaining at least one false positive is:

$$
P(\text{at least one})
=
1-(1-\alpha)^{100}.
$$

Substituting:

$$
P(\text{at least one})
=
1-(0.95)^{100},
$$

which is approximately:

$$
0.994.
$$

So even though any particular result would occur only 5 percent of the time under the null hypothesis, it is nearly certain that *some* apparently significant result will appear if enough tests are conducted.

This is why statistical analysis cannot simply report the most interesting result from a large search as though that result had been the only hypothesis tested.

The number of places one looked matters.

Human cognition performs an informal version of this search constantly.

We notice relationships among:

- names,
- birthdays,
- dates,
- memories,
- dreams,
- conversations,
- locations,
- illnesses,
- prayers,
- deaths,
- recoveries,
- songs,
- numbers,
- anniversaries,
- family histories,
- chance encounters.

The search is not necessarily conscious. We are simply very good at recognizing patterns when they appear.

But probabilistically, the effect is the same.

If we search enough possible relationships, some will be striking.

## The Texas Sharpshooter

The same structure is captured by the Texas sharpshooter fallacy.

Imagine someone fires a large number of bullets randomly at the side of a barn.

Afterward, the shooter finds the densest cluster of bullet holes and paints a target around it.

The cluster may genuinely be tight.

If the target had been painted there *before* the shooting, the result would be impressive.

But because the target was drawn afterward, the probability calculation changes completely.

The shooter was not attempting to hit that particular location.

They were effectively allowed to search the entire barn for whichever region happened to contain the best cluster.

The relevant event was therefore not:

$$
\text{“the bullets cluster around this predetermined point.”}
$$

It was closer to:

$$
\text{“some region of the barn contains an unusually tight cluster.”}
$$

The latter event is much more probable.

This is precisely why post-hoc specification matters.

A pattern discovered after the data are observed cannot ordinarily be assigned the same evidential significance as a pattern specified before the data were generated.

## Drawing the Target Around Experience

Many extraordinary coincidences have this structure.

First:

$$
\text{reality generates an outcome}.
$$

Then:

$$
\text{we inspect the outcome}.
$$

Then:

$$
\text{we discover an interesting description}.
$$

Finally:

$$
\text{we calculate the improbability of that description}.
$$

The sequence matters.

If the final description had been specified before the event occurred, its probability could be highly informative.

But when the description is selected because it fits the observed outcome, the raw probability of that description can greatly exaggerate how surprising the process actually was.

The problem is not that the calculated probability is necessarily mathematically wrong.

It may be perfectly correct that:

$$
P(D)=10^{-9}
$$

for some narrowly defined description $$D$$.

The problem is that $$D$$ was selected from a large family of descriptions only after the outcome was known.

The probability calculation answers:

> “How often would this particular description occur?”

But the phenomenon requiring explanation may instead be:

> “How often would some sufficiently striking description be found?”

Those are not the same question.

## Event Selection

There is another layer.

We do not analyze every event that happens to us.

Most events disappear from memory almost immediately.

A person may experience thousands of mundane occurrences in a day:

- ordinary conversations,
- unremarkable journeys,
- thoughts that lead nowhere,
- people thought about who never call,
- prayers followed by nothing memorable,
- illnesses that proceed normally,
- coincidences that almost line up but do not.

These generally do not become stories.

What becomes a story is the exceptional case.

So before description selection even begins, there is already **event selection**:

$$
\text{all events}
\rightarrow
\text{salient events}
\rightarrow
\text{events remembered and reported}.
$$

This means the set of events we hear about is highly filtered.

We disproportionately encounter the strange coincidence rather than the millions of non-coincidences that surrounded it.

We encounter the improbable recovery rather than the enormous number of ordinary recoveries.

We remember the thought immediately followed by the phone call rather than the thousands of thoughts followed by nothing relevant.

The extraordinary event is therefore selected from a much larger background that is psychologically invisible.

## Description Selection

Once the event itself has been selected, a second filtering process begins.

We identify the properties that make it interesting.

Thus:

$$
\text{selected event}
\rightarrow
\text{many possible descriptions}
\rightarrow
\text{salient description}.
$$

These two processes reinforce each other.

First, we select unusual events.

Then, within those events, we select unusual descriptions.

By the time the story reaches conscious reflection, the final object of analysis may already have passed through multiple layers of selection.

The resulting event can therefore look far more probabilistically exceptional than the underlying generative process really was.

## Meaning Is Not an Illusion

None of this requires claiming that the event lacks personal meaning.

A coincidence can be genuinely moving.

An unlikely recovery can transform someone's life.

An unexpected encounter can carry tremendous emotional significance.

Probability theory does not tell us what an event is allowed to mean to a person.

The distinction is between **personal significance** and **evidential significance**.

The fact that an event is meaningful does not automatically tell us why it occurred.

Likewise, recognizing selection effects does not erase the subjective experience. It simply prevents subjective importance from being confused with a probability calculation.

This distinction becomes especially important once the event is interpreted not merely as meaningful, but as **intentional**.

## From Significance to Agency

At this point, the structure is beginning to emerge.

First, an enormous world produces vast numbers of improbable events.

Then:

$$
\text{an unusual event is selected}.
$$

Next:

$$
\text{a meaningful description is selected}.
$$

The result is an event that appears extraordinarily unlikely under a very specific description.

But a miracle claim commonly goes one step further.

The observer does not merely conclude:

> “This event is extraordinary.”

The observer concludes:

> “This event happened for a reason.”

And often:

> “Someone intended this to happen.”

That inference introduces an entirely new probabilistic problem.

An unlikely event and an intentionally produced event are not the same category.

The fact that an event appears improbable under one description does not, by itself, establish that an agent selected that outcome.

The argument has moved from probability to agency.

And once divine agency is proposed, a new question becomes unavoidable:

> Even if this event was extraordinarily unlikely under ordinary natural processes, how likely was it under the hypothesis of divine intention?

That is where the analysis must become Bayesian.

# III. From Improbability to Divine Agency

Once an event has been selected as extraordinary and described in a way that makes its improbability salient, a common next step is to infer agency.

The reasoning often takes a form like this:

1. Event $$E$$ occurred.
2. $$E$$ was extremely improbable under ordinary natural processes.
3. Therefore ordinary natural processes are an inadequate explanation.
4. Therefore $$E$$ was probably intentional.
5. Therefore divine intervention is a plausible or likely explanation.

The intuitive force of this argument comes from the first two steps. If something appears too improbable to have happened naturally, it is tempting to conclude that some intelligence must have intended it.

But this inference moves too quickly.

The fact that an event is improbable under one hypothesis does not establish that another hypothesis is probable. At minimum, one must ask whether the alternative hypothesis actually made the event more likely.

That is a Bayesian question.

## The Bayesian Structure

Let

$$
N=\text{the event arose through non-divine natural processes}
$$

and

$$
D=\text{the event resulted from divine intervention}.
$$

After observing event $$E$$, the posterior odds are:

$$
\frac{P(D\mid E)}{P(N\mid E)}
=
\frac{P(D)}{P(N)}
\times
\frac{P(E\mid D)}{P(E\mid N)}.
$$

This equation separates two things.

The first is the prior odds:

$$
\frac{P(D)}{P(N)}.
$$

The second is the evidential contribution of the event:

$$
\frac{P(E\mid D)}{P(E\mid N)}.
$$

This second ratio is the Bayes factor.

It tells us how strongly the observed event discriminates between the two hypotheses.

This immediately reveals the weakness in the common miracle inference.

The question is not merely:

> How improbable was $$E$$ under natural processes?

The relevant question is:

> How much more probable was $$E$$ under divine intervention than under natural processes?

Those are not the same question.

## An Improbable Natural Event May Provide No Evidence for Divine Intervention

Suppose:

$$
P(E\mid N)=10^{-9}.
$$

That is an extraordinarily small probability.

If we stop here, the event sounds overwhelmingly mysterious.

But now suppose:

$$
P(E\mid D)=10^{-9}.
$$

Then the Bayes factor is:

$$
BF=
\frac{10^{-9}}{10^{-9}}
=1.
$$

The event is highly surprising under both hypotheses and therefore provides no evidence favoring one over the other.

Now suppose instead that:

$$
P(E\mid D)=10^{-12}.
$$

Then:

$$
BF=
\frac{10^{-12}}{10^{-9}}
=
10^{-3}.
$$

The event would actually favor the natural hypothesis over the divine one.

Only if:

$$
P(E\mid D)\gg P(E\mid N)
$$

does the event provide substantial evidence for divine intervention.

So the claim:

> “This event was extraordinarily unlikely naturally”

does not, by itself, establish:

> “This event was probably divinely caused.”

What is missing is a comparative likelihood.

## Surprise Is Not the Same as Evidence

This distinction can be made even clearer through information theory.

The surprisal of an event under hypothesis $$H$$ is:

$$
I(E\mid H)
=
-\log_2P(E\mid H).
$$

If:

$$
P(E\mid N)=2^{-30},
$$

then the event carries thirty bits of surprise under the natural hypothesis.

But evidence for $$D$$ over $$N$$ depends on:

$$
\log_2
\frac{P(E\mid D)}
{P(E\mid N)}.
$$

Suppose again that:

$$
P(E\mid D)=2^{-30}.
$$

Then:

$$
\log_2BF
=
\log_2
\frac{2^{-30}}{2^{-30}}
=
0.
$$

The event contains thirty bits of surprise but zero bits of evidence favoring divine intervention.

That distinction is central:

> **Surprise measures how unexpected an event is under a hypothesis. Evidence measures how differently competing hypotheses expected it.**

A miracle argument that focuses only on natural improbability confuses these two quantities.

## The Missing Question: Why Would God Do This?

At this point, a deeper problem emerges.

Suppose the proposed explanation is:

> “God caused $$E$$.”

What exactly does that tell us about:

$$
P(E\mid D)?
$$

Not very much by itself.

A divine being may be capable of producing $$E$$. But capability is not the same thing as likelihood.

The statement:

> “God could have done this”

establishes, at most, that the event is compatible with divine agency.

It does not tell us whether God would be likely to choose that event rather than any of the alternatives.

Bayesian analysis therefore forces a question that miracle arguments often leave implicit:

> Why would this being choose this particular action, at this particular time, involving this particular person, rather than one of the enormous number of other actions available?

This is the problem of divine psychology.

## Capability and Propensity

Suppose an agent is capable of actions:

$$
A_1,A_2,\ldots,A_k.
$$

If the agent is divine, that action space may be enormous.

The probability of observing $$E$$ under divine intervention can be represented schematically as:

$$
P(E\mid D)
=
\sum_i
P(E\mid A_i,D)P(A_i\mid D).
$$

Even if there is some action $$A_E$$ such that:

$$
P(E\mid A_E,D)=1,
$$

we still need to know:

$$
P(A_E\mid D).
$$

That is, how likely is the deity to choose the action that produces $$E$$?

Without an independent theory of divine preferences, motivations, goals, constraints, or intentions, that probability may be difficult or impossible to establish.

This matters because a miracle argument often treats divine agency as though it automatically assigns high probability to the observed event.

But merely saying:

> “God wanted this to happen”

after the event occurred does not show that the event was probable under a divine hypothesis beforehand.

## The Divine Action Space

Imagine a plane crash in which one person survives and many others die.

Afterward, the survivor says:

> “God saved me.”

Perhaps God could have saved that person.

But if divine intervention is the explanation, many other possibilities must also be considered.

God could have:

- prevented the plane from crashing,
- saved everyone,
- saved a different person,
- saved no one,
- caused the crash to occur differently,
- prevented the flight from departing,
- intervened in another event entirely,
- or performed an unmistakable public miracle instead.

The relevant theological hypothesis therefore does not initially specify one outcome. It contains a potentially vast action space.

The probability of the observed outcome under divine intervention depends on how probability is distributed across that action space.

If the divine hypothesis permits almost anything, then the fact that the observed outcome is compatible with it is not especially informative.

Compatibility is cheap.

Prediction is harder.

## Post-Hoc Specification of Divine Intention

The problem becomes especially clear when intention is specified only after the event.

Suppose event $$E$$ occurs.

We then define:

$$
D_E=
\text{“God specifically intended to cause }E\text{.”}
$$

Under this newly constructed hypothesis:

$$
P(E\mid D_E)\approx1.
$$

That seems impressive.

If:

$$
P(E\mid N)=10^{-9},
$$

then one might be tempted to conclude that the Bayes factor strongly favors the divine hypothesis.

But this comparison is misleading.

The hypothesis $$D_E$$ was tailored to the observation.

Before $$E$$ occurred, there might have been many possible divine-intention hypotheses:

$$
D_1,D_2,\ldots,D_k.
$$

Each corresponds to a different thing God might have chosen to do.

If there was no independent reason beforehand to privilege $$D_E$$ over the alternatives, then its apparent predictive success is illusory.

It did not predict the event.

It was constructed around it.

## Accommodation Is Not Prediction

This gives us a broader epistemic distinction.

Prediction has the structure:

$$
\text{hypothesis}
\rightarrow
\text{specific expectation}
\rightarrow
\text{observation}.
$$

Accommodation has the structure:

$$
\text{observation}
\rightarrow
\text{interpretation}
\rightarrow
\text{hypothesis fitted to observation}.
$$

Both can produce explanations.

But they are not evidentially equivalent.

If someone says before an event:

> “At noon tomorrow, person $$X$$ will experience event $$E$$ because of divine intervention,”

and the event occurs under controlled conditions, the theological hypothesis has constrained the outcome space before the observation.

That is potentially strong evidence.

By contrast, if the event occurs first and the explanation afterward becomes:

> “God must have intended this outcome,”

then the explanation has accommodated the evidence rather than predicted it.

This distinction becomes even more important when the explanatory system can accommodate many different outcomes.

## A Predictive Distribution Must Exist Before the Outcome

A model cannot simply assign high probability to whichever event happens after seeing the result.

Suppose a divine hypothesis permits:

$$
E_1,E_2,\ldots,E_k.
$$

Before observation, its predictive probability must be distributed across those possibilities.

It cannot coherently say:

$$
P(E_i\mid D)\approx1
$$

for whichever $$E_i$$ happens to occur.

That would require the probabilities to sum to far more than one.

A serious predictive model therefore has to say something about which outcomes are more likely than others.

If the hypothesis does not specify that, then its predictive content is weak.

This is the beginning of the overfitting problem.

## The Problem of Inscrutable Intentions

A common response is that divine intentions are beyond human understanding.

Perhaps that is true.

But epistemically, this creates a tradeoff.

If God's reasons are inscrutable, then it becomes difficult to say:

$$
P(E\mid D)
$$

with any confidence.

The same move that protects the hypothesis from disconfirmation also limits its ability to receive confirmation.

If almost any outcome can be reconciled with divine intention, then no particular outcome strongly favors the hypothesis.

This produces an important principle:

> **The less constrained divine intention is, the harder the hypothesis is to falsify—but the weaker any particular event becomes as evidence for it.**

A model that can explain everything may predict very little.

## The Natural Improbability Has Not Disappeared

This also exposes an important asymmetry in miracle reasoning.

The argument may begin by asking:

> “How could this particular event have happened naturally?”

But once divine agency is proposed, the corresponding question becomes:

> “Why would this particular divine agent choose this particular event?”

The improbability problem has not necessarily been solved.

It may simply have been relocated.

Under the natural model, the question is:

$$
P(E\mid N).
$$

Under the divine model, the question becomes:

$$
P(E\mid D),
$$

which itself depends on something like:

$$
P(\text{divine choice of }E\mid D).
$$

If that quantity is unknown, then the divine explanation has not automatically gained an advantage.

## The Non Sequitur

The common inference can now be stated more precisely.

It moves from:

$$
P(E\mid N)\ll1
$$

to:

$$
P(D\mid E)\gg1.
$$

But Bayes' theorem shows that this conclusion does not follow without additional premises.

We need to know:

$$
P(E\mid D),
$$

the prior odds:

$$
\frac{P(D)}{P(N)},
$$

and whether the event was specified before or after observation.

We also need to know:

- how many alternative events would have counted as miraculous,
- how many opportunities existed,
- how many descriptions were available,
- how many divine intentions could have been attributed,
- and whether the divine hypothesis actually placed substantial probability on this particular outcome beforehand.

Without that information, the inference from improbability to divine agency is incomplete.

## What Strong Evidence Would Require

This analysis does not imply that no event could ever provide evidence for divine intervention.

It tells us what stronger evidence would have to look like.

A compelling miracle claim would ideally involve:

- a narrowly specified event,
- identified before it occurs,
- with genuinely low probability under plausible natural alternatives,
- and comparatively high probability under a theological hypothesis that independently predicts it.

In other words, the theological hypothesis would need to do more than say:

> “God could have caused this.”

It would need to say something closer to:

> “Given what this hypothesis says about divine intentions, this is the kind of event we should actually expect.”

Only then can the observation discriminate between competing explanations.

## From Bayesian Evidence to Model Flexibility

The analysis now points toward a broader problem.

Many theological systems possess substantial interpretive flexibility.

The same event can be described in different ways.

Different intentions can be attributed to it.

Different outcomes can be reconciled with different divine purposes.

And different religious traditions can interpret similar events as evidence for incompatible theological conclusions.

This raises a new question.

If a theological model can be adjusted after the fact to accommodate almost any outcome, is its explanatory success genuinely predictive?

Or is it behaving like an overfit model: exceptionally good at explaining the data it has already seen, but weakly constrained before the data arrive?

That is the next stage of the analysis.

# IV. Miracle Attribution as Model Overfitting

The previous section showed that an improbable event does not become evidence for divine intervention merely because it is difficult to explain under natural processes. A divine explanation must itself assign a comparatively high probability to the event. But this requirement creates a further problem whenever the theological framework is flexible enough to accommodate many different outcomes after they occur.

This is where the analogy with model overfitting becomes useful.

In statistics and machine learning, a model is overfit when it captures the peculiarities of the data it has already seen so closely that its apparent explanatory success does not generalize well to new data. The model may fit the training set almost perfectly while having weak predictive power outside it.

Something structurally similar can happen in the interpretation of miracles.

A theological system may be able to explain an extraordinary event very well after the event has occurred. It may identify the relevant feature, assign a divine intention, connect the outcome to a theological doctrine, and produce a narrative that makes the event appear almost inevitable in retrospect.

But this raises the question:

> Did the theology predict the event, or did the theology possess enough interpretive flexibility to fit the event after the fact?

Those are not the same epistemic achievement.

## The Overfitting Analogy

The analogy can be made fairly precise.

In a predictive model:

- the **training data** are the events already observed;
- **feature selection** is the process of deciding which properties of those events matter;
- **model selection** is the choice of explanatory framework;
- **parameter fitting** is the adjustment of the model to account for the data;
- **overfitting** occurs when the model explains the observed data extremely well while generalizing poorly;
- **out-of-sample testing** asks whether the model successfully predicts new observations that were not used to construct it.

A miracle interpretation can follow a similar sequence.

First, the event occurs.

Then one selects the features that appear significant.

Then the event is interpreted through a theological framework.

Then a particular divine purpose or intention is assigned.

The result is a highly specific explanation of the observed outcome.

The sequence can be represented schematically as:

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

The danger is that retrospective explanatory fit can be mistaken for predictive success.

## Bayesian Complexity and the Cost of Flexibility

Bayesian model comparison provides a formal way to understand why flexible explanations should be treated cautiously.

Suppose a theological model $$M$$ contains interpretive parameters $$\theta$$. These parameters might represent:

- divine motives,
- theological categories,
- symbolic interpretations,
- relevant doctrines,
- possible forms of intervention,
- or possible reasons for allowing or preventing some event.

After observing event $$E$$, one can search through the available parameter space and find the setting that fits the observation best:

$$
\hat{\theta}
=
\arg\max_\theta P(E\mid M,\theta).
$$

Perhaps the best-fitting interpretation gives:

$$
P(E\mid M,\hat{\theta})\approx1.
$$

That can look impressive.

But Bayesian model comparison does not evaluate the model only at the parameter value that fits the observation best.

It asks for the model's predictive probability before the evidence is used to choose the interpretation:

$$
P(E\mid M)
=
\int
P(E\mid M,\theta)
P(\theta\mid M)
\,d\theta.
$$

The model must average over the possibilities it allowed beforehand.

If many different theological intentions were possible, then a model does not receive the full evidential credit of whichever one happens to fit the observed outcome.

This is the Bayesian version of the complexity penalty.

A flexible model can always improve its retrospective fit by introducing more possible interpretations. But the more possibilities it admits, the more thinly its prior predictive probability must be distributed across them.

This is why flexibility is a double-edged sword.

It makes accommodation easier.

But it weakens prediction.

## Retrospective Precision Can Be Misleading

Suppose that after an extraordinary recovery, someone says:

> “God preserved this person because they still had an important purpose to fulfill.”

The explanation is highly specific.

It identifies:

- the event,
- the beneficiary,
- the divine intention,
- and the significance of the outcome.

But notice the direction of construction.

The person survived first.

The purpose was inferred afterward.

If the person had died, another interpretation might have been available:

> “God called them home.”

If they had recovered gradually through ordinary medicine:

> “God worked through the doctors.”

If their condition had persisted:

> “God has a purpose in their suffering.”

The theological framework therefore does not necessarily predict one specific outcome.

It may contain a family of explanations capable of accommodating many possible outcomes.

The precision appears only after the data are known.

This is exactly the kind of situation in which an overfit model can look more powerful than it really is.

## Explanatory Flexibility and Predictive Weakness

A model becomes predictively informative by excluding possibilities.

If a theory says:

> Under these conditions, outcome $$E$$ is substantially more likely than outcomes $$F$$, $$G$$, and $$H$$,

then observing $$E$$ can confirm the theory.

But if the theory says:

> $$E$$ would be consistent with divine purpose, but so would $$F$$, $$G$$, and $$H$$,

then the occurrence of $$E$$ carries much less evidential weight.

A theory that accommodates every possibility distributes its support across every possibility.

This can be expressed in a general principle:

> **The more outcomes a hypothesis can absorb without difficulty, the less strongly any one outcome confirms it.**

This does not mean that flexible explanations are always false.

It means that explanatory flexibility should not be confused with evidential strength.

## Denominational Disagreement

This problem becomes visible when different religious traditions interpret the same kinds of events differently.

Within Christianity alone, traditions differ substantially over what sorts of events should count as miracles, what kinds of supernatural action remain possible, and what theological significance should be assigned to particular phenomena.

One tradition may interpret an event through:

- saintly intercession,
- Marian devotion,
- sacramental theology,
- charismatic gifts,
- prophecy,
- or healing.

Another tradition may reject some of those categories entirely.

A phenomenon interpreted as divine intervention by one group may be understood by another as:

- coincidence,
- mistaken attribution,
- psychological suggestion,
- ordinary providence,
- or even theological error.

The event itself has not changed.

What changes is the interpretive framework.

This illustrates an important principle:

> **Theological significance is partly model-relative.**

An event does not arrive already classified as a Catholic miracle, a Pentecostal healing, or a Protestant act of providence.

The theological model contributes the categories through which the event is interpreted.

## Competing Religious Attributions

The same problem becomes even clearer across religions.

Different religious traditions report extraordinary events and interpret them as confirmation of incompatible theological systems.

Schematically:

$$
E_C\rightarrow T_C,
$$

$$
E_M\rightarrow T_M,
$$

$$
E_H\rightarrow T_H.
$$

The letters here need not stand for any particular traditions. The point is simply that similar forms of reasoning can be used to support mutually incompatible conclusions.

A striking recovery may be interpreted as evidence of one deity in one culture and another deity in another.

A vision may be understood through one doctrinal framework by one community and an incompatible framework by another.

A coincidence may be interpreted as providential confirmation of entirely different theological commitments depending on who experiences it.

This creates a problem of discrimination.

If the same kind of evidence can be assimilated equally well into competing models, then the evidence may not strongly distinguish between those models.

A hypothesis does not gain much support merely because it can explain an observation that rival hypotheses can explain equally well.

## The Symmetry Test

This suggests a useful epistemological test.

Suppose someone regards an extraordinary event as strong evidence for their own religious tradition.

Ask:

> Would I regard the same kind of reasoning as equally compelling if a member of a rival tradition used it to confirm their theology?

If the answer is no, then one should ask what distinguishes the cases.

Perhaps there is a genuine asymmetry.

Perhaps one event is better documented.

Perhaps one tradition made a prior prediction that another did not.

Perhaps one hypothesis assigns a much higher likelihood to the event.

But if no such independent difference can be established, then the evidential force may be coming partly from prior theological commitment rather than from the event itself.

The symmetry test does not prove that all miracle claims are equally weak.

It asks whether the inferential standard is being applied consistently.

## Model-Relative Descriptions

This also returns us to the earlier problem of description selection.

The same event can be described in very different ways depending on the model.

A recovery might be described as:

> “spontaneous remission,”

or:

> “an answer to prayer,”

or:

> “intercession by a saint,”

or:

> “evidence of charismatic healing,”

or:

> “an unexplained medical event.”

These are not merely alternative labels.

They carve the event into different explanatory categories.

The model determines which features are emphasized and which are ignored.

A theological framework can therefore influence not only the explanation of the event, but the very description of what the event is.

This creates an additional layer of flexibility:

$$
\text{same observation}
\rightarrow
\text{different model}
\rightarrow
\text{different salient features}
\rightarrow
\text{different explanation}.
$$

The event is not interpreted in a vacuum.

## The Plane-Crash Survivor

The plane-crash example reveals another important form of selection.

Suppose a plane carrying two hundred people crashes.

One person survives.

One hundred and ninety-nine die.

The survivor says:

> “God saved me for a reason.”

The selected datum is:

$$
E=\text{this person survived}.
$$

But the complete outcome is:

$$
D=
\{199\text{ deaths},1\text{ survival}\}.
$$

Why is the survivor's outcome isolated and treated as evidence of divine intention?

If divine agency is being proposed to explain the event, then the entire pattern should matter.

Why did the intervention take the form:

$$
199\text{ deaths}+1\text{ survival}?
$$

Why this survivor?

Why not prevent the crash?

Why not save everyone?

Why not intervene in some different way?

The miracle narrative usually focuses on the one salient success and treats the remaining outcomes as background.

This is a form of event selection.

## Survivorship Bias and Miracle Testimony

The plane-crash example also illustrates a deeper reporting asymmetry.

Survivors can:

- tell their stories,
- interpret their survival,
- describe meaningful coincidences,
- give testimony,
- publish memoirs,
- speak about providence.

The dead cannot generate symmetrical accounts of divine non-intervention.

This creates a structural bias in the available testimony.

The people most capable of reporting extraordinary survival are precisely the people who survived.

The result is that miracle narratives can become disproportionately populated by the favorable tail of the outcome distribution.

This does not mean those survivors are dishonest.

It means that the available evidence has been selected by the outcome itself.

## Prayer and Asymmetric Interpretation

The same asymmetry is visible in prayer.

Consider several possible outcomes after someone prays for recovery.

If the person recovers unexpectedly:

> God performed a miracle.

If the person recovers through medical treatment:

> God worked through the doctors.

If the person recovers slowly:

> God answered in his own time.

If the illness persists:

> God has a purpose in the suffering.

If the person dies:

> God called them home.

If nothing apparently happens:

> God's answer was no, or not yet.

Again, the point is not that any particular interpretation is necessarily false.

The issue is that the system can accommodate nearly every possible outcome.

This creates a predictive problem.

If:

$$
E_1,E_2,E_3,E_4,E_5
$$

can all be readily incorporated into the same theological framework, then observing $$E_1$$ may not be strong confirmation of that framework.

The model survived the observation because it was flexible enough to survive nearly any observation.

## One-Sided Updating

A well-calibrated evidential system should specify what counts:

- in favor of the hypothesis,
- against the hypothesis,
- and as neutral.

But some miracle reasoning operates asymmetrically.

A favorable event increases confidence:

$$
\text{unexpected recovery}\rightarrow\text{evidence for intervention}.
$$

An unfavorable event does not decrease confidence:

$$
\text{death}\rightarrow\text{mysterious divine purpose}.
$$

This creates a form of one-sided updating.

The hypothesis gains credit when events appear to support it but is protected from evidential loss when events appear contrary to it.

That is not ordinary Bayesian reasoning.

Bayesian updating requires that evidence can move probabilities in both directions.

If a model is configured so that no possible observation counts significantly against it, then the model may be difficult to falsify, but it also becomes difficult to confirm.

## A Theory That Explains Everything

This leads to a broader philosophical point.

Suppose a theory can accommodate:

- survival,
- death,
- recovery,
- illness,
- success,
- failure,
- answered prayer,
- unanswered prayer,
- visible intervention,
- hidden intervention.

It may appear extraordinarily powerful because nothing falls outside its explanatory reach.

But there is an important distinction between:

> a theory that explains every outcome after it occurs,

and:

> a theory that successfully tells us which outcome to expect before it occurs.

The first is explanatory flexibility.

The second is predictive power.

They should not be confused.

A theory can have nearly perfect retrospective explanatory coverage and very little prospective constraint.

That is precisely the pattern associated with overfitting.

## Training Data and Test Data

The machine-learning analogy can now be stated more sharply.

Observed miracle reports function like training data.

The theological system is repeatedly adjusted or interpreted so that those observations make sense.

But genuine predictive success requires something like a test set: events not used to construct the explanation.

The important question becomes:

> What did the model say before the next event occurred?

If a theological hypothesis repeatedly made narrow, risky predictions and those predictions succeeded, that would be evidence of generalization.

If instead the interpretive framework changes after each outcome so that the result always becomes meaningful, then the model may fit the past while predicting little about the future.

In machine-learning terms:

> **A model that memorizes the training data has not demonstrated that it understands the underlying process.**

## The Search Over Intentions

The overfitting problem becomes even stronger once divine intentions are included.

Suppose an event can be associated with many possible purposes:

- to protect someone,
- to teach someone,
- to punish someone,
- to inspire faith,
- to reveal providence,
- to preserve free will,
- to produce spiritual growth,
- to test belief,
- to remain hidden,
- to fulfill some unknown plan.

After almost any outcome, one can search through this intention space until a plausible purpose is found.

This creates another look-elsewhere effect.

We are no longer searching merely over:

$$
\text{events}
$$

and:

$$
\text{descriptions}.
$$

We are also searching over:

$$
\text{possible intentions}.
$$

The full process is therefore:

$$
\text{event space}
\times
\text{description space}
\times
\text{intention space}.
$$

That combined space can be enormous.

A meaningful explanation discovered somewhere in it may feel highly specific even though the search process itself made such a fit likely.

## Three Layers of Selection

The structure of miracle attribution can now be summarized as three nested selection processes.

First:

$$
\text{Which event?}
$$

Out of an enormous number of occurrences, some event is selected because it is unusual or emotionally salient.

Second:

$$
\text{Which description?}
$$

Out of many possible ways to characterize the event, one description makes it appear especially meaningful or improbable.

Third:

$$
\text{Which intention?}
$$

Out of many possible divine purposes, one is selected that makes the outcome appear purposeful.

Thus:

$$
\text{event selection}
\rightarrow
\text{description selection}
\rightarrow
\text{intention selection}.
$$

Each stage narrows the story after the fact.

By the end, the explanation can appear remarkably precise.

But its precision may be retrospective rather than predictive.

## Why This Matters for Religious Disagreement

This framework helps explain why people within different theological systems can encounter similar events and reach very different conclusions.

They are not necessarily disagreeing about the raw event.

They may be operating with different:

- description spaces,
- intention spaces,
- background doctrines,
- theological expectations,
- and criteria for what counts as supernatural.

A Catholic, a Pentecostal, a cessationist Protestant, a Muslim, a Hindu, and a naturalist may observe a superficially similar event and classify it in radically different ways.

That is exactly what we should expect if the evidence underdetermines the interpretation and the background model contributes heavily to the final explanation.

The event alone does not resolve the disagreement.

## The Deeper Lesson

The central problem is not that theological explanations are necessarily incapable of explaining extraordinary events.

Quite the opposite.

The problem is that they may be capable of explaining too many of them, in too many different ways, after the outcome is already known.

That flexibility creates an illusion of precision.

A narrative may fit an event beautifully.

It may make the timing seem meaningful.

It may supply a motive.

It may connect the event to a larger theological story.

But none of those things, by themselves, establish that the model assigned substantial probability to the event beforehand.

The distinction can be stated simply:

$$
\text{retrospective explanatory fit}
\neq
\text{prospective predictive success}.
$$

And this is the point at which the earlier pieces of the argument begin to converge.

The law of truly large numbers explains why extraordinary events will continually occur.

Selection effects explain why some of them become salient.

Description selection explains why they can appear uniquely meaningful.

Divine-intention selection explains why they can appear purposeful.

Model flexibility explains why the resulting theological story can fit the event so well.

But none of those facts alone establish that the event was actually predicted by the theological hypothesis.

The final question is therefore not:

> Can this event be interpreted as a miracle?

With enough flexibility, many events can.

The more important question is:

> Did the miracle hypothesis make this event substantially more expected before the event occurred than competing explanations did?

That is the difference between a model that accommodates the world and a model that successfully predicts it.

# V. The Probabilistic Anatomy of a Miracle

The analysis so far has moved through several distinct layers.

First, the law of truly large numbers showed why extremely improbable events should occur regularly in a world containing enormous numbers of opportunities. Then the problem of description showed why some of those events become psychologically salient while others remain unnoticed. Bayesian analysis showed that natural improbability is not itself evidence of divine action. Finally, the model-overfitting analogy showed how flexible theological interpretations can produce strong retrospective explanations without corresponding predictive power.

These points can now be combined into a single structure.

A miracle claim often begins not with a prediction, but with an observation.

Something unusual happens.

The event is noticed because it is rare, emotionally significant, or narratively striking. A particular description is then selected that makes the event appear especially improbable or meaningful. The event is placed inside a theological framework. A divine intention is assigned. The final story can become highly specific:

> This happened to this person, at this time, for this reason, because God intended this outcome.

By the end of the process, the event can seem almost tailor-made.

But the apparent precision of the explanation may have been generated gradually after the event occurred.

The full sequence can be represented as:

$$
\text{enormous event space}
$$

$$
\downarrow
$$

$$
\text{rare events inevitably occur}
$$

$$
\downarrow
$$

$$
\text{salient event selected}
$$

$$
\downarrow
$$

$$
\text{meaningful description selected}
$$

$$
\downarrow
$$

$$
\text{natural improbability emphasized}
$$

$$
\downarrow
$$

$$
\text{theological framework applied}
$$

$$
\downarrow
$$

$$
\text{divine intention attributed}
$$

$$
\downarrow
$$

$$
\text{retrospective fit experienced as confirmation}.
$$

This is the probabilistic anatomy of many miracle claims.

The important point is not that any individual step must be illegitimate. The problem arises when the final specificity of the explanation is treated as though it had existed before the observation.

## Three Different Questions

Miracle discussions often collapse several distinct questions into one.

The first is:

> Was the event improbable?

The second is:

> Was the event intentional?

The third is:

> Was the intention divine?

These are separate inferential steps.

An event can be highly improbable without being intentional.

An event can be intentional without being divine.

And an event can be compatible with divine agency without providing substantial evidence for it.

The distinctions can be written simply as:

$$
\text{improbable}
\not\Rightarrow
\text{intentional},
$$

and:

$$
\text{intentional}
\not\Rightarrow
\text{divine}.
$$

Much of the intuitive force of miracle claims comes from moving across these transitions too quickly.

## The First Transition: From Improbability to Intention

The fact that an event is unlikely does not imply that it was selected by an agent.

Every shuffled deck produces an exact sequence with probability:

$$
\frac{1}{52!}.
$$

Every lottery winner experiences an outcome that was extraordinarily unlikely for that particular person.

Every sufficiently large population generates extreme outliers.

The world constantly produces outcomes that would have been difficult to predict beforehand.

Therefore:

$$
P(E\mid N)\ll1
$$

does not imply:

$$
P(\text{intentional causation}\mid E)\gg1.
$$

To infer intention, one needs evidence that the observed structure is more likely under intentional production than under the relevant alternatives.

This is why prior specification matters so much.

If an agent announces a target before acting and repeatedly hits it, intention is plausible because the target was fixed independently of the outcome.

If the target is drawn around the result afterward, the inference is weaker.

## The Second Transition: From Intention to Divinity

Even if intentional causation were established, a further inference would still be required.

Suppose an event contains features that strongly suggest agency.

That does not yet establish the identity of the agent.

One must distinguish among:

- human action,
- fraud,
- hidden technological intervention,
- unknown natural processes,
- non-divine agency,
- and divine intervention.

The theological conclusion therefore requires more than establishing that chance alone is an incomplete explanation.

It requires positive discrimination among competing causal hypotheses.

This is another place where the argument from improbability can become too quick.

The structure:

$$
\text{chance seems unlikely}
\rightarrow
\text{therefore God}
$$

omits a potentially large hypothesis space between those two points.

## Compatibility Is Not Confirmation

A further distinction is essential.

An event may be compatible with a hypothesis without providing evidence for it.

Suppose hypothesis $$H$$ permits event $$E$$.

Then:

$$
P(E\mid H)>0.
$$

But this tells us almost nothing about whether $$E$$ confirms $$H$$.

For confirmation, the event needs to be comparatively more likely under $$H$$ than under relevant competitors.

In Bayesian terms, what matters is:

$$
\frac{P(E\mid H)}
{P(E\mid H')}.
$$

If both hypotheses accommodate the event equally well, then the observation does little to distinguish them.

This is especially important for theological claims because a broad divine hypothesis may be compatible with an enormous range of outcomes.

The statement:

> “God could have done this”

is therefore much weaker than:

> “If this theological hypothesis were true, we would have had strong reason to expect this event rather than its alternatives.”

The latter is what evidential support requires.

## A Better Standard for Miracle Claims

The analysis does not imply that miracle claims should be dismissed automatically.

Instead, it suggests a more demanding standard.

A strong miracle claim would need to minimize the same sources of flexibility that make post-hoc explanations easy.

Several features would make such a claim substantially more informative.

### Antecedent Specification

The relevant event should be identified before it occurs.

If the target is fixed beforehand, then the probability calculation is not contaminated by retrospective selection.

This transforms:

$$
\text{outcome}
\rightarrow
\text{description}
$$

into:

$$
\text{description}
\rightarrow
\text{outcome}.
$$

That reversal is crucial.

### Narrow Prediction

The hypothesis should constrain what is expected.

A theory that predicts one narrow class of outcomes is more informative than one compatible with almost anything.

If a theological hypothesis predicts:

$$
E
$$

rather than:

$$
E\lor F\lor G\lor H\lor\cdots,
$$

then observing $$E$$ carries more evidential weight.

Prediction gains force by excluding alternatives.

### Low Probability Under Natural Alternatives

The event should genuinely be unlikely under plausible non-divine explanations.

This requires more than saying that the exact outcome was improbable.

The relevant probability must account for:

- the total number of opportunities,
- the look-elsewhere effect,
- alternative descriptions,
- selection effects,
- and realistic natural mechanisms.

The correct denominator matters.

### High Probability Under the Divine Hypothesis

This is the requirement most often neglected.

A miracle claim does not become strong merely because:

$$
P(E\mid N)
$$

is small.

One also needs an independent basis for thinking:

$$
P(E\mid D)
$$

is comparatively large.

Without that, the Bayes factor cannot be established.

### Independent Reasons About Divine Intention

The predicted action should not be inferred solely from the fact that the action occurred.

There must be some prior theological reason to expect:

- this kind of intervention,
- for this kind of purpose,
- under these circumstances.

Otherwise divine psychology is being reconstructed from the outcome.

### Correction for Multiple Opportunities

The calculation should include the full opportunity space.

If millions of events could have generated a miracle narrative, one should not calculate the probability of the selected case as though it were the only relevant opportunity.

Likewise, if many different descriptions would have counted as meaningful, that multiplicity must be considered.

### Symmetrical Treatment of Success and Failure

A serious evidential framework must allow observations to count against the hypothesis.

If successful outcomes confirm the model while failures are automatically reinterpreted as hidden purpose, the updating procedure becomes one-sided.

A meaningful prediction must risk being wrong.

### Discrimination Between Competing Theologies

A miracle claim should not merely distinguish:

$$
\text{natural}
$$

from:

$$
\text{supernatural}.
$$

If the event is being used to support a particular religion, denomination, or theological doctrine, then it should also discriminate among rival religious explanations.

Otherwise the evidence may at most support a very broad claim about agency, not the specific theology being asserted.

## What a Strong Case Might Look Like

Consider an intentionally exaggerated example.

Suppose a religious community publicly announces in advance that:

- a specific person,
- at a specific location,
- at a specific time,
- will experience a specific physically extraordinary event,
- under clearly stated theological conditions.

The claim is recorded before the event.

Independent observers are present.

The event occurs as specified.

The phenomenon is difficult to explain under known natural processes.

The theological hypothesis had a clear prior reason to predict precisely that outcome.

Failed predictions from the same system are also recorded rather than ignored.

This would be epistemically different from a spontaneous recovery interpreted retrospectively.

The important difference would not merely be that the event was more dramatic.

It would be that the hypothesis constrained the outcome space beforehand.

Its success would therefore resemble genuine out-of-sample prediction.

The relevant Bayes factor could plausibly become large:

$$
BF=
\frac{P(E\mid D)}
{P(E\mid N)}.
$$

This is what strong miracle evidence would have to approximate.

## Why This Standard Is Not Anti-Miracle by Definition

It is important that the method not assume its conclusion.

If one begins by declaring that miracles are impossible, then no evidence could ever count.

That would make the argument circular.

The probabilistic approach does something different.

It leaves open the possibility that:

$$
P(D\mid E)
$$

could become large.

But it insists that the increase must come through ordinary evidential reasoning.

The miracle hypothesis must make successful predictions, outperform alternatives, and survive failed opportunities.

In that sense, the method is neutral with respect to the metaphysical possibility of miracles.

It asks only whether the evidence actually favors the hypothesis.

## What the Argument Does Not Show

The argument therefore does not establish:

$$
P(D)=0.
$$

It does not prove that divine intervention never occurs.

It does not show that every miracle testimony is fraudulent.

It does not imply that personally meaningful coincidences are psychologically trivial.

It does not establish that unusual recoveries or extraordinary survivals are uninteresting.

Nor does it require that every unexplained event eventually receive a conventional natural explanation.

The conclusion is narrower.

It concerns what can legitimately be inferred from improbability.

The argument establishes that:

> **The natural improbability of a retrospectively selected event is insufficient, by itself, to establish intentional divine causation.**

That is a modest claim, but it has broad consequences.

## Why “Unexplained” Is Not a Causal Explanation

Another distinction follows.

Sometimes an event genuinely remains unexplained.

This can be expressed as:

$$
P(\text{current explanation is adequate})\text{ is low}.
$$

But from this it does not follow that a particular alternative explanation is true.

Ignorance does not automatically transfer probability to whichever hypothesis is most culturally or emotionally available.

The proper conclusion from:

> “We do not currently know why this happened”

may simply be:

> “We do not currently know why this happened.”

An explanatory gap is not itself evidence for a particular agent.

This is especially important when the proposed agent has poorly specified motivations.

If the natural explanation is unknown and the divine explanation also lacks a clear predictive distribution, then uncertainty remains on both sides.

## The Importance of the Full Dataset

The same principle applies to selective evidence.

Suppose one person recovers unexpectedly from a disease after prayer.

That event may seem remarkable.

But if the claim concerns the efficacy of divine intervention, the relevant evidence includes not only the recovery but all comparable cases:

- prayers followed by recovery,
- prayers followed by no recovery,
- no prayer followed by recovery,
- no prayer followed by no recovery.

The probability model should be conditioned on the complete evidence rather than the most memorable case.

In simplified form, the relevant comparison is not:

$$
P(\text{this recovery})
$$

but something more like:

$$
P(\text{observed pattern of recoveries and failures}\mid H).
$$

The same logic applies to survival, prophecy, visions, coincidences, and other miracle claims.

Evidence should be evaluated at the level of the process, not merely the anecdote.

## The Difference Between a Story and a Model

Miracle narratives are often compelling because stories naturally emphasize coherence.

A story selects:

- relevant characters,
- relevant events,
- meaningful timing,
- causal relationships,
- and resolution.

That structure is precisely what makes stories intelligible.

But probability models operate differently.

A model must account not only for the events that complete the narrative, but for the enormous background of events that did not.

The story asks:

> Why did this happen?

The model asks:

> How often would this kind of outcome arise under each competing hypothesis?

Those are different forms of explanation.

The first seeks meaning.

The second seeks discrimination.

Confusing them can make a meaningful narrative appear more evidentially powerful than it is.

## Meaning and Cause

This distinction allows a more charitable way to think about religious experience.

An event can have profound personal meaning without its causal interpretation being established.

Someone may survive an accident and experience that survival as a moral turning point.

Someone may recover from illness and interpret the experience through prayer.

Someone may encounter a coincidence that reorganizes how they think about their life.

Those meanings are real in the sense that they affect the person's values, identity, and decisions.

But:

$$
\text{meaningful to an observer}
$$

does not entail:

$$
\text{intentionally produced for that meaning}.
$$

This is another place where different explanatory domains should not be collapsed.

A psychological or existential interpretation is not automatically a causal inference.

## From Miracles to a General Epistemic Principle

Although the discussion has focused on religion, the underlying principle is much broader.

The same structure appears whenever humans infer agency or hidden design from unusual events.

It appears in:

- conspiracy reasoning,
- paranormal claims,
- financial pattern detection,
- prophecy,
- pseudoscientific prediction,
- retrospective historical explanation,
- and everyday coincidence.

The general lesson is:

> **A pattern discovered after searching a large space of possibilities should not be evaluated as though that pattern had been uniquely specified beforehand.**

Likewise:

> **An explanation capable of accommodating many outcomes should not receive the evidential credit of a model that specifically predicted the observed one.**

Miracle reasoning is therefore one instance of a more general problem in human inference.

## The Central Asymmetry

By this point, the deepest asymmetry in many miracle claims should be visible.

Natural explanations are often required to specify:

- exact probabilities,
- mechanisms,
- frequencies,
- causal pathways,
- and alternative outcomes.

The divine explanation, by contrast, may be permitted to remain:

> “God wanted this.”

But if the natural hypothesis is penalized for failing to make the event highly probable, then the divine hypothesis should be held to the same standard.

It must also answer:

> Why this outcome?

> Why this person?

> Why this time?

> Why this manner of intervention?

> Why not the alternatives?

If those questions cannot be answered, then the divine hypothesis may remain possible, but its comparative likelihood is not established.

The evidential standards should be symmetrical.

## The Core Inference Revisited

The common miracle inference can now be reconstructed.

It begins with:

$$
P(E\mid N)\ll1.
$$

It then moves, often implicitly, toward:

$$
P(D\mid E)\gg1.
$$

But between those statements lie several unresolved questions:

$$
P(E\mid D)=?
$$

How large was the relevant event space?

How many opportunities existed?

How many possible descriptions would have counted as significant?

Was the event specified before or after observation?

How many divine intentions were available?

Which observations would have counted against the divine hypothesis?

Would the same reasoning be accepted when used by a competing religion?

Until those questions are addressed, the inference remains incomplete.

The event may be astonishing.

It may be unexplained.

It may be deeply meaningful.

But those facts alone do not establish divine intention.

## A More Careful Vocabulary

It is therefore useful to separate several categories that ordinary language often collapses.

An event can be:

**rare** — it has low probability under some specified model.

**surprising** — it was not strongly expected by an observer.

**salient** — it attracts attention because of its emotional or structural features.

**meaningful** — it is integrated into a person's narrative or worldview.

**unexplained** — no currently accepted causal account adequately explains it.

**intentional** — it was deliberately selected by an agent.

**divine** — the relevant agent is a deity.

None of these categories automatically entails the next.

The movement from one to another requires additional evidence.

That is perhaps the simplest way to understand the entire argument.

## Toward a Probabilistic Understanding of Miracles

A probability-based understanding of miracle claims therefore begins not by asking whether miracles are possible, but by asking how extraordinary events arise and how they acquire interpretation.

The law of truly large numbers tells us that rare events should occur.

Selection effects tell us why some become memorable.

Description selection tells us why they can appear exquisitely specific.

Bayesian reasoning tells us that natural improbability alone does not favor divine intervention.

The analysis of divine psychology tells us that an agent's capability does not establish its propensity to act.

Model overfitting explains how theological systems can achieve excellent retrospective fit.

And theological pluralism shows why the same kinds of events can support incompatible interpretations.

Taken together, these ideas do not eliminate the category of miracle.

They make the evidential threshold clearer.

A miracle, if it is to function as evidence rather than simply as a theological interpretation of an unusual event, must do more than surprise us.

It must discriminate.

# VI. Conclusion: From Anomaly to Intention

The question “What are the odds?” often feels like the beginning and end of an argument about miracles.

In reality, it is only the beginning.

To ask what the odds are, we first have to specify the event. We have to know the relevant reference class, the number of opportunities, the range of alternative outcomes, and the number of descriptions under which the event could have appeared significant. We have to distinguish the probability of one exact outcome from the probability that some comparably striking outcome would occur somewhere in a vast event space.

Once those distinctions are made, much of the apparent mystery surrounding rare events begins to dissolve.

A one-in-a-million event is extraordinary when there is one opportunity for it to occur. It is expected when there are millions of opportunities. A fantastically improbable card sequence is unremarkable if some sequence had to occur. A coincidence can be genuinely rare under the description selected after the fact while being unsurprising as one member of a much larger family of possible coincidences.

The world does not need to suspend probability in order to generate extraordinary events.

It needs only enough opportunities.

This is the basic lesson of Littlewood's intuition, Dyson's formulation, and the law of truly large numbers. But the argument does not end there, because humans do not observe the world as passive statistical instruments.

We select.

Out of the enormous number of events that occur, we remember the unusual ones. Out of the many ways an event can be described, we notice the description that makes it meaningful. Out of the many possible interpretations available, we may select one that fits our prior worldview.

The process can be summarized as:

$$
\text{event selection}
\rightarrow
\text{description selection}
\rightarrow
\text{intention selection}.
$$

At each stage, the event becomes more narratively specific.

By the end, an occurrence that began as one outcome among countless others can acquire a remarkably precise interpretation:

> This happened to me, at this moment, for this reason, because it was intended.

But the precision of a retrospective explanation should not be confused with the precision of a prediction.

That distinction is where Bayesian reasoning becomes indispensable.

The fact that an event is improbable under natural processes does not by itself imply that divine intervention is probable.

The relevant comparison is not merely:

$$
P(E\mid N).
$$

It is:

$$
\frac{P(E\mid D)}
{P(E\mid N)}.
$$

An event favors divine intervention only insofar as the divine hypothesis made that event more expected than the alternatives did.

This is the distinction between surprise and evidence.

An event can be extraordinarily surprising under one model while providing no support for another. It can be unexplained without being divinely explained. It can be meaningful without being intentional. It can be intentional without being divine.

These distinctions are easy to collapse because they often occur together in human experience.

Someone survives an accident against extraordinary odds. The survival is rare. The person experiences it as meaningful. The timing appears significant. A theological interpretation supplies a reason.

The resulting narrative can be deeply compelling.

But the inferential structure still contains several separate steps:

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

and:

$$
\text{compatible with a hypothesis}
\not\Rightarrow
\text{evidence for that hypothesis}.
$$

The last distinction is especially important.

A theological model may be capable of accommodating an event beautifully after it occurs. But if the model was also capable of accommodating many alternative outcomes, then the fact that it can explain the one that happened is not necessarily impressive.

A model that can explain survival, death, recovery, illness, success, failure, answered prayer, unanswered prayer, visible intervention, and hidden purpose has enormous interpretive flexibility.

That flexibility can make the model feel powerful.

But predictive power comes from constraint.

A model becomes informative when it says that some outcomes should be expected more than others. It risks being wrong. It allows future observations to count against it.

A theory that can accommodate nearly everything may be difficult to falsify, but that same flexibility limits how strongly any particular event can confirm it.

This is why the analogy with model overfitting is useful.

A highly flexible model can fit the data already observed with remarkable precision. It can identify the relevant features, choose the interpretation, and produce an elegant explanation. But without successful prediction outside the data used to construct the explanation, retrospective fit does not establish general explanatory power.

The same issue appears in religious pluralism.

Different denominations and different religions can interpret similar extraordinary events through incompatible theological frameworks. The same kind of recovery, vision, coincidence, or apparent answer to prayer can be taken as confirmation of very different doctrines.

This does not prove that every interpretation is false.

It does show that the raw event does not uniquely determine its theological meaning.

The interpretive model contributes substantially to the conclusion.

That fact should make us cautious whenever an event is presented as though its theological significance were simply contained within the event itself.

The plane-crash survivor provides a particularly stark example.

If one person survives while many others die, the survival may be interpreted as providential. But the complete dataset contains both the survival and the deaths.

To isolate the survivor as evidence of divine intervention while treating the deaths as theologically neutral is already to make a selection.

The same asymmetry can appear in prayer. A recovery may be counted as answered prayer, while death or continued illness is interpreted through a different theological explanation that leaves the hypothesis intact.

If evidence can only confirm a belief and almost never count against it, then something other than ordinary probabilistic updating is occurring.

A stronger miracle claim would look different.

It would narrow the outcome space before the event.

It would specify what should happen.

It would expose itself to failure.

It would establish that the event is genuinely improbable under plausible alternatives.

And it would provide independent reasons for thinking that the proposed divine hypothesis assigns comparatively high probability to that event.

In other words, it would move from:

$$
\text{observation}
\rightarrow
\text{interpretation}
$$

toward:

$$
\text{hypothesis}
\rightarrow
\text{prediction}
\rightarrow
\text{observation}.
$$

Such evidence is possible in principle.

Nothing in probability theory requires that:

$$
P(D)=0.
$$

The point is not that miracles cannot happen.

The point is that rare events do not become miracles merely by being rare.

Nor do meaningful events become intentional merely by being meaningful.

Nor does an unexplained event become evidence of divine agency merely because a divine explanation can be constructed after the fact.

The evidential question begins only after all of these distinctions have been made.

We must ask:

What was the relevant event space?

How many opportunities existed?

Was the event specified in advance?

How many other outcomes would also have seemed miraculous?

How many descriptions could have made the event significant?

Why would the proposed agent choose this outcome rather than another?

What would have counted against the hypothesis?

And most importantly:

Did the proposed divine explanation actually make this event more expected than competing explanations did?

Once the question is framed this way, the category of “miracle” begins to separate into several different phenomena.

There is the improbable event.

There is the human recognition of significance.

There is the attribution of intention.

And there is the further theological claim about the identity of the agent.

Those are not one inference.

They are several.

Probability theory cannot tell us what events are allowed to mean to us. It cannot rule out every form of divine action. But it can tell us when our astonishment has outrun our evidence.

In a sufficiently large world, extraordinary events are not exceptions to probability.

They are consequences of it.

The world supplies the anomaly.

Selection makes it salient.

Interpretation makes it meaningful.

Overfitting can make it look predicted.

The remaining question is whether anything actually predicted it.