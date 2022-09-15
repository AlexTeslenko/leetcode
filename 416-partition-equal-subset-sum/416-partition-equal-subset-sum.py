class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        cache = [False for i in range(sum(nums))]
        half_sum = sum(nums) / 2
        #print(half_sum)
        
        @lru_cache(maxsize=None)
        def find_sum(nums, i, cur_sum):
            #print(cur_sum)
            if cur_sum == 0:
                return True
            
            if cur_sum < 0 or i > len(nums) - 1:
                return False
            
            #if cache[int(cur_sum)]:
            #    return cache[int(cur_sum)]
            
            found_sum = find_sum(nums, i+1, cur_sum-nums[i]) or find_sum(nums, i+1, cur_sum)
            #cache[int(cur_sum)] = found_sum
            
            return found_sum
        
        
        found_sum = find_sum(tuple(nums), 0, half_sum)
        #print(cache)
        return found_sum
        