class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        num_hills = 0
        left_ptr, right_ptr = 1, 1
        while right_ptr < len(nums)-1:
            if nums[left_ptr-1] < nums[right_ptr] > nums[right_ptr+1] or \
            nums[left_ptr-1] > nums[right_ptr] < nums[right_ptr+1]:
                num_hills += 1
                left_ptr = right_ptr = right_ptr + 1
            elif nums[right_ptr] == nums[right_ptr+1]:
                right_ptr += 1
            else:
                left_ptr = right_ptr = right_ptr + 1
        
        return num_hills
                
        