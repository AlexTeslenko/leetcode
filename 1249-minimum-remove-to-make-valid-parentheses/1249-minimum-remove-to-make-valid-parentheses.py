class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removed_idx = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    removed_idx.append(i)
        
        removed_idx += stack
        
        result_str = ""
        for i in range(len(s)):
            if s[i] not in [')', '(']:
                result_str = result_str + s[i]
            else:
                if i not in removed_idx:
                    result_str = result_str + s[i]
        
        return result_str
        