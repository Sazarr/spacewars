def move_zeros(lst):
    non_zero_index = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[non_zero_index], lst[i] = lst[i], lst[non_zero_index]
            non_zero_index +=1
    return lst
def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array


