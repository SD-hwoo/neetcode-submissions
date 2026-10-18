# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS
        # Keep track of each path's line of numbers? and keep track of largest val?

        def search_dfs(node, max_val):
            if not node:
                return 0
            
            if max_val > node.val: 
                return 0 + search_dfs(node.left, max_val) + search_dfs(node.right, max_val)
            max_val = node.val
            return 1 + search_dfs(node.left, max_val) + search_dfs(node.right, max_val)
        return search_dfs(root, root.val)
