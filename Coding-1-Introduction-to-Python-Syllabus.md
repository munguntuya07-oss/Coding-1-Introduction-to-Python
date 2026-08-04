# Coding 1: Introduction to Python (ECBS5208)

**Academic year** 2026–2027 · **Term** Fall · **Host unit** Department of Economics
**Course level** 7 · **US credits** 1 · **ECTS credits** 2
**Instructor** Ulrich Wohak, PhD
**Meetings** Wednesdays, 15:40–17:20 · 16 September – 21 October 2026 (6 sessions) · Room TBC
**Course repository** `Coding-1-Introduction-to-Python`

---

## Background and overall aim

**Content.** This course introduces students to the basics of Python programming with a
focus on data handling, visualization, and foundational scripting. It is designed as a
beginner-level coding course specifically for students aiming to analyze and work with
data using Python. The course is built around interactive notebooks and real datasets,
enabling students to learn by doing.

**Relevance.** Python is de facto the lingua franca in data engineering, data science, and
data analytics. Most data solutions are deployed in production environments in Python, so
anyone looking for a position in the data world must be able to code in this language.

**Position in the sequence.** Coding 1 is the foundational course of the coding sequence.
Its purpose is to build the baseline programming literacy that every later course assumes:
reading code, writing it by hand, and reasoning about why it fails. Coding 2 (ECBS5306),
which follows in the same term, builds on this foundation and is where AI-assisted coding
is introduced. See the AI policy below.

## Course prerequisites

- Mathematics pre-session course.
- Students are expected to bring their own laptops to follow the coding classes.

No prior programming experience is assumed. Students should complete the environment setup
described in `lectures/lecture00-intro/setup.md` before or during Session 1.

## Waiting list handling

MS in Business Analytics students and MA in Economics, Data and Policy students have first
priority. All other students will be placed on the waiting list.

## Learning outcomes

**Key outcomes.** By the end of the course, students will be able to:

- Write and debug basic Python programs.
- Use key data structures like lists and dictionaries.
- Read from and write to files.
- Work with structured datasets using pandas.
- Create visualizations using matplotlib and plotnine.
- Use loops, conditionals, and functions to automate tasks.
- Perform exploratory data analysis.

**Other outcomes.** The course will also help develop skills in the following areas:

- *Critical thinking* — reproduce errors and debug broken code.
- *Quantitative reasoning* — break down tasks into manageable components.
- *Technology skills* — learn Python's modelling tools and plotting libraries.
- *Interpersonal communication skills* — ability to interpret and communicate outputs.

**Supporting outcomes specific to this delivery.** Students will additionally be able to
work in a reproducible project environment managed by `uv`, use JupyterLab as a structured
environment for exploratory coding, construct reliable file paths with basic encoding
awareness, and handle common data-workflow failures with defensive coding and exceptions.

## Learning activities and teaching methods

The course will be conducted as a series of interactive lectures during which we go through
concepts and applications together. In addition, students will have in-class quizzes and
homework exercises.

Each session follows the same shape:

1. A short start-of-class quiz on the previous session (from Session 2 onward).
2. Live-coded walkthrough of the session's lecture notebook(s) from `lectures/`.
3. A 10–20 minute in-class practice notebook from `exercises/`, worked individually or in
   pairs, then discussed.
4. The homework assignment for the coming week.

All materials are distributed through the course repository. Students clone the repository,
create the environment with `uv sync`, download external datasets with
`uv run python scripts/fetch_data.py`, and work in JupyterLab. Students type their own code:
notebooks are worked through by hand, not by pasting completed solutions.

## Assessment

Grading will be based on the total score out of 100, in line with CEU Department of
Economics and Business grading guidelines. In particular:

a. The median student can expect to get a B+.
b. Probably not more than 1/3 of the students can expect to get an A or A−.
c. The passing grade is 50%.

The final grade is based on:

| Component | Weight | Detail |
| --- | --- | --- |
| Start-of-the-class quiz | 20% | 5 quizzes at the start of Sessions 2–6, 4% each. Short, closed-book, on the previous session's material. |
| Homework submissions | 20% | 5 assignments, 4% each, issued at the end of Sessions 1–5 and due before the following session. |
| Closed-book final exam | 60% | Written, closed-book, no computer. Covers the whole course. **No exam slot has been allocated yet** — the date will be confirmed with the registrar and announced in class. |

Each homework assignment is short — roughly 10–20 minutes of focused practice on the
session's material — and is graded for completion and for evidence of genuine effort, not
for polish. Assignments are posted in the course repository at the end of each session.

Because the final exam is closed-book and handwritten, in-class practice and homework are
deliberately designed to build recall of syntax rather than reliance on lookup.

## AI policy

**The use of AI is not allowed in this course.**

This course is introductory, and we are mostly going to be learning a lot of basic syntax.
For that reason, the use of AI is not permitted for any part of the course: in-class
exercises, homework submissions, quizzes, or the final exam. You are expected to write your
code by hand, read error messages yourself, and work out what went wrong. That difficulty is
the point — it is where the learning happens, and the closed-book final exam is set on the
assumption that you have done it.

I define "AI" here as LLM and other machine learning methods including ChatGPT, GitHub
Copilot, Bard, Claude, Grammarly, DeepL, and any other available tools. This includes
AI-completion features built into editors: if you use VS Code, disable Copilot and any
inline AI suggestions for your course work.

**This policy is specific to Coding 1, and it changes in the next course.** Coding 2
(ECBS5306) permits AI as an assistant that helps you code and debug faster, rather than as a
substitute for doing the work. The reason for the order is straightforward: you can only
judge whether an AI-generated solution is correct, efficient, or appropriate if you can
already read and write the code yourself. Coding 1 builds that judgment; Coding 2 puts it to
use.

What is permitted in Coding 1: the official documentation for Python, pandas, plotnine, and
matplotlib; the course notebooks; textbooks and course notes; and discussing concepts with
classmates. What is not permitted: generating, completing, translating, or explaining code
with an AI tool.

## Course contents

The course runs over six 100-minute sessions. Lecture material lives in `lectures/`,
in-class practice notebooks in `exercises/`. The two blocks below follow the study guide's
grouping, with one adjustment: plotting is delivered at the start of the second block rather
than the end of the first, so that pandas has a full session of its own.

### Sessions 1–3

**Session 1 — 16 September · Setup and general coding principles**

- Python, JupyterLab, and VS Code; the `uv`-managed project environment; running a script
  from the console; why version control matters and what Git and GitHub offer.
- General coding principles: how to name variables, why and how to comment scripts.
- Variables, assignment, and the primitive types (integers, floats, booleans); expressions
  and operators; string manipulation and formatting.
- Materials: `lectures/lecture00-intro`, `lectures/lecture01-coding-basics`.
- In class: `exercises/session03-coding-basics-i.ipynb`,
  `exercises/session04-coding-basics-ii.ipynb`.

**Session 2 — 23 September · Basic data structures and file I/O**

- The four Python collections: lists, tuples, sets, dictionaries. Inspecting, searching,
  modifying, and iterating; set operations; casting between collection types.
- JSON strings to dictionaries and back; importing modules and writing your own.
- Opening files for reading, reading text line by line, handling encodings; writing,
  appending, and overwriting; working directories, listing files, OS-specific paths,
  creating directories.
- Materials: `lectures/lecture02-basic-structures`, `lectures/lecture03-data-IO`.
- In class: `exercises/session05-basic-structures-i.ipynb` through
  `exercises/session08-data-io-ii.ipynb`.

**Session 3 — 30 September · Data containers: pandas**

- Creating `Series` and `DataFrame`s from series, dictionaries, and lists; access with `loc`
  and `iloc`; resetting the index; renaming columns; reading DataFrame metadata.
- Data munging: adding variables, splitting a character variable, type conversion, string
  methods on Series, filtering and tabulating values, missing values, replacing values,
  handling duplicates, chaining operations, and sorting.
- Data: hotels-vienna, hotels-europe.
- Materials: `lectures/lecture04-pandas-basics`.
- In class: `exercises/session09-pandas-basics-i.ipynb` through
  `exercises/session12-pandas-munging-ii.ipynb`.

### Sessions 4–6

**Session 4 — 7 October · Plotting and control flow**

- matplotlib first: the `Figure` and `Axes` objects, axis limits, legends, log scales, a
  second axis, bar spacing and grids, charts within charts. Students meet the explicit,
  step-by-step plotting model before any higher-level abstraction, so that they know what a
  figure is actually made of.
- plotnine and the grammar of graphics, introduced second as a more compact way to express
  the same ideas: `geoms`, continuous and discrete scales, limits and break points,
  annotation with lines, points and text; bar charts (simple, stacked, percentage), box
  plots, violin plots, colour values.
- Conditionals and control flow: the anatomy of `if`/`else`, `for` loops, `while` loops, and
  list comprehensions.
- Materials: `lectures/lecture05-graphs-basics`, `lectures/lecture06-conditionals`.
- In class, in this order: `exercises/session16-matplotlib.ipynb`,
  `exercises/session14-plotnine-i.ipynb`, `exercises/session15-plotnine-ii.ipynb`,
  `exercises/session17-control-flow-i.ipynb`, `exercises/session18-control-flow-ii.ipynb`.

**Session 5 — 14 October · Functions, exception handling, and descriptive statistics**

- User-defined functions: structure, arguments, return values, docstrings, `help`, `lambda`
  functions, and refactoring repeated code into reusable helpers.
- Exception handling: `try` and `except`, identifying exception types, and selecting actions
  based on the type of error encountered.
- Data exploration, part 1: `describe` and `skim` for quick summaries; means, medians,
  standard deviations, percentiles, counts of missing values; grouped descriptives with
  `groupby` and `agg`; histograms and kernel densities, and the role of bin width and
  bandwidth.
- Materials: `lectures/lecture08-functions`, `lectures/lecture09-exception-handling`,
  `lectures/lecture07-data-exploration` (first part).
- In class: `exercises/session21-functions-i.ipynb`,
  `exercises/session22-functions-ii.ipynb`, `exercises/session23-exceptions.ipynb`,
  `exercises/session19-data-exploration-i.ipynb`.

**Session 6 — 21 October · Association, hypothesis tests, and wrap-up**

- Data exploration, part 2: hypothesis testing with t-tests (two-sided and one-sided,
  and across groups); association between two variables with `cov` and `corr`; scatter
  plots; bin-scatters with equidistant bins and with equal numbers of observations per bin;
  correlations within subgroups.
- Course review and preparation for the closed-book final exam.
- *Optional, time permitting* — a preview of Coding 2: introduction to regression with
  binary means, binscatter, lowess, and a simple linear regression estimated with
  `statsmodels`, including predictions, residuals, and identifying the best and worst hotel
  deals. This material is not examinable in Coding 1.
- Materials: `lectures/lecture07-data-exploration` (second part), and optionally
  `lectures/lecture10-intro-to-regression`.
- In class: `exercises/session20-data-exploration-ii.ipynb`, and optionally
  `exercises/session24-regression-i.ipynb`, `exercises/session25-regression-ii.ipynb`.

## Software and course materials

The course uses Python 3.12 with an environment managed by `uv`. After cloning the
repository:

```bash
uv sync
uv run python scripts/fetch_data.py
uv run jupyter lab
```

Do not use `pip`, `pipenv`, or `%pip`/`!pip` inside notebooks to manage the course
environment; `uv` is the only supported workflow, and the repository's checks enforce this.

Core packages: `pandas`, `numpy`, `plotnine`, `matplotlib`, `scipy`, `statsmodels`,
`skimpy`, `stargazer`, `jupyterlab`.

Datasets are not stored in the repository. `scripts/fetch_data.py` downloads them into
`data/raw/`: hotels-vienna, hotels-europe (prices and features), sp500, and billion-prices.
Sources are documented in `data/README.md`.

## Readings and further material

There is no required textbook. The following are supplementary and optional:

- Békés, G. and Kézdi, G., *Data Analysis for Business, Economics, and Policy* — the source
  of the datasets and case studies used throughout the course.
- Turrell, A., *Coding for Economists* — a useful companion for data exploration.
- The official documentation for Python, pandas, plotnine, and matplotlib. Learning to read
  documentation is itself a course objective.

Individual lecture READMEs list further material specific to each topic.

## Attribution

Selected lecture materials are adapted from the MIT-licensed
`gabors-data-analysis/da-coding-python` course materials, which credit Peter Duronelly,
Adam Vig, Agoston Reguly, and Gabor Bekes. See `NOTICE.md` for details.

## Contact details

Ulrich Wohak, PhD — instructor. Email address and office hours to be announced.
