# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0
            
            left_subtree = dfs(root.left)
            if not left_subtree:
                root.left = None
                
            right_subtree = dfs(root.right)
            if not right_subtree:
                root.right = None
            
            if not left_subtree and not right_subtree and root.val == 0:
                return 0
            else:
                return 1
        
        ans = dfs(root)
        
        if ans == 0:
            return None
        return root
            
            
        