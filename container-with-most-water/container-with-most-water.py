class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_ptr, right_ptr = 0, len(height) - 1
        
        while left_ptr < right_ptr:
            cur_area = (right_ptr - left_ptr) * min(height[left_ptr], height[right_ptr])
            max_area = max(max_area, cur_area)
            
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        
        return max_area
            