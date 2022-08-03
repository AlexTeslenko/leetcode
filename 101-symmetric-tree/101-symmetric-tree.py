# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root, root])

        while queue:
            node_1 = queue.popleft()
            node_2 = queue.popleft()
            
            if not node_1 and not node_2: continue
            if not node_1 or not node_2: return False
            if node_1.val != node_2.val: return False 
            
            queue.append(node_1.left)
            queue.append(node_2.right)
            
            queue.append(node_2.left)
            queue.append(node_1.right)
        
        return True
            
        