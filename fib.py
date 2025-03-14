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

