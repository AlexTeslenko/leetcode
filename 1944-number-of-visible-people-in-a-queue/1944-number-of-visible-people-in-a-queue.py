class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        output = [0 for _ in heights]
        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
                output[i] += 1
            if stack:
                output[i] += 1
                
            stack.append(heights[i])
        
        return output
                
        