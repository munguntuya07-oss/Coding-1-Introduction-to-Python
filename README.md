# Coding 1: Introduction to Python

Course materials for **ECBS5208 Coding 1: Introduction to Python** at CEU, Department of
Economics. The course runs from **September 16, 2026** to **October 21, 2026**.

The full syllabus is in
[`Coding-1-Introduction-to-Python-Syllabus.md`](Coding-1-Introduction-to-Python-Syllabus.md).

## Course Overview

Coding 1 is an introductory programming course for students who are learning to use Python for data management and data analysis. The course focuses on general coding principles, Python syntax, reproducible project workflows, and environment management with `uv`.

The goal is to build a solid programming foundation before students move on to more advanced analytics work. Students will practice writing, reading, debugging, and organizing code in notebooks and small scripts while working with realistic tabular datasets.

This course will **not** use artificial intelligence tools or large language models. The subsequent course will actively use AI and LLMs, but Coding 1 deliberately focuses on programming basics first: understanding code, controlling the Python environment, manipulating data, and reasoning through errors without AI assistance.

## Course Structure

The course meets once per week for 100 minutes, on Wednesdays 15:40-17:20, for six sessions. The ordered plan is in `schedule/session_plan.md`.

The first sessions introduce the Python working environment, notebooks, variables, expressions, strings, core data structures, and file I/O. The middle sessions develop pandas, data cleaning, visualization, and control flow. The final sessions cover functions, exceptions, and exploratory data analysis. Introductory regression is optional material that previews Coding 2.

## Course Materials

- `lectures/`: adapted lecture notebooks from `lecture00-intro` through `lecture10-intro-to-regression`
- `exercises/`: short 10-20 minute practice notebooks for substantive class sessions
- `data/README.md`: dataset inventory and external source notes
- `scripts/fetch_data.py`: dataset fetch script for external OSF data used by selected lectures
- `scripts/check_no_pip.py`: validation script that keeps student-facing materials on the `uv` workflow
- `scripts/check_notebooks.py`: notebook validation for JSON, kernel metadata, imports, syntax, and local data references
- `schedule/session_plan.md`: ordered session plan for the 2026 course
- `Coding-1-Introduction-to-Python-Syllabus.md`: the course syllabus, aligned with the CEU study guide entry for ECBS5208

## Learning Outcomes

By the end of Coding 1, students should be able to:

- Work with a Python project environment managed by `uv`.
- Use JupyterLab notebooks as a structured environment for exploratory coding.
- Write clear Python code using variables, expressions, strings, functions, and common data structures.
- Read from and write to local files using reliable paths and basic encoding awareness.
- Load, inspect, clean, filter, transform, and summarize tabular data with pandas.
- Create basic visualizations with plotnine and matplotlib.
- Use conditionals, loops, comprehensions, and functions to make code reusable.
- Handle common data workflow failures with defensive coding and exceptions.
- Carry out introductory exploratory data analysis, including descriptive statistics, distributions, association, and simple hypothesis-test workflows.
- Estimate and interpret introductory regression models using Python.

## Pedagogical Position

Coding 1 is intentionally about fundamentals. Students are expected to develop enough fluency to understand what their code does, why errors happen, and how to evaluate data workflow results. AI-assisted programming is useful in later work, but this course first builds the baseline programming literacy needed to use those tools responsibly.

## Attribution

Selected lecture materials are adapted from the MIT-licensed `gabors-data-analysis/da-coding-python` course materials. See `NOTICE.md` for details.

## AI Attribution

AIA HAb SeCeNc Hin R GPT-5.5 Opus4.7 v1.0

This statement documents how this repository was created. It does not change the course policy: students in Coding 1 will not use artificial intelligence tools or large language models for course work.
