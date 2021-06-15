# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        param = [False]
        self.pathSumUtil(root, targetSum, param)
        return param[0]

    def pathSumUtil(self, root, targetSum, param):
        if not param[0]:
            if root is None:
                return
            if root.left is None and root.right is None:
                if targetSum == root.val:
                    param[0] = True
            elif root is not None:
                self.pathSumUtil(root.left, targetSum-root.val, param)
                self.pathSumUtil(root.right, targetSum-root.val, param)