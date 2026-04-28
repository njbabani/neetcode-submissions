# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        solution = 'recursion'

        if solution == 'iteration':
            prev, curr = None, head

            while curr != None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        if solution == 'recursion':
            # If head is null return null
            def reverse(cur, prev):
                if cur is None:
                    return prev
                else:
                    next = cur.next
                    cur.next = prev
                    return reverse(next, cur)

            return reverse(head, None)
