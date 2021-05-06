'''
Given a linked list, swap every two adjacent nodes and return its head.

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

link -> https://leetcode.com/problems/swap-nodes-in-pairs/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_in_pairs(head, k):
    itr = head
    length = 0
    while itr is not None:
        length += 1
        itr = itr.next

    return reverse(head, 2, length)


def reverse(head, k, length):

    if head is None or head.next is None:
        return head

    if length < k:
        return head

    prev = None
    curr = head
    nxt = None
    i = 0
    while curr is not None and i < k:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        i += 1
    if (nxt is not None):
        head.next = reverse(nxt, k, length - k)
    return prev


def print_list(head):
    itr = head
    while itr is not None:
        print("{} ->".format(itr.val), end="")
        itr = itr.next
    print('None', end="\n")


if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    result = swap_in_pairs(head, 3)

    print_list(result)
