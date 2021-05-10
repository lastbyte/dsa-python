'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

            3
           / \
          9  20
            /  \
           15   7   

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1

link -> https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maximum_depth(self, root):
        return 0 if root is None else self.maximum_depth_util(root,1,[0])

    def maximum_depth_util(self, root, depth, max_depth):
        if root is not None:
            if depth > max_depth[0]:
                max_depth[0] = depth
            self.maximum_depth_util(root.left,depth+1, max_depth)
            self.maximum_depth_util(root.right, depth+1, max_depth)
        return max_depth[0]

    def maximum_depth_1(self,root):
        return self.height(root)

    def height(self,root):
        return 0 if root is None else 1 + max(self.height(root.left), self.height(root.right))


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = solution.maximum_depth_1(root)
    print(result)
