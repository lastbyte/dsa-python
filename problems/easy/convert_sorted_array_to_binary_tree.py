# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.sortedArrayToBSTUtil(nums, 0, len(nums)-1)

    def sortedArrayToBSTUtil(self, nums, left, right):

        if left == right:
            return TreeNode(nums[left])
        elif left < right:
            mid = left + (right - left) / 2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBSTUtil(nums, left, mid-1)
            root.right = self.sortedArrayToBSTUtil(nums, mid+1, right)
        else:
            return None
        return root
