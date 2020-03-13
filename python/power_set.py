"""8.4 Power Set: Write a method to return all subsets of a set.
"""
def power_set(array: list)-> list:
    """DP, explore the DAG
    """
    res = []
    def dp(sub, current=[]):
        if not sub: res.append(current); return
        dp(sub[1:], current + [sub[0]])  # we take it
        dp(sub[1:], current)  # or we dont...
    dp(array)
    return res

# test
test = [1,2,3,4]
test = [1,2,3]
print(f'test: {test}, power set: {power_set(test)}')
