class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        incrementor = 1
        for i in range(len(digits)-1, -1, -1):
            new_digit = digits[i] + incrementor
            if new_digit < 10:
                digits[i] = new_digit
                incrementor = 0
                return digits
            else:
                digits[i] = 0
        
        return [1] + digits
                
        