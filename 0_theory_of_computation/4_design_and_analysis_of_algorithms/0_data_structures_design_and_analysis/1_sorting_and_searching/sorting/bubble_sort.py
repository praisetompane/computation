def sort(arr):
    """
    basic bubble sort implementation
    example:
        data = 5,4,3,2,1

        Comparisons
            5 -> 4,3,2,1
            4 -> 3,2,1
            3 -> 3,2
            2 -> 1
            1 -> Nothing

            N = 5
            Comparisons = 10
            2N comparisons
            Formula: (N - 1) + (N - 2) + (N - 3) ... + 1
            4 + 3 + 2 + 1 + 1

        Swaps
            4
            3
            2
            1
            0

        Swaps = 9
        Formula: (N - 1) + (N - 2) + (N - 3)
    """
    _sorted = False
    unsorted_until_index = len(arr) - 1
    while not _sorted:
        _sorted = True
        for i in range(unsorted_until_index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                _sorted = False
    unsorted_until_index = unsorted_until_index - 1
    return arr
