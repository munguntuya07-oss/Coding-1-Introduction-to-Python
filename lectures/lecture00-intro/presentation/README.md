# Coding 1 course introduction

[Open the course introduction slides](course-introduction.pdf).

The opening takes about 20 minutes before setup and programming. It contains 18 main
slides and two reference slides. Instructor information and course administration come
first, followed by the learning goals, Python, and the project workflow.

## Course information

- Six teaching sessions, 16 September to 21 October 2026.
- Five closed-book, multiple-choice quizzes on Moodle in Sessions 2–6 contribute 20%
  of the grade (4% each). They open five minutes after class starts and remain open
  for five minutes: 15:45–15:50 for our 15:40 start. Students must be on time and
  physically present in class when taking the quiz.
- Five in-class assignments in Sessions 2–6 contribute 20%.
- The written, closed-book final exam contributes 60% and takes place on
  Friday, 6 November 2026 at 13:30. It does not replace a teaching session.
- Session 1 is ungraded. Optional practice notebooks are ungraded and uncollected.
- No AI tools for any coursework, including optional practice.

The syllabus and session plan govern the delivery details. Unlike the Stata classroom
setup, Coding 1 uses the supplied course repository and teaches the GitHub submission
workflow. The presentation contains no exam questions or solutions.

## In-class assignment recipe

Slides 6–7 explain the assignment workflow:

1. The instructor keeps each assignment private until it starts, then makes it public
   and pins it on [the instructor's GitHub profile](https://github.com/ulrichwohak).
2. Students open the pinned assignment and fork it to their own GitHub account.
3. Students clone **their own fork** onto their computer. Each new assignment needs a
   new fork and clone. `git pull` only updates an existing local clone.
4. Students open that assignment folder, read the README, and think through the script.
   They follow the task's instructions about when to run it.
5. Students add the requested comments or docstrings and save, keeping executable code
   unchanged. Predict-then-verify tasks require the prediction commit before execution.
6. Students stage, commit, and push their work to their fork before class ends, then
   check on GitHub that the comments arrived. No pull request or email is needed.

Students share their GitHub username in Session 1 so the instructor can identify their
forks. That session's submission practice is ungraded.

**Visibility:** forks of public repositories are public, so classmates can see pushed
answers. Making the original repository private again does not make those forks private.
This release workflow does not provide confidential submissions.
See [GitHub's fork visibility documentation](https://docs.github.com/en/pull-requests/reference/forks).

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
