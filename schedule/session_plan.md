# Coding 1 2026 Session Plan

**ECBS5208 Coding 1: Introduction to Python**, Fall term 2026-2027.

Six sessions, Wednesdays 15:40-17:20 (100 minutes), 16 September to 21 October 2026. Dates
and times are taken from the TimeEdit allocation for `ECBS5208A_T1_2026`, Group A. Room TBC.

There is no reading week inside the course: the six sessions run on six consecutive
Wednesdays. No final exam slot has been allocated yet.

| Session | Date | Topic | Lecture materials | Graded exercise | Voluntary practice (at home) |
| --- | --- | --- | --- | --- | --- |
| 1 | Wed 16 Sep | Setup and general coding principles | `lectures/lecture00-intro`, `lectures/lecture01-coding-basics` | none - Git walkthrough and practice commit | `lecture01-coding-basics-i`, `lecture01-coding-basics-ii` |
| 2 | Wed 23 Sep | Basic data structures and file I/O | `lectures/lecture02-basic-structures`, `lectures/lecture03-data-IO` | predict-then-verify on dict/set operations | `lecture02-basic-structures-i`, `lecture02-basic-structures-ii`, `lecture03-data-io-i`, `lecture03-data-io-ii` |
| 3 | Wed 30 Sep | Data containers: pandas | `lectures/lecture04-pandas-basics` | name the concept over a pandas pipeline | `lecture04-pandas-basics-i`, `lecture04-pandas-basics-ii`, `lecture04-pandas-munging-i`, `lecture04-pandas-munging-ii` |
| 4 | Wed 7 Oct | Plotting (matplotlib first, then plotnine) and control flow | `lectures/lecture05-graphs-basics`, `lectures/lecture06-conditionals` | comment a figure script layer by layer; annotate loop state | `lecture05-matplotlib`, `lecture05-plotnine-i`, `lecture05-plotnine-ii`, `lecture06-control-flow-i`, `lecture06-control-flow-ii` |
| 5 | Wed 14 Oct | Functions, exception handling, descriptive statistics | `lectures/lecture08-functions`, `lectures/lecture09-exception-handling`, `lectures/lecture07-data-exploration` (part 1) | docstring three functions; explain a raised exception | `lecture08-functions-i`, `lecture08-functions-ii`, `lecture09-exceptions`, `lecture07-data-exploration-i` |
| 6 | Wed 21 Oct | Association, hypothesis tests, wrap-up | `lectures/lecture07-data-exploration` (part 2); optional `lectures/lecture10-intro-to-regression` | name the concept over correlation and bin-scatter | `lecture07-data-exploration-ii`; optional `lecture10-regression-i`, `lecture10-regression-ii` |

## Open tasks

- **No assessment materials exist yet.** The grading scheme requires 5 quizzes (20%), 5
  code-reading exercise repositories (20%), and a closed-book final (60%). None are written.
- **Five template repositories to build**, one per graded session. Each holds a README with
  the task, a 25-40 line uncommented `.py` script using that session's concepts, and a
  rubric. Use `.py` rather than `.ipynb`: a comment-only change to a notebook produces an
  unreadable JSON diff, whereas in a script `git diff` shows exactly the added lines, so
  grading is reading a diff.
- **Distribution mechanism undecided.** Per-student repositories need creating, collecting,
  and timestamping. GitHub Classroom is the obvious candidate and would remove the
  "send me the link" step, but its current setup flow needs checking before committing to
  it. Cohort size is the deciding input and is not yet known.
- **Git is a hard prerequisite from Session 2.** `lecture00` currently covers only why
  version control matters, not how to use it. Session 1 must now teach clone, commit, and
  push, and get GitHub authentication working for every student; authentication is the part
  that will eat the clock. A browser-based fallback (editing and committing in the GitHub
  web UI) avoids local setup entirely if the room runs short.
- **AI carve-out is deliberate.** The voluntary practice notebooks are not collected and
  carry no marks, so AI use there is permitted. The prohibition binds the quizzes, the
  code-reading exercises, and the final exam. Note this diverges from the study guide's
  blanket wording, which says AI is not allowed in the course at all.
- **Registrar wording.** The study guide calls the 20% component "Homework submissions".
  Nothing is now submitted from home. The weight is unchanged, but the label should either
  be reworded with the registrar or left as the formal name for the component.

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
