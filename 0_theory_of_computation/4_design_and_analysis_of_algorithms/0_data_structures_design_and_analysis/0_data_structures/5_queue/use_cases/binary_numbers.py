from impl.queue_deque_based import Queue


def print_binary_numbers(n):
    """
        8 bits  : 00000000
        0       : 0
        1       : 1
        2       : 1 + 0
        3       : 1 + 1
        4       : 1 + 0 + 0
        5       : 1 + 0 + 1
        6       : 1 + 1 + 0
        7       : 1 + 1 + 1
        8       : 1 + 0 + 0 + 0
        9       : 1 + 0 + 0 + 1
        10      : 1 + 0 + 1 + 0
    """
    numbers = Queue()
    # initial starting number
    print("0")
    numbers.enqueue("1")

    for _ in range(n):
        # print the last first entry as the current digit and remove it from queue
        current_number = numbers.dequeue()
        print(current_number)

        # generate next digits with current number as prefix
        numbers.enqueue(current_number + "0")
        numbers.enqueue(current_number + "1")


if __name__ == "__main__":
    print_binary_numbers(20)
