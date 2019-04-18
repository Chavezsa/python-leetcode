# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed. 
#
# 
#
# Example: 
#
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = traverse = ListNode(-1)
        dummy.next = head

        while traverse.next and traverse.next.next:
            tmp = traverse.next
            traverse.next = tmp.next
            tmp.next = traverse.next.next
            traverse.next.next = tmp
            traverse = tmp

        return dummy.next

    def swapPairs1(self, head: ListNode) -> ListNode:
        if head and head.next:
            dummy = head
            head = head.next
            dummy.next = head.next
            head.next = dummy
            head.next.next = self.swapPairs1(head.next.next)

        return head

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)

    l1.next = l2
    l2.next = l3
    l3.next = l4

    node = Solution().swapPairs(l1)
    while node:
        print(node.val)
        node = node.next
