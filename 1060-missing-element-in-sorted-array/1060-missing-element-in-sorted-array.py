class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        zero_idx_el = nums[0]
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = low + (high - low) // 2
            curr_missed = nums[middle] - zero_idx_el - middle
    
            if curr_missed >= k:
                high = middle - 1
            else:
                low = middle + 1

        return nums[high] + k - (nums[high] - zero_idx_el - (high))

        