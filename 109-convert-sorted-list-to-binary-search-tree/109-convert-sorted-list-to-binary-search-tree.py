# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        def build_tree(vals, low, high):
            if high < low:
                return
            
            middle = low + (high - low) // 2
            
            root = TreeNode(vals[middle])
            
            root.left = build_tree(vals, low, middle-1)
            root.right = build_tree(vals, middle+1, high)
            
            return root
        
        root = build_tree(vals, 0, len(vals)-1)
        
        return root