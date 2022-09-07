"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        new_node.next = new_node
        if not head:
            return new_node
        
        prev_node = head
        cur_node = head.next
        to_insert = False
        while True:
            if (prev_node.val <= new_node.val <= cur_node.val):     
                to_insert = True
            elif prev_node.val > cur_node.val:
                if new_node.val >= prev_node.val or new_node.val <= cur_node.val:
                    to_insert = True
            
            if to_insert:
                new_node.next = prev_node.next
                prev_node.next = new_node
                return head
            
            prev_node = cur_node
            cur_node = cur_node.next
            
            if prev_node == head:
                break
        
        new_node.next = cur_node
        prev_node.next = new_node
        
        return head

    
    
    '''
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        
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
                return head
            
            prev = curr
            curr = curr.next
            
            if prev == head:
                break
        
        new_node = Node(insertVal)
        new_node.next = curr
        prev.next = new_node
        
        return head
    '''