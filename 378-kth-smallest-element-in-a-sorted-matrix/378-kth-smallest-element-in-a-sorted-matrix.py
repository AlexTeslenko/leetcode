class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        elements = []
        for row in matrix:
            elements += row
        
        elements.sort()
        return elements[k-1]
        