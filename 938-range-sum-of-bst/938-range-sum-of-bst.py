# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root, low, high)
          
    
    def dfs(self, root, low, high):
        if root is None:
            return 0

        range_sum = 0
        if root.left:
            range_sum += self.dfs(root.left, low, high)
        
        if root.right:
            range_sum += self.dfs(root.right, low, high)
            
        if low <= root.val <= high:
            range_sum += root.val
            
        return range_sum