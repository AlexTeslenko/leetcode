# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue = deque([self.root])
        self.parents = deque([self.root])
        while self.queue:
            cur_root = self.queue.popleft()
            if cur_root.left:
                self.queue.append(cur_root.left)
                self.parents.append(cur_root.left)
            if cur_root.right:
                self.queue.append(cur_root.right)
                self.parents.append(cur_root.right)
            
            if cur_root.left and cur_root.right:
                self.parents.popleft()
                

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        parent = None
        if len(self.parents):
            if not self.parents[0].left:
                self.parents[0].left = new_node
                parent =  self.parents[0]
            else:
                self.parents[0].right = new_node
                parent = self.parents.popleft()
        else:
            self.root = new_node
        
        self.parents.append(new_node)
        
        return parent.val if parent else -1
         

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()