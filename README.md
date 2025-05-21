# What is Computation?
![build status](https://github.com/praisetompane/computation/actions/workflows/computation.yaml/badge.svg) <br>

- [What is Computation?](#what-is-computation)
  - [Objectives](#objectives)
  - [Definitions](#definitions)
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
- An attempt at unpacking Computation and the implementation of computing machinery in layman's terms.

## Definitions
- def computation¹: the **transformation** of **sequences of symbols** by **precise rules**(Konrad, 2015:6).
  - def symbols = {1,0,\*,{,;,<,>,...}
    - example sequences:
      - 11010
      - ;\*>{11}
        i.e. any sequence of the valid symbols
  - def precise rules = steps to follow

- def computation²: The **evolution process** of some environment, by a **sequence of "simple, local" steps** (Stanford Encyclopedia of Philosophy).
- def computation³: a list of steps to do something
- def compute: to do/run a computation.

- Formal Classification Scheme:
  - [ACM](https://dl.acm.org/ccs)
  - [ZBMATH](https://zbmath.org/classification/?q=cc%3A68)

## Learning Order
- [5_software_and_its_engineering](5_software_and_its_engineering)
  - [1_general_programming_languages](5_software_and_its_engineering/0_software_notations_and_tools/1_general_programming_languages)
    - [1_imperative_languages](5_software_and_its_engineering/0_software_notations_and_tools/1_general_programming_languages/0_language_types/1_imperative_languages.txt)
    - [2_functional_languages](5_software_and_its_engineering/0_software_notations_and_tools/1_general_programming_languages/0_language_types/2_functional_languages.txt)
    - [0_assembly_languages](5_software_and_its_engineering/0_software_notations_and_tools/1_general_programming_languages/0_language_types/0_assembly_languages.txt)
    - [3_multiparadigm_languages](5_software_and_its_engineering/0_software_notations_and_tools/1_general_programming_languages/0_language_types/3_multiparadigm_languages.txt)
- [1_mathematics_of_computing](1_mathematics_of_computing/)
- [0_theory_of_computation](0_theory_of_computation)
  - [4_design_and_analysis_of_algorithms](0_theory_of_computation/4_design_and_analysis_of_algorithms/)
  - [0_logic](0_theory_of_computation/0_logic)
  - [1_models_of_computation](0_theory_of_computation/1_models_of_computation/0_computability/)
  - [2_formal_languages_and_automata_theory](0_theory_of_computation/2_formal_languages_and_automata_theory)
  - [3_computational_complexity_and_cryptography](0_theory_of_computation/3_computational_complexity_and_cryptography)
- [2_hardware](2_hardware)
- [3_computer_systems_organization](3_computer_systems_organization/)

## Dependencies
- [Docker](https://docs.docker.com/get-started/)

## Setup Instructions
- The repository is configured to use [devcontainers](https://containers.dev) for development. <br>It requires no setup except an editor that supports devcontainers, which will prompt you on first open to start it in a container.
    - [Supported Editors](https://containers.dev/supporting)
    - [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)

## History
- [The Modern History of Computing](https://plato.stanford.edu/entries/computing-history/)

## Tools
[Theoretical CS Visualizer](https://www.theoreticalcs.io/)
[Reverse Engineering](https://crackmes.one)

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
- [HackerNews](https://news.ycombinator.com/news)

## Computer Scientists
- Erik Demaine
- Jelani Nelson
- Katherine Johnson
- [ACM A.M. Turing Award Laureate Interviews](https://www.youtube.com/playlist?list=PLn0nrSd4xjjaSLBSzmno-3Ods6FJE9nlO)
- [The Academic Genealogy of Computer Science](https://academictree.org/computerscience/)

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
**MYINC**: My Insight/Conjecture [Could Be Unoriginal/False and Likely Is]

**Disclaimer**: This is an ongoing and incomplete project to unpack these concepts and serves as my exosomatic memory.