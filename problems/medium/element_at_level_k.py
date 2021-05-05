from pprint import pprint


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def element_at_level_k(root: Node, target_level: int):
    lv = []
    if root is None:
        return

    queue = []
    level = 0
    queue.append(root)
    while len(queue) > 0:
        level+=1
        n = len(queue)
        for i in range(n):
            elem = queue.pop(0)
            if level == target_level:
                lv.append(elem.val)
            if elem.left is not None:
                queue.append(elem.left)
            if elem.right is not None:
                queue.append(elem.right)

    return lv

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(5)
    root.right = Node(2)
    root.right.right = Node(1)
    root.right.left = Node(3)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    pprint(element_at_level_k(root, 2))


