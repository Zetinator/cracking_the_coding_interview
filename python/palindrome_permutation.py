"""1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""
from collections import Counter
def palindrome_permutation(string: str)-> bool:
    """naive implementation, multiset
    """
    if not string: return True
    preprocessed = string.lower().replace(' ','')
    chance = True if not len(preprocessed)%2 == 0 else False
    counter = Counter(preprocessed)
    for e in counter.values():
        if not e%2 == 0:
            if not chance: return False
            else: chance = False
    return True

# test
test = "erick quiere mucho a su marion :("
test = "Tact Coa"
print(f'is palindrome_permutation? test: {test} ans: {palindrome_permutation(test)}')
