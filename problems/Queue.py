class LinkedList:
    """
    helper Node class
    """

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next_node = next_node


class Queue:

    def __init__(self):
        self.memory = None
        self.front = None
        self.back = None

    def enqueue(self, value):
        if self.is_empty():
            self.memory = LinkedList(value)
            self.front = self.back = self.memory
            return True
        else:
            node_inserted = LinkedList(value)
            self.back.next_node = node_inserted
            self.back = node_inserted

    def dequeue(self):
        if self.is_empty():
            return False
        else:
            node_removed = self.front
            self.front = self.front.next_node
            if self.is_empty():
                self.front = self.back = None
            return node_removed

    def is_empty(self):
        if self.front == self.back and self.front is None and self.back is None:
            return True
        return False

    def __str__(self):
        node = self.front
        ret_string = ""
        while node is not None:
            ret_string += str(node.value) + "-->"
            node = node.next_node
        ret_string += "null"
        return ret_string


if __name__ =="__main__":
    queue = Queue()
    print(queue.is_empty())
    queue.enqueue(1)
    print(queue.is_empty())
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue)
    queue.enqueue(5)
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)