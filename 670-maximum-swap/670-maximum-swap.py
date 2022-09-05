class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(ch) for ch in str(num)]

        idx_to_swap, digit_to_swap = -1, -1

        for i in range(1, len(digits)):
            if digits[i] > digits[i-1]:
                idx_to_swap = i - 1
                digit_to_swap = digits[i-1]
                break
        
        if idx_to_swap != -1:
            max_idx, max_num_to_swap = i, digits[i]
            for i in range(max_idx+1, len(digits)):
                if digits[i] >= max_num_to_swap:
                    max_idx = i
                    max_num_to_swap = digits[i]
            
            for i in range(max_idx, -1, -1):
                if digits[i] < max_num_to_swap:
                    idx_to_swap = i
            
            digits[idx_to_swap], digits[max_idx] = digits[max_idx],  digits[idx_to_swap]
                    
        new_num = 0
        for digit in digits:
            new_num = new_num * 10 + digit
                
        return new_num
        