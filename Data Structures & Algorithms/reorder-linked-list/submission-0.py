# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # First split list
        slow = head
        fast = head
        while fast and fast.next:
            cutoff = slow
            slow = slow.next
            fast = fast.next.next
        cutoff.next = None
        # Second reverse list
        before = None
        last = slow
        after = last.next
        while after:
            last.next = before
            before = last
            last = after
            after = after.next
        last.next = before

        result = head
        start = head.next
        while start and last:
            result.next = last
            result = result.next
            last = last.next
            result.next = start
            result = result.next
            start = start.next
        if start:
            result.next = start
        if last:
            result.next = last