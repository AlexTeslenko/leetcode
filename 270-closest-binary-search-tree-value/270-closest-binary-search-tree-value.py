# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_diff_val = [math.inf, math.inf]
        self.dfs(root, target, closest_diff_val)
        
        return closest_diff_val[1]
            
        
    def dfs(self, root, target, closest_diff_val):
        if root is None:
            return
        
        
        if abs(target - root.val) < closest_diff_val[0]:
            closest_diff_val[0] = abs(target - root.val)
            closest_diff_val[1] = root.val
            
        if root.val < target:
            self.dfs(root.right, target, closest_diff_val)
        else:
            self.dfs(root.left, target, closest_diff_val)
            
        return
        
        
        
            