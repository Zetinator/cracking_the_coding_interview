"""8.2 Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board.
"""
def eight_queens(n: int)-> int:
    eight_queens.BOARD_SIZE = n
    # define a validation function
    def under_attack(column, existing_queens):
        row = len(existing_queens)
        for queen in existing_queens:
            r,c = queen
            if r == row: return True # Check row
            if c == column: return True # Check column
            if (column-c) == (row-r): return True # Check left diagonal
            if (column-c) == -(row-r): return True # Check right diagonal
        return False
    # recurse and conquer
    def solve(n):
        if n == 0: return [[]]
        smaller_solutions = solve(n-1)
        solutions = []
        for solution in smaller_solutions:
            for column in range(eight_queens.BOARD_SIZE):
                # try a new queen to row = n, column = column
                if not under_attack(column , solution):
                    solutions.append(solution + [(n-1,column)])
        return solutions
    return solve(n)

# test
test = 8
print(f'eight_queens {test}x{test}: solutions: {eight_queens(test)}')
queens = [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)]
matrix = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        ]
def paint(nodes, matrix):
    for node in nodes:
        x, y = node
        matrix[x][y] = 1
    return matrix
paint(queens, matrix)
print(f'example:')
for e in matrix: print(e)
