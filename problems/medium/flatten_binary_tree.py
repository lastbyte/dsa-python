# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        if root.left is not None:
            tmp = root.right
            root.right = root.left
            k = root.right
            while k.right is not None:
                k = k.right
            k.right = tmp

        self.flatten(root.left)
        self.flatten(root.right)
