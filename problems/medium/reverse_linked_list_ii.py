'''
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

link -> https://leetcode.com/problems/reverse-linked-list-ii/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        stringval = ''
        itr = self
        while itr is not None:
            stringval += str(itr.val) + "->"
            itr = itr.next
        return stringval


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        listItr = head
        prev = None
        while left > 1:
            prev = listItr
            listItr = listItr.next
            left = left - 1
            right = right - 1

        if prev is not None:
            prev.next = self.reverse(prev.next, right)
            return head
        else:
            return self.reverse(head, right)

    def reverse(self, head: ListNode, k: int) -> ListNode:
        prev = None
        curr = head

        while k > 0:
            tmp = ListNode(curr.val, curr.next)
            curr.next = prev
            prev = curr
            curr = tmp.next
            k = k - 1

        head.next = curr
        return prev

    def printList(self, head: ListNode):
        itr = head
        while itr is not None:
            print(f'{itr.val} -> ')
            itr = itr.next


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    k = Solution().reverseBetween(l, 1, 4)
    Solution().printList(k)
