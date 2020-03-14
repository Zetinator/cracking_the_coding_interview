"""8.11 Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.
"""
from functools import lru_cache
def coin(n: int)-> int:
    """classic, count the number of stairs problem
    """
    @lru_cache(maxsize=None)
    def r(n):
        if n <= 0: return 0
        if n == 1: return 1
        if n == 5: return r(n-1) + 1
        if n == 10: return r(n-5) + r(n-1) + 1
        if n == 25: return r(n-10) + r(n-5) + r(n-1) + 1
        return sum([r(n-25), r(n-10), r(n-5), r(n-1)])
    return r(n)

# test
test = 75
print(f'ways to give {test}: change: {coin(test)}')
