'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

link -> https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_path_sum(self, root: TreeNode):
        max_sum = [-float('inf')]
        self.max_sum_path_util(root, max_sum)
        return max_sum[0]

    def max_sum_path_util(self, root: TreeNode, max_sum: List[int]):
        #base case
        if root is None:
            return 0

        sum_from_root_to_left_child = self.max_sum_path_util(root.left, max_sum)
        sum_from_root_to_right_child = self.max_sum_path_util(root.right, max_sum)

        if root.val > max_sum[0]:
            max_sum[0] = root.val
        if root.val + sum_from_root_to_left_child > max_sum[0]:
            max_sum[0] = root.val + sum_from_root_to_left_child
        if root.val + sum_from_root_to_right_child > max_sum[0]:
            max_sum[0] = root.val + sum_from_root_to_right_child
        if root.val + sum_from_root_to_left_child + sum_from_root_to_right_child > max_sum[0]:
            max_sum[0] = root.val + sum_from_root_to_left_child + sum_from_root_to_right_child

        return max(root.val, root.val + max(sum_from_root_to_left_child, sum_from_root_to_right_child))


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(9)
    root.left = TreeNode(6)
    root.right = TreeNode(-3)
    root.right.left = TreeNode(-6)
    root.right.right = TreeNode(2)
    root.right.right.left = TreeNode(2)
    root.right.right.left.left = TreeNode(-6)
    root.right.right.left.right = TreeNode(-6)
    root.right.right.left.left.left = TreeNode(-6)
    result = solution.max_path_sum(root)
    print(result)