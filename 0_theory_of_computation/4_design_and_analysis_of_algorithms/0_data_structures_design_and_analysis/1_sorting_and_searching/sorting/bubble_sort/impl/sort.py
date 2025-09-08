from typing import List, Any


def sort(values: List[Any]):
    """
    - intuition: per iteration of the entire search space:
                    move/'bubble up' one value to its correct location
    - properties:
        - Performance:
            - Time = O(𝑁*𝑁
                     O(𝑁²)
    """

    for i in range(0, len(values)):  # O(𝑁)
        swapped = False
        for j in range(0, len(values) - 1 - i):  # O(𝑁)
            if values[j] > values[j + 1]:  # O(1)
                temp = values[j]
                values[j] = values[j + 1]
                values[j + 1] = temp
                swapped = True
        if not swapped:
            return values
    return values
