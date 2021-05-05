
class Node:

    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value;
        self.left = left
        self.right = right
        self.parent = parent


##########################
#       10
#      /   \
#     8     2
#    / \   /
#   3   5 2
#
###########################
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.right.left = Node(2)


def pre_order_traversal(root):
    if root is not None :
        print(root.value)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def post_order_traversal(root):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value)


def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.value)
        in_order_traversal(root.right)


def next_node(tree, target, found, ret_node):

    if tree is not None and ret_node is None:
        next_node(tree.left, target, found, ret_node)
        print("current node is : {0} "
              "value fo found is : {1} "
              "the value of return node is : {2}".format(str(tree.value), str(found), str(ret_node)))
        if found is True and ret_node is None:
            ret_node = tree
        if tree.value == target:
            found = True
        next_node(tree.right, target, found, ret_node)


# pre_order_traversal(root)
in_order_traversal(root)
# post_order_traversal(root)
ret_node = None
found = False
next_node(root, 8, found, ret_node)
print(" next node of node with value 8 is " + str(ret_node.value))
