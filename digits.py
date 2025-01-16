def expanded_form(num):

    num_str = str(num)
    length = len(num_str)
    parts = [num_str[i] + "0" * (length - i - 1) for i in range(length) if num_str[i] != "0"]

    return " + ".join(parts)


def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')