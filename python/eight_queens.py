"""8.2 Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board.
"""
from functools import lru_cache
def eight_queens(n: int)-> int:
    """the classical... no shortcuts, just DP
    """
    eight_queens.SIZE = n
    def valid(state, node):
        row, column = node
        if not row < eight_queens.SIZE or not column < eight_queens.SIZE: return False
        for node in state:
            row_d = abs(node[0] - node[0])
            column_d = abs(node[1] - node[1])
            if row_d == 0 or column_d == 0 or row_d == column_d: return False
        return True
    def r(node, state=(0,[])):
        row, column = node
        n_queens, queens = state
        if row == eight_queens.SIZE: return state
        ans = []
        for c in range(eight_queens.SIZE):
            print(f'status: from: {node}, state: {state}')
            if valid(queens, (row, c)): 
                ans.append(r((row+1, c), (n_queens+1, queens+[node])))
        return max(ans, key=lambda state: state[0])
    state = r((0,0))
    return state

# test
test = 8
print(f'eight_queens {test}x{test}: solution: {eight_queens(test)}')
