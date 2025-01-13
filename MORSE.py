from preloaded import MORSE_CODE

def decode_morse(morse_code):
    # Remove leading/trailing whitespace
    morse_code = morse_code.strip()
    
    # Split into words (separated by 3 spaces)
    words = morse_code.split('   ')
    
    # Decode each word
    decoded_words = []
    for word in words:
        # Split word into characters (separated by single space)
        chars = word.split(' ')
        # Decode each character using MORSE_CODE dictionary
        decoded_word = ''.join(MORSE_CODE[char] for char in chars)
        decoded_words.append(decoded_word)
    
    # Join words with spaces
    return ' '.join(decoded_words)


def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))