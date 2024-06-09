Parse git-log Output Github Action
===

Thanks `claude-3-opus-20240229` and [LMSYS ChatBot Arena](https://chat.lmsys.org) for first draft.

<a href="https://circleci.com/gh/badges/shields/tree/master">
    <img src="https://img.shields.io/circleci/project/github/badges/shields/master" alt="build status">
</a>
<a href="https://circleci.com/gh/badges/daily-tests">
    <img src="https://img.shields.io/circleci/project/github/badges/daily-tests?label=service%20tests"
        alt="service-test status">
</a>
<a href="https://coveralls.io/github/badges/shields">
    <img src="https://img.shields.io/coveralls/github/badges/shields"
        alt="coverage">
</a>
<a href="https://lgtm.com/projects/g/badges/shields/alerts/">
    <img src="https://img.shields.io/lgtm/alerts/g/badges/shields"
        alt="Total alerts"/>
</a>

![coverage](https://img.shields.io/badge/coverage-80%25-yellowgreen)
![version](https://img.shields.io/badge/version-1.2.3-blue)
![dependencies](https://img.shields.io/badge/dependencies-out%20of%20date-orange)
![codacy](https://img.shields.io/badge/codacy-B-green)
![semver](https://img.shields.io/badge/semver-2.0.0-blue)

<!--
[![CodeQL](https://github.com/qte77/ML-HF-WnB-MVP/actions/workflows/codeql.yml/badge.svg)](https://github.com/qte77/ML-HF-WnB-MVP/actions/workflows/codeql.yml)
[![Lint Code Base](https://github.com/qte77/ML-HF-WnB-MVP/actions/workflows/linter.yml/badge.svg)](https://github.com/qte77/ML-HF-WnB-MVP/actions/workflows/linter.yml)
[![Links (Fail Fast)](https://github.com/qte77/ML-HF-WnB-MVP/actions/workflows/links-fail-fast.yml/badge.svg)](https://github.com/qte77/ML-HF-WnB-MVP/actions/workflows/links-fail-fast.yml)
-->

App skeleton to be used as github template repo.

Status
---

**[DRAFT]** **[WIP]** --> not fully implemented

Quickstart
---

* Quickstart

TOC
---

* [Usage](#usage-)
* [Install](#install-)
* [Purpose](#purpose-)
* [Reason](#reason-)
* [Paradigms](#paradigms-)
* [App Structure](#app-structure-)
* [App Details](#app-details-)
* [TODO](#todo-)
* [Inspirations](#inspirations-)
* [Rescources](#resources-)

Usage [↑](#toc)
---

* TODO Usage

Install [↑](#toc)
---

* TODO Install

Purpose [↑](#toc)
---

* TODO Purpose

Reason [↑](#toc)
---

* TODO Reason

Paradigms [↑](#toc)
---

* Keep to low branching factor and single outcomes
* Export complex functions into modules
* Aims for coding approach
  * Behavior Driven Design (What should it do?)
  * Test Driven Design (Does it do?)
* Aims for code quality
  * Works, i.e. passes tests which were written before
  * Modular and cohesive
  * Separation of concerns and appropriate coupling
  * Abstraction and information hiding
* Aims for CI/CD
  * Unit Testing
  * Acceptance Testing
  * Performance Testing
  * Static Analysis
  * Sign-offs
  * Security Testing
  * Scalability Testing
  * Realeasable Outcome

App Structure [↑](#toc)
---

```sh
/
├─ sub1/
│  ├─ sub1sub1/
│  │  ├─
│  │  └─
│  └─ file
├─ sub2/
│  └─ file
├─ file
└─ file
```

App Details [↑](#toc)
---

* Details

TODO [↑](#toc)
---

* Structure
  * [x] Test [Pipfile](https://pypi.org/project/pipfile/)
    * Adopted as [proposed successor](https://github.com/pypa/pipfile#the-concept) of requirements.txt
    * Several advantages like auto-venv and combined prod/dev in one TOML
    * [pipenv with Pipfile & Pipfile.lock](https://pipenv.pypa.io/en/latest/basics/)
    * `pipenv install -e` for [editable mode](https://pipenv.pypa.io/en/latest/basics/#a-note-about-vcs-dependencies), i.e. 'dependency resolution can be performed with an up to date copy of the repository each time it is performed'
  * [x] Use `Makefile` instead of self-implemented imparative `setup.sh`
    * Test successful and functional
  * [ ] Dynamically create a hierarchical configuration with [hydra](https://hydra.cc/docs/intro/)
  * [ ] Implement basic CI/CD-Skeleton
  * [ ] Create /docs with [`sphinx`](https://www.sphinx-doc.org/) gh-action
  * [ ] Have a look at [ReadTheDocs](http://docs.readthedocs.io/en/latest/yaml-config.html)
* Coding
  * [x] Try `dataclass` and `field` from [`dataclasses`](https://docs.python.org/3/library/dataclasses.html)
    * Used to auto add special classes like `__init__`, `__str__`, `__repr__`
    * Suitable for more complex classes and projects
  * [ ] Have a look at [PyTest](http://pytest.org/) to prepare for TDD and BDD
  * [ ] Consistent typing and type hinting
  * [ ] Use [`pydantic`](https://pydantic-docs.helpmanual.io/) or [`traitlets`](https://pypi.org/project/traitlets/) for type hinting or strong typing
  * [ ] Consistent usage of pydoc for /docs with [`pandoc`](https://pypi.org/project/pandoc/)
  * [ ] Decouple concerns into separate containers, e.g. avoid big container because of `torch`
  * Uses type hinting and decorators
  * [ ] Consistent usage of `if` or `try` for features and catches
  * [ ] Try [`logging`](https://docs.python.org/3/howto/logging.html) instead of `print()`
* API
  * [ ] Try [`arparse`](https://docs.python.org/3/library/argparse.html)
  * [ ] Implement basic API, e.g. with [gunicorn](https://github.com/benoitc/gunicorn) or [FastAPI](https://github.com/tiangolo/fastapi)
* Dependency tracking and app sourcing
  * [x] Test `__init__.py` for packing
    * Only needed for [regular packages Python 3.2 and earlier](https://docs.python.org/3/reference/import.html#regular-packages)
    * Python 3.3 and above uses [namespace packages](https://docs.python.org/3/reference/import.html#namespace-packages), see [PEP 420 - Implicit Namespace Packages](https://peps.python.org/pep-0420/)
  * [ ] Test conda [creating an environment from an environment.yml file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
    * `conda env create -f environment.yml`
  * [ ] Provide package as [single source app version](https://packaging.python.org/guides/single-sourcing-package-version/) with `setup.py`
  * [ ] Experiment with [`pyproject.toml`](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) to build app wheel
* Best Practices
  * [x] Adopt [SemVer](https://semver.org/)
    * Using MAJOR.MINOR.PATCH (Breaking.Feature.Patch)
  * [x] Adopt [`CHANGELOG.md`](https://keepachangelog.com/)
    * Using `Added`, `Removed`, `Changed` and `Unreleased`
    * Also recommended: `Deprecated`, `Fixed` and `Security`
  * [x] Adopt [Semantic commit messages](https://www.conventionalcommits.org/)
    * Purposful add human and machine readable meaning to commit messages
  * [ ] Adhere to [Docker BP](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
  * [ ] Adhere to BP from [The Hitchhiker's Guide to Python!](https://docs.python-guide.org/)

Inspirations [↑](#toc)
---

* While-True-Do.io [Repo template](https://github.com/whiletruedoio/template)
* Arc-Project [Pydantic](https://github.com/arc-community/arc)
* Mala-Project [Pydoc to Sphinx](https://github.com/mala-project/mala)
* xformers [Conda env file](https://github.com/facebookresearch/xformers)
* Jupyter [Notebook structure](https://github.com/jupyter/notebook)

Resources [↑](#toc)
---

* Development
  * Dave Farley: [Test Driven Development vs Behavior Driven Development](https://www.youtube.com/watch?v=Bq_oz7nCNUA)
  * Dave Farley: [How to Build a DEPLOYMENT PIPELINE? (Continuous Delivery)](https://www.youtube.com/watch?v=x9l6yw1PFbs)
  * Martin Fowler: []()
