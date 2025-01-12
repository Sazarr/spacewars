def find_even_index(arr):
    """
    Optimized solution to find the lowest index N where the sum of the integers
    to the left of N equals the sum of the integers to the right of N.
    """
    total_sum = sum(arr)
    left_sum = 0

    for i, num in enumerate(arr):
        # Right sum can be derived as total_sum - left_sum - current element
        if left_sum == (total_sum - left_sum - num):
            return i
        left_sum += num

    return -1


# Example usage
print(find_even_index([1, 2, 3, 4, 3, 2, 1]))  # Output: 3
print(find_even_index([1, 100, 50, -51, 1, 1]))  # Output: 1
print(find_even_index([20, 10, -80, 10, 10, 15, 35]))  # Output: 0
print(find_even_index([1, 2, 3]))  # Output: -1
