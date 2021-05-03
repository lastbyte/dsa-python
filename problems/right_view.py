from pprint import pprint


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_view(root : Node):
    rv = []
    if root is None:
        return

    queue = []

    queue.append(root)
    while len(queue) > 0 :
        n = len(queue)
        for i in range(n):
            elem = queue.pop(0)
            if i == 0:
                rv.append(elem.val)
            if elem.right is not None:
                queue.append(elem.right)
            if elem.left is not None:
                queue.append(elem.left)

    return rv


def right_view_1(root : Node, level, max_level, rv):
    if root is None:
        return

    if (level > max_level[0]):
        max_level[0] = level
        rv.append(root.val)

    if root.right is not None:
        right_view_1(root.right, level+1, max_level,rv)
    if root.left is not None:
        right_view_1(root.left, level+1,max_level,rv)

# Driver Code
if __name__ == '__main__':
    root = Node(4)
    root.left = Node(5)
    root.right = Node(2)
    root.right.right = Node(1)
    root.right.left = Node(3)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    pprint(right_view(root))
    rv=[]
    right_view_1(root, 1, [0],rv)
    pprint(rv)

