# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p.val
        self.q = q.val
        self.lca = None
        found_p_q = [False, False]
        self.dfs(root)
        
        return self.lca
        
        
        
    def dfs(self, root):
        if not root:
            return [False, False]
        
        found_p_q_1 = self.dfs(root.left)
        found_p_q_2 = self.dfs(root.right)
        
        found_p_q = [False, False]
        if root.val == self.p or found_p_q_1[0] or found_p_q_2[0]:
            found_p_q[0] = True
        
        if root.val == self.q or found_p_q_1[1] or found_p_q_2[1]:
            found_p_q[1] = True
            
        if found_p_q[0] and found_p_q[1] and not self.lca:
            self.lca = root
        
        print(found_p_q)
        print(root.val)
        
        return found_p_q
        
            
        
        