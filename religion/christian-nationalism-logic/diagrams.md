# Causal Loop Diagrams

## Diagram 1 — Core reinforcing loops (R1–R5)

```plantuml
@startuml
top to bottom direction
skinparam backgroundColor white
skinparam defaultFontName Arial
skinparam dpi 170
skinparam nodesep 60
skinparam ranksep 80
skinparam padding 12
skinparam ArrowColor #444444
skinparam ArrowThickness 1.25
skinparam packageStyle rectangle
skinparam ArrowFontSize 18
skinparam ArrowFontStyle bold
skinparam titleFontSize 20
skinparam packageFontSize 16
skinparam package {
  BorderColor #666666
  BackgroundColor #FAFAFA
  FontStyle bold
}

skinparam rectangle {
  BackgroundColor #FDFDFD
  BorderColor #333333
  RoundCorner 15
  FontSize 16
}

title Core Reinforcing Loops (R1–R5)

package "R1 — Cosmic war threat inflation" {
  rectangle "Cosmic-war framing\n\n(sacralized conflict lens)" as CWF
  rectangle "Perceived threat\n\n(enemy presence / danger)" as PT
  rectangle "Boundary policing\n\n(guarding orthodoxy / identity)" as BP
  rectangle "Out-group hostility\n\n(moralized antagonism)" as OGH
  rectangle "Intergroup conflict\n\n(open social or political clash)" as IGC
  rectangle "\"Evidence\" of cosmic war\n\n(conflict re-read as proof)" as EVCW

  CWF --> PT : +
  PT --> BP : +
  BP --> OGH : +
  OGH --> IGC : +
  IGC --> EVCW : +
  EVCW --> CWF : +
}

package "R2 — Moral monopoly -> distrust -> preemptive coercion" {
  rectangle "Exclusivism /\nmoral monopoly belief\n\n'only one right order'" as EX
  rectangle "Moral out-group distrust\n\nothers seen as corrupting" as MOD
  rectangle "Fear of out-group\n\nthreat perception intensifies" as FOG
  rectangle "Support for coercive control\n\nforce feels protective" as SCC
  rectangle "Enforcement capacity used\n\nrules, sanctions, pressure" as ECU
  rectangle "Out-group resentment /\nresistance\n\nbacklash to control" as OGR
  rectangle "Threat signals\n\nresentment read as danger" as TS

  EX --> MOD : +
  MOD --> FOG : +
  FOG --> SCC : +
  SCC --> ECU : +
  ECU --> OGR : +
  OGR --> TS : +
  TS --> FOG : +
}

package "R3 — Purity policing cohesion loop" {
  rectangle "Perceived social disorder\n\nmoral decline / instability" as PSD
  rectangle "Purity / contamination salience\n\npollution frame activated" as PCS
  rectangle "Scapegoating of deviants\n\nblame assigned to offenders" as SCD
  rectangle "Short-term in-group cohesion\n\nunity through exclusion" as SIGC
  rectangle "Leader legitimacy\n\nauthority strengthened" as LL
  rectangle "Capacity to police purity\n\norganizational readiness" as CPP
  rectangle "Purity policing intensity\n\nstronger enforcement" as PPI

  PSD --> PCS : +
  PCS --> SCD : +
  SCD --> SIGC : +
  SIGC --> LL : +
  LL --> CPP : +
  CPP --> PPI : +
  PPI --> PSD : +
}

package "R4 — Outsourced vengeance / deferred revenge" {
  rectangle "Harm / grievance\n\ninjury, humiliation, loss" as HG
  rectangle "Anger\n\naffective escalation" as AN
  rectangle "Divine vengeance salience\n\npunishment imagined as just" as DVS
  rectangle "Moral certainty /\ncontempt\n\nopponent judged absolutely" as MCC
  rectangle "Dehumanization\n\nreduced moral standing" as DH
  rectangle "Willingness to support\nharsh punishment\n\nseverity normalized" as WSHP
  rectangle "Institutional coercion\n\npunishment through systems" as IC

  HG --> AN : +
  AN --> DVS : +
  DVS --> MCC : +
  MCC --> DH : +
  DH --> WSHP : +
  WSHP --> IC : +
  IC --> HG : +
}

package "R5 — Literalism / hard commands escalation" {
  rectangle "Literalism /\ninerrancy intensity\n\nlow interpretive flexibility" as LIT
  rectangle "Perceived divine\nmandate certainty\n\ncertainty of command" as PDMC
  rectangle "Compromise taboo\n\nconcession feels sinful" as CT
  rectangle "Polarization\n\npositions harden" as POL
  rectangle "Conflict\n\nsocial confrontation" as CON
  rectangle "Identity threat\n\nself-understanding destabilized" as IT
  rectangle "Demand for certainty\n\npeople seek harder answers" as DFC

  LIT --> PDMC : +
  PDMC --> CT : +
  CT --> POL : +
  POL --> CON : +
  CON --> IT : +
  IT --> DFC : +
  DFC --> LIT : +
}

IGC --> PT : +
IGC --> HG : +
IGC --> CON : +

PT --> FOG : +
PT --> PSD : +

ECU --> BP : +
ECU --> IC : +

OGH --> DH : +
DH --> OGH : +

IC --> IGC : +
IC --> PSD : +

PPI --> BP : +
PPI --> ECU : +

FOG --> PCS : +
TS --> PT : +

POL --> BP : +
POL --> OGH : +

MCC --> CT : +
DVS --> CT : +

IT --> PT : +
DFC --> EX : +

@enduml
```

## Diagram 2 — Balancing loops (B1–B3) and failure modes

```plantuml
@startuml
top to bottom direction
skinparam backgroundColor white
skinparam defaultFontName Arial
skinparam dpi 170
skinparam nodesep 60
skinparam ranksep 80
skinparam padding 12
skinparam ArrowColor #444444
skinparam ArrowThickness 1.25
skinparam packageStyle rectangle
skinparam ArrowFontSize 18
skinparam ArrowFontStyle bold
skinparam titleFontSize 20
skinparam packageFontSize 16
skinparam package {
  BorderColor #666666
  BackgroundColor #FAFAFA
  FontStyle bold
}

skinparam rectangle {
  BackgroundColor #FDFDFD
  BorderColor #333333
  RoundCorner 15
  FontSize 16
}

title Balancing Loops (B1–B3) and Their Failure Modes

package "B1 — Mercy / enemy-love / forgiveness" {
  rectangle "Mercy norms\n\nrestraint,\nforgiveness,\nenemy-love" as MN
  rectangle "Retaliation impulses\n\ndesire to\nstrike back" as RI
  rectangle "Intergroup conflict\n\nactive social or\npolitical antagonism" as IGC
  rectangle "Perceived threat\n\ndanger\ninterpretation" as PT
  rectangle "Boundary policing\n\ncontrol in defense\nof order" as BP

  MN --> RI : -
  RI --> IGC : +
  IGC --> PT : +
  PT --> BP : +
  BP --> MN : -
}

package "B1 failure modes" {
  rectangle "Bounded mercy\n\nmercy only for\ninsiders" as BM
  rectangle "Institutional partition\n\nprivate mercy,\npublic punishment" as IP
  rectangle "Temporal deferral\n\nmercy now,\npunishment later" as TD
  rectangle "Persecution recoding\n\ncontrol reframed as\nself-defense" as PR

  MN --> BM : +
  BM --> IGC : +
  MN --> IP : +
  IP --> BP : +
  MN --> TD : +
  TD --> IGC : +
  IGC --> PR : +
  PR --> PT : +
}

package "B2 — Humility / self-critique" {
  rectangle "Humility norms\n\nfallibility\nacknowledged" as HN
  rectangle "Moral certainty /\nself-righteousness\n\ncertainty about\nown purity" as MCSR
  rectangle "Dehumanization\n\nothers morally\ndowngraded" as DH
  rectangle "Support for coercion\n\ncontrol endorsed as\nnecessary" as SFC
  rectangle "Conflict\n\nsocial struggle\nintensifies" as CON

  HN --> MCSR : -
  MCSR --> DH : +
  DH --> SFC : +
  SFC --> CON : +
  CON --> HN : -
}

package "B2 failure modes" {
  rectangle "Moral licensing\n\n'humility' proves\nrighteousness" as ML
  rectangle "Hierarchy capture\n\n'humility' becomes\ndownward obedience" as HC
  rectangle "Selective application\n\nhumility demanded\nof subordinates" as SA
  rectangle "Authority / obedience\n\npower asymmetry\nnormalized" as AO
  rectangle "Policing intensity\n\nstricter\nenforcement" as PI

  HN --> ML : +
  ML --> MCSR : +
  HN --> HC : +
  HC --> AO : +
  AO --> PI : +
  HN --> SA : +
  SA --> AO : +
}

package "B3 — Nonviolence / sanctity-of-life" {
  rectangle "Nonviolence norms\n\nviolence morally\nrestrained" as NV
  rectangle "Legitimacy of\nviolent means\n\nforce seen as\npermissible" as LVM
  rectangle "Violence\n\nactual coercive\naction" as V
  rectangle "Grievance\n\nhurt and backlash\naccumulate" as G

  NV --> LVM : -
  LVM --> V : +
  V --> G : +
  G --> NV : -
}

package "B3 failure modes" {
  rectangle "Reclassification\n\nviolence renamed\n'justice' or 'defense'" as RC
  rectangle "Delegation to state /\nmilitia / divine violence\n\noutsourced force" as DV
  rectangle "Apocalyptic urgency\n\nemergency\nmentality" as AU
  rectangle "Emergency override\n\nnormal restraint\nsuspended" as EO

  NV --> RC : +
  RC --> LVM : +
  NV --> DV : +
  DV --> V : +
  AU --> EO : +
  EO --> LVM : +
}
@enduml
```

## Diagram 3 — Enabling conditions that amplify loops and weaken restraints

```plantuml
@startuml
top to bottom direction
skinparam backgroundColor white
skinparam defaultFontName Arial
skinparam dpi 170
skinparam nodesep 60
skinparam ranksep 80
skinparam padding 12
skinparam ArrowColor #444444
skinparam ArrowThickness 1.25
skinparam packageStyle rectangle
skinparam ArrowFontSize 18
skinparam ArrowFontStyle bold

skinparam titleFontSize 20
skinparam packageFontSize 16
skinparam package {
  BorderColor #666666
  BackgroundColor #FAFAFA
  FontStyle bold
}

skinparam rectangle {
  BackgroundColor #FDFDFD
  BorderColor #333333
  RoundCorner 15
  FontSize 16
}

title Enabling Conditions: What Raises Gain and Weakens Balancers

package "Doctrinal absolutization" {
  rectangle "Exclusive truth claims\n\nerror becomes existential" as ETC
  rectangle "Divine command /\nscripture-as-directive\n\nobedience overrides hesitation" as DCD
  rectangle "Literalism /\ninerrancy\n\nreduced interpretive friction" as LI
}

package "Boundary criminalization" {
  rectangle "Heresy / apostasy /\nblasphemy framing\n\ndeviation treated as threat" as HAB
  rectangle "Purity / abomination\ncategories\n\ndifference moralized as contamination" as PAC
}

package "Eschatological intensification" {
  rectangle "Cosmic war +\napocalyptic urgency\n\ndisagreement sacralized" as CWAU
  rectangle "Divine vengeance /\nhell-as-justice\n\npunitive imagination sanctified" as DVH
}

package "Political sacralization" {
  rectangle "Sacred land /\nchosenness politicization\n\nterritory and identity sacralized" as SLCP
  rectangle "Missionary universalism\nunder power\n\nexpansion takes coercive form" as MU
  rectangle "Centralized orthodoxy +\nscalable enforcement\n\nideas become apparatus" as COSE
}

package "Amplified reinforcing loops" {
  rectangle "R1 gain\n\ncosmic war loop strengthens" as R1G
  rectangle "R2 gain\n\ncoercive distrust loop strengthens" as R2G
  rectangle "R3 gain\n\npurity-policing loop strengthens" as R3G
  rectangle "R4 gain\n\nvengeance loop strengthens" as R4G
  rectangle "R5 gain\n\ncertainty / literalism loop strengthens" as R5G
}

package "Weakened balancing loops" {
  rectangle "B1 effectiveness\n(mercy)\n\nlower ability to damp retaliation" as B1E
  rectangle "B2 effectiveness\n(humility)\n\nlower ability to check certainty" as B2E
  rectangle "B3 effectiveness\n(nonviolence)\n\nlower ability to restrain force" as B3E
}

ETC --> R1G : +
ETC --> R2G : +
ETC --> B2E : -

DCD --> R3G : +
DCD --> R5G : +

LI --> R3G : +
LI --> R5G : +

HAB --> R2G : +
HAB --> B1E : -

PAC --> R3G : +
PAC --> B1E : -
PAC --> B3E : -

CWAU --> R1G : +
CWAU --> R5G : +
CWAU --> B1E : -
CWAU --> B2E : -
CWAU --> B3E : -

DVH --> R4G : +
DVH --> B1E : -

SLCP --> R1G : +

MU --> R2G : +
MU --> R3G : +

COSE --> R2G : +
COSE --> R3G : +
COSE --> B2E : -

@enduml
```
## Diagram 4A — Structural and interpretive interventions with backlash

```plantuml
@startuml
scale 0.58
top to bottom direction
skinparam backgroundColor white
skinparam defaultFontName Arial
skinparam dpi 120
skinparam nodesep 40
skinparam ranksep 55
skinparam padding 8
skinparam ArrowColor #444444
skinparam ArrowThickness 1.05
skinparam packageStyle rectangle

skinparam titleFontSize 16
skinparam packageFontSize 13
skinparam ArrowFontSize 18
skinparam ArrowFontStyle bold
skinparam package {
  BorderColor #666666
  BackgroundColor #FAFAFA
  FontStyle bold
}

skinparam rectangle {
  BackgroundColor #FDFDFD
  BorderColor #333333
  RoundCorner 12
  FontSize 13
}

title Diagram 4A — Structural and Interpretive Interventions with Backlash

package "I1 + R6 — Interpretive moderation and backlash" {
  rectangle "Interpretive moderation\n\ncontextual reading\nsoftens rigidity" as IM
  rectangle "Literalism\n\nhard textual\ncertainty" as LIT
  rectangle "Mandate certainty\n\ncommands feel\nabsolute" as MC
  rectangle "Compromise taboo\n\nconcession feels\nfaithless" as CT
  rectangle "Conflict\n\npolarized\nstruggle" as CON

  rectangle "'Watering down truth'\n\nmoderation seen\nas betrayal" as WDT
  rectangle "Identity threat\n\nloss of certainty\nor status" as IT
  rectangle "Demand for certainty\n\nharder boundaries\nsought" as DFC

  IM --> LIT : -
  LIT --> MC : +
  MC --> CT : +
  CT --> CON : +

  IM --> WDT : +
  WDT --> IT : +
  IT --> DFC : +
  DFC --> LIT : +
}

package "I2 + R7 — Pluralism protections and security spiral" {
  rectangle "Pluralism protections\n\nrights of conscience\nlimit domination" as PP
  rectangle "Boundary policing\n\nattempt to restore\ncontrol" as BP
  rectangle "Persecution of dissenters\nor out-group\n\npunitive response" as PDO
  rectangle "Threat\n\ndanger\nperception" as TH

  rectangle "Visibility of difference\n\nmore public\nplurality" as VOD
  rectangle "Perceived disorder\n\nplurality read\nas decay" as PD
  rectangle "Purity anxiety\n\ncontamination\nfear" as PA
  rectangle "Boundary-policing\nmovement\n\nrestoration drive" as BPM

  PP --> BP : -
  BP --> PDO : +
  PDO --> TH : +
  TH --> PP : -

  PP --> VOD : +
  VOD --> PD : +
  PD --> PA : +
  PA --> BPM : +
  BPM --> PP : -
}

package "I3 + R8 — Church-state separation and restoration backlash" {
  rectangle "Church-state separation\n\ncoercive capacity\nreduced" as CSS
  rectangle "Scalable punishment\n\nstate-backed\nenforcement" as SP
  rectangle "Conflict / grievance\n\nhurt and\nresentment" as CG
  rectangle "Demand for coercion\n\npressure for\nstronger control" as DFC2

  rectangle "Moral chaos\n\nloss of sacred\norder felt" as PMC
  rectangle "'Restore godly order'\nmovement\n\nreactionary\nmobilization" as RGOM
  rectangle "Political sacralization\n\nstate cast as\nholy instrument" as PS
  rectangle "Enforcement capacity\n\npower available\nagain" as EC

  CSS --> SP : -
  SP --> CG : +
  CG --> DFC2 : +
  DFC2 --> CSS : -

  CSS --> PMC : +
  PMC --> RGOM : +
  RGOM --> PS : +
  PS --> EC : +
  EC --> CSS : -
}

CON --> TH : +
TH --> IT : +
BP --> PA : +
BP --> PMC : +
CG --> TH : +
PA --> BPM : +
IT --> DFC : +

@enduml
```

## Diagram 4B — Punishment, contact, and intervention erosion

```plantuml
@startuml
scale 0.58
top to bottom direction
skinparam backgroundColor white
skinparam defaultFontName Arial
skinparam dpi 120
skinparam nodesep 40
skinparam ranksep 55
skinparam padding 8
skinparam ArrowColor #444444
skinparam ArrowThickness 1.05
skinparam packageStyle rectangle

skinparam titleFontSize 16
skinparam packageFontSize 13
skinparam ArrowFontSize 18
skinparam ArrowFontStyle bold

skinparam package {
  BorderColor #666666
  BackgroundColor #FAFAFA
  FontStyle bold
}

skinparam rectangle {
  BackgroundColor #FDFDFD
  BorderColor #333333
  RoundCorner 12
  FontSize 13
}

title Diagram 4B — Punishment, Contact, and Why Interventions Erode

package "I4 + R9 — Restorative justice and backlash" {
  rectangle "Restorative justice\n\ntheology of repair\nover punishment" as RJT
  rectangle "Divine vengeance\nsalience\n\npunitive imagination" as DVS
  rectangle "Contempt\n\nmoral\nhardening" as CPT
  rectangle "Dehumanization\n\nothers seen as\nless worthy" as DH
  rectangle "Support for harsh\ncoercion\n\nseverity endorsed" as SHC

  rectangle "'Soft on evil'\n\nmercy framed\nas weakness" as SOE
  rectangle "Fear\n\ndanger and\nexposure felt" as FEAR
  rectangle "Demand for punishment\n\ncalls for\nseverity" as DFP

  RJT --> DVS : -
  DVS --> CPT : +
  CPT --> DH : +
  DH --> SHC : +

  RJT --> SOE : +
  SOE --> FEAR : +
  FEAR --> DFP : +
  DFP --> DVS : +
}

package "I5 + R10 — Intergroup contact and segregation backlash" {
  rectangle "Intergroup contact\n\nhumanization through\nencounter" as ICME
  rectangle "Dehumanization\n\nshared humanity\nless recognized" as DH2
  rectangle "Fear\n\nanxiety about\nthe other" as FEAR2
  rectangle "Support for coercion\n\ncontrol framed\nas safety" as SFC

  rectangle "Boundary entrepreneurs\n\nactors profiting\nfrom division" as BE
  rectangle "Segregation /\npurity boundaries\n\ncontact reduced" as SPB

  ICME --> DH2 : -
  DH2 --> FEAR2 : +
  FEAR2 --> SFC : +

  ICME --> BE : +
  BE --> SPB : +
  SPB --> ICME : -
  SPB --> DH2 : +
}

package "Meta-dynamic — why interventions erode" {
  rectangle "Balancers strengthened\n\ninitial\nde-escalation" as BS
  rectangle "Identity-threat backlash\n\nloss interpreted\nas danger" as ITB
  rectangle "Control loops reactivated\n\ncertainty, purity,\nand control return" as CPCR
  rectangle "Moderation erodes\n\nintervention loses\nforce" as ME

  BS --> ITB : +
  ITB --> CPCR : +
  CPCR --> ME : +
  ME --> BS : -
}

FEAR --> FEAR2 : +
FEAR2 --> FEAR : +
DFP --> SHC : +
DH --> DH2 : +
DH2 --> DH : +
SFC --> ITB : +
SHC --> ITB : +
CPCR --> DVS : +
CPCR --> DH : +
CPCR --> BE : +
BS --> RJT : +
BS --> ICME : +

@enduml
```