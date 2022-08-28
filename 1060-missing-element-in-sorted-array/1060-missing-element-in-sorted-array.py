class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        zero_idx_el = nums[0]
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = low + (high - low) // 2
            curr_missed = nums[middle] - zero_idx_el - middle
            print(middle)
            if curr_missed >= k:
                high = middle - 1
            else:
                low = middle + 1

        return nums[low-1] + k - (nums[low-1] - zero_idx_el - (low-1))

        