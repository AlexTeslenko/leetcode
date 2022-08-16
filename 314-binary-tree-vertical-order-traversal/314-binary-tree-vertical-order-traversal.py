# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels_columns = {}
        self.dfs(root, 0, 0, levels_columns)
        
        #print(levels_columns)
        levels = {}
        for key in sorted(levels_columns):
            if key[0] not in levels:
                levels[key[0]] = []
            for item in levels_columns[key]:
                levels[key[0]].append(item)
        
        #print(levels)
        vals = []
        for key in sorted(levels):
            vals.append(levels[key])
            
        return vals
        
    def dfs(self, root, cur_level, cur_column,  levels_columns):
        if not root:
            return None
        
        if (cur_level, cur_column) not in levels_columns:
            levels_columns[(cur_level, cur_column)] = []
        
        levels_columns[(cur_level, cur_column)].append(root.val)
        
        if root.left:
            self.dfs(root.left, cur_level - 1, cur_column + 1,  levels_columns)
        
        if root.right:
            self.dfs(root.right, cur_level + 1, cur_column + 1, levels_columns)
        
        return
        