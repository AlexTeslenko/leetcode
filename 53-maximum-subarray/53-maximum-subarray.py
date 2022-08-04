class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_subarray = nums[0]
        max_subarray = nums[0]
        
        for i in range(1, len(nums)):
            if cur_subarray < 0:
                cur_subarray = 0
            cur_subarray += nums[i]
            
            if cur_subarray > max_subarray:
                max_subarray = cur_subarray
                
        return max_subarray
        