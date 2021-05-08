class tree_node:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = None
        self.right = None


class avl_tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        self.root = self.insert_util(self.root, val)

    def insert_util(self, root, val):
        if root is None:
            root = tree_node(val)

        elif (val < root.val):
            root.left = self.insert_util(root.left, val)
        else:
            root.right = self.insert_util(root.right, val)

        l_height = self.height(root.left)
        r_height = self.height(root.right)

        if (l_height - r_height > 1):
            if (val < root.left.val):
                return self.rotate_right(root)
            if (val > root.left.val):
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        elif (l_height - r_height < -1):
            if (val > root.right.val):
                return self.rotate_left(root)
            if (val < root.right.val):
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
        return root

    def rotate_left(self, root):
        new_root = root.right
        tmp = new_root.left
        new_root.left = root
        root.right = tmp
        return new_root

    def rotate_right(self, root):
        new_root = root.left
        tmp = new_root.right
        new_root.right = root
        root.left = tmp
        return new_root

    def height(self, root):
        return 0 if root is None else 1 + max(self.height(root.left),
                                              self.height(root.right))

    def search(self, key):
        return self.search_util(self.root, key)

    def search_util(self, root, key):
        if root is None:
            return None

        if root.val == key:
            return root

        return self.search_util(root.left, key) or self.search_util(
            root.right, key)

    
    def print(self):


if __name__ == "__main__":
    avl = avl_tree()
    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    avl.insert(4)
    avl.insert(5)
    avl.insert(6)
    avl.insert(7)
    avl.insert(8)
    avl.insert(9)
    avl.insert(10)
    avl.insert(11)
    avl.insert(12)
    root = avl.root
    avl.print()
