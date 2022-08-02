class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i, num in enumerate(nums):
            left = target - num
            if left in nums_dict:
                return [nums_dict[left], i]
            nums_dict[num] = i

                
                
                
                
                
                
                
                
                
                
#              