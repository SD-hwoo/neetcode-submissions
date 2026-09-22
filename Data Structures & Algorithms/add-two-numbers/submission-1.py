# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        traverse1 = l1
        traverse2 = l2
        result = ListNode(0)
        traverse3 = result
        carry = 0
        while traverse1 and traverse2:
            new_val = traverse1.val + traverse2.val + carry
            carry = 0
            if new_val > 9:
                carry += 1
                new_val -= 10
            new_node = ListNode(new_val)
            traverse3.next = new_node
            traverse3 = traverse3.next
            traverse1 = traverse1.next
            traverse2 = traverse2.next
        if traverse1:
            while traverse1:
                new_val = traverse1.val + carry
                carry = 0
                if new_val > 9:
                    carry += 1
                    new_val -= 10
                new_node = ListNode(new_val)
                traverse3.next = new_node
                traverse3 = traverse3.next
                traverse1 = traverse1.next
        elif traverse2:
            while traverse2:
                new_val = traverse2.val + carry
                carry = 0
                if new_val > 9:
                    carry += 1
                    new_val -= 10
                new_node = ListNode(new_val)
                traverse3.next = new_node
                traverse3 = traverse3.next
                traverse2 = traverse2.next
        if carry:
            traverse3.next = ListNode(carry)
        return result.next
