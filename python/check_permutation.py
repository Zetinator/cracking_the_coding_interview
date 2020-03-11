"""1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
"""
from collections import Counter
def check_permutation(string_1: str, string_2: str)-> bool:
    """naive implementation, multiset
    """
    if not string_1 and not string_2: return True
    s_1 = Counter(string_1)
    s_2 = Counter(string_2)
    return s_1 == s_2

# test
test_1 = "erick"
test_2 = "ricke"
print(f'is permutation? test: {test_1} vs {test_2} ans: {check_permutation(test_1, test_2)}')

