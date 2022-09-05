class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_start, window_end = 0, 0
        cur_sum = 0
        max_avg = -math.inf
        while window_end < len(nums):
            cur_sum += nums[window_end]
            if window_end - window_start + 1 == k:
                max_avg = max(max_avg, cur_sum / k)
                cur_sum -= nums[window_start]
                window_start += 1
            
            window_end += 1
            
        return max_avg
        