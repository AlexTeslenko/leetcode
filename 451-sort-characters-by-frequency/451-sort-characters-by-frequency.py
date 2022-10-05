from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        num_chs = Counter(s)
        ch_nums_sorted = sorted(num_chs.items(), key=lambda x: x[1], reverse=True)
        
        sorted_s = ''
        for num, ch in ch_nums_sorted:
            sorted_s += ch * num
        
        return sorted_s
        