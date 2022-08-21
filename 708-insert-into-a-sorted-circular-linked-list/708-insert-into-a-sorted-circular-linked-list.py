"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return  new_node
        
        first_node = head
        prev, curr = head, head.next
        to_insert = False
        while curr:
            if (insertVal <= curr.val and insertVal >= prev.val): 
                to_insert = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    to_insert = True

            if to_insert:
                new_node = Node(insertVal)
                new_node.next = curr
                prev.next = new_node
                break
            
            prev = curr
            curr = curr.next
            
            if prev == head:
                break
        
        prev.next = Node(insertVal, curr)
        
        return first_node
            