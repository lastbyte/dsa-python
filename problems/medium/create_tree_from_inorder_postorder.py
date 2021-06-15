# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 1:
            return TreeNode(postorder[0])
        root = TreeNode(postorder[len(postorder) - 1])
        index = inorder.index(postorder[len(postorder) - 1])
        if index > 0:
            root.left = self.buildTree(inorder[0:index], postorder[0:index])
        if index < len(postorder) - 1:
            root.right = self.buildTree(inorder[index + 1:], postorder[index:len(postorder)-1])

        return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

Solution().buildTree(inorder, postorder)