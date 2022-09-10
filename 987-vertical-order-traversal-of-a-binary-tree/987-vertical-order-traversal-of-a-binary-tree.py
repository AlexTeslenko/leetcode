# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0, 0)])
        col_to_node = {}
        while queue:
            node, row, col = queue.popleft()
            if (col, row) not in col_to_node:
                col_to_node[(col, row)] = []
            col_to_node[(col,row)].append(node.val)
            
            if node.left:
                queue.append((node.left, row+1, col-1))
            if node.right:
                queue.append((node.right, row+1, col+1))
        
       
        sorted_keys = list(col_to_node.keys())
        sorted_keys.sort(key=lambda x: x[1])

        sorted_by_row = {}
        for key in sorted_keys:
            if key[0] not in sorted_by_row:
                sorted_by_row[key[0]] = []
            
            col_to_node[key].sort()
            sorted_by_row[key[0]] +=  col_to_node[key]
        
        sorted_keys = list(sorted_by_row.keys())
        sorted_keys.sort()
        
        output = [sorted_by_row[key] for key in sorted_keys]

        return output
            
        