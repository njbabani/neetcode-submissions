# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        solution = 'iteration'

        if solution == 'iteration':
            prev, curr = None, head

            while curr != None:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        if solution == 'recursion':
            def reverse(cur, prev):
                if cur is None:
                    return prev
                else:
                    next = cur.next
                    cur.next = prev
                    return reverse(next, cur)

            return reverse(head, None)
