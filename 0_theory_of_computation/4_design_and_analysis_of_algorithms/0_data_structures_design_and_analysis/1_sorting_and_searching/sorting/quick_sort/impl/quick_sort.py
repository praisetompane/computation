from typing import List, Any


def _swap(values: List[Any], index_a: int, index_b: int) -> None:
    temp = values[index_a]
    values[index_a] = values[index_b]
    values[index_b] = temp


def _sort_around_partition_value(
    values: List[Any], start_index: int, end_index: int
) -> int:
    """Flow:
            Shuffles values around the partition value:
                - Values less than the partition value are placed to its left.
                - Values greater than the partition value are placed its right.

            Places the partition value into its correct sorted position(i.e. the middle of the list).

    Args:
        values (List[Any]): list of values to sort around a partition.
        start_index (int): start index of the subarray.
        end_index (int): end index of the subarray.

    Returns:
        int: partition value's new index.
    """
    partition_index = start_index
    partition_value = values[partition_index]
    # tracks last seen value that is greater than the partition
    left_partition_pointer = start_index
    # tracks last seen value that is less than the partition
    right_partition_pointer = end_index

    while left_partition_pointer < right_partition_pointer:
        """
        search for the index of a value that is GREATER than the partition value on the left side.
        values GREATER than than the partition value should not be found on the left side,
        hence we are looking for them, to move them to their correct side(i.e. right side).
        """
        while (
            left_partition_pointer < end_index
            and values[left_partition_pointer] <= partition_value
        ):
            left_partition_pointer += 1

        """
        search for the index of a value that is LESS than the partition value on the right side.
        values LESS than than the partition value should not be found on the right side,
        hence we are looking for them, to move them to their correct side(i.e. left side).
        """
        while values[right_partition_pointer] > partition_value:
            right_partition_pointer -= 1

        # swap values on the left and right side that are not on their correct side.
        if left_partition_pointer < right_partition_pointer:
            _swap(
                values,
                left_partition_pointer,
                right_partition_pointer,
            )

    """place partition value into its correct spot:
        swap it with the last value seen that is less than itself.
    """
    _swap(values, partition_index, right_partition_pointer)
    return right_partition_pointer


def sort(values: List[Any]) -> List[Any]:
    """Sort values in place in ascending order.

    Args:
        values (List[Any]): list of values to sort.

    Returns:
        List[Any]: sorted list of the values
    """

    def _sort(values: List[Any], start_index: int, end_index: int) -> None:
        """Sort each subarray in place using _sort_around_partition_value.

        Args:
            values (List[Any]): values to sort.
            start_index (int): subarray start index.
            end_index (int): subarray end index.
        """
        if start_index < end_index:
            # the value at the partition_index is now sorted
            partition_index = _sort_around_partition_value(
                values, start_index, end_index
            )
            # sort left partition(i.e. subarray)
            _sort(values, start_index, partition_index - 1)
            # sort right partition(i.e. subarray)
            _sort(values, partition_index + 1, end_index)

    _sort(values, 0, len(values) - 1)

    return values
