'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

 

Example 1:

3 -> 2 -> 0 -> -4 -:
          |________| 

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

1 -> 2 -:
|________|

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

1 -> None

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list

link -> https://leetcode.com/problems/linked-list-cycle-ii/

'''


class Solution:
    def has_loop(self, head):
        # initialize loop_found to false
        loop_found = False
        if head is None or head.next is None:
            return loop_found

        slow_ptr, fast_ptr = head, head
        # move to next position for 1 time
        slow_ptr, fast_ptr = slow_ptr.next, fast_ptr.next if fast_ptr.next is None else fast_ptr.next.next
        while slow_ptr is not None and fast_ptr is not None and not loop_found:
            if slow_ptr == fast_ptr:
                loop_found = True
            else:
                slow_ptr, \
                fast_ptr = slow_ptr.next, \
                        fast_ptr.next.next \
                            if fast_ptr.next is not None \
                            else fast_ptr.next

        if loop_found:
            slow_ptr = head
            pos = 0
            while slow_ptr != fast_ptr:
                slow_ptr, fast_ptr = slow_ptr.next, fast_ptr.next
                pos += 1
            return pos

        return None


class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next
