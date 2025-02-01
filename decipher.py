import re


def solve_runes(expression: str) -> int:
    # Split expression into LHS and RHS
    left, right = expression.split("=")

    # Extract existing digits in the expression
    existing_digits = set(re.sub(r"[^0-9]", "", expression))  # Set of digits used in the expression

    # Function to check if a number is valid (no leading zeros unless single-digit "0")
    def is_valid_number(num_str):
        return num_str == "0" or not re.match(r"^-?0\d", num_str)

    # Try replacing "?" with digits from 0-9, ensuring it's not in existing digits
    for digit in map(str, range(10)):  # Digits "0" to "9"
        if digit in existing_digits:
            continue  # Skip digits already present

        # Replace all '?' in the expression with the candidate digit
        new_expr = expression.replace("?", digit)

        # Extract operands and operator from the left-hand side
        match = re.match(r"(-?\d+)([+\-*])(-?\d+)", left.replace("?", digit))
        if not match:
            continue

        operand1, operator, operand2 = match.groups()
        result = right.replace("?", digit)

        # Validate that we don't create an invalid number
        if not (is_valid_number(operand1) and is_valid_number(operand2) and is_valid_number(result)):
            continue

        # Evaluate the equation
        if eval(f"{int(operand1)} {operator} {int(operand2)}") == int(result):
            return int(digit)  # Return the first (smallest) valid digit

    return -1  # If no valid digit found
