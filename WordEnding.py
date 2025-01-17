def pig_it(text):
    words = text.split()
    pig_latin_words = [
        word[1:] + word[0] + "ay" if word.isalpha() else word
        for word in words
    ]
    return " ".join(pig_latin_words)
