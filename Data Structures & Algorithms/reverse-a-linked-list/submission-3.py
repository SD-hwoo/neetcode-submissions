# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        current = head
        new = head.next
        old = None
        current.next = old
        old = current
        
        while new.next:
            current = new
            new = new.next
            current.next = old
            old = current
        new.next = current
        return new

