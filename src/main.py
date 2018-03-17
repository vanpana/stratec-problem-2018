import copy

import sys

from src.file_worker import read_from_file, save_to_file
from src.path_finder import fill_matrix_with_possible_paths, get_shortest_path

if __name__ == '__main__':
    sys.setrecursionlimit(6000)

    # Read the data from file
    no_rows, no_cols, no_height, matrix, no_routes, routes = read_from_file("../data/data.in")

    # Calculate shortest route for every pair
    for route in routes:
        # Backup the original matrix for reuse
        route_matrix = copy.deepcopy(matrix)

        # Mark the starting point
        route_matrix[route.start_x][route.start_y][route.start_z] = 0
        route_matrix[route.destination_x][route.destination_y][route.destination_z] = no_rows * no_cols * no_height

        # Fill the matrix with the distances from the start point to the destination
        fill_matrix_with_possible_paths(route_matrix, route.start_x, route.start_y, route.start_z, 1,
                                        route.destination_x, route.destination_y, route.destination_z)

        # Build the solution string
        solution = str(route.index) + "\n"
        for direction in get_shortest_path(route_matrix, route.destination_x, route.destination_y, route.destination_z):
            solution += direction.value + " "

        print(solution)

        # Append the solution to the output file
        save_to_file("../data/data.out", solution)
