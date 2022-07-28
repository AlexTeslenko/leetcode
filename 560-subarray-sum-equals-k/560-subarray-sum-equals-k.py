class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        total = 0
        
        for start in range(len(nums)):
            cur_sum = 0
            for end in range(start, len(nums)):
                cur_sum += nums[end]
                if cur_sum == k:
                    total += 1 
        
        return total
        '''
        
        total = 0
        sum_occurances = {0:1}
        cur_sum = 0
        end_k_diff = k
        for i in range(len(nums)):
            cur_sum += nums[i]
            end_k_diff = cur_sum - k
            if end_k_diff in sum_occurances:
                total += sum_occurances[end_k_diff]
            
            if cur_sum  not in sum_occurances:
                sum_occurances[cur_sum] = 0
            
            sum_occurances[cur_sum] += 1
        
        return total
            