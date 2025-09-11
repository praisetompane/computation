from typing import List, Any


def _sort(values: List[Any], key: str):
    for target_sort_index in range(0, len(values)):  # O(𝑁)
        minimum_value_index = target_sort_index
        for j in range(target_sort_index, len(values)):  # O(𝑁)
            if values[minimum_value_index][key] > values[j][key]:  # O(1)
                minimum_value_index = j

        if minimum_value_index != target_sort_index:
            temp = values[minimum_value_index]
            values[minimum_value_index] = values[target_sort_index]
            values[target_sort_index] = temp

    return values


def sort(values: List[Any], keys: List[str]):
    sorted_values = values
    for k in reversed(keys):
        sorted_values = _sort(sorted_values, k)

    return sorted_values
