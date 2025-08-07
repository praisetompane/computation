"""
objective:
    rotate array elements to the left n times.
flow:
    for rotations
        foreach index
            newIndex = index - 1
            if newIndex >= 0
                newArray[newIndex] = array[index]
            else
                newArray[lastIndex] = array[index]
"""


def new_index(index, rotations, arr_length):
    """
    remarks:
        NB: Example of calculating a future state once
    """
    target_index = index - rotations
    abs_target_index = abs(target_index)
    if target_index < 0:
        return arr_length - abs_target_index
    else:
        return abs_target_index


def rotateLeft(d, arr):
    arr_length = len(arr)
    print(arr_length)
    new_array = [0 for _ in range(arr_length)]
    for i in range(arr_length):
        new_array[new_index(i, d, arr_length)] = arr[i]
    return new_array
