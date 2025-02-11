def snail(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)

        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop(-1))

        if matrix:
            result += matrix.pop(-1)[::-1]

        if matrix and matrix[0]:
            for row in reversed(matrix):
                result.append(row.pop(0))

    return result


import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out