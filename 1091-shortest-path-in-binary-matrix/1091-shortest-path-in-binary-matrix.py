from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (1,-1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        min_path_lenght = 1000
        if grid[0][0] == 1:
            return -1
        
        queue = deque([(0,0,1)])
        grid[0][0] = 1
        while queue:
            row, col, path_ln = queue.popleft()
            
            if row == len(grid)-1 and col == len(grid[0])-1:
                min_path_lenght = min(min_path_lenght, path_ln)
            
            for dr in dirs:
                new_row = row + dr[0]
                new_col = col + dr[1]
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 0:
                    queue.append((new_row, new_col, path_ln+1))
                    grid[new_row][new_col] = 1
        
        return min_path_lenght if min_path_lenght != 1000 else -1
            
            
        
        