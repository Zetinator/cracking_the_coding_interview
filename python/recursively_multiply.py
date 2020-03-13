"""8.5 Recursive Multiply: Write a recursive function to multiply two positive integers without using
the * operator (or / operator) . You can use addition, subtraction, and bit shifting, but you should
minimize the number of those operations.
"""
from functools import lru_cache

def multiply(n1: int, n2: int)-> int:
    """naive O(n)
    """
    if n1 < n2: n1, n2 = n2, n1
    @lru_cache(maxsize=None)
    def r(n1, n2, res=0):
        if n2 == 0: return res
        return r(n1, n2-1, res+n1)
    return r(n1, n2)

def multiply(n1: int, n2: int)-> int:
    """O(lg(n)), stack in powers of 2
    """
    if n1 > n2: n1, n2 = n2, n1
    @lru_cache(maxsize=None)
    def r(n1, n2):
        print(f'status: n1: {n1}, n2: {n2}')
        if n1 == 0: return 0
        if n1 == 1: return n2
        res = r(n1 >> 1, n2)
        if n1%2 == 0: return res + res
        else: return res + res + n2
    return r(n1, n2)

# test
t_1 = 5
t_2 = 8
print(f'multiply {t_1} vs {t_2}, multiply: {multiply(t_1, t_2)}')
