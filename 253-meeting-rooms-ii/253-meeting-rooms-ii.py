class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_intervals = sorted([interval[0] for interval in intervals])
        end_intervals = sorted([interval[1] for interval in intervals])
        
        start_ptr, end_ptr = 0, 0
        num_rooms = 0
        
        while start_ptr < len(start_intervals):
            if start_intervals[start_ptr] >= end_intervals[end_ptr]:
                end_ptr += 1
            else:
                num_rooms += 1
            
            start_ptr += 1
        
        return num_rooms

            