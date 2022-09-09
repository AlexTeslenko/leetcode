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
    
    '''
        ch_order = {ch:i for i, ch in enumerate(order)}
        s_ordered = [[] for ch in order]
        
        new_s = ""
        for ch in s:
            if ch in ch_order:
                s_ordered[ch_order[ch]].append(ch)
            else:
                new_s = new_s + ch
        
        ordered_s = ""
        for el in s_ordered:
            if len(el):
                for ch in el:
                    ordered_s = ordered_s + ch
        
        return ordered_s + new_s
    '''
        
        