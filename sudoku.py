import math
def is_valid_sudoku(grid):
    N = len(grid)
    sqrt_N = math.isqrt(N)
    if sqrt_N * sqrt_N != N:
        return False

    expected_set = set(range(1, N + 1))

    for i in range(N):
    if set(grid[i]) != expected_set:
        return False  # Row check
    if set(row[i] for row in grid) != expected_set:
        return False  # Column check
    # Check sub-grids
    for row in range(0, N, sqrt_N):
        for col in range(0, N, sqrt_N):
            sub_grid = set()
            for r in range(row, row + sqrt_N):
                for c in range(col, col + sqrt_N):
                    sub_grid.add(grid[r][c])
            if sub_grid != expected_set:
                return False
    return True
