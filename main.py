import math


def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(float, line.split())) for line in file]
    return matrix

def write_solution_to_file(filename, solution):
    with open(filename, 'w') as file:
        for s in solution:
            file.write(f"{s}\n")

def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(el, end = ' ')
        print()

def find_max_off_diagonal_element(matrix, n):
    max_val = 0.0
    for i in range(n):
        for j in range(i+1, n):
            if abs(matrix[i][j]) > abs(max_val):
                max_val = matrix[i][j]
                max_coords = (i, j)
    print("====")
    print(max_coords)
    print("====")
    return max_coords

def rotate(matrix, i, j, n):
    if matrix[i][i] == matrix[j][j]:
        phi = math.pi / 4
    else:
        phi = 0.5 * math.atan(2*matrix[i][j] / (matrix[i][i] - matrix[j][j]))

    c = math.cos(phi)
    s = math.sin(phi)

    for k in range(n):
        if k != i and k != j:
            temp_i = c * matrix[i][k] + s * matrix[j][k]
            temp_j = -s * matrix[i][k] + c * matrix[j][k]
            matrix[i][k] = temp_i
            matrix[j][k] = temp_j

    print_matrix(matrix)
    print()

    for k in range(n):
        if k != i and k != j:
            matrix[k][i] = matrix[i][k]
            matrix[k][j] = matrix[j][k]

    print_matrix(matrix)
    print()

    matrix[i][i] = c * c * matrix[i][i] + 2 * c * s * matrix[i][j] + s * s * matrix[j][j]
    matrix[j][j] = s * s * matrix[i][i] - 2 * c * s * matrix[i][j] + c * c * matrix[j][j]
    matrix[i][j] = matrix[j][i] = 0.0

    print_matrix(matrix)
    print("///////////////")

def solve(matrix, n):
    for _ in range(n):
        i, j = find_max_off_diagonal_element(matrix, n)
        rotate(matrix, i, j, n)

    solution = [matrix[i][i] for i in range(n)]
    return solution

def main():
    matrix = read_matrix_from_file("input.txt")
    n = len(matrix)
    solution = solve(matrix, n)
    write_solution_to_file("output.txt", solution)

if __name__ == "__main__":
    main()
