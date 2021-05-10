'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:

            3
           / \
          9  20
            /  \
           15   7   

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

link -> https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def level_order_traversal(self,root):
        traversal_list = []
        if root is None:
            return traversal_list
        mem_queue = []
        mem_queue.append(root)

        while len(mem_queue) > 0 :
            tmp = mem_queue.copy()
            mem_queue = []
            traversal_list.append([elem.val for elem in tmp])
            for elem in tmp:
                if elem.left is not None:
                    mem_queue.append(elem.left)
                if elem.right is not None:
                    mem_queue.append(elem.right)
        return traversal_list

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = solution.level_order_traversal(None)
    print(result)

