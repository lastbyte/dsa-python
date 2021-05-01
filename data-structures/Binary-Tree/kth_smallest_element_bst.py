# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.inOrder(root)[k-1]

    def inOrder(self, root: TreeNode) -> int:
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right) if root else []
