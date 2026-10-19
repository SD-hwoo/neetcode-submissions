# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([(root, (float('-inf'), float('inf')))])
        while q:
            node, interval = q.popleft()
            if interval[0] < node.val < interval[1]:
                if node.left:
                    q.append((node.left, (interval[0], min(node.val, interval[1]))))
                if node.right:
                    q.append((node.right, (max(node.val, interval[0]), interval[1])))
            else:
                return False
        return True