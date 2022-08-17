from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        
        visited = set()
        queue = deque()
        queue.append((0, 0, 1))
        diretions = [(-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        min_path = math.inf
        
        while queue:
            cur_node = queue.popleft()
            if cur_node[0] == len(grid) - 1 and cur_node[1] == len(grid[0]) - 1:
                min_path = min(min_path, cur_node[2])
                
            if (cur_node[0], cur_node[1]) not in visited:
                for direction in diretions:
                    new_node = (cur_node[0] + direction[0], cur_node[1] + direction[1])
                    if new_node[0] >= 0 and new_node[0] < len(grid) and new_node[1] >=0 and new_node[1] < len(grid[0]):
                        if grid[new_node[0]][new_node[1]] == 0:
                            queue.append((new_node[0], new_node[1], cur_node[2]+1))
            
            visited.add((cur_node[0], cur_node[1]))
        
        if min_path == math.inf:
            return -1
        
        return min_path
            
        
        