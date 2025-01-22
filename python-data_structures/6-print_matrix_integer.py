#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j, data in enumerate(row):
            if len(row) - 1 > j:
                print("{:d}".format(data), end=" ")
            else:
                print("{:d}".format(data), end="")
        print("")
