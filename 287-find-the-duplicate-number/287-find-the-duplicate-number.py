from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counted = Counter(nums)
        for key in  counted:
            if counted[key] >= 2:
                return key