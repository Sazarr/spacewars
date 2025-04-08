from collections import Counter

def listPosition(word):
    l, r, s = len(word), 1, 1
    c = Counter()

    for i in range(l):
        x = word[(l - 1) - i]
        c[x] += 1
        for y in c:
            if (y < x):
                r += s * c[y] // c[x]
        s = s * (i + 1) // c[x]
    return r

from math import factorial
from collections import Counter

def list_position(word):
    letter_counts = Counter(word)

    def calculate_permutations_with_repeats(total_length, counts):
        perms = factorial(total_length)
        for count in counts.values():
            if count > 1:
                perms //= factorial(count)
        return perms

    rank = 1
    length = len(word)

    for i in range(length):
        current_letter = word[i]
        for c in sorted(letter_counts.keys()):
            if c < current_letter and letter_counts[c] > 0:
                letter_counts[c] -= 1

                remaining_length = length - i - 1
                perms = calculate_permutations_with_repeats(remaining_length, letter_counts)

                rank += perms

                letter_counts[c] += 1

        letter_counts[current_letter] -= 1
        if letter_counts[current_letter] == 0:
            del letter_counts[current_letter]

    return rank
