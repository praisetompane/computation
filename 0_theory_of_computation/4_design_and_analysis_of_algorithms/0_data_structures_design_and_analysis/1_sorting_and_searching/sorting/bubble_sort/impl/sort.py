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

    for _ in range(0, len(values)):  # O(𝑁)
        for j in range(0, len(values) - 1):  # O(𝑁)
            if values[j] > values[j+1]:  # O(1)
                temp = values[j]
                values[j] = values[j+1]
                values[j+1] = temp
    return values