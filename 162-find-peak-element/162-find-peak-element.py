class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        
        left_ptr, right_ptr = 0, len(nums) - 1
        
        while left_ptr <= right_ptr:
            middle = left_ptr + (right_ptr - left_ptr) // 2
            
            if middle-1 >= 0 and nums[middle] < nums[middle-1]:
                right_ptr = middle - 1
            elif middle+1 < len(nums) and  nums[middle] < nums[middle+1]:
                left_ptr = middle + 1
            else:
                return middle
        
        return 0