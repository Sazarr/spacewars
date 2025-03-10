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


from math import factorial
from collections import Counter


def get_word_rank(word):
    # Create a frequency counter of letters in the word
    letter_counts = Counter(word)

    # Precalculate factorial for used letters
    def multiset_permutation_count(counts):
        # Calculate the denominator for repeated letters
        denominator = 1
        for count in counts.values():
            denominator *= factorial(count)
        return denominator

    # Calculate rank
    rank = 1
    length = len(word)

    for i in range(length):
        for c in sorted(set(word[i:])):
            if c < word[i]:
                temp_counts = letter_counts.copy()
                temp_counts[c] -= 1

                current_perms = factorial(length - i - 1)

                current_perms //= multiset_permutation_count(temp_counts)

                rank += current_perms

        letter_counts[word[i]] -= 1
 rank

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
