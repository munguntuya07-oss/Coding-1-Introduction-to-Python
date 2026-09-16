# Coding 1 course introduction

[Open the course introduction slides](course-introduction.pdf).

The opening takes about 18 minutes before setup and programming. It contains 16 main
slides and two reference slides. Instructor information and course administration come
first, followed by the learning goals, Python, and the project workflow.

## Course information

- Six teaching sessions, 16 September to 21 October 2026.
- Five quizzes in Sessions 2–6 contribute 20% of the grade.
- Five in-class assignments in Sessions 2–6 contribute 20%.
- The written, closed-book final exam contributes 60% and takes place on
  Friday, 6 November 2026 at 13:30. It does not replace a teaching session.
- Session 1 is ungraded. Optional practice notebooks are ungraded and uncollected.
- No AI tools for any coursework, including optional practice.

The syllabus and session plan govern the delivery details. Unlike the Stata classroom
setup, Coding 1 uses the supplied course repository and teaches the GitHub submission
workflow. The presentation contains no exam questions or solutions.

## Instructor files

- `course-introduction.tex`: editable LaTeX Beamer source with speaking notes and timings.
- `course-introduction.pdf`: slides for projection and student reading.
- `course-introduction-presenter.pdf`: the slides with speaking notes on the right.
- `Makefile`: builds both PDFs with `pdflatex`.

The source, presenter PDF, and Makefile are locally ignored to keep instructor files
separate from the student-facing PDF. Students do not need LaTeX.

From this directory, run `make` to compile into `build/`. Run `make publish` to copy the
compiled PDFs into this directory. This target only copies local files; it does not commit
or push anything. Keep the presenter PDF on the instructor screen.

The deck follows the typography, colours, and 16:9 layout of the Stata introduction.
Content follows the Coding 1 syllabus, with sources in the speaker notes. The notes use
the confirmed six-teaching-session schedule and the separate exam on
Friday, 6 November 2026 at 13:30.
