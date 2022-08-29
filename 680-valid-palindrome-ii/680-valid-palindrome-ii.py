class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        left_ptr, right_ptr = 0, len(s)-1
        
        while left_ptr < right_ptr:
            if s[left_ptr] == s[right_ptr]:
                left_ptr += 1
                right_ptr -= 1
            elif  s[left_ptr] != s[right_ptr]:
                return self.check_palindrom(s, left_ptr+1, right_ptr) or self.check_palindrom(s, left_ptr, right_ptr-1)
        
        return True
    
    def check_palindrom(self, s, left_ptr, right_ptr):
        while left_ptr < right_ptr:
            if s[left_ptr] == s[right_ptr]:
                left_ptr += 1
                right_ptr -= 1
            else:
                return False
        return True
    
    '''
        s_revert = s[::-1]
        i, j = 0, len(s) - 1
    
        while i <= j:
            if s[i] != s[j]:
                return self.check_palindrom(s, i+1, j) or self.check_palindrom(s, i, j-1)
            i += 1
            j -= 1
        return True

    
    def check_palindrom(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
    '''
            
            
