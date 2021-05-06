'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 3:
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:
Input: head = [1], k = 1
Output: [1]

link -> https://leetcode.com/problems/reverse-nodes-in-k-group/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_in_groups(head,k):
    itr = head
    length=0
    while itr is not None:
        length+=1
        itr = itr.next

    return reverse(head,k,length)

def reverse(head, k, length):

    if head is None or head.next is None:
        return head

    if length < k :
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
        head.next = reverse(nxt, k, length-k)
    return prev



def print_list(head):
    itr = head
    while itr is not None:
        print("{} ->".format(itr.val), end="")
        itr = itr.next
    print('None', end="\n")

if __name__ == "__main__" :

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    result  = reverse_in_groups(head, 3)

    print_list(result)
