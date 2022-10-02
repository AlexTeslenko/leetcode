# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.max_layer_1 = 0
        self.LCA = None
        
        def dfs(root, layer):
            if not root:
                return layer
            
            left_level = dfs(root.left, layer+1)
            right_level = dfs(root.right, layer+1)
            
            if left_level > self.max_layer_1 or right_level > self.max_layer_1 or(right_level == left_level == self.max_layer_1):
                if left_level == right_level:
                    self.max_layer_1 = left_level
                    self.LCA = root
                    return left_level
                elif left_level > right_level:
                    self.max_layer_1 = left_level
                    self.LCA = root.left
                    return left_level
                else:
                    self.max_layer_1 = right_level
                    self.LCA = root.right
                    return right_level
            
            return max(left_level, right_level)
        
        dfs(root, 0)
        return self.LCA
            
        
                
            
            
            
        