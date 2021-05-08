'''
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:

Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 
Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
All Nodes will have unique values.

link -> https://leetcode.com/problems/inorder-successor-in-bst/
'''
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_next_node(self, root, target):
        path = self.find_path_till_element(root, target, [])
        if path is None:
            return None
        else:
            for i in range(len(path)):
                if i == 0:
                    if path[i].right is not None:
                        return self.find_min_in_bst(path[i].right)
                else:
                    if path[i].left == path[i - 1]:
                        return path[i]

            return None

    def find_path_till_element(self, tree, target, path):
        if tree is not None:
            if target.val == tree.val:
                path = [tree] + path
                return path
            if target.val < tree.val:
                path = self.find_path_till_element(tree.left, target,
                                                   [tree] + path)
            else:
                path = self.find_path_till_element(tree.right, target,
                                                   [tree] + path)
        return path if len(path) > 0 and path[0].val == target.val else None

    def find_min_in_bst(self, tree):
        if tree is None:
            return None
        if tree.left is None:
            return tree
        else:
            return self.find_min_in_bst(tree.left)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(12)
    root.left.right = Node(9)
    root.left.left = Node(3)
    root.right.left = Node(11)
    sol = Solution()
    target = root.left
    result = sol.find_next_node(root, target)
    print("{} : {}".format(target.val, result.val))
