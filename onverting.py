from math import factorial
from collections import Counter

def rank_word(word):
    letter_counts = Counter(word)
    sorted_letters = sorted(letter_counts.keys())
    rank = 1  # Starts from 1
    word_length = len(word)

    for i, letter in enumerate(word):
        for smaller_letter in sorted_letters:
            if smaller_letter >= letter:
                break
            if letter_counts[smaller_letter] > 0:
                # Compute permutations if `smaller_letter` was placed first
                letter_counts[smaller_letter] -= 1
                rank += factorial(word_length - i - 1) // prod_factorials(letter_counts)
                letter_counts[smaller_letter] += 1  # Restore the count

        # Reduce letter count for the placed letter
        letter_counts[letter] -= 1
        if letter_counts[letter] == 0:
            sorted_letters.remove(letter)

    return rank

def prod_factorials(counter):
    """ Returns product of factorials of letter counts """
    return factorial(sum(counter.values())) // prod(factorial(v) for v in counter.values())

def prod(iterable):
    """ Computes the product of an iterable of numbers """
    result = 1
    for x in iterable:
        result *= x
    return result
