def isPP(n):
    from math import isqrt, log


    for m in range(2,isqrt(n)+1):
        for k in range(2, int(log(n, m)) + 2):
            if m**k == n:
                return [m, k]


    return None


def isPP(n):
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i**j > n:
                break
            elif i**j == n:
                return [i, j]
    return None