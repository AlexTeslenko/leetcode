from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counted_nums = Counter(nums)

        for val in counted_nums.values():
            if val > 1:
                return True
        
        return False

        