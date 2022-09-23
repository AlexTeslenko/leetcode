# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.max_cons = 0
        
        def find_longest_cons(root, parent_val, cur_cons):
            if not root:
                return
            
            if root.val - parent_val == 1:
                cur_cons += 1
            else:
                cur_cons = 1
                
            self.max_cons = max(self.max_cons, cur_cons)
            
            find_longest_cons(root.left, root.val, cur_cons)
            find_longest_cons(root.right, root.val, cur_cons)
            
        
        find_longest_cons(root, -30001, 0)
        
        return self.max_cons
            
            
            
            
        