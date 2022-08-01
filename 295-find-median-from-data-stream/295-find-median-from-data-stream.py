from heapq import *

class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        self.size = 0
        

    def addNum(self, num: int) -> None:
        heappush(self.left_heap, -num)
        max_val = heappop(self.left_heap)
        heappush(self.right_heap, -max_val)
        
        if len(self.right_heap) > len(self.left_heap):
            min_val = heappop(self.right_heap)
            heappush(self.left_heap, -min_val)
            
    def findMedian(self) -> float:
        #print(self.left_heap)
        #print(self.right_heap)
        if len(self.right_heap) == len(self.left_heap):
            median_1 = heappop(self.left_heap)
            median_2 = heappop(self.right_heap)
            heappush(self.left_heap, median_1)
            heappush(self.right_heap, median_2)
            return (-median_1 + (median_2)) / 2
        elif len(self.right_heap) > len(self.left_heap):
            median = heappop(self.right_heap)
            heappush(self.right_heap, median)
            return median
        else:
            median = heappop(self.left_heap)
            heappush(self.left_heap, median)
            return -median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()