class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = 0
        actual_sum = 0
        for i in range(len(nums)):
            expected_sum += i
            actual_sum += nums[i]
        
        expected_sum += len(nums)
        
        missed_num = expected_sum - actual_sum
        
        return missed_num
                    
                
            