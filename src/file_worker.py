from src.path_finder import accelerate
from src.route import Route


def read_from_file(filename):
    """
    Reads the lines from the file and returns an the matrix dimensions, the integer matrix, the number of routes and
     a list of routes from the read data
    :param filename: The path of the data file
    """
    no_rows = 0
    no_cols = 0
    no_height = 0
    matrix = []

    no_routes = 0
    routes = []
    with open(filename, "r") as file:
        for line in file:
            elements = line.strip("\n").split(" ")

            # Save the number of routes
            if len(elements) == 1:
                no_routes = int(elements[0])

            # Save the number of rows and cols
            elif len(elements) == 3:
                no_rows, no_cols, no_height = int(elements[0]), int(elements[1]), int(elements[2])
                matrix = [[[no_rows * no_cols * no_height for _ in range(no_height)] for _ in range(no_cols)] for _ in range(no_rows)]

            # Save the route
            elif len(elements) == 7:
                routes.append(Route(*elements))

            # Replace any non-zero values with negative one, all zero values with maximum possible value and add the
            # element in the matrix
            else:
                if int(elements[3]) != 0:
                    value = -1

                    # Fill with values from the bottom to the current height so the tube can't pass through
                    for height in range(int(elements[2]) + 1):
                        matrix[int(elements[0])][int(elements[1])][height] = value

    return no_rows, no_cols, no_height, matrix, no_routes, routes


def save_to_file(filename, solution):
    with open(filename, "a") as file:
        file.write(solution + "\n")


def build_solution(route_index, path, acceleration=False):
    """
    Builds the solution (acceleration is optional)
    :rtype: Solution as a string
    """
    solution = ""
    for direction in path:
        solution += direction.value + " "

    if acceleration:
        solution = accelerate(solution)

    solution = str(route_index) + "\n" + solution

    return solution