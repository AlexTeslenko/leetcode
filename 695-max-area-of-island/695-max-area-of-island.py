from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        def bfs(grid, row, col):
            dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            cur_area = 0
            queue = deque([(row, col)])
            grid[row][col] = 0
            while queue:
                row, col = queue.popleft()
                cur_area += 1
                for dr in dirs:
                    new_row, new_col = dr[0] + row, dr[1] + col
                    
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and \
                        grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 0
                        queue.append((new_row, new_col))
            
            return cur_area
        
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = bfs(grid, row, col)
                    #print(area)
                    max_area = max(max_area, area)
        
        return max_area
                    
                    
                
        
        