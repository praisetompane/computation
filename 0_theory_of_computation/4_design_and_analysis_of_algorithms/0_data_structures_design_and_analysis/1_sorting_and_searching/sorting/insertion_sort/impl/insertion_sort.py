from typing import List, Any


def sort(values: List[Any]):
    for idx, value_to_insert in enumerate(values):
        i = idx - 1
        while i >= 0:
            if value_to_insert < values[i]:
                temp = values[i]
                values[i] = value_to_insert
                values[i + 1] = temp
            i -= 1
    return values
