'''
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

link -> https://leetcode.com/problems/rotate-list/
'''

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def rotateRight(slef, head: ListNode, k: int) -> ListNode:

        #base condition 
        if head is None or head.next is None or k == 0:
            return head;

        #get the lenght of the list
        ptr = head;
        length = 1

        while ptr.next is not None:
            length+=1
            ptr=  ptr.next

        # get to the kth node from end
        
        ptr1 = head
        ptr2 = head
        
        # change k if it is larger than the length os the list
        k = k%length
        
        if k == 0:
            return head
        #take a counter for k
        counter = 0
        while counter < k:
            ptr1 = ptr1.next
            counter+=1
        
        while ptr1.next is not None:
            ptr2 = ptr2.next
            ptr1 = ptr1.next;
        
        ptr1.next = head
        head = ptr2.next
        ptr2.next = None
        return head


if __name__ == "__main__":
    solution = Solution();
    head = ListNode(1);
    head.next = ListNode(2);
    head.next.next = ListNode(3);
    head.next.next.next = ListNode(4);
    head.next.next.next.next = ListNode(5);
    head.next.next.next.next.next = ListNode(6);

    result = solution.rotateRight(head, 2)
