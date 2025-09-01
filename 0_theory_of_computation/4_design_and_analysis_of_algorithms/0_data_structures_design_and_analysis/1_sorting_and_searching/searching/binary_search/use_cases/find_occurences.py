from binary_search.impl.binary_search import binary_search_recursive


def find_occurence_indices(value, search_space):
    indices = []
    value_index = binary_search_recursive(value, search_space)

    if value_index != -1:
        indices.append(value_index)
        indices += collect_left_side_indices(value, search_space, value_index)
        indices += collect_right_side_indices(value, search_space, value_index)

    return indices


def collect_right_side_indices(value, search_space, value_index):
    indices = []
    idx = value_index + 1
    while idx < len(search_space):
        if search_space[idx] == value:
            indices.append(idx)
        break
    return indices


def collect_left_side_indices(value, search_space, value_index):
    indices = []
    idx = value_index - 1
    while idx > 0:
        if search_space[idx] == value:
            indices.append(idx)
        break
    return indices
