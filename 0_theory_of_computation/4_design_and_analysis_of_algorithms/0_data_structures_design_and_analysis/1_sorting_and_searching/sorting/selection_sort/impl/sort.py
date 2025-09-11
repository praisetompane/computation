from typing import List, Any


def sort(values: List[Any]):
    """
    - formal: ???
        - in words: ???

    - plain english: ???

    - intuition: per iteration of the entire search space:
                    find(i.e. select) best match for your predicate(i.e. lowest | highest)
                        move it to the target sort index
                    then remove the target sort index and its value from the search space, because it is already sorted(i.e. it has the correct value)
                        i.e. shrink|reduce the search space to have only unsorted values

    - properties:
        - Performance:
            - Time = O(𝑁*𝑁
                     O(𝑁²)
    - examples: 0_theory_of_computation/4_design_and_analysis_of_algorithms/0_data_structures_design_and_analysis/1_sorting_and_searching/sorting/test_selection_sort.py

    - use cases:
        - ordering

    - proof: ???

    """
    for target_sort_index in range(0, len(values)):  # O(𝑁)
        for j in range(target_sort_index + 1, len(values)):  # O(𝑁)
            if values[target_sort_index] > values[j]:  # O(1)
                temp = values[j]
                values[j] = values[target_sort_index]
                values[target_sort_index] = temp

    return values


from enum import Enum


class SORT_DIRECTION(Enum):
    ASC = 1
    DESC = 0

    def __str__(self) -> str:
        return self.name


def sort_explicit(
    values: List[Any], sort_direction: SORT_DIRECTION = SORT_DIRECTION.ASC
) -> List[Any]:
    """_summary_

    Args:
        values (List[Any]): values to sort
        sort_direction (SORT_DIRECTION): Ascending or Descending order

    Returns:
        List[Any]: new sorted list

    Performance:
        Tine = O(1) + O(1) + O(𝑁 * 𝑁)
               O(1) + O(1) + O(𝑁²)
               O(𝑁²)
    """
    if len(values) == 0:
        return []

    _values = []  # O(1)
    value_to_sort = values[0]  # O(1)
    search_sub_space = values  # O(𝑁)

    for _ in range(len(values)):  # O(𝑁)
        if sort_direction == SORT_DIRECTION.ASC:
            value_to_sort = min(search_sub_space)  # O(𝑁)
        elif sort_direction == SORT_DIRECTION.DESC:
            value_to_sort = max(search_sub_space)  # O(𝑁)
        else:
            raise ValueError(f"Invalid sort direcion: {sort_direction}")
        # 'bubble to'/move the best match for your predicate(i.e. lowest | highest) to the target sort index(i.e. its correct location)
        _values.append(value_to_sort)

        # collect up unsorted values into reduced search space
        value_to_sort_current_index = search_sub_space.index(value_to_sort)
        search_sub_space[value_to_sort_current_index] = search_sub_space[0]

        # shrink/reduce the search space to have only unsorted values
        search_sub_space = search_sub_space[1:]
    return _values
