from src.Direction import Direction


def fill_matrix_with_possible_paths(matrix, current_x, current_y, current_z, value,
                                    destination_x, destination_y, destination_z):
    """
    Applies Lee's algorithm and fills the matrix with the distances from the starting point
    :rtype: Filled matrix with possible distances
    """
    print(current_x, current_y, current_z, value)
    if current_x == destination_x and current_y == destination_y and current_z == destination_z:
        return value

    # Check Up
    if current_x - 1 >= 0 and value + 1 < matrix[current_x - 1][current_y][current_z]:
        matrix[current_x - 1][current_y][current_z] = value
        fill_matrix_with_possible_paths(matrix, current_x - 1, current_y, current_z, value + 1,
                                        destination_x, destination_y, destination_z)

    # Check Down
    if current_x + 1 < len(matrix) and value + 1 < matrix[current_x + 1][current_y][current_z]:
        matrix[current_x + 1][current_y][current_z] = value
        fill_matrix_with_possible_paths(matrix, current_x + 1, current_y, current_z, value + 1,
                                        destination_x, destination_y, destination_z)

    # Check Left
    if current_y - 1 >= 0 and value + 1 < matrix[current_x][current_y - 1][current_z]:
        matrix[current_x][current_y - 1][current_z] = value
        fill_matrix_with_possible_paths(matrix, current_x, current_y - 1, current_z, value + 1,
                                        destination_x, destination_y, destination_z)

    # Check Right
    if current_y + 1 < len(matrix[current_y - 1]) and value + 1 < matrix[current_x][current_y + 1][current_z]:
        matrix[current_x][current_y + 1][current_z] = value
        fill_matrix_with_possible_paths(matrix, current_x, current_y + 1, current_z, value + 1,
                                        destination_x, destination_y, destination_z)

    # Check Descend
    # == Directly descending
    if current_z - 1 >= 0 and value + 1 < matrix[current_x][current_y][current_z - 1]:
        matrix[current_x][current_y][current_z - 1] = value
        fill_matrix_with_possible_paths(matrix, current_x, current_y, current_z - 1, value + 1,
                                        destination_x, destination_y, destination_z)

    # == Descending and Up
    if current_z - 1 >= 0 and current_x - 1 >= 0 and value + 1 < matrix[current_x - 1][current_y][current_z - 1]:
        matrix[current_x - 1][current_y][current_z - 1] = value
        fill_matrix_with_possible_paths(matrix, current_x - 1, current_y, current_z - 1, value + 1,
                                        destination_x, destination_y, destination_z)

    # == Descending and Down
    if current_z - 1 >= 0 and current_x + 1 < len(matrix) \
            and value + 1 < matrix[current_x + 1][current_y][current_z - 1]:
        matrix[current_x + 1][current_y][current_z - 1] = value
        fill_matrix_with_possible_paths(matrix, current_x + 1, current_y, current_z - 1, value + 1,
                                        destination_x, destination_y, destination_z)

    # == Descending and Left
    if current_z - 1 >= 0 and current_y - 1 >= 0 and value + 1 < matrix[current_x][current_y - 1][current_z - 1]:
        matrix[current_x][current_y - 1][current_z - 1] = value
        fill_matrix_with_possible_paths(matrix, current_x, current_y - 1, current_z - 1, value + 1,
                                        destination_x, destination_y, destination_z)

    # == Descending and Right
    if current_z - 1 >= 0 and current_y + 1 < len(matrix[current_y - 1]) \
            and value + 1 < matrix[current_x][current_y][current_z - 1]:
        matrix[current_x][current_y + 1][current_z - 1] = value
        fill_matrix_with_possible_paths(matrix, current_x, current_y + 1, current_z - 1, value + 1,
                                        destination_x, destination_y, destination_z)

    # Check Pull
    # == Directly pull
    if current_x == 0 and current_y == 12 and current_z == 7:
        print(current_z)

    if current_z + 1 < len(matrix[current_y - 1][current_z + 1]) \
            and value + 1 < matrix[current_x][current_y][current_z + 1]:
        matrix[current_x][current_y][current_z + 1] = value
        fill_matrix_with_possible_paths(matrix, current_x, current_y, current_z + 1, value + 1,
                                        destination_x, destination_y, destination_z)

    # == Pull and Up
    if current_z + 1 < len(matrix[current_y - 1][current_z + 1]) and current_x - 1 > 0 \
            and value + 1 < matrix[current_x - 1][current_y][current_z + 1]:
        matrix[current_x - 1][current_y][current_z + 1] = value
        fill_matrix_with_possible_paths(matrix, current_x - 1, current_y, current_z + 1, value + 1,
                                        destination_x, destination_y, destination_z)

    # == Pull and Down
    if current_z + 1 < len(matrix[current_y - 1][current_z + 1]) and current_x + 1 < len(matrix) \
            and value + 1 < matrix[current_x + 1][current_y][current_z + 1]:
        matrix[current_x + 1][current_y][current_z + 1] = value
        fill_matrix_with_possible_paths(matrix, current_x + 1, current_y, current_z + 1, value + 1,
                                        destination_x, destination_y, destination_z)

    # == Pull and Left
    if current_z + 1 < len(matrix[current_y - 1][current_z + 1]) and current_y - 1 >= 0 \
            and value + 1 < matrix[current_x][current_y - 1][current_z + 1]:
        matrix[current_x][current_y - 1][current_z + 1] = value
        fill_matrix_with_possible_paths(matrix, current_x, current_y - 1, current_z + 1, value + 1,
                                        destination_x, destination_y, destination_z)

    # == Pull and Right
    if current_z + 1 < len(matrix[current_y - 1][current_z + 1]) and current_y + 1 < len(matrix[current_y - 1]) \
            and value + 1 < matrix[current_x][current_y + 1][current_z + 1]:
        matrix[current_x][current_y + 1][current_z + 1] = value
        fill_matrix_with_possible_paths(matrix, current_x, current_y + 1, current_z + 1, value + 1,
                                        destination_x, destination_y, destination_z)


def get_shortest_path(matrix, destination_x, destination_y, destination_z):
    """
    Creates a list with the shortest directions from the start to the destination
    :rtype: list of Directions
    """
    path = []
    distance = matrix[destination_x][destination_y][destination_z]

    current_x, current_y, current_z = destination_x, destination_y, destination_z

    # Every move is mirrored
    while distance:
        # Go down
        if matrix[current_x - 1][current_y][current_z] == distance - 1:
            path.append(Direction.DOWN)
            current_x -= 1

        # Go up
        elif matrix[current_x + 1][current_y][current_z] == distance - 1:
            path.append(Direction.UP)
            current_x += 1

        # Go right
        elif matrix[current_x][current_y - 1][current_z] == distance - 1:
            path.append(Direction.RIGHT)
            current_y -= 1

        # Go left
        elif matrix[current_x][current_y + 1][current_z] == distance - 1:
            path.append(Direction.LEFT)
            current_y += 1

        # Descend
        elif matrix[current_x][current_y][current_z + 1] == distance - 1:
            path.append(Direction.DESCEND)
            current_z += 1

        # == Descend down
        elif matrix[current_x - 1][current_y][current_z + 1] == distance - 1:
            path.append(Direction.DESCEND_DOWN)
            current_x -= 1
            current_z += 1

        # == Descend up
        elif matrix[current_x + 1][current_y][current_z + 1] == distance - 1:
            path.append(Direction.DESCEND_UP)
            current_x += 1
            current_z += 1

        # == Descend right
        elif matrix[current_x][current_y - 1][current_z + 1] == distance - 1:
            path.append(Direction.DESCEND_RIGHT)
            current_y -= 1
            current_z += 1

        # == Descend left
        elif matrix[current_x][current_y + 1][current_z + 1] == distance - 1:
            path.append(Direction.DESCEND_LEFT)
            current_y += 1
            current_z += 1

        # Pull
        elif matrix[current_x][current_y][current_z - 1] == distance - 1:
            path.append(Direction.PULL)
            current_z -= 1

        # == Pull down
        elif matrix[current_x - 1][current_y][current_z - 1] == distance - 1:
            path.append(Direction.PULL_DOWN)
            current_x -= 1
            current_z -= 1

        # == Pull up
        elif matrix[current_x + 1][current_y][current_z - 1] == distance - 1:
            path.append(Direction.PULL_UP)
            current_x += 1
            current_z -= 1

        # == Pull right
        elif matrix[current_x][current_y - 1][current_z - 1] == distance - 1:
            path.append(Direction.PULL_RIGHT)
            current_y -= 1
            current_z -= 1

        # == Pull left
        elif matrix[current_x][current_y + 1][current_z - 1] == distance - 1:
            path.append(Direction.PULL_LEFT)
            current_y += 1
            current_z -= 1

        distance -= 1

    # Reverse the path
    path.reverse()

    return path
