'''
given root node of a binary tree return the pre-order traversal of the nodes 

            3
           / \
          1  7
            /  \
           5    9
          / \  / \ 
         4  6 8  10
link -> https://www.geeksforgeeks.org/iterative-preorder-traversal/
'''


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pre_order_traversal(self, root, traversal):
        if root is not None:
            traversal.append(root.val)
            self.pre_order_traversal(root.left, traversal)
            self.pre_order_traversal(root.right, traversal)
        return traversal

    def pre_order_traversal_iterative(self, root):
        traversal = []
        if root is None:
            return traversal

        mem_stack = []
        mem_stack.append(root)
        while len(mem_stack) > 0:
            elem = mem_stack.pop()
            traversal.append(elem.val)
            if elem.right is not None:
                mem_stack.append(elem.right)
            if elem.left is not None:
                mem_stack.append(elem.left)

        return traversal


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(7)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(9)
    root.right.left.left = TreeNode(4)
    root.right.left.right = TreeNode(6)
    root.right.right.right = TreeNode(10)   
    result = solution.pre_order_traversal(root, [])
    print(result)
    result = solution.pre_order_traversal_iterative(root)
    print(result)