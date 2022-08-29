class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        prev_greater, prev_equal, prev_less = False, False, False
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                prev_less = True
            elif nums[i] == nums[i-1]:
                prev_equal = True
            elif nums[i] < nums[i-1]:
                prev_greater = True
        
        if prev_greater and prev_less:
            return False
        
        return True
            
        