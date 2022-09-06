class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hash_maps = {}
        for s in strings:
            first_ch = s[0]
            first_num = (ord(first_ch) - ord('a'))
            num = ''
            for ch in s:
                cur_num = (ord(ch) - first_num) % 26
                num = num + str(cur_num)
            
            if num not in hash_maps:
                hash_maps[num] = []
            hash_maps[num].append(s)
        
        return hash_maps.values()
            