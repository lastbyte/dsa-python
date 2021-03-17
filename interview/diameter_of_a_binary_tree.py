"""

Question :
    Given the root of a binary tree return the diameter of the binary tree?
    diameter is defined as Maximum number of nodes present in any path of a
    binary tree.

    eg :

Constructed binary tree is
              1
            /   \
          2      3
        /  \
      4     5
     /    /  \
    10   6    7
   /      \
  11       8
            \
             9

diameter of this tree is 8 node 11 to node 9

@author Nishant Kumar

"""


def test():
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

    print("diameter of tree is " + str(diameter(n1)))


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(binary_tree: BinaryTree):
    """

        :param binary_tree:
        :return: integer value

        either the path with maximum nodes is present in the left , right subtree or it
        passes through the node

        we call it recursively for left subtree and the right subtree to get the height
        of left and right respectively.

        height = maximum (height of right subtree , height of left subtree) + 1
               = 0  if current node is none
    """
    return 0 if (binary_tree is None) else 1 + max(height(binary_tree.left), height(binary_tree.right))


def diameter(binary_tree: BinaryTree):
    """

        :param binary_tree:
        :return: integer value

        either the path with maximum nodes is present in the left , right subtree or it
        passes through the node

        we call it recursively for left subtree and the right subtree to get the maximum
        diameter of left and right respectively.

        maximum_number of nodes in the path
        passing through the current node     = height of right subtree + height of left subtree
                                              + 1

        which ever of the three is greater is the diameter

    """
    return 0 if (binary_tree is None) else max(1 + height(binary_tree.left) + height(binary_tree.right),
                                               diameter(binary_tree.left), diameter(binary_tree.right))


if __name__ == "__main__":
    test()
