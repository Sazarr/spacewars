def last_digit(a, b):
    if b == 0:
        return 1  # By definition, 0^0 = 1

    # Get the last digit of a
    last_digit = a % 10

    # Cycles for last digits (0-9)
    cycles = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }

    # Get the cycle of the last digit
    cycle = cycles[last_digit]
    cycle_length = len(cycle)

    # Find the effective exponent position in the cycle
    index = (b - 1) % cycle_length  # (b - 1) to get 0-based index

    # Return the last digit from the cycle
    return cycle[index]
