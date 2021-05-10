'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:
            1
           / \
          /   \     
         2     2
        / \   / \
       3   4 4   3

Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:

            1
           / \
          2   2
           \   \
            3   3

Input: root = [1,2,2,null,3,null,3]
Output: false

link -> https://leetcode.com/problems/symmetric-tree/
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_symmetric(self,root):
        if root is None:
            return True
        return self.is_inverted(root.left, root.right)

    def is_inverted(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None:
            return False
        if root2 is None and root1 is not None:
            return False
        return self.is_inverted(root1.left , root2.right) and self.is_inverted(root1.right, root2.left) and root1.val == root2.val


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    result = solution.is_symmetric(root)
    print(result)