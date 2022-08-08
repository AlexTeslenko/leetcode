# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        left_to_right = True
        output = []
        queue = deque([root])
        
        if not root:
            return output
        
        while queue:
            level_size = len(queue)
            level_nodes = [0 for i in range(level_size)]
            for i in range(level_size):
                node = queue.popleft()
                if left_to_right:
                    level_nodes[i] = node.val
                else:
                    level_nodes[level_size - i-1] = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            output.append(level_nodes)
            left_to_right = not left_to_right
        
        return output
            
        
                
        
        