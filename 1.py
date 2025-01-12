def alphabet_position(text):
    """
    Replaces each letter in the input string with its position in the alphabet.

    Args:
        text (str): The input string.

    Returns:
        str: A string of space-separated numbers representing the positions of the letters.
    """
    return ' '.join(str(ord(char) - ord('a') + 1) for char in text.lower() if char.isalpha())

