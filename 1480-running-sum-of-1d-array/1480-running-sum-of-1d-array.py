class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        running_sum = 0
        
        for num in nums:
            running_sum += num
            output.append(running_sum)
        
        return output