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
            
            
