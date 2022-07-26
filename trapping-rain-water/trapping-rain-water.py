class Solution:
    def trap(self, height: List[int]) -> int:
        if not len(height):
            return 0
        
        total_water_level = 0
        left_idx, right_idx = 0, len(height)-1
        left_max, right_max = 0, 0
        while(left_idx <= right_idx):
            if height[left_idx] < height[right_idx]:
                if height[left_idx] < left_max:
                    total_water_level += left_max - height[left_idx]
                else:
                    left_max = height[left_idx]
                left_idx += 1
            else:
                if height[right_idx] < right_max:
                    total_water_level += right_max - height[right_idx]
                else:
                    right_max = height[right_idx]
                right_idx -= 1
        
        return total_water_level
        