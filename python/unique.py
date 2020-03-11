"""1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""
def unique(string: str)-> bool:
    """naive implementation, memory intensive
    """
    memory = set()
    for e in string:
        if e in memory: return False
        memory.add(e)
    return True

# test
test = "erick quiere mucho a su marion"
test = "unique"
# test = "qwerty"
print(f'is unique? test: {test} ans: {unique(test)}')

