def generate_hashtag(s):
    words = s.strip().split()
    if not words:
        return False
    #first_s = s[0]
    hashtag_text = "#" + ''.join(word.capitalize() for word in words)
    if len(hashtag_text) > 140:

        return False

    return hashtag_text