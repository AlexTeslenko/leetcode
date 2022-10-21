# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val, root)
            return new_node
        
        def dfs(root, val, depth, cur_depth):
            if not root:
                return
            
            if cur_depth+1 == depth:
                new_node_left = TreeNode(val)
                new_node_right = TreeNode(val)
                if root.left:
                    new_node_left.left = root.left 
                if root.right:
                    new_node_right.right = root.right
                    
                root.left = new_node_left
                root.right = new_node_right
                
                return
            
            dfs(root.left, val, depth, cur_depth+1)
            dfs(root.right, val, depth, cur_depth+1)
        
        dfs(root, val, depth, 1)
        
        return root
        