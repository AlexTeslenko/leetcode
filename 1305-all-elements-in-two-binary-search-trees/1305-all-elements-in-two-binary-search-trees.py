# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ordered_nodes_1 = []
        ordered_nodes_2 = []
        
        def traverse_tree(root, ordered_nodes):
            if not root:
                return
            
            traverse_tree(root.left, ordered_nodes)
            ordered_nodes.append(root.val)
            traverse_tree(root.right, ordered_nodes)
        
        
        traverse_tree(root1, ordered_nodes_1)
        traverse_tree(root2, ordered_nodes_2)
        
        ptr_1, ptr_2 = 0, 0
        combined_nodes = []
        
        while ptr_1 < len(ordered_nodes_1) and ptr_2 < len(ordered_nodes_2):
            if ordered_nodes_1[ptr_1] <= ordered_nodes_2[ptr_2]:
                combined_nodes.append(ordered_nodes_1[ptr_1])
                ptr_1 += 1
            elif ordered_nodes_2[ptr_2] < ordered_nodes_1[ptr_1]:
                combined_nodes.append(ordered_nodes_2[ptr_2])
                ptr_2 += 1
        while ptr_1 < len(ordered_nodes_1):
            combined_nodes.append(ordered_nodes_1[ptr_1])
            ptr_1 += 1
        while ptr_2 < len(ordered_nodes_2):
            combined_nodes.append(ordered_nodes_2[ptr_2])
            ptr_2 += 1
            
        return combined_nodes
            
            
            
        