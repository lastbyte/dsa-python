'''
given root node of a binary tree return the in-order traversal of the nodes 

            3
           / \
          9  20
            /  \
           15   7   

link -> https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
'''


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def in_order_traversal(self, root, traversal):
        if root is not None:
            self.in_order_traversal(root.left,traversal)
            traversal.append(root.val)
            self.in_order_traversal(root.right,traversal)
        return traversal

    def in_order_traversal_iterative(self,root):
        traversal = []
        if root is None:
            return traversal
        mem_stack = []
        elem = root
        done = False
        while not done:
            if elem is not None:
                mem_stack.append(elem)
                elem = elem.left
            elif len(mem_stack) > 0:
                elem = mem_stack.pop()
                traversal.append(elem.val)
                elem = elem.right
            else:
                done = True

        return traversal

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = solution.in_order_traversal(root,[])
    print(result)
    result = solution.in_order_traversal_iterative(root)
    print(result)