'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

link -> https://leetcode.com/problems/reverse-linked-list/

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head):

        if head is None or head.next is None:
            return head

        prev = None
        curr = head
        nxt = curr.next
        while nxt is not None:
            tmp = nxt.next
            curr.next = prev
            nxt.next = curr

            prev = curr
            curr = nxt
            nxt = tmp

        return curr
