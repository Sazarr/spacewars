def find_uniq(arr):
    if arr[0] == arr[1]:
        common = arr[0]
    else:
        common = arr[2]  # If arr[0] and arr[1] are different, then arr[2] must be common

    # Find the unique number by looking for the one that differs from `common`
    for n in arr:
        if n != common:
            return n