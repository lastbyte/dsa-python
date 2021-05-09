'''
Given a Binary Tree, print left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from left side.

Examples: 

Input : 
                 1
               /   \
              2     3
             / \     \
            4   5     6             
Output : 1 2 4

Input :
        1
      /   \
    2       3
      \   
        4  
          \
            5
             \
               6
Output :1 2 4 5 6

link -> https://www.geeksforgeeks.org/print-left-view-binary-tree/

'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def left_view(self, root):
        lv = []
        if root is None:
            return

        queue = []

        queue.append(root)
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                elem = queue.pop(0)
                if i == 0:
                    lv.append(elem.val)
                if elem.left is not None:
                    queue.append(elem.left)
                if elem.right is not None:
                    queue.append(elem.right)

        return lv

    def left_view_1(self, root, level, max_level, lv):
        if root is None:
            return

        if level > max_level[0]:
            lv.append(root.val)
            max_level[0] = level

        self.left_view_1(root.left, level + 1, max_level, lv)
        self.left_view_1(root.right, level + 1, max_level, lv)
        return lv
