from src.route import Route


def read_from_file(filename):
    """
    Reads the lines from the file and returns an the matrix dimensions, the integer matrix, the number of routes and
     a list of routes from the read data
    :param filename: The path of the data file
    """
    no_rows = 0
    no_cols = 0
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
            elif len(elements) == 2:
                no_rows, no_cols = int(elements[0]), int(elements[1])

            # Save the route
            elif len(elements) == 5:
                routes.append(Route(*elements))

            # Replace any non-zero values with negative one, all zero values with maximum possible value
            #  and save the line in the matrix
            else:
                matrix.append([-1 if int(number) != 0 and int(number) != 2 else no_rows * no_cols for number in elements])

    return no_rows, no_cols, matrix, no_routes, routes
