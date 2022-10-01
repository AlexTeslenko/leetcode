class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        if not words:
            return s
        
        ranges = []
        for word in words:
            word_len = len(word)
            i = 0
            while i + word_len <= len(s):
                if s[i:i+word_len] == word:
                    ranges.append((i, i+word_len))
                i += 1
        
        if not ranges:
            return s
        
        ranges.sort(key=lambda x: x[0])
        
                    
        merged_ranges = []
        rn_start= ranges[0][0]
        rn_end = ranges[0][1]
        
        for i in range(1, len(ranges)):
            cur_range = ranges[i]
            if cur_range[0] <= rn_end:
                rn_end = max(rn_end, cur_range[1])
            else:
                merged_ranges.append((rn_start, rn_end))
                rn_start = cur_range[0]
                rn_end = cur_range[1]
        
        merged_ranges.append((rn_start, rn_end))
        
        output_str = s
        begin = 0
        for rn in merged_ranges:
            output_str = output_str[:rn[0]+begin] + '<b>' + output_str[begin+rn[0]:begin+rn[1]] + '</b>' + output_str[begin+rn[1]:]
            begin += 7
        
        return output_str
            
            
            
        