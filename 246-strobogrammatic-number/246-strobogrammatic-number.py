class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        reversed_num = ''
        for ch in num[::-1]:
            if ch == '9':
                reversed_num += '6'
            elif ch =='6':
                reversed_num += '9'
            elif ch in ['0', '1', '8']:
                reversed_num += ch
            else:
                reversed_num += 'n'
        return num == reversed_num
        