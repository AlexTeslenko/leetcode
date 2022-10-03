class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_ranges = {}
        for i, ch in enumerate(s):
            if ch not in letter_ranges:
                letter_ranges[ch] = [i, i]
            letter_ranges[ch][1] = i
        
        letter_ranges_list = list(letter_ranges.values())
        
        merged_ranges = []
        
        range_start = letter_ranges_list[0][0]
        range_end = letter_ranges_list[0][1]
        
        for i in range(1, len(letter_ranges_list)):
            if letter_ranges_list[i][0] <= range_end:
                range_end = max(range_end, letter_ranges_list[i][1])
            else:
                merged_ranges.append((range_start, range_end))
                range_start = letter_ranges_list[i][0]
                range_end = letter_ranges_list[i][1]
        
        merged_ranges.append((range_start, range_end))
        
        output = [rn[1] - rn[0] + 1 for rn in merged_ranges]
        return output
        
        