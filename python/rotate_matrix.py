"""1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. (an you do this in place?
"""
def rotate_matrix(matrix: list)-> list:
    """in place matrix rotation... a classical
    we swap "rings" of the matrix one pixel at the time...
    """
    def swap_node(node_1, node_2):
        """aux function to ease the swap by "nodes", instead of coordinates
        """
        i, j = node_1
        k, l = node_2
        matrix[i][j], matrix[k][l] = matrix[k][l], matrix[i][j]
    # well traverse the matrix by rings (offsets from the main frame)
    rings = len(matrix)//2
    for ring in range(rings):
        for i in range(len(matrix)-1 - ring*2):
            # define spatial nodes
            upper_left = (ring, i + ring)
            upper_right = (i + ring, len(matrix)-1 - ring)
            lower_left = (len(matrix)-1 - i - ring, ring)
            lower_right = (len(matrix)-1 - ring, len(matrix)-1 - i - ring)
            # swap nodes:
            swap_node(upper_left, upper_right)
            swap_node(upper_right, lower_right)
            swap_node(lower_left, lower_right)
    return matrix

# test
t_1 = [
        [0,1],
        [2,3],
        ]
t_1 = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        ]
# => [
        # [2,5,8],
        # [1,4,7],
        # [0,3,6],
        # ]
print(f'rotate_matrix: test: {t_1} ans: {rotate_matrix(t_1)}')
