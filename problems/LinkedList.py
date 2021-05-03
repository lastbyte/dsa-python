class LinkedList:
    """
    helper Node class
    """

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next_node = next_node


def insert_at_end(linked_list, value):
    if linked_list is None:
        return LinkedList(value)
    itr = linked_list

    while itr.next_node is not None:
        itr = itr.next_node
    itr.next_node = LinkedList(value)


def insert_at_start(linked_list, value):
    node_to_insert = LinkedList(value)
    node_to_insert.next_node = linked_list
    return node_to_insert


def delete(linked_list, value):
    if linked_list is None:
        return
    prev_node = None
    curr_node = linked_list
    deleted = False
    while curr_node is not None and not deleted:
        if curr_node.value == value:
            if prev_node is None:
                return curr_node.next_node
            else:
                prev_node.next_node = curr_node.next_node
                deleted = True
        prev_node = curr_node
        curr_node = curr_node.next_node
    return linked_list


def reverse(linked_list: LinkedList):
    if linked_list is None:
        return

    prev_ptr, curr_ptr, next_ptr = None, linked_list, linked_list.next_node

    while next_ptr is not None:
        curr_ptr.next_node = prev_ptr
        prev_ptr = curr_ptr
        curr_ptr = next_ptr
        next_ptr = next_ptr.next_node

    curr_ptr.next_node = prev_ptr
    return curr_ptr


def print_list(linked_list):
    itr = linked_list
    while itr is not None:
        print(str(itr.value) + " --> ", end="")
        itr = itr.next_node
    print("null")


if __name__ == "__main__":
    n1 = LinkedList(1)
    n2 = LinkedList(2)
    n3 = LinkedList(3)
    n4 = LinkedList(4)
    n5 = LinkedList(5)
    n1.next_node = n2
    n2.next_node = n3
    n3.next_node = n4
    n4.next_node = n5

    print("original list : ", end="")
    original_list = n1;
    print_list(original_list)

    print("reverse list : ", end="")
    reverse_list = reverse(original_list)
    print_list(reverse_list)

    original_list = reverse(reverse_list)

    print("insert 6 at end : ", end="")
    insert_at_end(original_list, 6)
    print_list(original_list)

    print("insert 7 at end : ", end="")
    insert_at_end(original_list, 7)
    print_list(original_list)

    print("insert 10 at start : ", end="")
    original_list = insert_at_start(original_list, 10)
    print_list(original_list)

    print("delete node with value 2 : ", end="")
    original_list = delete(original_list, 2)
    print_list(original_list)
