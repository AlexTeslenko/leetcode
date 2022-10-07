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
        if not head:
            return 
        
        new_head = Node(head.val, head.next)
        node_dict = {head: new_head}
        
        first_node = head
        first_node_copy = new_head
        
        
        while first_node.next:
            new_node = Node(first_node.next.val)
            node_dict[first_node.next] = new_node
            
            first_node_copy.next = new_node
            first_node_copy = first_node_copy.next
            first_node =  first_node.next
        
        first_node = head
        first_node_copy = new_head
        
        while first_node:
            if first_node.random:
                first_node_copy.random = node_dict[first_node.random]
            
            first_node_copy = first_node_copy.next
            first_node =  first_node.next
        
        return new_head
        
        
        '''
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
        '''