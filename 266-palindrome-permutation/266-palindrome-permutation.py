from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ch_freq = Counter(s)
        num_odd = 0
        for ch in ch_freq:
            if ch_freq[ch] %2 != 0:
                num_odd += 1
        
        if num_odd > 1:
            return False
        return True
        
        