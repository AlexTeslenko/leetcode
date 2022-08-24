# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.start_iter = 0
        self.vals = []
        self._dfs(root)
        
    def _dfs(self, root):
        if root.left:
            self._dfs(root.left)
        
        self.vals.append(root.val)
        
        if root.right:
            self._dfs(root.right)
        
        

    def next(self) -> int:
        val =  self.vals[self.start_iter]
        self.start_iter += 1
        return val
    

    def hasNext(self) -> bool:
        if self.start_iter < len(self.vals):
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()