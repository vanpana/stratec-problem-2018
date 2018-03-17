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
                matrix = [[[[] for _ in range(no_height)] for _ in range(no_cols)] for _ in range (no_rows)]

            # Save the route
            elif len(elements) == 7:
                routes.append(Route(*elements))

            # Replace any non-zero values with negative one, all zero values with maximum possible value
            #  and save the line in the matrix
            else:
                if int(elements[3]) != 2 and int(elements[3]) != 0:
                    value = -1
                else:
                    value = int(elements[3])
                matrix[int(elements[0])][int(elements[1])][int(elements[2])] = value
                # matrix.append([-1 if int(number) != 0 and int(number) != 2 else no_rows * no_cols for number in elements])

    return no_rows, no_cols, no_height, matrix, no_routes, routes


def save_to_file(filename, solution):
    with open(filename, "a") as file:
        file.write(solution + "\n")
