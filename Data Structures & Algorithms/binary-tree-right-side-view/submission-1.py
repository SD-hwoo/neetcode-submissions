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
        result.append(root.val)
        while q:
            level = []
            
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    level.append(node.left)
                    q.append(node.left)
                if node.right:
                    level.append(node.right)
                    q.append(node.right)
            if level:
                result.append(level[-1].val)
        
        return result

