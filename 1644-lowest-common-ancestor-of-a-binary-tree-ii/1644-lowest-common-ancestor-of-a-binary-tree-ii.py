# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = TreeNode(None)
        
        self.dfs(root, p, q, lca)
        
        if lca.val is None:
            return None
        
        return lca
    
    def dfs(self, root, p, q, lca):
        if root is None:
            return [False, False]
        
        left_node = self.dfs(root.left, p, q, lca)
        right_node = self.dfs(root.right, p, q, lca)
        
        found_p, found_q = False, False
        
        if left_node[0] or right_node[0] or root.val == p.val:
            found_p = True
            
        if left_node[1] or right_node[1] or root.val == q.val:
            found_q = True
        
        if found_p and found_q and not lca.val:
            lca.val = root.val
        
        return [found_p, found_q]
        
        