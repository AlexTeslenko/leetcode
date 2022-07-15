class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_freq = {}
        for num in nums1:
            if num not in num_freq:
                num_freq[num] = 0
            num_freq[num] += 1
            
        result = []
        
        for num in nums2:
            if num in num_freq and num_freq[num] > 0:
                result.append(num) 
                num_freq[num] -= 1
                
        return result