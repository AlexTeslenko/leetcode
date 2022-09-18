import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_to_point = {}
        heap = []
        for i in range(k):
            cur_point = points[i]
            dist = -sqrt(cur_point[0]**2 + cur_point[1]**2)
            if dist not in dist_to_point:
                dist_to_point[dist] = []
            dist_to_point[dist].append(cur_point) 
            heap.append(dist)
        
        heapq.heapify(heap)
        
        for i in range(k, len(points)):
            cur_point = points[i]
            dist = -sqrt(cur_point[0]**2 + cur_point[1]**2)
            heap_max = heapq.heappop(heap)
            if dist > heap_max:
                heapq.heappush(heap, dist)
                if dist not in dist_to_point:
                    dist_to_point[dist] = []
                dist_to_point[dist].append(cur_point)
                dist_to_point[heap_max].pop()
            else:
                heapq.heappush(heap, heap_max)
                
        output = []
        for val in dist_to_point.values():
            if len(val):
                for point in val:
                    output.append(point) 
        return output
        
            