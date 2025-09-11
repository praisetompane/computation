from typing import List, Any


def _sort(values: List[Any], key: str, previous_key: str):
    for target_sort_index in range(0, len(values)):  # O(𝑁)
        minimum_value_index = target_sort_index
        for j in range(target_sort_index + 1, len(values)):  # O(𝑁)
            if (
                values[minimum_value_index][key] > values[j][key]
                and values[minimum_value_index][previous_key] >= values[j][previous_key]
            ):  # O(1)
                minimum_value_index = j

        if minimum_value_index != target_sort_index:
            temp = values[minimum_value_index]
            values[minimum_value_index] = values[target_sort_index]
            values[target_sort_index] = temp

    return values


def sort(values: List[Any], keys: List[str]):
    sorted_values = values
    previous_key = keys[0]
    for k in keys:
        sorted_values = _sort(sorted_values, k, previous_key)
        previous_key = k

    return sorted_values
