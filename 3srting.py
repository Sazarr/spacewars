import re
from collections import Counter

def top_3_words(text):
    # Find words with optional apostrophes using regex
    words = re.findall(r"[a-zA-Z]+':?[a-zA-Z]*", text.lower())

    # Count occurrences
    word_counts = Counter(words)

    # Return the top 3 most common words
    return [word for word, _ in word_counts.most_common(3)]