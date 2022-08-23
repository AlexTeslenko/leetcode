class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        el_freq = {}
        for el in nums:
            if el not in el_freq:
                el_freq[el] = 0
            el_freq[el] += 1
        
        freq_list =[(el, freq) for el, freq in el_freq.items()]
        
        freq_list.sort(reverse=True, key=lambda x: x[1])
        
        return [freq_list[i][0] for i in range(k)]
        