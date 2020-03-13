"""8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def triple_step(n: int)-> int:
    """classic, decompose in subproblems + memoization
    """
    # base cases
    if n <= 1: return 1
    if n == 2: return 3
    if n == 3: return 3
    # recurse
    return sum((triple_step(n-1), triple_step(n-2), triple_step(n-3)))

# test
test = 5
print(f'how many ways to run up {test} stairs?: {triple_step(test)}')
