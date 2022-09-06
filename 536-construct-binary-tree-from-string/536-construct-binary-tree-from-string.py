# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def get_num(s, indx):
            is_negative = False
            if s[indx] == '-':
                is_negative = True
                indx += 1
            
            val = 0
            while indx < len(s) and s[indx].isnumeric():
                val = val * 10 + int(s[indx])
                indx += 1
            
            if is_negative:
                val = -val
                
            return val, indx
        
        def str_to_tree(s, indx):
            if indx == len(s):
                return None, indx
            
            value, indx = get_num(s, indx)
            
            root = TreeNode(value)
            
            if indx < len(s) and s[indx] == '(':
                root.left, indx = str_to_tree(s, indx+1)
                
            if root.left and indx < len(s) and s[indx] == '(':
                root.right, indx = str_to_tree(s, indx+1)

            return root, indx+1
            
        root, indx =  str_to_tree(s, 0)
        return root