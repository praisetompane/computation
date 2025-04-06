"""
def:
    tree with zero, one or two children
    if node has two children:
        one child has value greater than parent's value
        one child has value less than parent's value

printing representations:
    in order
    pre order
    post order

    NB: These are all relative to the parent
        i.e. in order = parent printed in middle, where it is in the tree
             pre order = parent printed 'pre'(i.e. before) children
             post order = parent printed 'post'(i.e. after) children

        children always printed from left to right.

"""


class Node:
    def __init__(self, val, leftchild=None, rightchild=None):
        self.val = val
        self._leftchild = leftchild
        self._rightchild = rightchild


class BinaryTree:
    def __init__(self, root):
        self._root = root

    # O(log N)
    def search(self, value):
        def _search(node):
            if not node:
                return None
            elif node.val == value:
                return node
            elif value < node.val:
                return _search(node._leftchild)
            elif value > node.val:
                return _search(node._rightchild)

        return _search(self._root)

    def insert(self, value):
        def _insert(node):
            if value < node.val and not node._leftchild:
                node.leftchild = node
            else:
                _insert(node._leftchild)

            if value > node.val and not node._rightchild:
                node._rightchild = node
            else:
                _insert(node._rightchild)

        _insert(self._root)

    def delete(value):
        def lift(node, nodeToDelete):
            if node._leftchild:
                node._leftchild = lift(node.leftchild, nodeToDelete)
                return node
            else:
                nodeToDelete.value = node.val
                return node._rightchild

        def _delete(node):
            if node is None:
                return None

            elif value < node.val:
                node._leftchild = _delete(node._leftchild)
                return node
            elif value > node.val:
                node.rightchild = delete(node.rightchild)
                return node
            elif value == node.val:
                if node._leftchild is None:
                    return node._rightchild
                elif node.rightchild is None:
                    return node._leftchild
                else:
                    node._rightchild = lift(node._rightchild, node)

        _delete(self.root)

    def print_tree(self):
        def _print(node):
            if node:
                if node._leftchild and node._rightchild:
                    print("/", "\\", end=""),
                    print(node._leftchild.val, end=""),
                    print(node._rightchild.val)
                    _print(node._leftchild)
                    _print(node._rightchild)
                if node._leftchild and not node._rightchild:
                    print("/")
                    print(node._leftchild.val)
                    _print(node._leftchild)
                if node._rightchild and not node._leftchild:
                    print("\\")
                    print(node._rightchild.val)
                    _print(node._rightchild)

        _print(self._root)

    def traverse_and_print(self):
        def _print(node):
            if node is None:
                return
            _print(node._leftchild)
            print(node.val)
            _print(node._rightchild)

        _print(self._root)


node52 = Node(52)
node61 = Node(61)
node56 = Node(56, node52, node61)

node82 = Node(82)
node95 = Node(95)
node89 = Node(89, node82, node95)

node30 = Node(30)
node40 = Node(40)
node33 = Node(33, node30, node40)

node4 = Node(4)
node11 = Node(11)
node10 = Node(10, node4, node11)

node25 = Node(25, node10, node33)
node75 = Node(75, node56, node89)
root = Node(50, node25, node75)

tree = BinaryTree(root)
print("searching for the value 11")
print(tree.search(50).val)

print("print the tree\n")
tree.print_tree()

tree.insert

print(tree.search(11).val)

tree.traverse_and_print()
