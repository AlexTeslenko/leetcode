class Solution:
    def countSubstrings(self, s: str) -> int:
        total_polinfromes = 0 
        dp = [[False for _ in s] for i in s]
        
        for i in range(len(s)):
            total_polinfromes += 1
            dp[i][i] = True
        
        for i in range(0, len(s)-1):
            dp[i][i+1] = s[i] == s[i+1]
            total_polinfromes += dp[i][i+1]
        
        for ln in range(3, len(s)+1):
            i = 0
            j = i + ln - 1
            while j < len(s):
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                total_polinfromes += dp[i][j]
                i += 1
                j += 1
   
        return total_polinfromes
    
        
        '''
        num_paindrs = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    #print(s[i:j])
                    num_paindrs += 1
        return num_paindrs
        '''
    
    
 