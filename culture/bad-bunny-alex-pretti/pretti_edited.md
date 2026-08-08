# Alex Pretti: When Something Becomes Evidence

This is something that has been on my mind for as long as I can remember. "Evidence” sounds like a simple, objective relationship (“E supports H”), but in actual inferential life it’s *mediated*—by background assumptions, concepts, standards, goals, and social context. So two people can share all the same “facts” and still reasonably (or unreasonably) disagree about what those facts mean for a claim. I first want to explore this nature of evidence, before showing how this "underdetermination" of evidence can be aritificially amplified (by the media), as observed in the Alex Pretti case.

Evidence isn’t a property of a fact alone; it’s a role a fact plays in an argument. A few concepts need to be clarified:

* **Data / fact**: some observation, testimony, measurement, record.
* **Hypothesis / theory**: what you’re trying to decide between. Some explanatory account of the data/facts.
* **Linking assumptions**: how the world would have to be for that data to show up if the hypothesis were true (measurement reliability, causal story, category definitions, base rates, etc.).
* **Standards of relevance**: what counts as “support” (prediction? explanation? coherence? robustness? practical stakes?).

On this view, *E becomes evidence for H only relative to a background package*: E is evidence for H **given** background assumptions B and a question Q. That’s already enough to explain a lot of “same facts, different conclusions” disagreements: people often share E, but not B or Q.

There are a few common mechanisms that explain why the same fact can support opposite conclusions. They look similar on the surface (“we disagree about evidence”), but they’re different kinds of disagreement.

1. **Different background beliefs (priors, base rates, auxiliary assumptions)**: Even in Bayesian terms, whether E favors A or B depends on *likelihoods* that come from background beliefs: P(E|A) vs P(E|B). If we disagree about those, we can disagree about evidential direction.
2. **Different “reference classes” (what this case is *a case of*)**:  fact can shift meaning depending on what category you place it in. For example, something as simple as “He left early" can be evidence of **disinterest** if it’s a date or evidence of **responsibility** if it’s a parent leaving to pick up a kid. The observed behavior is the same; the classification changes the inference.
3. **Different causal stories (correlation gets “explained away”)**: E can look like evidence for H until someone introduces an alternative causal pathway that makes E expected even if H is false. This is one big way “facts themselves impact interpretive frames”: new facts can change which causal model you think you’re in, which changes what counts as evidence going forward.
4. **Different standards of support (prediction vs explanation vs robustness)**: Two people might both agree that E raises P(H), but disagree whether that is *good enough* to “count as evidence worth acting on.” One person might say “It nudges probability, so it’s evidence.” Another might say “Unless it’s robust across methods / not cherry-pickable / survives adversarial checks, it’s not evidence (or not strong evidence).” So the dispute isn’t about probability raising, but about *epistemic norms*.
5. **Different feature selection (which aspect of the fact matters)**: Many facts are high-dimensional. A graph has slope, variance, outliers, time window, scale, omitted variables. A witness report has confidence, vantage point, incentives, consistency, corroboration. Evidence disputes often come from spotlighting different features: one person treats the outliers as signal, the other as noise.

Its also common to have situations where “E used to support A, now supports B”. For example, a shift after sustained media exposure can happen through multiple routes, some rational, some not.

- Rational-ish routes (in principle): In Bayesian terms, it can be perfectly coherent if your model of the world changes, what E discriminates between changes too.

  * **New auxiliary beliefs**: you learn (or think you learn) the measurement is biased, or the causal mechanism is different than assumed.
  * **Reframing the question**: you stop asking “Is A true?” and start asking “Is A *the best explanation*?” or “Is A *what matters*?”
  * **Changing the hypothesis space**: you previously considered only A vs not-A; later you entertain B as a live alternative that fits E better.

- Non-rational / socially-driven routes

  * **Motivated reasoning**: you prefer B (identity, group status, moral signaling), so you re-weight what “counts.”
  * **Availability and salience**: media makes certain exemplars vivid, changing what seems typical.
  * **Concept drift**: the meaning of key terms shifts (“fraud,” “violence,” “freedom,” “expert”), so the same E is now “about” something else.
  * **Trust realignment**: you change which sources you treat as credible, which affects what you treat as “fact” in the first place.

So the evidential relation changes either because the world-model changes, or because the attention/trust/identity machinery changes (or both).

Philosophers often define evidence as a probability raising relation, that is: “E is evidence for H iff it raises P(H)”. This hides the messy parts of reasoning with and about evidence in the wild. The definition excludes recurring questions such as:

* Where do priors come from?
* How do we choose the hypothesis space?
* How do we model likelihoods?
* What do we treat as the relevant description of E?
* How do we handle underdetermination (many theories fit the same facts)?

Those are not small technicalities; they’re where most disagreement lives. In real life, we often use *meta-evidential* norms—criteria that make a putative E trustworthy as evidence:

* **Independence**: does it survive when measured different ways?
* **Robustness / replication**: does it repeat across contexts?
* **Specificity**: is it predicted uniquely by H, or also by many rivals?
* **Resistance to cherry-picking**: does it depend on selective time windows, metrics, or anecdotes?
* **Error sensitivity**: would we likely notice if we were wrong?
* **Adversarial testing**: has it been stress-tested by people who *want* to debunk it?

Notice these norms aren’t captured by “probability raising” alone—they’re about *how likely we are to be misled*, given human and institutional limitations.

When you hear “E is evidence for H,” silently expand it to: Under description D of the data, within model M, given background assumptions B, with standards S, for question Q, E supports H. Then disagreements become diagnosable:

* Are we disagreeing about **D** (what the fact is, or which aspect matters)?
* about **M/B** (causal story, base rates, reliability, incentives)?
* about **S** (what level/type of support counts)?
* about **Q** (what we’re even trying to decide)?

Its this level of metaevidential reasoning that media operates. 

### How this Relates to the Case

What revived this line of questioning was the recent murder if Alex Pretti. I know people that, in the past, have viewed similar events as clear brutality and murder. However, after massive exposure to Fox News, and other life events, they see the Alex pretti case as a clear example of “terrorism” or whatever the current federal governments narrative is. 

People “seeing the same event” but slotting it into *brutality/murder* vs *terrorism*—is almost a textbook case of how **classification frames** and **trust networks** turn raw facts into “evidence for X.” Using the Alex Pretti case as the anchor: the dispute isn’t only “what happened,” it’s also “*what kind of thing was it?*” In public reporting, you can already see (1) contested factual claims about the encounter and (2) official/political labels being applied (e.g., “domestic terrorist,” “would-be assassin”), alongside calls for investigations. ([Axios][18]) Here are the main moving parts that produce the divergence:

A lot of disagreement happens *upstream* of “probability raising,” at the level of **what gets treated as the stable fact**. In this case, different information environments emphasize different “base facts”: official statements about the threat posed / firearm / resistance ([People.com][19]),  video interpretations (what was in his hands, what happened right before shots, etc.) , and internal/preliminary review claims that contradict an initial narrative ([opb][20]). If someone comes to treat *the government’s characterization* as the primary datum (and contrary footage as deceptive/edited/out-of-context), then the evidential pipeline flips even if the “surface facts” sound similar. 

Labels like “terrorism” aren’t just descriptions; they bundle an entire causal-moral package: who is presumed the aggressor, what level of force is presumed justified, and whether the event is treated as a one-off tragedy or part of a larger coordinated threat. So the same observed elements (“there was a gun nearby,” “there was a protest,” “agents shot him”) can be *reinterpreted* once the category is chosen. And crucially: in public discourse, category selection is often driven by **authority cues** and **coalitional cues** (who said it, which side says it), not just by a neutral review of details. You can see high-profile figures amplifying “assassin/terrorist” framings even amid disputed accounts. ([New York Post][21])

When you watch two people argue, it can look like “same facts, different inference,” but it might be one of these:

1. Factual-model dispute (potentially evidence-responsive) - This kind of disagreement *can* update with better evidence—body-cam releases, independent investigations, corroborated timelines. There are ongoing investigations reported (civil rights / DHS / DOJ), which is exactly the kind of thing that—if trusted—should move beliefs. They genuinely disagree about:

  * what happened (e.g., whether he was armed at the moment he was shot)
  * source reliability (video vs DHS vs witnesses vs internal review)
  * causal story (threat escalation, sequence of actions)

2. Norm/identity dispute (only loosely evidence-responsive) - Here, extra facts often don’t resolve it, because the disagreement is about **standards** and **trust**, not data. They may share many “facts” but disagree about:

  * what “counts” as terrorism (concept boundaries drift)
  * what level of threat “justifies” lethal force (norms)
  * whose institutions are trusted (epistemic allegiance)

Long media exposure can genuinely change “what counts as evidence”. Even without bad faith, people can undergo something like lens training:

* **Salience training:** repeated examples make certain interpretations feel “obvious” (availability effects).
* **Suspicion inversion:** the person learns to treat contrary sources as inherently manipulative; disconfirming facts become evidence of “cover-up.”
* **Concept drift:** “terrorist” expands from “politically motivated violence against civilians” to “anyone opposing state enforcement with perceived threat potential.”
* **Default causal script:** “protester + gun” becomes an automatic “attack on law enforcement” script.

Once those updates occur, the same E will be routed differently: not because they “ignored evidence,” but because they changed the *epistemic wiring* that tells them what evidence even is. If you want to locate where the divergence is, try asking (even just in your own head) four questions:

1. **What are you treating as the fixed facts?** (video? official statements? medical examiner classification? witness reports?) ([People.com][19])
2. **Which sources are allowed to count, and which are disqualified in advance?** (this is often the biggest divider)
3. **What category is being applied (terrorism / murder / tragedy / justified force), and what does that category imply?**
4. **What would change your mind?**
   * If the answer is “nothing,” it’s mostly identity/team.
   * If the answer names concrete potential releases/findings, it’s at least partially evidence-governed.

In later sections, we will discuss how media can effectively change these epistemic norms and frames.

### Facts of the Situation

Multiple major outlets describe video/forensic analyses show two incontrovertible facts: **(1) he’s disarmed**, and then **(2) agents fire ~10 rounds into him**. Reuters reported verified video footage, showing him holding a cellphone, being wrestled/disarmed, and then shot, and ABC reports a forensic audio analysis finding **10 shots in under ~5 seconds**. ([Reuters][22]) People also summarizes footage (citing other reporting) as showing him unarmed/holding a phone while pinned. ([People.com][23]) So given *those* facts, the interesting question becomes: **how can someone still come away with “terrorism” (or “justified”) rather than “brutality/murder”?** Here are the main mechanisms that produce that divergence—even when people aren’t consciously lying.

A “terrorism” lens can treat *the disarmed moment* as almost irrelevant, because it’s classifying the person/event as belonging to a threat category: “He was a terrorist *because he intended violence / was part of an attack / aligned with a cause*”. Then the shooting is interpreted as “neutralization,” “split-second,” “chaotic,” or “tragic but necessary.” So the evidential center moves from **what happened at second T** to a broader claim like **what kind of actor this was**. That’s why two people can agree “he was disarmed” and still disagree on the headline label.

Once someone’s information environment (say Fox News + social feeds) trains them to distrust certain sources, disconfirming facts stop functioning as evidence and become “propaganda,” “selective editing,” or “context missing.” At that point, *even identical footage* can be pre-labeled: “That video angle is misleading”, “We don’t see what happened right before”, “He could still reach for a weapon”, or “The government has intel we don’t”. In fact, these were some of the exact responses I encountered when confronting people with these two basic facts. This is less “probability raising” and more “which pipelines are allowed to produce facts.”

I focus on the **terminal slice** of the event: disarmed → shot many times → therefore brutality/murder. A security-state lens focuses on the **process slice**: “threat emergence → struggle → risk to agents → lethal force.” In that frame, once a gun is in play, later disarmament doesn’t erase the earlier threat narrative—it just becomes “the moment right before he was shot.” Reuters/People/others describe the official account emphasizing resistance/handgun, while other reviews describe evidence contradicting parts of that. The interpretive fight is often: *which slice gets to be “the fact” that controls the conclusion?* Unfortunately, this is often determined by who can control or influence the media. 

There is also moral inversion: “If he’s the enemy, then constraint violations become ‘necessary’”. This is how highly publicized events become like “team sports”, but it’s more specific than “identity politics.” It’s a moral-cognitive switch. If *they* are “terrorists,” then harsh force reads as protection. If *we* are “protectors,” then errors are excused as fog-of-war. Errors are okay in a situation where you are against a terrorist. Once that inversion happens, the same detail (“10 shots”) can be heard as either “execution” or “they had to make sure he was down.”

In polarized contexts, endorsements by officials (e.g., Department of Homeland Security statements) or party-aligned figures can function as evidence *even when the underlying factual claims are contested*. And when later evidence contradicts initial narratives, some people update; others double down by treating the contradiction itself as proof of a conspiracy or hostile media. Reuters also reports DOJ/DHS civil-rights review activity around the incident, which becomes “evidence” differently depending on trust. ([Reuters][22])

Even if everyone agreed on the two facts, people can still diverge because they’re answering different implicit questions: “Was lethal force justified at the moment he was disarmed?” versus “Was he a member/example of a threatening category, and are agents broadly justified against that category?" Those are *not the same inferential target*, so “what counts as evidence” shifts. A good question to ask your interlocutor in discussions like these is: “What specific new information would make you stop calling it terrorism and start calling it unjustified killing?” If they can name concrete potential updates (body-cam release, timeline, independent reconstruction), they’re at least *somewhat* evidence-responsive. If the answer is “nothing,” it’s almost purely coalitional. The latter is unfortunately what characerizes most situations. Many people think its noble to firmly entrench yourself in an opinion regardless of counterevidence. They actually think its a virtue. 

### Bayesian Perspective

Bayesian updating is a rule for *conditionalizing once you already have a model*, but a lot of the real action is in **model formation**: deciding (i) what your hypothesis space is, (ii) what counts as the observation, and (iii) how the observation is generated. Bayes tells you how to update **inside** a model but it doesn’t necessarily tell you which model you should be in (anyone who studies statistics will yell at me for saying this; obviously there are model selection criterion but im taking the space of possible models to largely be a function of the meta-level filters that are a function of media). Deciding "what is evidence” is largely about **choosing/constructing the model**.

Bayes assumes E and H are already well-defined random variables. In the equation, (H) and (E) aren’t English sentences; they’re events/propositions in an algebra with specified meanings. To even write (P(E\mid H)), you’ve already done a ton of work: you have fixed a hypothesis space ({H_i}) (“what are the live possibilities?”), you have fixed an observation space ({E_j}) (“what are we treating as the data?”), and you have fixed a *likelihood model* (P(E\mid H)) (“how would the world produce this data under each hypothesis?”). Choosing (E) and (H) is outside the bare update rule.

Two people can update in opposite directions without “violating Bayes”. That can happen through several “external” degrees of freedom:

1. Different hypothesis spaces: If one person’s space is ({A, \lnot A}) and another’s is ({A, B, C}), the same observation can shift mass differently. Sometimes adding a new live alternative “explains away” what previously supported (A).
2. Different descriptions of E (coarse vs fine graining): One person uses (E) = “he was shot 10 times,” another uses (E') = “he was shot 10 times *after being disarmed*,” another uses (E'') = “a video shows X.” Those are different propositions; Bayes will happily treat them differently. This is basically: *what is the data point? the raw sensory stream, a testimony, a measurement outcome, or an interpreted claim?*
3. Different likelihoods (the real engine of disagreement): Even with the same H and E, if I think (P(E\mid H)) is high and you think it’s low, we’ll diverge. And those likelihood disagreements are often *about* the upstream “evidence” issues such as: reliability of sources, selection effects, incentives to distort, and what background conditions obtain. 

So what is Bayesianism good for here? It’s good for *locating* disagreement. When two people disagree about “what counts as evidence,” Bayesian framing helps you ask: Are we disagreeing about the **hypothesis space**? the **data proposition** (what E even is)? the **trust/measurement model** (how E was generated)? the **likelihoods** (diagnosticity)? or the **priors**? That turns “we see the same facts differently” into a checklist of specific moving parts.

### Bayes Applied to Alex Pretti

Applying the Bayesian “what counts as evidence is upstream of Bayes” point to the Alex Pretti case actually becomes very concrete, because we can *name* the hidden variables people are implicitly disagreeing about. Major reporting does support *something close* to what i've summarized, but with the normal caveat that investigations are ongoing:

* Reuters reports video it verified shows Alex Pretti holding a cellphone, being wrestled to the ground and disarmed, and then being shot moments later. ([Reuters][24])
* ABC reports a forensic audio analysis finding **10 shots in under five seconds**. ([ABC News][25])
* AP reports videos contradict initial DHS claims and show a firearm being removed while he appears to be holding only a phone. ([AP News][26])
* Reuters also reports an initial government review did **not** mention him “brandishing” a firearm (contrary to early official rhetoric). ([Reuters][27])
* Reuters fact-checks viral edited imagery that implied he was holding a gun in-hand. ([Reuters][28])

1. Set up a Bayesian toy model for the dispute

Let’s define competing hypotheses (these are simplified but map to the debate):

* **H₁ (Unjustified lethal force / wrongful killing):** lethal force was not justified at the moment shots were fired.
* **H₂ (Justified lethal force):** lethal force was justified (e.g., imminent threat, reasonable perception of threat).
* **H₃ (“Terrorism” framing):** Pretti was a “terrorist” / would-be attacker (a category/intent claim), and the shooting is treated as neutralization.

Now define evidence candidates:

* **Eᵥ:** Verified bystander video shows him holding a phone, pinned/disarmed, then shot. ([Reuters][24])
* **E₁₀:** 10 shots fired in <5 seconds (forensic audio analysis). ([ABC News][25])
* **Eₒ:** Official/DHS initial narrative emphasizing firearm/threat (even when later evidence disputes details). ([AP News][26])

Bayes update inside a model is:
[
\text{Posterior odds} \propto \text{Prior odds} \times \frac{P(E \mid H_i)}{P(E \mid H_j)}
]

The whole fight is: **what is E**, and **what are the likelihoods** (P(E\mid H)).

2. The “what counts as evidence” problem becomes explicit as latent variables

People are not updating on “what happened.” They’re often updating on:

  * a) trust variable: which channel produces “real E”? Let **T** be “Reuters/AP/ABC video verification is reliable” vs “mainstream outlets manipulate / omit context.”

    * If (T=\text{high}), then Eᵥ is high-quality evidence.
    * If (T=\text{low}), then Eᵥ is *not* treated as E at all — it becomes “propaganda,” and may even be used as evidence of conspiracy.

This is why two people can hear the same sentence (“video shows he was holding a phone”) and treat it oppositely. Reuters even had to fact-check a viral altered image implying a gun-in-hand — that kind of info warfare feeds distrust and changes T. ([Reuters][28])

  * b) A “frame” variable: what question are we answering? Let **F** be the frame:

    * (F=) **use-of-force frame**: “Was lethal force justified at the moment of shooting?”
    * (F=) **threat-category frame**: “Was he the kind of person/event that counts as terrorism?”

Under the threat-category frame, the *moment* of being disarmed can be demoted in relevance. The model shifts from “imminent threat now” to “intent / affiliation / category,” which is not the same hypothesis. Bayes can’t tell you which F to adopt; it can only update once you’ve adopted it. If you want to describe the divergence precisely in Bayesian terms, people aren’t disagreeing mainly about Bayes’ rule. They’re disagreeing about the *inputs*:

1. **Hypothesis space** (is “terrorist” a live hypothesis? is “state murder” a live hypothesis?)
2. **Evidence variable** (is the bystander video a legitimate observation? is the official narrative the observation?)
3. **Likelihood model** (how often does “disarmed + 10 shots” happen under justified force vs unjustified force?)
4. **Trust and framing latent variables** (T and F)

That’s why the same public event can produce opposite posterior movements even among “Bayes-respecting” reasoners. A sharp way to test whether someone is updating on evidence or allegiance is to ask them to specify **an observation that would have high likelihood under the rival hypothesis**. For example, if someone is in the “terrorism / justified” camp, ask: “If independent body-cam angles show he was pinned and his firearm was already in an agent’s hand *before* the first shot, what does that do to your confidence in ‘justified’?” (AP/Reuters reporting suggests the video is already close to this.) ([AP News][26]) If they can articulate a counterfactual that would move them, they’re at least modeling evidence. If they can’t, then their “Bayes” is effectively frozen because priors/trust/frame dominate.

### This is not just "disagreement"

What the Alex Pretti case “shows” at a deeper level isn’t just disagreement over an incident; it’s the way **media ecosystems can rewire the inputs to reasoning**—your categories, priors, likelihoods, and even what counts as a datum worth updating on. You can see the basic ingredients in the public record:

* There’s contested narration early on from officials, and then a lot of public attention to bystander video and reconstructions. Reuters reports verified video showing Pretti holding a cellphone, being wrestled/disarmed, then shot; Reuters also reports a preliminary CBP review that didn’t include the “brandishing” claim that circulated in the first hours. ([Reuters][30])
* There was also an explicit “information war” artifact: Reuters fact-checked a viral edited still that nudged viewers toward “he had something (a gun) in his hand,” illustrating how small manipulations can steer interpretation. ([Reuters][31])
* Independent / transparent investigation demands became part of the story itself, with former DOJ lawyers calling for transparency and polling showing broad support for independent investigation. ([Axios][32])

Media ecosystems don’t just *add evidence*; they set the “epistemic parameters”. Bayes assumes you already have a hypothesis space (H), an observation (E), priors (P(H)), and likelihoods (P(E\mid H)). A polarized media ecosystem pressures **all four**—especially the parts Bayes treats as “given.”

Calling something “terrorism,” “rioting,” “self-defense,” “execution,” etc. isn’t a conclusion at the end of reasoning—it’s often a **front-loaded categorization** that changes what hypotheses feel live. Once “terrorist” becomes a salient category, the implicit hypothesis set shifts from “justified vs unjustified force at the moment" to “neutralizing an enemy actor vs being soft on enemies” …and a ton of downstream reasoning is now happening inside that different space. You can watch this happen socially: high-profile political statements become “evidence tokens” for the category claim, even when later reporting complicates the initial narrative. ([Axios][32])

A key hidden variable is: **which institutions you treat as truth-generators**. If a person’s ecosystem trains them that “mainstream verification” is suspect, then Reuters/AP/ABC-style claims about video or reconstructions don’t function as (E); they function as anti-evidence (“they’re covering for the other side”). Reuters’ fact-check about edited imagery is a good micro-example of how the ecosystem can inject ambiguity and then monetize the ambiguity. ([Reuters][31])

The likelihood (P(E\mid H)) is basically “how expected is this observation if that story about the world is true?” Media ecosystems sell *stories* (causal scripts): “lawless chaos / threats to order”, “state overreach / impunity”, “deep state / coverups” and “violent radicals everywhere”. Those scripts change the likelihoods people implicitly assign. For instance, if you’ve been trained into a “constant threat” script, then “multiple shots quickly” can be felt as *expected* under “reasonable officer response,” inflating (P(E\mid H_{\text{justified}})) and shrinking the Bayes factor.

Profit + algorithms push toward frames that are *high engagement*, not high accuracy. Two mechanisms matter a lot. First, Engagement incentives favor high-arousal frames. Platforms and audience-driven media reward content that triggers outrage, fear, and certainty—because it keeps people watching/sharing. That doesn’t merely misinform; it **selects for frames that are resistant to disconfirmation** (e.g., conspiracy-friendly frames where counterevidence proves the conspiracy). Research/policy summaries on polarization and platform incentives describe how algorithmic distribution and self-selection can create homogeneous clusters and accelerate misinformation diffusion. ([citap.unc.edu][33]) Second, Participatory disinformation turns users into co-producers. “Participatory disinformation” is exactly what it sounds like: people aren’t just consuming a narrative; they’re *helping make it*. The Reuters edited-still episode is an example of how small “crowd-sourced interpretation hacks” can be amplified until they feel like common knowledge. ([Reuters][31]) That co-production creates identity investment: backing down isn’t just updating a belief; it’s abandoning a team contribution.

Institutional rot isn’t only “bad actors”; it’s broken feedback loops.  **Information correction** gets weaker when local institutions can’t credibly investigate or communicate, or when federal/local conflict makes transparency harder (raised in reporting about investigative friction and calls for independent probes). ([Axios][32]) **Accountability capacity** can be affected by staffing/mandate changes and selective enforcement patterns—Reuters has reporting more broadly about scaled-back civil-rights enforcement capacity and how that interacts with cases like Pretti’s. ([Reuters][34]) In Bayesian language: the system’s ability to generate high-quality (E) deteriorates, and then people rationally (or semi-rationally) fall back on identity/trust proxies. These are feedback loops inherent to the system. 

The Pretti episode is a case study in how modern information systems shift people from updating on *shared public evidence* to updating on *identity-indexed narratives*, because the ecosystem manipulates (i) what counts as an observation, (ii) who is trusted to certify observations, and (iii) which frames are emotionally and socially rewarded.


# The Ecosystem

Causal scripts diffuse through social networks via platform incentives, influencers, and algorithmic boosting etc. Public discourse becomes degraded as a consequence, leading to deep disagreement and policy impasse etc. Causal scripts produce patterned like responses and arguments, so much so that it's almost predictable what a person will say; and what they say is normally a variation of the common responses that have become acceptable discourse, as dictated by these platform media norms. "Arguments" are not really arguments, but thought terminating cliches used to signal identity. This is the “ecosystem-level” story: **causal scripts** (ready-made explanations + moral conclusions) spread through networks in ways that are *structurally favored* by platform incentives, and the result is **degraded discourse**: people talk past each other, disagreements become “deep” (about trust and identity), and policy gets stuck.

Causal scripts usually do not become dominant all at once. They tend to spread in stages, moving from a niche interpretation to a default lens for understanding events, and the first push often comes from the way platforms are designed. On major social platforms, ranking systems heavily reward engagement signals like replies, reshares, and watch time, and research consistently shows that this tends to amplify emotionally charged and divisive content because outrage and conflict generate exactly those kinds of reactions ([Knight First Amendment Institute][36]). In practice, that gives certain narratives a built-in advantage: scripts that make people angry, afraid, or morally certain travel farther and faster than ones that ask for patience or nuance.

Influencers play a major role in this process, not just by offering opinions, but by acting as what you might call “script entrepreneurs.” What they often produce is not a one-off take, but a reusable narrative template: a cast of heroes, villains, and victims; a causal mechanism that explains what is “really” happening; a moral frame that tells people what they should feel; and an action cue that tells them what to do next, whether that is sharing, boycotting, voting, or punishing. The strength of this packaging is that it is optimized for speed. It is short, vivid, and easy to repeat, which makes it highly portable across audiences. In that sense, it works like plug-and-play cognition: once people learn the template, they can apply it to the next event almost automatically.

Once one of these templates starts gaining traction inside a particular community, algorithmic boosting and network structure can turn it into a cascade. Social networks are shaped by homophily, so people are often surrounded by others who already share similar views, and that makes reinforcement easy. Likes and retweets function as social rewards, repeated posts across multiple accounts create the appearance of consensus, and remixable formats like clips, stitches, and quote-tweets help the script spread while preserving its core message. Formal social network models show how misinformation and fake news interact with these network dynamics to increase polarization and lock in false beliefs over time ([ScienceDirect][37]).

What makes this especially durable is that the process is not only top-down. Audiences become active participants in producing and maintaining the script. Communities collaboratively “work” the narrative by extracting short clips, creating captions and memes, collecting “receipts,” inventing rebuttal fragments, and building a shared vocabulary around the story. Research on participatory disinformation directly describes how these collaborative dynamics help shape disinformation narratives and sustain them long after the original post or claim appeared ([ACM Digital Library][38]). By that point, the script is no longer just a message people encountered; it becomes a communal object that they helped build. People are no longer merely persuaded by it—they are invested in it.

What makes this even more powerful is that the process is no longer purely top-down. Audiences don’t just consume the script; they help produce it. Communities collectively refine the narrative by cutting clips, making memes, writing captions, gathering “receipts,” and inventing shared phrases or rebuttals. Over time, the script becomes a communal object—something people have contributed to, defended, and circulated together. At that point, they’re not simply persuaded by it; they’re socially and emotionally invested in keeping it alive.

This is where the deeper damage shows up: public discourse starts to break down because the epistemic commons—the shared space where people can at least agree on what reality looks like—begins to collapse. Once these scripts take over, disagreement is no longer just about interpreting the same evidence differently. It becomes a fight over what even counts as evidence in the first place: whether a video is trustworthy, whether officials can be believed, whether independent reporting is actually independent, and even what category an event belongs in—terrorism, brutality, self-defense, false flag, and so on. Those judgments happen upstream of reasoning itself. They shape the priors people start with, what explanations they consider possible, and how they process any new information that comes in.

As that happens, people also begin updating less on signals from the world and more on signals from their social group. In other words, the “evidence” stops being the event itself and starts being who is saying what about it. Coalition cues become more important than direct observation. So the exact same piece of new information can be interpreted in completely opposite ways: for one group, it confirms wrongdoing; for another, it confirms media manipulation, depending on which meta-frame is already dominant.

Over time, this feeds affective polarization—the emotional side of polarization, where the issue is not just disagreement but growing dislike and distrust of the other side. There is a growing body of empirical work suggesting that algorithmic exposure can intensify this kind of affective polarization, shaping not just what people believe, but how they feel about political opponents ([arXiv][39]). And once that emotional hostility rises, argument starts to feel less like a search for truth and more like moral combat. Persuasion becomes harder, because changing your mind can feel like siding with the enemy. Compromise begins to look like betrayal. That is how discourse degrades from debate into deadlock, and why policy impasse becomes not just common, but structurally baked in.

Once a script is installed, people’s responses start to feel surprisingly predictable—not because they are incapable of thinking, but because they are drawing from a small, familiar library of memetic modules. You can often hear the same moves repeated in different combinations: a labeling move that assigns a role instantly (“terrorist,” “thug,” “crisis actor,” “deep state,” “woke,” “bootlicker”); a delegitimization move that discredits the source (“fake news,” “out of context,” “do your own research”); a whatabout move that redirects attention (“what about when *they* did X?”); a motive move that reframes the other person’s concern as bad faith (“you only care because…”); and a closure move that shuts down further discussion (“case closed,” “obvious”). What looks like spontaneous argument is often a rapid assembly of these preloaded pieces.

The important point is that this is not just a personal failing or a character flaw. It is a structural feature of highly compressed discourse—communication shaped by platforms that reward speed, certainty, and virality over reflection. In that environment, the most successful responses are not the most careful ones, but the ones that are easiest to recognize, repeat, and deploy under pressure. That is why arguments online can start to feel less like open inquiry and more like scripted reflexes. There is even computational research identifying recurring rhetorical patterns in divisive online speech, including slogans, thought-terminating clichés, and repetition, which helps explain why these exchanges often sound formulaic even when they feel emotionally intense ([Nature][40]).

You can frame this as the difference between two very different kinds of speech: arguments that are trying to track the truth, and phrases that are really tracking social identity. In the ideal sense, arguments are supposed to be truth-seeking. They make their premises visible, invite counterevidence, and leave open the possibility that new information could change the conclusion. A real argument, even a passionate one, still gives you some sense of what would make the speaker revise their view.

Thought-terminating clichés do something else entirely. They are less about inquiry and more about social coordination. Instead of opening a claim up to testing, they close the discussion down with phrases like “obvious” or “nothing to see here.” Instead of explaining a mechanism, they substitute a label. Instead of engaging with evidence, they signal coalition membership—basically, “I know the code, and I belong to the group that uses it.” In that way, they also protect the script from falsification, because they preemptively mark certain kinds of evidence as invalid before they are even considered.

If you want to put it in Bayesian terms, these phrases often act like likelihood-nullifiers: they make it so that no possible evidence (E) will count against a favored hypothesis (H), because the channel that produced (E) has already been declared illegitimate. Once that move is in place, the conversation may still look like an argument on the surface, but functionally it has stopped being one. A tight “mechanism → consequence” pattern you can use to identify the phenomena:

1. Engagement-based ranking disproportionately rewards high-arousal, conflictual content. ([Knight First Amendment Institute][36])
2. Influencers and communities package repeatable causal scripts that fit those incentives. ([ACM Digital Library][38])
3. Algorithmic diffusion + homophilous networks turns scripts into default lenses. ([ScienceDirect][37])
4. Scripts compress discourse into predictable, memetic “argument forms,” including slogans and thought-terminating clichés. ([Nature][40])
5. The epistemic commons erodes, deep disagreement rises (trust, categories, standards), and policy becomes harder because compromise is re-coded as identity betrayal. ([OUP Academic][41])


### Self Sealing Discourse and Echo Chambers

Once a community internalizes certain causal scripts, it doesn’t just “have opinions.” It acquires a **self-sealing epistemic immune system**—a set of habits, categories, and stock moves that prevent outside information from functioning as evidence. Two pieces of theory are perfect for this:

* **C. Thi Nguyen** on *epistemic bubbles vs echo chambers* (and why echo chambers are hard to “pop”) ([Cambridge University Press & Assessment][42])
* **Endre Begby** on *evidential preemption* (how testimony can inoculate audiences against later counterevidence) ([PhilPapers][43])

Phrases like “you should comply with the law” and “Alex Pretti is protecting pedophiles and murderers” directly connect to “enemy from within” rhetoric and institutional/policy breakdown. Below I’ll build the self-sealing pattern step-by-step, then show how these sorts of phrases contribute to the breakdown. 

1. The diffusion engine: why scripts spread fast and stick

  What platforms reward, more than anything, is what you might call high-velocity cognition: fast, compressed ways of interpreting events that are easy to feel and even easier to share. A causal script works perfectly in that environment because it bundles several things at once—a simplified explanation of what happened, a moral verdict about who is guilty, and an action cue telling people what to do next. In attention markets, the scripts that win are usually the ones that are emotionally high-arousal (anger, fear, disgust), identity-confirming (clear signals about “us” versus “them”), short and memetic enough to repeat, and conflict-maximizing enough to trigger replies, quote-posts, duets, and stitches. You can see this in amplification dynamics themselves: engagement-based ranking systems can end up disproportionately boosting divisive content precisely because it produces the strongest engagement signals ([Aeon][44]).

  Influencers are central to this because they do more than pass along beliefs—they package templates. A strong influencer script usually includes a cast list (heroes and villains), a causal story (“what’s really happening”), a normative verdict (who deserves what), an epistemic rule (who should be trusted and who should be dismissed), and a participation cue (“share this,” “wake up,” “they’re lying to you”). That final piece is especially important, because it shifts the audience from passive consumers into active participants. People are no longer just reacting to a message; they are being recruited into helping reproduce it.

  Once that participation is rewarded with likes, status, and in-group approval—especially when people get social points for “ratioing” outsiders or defending the group line—disinformation and narrative warfare become collaborative projects. The community starts building a shared repertoire: catchphrases, screenshots, “debunk” fragments, attack lines, lists of enemy outlets, and ready-made responses. Over time, that repertoire becomes the social toolkit people reach for automatically, which is exactly why later responses can feel so predictable. They are not being generated from scratch each time; they are being assembled from a common script the group has already built together.

2. Nguyen’s distinction: bubbles are omission; echo chambers are *discrediting*

  Nguyen’s key distinction is really useful here because it separates two things that often get lumped together. In an epistemic bubble, important voices are missing mostly by omission—you simply do not encounter them, so your view of the world is incomplete ([Cambridge University Press & Assessment][42]). In an echo chamber, though, the dynamic is much stronger: outside voices are not just absent, they are actively excluded and discredited, and members are trained in advance to distrust anything those outsiders say ([Cambridge University Press & Assessment][42]).

  That difference matters because it changes what “more information” can actually do. A bubble can sometimes be burst by exposure—if someone finally sees the missing evidence or perspective, it may genuinely shift their view. But echo chambers are more self-sealing. They often convert exposure into a reinforcement event, because the outside source has already been pre-labeled as corrupt, biased, or deceptive. So when contradictory evidence appears, it does not function as a challenge; it functions as proof that the chamber’s warning about outsiders was right.

  That is why the phenomenon feels so durable. It is not just a filter bubble problem, where people are missing information. It is more specifically echo-chamber logic, where the system is built to neutralize outside information before it can do any epistemic work.


3. Begby’s evidential preemption: inoculation against future counterevidence

  Begby’s mechanism helps explain exactly how these narratives become self-sealing, because the persuasion is not just about getting someone to believe a claim in the moment. It is about shaping how they will interpret future evidence. His idea of *evidential preemption* is, roughly, that a speaker asserts a claim (p) while also warning the audience that they will later encounter apparent evidence against (p)—but that this future evidence should be treated as misleading, deceptive, or already accounted for ([PhilPapers][43]). In other words, the message arrives with its own built-in defense system.

  You can see the structure everywhere in politics and media: “They’re going to tell you X, but that’s propaganda,” or “that clip is out of context,” or “it’s a hoax,” or “those are paid actors.” The power of this move is that it does not just persuade you now; it pre-programs your response later. When counterevidence eventually appears, it no longer lands as counterevidence. It lands as confirmation that the warning was correct. Begby explicitly describes this as a kind of inoculation—an audience is primed in advance to resist future contrary evidence ([endrebegby.synthasite.com][45]).

  When you combine that with Nguyen’s distinction, the full loop becomes clear. In an echo chamber, outsiders are already discredited, so their testimony is treated as suspect before it is even heard ([Cambridge University Press & Assessment][42]). Then evidential preemption adds a second layer: any future contradiction is pre-labeled as manipulation, which means it never gets to function as evidence in the first place ([PhilPapers][43]). That is the core of the self-sealing dynamic you are describing: not just disagreement, but a structure that protects itself by training people how to dismiss disconfirming evidence before it arrives.

4. The self-sealing discourse pattern, step by step

  Here is a fuller way to describe the anatomy of how these discourse ecosystems become closed under revision. It usually starts with a script installing a frame—basically, a preloaded answer to what kind of event this is. The frame determines which categories feel relevant from the beginning: law and order, terrorism, corruption, degeneracy, threat, protection, betrayal. Once that frame is in place, it does more than shape interpretation. It selects what data seem salient, which details get ignored, and even which hypotheses feel plausible enough to consider. Before people are debating facts, they are already operating inside a pre-structured sense of what sort of story they are in.

  The next step is that the script installs an epistemic authority map: a social ranking of who counts as a reliable knower and who does not. This is where the difference between an epistemic bubble and an echo chamber really matters. In a bubble, people may simply not encounter relevant outside voices. In an echo chamber, those voices are actively framed as untrustworthy by nature, so their testimony is discounted in advance ([Cambridge University Press & Assessment][42]). That means the issue is no longer just missing information—it is a prior commitment about which sources are allowed to count as information at all.

  From there, the script installs preemption moves for dealing with counterevidence before it even appears. This is where Begby’s idea of evidential preemption fits perfectly: instead of waiting to see what critics will say, the audience is preloaded with a deflationary story that explains away future contradictions ([PhilPapers][43]). The patterns are familiar: source deflation (“fake news,” “state media,” “bought”), context deflation (“out of context,” “edited clip”), motive deflation (“they want chaos,” “they protect criminals”), and process deflation (“the investigation is rigged”). The point is not merely to argue against specific evidence, but to lower the evidential status of entire channels in advance.

  Once those pieces are in place, conversation starts to become ritualized. Because the script offers a limited repertoire of acceptable moves, responses begin to follow a recognizable sequence: label, delegitimize, moralize, close inquiry, then pivot to coalition action. That is why so many exchanges feel strangely predictable, as if you can forecast the next few lines before they are spoken. The discussion still looks like argument on the surface, but underneath it is often a scripted performance constrained by the group’s repertoire.

  At the final stage, self-sealing emerges. When counterevidence arrives, it is typically filtered out, distrusted because it comes from an outsider, reinterpreted to fit the corruption or conspiracy frame, or treated as socially risky to engage with seriously because doing so invites sanctions from the group. At that point, argument is no longer doing much epistemic work. It is no longer primarily about testing claims against the world. It is performing membership—showing that you know the script, trust the right people, and reject the right enemies.

  Phrases like “you should comply with the law” sound, on the surface, like neutral moral guidance, but inside a self-sealing discourse ecosystem they often do much more than state a norm. They can lock the frame of the conversation by shifting the question away from what actually happened or whether a response was justified, and toward a simpler obedience-versus-deviance narrative. They also invert agency: if harm occurred, responsibility gets redirected onto the person who was targeted, because the key fact is now framed as noncompliance. And once “compliance” becomes the central lens, inquiry itself can be shut down. Further investigation into context, proportionality, or causation is treated as irrelevant—“doesn’t matter, they should have complied.” In that sense, the phrase functions like a thought-terminating cliché: it compresses a complex factual and moral assessment into a single move that ends the need to examine particulars.

  The phrase “he is protecting pedophiles and murderers” works differently, but just as powerfully. It combines enemy construction with evidential preemption. Instead of treating disagreement as an error, it recasts disagreement as moral contamination: if you question the script, you are not merely mistaken, you are complicit. It also expands the scope of the conflict. What might have started as a specific factual or legal question gets transformed into a civilizational struggle against absolute evil, which makes nuance feel not just unnecessary but dangerous. And once that framing is installed, any attempt to insist on due process, proportionality, or evidential standards can be redescribed as “protection” of the enemy class.

  This is especially effective in echo-chamber environments because it creates asymmetric social costs. Calling for caution, verification, or procedural fairness becomes risky, because it can be interpreted as disloyalty or hidden sympathy for the condemned group. That is how epistemic norms get overridden: not necessarily because people stop caring about truth in the abstract, but because identity safety and coalition signaling become more immediately important than evidential discipline.

5. “Enemy from within” rhetoric as a stabilizer of echo chambers

  Once outsiders are classified as enemies, keeping an echo chamber closed becomes much easier, because the closure is no longer just informational—it becomes moral and social. Nguyen’s point about echo chambers is that they do not merely omit outside voices; they actively train members to distrust them, and “enemy” rhetoric supercharges that process by turning distrust into a virtue while making trust feel like betrayal ([Cambridge University Press & Assessment][42]). In that environment, skepticism is no longer a selective intellectual habit; it becomes a loyalty test.

  At the same time, counterevidence stops functioning as evidence and starts functioning as a hostile act. This is where Begby-style preemption fits perfectly: if people are told in advance that “they will show you X to trick you,” then any future contradiction is received not as information but as an attack vector ([PhilPapers][43]). The audience is not just prepared to reject the content; they are prepared to experience it as manipulation. That changes the emotional valence of inquiry itself, because engagement with outside evidence begins to feel dangerous rather than clarifying.

  And once the out-group is coded as the enemy, changing your mind becomes much more costly. Updating your beliefs is no longer framed as learning or correcting an error; it is framed as defection, as switching sides. That raises both the psychological and social price of revision, because what is at stake is not just whether a claim is true, but whether you still belong. This is the point where discourse becomes truly self-sealing: it closes not only at the level of cognition, but at the level of identity and social membership.

6. From degraded discourse to deep disagreement and policy impasse

  Once many groups are operating with different scripts, the shared epistemic commons that policy depends on starts to disappear. The disagreement is no longer just about conclusions; it is about the machinery of justification itself. People begin to differ on what counts as evidence, who counts as a credible witness, which institutions are legitimate fact-certifiers, and what norms should govern dispute resolution in the first place—courts, elections, journalism, expertise, or something else. So even when everyone says “show me evidence,” they are often talking about entirely different pipelines for producing and validating truth. On the surface, it sounds like a common demand. Underneath, the standards are no longer shared.

  That is why policy compromise becomes so hard. Once the script moralizes the conflict, compromise itself gets recoded as corruption or surrender. If the other side is framed as “protecting pedophiles and murderers,” then negotiation starts to look immoral. If your own side is framed as the last defense against chaos, then restraint looks like weakness and procedural caution looks like betrayal. Under those conditions, deliberation loses legitimacy, because the issue is no longer treated as a dispute among citizens but as a battle between good and evil.

  The result is a system structurally pulled toward stalemate or escalation. Stalemate happens when no shared standards remain for resolving disputes. Escalation happens when each side sees the breakdown of compromise as proof that stronger tactics are justified. Either way, the conditions for ordinary democratic problem-solving deteriorate, because the very tools that make compromise possible—shared evidence, trusted procedures, and mutual legitimacy—have been hollowed out.

  A useful diagnostic is to ask a very simple question: what, exactly, would change this person’s mind? In a real argument, people can usually answer that. They can name the kind of evidence, event, or counterexample that would make them revise their view, even if they still strongly disagree in the moment. That openness is part of what makes the exchange truth-tracking rather than purely performative. In self-sealing discourse, though, that question tends to trigger more script instead of a real condition for revision. The answer is not a testable threshold; it is a closure move: “nothing, because they lie,” “it’s all rigged,” “you’re with the enemy.” At that point, the response is no longer about evidence at all. It is a way of defending the frame, the authority map, and the group boundary in one stroke. That is basically evidential preemption operating at the level of the whole community. The group has already installed a system in which potential disconfirming evidence is neutralized before it arrives, so “what would change my mind?” no longer functions as an epistemic question. It becomes a loyalty check.

  Platform incentive structures amplify high-arousal, identity-confirming causal scripts. Those scripts don’t merely spread beliefs; they reshape epistemic norms by (i) discrediting outsiders (echo-chamber structure) and (ii) inoculating members against counterevidence (evidential preemption). The result is self-sealing discourse: predictable “arguments” that function as identity signals and thought-terminating clichés, degrading the epistemic commons and producing deep disagreement and policy impasse.


[18]: https://www.axios.com/2026/02/04/trump-alex-pretti-shooting-americans-investigation? "Most Americans concerned over Trump admin's handling of Alex Pretti shooting"
[19]: https://people.com/alex-pretti-s-cause-of-death-revealed-as-medical-examiner-rules-death-homicide-11898096? "Alex Pretti's Cause of Death Revealed as Medical Examiner Rules Death a Homicide"
[20]: https://www.opb.org/article/2026/01/29/internal-review-contradicts-white-house-narrative-of-prettis-death/? "Internal review contradicts White House narrative of Pretti's ..."
[21]: https://nypost.com/2026/02/04/us-news/jd-vance-wont-apologize-for-alex-pretti-minneapolis-shooting-calling-icu-nurse-would-be-assassin/? "JD Vance won't apologize for spreading claim Alex Pretti was would-be 'assassin'"
[22]: https://www.reuters.com/legal/government/us-justice-dept-opens-civil-rights-probe-into-alex-pretti-shooting-official-says-2026-01-30/? "US Justice Dept opens civil rights probe into Alex Pretti shooting, official says"
[23]: https://people.com/alex-pretti-s-cause-of-death-revealed-as-medical-examiner-rules-death-homicide-11898096? "Alex Pretti's Cause of Death Revealed as Medical Examiner Rules Death a Homicide"
[24]: https://www.reuters.com/legal/government/us-justice-dept-opens-civil-rights-probe-into-alex-pretti-shooting-official-says-2026-01-30/? "US Justice Dept opens civil rights probe into Alex Pretti shooting, official says"
[25]: https://abcnews.go.com/Politics/minute-minute-timeline-fatal-shooting-alex-pretti-federal/story?id=129547199& "A minute-by-minute timeline of the fatal shooting of Alex Pretti ..."
[26]: https://apnews.com/article/65a963816603a08bbc9db83961dd173f? "The Justice Department has opened a federal civil rights probe into the killing of Alex Pretti"
[27]: https://www.reuters.com/legal/government/us-review-alex-pretti-killing-does-not-mention-him-brandishing-firearm-2026-01-28/? "US review of Alex Pretti killing does not mention him ..."
[28]: https://www.reuters.com/fact-check/verified-footage-showing-alex-prettis-death-edited-alter-object-hand-2026-01-27/? "Verified footage showing Alex Pretti's death edited to alter ..."
[29]: https://nypost.com/2026/01/30/us-news/doj-civil-rights-division-is-investigating-alex-pretti-killing/? "DOJ Civil Rights Division is investigating Alex Pretti killing"
[30]: https://www.reuters.com/legal/government/us-justice-dept-opens-civil-rights-probe-into-alex-pretti-shooting-official-says-2026-01-30/? "US Justice Dept opens civil rights probe into Alex Pretti shooting, official says"
[31]: https://www.reuters.com/fact-check/verified-footage-showing-alex-prettis-death-edited-alter-object-hand-2026-01-27/? "Verified footage showing Alex Pretti's death edited to alter ..."
[32]: https://www.axios.com/2026/02/04/minnesota-killings-investigation-pretti-good? "Exclusive: 300+ ex-DOJ lawyers demand transparent Minnesota shooting probes"
[33]: https://citap.unc.edu/news/local-news-platforms-mis-disinformation/? "Addressing the decline of local news, rise of platforms, and ..."
[34]: https://www.reuters.com/world/justice-department-unit-police-misconduct-sees-staffing-plunge-probes-scaled-2026-02-05/? "Justice Department unit on police misconduct sees staffing plunge and probes scaled back, sources say"
[35]: https://www.reuters.com/legal/government/us-review-alex-pretti-killing-does-not-mention-him-brandishing-firearm-2026-01-28/? "US review of Alex Pretti killing does not mention him ..."
[36]: https://knightcolumbia.org/content/engagement-user-satisfaction-and-the-amplification-of-divisive-content-on-social-media? "Engagement, User Satisfaction, and the Amplification of ..."
[37]: https://www.sciencedirect.com/science/article/abs/pii/S0176268022000623? "Social media networks, fake news, and polarization"
[38]: https://dl.acm.org/doi/10.1145/3579616? "How Participatory Disinformation Shaped Deep Stories to ..."
[39]: https://arxiv.org/html/2411.14652v1? "Social Media Algorithms Can Shape Affective Polarization ..."
[40]: https://www.nature.com/articles/s41599-025-06277-7? "Drawing digital lines: pattern analysis of divisive rhetoric in ..."
[41]: https://academic.oup.com/anncom/article/45/3/188/7912664? "Role of (Social) Media in Political Polarization: A Systematic ..."
[42]: https://www.cambridge.org/core/journals/episteme/article/echo-chambers-and-epistemic-bubbles/5D4AC3A808C538E17C50A7C09EC706F0? "ECHO CHAMBERS AND EPISTEMIC BUBBLES"
[43]: https://philpapers.org/rec/BEGEP-2? "Evidential Preemption - Endre Begby"
[44]: https://aeon.co/essays/why-its-as-hard-to-escape-an-echo-chamber-as-it-is-to-flee-a-cult? "Why it's as hard to escape an echo chamber ..."
[45]: https://endrebegby.synthasite.com/resources/Evidential%20Preemption%2C%20web%20draft.pdf? "Evidential Preemption"
