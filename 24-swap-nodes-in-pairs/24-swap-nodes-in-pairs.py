# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first_node = head
        second_node = head.next
        
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
            
        
        return second_node
        
        
        '''
                next_head = head.next
        first = next_head
        while head and next_head:
            temp = head
            head.next = next_head.next
            next_head.next = head
            head = head.next
            next_head = head.next
            print(head.val, next_head.val)
        
        return first
        '''
        

        
            
                 