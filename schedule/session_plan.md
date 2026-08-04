# Coding 1 2026 Session Plan

**ECBS5208 Coding 1: Introduction to Python**, Fall term 2026-2027.

Six sessions, Wednesdays 15:40-17:20 (100 minutes), 16 September to 21 October 2026. Dates
and times are taken from the TimeEdit allocation for `ECBS5208A_T1_2026`, Group A. Room TBC.

There is no reading week inside the course: the six sessions run on six consecutive
Wednesdays. No final exam slot has been allocated yet.

| Session | Date | Topic | Lecture materials | In-class exercises |
| --- | --- | --- | --- | --- |
| 1 | Wed 16 Sep | Setup and general coding principles | `lectures/lecture00-intro`, `lectures/lecture01-coding-basics` | `lecture01-coding-basics-i`, `lecture01-coding-basics-ii` |
| 2 | Wed 23 Sep | Basic data structures and file I/O | `lectures/lecture02-basic-structures`, `lectures/lecture03-data-IO` | `lecture02-basic-structures-i`, `lecture02-basic-structures-ii`, `lecture03-data-io-i`, `lecture03-data-io-ii` |
| 3 | Wed 30 Sep | Data containers: pandas | `lectures/lecture04-pandas-basics` | `lecture04-pandas-basics-i`, `lecture04-pandas-basics-ii`, `lecture04-pandas-munging-i`, `lecture04-pandas-munging-ii` |
| 4 | Wed 7 Oct | Plotting (matplotlib first, then plotnine) and control flow | `lectures/lecture05-graphs-basics`, `lectures/lecture06-conditionals` | `lecture05-matplotlib`, `lecture05-plotnine-i`, `lecture05-plotnine-ii`, `lecture06-control-flow-i`, `lecture06-control-flow-ii` |
| 5 | Wed 14 Oct | Functions, exception handling, descriptive statistics | `lectures/lecture08-functions`, `lectures/lecture09-exception-handling`, `lectures/lecture07-data-exploration` (part 1) | `lecture08-functions-i`, `lecture08-functions-ii`, `lecture09-exceptions`, `lecture07-data-exploration-i` |
| 6 | Wed 21 Oct | Association, hypothesis tests, wrap-up | `lectures/lecture07-data-exploration` (part 2); optional `lectures/lecture10-intro-to-regression` | `lecture07-data-exploration-ii`; optional `lecture10-regression-i`, `lecture10-regression-ii` |

## Open tasks

- **No assessment materials exist yet.** The grading scheme requires 5 quizzes (20%), 4
  homework assignments (20%), and a closed-book final (60%). None of these are written. The
  repository contains no quiz, homework, assignment, or exam file of any kind.
- **Homework runs in Sessions 2-5 only.** Session 1 is setup and orientation, so no homework
  is set; the four assignments are issued at the end of Sessions 2, 3, 4, and 5, at 5% each.
- **Homework seeds are partial.** Seven lecture READMEs carry short upstream practice
  prompts under `## Homework` — lecture02, lecture03, lecture04, lecture07, lecture08,
  lecture09, lecture10. Coverage against the four homework sessions:

  | Session | Lectures | Homework seed available? |
  | --- | --- | --- |
  | 2 | lecture02, lecture03 | Yes, two prompts |
  | 3 | lecture04 | Yes, one prompt |
  | 4 | lecture05, lecture06 | No — neither README has a `## Homework` section |
  | 5 | lecture07, lecture08, lecture09 | Yes, three prompts |

  Session 4 is the only one needing an assignment written from scratch. Note that
  lecture08's prompt is written to be done together with lecture06, so the bootstrap
  exercise could be split to cover Session 4's control-flow material.
- **Seed prompts point at external OSF downloads.** Several reference OSF URLs directly
  rather than `data/raw/` after `scripts/fetch_data.py`; they need rewriting to the
  repository's local-data convention before being issued.
- **Submission platform is a placeholder.** The syllabus says assignments are distributed
  and submitted through "the CEU online course platform" without naming it. The instructor
  will confirm the actual system; update the syllabus then.

## Notes

- **Exercise filenames follow the lecture, not the session.** Exercises are named
  `lectureNN-topic.ipynb`, matching the `lectures/lectureNN-*` directory they practise.
  Sessions bundle several lectures, so one session draws on several prefixes; use the table
  above to see which. This decoupling is deliberate: session packing may change, but an
  exercise always belongs to its lecture.
- **Session 4 order.** matplotlib is taught before plotnine so students see the explicit
  `Figure`/`Axes` model before the grammar-of-graphics abstraction.
- **Session 5 splits `lecture07`.** The natural breakpoints in that lecture are
  hypothesis-testing and association; part 1 stops before hypothesis testing.
- **Regression is optional** and not examinable in Coding 1. It previews Coding 2
  (ECBS5306).
- **SQL is not taught in this course.** `lectures/lecture01-coding-basics/README.md`,
  `lectures/lecture02-basic-structures/`, and `exercises/lecture01-coding-basics-ii.ipynb`
  still contain SQL string-building examples inherited from the upstream material; they are
  not part of the syllabus.
