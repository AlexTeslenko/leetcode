# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first_ptr, second_ptr = dummy, dummy
        for i in range(n+1):
                first_ptr = first_ptr.next
        
        while first_ptr:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next
        
        second_ptr.next = second_ptr.next.next

        
        return dummy.next
        