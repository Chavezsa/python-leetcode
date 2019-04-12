# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def convert_sum(self, sum: int) -> (int, int):
        return (sum % 10, 1) if sum >= 10 else (sum, 0)

    def addTwoNumbers(self, first: ListNode, second: ListNode) -> ListNode:

        if first and not second:
            return first
        if not first and second:
            return second
        extra = 0
        dummy_node = ListNode(-1)
        moved_node = dummy_node
        # 也可以是用while first or second
        while first and second:
            temp_sum, extra = self.convert_sum(first.val + second.val + extra)

            moved_node.next = ListNode(temp_sum)
            moved_node = moved_node.next
            first = first.next
            second = second.next

        while first:
            temp_sum, extra = self.convert_sum(first.val + extra)
            moved_node.next = ListNode(temp_sum)
            moved_node = moved_node.next
            first = first.next
        while second:
            temp_sum, extra = self.convert_sum(second.val + extra)
            moved_node.next = ListNode(temp_sum)
            moved_node = moved_node.next
            second = second.next

        if extra == 1:
            moved_node.next = ListNode(extra)
        return dummy_node.next