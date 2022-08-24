class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hash_maps = {}
        for string in strings:
            shift = ord(string[0])
            
            shifted_str = ''
            print(string)
            for ch in string:
                print(str((ord(ch) - shift) % 26))
                shifted_str += str((ord(ch) - shift) % 26 - ord('a')) 
            
            print(shifted_str)
            if shifted_str not in hash_maps:
                hash_maps[shifted_str] = []
            hash_maps[shifted_str].append(string)
        
        print(hash_maps)
        result = [value for value in hash_maps.values()]
        
        return result