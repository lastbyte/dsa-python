# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        traversal = []
        return self.levelOrderBottomUtil(root, traversal)[::-1]

    def levelOrderBottomUtil(self, root: TreeNode, traversal: List[List[int]]) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]

        while len(queue) > 0:
            tmp_queue = []
            lst = []
            while len(queue) > 0:
                elem = queue.pop(0)
                if elem.left is not None:
                    tmp_queue.append(elem.left)
                if elem.right is not None:
                    tmp_queue.append(elem.right)
                lst.append(elem.val)
            traversal.append(lst.copy())
            queue = tmp_queue.copy()
        return traversal
