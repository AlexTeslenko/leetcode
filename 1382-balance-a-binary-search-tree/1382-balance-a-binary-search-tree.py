# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.nodes = []
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            self.nodes.append(root.val)
            inorder(root.right)
        
        inorder(root)

        def build_tree(start, end):
            if start > end:
                return
            else:
                middle = start + (end - start) // 2
                node = TreeNode(self.nodes[middle])
  
                node.left = build_tree(start, middle-1)
                node.right = build_tree(middle+1, end)
            
                return node
        
        start, end = 0, len(self.nodes)-1
        
        root = build_tree(start, end)
        
        return root
    
         
        '''       
        nodes = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        
        def build_tree(start, end, nodes):
            if start > end: 
                return
            
            middle = start + (end - start) // 2
            root = TreeNode(nodes[middle])
            
            if start < end:
                root.left = build_tree(start, middle-1, nodes)
                root.right = build_tree(middle+1, end, nodes)
            
            return root
        
        root = build_tree(0, len(nodes)-1, nodes)
        
        return root
        '''
            
            