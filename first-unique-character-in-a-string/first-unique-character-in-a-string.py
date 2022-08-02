class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_ocurs = {}
        for i in range(len(s)):
            if s[i] not in ch_ocurs:
                ch_ocurs[s[i]] = [i, 0]
            
            ch_ocurs[s[i]][1] += 1
            
        
        uniq_chars = [val[0] for key,val in ch_ocurs.items() if val[1] == 1]
        
        return min(uniq_chars) if len(uniq_chars) else -1
        
        
        