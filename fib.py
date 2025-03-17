def fib(n):
    """
    Calculate the nth Fibonacci number where:
    fib(0) = 0
    fib(1) = 1
    fib(n+2) = fib(n+1) + fib(n)

    Can handle n up to 2,000,000 and negative n values.
    Returns the exact integer result.
    """
    if n == 0:
        return 0

    # Handle negative indices
    if n < 0:
        # Use the identity: fib(-n) = (-1)^(n+1) * fib(n)
        return (-1) ** (n + 1) * fib(-n) if n % 2 == 0 else -fib(-n)

    # Use fast doubling method for large n
    # Returns [F(n), F(n+1)]
    def fibonacci_pair(n):
        if n == 0:
            return (0, 1)

        # Calculate [F(n//2), F(n//2 + 1)]
        a, b = fibonacci_pair(n // 2)

        # F(2k) = F(k) * (2*F(k+1) - F(k))
        # F(2k+1) = F(k+1)^2 + F(k)^2
        c = a * ((b << 1) - a)
        d = a * a + b * b

        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return fibonacci_pair(n)[0]


def fib(n):
    """
    Calculate the nth Fibonacci number where:
    fib(0) = 0
    fib(1) = 1
    fib(n+2) = fib(n+1) + fib(n)

    Can handle n up to 2,000,000 and negative n values.
    Returns the exact integer result.
    """
    if n == 0:
        return 0

    # Handle negative indices
    if n < 0:
        # For negative indices, we use the formula:
        # fib(-n) = (-1)^(n+1) * fib(n)
        return (-1) ** (n + 1) * fib(abs(n))

    # Use fast doubling method for large n
    # Returns [F(n), F(n+1)]
    def fibonacci_pair(n):
        if n == 0:
            return (0, 1)

        # Calculate [F(n//2), F(n//2 + 1)]
        a, b = fibonacci_pair(n // 2)

        # Use these identities:
        # F(2k) = F(k) * (2*F(k+1) - F(k))
        # F(2k+1) = F(k+1)^2 + F(k)^2
        c = a * ((b * 2) - a)
        d = a * a + b * b

        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return fibonacci_pair(n)[0]


def fib(n):
    """
    Calculate the nth Fibonacci number using matrix exponentiation.
    Handles all values of n including negative.
    """
    if n == 0:
        return 0

    # Handle negative indices using the property:
    # F(-n) = (-1)^(n+1) * F(n)
    negative = n < 0
    n = abs(n)

    # Matrix exponentiation approach for F(n)
    def matrix_power(matrix, power):
        # Initialize result as identity matrix
        result = [[1, 0], [0, 1]]

        # Binary exponentiation
        while power > 0:
            if power & 1:  # power % 2 == 1
                result = matrix_multiply(result, matrix)
            matrix = matrix_multiply(matrix, matrix)
            power >>= 1  # power //= 2

        return result

    def matrix_multiply(A, B):
        C = [[0, 0], [0, 0]]
        C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
        return C

    # Base matrix [[1,1],[1,0]]
    F = [[1, 1], [1, 0]]

    # Get F^n
    if n == 1:
        result = 1
    else:
        result = matrix_power(F, n - 1)[0][0]

    # Apply sign adjustment for negative indices
    if negative:

        if n % 2 == 0:
            result = -result

    return result

def fib(n):
    if n == 0:
        return 0
    elif n < 0:
        return -fib(-n) if n % 2 == 0 else fib(-n)

    def mat_mult(A, B):
        """Multiplies two 2x2 matrices."""
        return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

    def mat_pow(matrix, exp):
        """Performs fast matrix exponentiation."""
        result = [[1, 0], [0, 1]]  # Identity matrix
        base = matrix

        while exp:
            if exp % 2:
                result = mat_mult(result, base)
            base = mat_mult(base, base)
            exp //= 2

        return result

    F = [[1, 1], [1, 0]]  # Fibonacci transformation matrix
    result = mat_pow(F, n - 1)
    return result[0][0]  # Fib(n) is stored at position (0,0) in the result matrix

