'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:

            3
           / \
          9  20
            /  \
           15   7   

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

link -> https://leetcode.com/problems/minimum-depth-of-binary-tree/

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimum_depth(self, root):
        return 0 if root is None else self.min_depth_util(root,1,[float('inf')])

    def min_depth_util(self, root, depth, max_depth):
        if root is not None:
            if depth < max_depth[0] and root.left is None and root.right is None:
                max_depth[0] = depth
            self.min_depth_util(root.left,depth+1, max_depth)
            self.min_depth_util(root.right, depth+1, max_depth)
        return max_depth[0]


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(7)
    result = solution.minimum_depth(root)
    print(result)