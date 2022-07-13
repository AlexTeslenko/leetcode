class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_iter = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_iter] = nums[zero_iter], nums[i]
                zero_iter += 1

                

                

