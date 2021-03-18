def has_loop(root):
    # initialize loop_found to false
    loop_found = False
    if root is None or root.next_node is None:
        return loop_found

    slow_ptr, fast_ptr = root, root
    # move to next position for 1 time
    slow_ptr, fast_ptr = slow_ptr.next_node, fast_ptr.next_node if fast_ptr.next_node is None else fast_ptr.next_node.next_node
    while slow_ptr is not None and fast_ptr is not None and not loop_found:
        if slow_ptr == fast_ptr:
            loop_found = True
        else:
            slow_ptr, fast_ptr = slow_ptr.next_node, fast_ptr.next_node if fast_ptr.next_node is None else fast_ptr.next_node.next_node

    if loop_found:
        slow_ptr = root
        while slow_ptr != fast_ptr:
            slow_ptr, fast_ptr = slow_ptr.next_node, fast_ptr.next_node
        return slow_ptr

    return loop_found;


class Node:
    """
    helper Node class
    """

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    nodes = []
    for i in range(10):
        nodes.append(Node(i))

    for i in range(9):
        nodes[i].next_node = nodes[i + 1]

    nodes[9].next_node = nodes[4]

    print("does Linked list has a loop ? " + str(has_loop(nodes[0])))
