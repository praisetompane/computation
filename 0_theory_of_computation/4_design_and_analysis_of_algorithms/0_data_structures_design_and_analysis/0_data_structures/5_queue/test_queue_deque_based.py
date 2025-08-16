from impl.queue_deque_based import Queue


def test_queue_interface():
    queue = Queue()

    print("Can enqueue to queue")
    assert queue.enqueue(1) == None
    assert queue.enqueue(2) == None

    print("Can check what is next is queue")
    assert queue.peek() == 1

    print("Can check size")
    assert queue.size() == 2

    print("Can remove next item in queue")
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2

    print("Can check if it is empty")
    assert queue.is_empty()

    print("Correctly informs user when empty")
    try:
        queue.dequeue()
    except IndexError as e:
        assert e.args[0] == "Queue is empty"


test_queue_interface()
