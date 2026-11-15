# CS3346A Assignment 2 student code

Python 3.10 or later. No dependencies, internet, model downloads, or API keys.
Open a terminal in this extracted folder. On Windows, `py -3` can replace
`python`; on macOS/Linux, use `python3` if `python` is unavailable.

1. Read the assignment PDF. Complete the two functions in `student_algorithms.py`.
2. Run `python -m unittest -v tests_public.py`.
3. Run `python run_assignment.py --out results.json`.
4. Submit your written report, `student_algorithms.py`, and `results.json`, using
   the Brightspace submission instructions. Include any extra tests you wrote.

The initial stubs deliberately raise NotImplementedError. The two public checks
fail until you implement the functions; that is expected. Passing these checks
does not establish full correctness. Keep all probability mass, use synchronous
sweeps, and handle a true terminal before considering next-state Q values.

The runtime reports approximations, a stopping delta and a fresh Bellman residual.
Do not label finite-precision output as the exact optimal value. Deterministic
updates require no random seed. The provided code aggregates multiple bounce
outcomes and represents cells by one-based (row,column) tuples.
