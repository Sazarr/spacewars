import math


def is_valid_sudoku(grid):
    N = len(grid)
    sqrt_N = math.isqrt(N)
    if sqrt_N * sqrt_N != N:
        return False

     expected_set = set(range(1, N + 1))

# Check rows and columns
for i in range(N):
    if set(grid[i]) != expected_set:
        return False  # Row check
    if set(row[i] for row in grid) != expected_set:
        return False  # Column check