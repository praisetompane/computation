class Node:
    def __init__(self, value: int, next: any = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head

    def add_next(self, current_node: Node, next_node: Node):
        current_node.next = next_node

    def __str__(self) -> str:
        string_value = ""
        current_node = self.head
        while current_node is not None:
            string_value += f"{current_node.value} "
            current_node = current_node.next

        return string_value

    def reverse(self):
        """
        Performance:

            Time = 𝑂(𝑁)
            Space = O(1): reuses existing nodes.

        """
        current_node = self.head
        next_node = None
        previous_node = None

        while current_node is not None:
            next_node = current_node.next

            # NB: The key is here. we set a node's successor(i.e. next) value to be its predecessor. which is what reversal means.
            # The rest is housekeeping to remember who was next and was the previous.
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node
        self.head = previous_node


head = Node(1)
linked_list = LinkedList(head)

node_2 = Node(2)
linked_list.add_next(head, node_2)

node_3 = Node(3)
linked_list.add_next(node_2, node_3)

node_4 = Node(4)
linked_list.add_next(node_3, node_4)

print(linked_list)

linked_list.reverse()

print(linked_list)
