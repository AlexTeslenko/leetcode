class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if len(stack):
                if stack[-1] != ch:
                    stack.append(ch)
                else:
                    stack.pop()
            else:
                 stack.append(ch)
        
        
        result_s = ''.join(stack)
        
        return result_s