## A Walton–Macagno Argumentation Framework for Interpretation

*A defeasible, goal-relative, dialectical method for settling meaning disputes across domains (law, scripture, philosophy, literature, data/model interpretation, institutional artifacts, and beyond).*

### Core commitments

Interpretation is best treated as a **defeasible claim about meaning**—a conclusion supported by **pro and con arguments** rather than a one-shot deduction. To interpret is to **associate an expression/element *E* in an artifact/document/object *D* with a meaning *M* in a context/use**, and then to defend that association under challenge.

Interpretive conclusions should be framed as **conceptual/terminological claims about “best interpretation”** relative to specified goals and standards—not as deontic “oughts.” The defeasibility of interpretive reasoning is made explicit through **critical questions** that expose defaults, assumptions, and points of vulnerability.

---

# 0) Trigger condition: when interpretation is needed

**Interpretation-in-the-strict-sense is appropriate when** there is a genuine doubt or conflict about what some element **E** in an artifact **D** *means/does/implies/applies-as*, such that **no unchallenged default meaning** settles the issue.

This corresponds to the transition from **prima facie understanding** (a shared, conventional default) to **interpretation proper**, where the default can no longer be taken for granted and must be defended, refined, or replaced.

---

# 1) The target form of an interpretive conclusion

### Interpretive claim (meaning-attribution under evaluation)

**BestInt(E, D | Cxt, G, A) ≡ M**
“Relative to context **Cxt**, goal **G**, and audience/standards **A**, the best (or most justified) interpretation of element **E** in artifact **D** is meaning **M**.”

This captures interpretation as a **meaning-attribution claim** made to overcome doubt, evaluated by an explicit set of criteria and dialectical tests.

---

# 2) A two-level Walton-style scheme

Interpretive disputes often involve two intertwined questions:

1. **Which evaluative framework should govern the dispute?** (meta-level)
2. **Given that framework, which interpretation is best?** (object-level)

These are modeled as two linked schemes.

---

## Scheme I: Argument for adopting an interpretive framework (meta-criteria)

### Claim (C)

For this dispute about **E** in **D** (in context **Cxt**) with goal **G**, we should evaluate interpretations using framework **F**—a **set of criteria** plus **priority rules** and **burden/standard of proof**.

### Premises

1. **Goal premise:** The practical/theoretical goal **G** of this interpretive task is specified (e.g., faithful reconstruction, legal applicability, theological normativity, aesthetic understanding, moral critique, predictive adequacy, explanatory adequacy, institutional compliance, etc.).
2. **Object premise:** **D** is an artifact of type **T** in domain **Dom** (statute, scripture, poem, scientific model, dataset, contract, UI spec, algorithmic output…), with authority-status **A** (binding, canonical, exemplary, exploratory, aesthetic…).
3. **Practice/fit premise:** In domain **Dom**, for objects like **T** with authority-status **A**, framework **F** is (a) recognized as appropriate and/or (b) best fits **G** and the relevant constraints (institutional, epistemic, moral, practical).
4. **Feasibility premise:** **F** can actually be applied here (available evidence, competence, time, procedural constraints).
5. **Defeasibility premise:** No overriding reason blocks using **F** (e.g., **F** violates binding authority or explicit procedural rules; **F**’s triggering conditions aren’t met; **F** yields contradictions with controlling constraints).

### Conclusion

Therefore, **F** is the (provisional/default) evaluative framework for settling interpretations of **E** in **D** for goal **G**.

**Defeasibility note:** Framework choice is itself defeasible. In practice, frameworks function as defaults that can be overridden when superior reasons arise.

---

## Scheme II: Argument from a framework to a “best interpretation” (object level)

### Claim (C)

Interpretation **M** is the best/most justified interpretation of **E** in **D** (in **Cxt**) for goal **G**, under framework **F**.

### Premises

1. **Doubt premise:** There is a genuine interpretive doubt/conflict about **E** in **D** in **Cxt** for goal **G** (i.e., no unchallenged default resolves it).
2. **Framework premise:** Framework **F** is applicable here (by Scheme I).
3. **Support premise:** Under **F**, there are sufficient pro-arguments supporting **M** from admissible sources of support (textual/structural evidence; contextual facts; genre constraints; intent evidence; precedent/tradition; functional/purpose evidence; empirical fit; institutional fit; explanatory/predictive adequacy; etc.).
4. **Defeat-management premise:** Defeaters against **M**—both rebutting alternatives and undercutting attacks on the inference—are answered or neutralized under **F**.
5. **Comparative premise:** Competing interpretations **M₁…Mₙ** are (i) considered and (ii) either rejected or shown not better than **M** under **F**.

### Conclusion

Therefore, **M** is (provisionally) justified as the best interpretation of **E** in **D** for goal **G**, under **F**.

---

# 3) A generic Walton-style scheme for interpretive fit under a goal

The two-level view can be implemented as a single, domain-general scheme that explicitly parameterizes context, goals, and standards.

## Scheme: Argument from Interpretive Fit Under a Goal

### Target conclusion

**BestInt(E, D | Cxt, G, A) ≡ M**

### Ordinary premises (grounds)

1. **Interpretandum identification:** Element/expression **E** occurs in artifact/object **D**, and the interpretive question is well-posed (the “thing to be interpreted” is fixed).
2. **Context specification:** Relevant context **Cxt** is identified (local co-text, broader corpus, historical setting, institutional setting, genre/discourse type, task setting).
3. **Goal specification:** Interpretive goal **G** is specified (recover intended message, apply a norm, preserve doctrinal coherence, achieve aesthetic illumination, obtain explanatory/predictive adequacy, etc.).
4. **Candidate meaning:** A candidate meaning/reading **M** is proposed at the appropriate grain size (propositional content, directive, theme, function, rule, model-structure, etc.).
5. **Method/criterion-set selected:** An evaluative set of criteria/warrants **K** (or framework **F**) is selected as appropriate to **(D, Cxt, G, A)**.
6. **Fit/support claim:** Under **K/F**, interpreting “**E in D as M**” is supported (linguistic fit, contextual fit, coherence, explanatory/predictive power, institutional fit, empirical fit, etc.).

### Major (warrant) premise — defeasible conditional

7. **Interpretive warrant:** If (1)–(6) obtain and no defeating exception applies, then **BestInt(E, D | Cxt, G, A) ≡ M**.

### Assumptions (defaults unless challenged)

8. **Default-meaning presumption:** There is a reasonable prima facie/default reading available given community conventions, unless challenged.
9. **Competence/normalcy assumptions:** Interpreter competence; normal discourse conditions; artifact integrity; data quality; stable background practices, etc.

### Exceptions (potential undercutters)

10. **Defeater conditions:** Superior reasons support rejecting **K/F** here or preferring a rival meaning **M′** (technical context defeats ordinary meaning; irony/sarcasm; corruption/variant text; genre shift; redaction; measurement error; institutional constraints; etc.).

### Conclusion

11. Therefore, **BestInt(E, D | Cxt, G, A) ≡ M** (defeasibly).

### Standard attack types

* **Undermining:** attack a premise (e.g., the alleged context is wrong; the evidence is weak).
* **Rebuttal:** support an incompatible conclusion (a rival interpretation **M′**).
* **Undercutting:** attack the inferential link by showing an exception applies (e.g., the canon/criterion is inapplicable here).

---

# 4) A repeatable workflow: the interpretive act as a dialectical procedure

1. **Fix the interpretandum:** Specify what exactly is being interpreted (**E** and **D**) and what would count as an answer.
2. **State the goal (G):** Clarify what interpretive success means (reconstruction, application, critique, explanation, prediction, aesthetic illumination, etc.).
3. **Set the audience/standard (A):** Identify who must be persuaded and what proof standard applies (court, scholarly community, faith community, lab/peer review, product team, etc.).
4. **Establish a default:** Start from a presumptive reading when available (prima facie understanding).
5. **Generate alternatives:** Enumerate plausible candidates {**M₁…Mₙ**}.
6. **Select warrants/criteria (K) / framework (F):** Choose admissible interpretive warrants and any priority rules, burdens, and standards appropriate to **G** and **A**.
7. **Build pro/con arguments:** Instantiate argument schemes supporting and attacking each candidate; make inferential dependencies explicit.
8. **Apply critical questions:** Surface assumptions and test for exceptions; ensure objections are handled rather than bypassed.
9. **Resolve conflicts:** Weigh competing arguments according to the selected proof standard and any priority rules when schemes collide.
10. **Output a statused conclusion:** Report not only **M**, but its dialectical status (e.g., *defensible* vs *justified*) relative to the current argument graph and standards—and note any remaining live defeaters or unresolved ties.

---

# 5) What can “back” an interpretation: hidden commitments and fault lines

In Toulmin terms, **backing** underwrites the warrants inside **K/F**—the often-implicit commitments that make a criterion seem appropriate. In real disputes, these are frequently the deepest sources of disagreement.

## A) Ontology and authority of the artifact

* **What is D?** (law, scripture, literature, model output, dataset, institutional directive…)
* **What kind of authority does it have?** (binding/coercive, canonical/normative, exemplary, exploratory, aesthetic…)
* **Where does authority live?** (original author, final text, community practice, institutional body, empirical performance, tradition…)

## B) Semantics and pragmatics (how meaning works)

* Meaning as ordinary-language default vs technical language vs contextual pragmatics
* Strong vs weak assumptions about semantic stability over time
* Genre conventions as binding constraints vs looser affordances
* The role of co-text and broader corpus in fixing meaning

This includes the crucial distinction between **prima facie understanding** (default meaning from shared socio-linguistic practice) and **interpretation** as a more complex presumptive reasoning task when doubt arises.

## C) Hermeneutic school commitments (illustrative)

* **Intentionalist:** author’s communicative intent is primary
* **Textualist/formalist:** artifact-internal constraints dominate
* **Purposivist/teleological:** function/aim/purpose dominates
* **Reader-response/reception:** uptake/community practice is central
* **Canonical/tradition-governed:** final form + rule-of-faith/tradition constrain
* **Deconstructive:** emphasizes instability/iterability; critiques closure assumptions
* **Constructive:** optimize philosophical/ethical/aesthetic fruitfulness subject to constraints (“textual friction”)

## D) Epistemic and procedural commitments

* What counts as admissible evidence (manuscripts, legislative history, author letters, experiments, lived experience, model diagnostics, institutional records…)
* Burdens of proof, burden-shifting during critical questioning, and proof standards
* Error-cost profiles (false positives vs false negatives in interpretation)

## E) Value commitments

* What “best” means: truth, coherence, justice, salvation, emancipation, predictive accuracy, utility, aesthetic richness, institutional safety, etc.
* Whether consequences are admissible as evidence (teleological/purposive vs strict literalism/textual constraint)
* Why this goal is the right one for this community and object (often moral/political/theological/pragmatic)

---

# 6) Critical questions: a comprehensive checklist

A central insight is that interpretive arguments share a general critical-question spine:

1. **What plausible alternatives exist?**
2. **What reasons reject them?**
3. **What reasons support an alternative as better/equally good?**

Below is that spine expanded into a full set covering task framing, framework choice (Scheme I), and interpretation choice (Scheme II).

---

## A. CQs about the interpretive task (framing)

1. What exactly is the disputed element **E** (term, clause, symbol, gesture, data feature, model component)?
2. What is the domain **Dom** and artifact type **T**?
3. What is the interpretive goal **G** (reconstruction, application, critique, explanation, prediction, optimization, aesthetic illumination, etc.)?
4. Is **G** legitimate/appropriate for this domain and audience (court, church, seminar, lab/peer review, product team)?
5. What decision/stakes hinge on the interpretation, and what error-cost profile follows?

---

## B. CQs about object identity and boundaries

6. Are we interpreting the right object **D** (which edition, manuscript tradition, translation, dataset version, model version, build)?
7. Are the boundaries of **E** correct (word, sentence, clause, whole work, canon, dataset slice, model family)?
8. Is **E/D** possibly corrupted, interpolated, mistranslated, noisy, non-authoritative, or otherwise unreliable for this question?

---

## C. CQs about context selection

9. What contexts **Cxt** are relevant (immediate co-text, broader corpus, genre, institutional setting, historical setting, speaker/audience situation, task setting)?
10. Why these contexts rather than others? Are we cherry-picking or importing context illicitly?

---

## D. CQs for Scheme I: choosing evaluative criteria / framework F

11. What alternative frameworks **F′** are plausible here (text-first, intent-first, purpose-first, reception-first, empirical-fit-first, tradition-first, etc.)?
12. What are the reasons to reject each **F′** (inapplicable, violates authority rules, ignores key evidence types, yields systematic bias, contradicts binding procedure, etc.)?
13. What are the reasons an alternative **F′** is better/equally good for **G**?
14. Are **F**’s triggering conditions actually met? (e.g., “technical meaning” requires a technical context; otherwise that canon is inapplicable.)
15. Does **F** specify priority rules for conflicts among criteria (what outranks what), and are those priority rules justified here?
16. Does **F** specify burdens/standards of proof—what counts as defeating vs merely raising doubt?
17. Does **F** rely on controversial background assumptions (inerrancy, strong intentionalism, strong skepticism, etc.), and are those defensible here?
18. Can **F** actually be applied given practical constraints (evidence availability, competence, time, procedure)?

---

## E. CQs for Scheme II: arguing for interpretation M under F

19. What is the prima facie/default reading—and why isn’t it sufficient here?
20. What admissible evidence supports **M** under **F** (textual, contextual, historical, empirical, institutional, genre-based, functional/purpose evidence, etc.)?
21. Are any key premises merely assumed (missing warrants, hidden definitional steps, suppressed context)?
22. What defeaters exist?

* **Rebutters:** rival interpretations **M′** supported by comparable arguments.
* **Undercutters:** attacks on applicability of the inference rule/criterion being used (e.g., “that canon doesn’t apply here”).

23. Have all reasonable alternative interpretations **M₁…Mₙ** been considered?
24. What reasons reject each alternative?
25. What reasons suggest an alternative is better/equally good?
26. If multiple interpretations remain comparably supported, what rule breaks ties (priority rules, charity, conservatism, simplicity, minimal revision, institutional safety, etc.)?
27. Is **M** consistent with the broader system/corpus/practice that **F** treats as relevant (precedent, tradition, genre family, model family)?
28. Does **M** overfit local details while breaking global constraints (or vice versa)?
29. Does **M** depend on anachronism or illicit context importation (especially for historically distant texts)?
30. Is **M** robust across nearby cases/usages, or does it only “work” for a cherry-picked scenario?
31. Does the evidence offered bear on **meaning** rather than merely on desirability, ideology, or association?
32. Is the evidence sufficient to support the premises if challenged (especially where CQs shift the burden back to the proponent)?
33. What counterevidence supports rebutting interpretations or attacks premises directly?
34. Is there an exception that blocks the inference from the support to the conclusion (irony, sarcasm, technical jargon, redaction, corruption, measurement error, domain shift, institutional constraint, etc.)—and is the alleged exception itself well-supported?

---

## F. CQs about procedural rationality, burden, and convergence

35. Who bears the burden to support the interpretation, and when does it shift during critical questioning?
36. What proof standard is in force (preponderance, beyond reasonable doubt, scholarly plausibility, domain-specific acceptance thresholds), and does the current pro/con graph meet it?
37. Given the current pro/con graph, is **M** merely **defensible** or actually **justified** under the chosen standard?
38. If multiple incompatible interpretations remain, does the downstream decision actually depend on choosing between them—or do rival interpretations converge on the same operative outcome (a weak-justification/convergence case)?

---

## G. CQs about output quality and interpretive robustness

39. Is **M** too vague (unfalsifiable/elastic) or too specific (overfitted)?
40. Does **M** remain plausible under small context changes, or is it fragile and “just-so”?
41. Does **M** integrate explanatoryly with other parts of **D** or the relevant corpus without ad hoc patches?
42. Are we “jumping to a conclusion” prematurely, rather than letting the objection-and-response cycle run to convergence?

### H. Dialectical/procedural CQs (burdens, standards, audiences)

22. **Burden allocation:** Who bears the burden to support the interpretation, and when does it shift during critical questioning? 
23. **Proof standard:** What proof standard is in force (preponderance, beyond reasonable doubt, scholarly plausibility, etc.), and does the argument meet it? (Carneades uses proof standards to resolve conflicts .)
24. **Defensible vs justified:** Is M merely defensible (supported in some acceptable extension), or justified in a stronger sense? 

---

# 7) Practical note on interpretive warrants (families of admissible support)

Across domains, interpretive support often draws from recurring families of warrants/criteria, including (non-exhaustively):

* **Ordinary meaning / conventional use** (often a default starting point)
* **Technical meaning** (triggered by technical context)
* **Contextual harmonization** (co-text/corpus coherence)
* **Precedent / tradition / canonical constraints**
* **Analogy and concept-based reasoning**
* **General principles and systematic fit**
* **Historical evidence** (authorship, drafting, redaction, reception history)
* **Purpose / function / teleology**
* **Substantive reasons** (domain-accepted normative or pragmatic reasons)
* **Intent evidence** (when admissible under the chosen framework)

Which of these are admissible, how they’re weighted, and which outrank which are questions for **Scheme I**.

---

# 8) What the framework delivers

The output of interpretive reasoning is not merely “**M**,” but a **statused interpretive conclusion**:

* **The proposed meaning-attribution:** **BestInt(E, D | Cxt, G, A) ≡ M**
* **Its dialectical status:** *defensible* vs *justified* (relative to proof standards and the current pro/con graph)
* **The governing evaluative framework:** **F** (criteria + priority + burdens/standards)
* **The live defeaters and unresolved ties:** what would need to change to overturn or strengthen the conclusion

This makes interpretation a transparent, revisable, burden-sensitive form of practical reasoning: a structured method for moving from doubt to a justified meaning-attribution under explicit goals and standards.
