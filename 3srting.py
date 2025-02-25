import re
from collections import Counter

def top_3_words(text):
    # Find words with optional apostrophes using regex
    words = re.findall(r"[a-zA-Z]+':?[a-zA-Z]*", text.lower())
    words = re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)*", text.lower())
    words = re.findall(r"[a-zA-Z]*'?([a-zA-Z]+(?:'[a-zA-Z]+)*)'?", text.lower())

    # Count occurrences
    word_counts = Counter(words)

    # Return the top 3 most common words
    return [word for word, _ in word_counts.most_common(3)]


from collections import Counter


def top_3_words(text):
    text = text.lower()
    words = []
    current_word = ""

    for i, char in enumerate(text):
        if char.isalpha():  # If it's a letter, add to the current word
            current_word += char
        elif char == "'":
            # If it's an apostrophe, check if it's between two letters
            if i > 0 and i < len(text) - 1 and text[i - 1].isalpha() and text[i + 1].isalpha():
                current_word += char
        else:
            # If we hit a non-letter character, store the current word
            if current_word:
                words.append(current_word)
                current_word = ""

    # Add last word if it wasn't stored
    if current_word:
        words.append(current_word)

    word_counts = Counter(words)

    return [word for word, _ in word_counts.most_common(3)]

import re
from collections import Counter

def top_3_words(text):

    text = text.lower()

    words = re.findall(r"(?=.*[a-z])[a-z']+", text)

    word_counts = Counter(words)
    return [word for word, count in word_counts.most_common(3)]

from collections import Counter
import re


def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]

#final