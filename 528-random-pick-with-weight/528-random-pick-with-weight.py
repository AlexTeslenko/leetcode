import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.probs = [weight / sum(w) for weight in self.w]
        self.ranges = []
        
        range_start = 0
        for i, prob in enumerate(self.probs):
            range_end = range_start + prob
            self.ranges.append((range_start, range_end))
            range_start = range_end

    def pickIndex(self) -> int:
        rand = random.random()
        left_idx, right_idx = 0, len(self.ranges)
        while left_idx < right_idx:
            middle_idx = left_idx + (right_idx - left_idx) // 2
            rn = self.ranges[middle_idx]
            if rn[0] <=  rand <= rn[1]:
                return middle_idx
            elif rand > rn[1]:
                left_idx =  middle_idx
            else:
                right_idx = middle_idx
        return left_idx
            
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()