"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        queue = deque([root])
        while queue:
            level_size = len(queue)
            prev_node = None
            for i in range(level_size):
                cur_node = queue.popleft()
                if prev_node:
                    prev_node.next = cur_node
                
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                
                prev_node = cur_node
        
        return root
        