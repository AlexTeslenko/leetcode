class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anns = {}
        for s in strs:
            sorted_s = sorted(s)
            sorted_s = ''.join(sorted_s)
            if sorted_s not in grouped_anns:
                grouped_anns[sorted_s] = []
            grouped_anns[sorted_s].append(s)
        
        return list(grouped_anns.values())
        