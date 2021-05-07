'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_from_last(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None

        prev, ptr1, ptr2, counter = None, head, head, 1
        while ptr2 is not None and counter < n:
            ptr2 = ptr2.next
            counter += 1

        while ptr2.next is not None:
            prev = ptr1
            ptr2 = ptr2.next
            ptr1 = ptr1.next

        if prev is None:
            return head.next
        else:
            prev.next = ptr1.next

        return head

    def pprint(self, head: ListNode):
        itr = head
        while itr is not None:
            print("{}->".format(itr.val), end="")
            itr = itr.next


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    result = solution.delete_from_last(head, 2)
    solution.pprint(result)
