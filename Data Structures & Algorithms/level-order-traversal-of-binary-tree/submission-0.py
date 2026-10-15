# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        process = []
        result = []

        process.append(root)
        result.append([root.val])
        while process:
            load = []

            load_val = []
            for node in process:
                if not node:
                    continue
                if node.left:
                    load.append(node.left)
                    load_val.append(node.left.val)
                if node.right:
                    load.append(node.right)
                    load_val.append(node.right.val)
            if load_val:
                result.append(load_val)
            process = load
        
        return result
