class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        
        peack = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                
                peack = i
                break
        
        before_peack_val = nums[peack - 1]
        i = peack
        while i < len(nums) and nums[i] > before_peack_val:
            i += 1
        
        nums[peack-1], nums[i-1] = nums[i-1], nums[peack-1]

        if peack == -1:
            peack = 0
            
        nums[peack:] = reversed(nums[peack:])
        
        
            