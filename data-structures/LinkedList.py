

class Node:
    """
    helper Node class
    """
    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next_node = next_node


def insert_at_end(linked_list, value):
    if linked_list is None:
        return Node(value)
    itr = linked_list

    while itr.next_node is not None:
        itr = itr.next_node
    itr.next_node = Node(value)


def reverse(linked_list: Node):
    if linked_list is None:
        return

    prev_ptr = None
    curr_ptr = linked_list
    next_ptr = curr_ptr.next_node

    while next_ptr is not None:
        curr_ptr.next_node = prev_ptr
        prev_ptr = curr_ptr
        curr_ptr = next_ptr
        next_ptr = next_ptr.next_node

    curr_ptr.next_node = prev_ptr
    return curr_ptr


def print_list(list):
    itr = list
    while itr is not None:
        print(str(itr.value) + " --> ", end="")
        itr = itr.next_node
    print("null")


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next_node = n2
    n2.next_node = n3
    n3.next_node = n4
    n4.next_node = n5

    print_list(n1)
    print_list(reverse(n1))

    insert_at_end(n5, 0)
    insert_at_end(n5, -1)
    print_list(n5)
