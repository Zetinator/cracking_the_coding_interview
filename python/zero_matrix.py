"""1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O
"""
def zero_matrix(matrix: list)-> list:
    # deep copy of matrix
    def zero_row(index):
        for j in range(len(matrix)):
            tmp[index][j] = 0
    def zero_column(index):
        for i in range(len(matrix)):
            tmp[i][index] = 0
    tmp = [row[:] for row in matrix]
    for i, row in enumerate(matrix):
        for j, e in enumerate(row):
            if e == 0: zero_row(i); zero_column(j)
    return tmp

# test
t_1 = [
        [9,1,2],
        [3,0,5],
        [6,7,8],
        ]
print(f'zero_matrix: test: {t_1} ans: {zero_matrix(t_1)}')
