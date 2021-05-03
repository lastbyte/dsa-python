from pprint import pprint


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_view(root : Node):
    lv = []
    if root is None:
        return

    queue = []

    queue.append(root)
    while len(queue) > 0 :
        n = len(queue)
        for i in range(n):
            elem = queue.pop(0)
            if i == 0:
                lv.append(elem.val)
            if elem.left is not None:
                queue.append(elem.left)
            if elem.right is not None:
                queue.append(elem.right)

    return lv


def left_view_1(root: Node, level, max_level, lv):
    if root is None:
        return

    if level > max_level[0] :
        lv.append(root.val)
        max_level[0] = level

    left_view_1(root.left, level+1, max_level, lv)
    left_view_1(root.right, level+1, max_level, lv)


# Driver Code
if __name__ == '__main__':
    root = Node(4)
    root.left = Node(5)
    root.right = Node(2)
    root.right.right = Node(1)
    root.right.left = Node(3)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    pprint(left_view(root))
    lv = []
    left_view_1(root, 1, [0], lv)
    pprint(lv)

