"""8.9 Parens: Implement an algorithm to print all valid (Le., properly opened and closed) combinations
of n pairs of parentheses.
"""
from functools import lru_cache
def generate_parens(n: int)-> list:
    res = []

    @lru_cache(maxsize=None)
    def r(left, right, current=''):
        if left < 0 or right < left: return
        if left == right == 0: res.append(current); return
        r(left-1, right, current + '(')
        r(left, right-1, current + ')')
    r(n, n)
    return res

# test
test = 4
print(f'possible parenthesis of {test}: {generate_parens(test)}')
