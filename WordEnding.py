def pig_it(text):
    words = text.split()
    pig_latin_words = [
        word[1:] + word[0] + "ay" if word.isalpha() else word
        for word in words
    ]
    return " ".join(pig_latin_words)


def pig_it(text):
    res = []

    for i in text.split():
        if i.isalpha():
            res.append(i[1:] + i[0] + 'ay')
        else:
            res.append(i)

    return ' '.join(res)