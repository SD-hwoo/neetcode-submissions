# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def search_sub(n1, n2):
            if not n1 and not n2:
                return True
            if not (n1 and n2):
                return False
            if n1.val == n2.val:
                return search_sub(n1.left, n2.left) and search_sub(n1.right, n2.right)
            return False
            
        possibilities = []
        def search_main(n1, n2):
            if not n1 or not n2:
                return None
            
            if n1.val == n2.val: 
                nonlocal possibilities
                possibilities.append(n1)
            left = search_main(n1.left, n2)
            right = search_main(n1.right, n2)

        search_main(root, subRoot)
        for n in possibilities:
            if search_sub(n, subRoot):
                return True
        return False