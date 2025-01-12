def printer_error(s):
    """
    Calculates the error rate of a printer based on a control string.

    Args:
        s (str): The control string containing letters from a to z.

    Returns:
        str: The error rate as a fraction (e.g., "3/56").
    """
    # Count the number of errors (letters not in the range 'a' to 'm')
    errors = sum(1 for char in s if char < 'a' or char > 'm')

    # Calculate the error rate
    error_rate = f"{errors}/{len(s)}"

    return error_rate


# Example usage
control_string = "aaaxbbbbyyhwawiwjjjwwm"
print(printer_error(control_string))  # Output: "8/22"
