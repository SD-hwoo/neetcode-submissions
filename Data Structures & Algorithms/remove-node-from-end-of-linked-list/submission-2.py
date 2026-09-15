# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse list, remove item, reverse it back
        if not head or not head.next:
            return
        before = None
        last = head
        after = head.next
        while after:
            last.next = before
            before = last
            last = after
            after = after.next
        last.next = before

        save_last = last

        for _ in range(1, n):
            lagger = last
            last = last.next

        forward = last.next
        if n == 1:
            save_last = save_last.next
            lagger = None
        else:    
            lagger.next = forward
        
        before = None
        last = save_last
        after = save_last.next
        while after:
            last.next = before
            before = last
            last = after
            after = after.next
        last.next = before
        return last