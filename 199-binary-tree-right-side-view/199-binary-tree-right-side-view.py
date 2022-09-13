# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size-1:
                    output.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return output
    
    '''
            vals = []
        #self.dfs(root, vals)
        self.bfs(root, vals)
        
        return vals
    


    def bfs(self, root, vals):
        if root is None:
            return
    
        queue = deque([root])
        level_size = 0
    
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
        
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
                if i == level_size - 1:
                    
                    vals.append(node.val)
        
    
    
    
    def dfs(self, root, vals):
        if root is None:
            return
        
        vals.append(root.val)
        
        if root.right:
            self.dfs(root.right, vals)
        else:
            if root.left:
                self.dfs(root.left, vals)
        '''
                    

        