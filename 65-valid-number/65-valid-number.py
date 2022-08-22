class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit, seen_exp, seen_dot = False, False, False
        for i in range(len(s)):
            ch = s[i]
            if ch.isnumeric():
                seen_digit = True
            elif ch in ['+', '-']:
                if i != 0 and (i > 0 and s[i-1] not in ['e', 'E']):
                    return False
            elif ch in ['e', 'E']:
                if not seen_digit or seen_exp:
                    return False
                else:
                    seen_exp = True
                    seen_digit = False
            elif ch == '.':
                if seen_dot or seen_exp:
                    return False
                else:
                    seen_dot = True
            else:
                return False
        
        return seen_digit
                
                
        