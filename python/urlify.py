"""1.3 URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
"""
def urlify(string: str)-> str:
    """naive implementation, linear scan, string builder
    one liner: string.replace(' ', '%20')
    """
    if not string: return string
    string = list(string)
    for i,e in enumerate(string):
        if e == ' ': string[i] = '%20'
    return ''.join(string)

# test
test = "erick quiere mucho a su marion :("
print(f'is permutation? test: {test} ans: {urlify(test)}')

