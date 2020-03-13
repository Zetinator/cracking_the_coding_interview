"""8.3 Magic Index: A magic index in an array A [1. .. n -1] is defined to be an index such that A[ i]
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
"""
def magic_index(array: list)-> int:
    """binary search + tweak
    left search: take the min(m-1, array[m])
    right search: take the max(m+1, array[m])
    """
    l,r = 0, len(array)-1
    while l<=r:
        m = (l+r)//2
        print(f'status: l: {l}, r: {r}, m: {m}, array_m: {array[m]}')
        if array[m] == m: return m
        if array[m] < m:
            l = max(m+1, array[m])
        else:
            r = min(m-1, array[m])
    raise KeyError('Not found')

# test
test = [-10,-5,2,2,2,3,4,7,9,12,13]
print(f'test: {test}. magic index: {magic_index(test)}')
