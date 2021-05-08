

class BST:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data)

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print(self.data)
        if self.right is not None:
            self.right.print_bst()


b = BST(10)
b.insert(2)
b.insert(15)
b.insert(5)
b.insert(12)
b.insert(1)

b.print_bst()