# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.vals = []
        self.cur_idx = 0
        
        def _dfs(root):
            if not root:
                return
            
            _dfs(root.left)
            self.vals.append(root.val)
            _dfs(root.right)
        
        _dfs(root)
            
        

    def next(self) -> int:
        cur_val = self.vals[self.cur_idx]
        self.cur_idx += 1
        return cur_val


    def hasNext(self) -> bool:
        if self.cur_idx < len(self.vals):
            return True
        return False

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()