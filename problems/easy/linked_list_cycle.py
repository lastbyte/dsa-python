'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:

3 -> 2 -> 0 -> -4 -:
          |________| 

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

1 -> 2 -:
|________| 

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

1 -> None

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

link -> https://leetcode.com/problems/linked-list-cycle/
'''


class Solution:
    def has_loop(self, root):
        # initialize loop_found to false
        loop_found = False
        if root is None or root.next_node is None:
            return loop_found

        slow_ptr, fast_ptr = root, root
        # move to next position for 1 time
        slow_ptr, fast_ptr = slow_ptr.next_node, fast_ptr.next_node if fast_ptr.next_node is None else fast_ptr.next_node.next_node
        while slow_ptr is not None and fast_ptr is not None and not loop_found:
            if slow_ptr == fast_ptr:
                loop_found = True
            else:
                slow_ptr, \
                fast_ptr = slow_ptr.next_node, \
                        fast_ptr.next_node.next_node \
                            if fast_ptr.next_node is not None \
                            else fast_ptr.next_node

        return loop_found


class Node:
    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next
