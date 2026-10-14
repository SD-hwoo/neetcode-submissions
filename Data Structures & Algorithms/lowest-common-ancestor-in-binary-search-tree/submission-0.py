# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find_entries(n_root):
            if not n_root:
                return None
            if p.val < n_root.val and q.val < n_root.val:
                return find_entries(n_root.left)
            if p.val > n_root.val and q.val > n_root.val:
                return find_entries(n_root.right)
            else:
                return n_root

        return find_entries(root)