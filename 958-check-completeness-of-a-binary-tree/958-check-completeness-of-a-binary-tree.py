# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        i = 0
        queue = [root]
        while queue[i]:
            node = queue[i]
            
            queue.append(node.left)
            queue.append(node.right)
            
            i += 1
        
        return not any(queue[i:])
                