def linear_search(value, search_space):
    i = 0
    upperBound = len(search_space) - 1
    while i <= upperBound:
        if value == search_space[i]:
            return i
        i = i + 1
    return None


def linear_search_enumerate(value, search_space):
    for idx, content in enumerate(search_space):
        if value == content:
            return idx
    return None
