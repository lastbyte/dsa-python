'''
82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

link -> https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        nxt = head.next
        return_val = head
        while nxt is not None:
            count = 0
            while nxt is not None and curr.val == nxt.val:
                curr = nxt
                nxt = nxt.next
                count += 1

            if count == 0:
                prev = curr
                curr = nxt
                nxt = nxt.next if nxt is not None else nxt.next

            elif count > 0 and prev is None:
                return_val = nxt
                curr = return_val
                nxt = curr.next if curr is not None else curr
            elif count > 0 and prev is not None:
                prev.next = nxt
                curr = nxt
                nxt = nxt.next if nxt is not None else nxt

        return return_val
