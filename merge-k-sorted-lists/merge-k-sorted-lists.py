# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        head = ListNode(-1)
        prev = head
        
        while True:
            min_val = 100000
            min_ptr = -1
            num_nans = 0
            for i in range(0, len(lists)):
                if lists[i] is not None:
                    if lists[i].val < min_val:
                        min_val = lists[i].val
                        min_ptr = i
                else:
                    num_nans += 1
            
            if num_nans == len(lists):
                break
                    
            prev.next = lists[min_ptr]
            prev = prev.next
            lists[min_ptr] = lists[min_ptr].next
            
        return head.next
        """
        
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
        
