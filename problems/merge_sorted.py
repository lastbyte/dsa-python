class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    ret_list = None
    ret_itr = None
    while l1 is not None and l2 is not None:

        if l1.val < l2.val :
            tmp_node = ListNode(l1.val)
            l1 = l1.next
        else:
            tmp_node = ListNode(l2.val)
            l2 = l2.next

        if ret_list is None:
            ret_list = tmp_node
            ret_itr = ret_list
        else:
            ret_itr.next = tmp_node
            ret_itr = ret_itr.next

    while l1 is not None:
        tmp_node = ListNode(l1.val)
        l1 = l1.next
        if ret_list is None:
            ret_list = tmp_node
            ret_itr = ret_list
        else:
            ret_itr.next = tmp_node
            ret_itr = ret_itr.next

    while l2 is not None:
        tmp_node = ListNode(l2.val)
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