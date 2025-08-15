from impl.stack_deque_based import Stack

"""
    general use case = undo operations
    Performance:
        N = length of item list
        Space = O(2 * N) = 𝑂(𝑁)
        write:
            Time = O(1)
        undo:
            Time= O(1)
        redo:
            Time= O(1)
        display:
            Time= O(1)
"""


class OperationsTracker:
    undo_stack = None
    redo_stack = None
    current_state = None

    def __init__(self, current_state):
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.current_state = current_state

    def add_operations_result(self, operation_result):
        self.undo_stack.push(operation_result)
        self.current_state += operation_result

        return self.display()

    def undo(self):
        self.redo_stack.push(self.undo_stack.peek())
        last_word = self.undo_stack.pop()
        self.current_state = self.current_state[: -len(last_word)]
        return self.display()

    def redo(self):
        self.current_state += self.redo_stack.pop()
        return self.display()

    def display(self):
        return self.current_state
