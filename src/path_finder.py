def fill_matrix_with_possible_paths(matrix, x, y, value, destination_x, destination_y):
    """
    :rtype: Filled matrix with possible distances
    """
    if x == destination_x and y == destination_y:
        return matrix

    # Check Up
    if x - 1 > 0 and value + 1 < matrix[x - 1][y]:
        matrix[x - 1][y] = value
        fill_matrix_with_possible_paths(matrix, x - 1, y, value + 1, destination_x, destination_y)

    # Check Down
    if x + 1 < len(matrix) and value + 1 < matrix[x + 1][y]:
        matrix[x + 1][y] = value
        fill_matrix_with_possible_paths(matrix, x + 1, y, value + 1, destination_x, destination_y)

    # Check Left
    if y - 1 >= 0 and value + 1 < matrix[x][y - 1]:
        matrix[x][y - 1] = value
        fill_matrix_with_possible_paths(matrix, x, y - 1, value + 1, destination_x, destination_y)

    # Check Right
    if y + 1 < len(matrix[y - 1]) and value + 1 < matrix[x][y + 1]:
        matrix[x][y + 1] = value
        fill_matrix_with_possible_paths(matrix, x, y + 1, value + 1, destination_x, destination_y)
