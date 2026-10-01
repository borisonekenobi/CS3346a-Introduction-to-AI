# CS3346A Assignment 1 student code

Python 3.10 or later; standard library only. No pip packages, paid services,
API keys, live data, or GPU are needed. Run commands in this folder.

1. Read the assignment and predict the Part C results before running the code.
2. Complete the two TODO regions in `student_search.py`.
3. Run `python -m unittest -v test_public`.
4. Run `python run_experiments.py`.
5. Open `results/comparison.svg` in a browser; include it in your report with
   your interpretation. The raw measurements are in `results/results.json`.

On macOS/Linux, use `python3` if `python` is unavailable. On Windows, `py -3`
is also suitable. A terminal/IDE is sufficient; Jupyter is optional.

Before completion, some tests fail with NotImplementedError. That is expected.
Public tests are small examples and do not cover all assessed cases.
The assignment specifies valid finite input trees and all tie/visit conventions.
You may create additional tiny practice trees without changing supplied files.

Submit your report PDF, `student_search.py`, and `results.json` in one ZIP.
Only the two TODO regions are assessed as implementation; do not replace
provided data, hard-code tree names/results, import an AI/search library,
or use global state. Keep function signatures unchanged.

The written work earns marks for reasoning even if your implementation is
incomplete. Include partial code and clearly label uncompleted experiments.
Do not fabricate results. Generative AI is not permitted unless Dr. Davis
announces a task-specific exception in class and in writing on Brightspace.
