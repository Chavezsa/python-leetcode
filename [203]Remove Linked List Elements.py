# Remove all elements from a linked list of integers that have value val.
#
# Example: 
#
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements1(self, head: ListNode, val: int) -> ListNode:
        dummy = traverse = ListNode(-1)
        while head:
            if head.val != val:
                traverse.next = head
                traverse = traverse.next
            head = head.next
        traverse.next = None
        return dummy.next

    def removeElements2(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        if head.val == val:
            head = self.removeElements2(head.next, val)
        else:
            head.next = self.removeElements2(head.next, val)

        return head
