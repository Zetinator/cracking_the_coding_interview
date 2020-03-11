"""1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""
from functools import lru_cache
def one_away(string_1: str, string_2: str)-> bool:
    """DP, classic edit distance
    funny move, we calculate the LCS and then substract from the len() of the biggest string in O(n*m)
    """
    if string_1 == string_2: return False
    @lru_cache(maxsize=1024)
    def dp(s_1, s_2, distance=0):
        """standard longest common substring
        """
        if not s_1 or not s_2: return distance
        if s_1[0] == s_2[0]: 
            return dp(s_1[1:], s_2[1:], distance+1)
        return max(dp(s_1[1:], s_2, distance), dp(s_1, s_2[1:], distance))
    return max(len(string_1), len(string_2)) - dp(string_1, string_2) == 1

# test
t_1 = "pale"
t_2 = "bake"
print(f'is one_away? test: {t_1} vs {t_2} ans: {one_away(t_1, t_2)}')
