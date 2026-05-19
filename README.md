# Math Investigative Task 2026: Using Sequences and Series to Design an IPPT Training Planner

## Core Idea

Create a training planner where a user enters:
- current ability
- target score
- number of weeks

The tool then uses mathematical sequences to generate a gradual training plan.

### Push-ups and sit-ups: arithmetic sequence

$$
u_n​=a+(n−1)d
$$

where:
- $u_n$ = target number of repetitions in week $n$
- $a$ = starting number of repetitions
- $d$ = weekly increase in repetitions
- $n$ = week number

If the user has a starting ability of $a$ reps and wants to reach a target of $T$ reps in $N$ weeks, the weekly increase can be calculated using:

$$
d = \frac{T - a}{N - 1}
$$

### Running: geometric sequence

For 2.4 km run, a geometric sequence can be used to model percentage-based improvement. This is more realistic as improvement becomes harder the better one's timing is.

$$
u_n = ar^{n - 1}
$$

where:
- $u_n$ = target 2.4 km timing in week $n$
- $a$ = starting timing
- $r$ = common ratio ($0 < r < 1$)
- $n$ = week number

If the user starts with a timing of $a$ seconds and wants to reach a target timing of $T$ seconds in $N$ weeks, then:

$$
T = ar^{N - 1}
$$

Rearranging to find the common ratio:

$$
r = \left(\frac{T}{a}\right)^{\frac{1}{N - 1}}
$$

## Website Structure

### User input (sliders + text field)

- current number of push-ups
- current number of sit-ups
- current 2.4 km run timing (mm:ss)
- target number of push-ups
- target number of sit-ups
- target 2.4 km run timing (mm:ss)
- number of training weeks

Display current score, target score, and suggest target 2.4km time to reach the next grade (if applicable)

### Output Table

The website should display the generated plan in a clear table.

Example:

| Week | Push-up Target | Sit-up Target | 2.4 km Target Timing |
|---|---:|---:|---:|
| 1 | 25 | 35 | 15:00 |
| 2 | 28 | 37 | 14:44 |
| 3 | 30 | 39 | 14:28 |
| ... | ... | ... | ... |

The table should make it easy for the user to follow their weekly targets.

## Realism Check

The website warns users if their target may be too difficult within the given number of weeks, by flagging at the bottom of the table when the user's goals could be unreasonable.
