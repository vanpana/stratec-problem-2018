from src.file_worker import read_from_file

if __name__ == '__main__':
    # Read the data from file
    no_rows, no_cols, matrix, no_routes, routes = read_from_file("../data/data.in")

    print(matrix)
