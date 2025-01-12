def count_bits(n):
    """
    Counts the number of bits equal to 1 in the binary representation of a number.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The count of 1 bits in the binary representation of n.
    """
    return bin(n).count('1')


# Example usage
print(count_bits(1234))  # Output: 5
