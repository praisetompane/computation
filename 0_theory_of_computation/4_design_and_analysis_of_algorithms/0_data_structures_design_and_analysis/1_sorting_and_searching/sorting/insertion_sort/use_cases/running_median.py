from insertion_sort.impl.insertion_sort import sort


def calculate_running_medians(values):
    medians = []
    for i in range(0, len(values)):
        sorted_values = sort(values[: i + 1])
        number_of_sorted_values = len(sorted_values)
        if number_of_sorted_values % 2 == 0:
            right_index = number_of_sorted_values // 2
            left_index = right_index - 1
            median = (sorted_values[right_index] + sorted_values[left_index]) / 2
            if median.is_integer():
                medians.append(int(median))
            else:
                medians.append(median)
        else:
            medians.append(sorted_values[number_of_sorted_values // 2])
    return medians
