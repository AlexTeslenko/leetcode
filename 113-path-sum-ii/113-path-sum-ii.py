# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        def dfs(root, cur_target, cur_path):
            if not root:
                return
            
            cur_target -= root.val
            cur_path.append(root.val)
            
            if cur_target == 0 and not root.left and not root.right:
                output.append(cur_path[:])
            
            dfs(root.left, cur_target, cur_path[:])
            dfs(root.right, cur_target, cur_path[:])
        
        
        dfs(root, targetSum, [])
        
        return output