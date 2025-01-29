def tribonacci(signature, n):
    # Handle edge cases
    if n == 0:
        return []
    if n <= 3:
        return signature[:n]

    # Initialize result with signature
    result = signature.copy()

    # Generate sequence
    for i in range(n - 3):
        result.append(sum(result[-3:]))

    return result
