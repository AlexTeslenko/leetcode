# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root1, root2):
            if not root1 and not root2:
                return None
            
            new_root = TreeNode()
            
            if root1 and root2:
                new_root.left = dfs(root1.left, root2.left)
                new_root.right = dfs(root1.right, root2.right)
                new_root.val = root1.val + root2.val
            elif root1:
                new_root.left = dfs(root1.left, None)
                new_root.right = dfs(root1.right, None)
                new_root.val = root1.val
            elif root2:
                new_root.left = dfs(None, root2.left)
                new_root.right = dfs(None, root2.right)
                new_root.val = root2.val
            
            return new_root
        
        return dfs(root1, root2)