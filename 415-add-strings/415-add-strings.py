class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for ch in num1:
            n = ord(ch) - ord('0')
            n1 = n1 * 10 + n
        
        for ch in num2:
            n = ord(ch) - ord('0')
            n2 = n2 * 10 + n
        
        return str(n1 + n2)

        
        
        