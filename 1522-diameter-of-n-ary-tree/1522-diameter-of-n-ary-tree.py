"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        max_dim = [0]
        dm = self.dfs(root, max_dim)
        
        return max_dim[0]
        
        
    
    def dfs(self, root, max_dim):
        if root is None:
            return 0
        
        children_dims = []
        
        for child in root.children:
            children_dims.append(self.dfs(child, max_dim))
        
        if len(children_dims) == 1:
            max_dim[0] = max(max_dim[0], children_dims[0])
        else:
            for i in range(len(root.children)):
                for j in range(i+1, len(root.children)):
                    max_dim[0] = max(max_dim[0], children_dims[i]+children_dims[j])
        
        return 1+max(children_dims) if children_dims else 1
        