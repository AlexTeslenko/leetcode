class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        self.cache = [[-1 for i in s] for j in s]
        answ = self.construct_palindrome1(s, 0, len(s)-1)
        return answ <= k
    
    def construct_palindrome1(self, s, i, j):

        if i == j:
            return 0
        if i+1 == j:
            if s[i] == s[j]:
                return 0
            else:
                return 1
        
        if self.cache[i][j] != -1:
            return self.cache[i][j]
        
        can_construct_2, can_construct_3  = 0, 0
        if s[i] == s[j]:
            self.cache[i][j] = self.construct_palindrome1(s, i+1, j-1)
        else:
            can_construct_2 = self.construct_palindrome1(s, i+1, j)
            can_construct_3 = self.construct_palindrome1(s, i, j-1)
        
            self.cache[i][j] = 1 + min(can_construct_2, can_construct_3)
        
        return self.cache[i][j]
            
        
        
    def construct_palindrome(self, s, cur_s, i, k, cur_k):
        
        if len(s) - len(cur_s) <= k and cur_s == cur_s[::-1]:
            return True
        
        if i >= len(s) or k < 0:
            return False
        
        if cur_s in self.mp:
            return self.mp[cur_s]
        
        str_1 = cur_s + s[i]
        if str_1 in self.mp:
            str_1_answ = self.mp[str_1]
        else:
            str_1_answ = self.construct_palindrome(s, str_1, i+1,  k, cur_k)
            self.mp[str_1] = str_1_answ
        
        str_2 = cur_s
        if str_2 in self.mp:
            str_2_answ = self.mp[str_2]
        else:
            str_2_answ = self.construct_palindrome(s, str_2, i+1,  k, cur_k-1)
            self.mp[str_2] = str_2_answ
        
        return str_1_answ or str_2_answ