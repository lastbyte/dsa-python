'''
Given a binary tree and a number, return true if the tree has a root-to-leaf path such that adding up all the values along the 
path equals the given number. Return false if no such path can be found. 

               10
             /    \
            8      2
          / \     /
         3   5   2


For example, in the above tree root to leaf paths exist with following sums.
21 –> 10 – 8 – 3 
23 –> 10 – 8 – 5 
14 –> 10 – 2 – 2
So the returned value should be true only for numbers 21, 23 and 14. For any other number, returned value should be false

link -> https://www.geeksforgeeks.org/root-to-leaf-path-sum-equal-to-a-given-number/

'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_path_sum(root, target, current_path_sum):
    if root is None and current_path_sum == target:
        return True
    if root is not None:
        return is_path_sum(root.left, target, current_path_sum + root.value) or \
               is_path_sum(root.right, target, current_path_sum + root.value)
    return False


if __name__=="__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.right = Node(5)
    root.left.left = Node(3)
    root.right.left = Node(2)

    is_sum_present = is_path_sum(root, 21, 0)
    print("is 21 any of the path sums ? " + str(is_sum_present))
    is_sum_present = is_path_sum(root, 20, 0)
    print("is 20 any of the path sums ? " + str(is_sum_present))
    is_sum_present = is_path_sum(root, 14, 0)
    print("is 14 any of the path sums ? " + str(is_sum_present))
    is_sum_present = is_path_sum(root, 23, 0)
    print("is 23 any of the path sums ? " + str(is_sum_present))
    is_sum_present = is_path_sum(root, 16, 0)
    print("is 16 any of the path sums ? " + str(is_sum_present))
