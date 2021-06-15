# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []
        self.pathSumUtil(root, targetSum, [], paths)
        return paths

    def pathSumUtil(self, root, targetSum, curr_path, paths):
        if root is None:
            return
        if root.left is None and root.right is None:
            if targetSum == root.val:
                curr_path.append(root.val)
                paths.append(curr_path.copy())
                curr_path.pop()
        elif root is not None:
            curr_path.append(root.val)
            self.pathSumUtil(root.left, targetSum - root.val, curr_path, paths)
            self.pathSumUtil(root.right, targetSum - root.val, curr_path, paths)
            curr_path.pop()
