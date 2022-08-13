"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a_path = p
        b_path = q
        
        while a_path != b_path:
            if a_path.parent:
                a_path = a_path.parent
            else:
                a_path = q
            
            if b_path.parent:
                b_path = b_path.parent
            else:
                b_path = p
        
        return a_path