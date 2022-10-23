class BinaryNode:
    def __init__(self, start=None, end=None, left=None, right=None) :
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = BinaryNode(start, end)
            return True
        else:
            return self.insert_node(self.root, start, end)
            
    
    def insert_node(self, root, start, end):
        if end <= root.start:
            if root.left:
                return self.insert_node(root.left, start, end)
            else:
                root.left = BinaryNode(start, end)
                return True
        elif start >= root.end:
            if root.right:
                return self.insert_node(root.right, start, end)
            else:
                root.right = BinaryNode(start, end)
                return True
        return False
                
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)