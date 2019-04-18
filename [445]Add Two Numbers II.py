# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
#
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
#
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, first: ListNode, second: ListNode) -> ListNode:
        if not first:
            return second
        if not second:
            return first

        first_value = 0
        second_value = 0

        while first:
            first_value = (10 * first_value) + first.val
            first = first.next

        while second:
            second_value = (10 * second.val) + second.val
            second = second.next

        node_sum = str(first_value + second_value)

        dummy = traversal = ListNode(-1)
        for item in node_sum:
            traversal.next = ListNode(int(item))
            traversal = traversal.next
        return dummy.next
