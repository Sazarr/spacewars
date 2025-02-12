import math


def is_valid_sudoku(grid):
    N = len(grid)
    sqrt_N = math.isqrt(N)
    if sqrt_N * sqrt_N != N:
        return False