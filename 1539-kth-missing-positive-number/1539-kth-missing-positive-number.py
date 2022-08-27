class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = left + (right - left) // 2
            missed_nums = arr[middle] - middle - 1
            if missed_nums < k:
                left = middle + 1
            else:
                right = middle - 1
        
        return k + left