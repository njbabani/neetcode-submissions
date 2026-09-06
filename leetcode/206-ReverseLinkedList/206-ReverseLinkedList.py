# Last updated: 9/6/2026, 2:56:19 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr != None:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward

        return prev