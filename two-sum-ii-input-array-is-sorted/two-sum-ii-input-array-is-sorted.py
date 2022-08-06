class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr, right_ptr = 0, len(numbers) - 1
        
        while left_ptr < right_ptr:
            cur_sum = numbers[left_ptr] + numbers[right_ptr]
            if cur_sum == target:
                return [left_ptr+1, right_ptr+1]
            elif cur_sum > target:
                right_ptr -= 1
            else:
                left_ptr += 1
        
        return [-1, -1]
        