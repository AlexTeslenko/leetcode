class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mods = {0: -1}
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            mod = cur_sum % k
            if mod not in mods:
                mods[mod] = i
            else:
                if i - mods[mod] >= 2:
                    return True
        
        return False