class Node:
    """
    helper Node class
    """

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


def has_loop(root):

    if root is None:
        return False

    if root.next_node is None:
        return False

    slow_ptr, fast_ptr = root, root

    # move to next position for 1 time
    slow_ptr, fast_ptr = slow_ptr.next_node, fast_ptr.next_node
    if fast_ptr is not None:
        fast_ptr = fast_ptr.next_node
    # initialize loop_found to false
    loop_found = False
    while slow_ptr is not None and fast_ptr is not None and not loop_found:
        if slow_ptr == fast_ptr:
            loop_found = True
            break
        slow_ptr, fast_ptr = slow_ptr.next_node, fast_ptr.next_node
        if fast_ptr is not None:
            fast_ptr = fast_ptr.next_node

    if loop_found:
        slow_ptr = root
        while slow_ptr != fast_ptr:
            slow_ptr, fast_ptr = slow_ptr.next_node, fast_ptr.next_node
        return slow_ptr

    return loop_found;


if __name__ == "__main__":
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)

    n0.next_node = n1
    n1.next_node = n2
    n2.next_node = n3
    n3.next_node = n4
    n4.next_node = n5
    n5.next_node = n6
    n6.next_node = n7
    n7.next_node = n8
    n8.next_node = n9
    n9.next_node = n5

    print("does Linked list has a loop ? " + str(has_loop(n0)))
