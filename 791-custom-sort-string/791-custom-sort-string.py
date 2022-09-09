class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_map = {ch: 0 for ch in s}
        for ch in s:
            s_map[ch] += 1
            
        ordered_s = ''
        
        for ch in order:
            if ch in s_map:
                new_s = ch * s_map[ch]
                del s_map[ch]
                ordered_s += new_s
        
        for ch in s_map:
            new_s = ch * s_map[ch]
            ordered_s += new_s
        
        return ordered_s
        
        
        