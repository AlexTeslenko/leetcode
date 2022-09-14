import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(min(k, len(matrix))):
            heap.append((matrix[i][0], i, 0))
        
        heapq.heapify(heap)
        
        while k > 1:
            #print(heap)
            el, row, col = heapq.heappop(heap)
            if row < len(matrix) and col+1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[row][col+1], row, col+1))
            k -= 1
        
        #print(heap)
        el, row, col = heapq.heappop(heap)
        return el
    
    
    
    
    
    
    
    ''' 
        elements = []
        for row in matrix:
            elements += row
        
        elements.sort()
        return elements[k-1]
    '''
        