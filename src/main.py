from src.file_worker import read_from_file
from src.path_finder import fill_matrix_with_possible_paths

if __name__ == '__main__':
    # Read the data from file
    no_rows, no_cols, matrix, no_routes, routes = read_from_file("../data/data.in")

    for route in routes:
        fill_matrix_with_possible_paths(matrix, route.start_x, route.start_y, 0, route.destination_x, route.destination_y)
        for line in matrix:
            for col in line:
                print(col, end="")
            print()
