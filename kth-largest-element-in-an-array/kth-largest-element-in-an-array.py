from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for i in range(k):
            heappush(heap, nums[i])
        
        for i in range(k, len(nums)):
            min_el = heappop(heap)
            heappush(heap, max(nums[i], min_el))
        
        min_el = heappop(heap)
        
        return min_el
