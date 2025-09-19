# What is Computation?
![build status](https://github.com/praisetompane/computation/actions/workflows/computation.yaml/badge.svg) <br>

**Disclaimer**: This is an ongoing and incomplete project to unpack these concepts and serves as my exosomatic memory.

- [What is Computation?](#what-is-computation)
  - [Objectives](#objectives)
  - [Definitions](#definitions)
      - [Formal Classification Scheme](#formal-classification-scheme)
      - [Foundations](#foundations)
      - [Invention | Discovery](#invention--discovery)
  - [Learning Order](#learning-order)
  - [Dependencies](#dependencies)
  - [Setup Instructions](#setup-instructions)
  - [History](#history)
  - [Tools](#tools)
  - [State Of The Art](#state-of-the-art)
  - [Community](#community)
  - [Computer Scientists](#computer-scientists)
  - [Testing](#testing)
  - [References](#references)
  - [Legend](#legend)

## Objectives
- An attempt at distilling to layman's terms:
  - Computation.
  - Computation's Foundations and Invention | Discovery.
  - Computation's Relationship with [Logic](https://github.com/praisetompane/logic) and [Mathematics](https://github.com/praisetompane/mathematics).

## Definitions
- def computation¹: the **transformation** of **sequences of symbols** by **precise rules**(Konrad, 2015:6).

- def computation²: The **evolution process** of some environment, by a **sequence of "simple, local" steps** (Stanford Encyclopedia of Philosophy).

- def computation³: the execution of a list of steps to do something.

#### Formal Classification Scheme
  - [ACM](https://dl.acm.org/ccs)

#### Foundations
  - [Theoretical Basis](https://zbmath.org/classification/?q=cc%3A03D)
  - [Formal Science](https://zbmath.org/classification/?q=cc%3A68)
  - [Philosophy](https://plato.stanford.edu/entries/computer-science/)

#### Invention | Discovery
![](1_mathematics_of_computing/mathematics-science-engineering.drawio.svg)

![](1_mathematics_of_computing/mathematics_and_computation.drawio.svg)

## Learning Order
- [0_theory_of_computation](0_theory_of_computation/)
  - [0_logic](0_theory_of_computation/0_logic)
  - [1_formal_languages_and_automata_theory](0_theory_of_computation/1_formal_languages_and_automata_theory/)
  - [2_models_of_computation](0_theory_of_computation/2_models_of_computation/0_computability/)
  - [3_computational_complexity_and_cryptography](0_theory_of_computation/3_computational_complexity_and_cryptography/0_complexity_theory_and_logic/)
- [1_mathematics_of_computing](1_mathematics_of_computing/)
- [0_theory_of_computation/4_design_and_analysis_of_algorithms](0_theory_of_computation/4_design_and_analysis_of_algorithms/)
- [2_hardware](2_hardware)
- [3_computer_systems_organization](3_computer_systems_organization/)
- [4_software_and_its_engineering](4_software_and_its_engineering)
  - [1_general_programming_languages](4_software_and_its_engineering/0_software_notations_and_tools/1_general_programming_languages/)
    - [0_assembly_languages](4_software_and_its_engineering/0_software_notations_and_tools/1_general_programming_languages/0_language_types/0_assembly_languages/0_assembly_languages.txt)
    - [1_imperative_languages](4_software_and_its_engineering/0_software_notations_and_tools/1_general_programming_languages/0_language_types/1_imperative_languages/0_imperative_languages.txt)
    - [2_functional_languages](4_software_and_its_engineering/0_software_notations_and_tools/1_general_programming_languages/0_language_types/2_functional_languages/0_functional_languages.txt)
    - [3_multiparadigm_languages](4_software_and_its_engineering/0_software_notations_and_tools/1_general_programming_languages/0_language_types/3_multiparadigm_languages/0_multiparadigm_languages.txt)

## Dependencies
- [Docker](https://docs.docker.com/get-started/)

## Setup Instructions
- The repository is configured to use [devcontainers](https://containers.dev) for development. <br>It requires no setup except an editor that supports devcontainers, which will prompt you on first open to start it in a container.
    - [Supported Editors](https://containers.dev/supporting)
    - [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)

## History
- [The Modern History of Computing](https://plato.stanford.edu/entries/computing-history/)

## Tools
- [Theoretical CS Visualizer](https://www.theoreticalcs.io/)
- [Reverse Engineering](https://crackmes.one)
- [Know Thy Complexities!](https://www.bigocheatsheet.com/)

## State Of The Art
- [Quanta Magazine](https://www.quantamagazine.org/computer-science/)
- [MIT EECS](https://www.eecs.mit.edu/research/computer-science/)
- [Development](https://www.infoq.com/development/)
- [Architecture & Design](https://www.infoq.com/architecture-design/)
- [AI, ML & Data Engineering](https://www.infoq.com/ai-ml-data-eng/)
- [AI, ML & Data Engineering](https://read.deeplearning.ai/the-batch/)
- [Culture & Methods](https://www.infoq.com/culture-methods/)
- [DevOps](https://www.infoq.com/devops/)

## Community

## Computer Scientists
- [The Academic Genealogy of Computer Science](https://academictree.org/computerscience/)
- [ACM A.M. Turing Award Laureate Interviews](https://www.youtube.com/playlist?list=PLn0nrSd4xjjaSLBSzmno-3Ods6FJE9nlO)
- Alan Turing
- Alonzo Church
- Donald Knuth
- Erik Demaine
- Jelani Nelson
- Katherine Johnson
- Grace Hopper
- Frances Elizabeth Allen

## Testing
- ### Execute Tests
  ```shell
  pytest
  ```

- ## Spell Check
```shell
pyspelling -c spellcheck.yaml
```

## References
- Konrad H. 2015. Computation in Science. Morgan & Claypool Publishers.
- [Stanford Encyclopedia of Philosophy. The Church-Turing Thesis](https://plato.stanford.edu/entries/church-turing/).

## Legend
**Q**: Question for later research<br>
**MYINC**: My Insight/Conjecture [Could Be Unoriginal/False and Likely Is]<br>
**see: ...**: Points to the definition of a concept used in another definition.
