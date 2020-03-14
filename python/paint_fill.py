"""8.10 Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.
"""
def bucket_fill(matrix: list, start: tuple, target: int)-> list:
    """the classics
    """
    # define valid functions
    row, column = start
    base = matrix[row][column]
    def valid(node):
        row, column = node
        if not 0 <= row < len(matrix) or not 0 <= column < len(matrix[0]): return False
        if matrix[row][column] != base: return False
        return True
    # define movements
    moves = {
            'up': lambda node: (node[0]-1, node[1]),
            'down': lambda node: (node[0]+1, node[1]),
            'left': lambda node: (node[0], node[1]-1),
            'right': lambda node: (node[0]-1, node[1]+1),
            }
    # propagate with standard bfs
    frontier = [start]
    while frontier:
        _next = []
        for node in frontier:
            # apply paint, ensure no revisiting
            row, column = node
            matrix[row][column] = target
            # explore valid neighbors
            for k, move in moves.items():
                next_node = move(node)
                row, column = next_node
                if valid(next_node): _next.append(next_node)
        frontier = _next
    return matrix

# test
test = [
        [0,0,0,0,2,0,0,0],
        [0,0,0,0,2,0,0,0],
        [0,0,0,2,2,0,0,0],
        [0,0,0,2,2,0,0,0],
        [0,0,0,0,2,0,0,0],
        [0,0,0,0,2,0,0,0],
        ]

print(f'test with:')
for e in test: print(e)
print(f'ans: ')
res = bucket_fill(test, (0,0), 1)
for e in res: print(e)
