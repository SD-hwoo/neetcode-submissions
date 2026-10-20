# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            #pop the smallest in the stack
            node = stack.pop()

            #decrement k because we always pop the smallest in the stack
            k -= 1
            if k == 0:
                return node.val
            node = node.right
