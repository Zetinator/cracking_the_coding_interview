"""8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
"""
def robot(matrix: list)-> list:
    """O(n*m)
    bfs, with no revisiting
    """
    if not matrix or not matrix[0]: return
    # define valid set of positions in the matrix
    def valid(node):
        row, column = node
        if not 0 <= row < len(matrix) or not 0 <= column < len(matrix[0]): return False
        if matrix[row][column] == 1: return False
        return True
    # define set of movements
    moves = {
            'right': lambda node: (node[0], node[1]+1),
            'down': lambda node: (node[0]+1, node[1]),
            }
    # execute standard bfs
    start, end = (0,0), (len(matrix)-1, len(matrix[0])-1)
    visited = set(start)
    frontier = [start]
    while frontier:
        _next = []
        for node in frontier:
            for k, move in moves.items():
                next_node = move(node)
                if valid(next_node) and next_node not in visited:
                    # match... we are done
                    if next_node == end: return True
                    visited.add(next_node)
                    _next.append(next_node)
        frontier = _next
    # matrix explored and "end" is out of reach
    return False

# test
test = [
        [0,0,0,0,0],
        [0,1,1,1,1],
        [0,1,0,0,0],
        [0,1,0,0,0],
        [0,0,0,0,0],
        ]
print(f'test: {test}, is the end reachable? {robot(test)}')
