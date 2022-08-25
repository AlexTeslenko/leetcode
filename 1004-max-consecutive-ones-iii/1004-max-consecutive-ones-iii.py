class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window_start = 0
        max_window = 0
        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                k -= 1
            
            while k < 0:
                if nums[window_start] == 0:
                    k += 1
                window_start += 1
            
            max_window = max(max_window, window_end - window_start + 1)
        
        return max_window
        