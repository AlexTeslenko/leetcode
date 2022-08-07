class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = math.inf
        closest_target = math.inf
        for i in range(len(nums)):
            left_ptr, right_ptr = i + 1, len(nums) - 1
            while left_ptr < right_ptr:
                cur_target = nums[i] + nums[left_ptr] + nums[right_ptr]
                cur_diff =  target - cur_target
                if abs(cur_diff) < abs(diff):
                    diff = cur_diff
                    closest_target = cur_target
                if cur_target <  target:
                    left_ptr += 1
                elif cur_target >= target:
                    right_ptr -= 1
            
            if diff == 0:
                break
                    
        return closest_target
                
        