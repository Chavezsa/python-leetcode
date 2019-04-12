# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 解法1， 我的解法， 不够Pythonic
    def mergeTwoLists1(self, first: ListNode, second: ListNode) -> ListNode:
        dummy = ListNode(-1)
        traversed = dummy
        while first or second:
            if first and not second:
                traversed.next = first
                break
            elif not first and second:
                traversed.next = second
                break
            else:
                if first.val < second.val:
                    traversed.next = ListNode(first.val)
                    first = first.next
                else:
                    traversed.next = ListNode(second.val)
                    second = second.next
            traversed = traversed.next

        return dummy.next

    # comes from https://leetcode.com/problems/merge-two-sorted-lists/discuss/9771/Simple-5-lines-Python
    def mergeTwoLists2(self, first: ListNode, second: ListNode) -> ListNode:
        if first and second:
            if first.val > second.val:
                first, second = second, first
            first.next = self.mergeTwoLists2(first.next, second)

        return first or second

    # comes from https://leetcode.com/problems/merge-two-sorted-lists/discuss/9771/Simple-5-lines-Python
    def mergeTwoLists3(self, first: ListNode, second: ListNode) -> ListNode:
        if not first or second and first.val > second.val:
            first, second = second, first
        if first:
            first.next = self.mergeTwoLists(first.next, second)
        return first
