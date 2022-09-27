# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(root, cur_sum):
            if not root:
                return False
            
            cur_sum -= root.val
            
            if not root.left and not root.right:
                if cur_sum == 0:
                    return True
                return False
            
            return dfs(root.left, cur_sum) or dfs(root.right, cur_sum)
        
        return dfs(root, targetSum)