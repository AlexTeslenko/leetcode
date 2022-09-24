class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        min_indx, min_num = 0, abs(nums[0])
        for i, num in enumerate(nums):
            if abs(num) < min_num:
                min_num =  abs(num)
                min_indx = i
                
        
        output = []
        left_ptr, right_ptr = min_indx - 1, min_indx
        while left_ptr >= 0 or right_ptr < len(nums):
            if left_ptr >=0 and right_ptr < len(nums):
                if abs(nums[left_ptr]) > abs(nums[right_ptr]):
                    output.append(nums[right_ptr]**2)
                    right_ptr += 1
                else:
                    output.append(nums[left_ptr]**2)
                    left_ptr -= 1
            elif left_ptr < 0 and right_ptr < len(nums):
                    output.append(nums[right_ptr]**2)
                    right_ptr += 1
            elif left_ptr >= 0 and right_ptr >= len(nums):
                    output.append(nums[left_ptr]**2)
                    left_ptr -= 1
        
        return output