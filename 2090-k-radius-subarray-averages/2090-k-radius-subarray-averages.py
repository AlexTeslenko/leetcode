class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        averages = []
        cur_sum = 0
        first_sum = True
        for i in range(len(nums)):
            #cur_sum += nums[i]
            if i - k < 0 or i + k >= len(nums):
                averages.append(-1)
            else:
                if first_sum and  i - k == 0 and i + k < len(nums):
                    cur_sum += sum(nums[i-k:i+k+1])
                    first_sum = False
                else:
                    cur_sum -= nums[i-k-1]
                    cur_sum += nums[i+k]
                    
                
                print(i, cur_sum)
                averages.append(int(cur_sum/(k*2+1)))
        
        return averages
                
                
                