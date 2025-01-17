def find_uniq(arr):
    if arr[0] == arr[1]:
        common = arr[0]
    else:
        common = arr[2]
    for n in arr:
        if n != common:
            return n


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b