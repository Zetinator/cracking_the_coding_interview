"""8.8 Permutations with Duplicates: Write a method to compute all permutations of a string whose
characters are not necessarily unique. The list of permutations should not have duplicates.
"""
def permutations(string: str)-> list:
    """recursive solution
    """
    string = list(set(string))
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
test = 'eeeeri'
print(f'permutations of {test}: {permutations(test)}')
