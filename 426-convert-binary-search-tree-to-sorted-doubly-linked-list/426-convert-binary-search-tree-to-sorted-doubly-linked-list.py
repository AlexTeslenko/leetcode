"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        self.head = None
        self.tile = None
        
        self.dfs2(root)
        
        self.tile.right = self.head
        self.head.left = self.tile
        
        return self.head
        
    
    def dfs2(self, root):
        if root is None:
            return
                
        if not root.left:
            if not self.head:
                self.head = root
                
        
        self.dfs2(root.left)
        
        if self.tile:
            print("self.tile.val: ", self.tile.val)
            print("root: ", root.val)
            self.tile.right = root
            root.left =  self.tile
        
        self.tile = root
        
        self.dfs2(root.right)
        
        
        