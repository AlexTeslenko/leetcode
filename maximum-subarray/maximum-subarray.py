class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        cur_subarray = nums[0]
        max_subarray = nums[0]
        
        for i in range(1, len(nums)):
            if cur_subarray < 0:
                cur_subarray = 0
            cur_subarray += nums[i]
            
            if cur_subarray > max_subarray:
                max_subarray = cur_subarray
                
        return max_subarray
        '''
        
        sums = [0 for i in nums]
        sums[0] = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            cur_sum = sums[i-1] + nums[i]
            if cur_sum > nums[i]:
                sums[i] = cur_sum
            else:
                 sums[i] = nums[i]
            
            max_sum = max(max_sum, sums[i])
        
        return max_sum
        
        