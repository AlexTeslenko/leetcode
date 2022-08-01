from heapq import *

class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.left_heap, -num)
        max_val = heappop(self.left_heap)
        heappush(self.right_heap, -max_val)
        
        if len(self.right_heap) > len(self.left_heap):
            min_val = heappop(self.right_heap)
            heappush(self.left_heap, -min_val)
            
    def findMedian(self) -> float:
        if len(self.right_heap) == len(self.left_heap):
            return (-self.left_heap[0] + (self.right_heap[0])) / 2
        elif len(self.right_heap) > len(self.left_heap):
            return self.right_heap[0]
        else:
            return -self.left_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()