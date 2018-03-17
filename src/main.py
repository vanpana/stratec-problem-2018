import copy

from src.file_worker import read_from_file, save_to_file
from src.path_finder import fill_matrix_with_possible_paths, get_shortest_path

if __name__ == '__main__':
    # Read the data from file
    no_rows, no_cols, matrix, no_routes, routes = read_from_file("../data/data.in")

    for route in routes:
        route_matrix = copy.deepcopy(matrix)
        route_matrix[route.start_x][route.start_y] = 0
        fill_matrix_with_possible_paths(route_matrix, route.start_x, route.start_y, 1, route.destination_x, route.destination_y)

        solution = str(route.index) + "\n"
        for direction in get_shortest_path(route_matrix, route.destination_x, route.destination_y):
            solution += direction.value + " "

        save_to_file("../data/data.out", solution)
