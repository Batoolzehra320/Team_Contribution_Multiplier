# Team Contribution Multiplier

##  Problem Overview

You are part of a software engineering team working on a group project.

Each team member contributes a performance score, which may be:
- Positive
- Negative
- Zero

Your task is to analyze the impact of each team member by calculating the total team performance if that member takes a break.

##  Problem Statement

You are given an integer array called `contributions`, where:

- `contributions[i]` represents the contribution score of the `i-th` team member.

Create a new array `impact` such that:
impact[i] = product of all contributions except contributions[i]

##  Constraints

- Do NOT use division.
- Time complexity should be O(n).
- Extra space (excluding output array) should be O(1).

##  Example
### Input
```python
contributions = [1, 2, 3, 4]
impact = [24, 12, 8, 6]
