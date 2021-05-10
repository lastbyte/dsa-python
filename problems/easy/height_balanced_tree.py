'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:
            3
           / \
          9  20
            /  \
           15   7   

Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:

                  1
                 / \
                2   2
               / \
              3   3
             / \
            4   4        

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_height_balanced(self, root):
        if root is None:
            return True
        l_height = self.height(root.left)
        r_height = self.height(root.right)
        return abs(l_height - r_height) <= 1 and self.is_height_balanced(root.left) and self.is_height_balanced(root.right)

    def height(self, root):
        return 0 if root is None else (1 + max(self.height(root.left), self.height(root.right)))


elems = [3, 9, 20, None, None, 15, 7]

if __name__ == "__main__":
    solution = Solution()
    #elems = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(7)

    
    result = solution.is_height_balanced(root)
    print(result)
