from typing import List


def sort[T](values: List[T]):
    if len(values) <= 0:
        return values
    else:
        sort_start_index = 0
        passes = len(values)

        while passes > 0:
            smallest = (sort_start_index, values[sort_start_index])

            for idx in range(sort_start_index, len(values)):
                if values[idx] < smallest[1]:
                    smallest = (idx, values[idx])

            # swap, make it a function
            temp = values[sort_start_index]
            values[sort_start_index] = smallest[1]
            values[smallest[0]] = temp

            passes -= 1
            sort_start_index += 1

    return values


if __name__ == "__main__":
    assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sort([4, 2, 3, 1, 5]) == [1, 2, 3, 4, 5]
    assert sort([]) == []
    assert sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
