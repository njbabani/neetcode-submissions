# Last updated: 9/6/2026, 2:55:56 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Store the slow and fast traversals of linked list
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            # Move slow by once
            slow = slow.next

            # Move fast by twice
            fast = fast.next.next

        return slow