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
        # Count smaller letters that could appear at this position
        for c in sorted(set(word[i:])):
            if c < word[i]:
                # Create a temporary letter counter
                temp_counts = letter_counts.copy()
                temp_counts[c] -= 1

                # Calculate permutations for this prefix
                current_perms = factorial(length - i - 1)

                # Adjust for letter frequencies
                current_perms //= multiset_permutation_count(temp_counts)

                # Add to rank
                rank += current_perms

        # Reduce count of current letter
        letter_counts[word[i]] -= 1

    return rank







