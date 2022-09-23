class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = deque()
        output = [0] * len(temperatures)
        
        for i, cur_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_temp:
                prev_idx = stack.pop()
                output[prev_idx] = i - prev_idx
            stack.append(i)
        
        return output
        
        '''
        
        ans, s = [0]*len(temperatures), deque()
        for cur, cur_tmp in enumerate(temperatures):
            while s and cur_tmp > temperatures[s[-1]]:
                ans[s[-1]] = cur - s[-1]
                s.pop()
            s.append(cur)
        return ans
        ''' 
        