class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_int = {   'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        
        num = 0
        i = 0
        while i < len(s):
            if i < len(s)-1:
                ch = s[i: i+2]
                if ch in rom_to_int:
                    num += rom_to_int[ch]
                    i += 2
                    continue
            
            ch = s[i]
            if ch in rom_to_int:
                num += rom_to_int[ch]
                i += 1
        
        return num
                
            
            
        