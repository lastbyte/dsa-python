'''
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

 

Example 1:

        3
       / \
      /   \     
     1     4
      \
       2

Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:

        5
       / \
      /   \     
     3     6
    / \
   2   4
  /
 1


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

link -> https://leetcode.com/problems/kth-smallest-element-in-a-bst/

'''
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
