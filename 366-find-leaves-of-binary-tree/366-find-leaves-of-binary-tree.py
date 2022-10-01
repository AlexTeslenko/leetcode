# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = collections.defaultdict(list)
                
        def dfs(root, layer):
            if not root:
                return layer
               
            left = dfs(root.left, layer)
            right = dfs(root.right, layer)
            
            cur_layer = max(left, right)
            
            output[cur_layer].append(root.val)
            return cur_layer + 1
        
        dfs(root, 0)
        
        return output.values()
        
        

    

            
                
        