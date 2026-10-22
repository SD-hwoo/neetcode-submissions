# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        values = {}
        for i in range(len(inorder)):
            values[inorder[i]] = i

        def build_tree(pre_start, in_start, in_end):
            if in_start > in_end:
                return None
            node = TreeNode(preorder[pre_start])
            mid = values[node.val]
            left_size = mid - in_start
                
            node.left = build_tree(pre_start + 1, in_start, mid - 1)
            node.right = build_tree(pre_start + 1 + left_size, mid + 1, in_end) 
            return node

        return build_tree(0, 0, len(inorder) - 1)

        