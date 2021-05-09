'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

 

Example 1:

    10 -> -3 -> 0 -> 5 -> 9

                |

                0
               / \
              /   \
            -3     9
            /     /
           /     /
        -10     5

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

link -> https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_list_to_bst(head):
    node = head
    tree_node = None
    while node is not None:
        tree_node = insert(tree_node, node.val)
        node = node.next
    return tree_node


def insert(tree_node, val):
    if tree_node is None:
        tree_node = TreeNode(val)

    elif (val < tree_node.val):
        tree_node.left = insert(tree_node.left, val)
    else:
        tree_node.right = insert(tree_node.right, val)

    l_height = height(tree_node.left)
    r_height = height(tree_node.right)

    if (l_height - r_height > 1):
        if (val < tree_node.left.val):
            return rotate_right(tree_node)
        if (val > tree_node.left.val):
            tree_node.left = rotate_left(tree_node.left)
            return rotate_right(tree_node)
    elif (l_height - r_height < -1):
        if (val > tree_node.right.val):
            return rotate_left(tree_node)
        if (val < tree_node.right.val):
            tree_node.right = rotate_right(tree_node.right)
            return rotate_left(tree_node)
    return tree_node


def rotate_left(root):
    new_root = root.right
    tmp = new_root.left
    new_root.left = root
    root.right = tmp
    return new_root


def rotate_right(root):
    new_root = root.left
    tmp = new_root.right
    new_root.right = root
    root.left = tmp
    return new_root


def height(root):
    return 0 if root is None else 1 + max(height(root.left), height(
        root.right))


def list_to_bst(head):
    return list_to_bst_util(head)


def list_to_bst_util(head):

    if head is None:
        return None

    if head.next is None:
        return TreeNode(head.val)

    slow_ptr = head
    fast_ptr = head
    prev = None
    while fast_ptr is not None and fast_ptr.next is not None:
        prev = slow_ptr
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next if fast_ptr.next is not None else fast_ptr.next

    prev.next = None
    root = TreeNode(slow_ptr.val)
    root.left = list_to_bst_util(head)
    root.right = list_to_bst_util(slow_ptr.next)

    return root


def level_by_traversal(root):
    lv = []
    if root is None:
        return

    queue = []
    level = 0
    queue.append(root)
    while len(queue) > 0:
        level += 1
        n = len(queue)
        for i in range(n):
            elem = queue.pop(0)
            lv.append(elem.val)
            if elem.left is not None:
                queue.append(elem.left)
            if elem.right is not None:
                queue.append(elem.right)

        lv.append("-")

    return lv


if __name__ == "__main__":
    lst = [-10, -3, 0, 5, 9]
    head = None
    itr = None
    for elem in lst:
        if head is None:
            head = ListNode(elem)
            itr = head
        else:
            itr.next = ListNode(elem)
            itr = itr.next

    result = sorted_list_to_bst(head)
    print(level_by_traversal(result))
