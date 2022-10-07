from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_ints = Counter(arr)
        
        return len(set(num_ints.values())) == len(num_ints)
        