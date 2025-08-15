from impl.stack_node_based import Stack


def punctuation(document):

    def is_valid_pair(_close_punctuation, _open_punctuation):
        valid_pairs = {")": "(", "]": "[", "}": "{", "'": "'", '"': '"'}
        return valid_pairs[_close_punctuation] == _open_punctuation

    stack = Stack()
    open_punctuation = {"{", "[", "("}
    close_punctuation = {")", "]", "}"}
    single_character_pair_punctuation = {"'", '"', '"'}

    for char in document:
        if char in single_character_pair_punctuation and stack.peek() is not char:
            stack.push(char)
        else:
            if char in open_punctuation:
                stack.push(char)
            else:
                if (
                    char in close_punctuation
                    or char in single_character_pair_punctuation
                ):
                    if stack.is_empty():
                        return False
                    else:
                        return is_valid_pair(char, stack.pop())

    return stack.size() == 0
