class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        window_start = 0
        distinct_chs = {}
        max_window = 0
        
        for window_end in range(len(s)):
            if s[window_end] not in  distinct_chs:
                distinct_chs[s[window_end]] = 0
            
            distinct_chs[s[window_end]] += 1
            
            while len(distinct_chs) > 2:
                distinct_chs[s[window_start]] -= 1
                
                if distinct_chs[s[window_start]] == 0:
                    del distinct_chs[s[window_start]]
                
                window_start += 1
            
            max_window = max(max_window, window_end - window_start + 1)
        
        return max_window
            
        
        