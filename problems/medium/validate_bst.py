'''
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

link -> https://leetcode.com/problems/validate-binary-search-tree/
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def validate_bst(self, root: TreeNode):
        if root is None :
            return True
        else:
            return self.validate_bst_util(root,-float('inf'),float('inf'))

    def validate_bst_util(self,root: TreeNode,min_val:int, max_val:int):
        is_left_valid = root.left is None or self.validate_bst_util(root.left,min_val,root.val)
        is_right_valid = root.right is None or self.validate_bst_util(root.right,root.val,max_val)
        is_node_valid = min_val < root.val < max_val
        return is_left_valid and is_right_valid and is_node_valid

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(0)
    result = solution.validate_bst(root)
    print(result)
