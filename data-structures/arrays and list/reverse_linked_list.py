# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def reverse(head):

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