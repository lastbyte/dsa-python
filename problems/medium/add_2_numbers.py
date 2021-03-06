'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

source -> https://leetcode.com/problems/add-two-numbers/

'''

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def add_2_numbers( l1 : ListNode , l2: ListNode):
    res_list = None
    # define the iterators
    itr1 = l1
    itr2 = l2
    itr3 = res_list

    carry = 0
    while itr1 is not None and itr2 is not None :
        res_node = ListNode()
        res_sum = (carry + itr1.val + itr2.val)
        node_value = res_sum // 10
        carry = res_sum % 10
        res_node.val = node_value
        if res_list is None:
            res_list = res_node
            itr3 = res_list
        else:
            itr3.next = res_node
            itr3 = itr3.next

        itr1 = itr1.next
        itr2 = itr2.next

    while itr1 is not None :
        res_node = ListNode()
        res_sum = (carry + itr1.val + itr2.val)
        node_value = res_sum // 10
        carry = res_sum % 10
        res_node.val = node_value
        itr3.next = res_node
        itr3 = itr3.next
        itr1 = itr1.next

    while itr2 is not None :
        res_node = ListNode()
        res_sum = (carry + itr1.val + itr2.val)
        node_value = res_sum // 10
        carry = res_sum % 10
        res_node.val = node_value
        itr3.next = res_node
        itr3 = itr3.next
        itr2 = itr2.next

    if carry > 0 :
        res_node = ListNode(carry)
        itr3.next = res_node

    return res_list
