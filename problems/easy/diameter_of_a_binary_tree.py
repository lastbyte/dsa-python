"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.The length of a path between two nodes is repres-
ented by the number of edges between them.

Example 1:

                1
               / \
              2   3
             / \
            4   5

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
                1
                 \
                  2

Input: root = [1,2]
Output: 1e

Example 3:

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

diameter of this tree is 7 node 11 to node 9

@author Nishant Kumar

link -> https://leetcode.com/problems/diameter-of-binary-tree/

"""



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter(root):

    diameter1 = height(root.left) + height(root.right)

    if root.left is not None:
        diameter1 = max(diameter1, diameter(root.left))
    if root.right is not None:
        diameter1 = max(diameter1, diameter(root.right))

    return diameter1


def height(root):
    return 0 if (
        root is None) else 1 + max(height(root.left), height(root.right))


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = diameter(root)
    print(result)
