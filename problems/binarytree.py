class BinaryTree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def pre_order_traversal(self):
        if self is not None:
            print(self.value, end="-->")
            if self.left is not None:
                self.left.pre_order_traversal()
            if self.right is not None:
                self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self is not None:
            if self.left is not None:
                self.left.post_order_traversal()
            if self.right is not None:
                self.right.post_order_traversal()
            print(self.value, end="-->")

    def in_order_traversal(self):
        if self is not None:
            if self.left is not None:
                self.left.in_order_traversal()
            print(self.value, end="-->")
            if self.right is not None:
                self.right.in_order_traversal()


n1 = BinaryTree(1)
n2 = BinaryTree(2)
n3 = BinaryTree(3)
n4 = BinaryTree(4)
n5 = BinaryTree(5)
n6 = BinaryTree(6)
n7 = BinaryTree(7)
n8 = BinaryTree(8)
n9 = BinaryTree(9)
n10 = BinaryTree(10)
n11 = BinaryTree(11)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.left = n10
n10.left = n11
n5.left = n6
n5.right = n7
n6.right = n8
n8.right = n9

n1.pre_order_traversal()
print("")
n1.in_order_traversal()
print("")
n1.post_order_traversal()