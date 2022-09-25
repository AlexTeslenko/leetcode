class Solution:
    def intToRoman(self, num: int) -> str:
        roman_int = ''
        i = 0
        while num:
            reminder = num % 10
            num = num // 10
            
            if i == 0:
                if reminder == 4:
                    roman_int = 'IV' + roman_int
                elif reminder == 9:
                    roman_int = 'IX' + roman_int
                elif reminder < 4:
                    roman_int = reminder * 'I' + roman_int
                elif reminder < 9:
                    roman_int = 'V' + (reminder - 5) * 'I' + roman_int
            elif i == 1:
                if reminder == 4:
                    roman_int = 'XL' + roman_int
                elif reminder == 9:
                    roman_int = 'XC' + roman_int
                elif reminder < 4:
                    roman_int = reminder * 'X' + roman_int
                elif reminder < 9:
                    roman_int = 'L' + (reminder - 5) * 'X' + roman_int
            elif i == 2:
                if reminder == 4:
                    roman_int = 'CD' + roman_int
                elif reminder == 9:
                    roman_int = 'CM' + roman_int
                elif reminder < 4:
                    roman_int = reminder * 'C' + roman_int
                elif reminder < 9:
                    roman_int = 'D' + (reminder - 5) * 'C' + roman_int
            elif i == 3:
                    roman_int = reminder * 'M' + roman_int
            
            i += 1
        
        return roman_int
            
            
            
            