from src.Direction import Direction


def fill_matrix_with_possible_paths(matrix, current_x, current_y, value, destination_x, destination_y):
    """
    Applies Lee's algorithm and fills the matrix with the distances from the starting point
    :rtype: Filled matrix with possible distances
    """
    if current_x == destination_x and current_y == destination_y:
        return value

    # Check Up
    if current_x - 1 > 0 and value + 1 < matrix[current_x - 1][current_y]:
        matrix[current_x - 1][current_y] = value
        fill_matrix_with_possible_paths(matrix, current_x - 1, current_y, value + 1, destination_x, destination_y)

    # Check Down
    if current_x + 1 < len(matrix) and value + 1 < matrix[current_x + 1][current_y]:
        matrix[current_x + 1][current_y] = value
        fill_matrix_with_possible_paths(matrix, current_x + 1, current_y, value + 1, destination_x, destination_y)

    # Check Left
    if current_y - 1 >= 0 and value + 1 < matrix[current_x][current_y - 1]:
        matrix[current_x][current_y - 1] = value
        fill_matrix_with_possible_paths(matrix, current_x, current_y - 1, value + 1, destination_x, destination_y)

    # Check Right
    if current_y + 1 < len(matrix[current_y - 1]) and value + 1 < matrix[current_x][current_y + 1]:
        matrix[current_x][current_y + 1] = value
        fill_matrix_with_possible_paths(matrix, current_x, current_y + 1, value + 1, destination_x, destination_y)


def get_shortest_path(matrix, destination_x, destination_y):
    """
    Creates a list with the shortest directions from the start to the destination
    :rtype: list of Directions
    """
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
