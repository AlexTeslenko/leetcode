import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        probs = [el / sum(w) for el in w]
        self.ranges = []
        prev_range_end = 0
    
        for i in range(len(probs)):
            range_start = prev_range_end
            range_end = range_start + probs[i]
            prev_range_end = range_end
            self.ranges.append((range_start, range_end))

    
    def pickIndex(self) -> int:
        random_num = random.random()
        low, high = 0, len(self.ranges)
        while low <= high:
            middle = low + (high - low) // 2
            if self.ranges[middle][0] <= random_num < self.ranges[middle][1]:
                return middle
            elif random_num > self.ranges[middle][1]:
                low = middle + 1
            else:
                high = middle - 1
        
        return middle

        
            
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()