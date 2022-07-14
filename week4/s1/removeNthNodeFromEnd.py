# Problem 1: Remove Nth Node from End of List (LeetCode LinkedList Medium 19)
# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Input: 1->2->3->4->5, n = 2
# Output: 1->2->3->5

# Explanation: We remove the second node from the end, the node with value 4
# Using two pointer and a dummy node

#               1->2->3->4->5
#           dummy -> 1->2->3->4->5
#           left (left pointer point at dummy node)
#                   right (right pointer point at one)
#           traverse right pointer n time, then start traversing left pointer (dummy node), when right pointer reach the end, left
# pointer will reach the node before the delete node.
# use left.next = left.next.next to delete


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
