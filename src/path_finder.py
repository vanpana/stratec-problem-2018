from src.Direction import Direction


def fill_matrix_with_possible_paths(matrix, x, y, value, destination_x, destination_y):
    """
    :rtype: Filled matrix with possible distances
    """
    if x == destination_x and y == destination_y:
        return value

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


def get_shortest_path(matrix, destination_x, destination_y):
    path = []
    distance = matrix[destination_x][destination_y]

    current_x, current_y = destination_x, destination_y

    # Every move is mirrored
    while distance:
        # Go down
        if matrix[current_x - 1][current_y] == distance - 1:
            path.append(Direction.DOWN)
            current_x -= 1

        # Go up
        elif matrix[current_x + 1][current_y] == distance - 1:
            path.append(Direction.UP)
            current_x += 1

        # Go right
        elif matrix[current_x][current_y - 1] == distance - 1:
            path.append(Direction.RIGHT)
            current_y -= 1

        # Go left
        elif matrix[current_x][current_y + 1] == distance - 1:
            path.append(Direction.LEFT)
            current_y += 1

        distance -= 1

    # Reverse the path
    path.reverse()

    return path
