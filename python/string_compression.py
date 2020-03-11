"""1.6 String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""
def string_compression(string: str)-> str:
    """2 stacks, one for the counting of the symbols and one as a string builder
    """
    res, stack = [], []
    for e in string:
        # no stack? then start appending
        if not stack: stack.append(e); continue
        # repetitions get pushed in
        if e == stack[0]: stack.append(e)
        # changes flush the repetitions into the compressed notation
        else:
            res.append(f'{stack[0]}{len(stack)}')
            stack = [e]
    # any remeinders? flush them
    if stack: res.append(f'{stack[0]}{len(stack)}')
    return ''.join(res)

# test
t_1 = "aabcccccaaa"
print(f'is string_compression? test: {t_1} ans: {string_compression(t_1)}')
