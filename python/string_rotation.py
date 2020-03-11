"""1.9 String Rotation: Assume you have a method isSubst ring which checks if one word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
"""
def string_rotation(string_1: str, string_2: str)-> bool:
    return string_2 in string_1 + string_1

# test
t_1 = "waterbottle"
t_2 = "erbottlewat"
print(f'string_rotation: test: {t_1} vs {t_2}, ans: {string_rotation(t_1, t_2)}')
