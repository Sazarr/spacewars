def expanded_form(num):

    num_str = str(num)
    length = len(num_str)
    parts = [num_str[i] + "0" * (length - i - 1) for i in range(length) if num_str[i] != "0"]

    return " + ".join(parts)


