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
        
        return lca
    
    def dfs(self, root, p, q, lca):
        if root is None:
            return False
        
        left_nod, right_nod = [False, False], [False, False]
        
        if root.left:
            left_nod = self.dfs(root.left, p, q, lca)
        
        if root.right:
            right_nod = self.dfs(root.right, p, q, lca)
            
        found_p, found_q = False, False
        
        if root.val == p.val or left_nod[0] or right_nod[0]:
            found_p = True
        
        if root.val == q.val or left_nod[1] or right_nod[1]:
            found_q = True
        
        #print(found_p, found_q, root.val, p.val, q.val)
        if found_p and found_q and lca.val == None:
            lca.val = root.val
            
        return [found_p, found_q]
            