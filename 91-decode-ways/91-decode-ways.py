class Solution:
    def numDecodings(self, s: str) -> int:
        self.cache = {}
        return self.createEncodings(s, 0)
    
    def createEncodings(self, s, i):
        if i in self.cache:
            return self.cache[i]
        
        if i == len(s):
            return 1
        
        if s[i] == '0':
            return 0
        
        if i+1 == len(s):
            return 1        
        
        num_maps = self.createEncodings(s, i+1)
        
        if 0 < int(s[i:i+2]) <= 26:
            num_maps += self.createEncodings(s, i+2)
        
        self.cache[i] = num_maps
        return self.cache[i] 
        
        