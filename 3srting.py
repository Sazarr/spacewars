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


["me'jfis", 'laudfweizh', "vyv'pcvxy"]
["me'jfis'", 'laudfweizh', "vyv'pcvxy"]

function
topThreeWords(text)
{
// Convert
to
lowercase and replace
any
character
that
's not a letter or apostrophe with a space
const
cleanedText = text.toLowerCase().replace( / [ ^ a - z
'\s]/g, ' ');

// Create
a
regex
that
matches
words
with at least one letter
const wordRegex = /[a-z]+['a-z]*/g;

// Find all valid words in the text
const words = cleanedText.match(wordRegex) | |[];

// Count word frequencies
const wordCounts = {};
for (const word of words) {
if (word) {
wordCounts[word] = (wordCounts[word] | | 0) + 1;
}
}

// Sort words by frequency and
return top
3
return Object.entries(wordCounts)
.sort((a, b) = > b[1] - a[1])
.slice(0, 3)
.map(entry= > entry[0]);
}