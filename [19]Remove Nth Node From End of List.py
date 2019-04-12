# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example: 
#
# 
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# 
#
# Note: 
#
# Given n will always be valid. 
#
# Follow up: 
#
# Could you do this in one pass? 
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法1 先遍历一遍，获取总的链表长度len，然后第二次扫描找出len -n个元素

class Solution:
    def get_length(self, head: ListNode) -> int:
        traversal_node = head
        length = 0
        while traversal_node:
            length += 1
            traversal_node = traversal_node.next
        return length

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = self.get_length(head)

        dummy_node = ListNode(-1)
        dummy_node.next = head
        traversal_node = dummy_node
        start = 0
        while start != length - n:
            traversal_node = traversal_node.next
            start += 1

        if traversal_node.next.next:
            traversal_node.next = traversal_node.next.next
        else:
            traversal_node.next = None

        return dummy_node.next

    def removeNthFromEnd1(self, head: ListNode, n: int):
        dummy_node = ListNode(-1)
        dummy_node.next = head

        previous = dummy_node
        behind = dummy_node
        index = 0

        while index < n + 1:
            previous = previous.next
            index += 1

        while behind and previous:
            behind = behind.next
            previous = previous.next

        if behind.next.next:
            behind.next = behind.next.next
        else:
            behind.next = None
        return dummy_node.next
