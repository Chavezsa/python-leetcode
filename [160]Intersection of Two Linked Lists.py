# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def get_list_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def getIntersectionNode(self, first: ListNode, second: ListNode) -> ListNode:
        max_len = self.get_list_length(first)
        min_len = self.get_list_length(second)

        if max_len < min_len:
            min_len, max_len = max_len, min_len
            first, second = second, first

        while min_len < max_len:
            first = first.next
            min_len += 1

        while first and second and first != second:
            first = first.next
            second = second.next

        return first

    def getIntersectionNode1(self, first: ListNode, second: ListNode) -> ListNode:
        p = first
        q = second
        while p != q:
            p = p.next if p else second
            q = q.next if q else first
        return p
