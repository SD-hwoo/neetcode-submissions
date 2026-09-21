"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        result = Node(0)
        build = result
        traverse = head
        original_to_copy = {}
        while traverse:
            current = Node(traverse.val)
            original_to_copy[traverse] = current
            build.next = current
            build = build.next
            traverse = traverse.next
        traverse = head
        build = result.next
        while traverse:
            if traverse.random:
                random_node = original_to_copy[traverse.random]
            else:
                random_node = None
            build.random = random_node
            traverse = traverse.next
            build = build.next

        return result.next

