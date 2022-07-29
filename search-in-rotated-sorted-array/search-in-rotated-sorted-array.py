class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = start + (end - start) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] >= nums[start]:
                if target >= nums[start] and target  < nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                if target > nums[middle] and target <= nums[end]:
                    start = middle + 1
                else:
                    end = end - 1
            
        return -1
        