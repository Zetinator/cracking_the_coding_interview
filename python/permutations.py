"""8.7 Permutations without Dups: Write a method to compute all permutations of a string of unique
characters.
"""
def permutations(string: str)-> list:
    """recursive solution
    """
    def r(sub_string):
        if len(sub_string) == 1: return sub_string
        ans = []
        first, remainder = sub_string[0], sub_string[1:]
        for permutation in r(remainder):
            for i in range(len(sub_string)):
                ans.append(permutation[:i] + first + permutation[i:])
        return ans
    return r(string)

# test
test = 'eri'
print(f'permutations of {test}: {permutations(test)}')
print(f'ground truth: ')
from itertools import permutations
for e in permutations(test, len(test)): print(e, end=' ')
