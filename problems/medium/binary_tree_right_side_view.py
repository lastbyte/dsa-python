'''
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

link -> https://leetcode.com/problems/binary-tree-right-side-view/
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def right_view(self, root):
        rv = []
        if root is None:
            return

        queue = []

        queue.append(root)
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                elem = queue.pop(0)
                if i == 0:
                    rv.append(elem.val)
                if elem.right is not None:
                    queue.append(elem.right)
                if elem.left is not None:
                    queue.append(elem.left)

        return rv

    def right_view_1(self, root, level, max_level, rv):
        if root is None:
            return

        if (level > max_level[0]):
            max_level[0] = level
            rv.append(root.val)

        if root.right is not None:
            self.right_view_1(root.right, level + 1, max_level, rv)
        if root.left is not None:
            self.right_view_1(root.left, level + 1, max_level, rv)
        return rv


# Driver Code
if __name__ == '__main__':
    root = Node(4)
    root.left = Node(5)
    root.right = Node(2)
    root.right.right = Node(1)
    root.right.left = Node(3)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    print(Solution().right_view(root))
    print(Solution().right_view_1(root, 1, [0], []))
