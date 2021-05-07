'''Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]

link -> https://leetcode.com/problems/merge-two-sorted-lists
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    ret_list = None
    ret_itr = None
    while l1 is not None and l2 is not None:

        if l1.val < l2.val :
            tmp_node = l1
            l1 = l1.next
        else:
            tmp_node = l2
            l2 = l2.next

        if ret_list is None:
            ret_list = tmp_node
            ret_itr = ret_list
        else:
            ret_itr.next = tmp_node
            ret_itr = ret_itr.next

    while l1 is not None:
        tmp_node = l1
        l1 = l1.next
        if ret_list is None:
            ret_list = tmp_node
            ret_itr = ret_list
        else:
            ret_itr.next = tmp_node
            ret_itr = ret_itr.next

    while l2 is not None:
        tmp_node = l2
        l2 = l2.next
        if ret_list is None:
            ret_list = tmp_node
            ret_itr = ret_list
        else:
            ret_itr.next = tmp_node
            ret_itr = ret_itr.next

    return ret_list



def printList(l :ListNode) :
    k = l
    while k is not None:
        print(str(k.val) + " -> ", end="")
        k = k.next

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

printList(l1)
print()
printList(l2)
print()
printList(mergeTwoLists(l1,l2))