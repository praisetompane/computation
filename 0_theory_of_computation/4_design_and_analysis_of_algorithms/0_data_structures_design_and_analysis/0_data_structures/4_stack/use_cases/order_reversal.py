from impl.stack_deque_based import Stack

"""
    general use case = reverse order
    Performance:
        N = length of item list
        Time = O(2 * N) = 𝑂(𝑁)
        Space = O(2 * N) = 𝑂(𝑁)
"""


def reverse_order(item_list):
    reverse_order = Stack()
    items_reversed = None

    for item in item_list:
        reverse_order.push(item)

    if isinstance(item_list, str):
        items_reversed = ""
        while reverse_order.is_empty() is False:
            items_reversed += reverse_order.pop()
    else:
        items_reversed = []
        while reverse_order.is_empty() is False:
            items_reversed.append(reverse_order.pop())

    return items_reversed
