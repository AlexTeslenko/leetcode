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
        
        
        node = self.head
       # while node != self.tile:
       #     print("node: ", node.val)
       #     print("left: ", node.left.val)
       #     print("right: ", node.right.val)
       #     node = node.right
        
        #print("node: ", self.tile.val)
        #print("left: ", self.tile.left.val)
        #print("right: ", self.tile.right.val)
        #print(self.head.val)
        #print(self.tile.val)
        
        #self.new_head = Node(0, None, self.head)
        
        
        return self.head
        
    
    def dfs2(self, root):
        if root is None:
            return
                
        if not root.left:
            if not self.head:
                self.head = root
                
        print(root.val)
        self.dfs2(root.left)
        
        if self.tile:
            self.tile.right = root
            root.left =  self.tile
        
        self.tile = root
        
        self.dfs2(root.right)
        
        #self.tile.left = root
        
        
        
         
        
        
        
        
        
        
        
        
        
        
        
        
    def dfs(self, root):
        if root is None:
            return
        
        if not root.left:
            if not self.head:
                self.head = root
        
                
        left_node = self.dfs(root.left)
        
        
        if left_node:
            left_node.right = root
            root.left = left_node
        
        right_node = self.dfs(root.right)
        
        if right_node:
            root.right = right_node
            right_node.left = root
        
        if not root.right:
            self.tile = root
        
        return right_node if right_node and left_node else root
            
        
        