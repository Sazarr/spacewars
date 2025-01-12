def likes(names):
    """
    Generates a text based on the number of people liking an item.

    Args:
        names (list): A list of names of people who like the item.

    Returns:
        str: A text string describing the likes.
    """
    n = len(names)
    if n == 0:
        return 'no one likes this'
    elif n == 1:
        return f'{names[0]} likes this'
    elif n == 2:
        return f'{names[0]} and {names[1]} like this'
    elif n == 3:
        return f'{names[0]} and {names[1]} and {name[2]} like this'
    elif n == 4:
        return f'{names[0]} and {names[1]} and {n - 2} other like this'

    print(likes([]))
    print(likes(["Peter"]))
    print(likes(["Jacob", "Alex"]))
    print(likes(["Max", "John", "Mark"]))
    print(likes(["Alex", "Jacob", "Mark", "Max"]))
