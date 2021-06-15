# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        if index > 0:
            root.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        if index < len(preorder)-1:
            root.right = self.buildTree(preorder[index+1:], inorder[index+1:])

        return root
