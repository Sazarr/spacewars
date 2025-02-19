def is_interesting(number, awesome_phrases):
    def is_followed_by_zeros(num):
        return num % 10 ** (len(str(num)) - 1) == 0

    def is_same_digit(num):
        return len(set(str(num))) == 1

    def is_sequential_inc(num):
        return str(num) in "1234567890"

    def is_sequential_dec(num):
        return str(num) in "9876543210"

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    def is_awesome_phrase(num):
        return num in awesome_phrases

    def check(num):
        if num < 100:
            return False
        return (is_followed_by_zeros(num) or is_same_digit(num) or
                is_sequential_inc(num) or is_sequential_dec(num) or
                is_palindrome(num) or is_awesome_phrase(num))

    if check(number):
        return 2
    if check(number + 1) or check(number + 2):
        return 1
    return 0
