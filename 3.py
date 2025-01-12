def max_multiple(divisor, bound):
    """
    Finds the largest integer N such that:
    - N is divisible by divisor.
    - N is less than or equal to bound.
    - N is greater than 0.
    """
    return bound - (bound % divisor)


# Example usage
print(max_multiple(2, 7))  # Output: 6
