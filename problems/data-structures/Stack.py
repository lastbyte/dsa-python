class LinkedList:
    """
    helper Node class
    """

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack:

    def __init__(self):
        self.memory = None
        self.top = None

    def push(self, value):
        if self.is_empty():
            self.memory = LinkedList(value)
            self.top = self.memory
            return True
        else:
            node_inserted = LinkedList(value)
            node_inserted.next_node = self.top
            self.top = node_inserted
            return True

    def pop(self):
        if self.is_empty():
            return False
        else:
            node_removed = self.top
            self.top = self.top.next_node
            if self.is_empty():
                self.top = None
            return node_removed

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def peek(self):
        return self.top

    def __str__(self):
        node = self.top
        ret_string = ""
        while node is not None:
            ret_string += str(node.value) + "-->"
            node = node.next_node
        ret_string += "null"
        return ret_string


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    print(stack.is_empty())
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)
    stack.push(5)
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
