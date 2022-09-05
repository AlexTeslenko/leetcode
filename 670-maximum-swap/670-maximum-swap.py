class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(ch) for ch in str(num)]
        #cur_num = num
        #while cur_num:
        #    last_digit = cur_num % 10
        #    digits.append(last_digit)
        #    cur_num //= 10
            
        idx_to_swap, digit_to_swap = -1, -1
        #digits.reverse()
        print(digits)
        for i in range(1, len(digits)):
            if digits[i] > digits[i-1]:
                idx_to_swap = i - 1
                digit_to_swap = digits[i-1]
                break
        
        print(digit_to_swap)
        
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
                    
        
        
        #if idx_to_swap != -1:
        #    max_num_to_swap = max(digits[idx_to_swap+1:])
        #    max_idx = digits[idx_to_swap+1:].index(max_num_to_swap) + idx_to_swap + 1
        #    print(max_idx)
        #    digits[idx_to_swap], digits[max_idx] = digits[max_idx],  digits[idx_to_swap]
        
        print(digits)
        new_num = 0
        for digit in digits:
            new_num = new_num * 10 + digit
        
          
        
        return new_num
        