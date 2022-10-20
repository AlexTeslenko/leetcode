class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_idx = {}
        for i, num in enumerate(nums):
            if num in nums_idx:
                if num in nums_idx:
                    if abs(nums_idx[num] - i) <= k:
                        return True
                    else:
                        nums_idx[num] = i
            else:
                nums_idx[num] = i
        
        return False
        