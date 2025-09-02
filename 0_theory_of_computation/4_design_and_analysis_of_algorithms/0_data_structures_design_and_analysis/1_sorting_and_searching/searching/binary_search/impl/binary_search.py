def binary_search_iterative_mutate_search_space(value, search_space):
    """NB: This is a poor search idea, because you loose the indexing into the original search space"""
    midpoint = 1
    while midpoint > 0:
        midpoint = int(len(search_space) / 2)
        if search_space[midpoint] == value:
            return midpoint
        elif value <= search_space[midpoint]:
            search_space = search_space[0:midpoint]
        else:
            search_space = search_space[midpoint:]
    return -1


def binary_search_iterative(value, search_space):
    lower_bound = 0
    upper_bound = len(search_space) - 1

    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2
        if value < search_space[midpoint]:
            upper_bound = midpoint - 1
        elif value > search_space[midpoint]:
            lower_bound = midpoint + 1
        elif value == search_space[midpoint]:
            return midpoint
    return -1


def binary_search_recursive(value, search_space):
    def recurse(upper_bound, lower_bound):
        midpoint = (lower_bound + upper_bound) // 2
        if midpoint < 0 or midpoint > len(search_space):
            return -1
        if value < search_space[midpoint]:
            return recurse(lower_bound, midpoint - 1)
        elif value > search_space[midpoint]:
            return recurse(midpoint + 1, upper_bound)
        elif value == search_space[midpoint]:
            return midpoint
        return -1

    return recurse(0, len(search_space) - 1)
