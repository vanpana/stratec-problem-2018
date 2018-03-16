def fill_matrix_with_possible_paths(matrix, x, y, value, destination_x, destination_y):
    """
    :rtype: Filled matrix with possible distances
    """
    print(matrix)

    # Check Left
    if x - 1 > 0 and value + 1 <= matrix[x - 1][y]:
        matrix[x - 1][y] = value
        fill_matrix_with_possible_paths(matrix, x - 1, y, value + 1, destination_x, destination_y)

    # Check Right
    if x + 1 < len(matrix) and value + 1 <= matrix[x][y + 1]:
        matrix[x + 1][y] = value
        fill_matrix_with_possible_paths(matrix, x + 1, y, value + 1, destination_x, destination_y)

    # Check Down
    if y - 1 > 0 and value + 1 <= matrix[x][y - 1]:
        matrix[x][y - 1] = value
        fill_matrix_with_possible_paths(matrix, x, y - 1, value + 1, destination_x, destination_y)

    # Check Up
    if y + 1 < len(matrix[y]) and value + 1 <= matrix[x][y+1]:
        matrix[x][y+1] = value
        fill_matrix_with_possible_paths(matrix, x, y + 1, value + 1, destination_x, destination_y)