class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        
        for i, num in enumerate(nums):
            right_sum -= num
            print(left_sum, right_sum)
            if left_sum == right_sum:
                return i
            left_sum += num
           
        
        return -1
            

                
            
        