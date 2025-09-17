from insertion_sort.use_cases.running_median import calculate_running_medians


def test_calculate_running_medians():
    values = [2, 1, 5, 7, 2, 0, 5]
    running_medians = calculate_running_medians(values)
    assert running_medians == [2, 1.5, 2, 3.5, 2, 2, 2]
