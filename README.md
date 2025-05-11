# What is Computation?
![build status](https://github.com/praisetompane/computation/actions/workflows/computation.yaml/badge.svg) <br>

## Objectives
- An attempt at unpacking Computation and the implementation of computing machines in layman's terms.

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
  
## Dependencies
- [Docker](https://docs.docker.com/get-started/)

## Setup Instructions
- The repository is configured to use [devcontainers](https://containers.dev) for development.
    - [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)

## History
- [The Modern History of Computing](https://plato.stanford.edu/entries/computing-history/)

## Tools
[Theoretical CS Visualizer](https://www.theoreticalcs.io/)
[Reverse Engineering](https://crackmes.one)

## State of the art
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

**Disclaimer**: This is an ongoing and incomplete project to unpack these concepts and serves as my distributed memory.
