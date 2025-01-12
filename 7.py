def to_camel_case(text):
    """
    Converts dash/underscore delimited words into camelCase or PascalCase.

    Args:
        text (str): The input text to be converted.

    Returns:
        str: The text in camelCase or PascalCase based on the input.
    """
    # Split the text into words using '-' and '_' as delimiters
    words = text.replace("-", "_").split("_")

    # Preserve the case of the first word, and capitalize subsequent words
    if not words[0]:
        return ""  # Handle empty input
    first_word = words[0]
    camel_case_text = first_word + ''.join(word.capitalize() for word in words[1:])

    return camel_case_text


# Example usage
print(to_camel_case("the-stealth-warrior"))  # Output: theStealthWarrior
print(to_camel_case("The_Stealth_Warrior"))  # Output: TheStealthWarrior
