

def check_int(prompt: str):
    num = input(prompt)
    try:
        return int(num)
    except Exception:
        check_int("Enter a valid integer: ")

# Makes the leading value of the row equal to 1
def divide_row(matrix: list, row_num: int, col_num: int):
    # Divide the row by the leading number
    matrix[row_num] = row_mult(matrix, row_num, 1/matrix[row_num][col_num])
    return row_add(matrix, row_num, matrix[row_num])

# Adds one row to every row
def row_add(matrix: list, row_num: int, row: list):
    # For each row in the matrix
    for i in range(len(matrix)):
        # Skip the row we want to keep
        if i == row_num:
            continue
        else:
            # Add the two rows together
            new_row = []
            for j in range(len(row)):
                new_row.append(matrix[i][j] - row[j])
            matrix[i] = new_row
    return matrix

# Multiplies a row by a factor
def row_mult(matrix: list, row_num: int, factor: int):
    new_row = []
    for num in matrix[row_num]:
        new_row.append(num * factor)
    matrix[row_num] = new_row
    return matrix

# Manages other functions to turn matrix to ref
def ref(matrix: list):
    for i in range(len(matrix)-1):
        matrix = divide_row(matrix, i, i) # Implement finding of the col number of the first non-zero value

    return matrix

def main():
    # Matrix dimensions
    m = check_int("Matrix rows m: ")
    n = check_int("Matrix cols n: ")
    
    # Fill the matrix
    matrix = [[0] * n] * m
    for i in range(m):
        for j in range(n):
            value = check_int(f"Cell {i}, {j}:\n")
            matrix[i][j] = value

    # Put into REF
    ref_matrix = ref(matrix)

    print(f"\nREF for matrix {m} x {n}\n\t{ref_matrix}")

main()