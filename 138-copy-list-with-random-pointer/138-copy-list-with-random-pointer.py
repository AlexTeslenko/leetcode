"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.visited_dict = {}
        head = self.copyList(head)
        
        return head
    
    def copyList(self, head):
        if head is None:
            return None
        
        if head in self.visited_dict:
            return self.visited_dict[head]
        
        node = Node(head.val)
        self.visited_dict[head] = node
        
        node.next = self.copyList(head.next)
        node.random = self.copyList(head.random)
        
        return node