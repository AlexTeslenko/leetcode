class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        stack = []
        output = [0 for i in range(len(temperatures))]
        
        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                prev_idx, prev_temp = stack.pop()
                output[prev_idx] = i - prev_idx
            stack.append((i, temperatures[i]))
        
        return output
        
        '''
        
        ans, s = [0]*len(temperatures), deque()
        for cur, cur_tmp in enumerate(temperatures):
            while s and cur_tmp > temperatures[s[-1]]:
                ans[s[-1]] = cur - s[-1]
                s.pop()
            s.append(cur)
        return ans
                    
        