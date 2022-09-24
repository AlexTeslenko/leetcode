# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        
        def traverse_tree(root):
            if not root:
                return 
            
            traverse_tree(root.left)
            heapq.heappush(heap, -root.val)
            print(heap)
            if len(heap) > k:
                heapq.heappop(heap)
            traverse_tree(root.right)
        
        traverse_tree(root)
        return -heap[0]
        
        
            
        