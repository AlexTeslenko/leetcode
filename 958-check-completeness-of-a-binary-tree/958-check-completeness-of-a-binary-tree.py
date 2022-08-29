# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        return self.method_2(root)
        '''
        i = 0
        queue = [root]
        while queue[i]:
            node = queue[i]
            
            queue.append(node.left)
            queue.append(node.right)
            
            i += 1
        
        return not any(queue[i:])
        '''
    
    def method_2(self, root):
        queue = deque([root])
        prev_node = root
        while queue:
            cur_node = queue.popleft()
            
            if cur_node:
                queue.append(cur_node.left)
                queue.append(cur_node.right)
            
                if prev_node is None:
                    return False
            
            prev_node = cur_node
        
        return True
            
                