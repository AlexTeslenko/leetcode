class Solution:
    def compress(self, chars: List[str]) -> int:
        left_ptr, right_ptr, insert_ptr = 0, 0, 0
        while right_ptr < len(chars):
            while right_ptr < len(chars) and chars[left_ptr] == chars[right_ptr]:
                right_ptr += 1
            
            chars[insert_ptr] = chars[left_ptr]
            insert_ptr += 1
                
            if right_ptr - left_ptr > 1:
                num_chs = str(right_ptr - left_ptr)
                for num_ch in num_chs:
                    chars[insert_ptr] = num_ch
                    insert_ptr += 1
            
            left_ptr = right_ptr
        
        
        
        return insert_ptr
                    
                
                
        