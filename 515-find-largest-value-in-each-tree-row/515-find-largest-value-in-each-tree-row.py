# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        max_vals = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            max_level_val = -math.inf
            for i in range(level_size):
                node = queue.popleft()
                max_level_val = max(max_level_val, node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            max_vals.append(max_level_val)
        
        return max_vals