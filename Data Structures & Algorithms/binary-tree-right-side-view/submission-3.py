# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS but only give the rightmost value?
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            level = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == n - 1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        
        return result

