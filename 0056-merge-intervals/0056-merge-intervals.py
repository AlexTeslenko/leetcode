class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        start_interval, end_interval = intervals[0][0], intervals[0][1]
        
        merged_intervals = []
        for i in range(1, len(intervals)):
            if intervals[i][0] >= start_interval and intervals[i][0] <= end_interval:
                end_interval = max(end_interval, intervals[i][1])
            else:
                merged_intervals.append([start_interval, end_interval])
                start_interval, end_interval = intervals[i][0], intervals[i][1]
                
        merged_intervals.append([start_interval, end_interval])
        
        return merged_intervals
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        intervals.sort(key=lambda x: x[0])
        
        merged_intervals = []
        start_int = intervals[0][0]
        end_int = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end_int:
                end_int = max(end_int, intervals[i][1])
            else:
                merged_intervals.append([start_int, end_int])
                start_int = intervals[i][0]
                end_int = intervals[i][1]
        
        merged_intervals.append([start_int, end_int])
        
        return merged_intervals
        
        
        '''
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []
        i = 1
        cur_inteval = intervals[0]
        while i < len(intervals):
            if (cur_inteval[0] <= intervals[i][0] and cur_inteval[1] >= intervals[i][0]) or (
                cur_inteval[0] >= intervals[i][0] and cur_inteval[0] <= intervals[i][1]):
                cur_inteval = [min(cur_inteval[0], intervals[i][0]), max(cur_inteval[1], intervals[i][1])]
                print(cur_inteval)
            else:
                merged_intervals.append(cur_inteval)
                cur_inteval = intervals[i]
            
            i += 1
        
        merged_intervals.append(cur_inteval)
        
        return merged_intervals
        '''
                                                                            
        '''
        i = 0
        merged_intervals = []
        while i < len(intervals):
            cur_interval = intervals[i]
            j = i + 1
            while j < len(intervals) and cur_interval[0] <= intervals[j][0] and cur_interval[1] >= intervals[j][0]:
                j += 1
            
            merged_interval = [min(cur_interval[0], intervals[j-1][0]), 
                                max(cur_interval[1], intervals[j-1][1])]
        
            merged_intervals.append(merged_interval)
            i = j
        
        return merged_intervals
        '''