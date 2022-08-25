import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums_positions = {}
        for i in range(len(nums)):
            if nums[i] not in self.nums_positions:
                self.nums_positions[nums[i]] = []
            self.nums_positions[nums[i]].append(i)
             

    def pick(self, target: int) -> int:
        return random.choice(self.nums_positions[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)