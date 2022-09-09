class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        degr_per_hour = 360/12
        degr_per_min_in_hour = degr_per_hour / 60
        degr_per_min = 360 / 60
        
        hour %= 12
        hour_degree = hour * degr_per_hour + minutes * degr_per_min_in_hour
        min_degree = minutes * degr_per_min
        
        print(hour_degree)
        print(min_degree)
        
        angle_diff = abs(min_degree - hour_degree)
        if angle_diff > 180:
            return 360 - angle_diff
        return angle_diff
        
        