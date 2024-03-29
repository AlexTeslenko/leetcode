# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [None]
        self.dfs(root, p, q, lca)
        
        return lca[0]
        
        
    def dfs(self, root, p, q, lca):
        if root is None:
            return
            
        p_q_node1, p_q_node2 = None, None
        if root.left:
            p_q_node1 = self.dfs(root.left, p, q, lca)
        if root.right:
            p_q_node2 = self.dfs(root.right, p, q, lca)
        
        if (p_q_node1 and p_q_node2 and not lca[0]) or \
              ( p_q_node1 and (root.val == p.val or root.val == q.val)) or \
            ( p_q_node2 and (root.val == p.val or root.val == q.val)):
            lca[0] = root
            
        if root.val == p.val or root.val == q.val:
            return root
        if p_q_node1:
            return p_q_node1
        if p_q_node2:
            return p_q_node2
            
        return
                

    
    
