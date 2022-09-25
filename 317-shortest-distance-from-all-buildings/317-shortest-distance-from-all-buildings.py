from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.dists = {}
        self.cur_grid = [[0 for i in self.grid[0]] for j in self.grid]
        self.num_build_visited = [[0 for i in self.grid[0]] for j in self.grid]
    
        def build_distances(row, col, num_visited):
            dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            #cur_grid = [[0 for i in self.grid[0]] for j in self.grid]
            visited = [[0 for i in self.grid[0]] for j in self.grid]
            
            visited[row][col] = 1
            queue = deque([(row, col)])
            steps = 1
            while queue:
                cur_level = len(queue)
                for i in range(cur_level):
                    cur_row, cur_col = queue.popleft()
                    for dr in dirs:
                        new_row, new_col = cur_row + dr[0], cur_col + dr[1]
                        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and not visited[new_row][new_col] and self.grid[new_row][new_col] == 0 and self.num_build_visited[new_row][new_col] == num_visited:
                            visited[new_row][new_col] = 1
                            self.cur_grid[new_row][new_col] += steps
                            self.num_build_visited[new_row][new_col] += 1
                            queue.append((new_row, new_col))
                steps += 1
            
            #return cur_grid
        
        total_houses = 0
        num_visited = -1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.grid[row][col] == 1:
                    total_houses += 1
                    num_visited += 1
                    cur_grid = build_distances(row, col, num_visited)
        
        min_dist = math.inf
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.grid[row][col] == 0:
                    if  self.num_build_visited[row][col] == total_houses:
                        min_dist = min(min_dist, self.cur_grid[row][col])
        
        return min_dist if min_dist < math.inf else -1
                    
                        
                         
                
        
        
                        
                    
                
                      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    '''
        min_dist = math.inf
        num_buildings = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    num_buildings += 1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 1 and grid[row][col] != 2:
                    cur_dist = self.calc_dist(grid, num_buildings, row, col)
                    #print(row, col)
                    #print(cur_dist)
                    min_dist = min(min_dist, cur_dist)
        
        return min_dist if min_dist < math.inf else -1
        
    
    def calc_dist(self, grid, num_buildings, cur_row, cur_col):
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited_nodes = [[False for _ in grid[0]] for j in grid]
        visited_nodes[cur_row][cur_col] = True
        next_steps = deque([(cur_row, cur_col)])
        total_steps = 0
        cur_steps = 0
        found_buildings = 0
        
        while next_steps and found_buildings != num_buildings:
            leve_size = len(next_steps)
            for i in range(leve_size):
                cur_step = next_steps.popleft()
                row = cur_step[0]
                col = cur_step[1]
                if grid[row][col] == 1:
                    found_buildings += 1
                    total_steps += cur_steps
                    #print(row, col, cur_steps)
                    continue
                
            
                for direction in directions:
                    next_row = row + direction[0]
                    next_col = col + direction[1]
                
                    if next_row >= 0 and next_col >= 0 and next_row < len(grid) and next_col < len(grid[0]) and not visited_nodes[next_row][next_col] and grid[next_row][next_col] != 2:
                        next_steps.append((next_row, next_col))
                        visited_nodes[next_row][next_col] = True
            
            cur_steps += 1
            
        
        if num_buildings != found_buildings:
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 0 and visited_nodes[row][col]:
                        grid[row][col] == 2
            return math.inf
        
        return total_steps
    '''                
        
        
        
        
        
    '''    
        
        min_distance = math.inf
        
        rows = len(grid)
        cols = len(grid[0])
        
        num_houses = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    num_houses += 1
                    
        for i in range(rows):
            for j in range(cols):
                min_distance = min(min_distance, self.find_distance(grid, i, j, num_houses))
        
        return min_distance
        
        
    
    def find_distance(self, grid, row, col, num_houses):
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque([[row, col]])
        
        visited = [[False for i in range(cols)] for j in range(rows)]
        visited[row][col] = True
        
        ditance_sum = 0
        houses_reached = 0
        steps = 0
        
        while queue and houses_reached != num_houses:
            level_size = len(queue)
            for i in range(level_size):
                curr = queue.popleft()
                
                row = curr[0]
                col = curr[1]
                
                if grid[row][col] == 1:
                    houses_reached += 1
                    ditance_sum += steps
                    continue
                    
                for dr in dirs:
                    next_row = row + dr[0]
                    next_col = col + dr[1]
                    
                    if next_row >= 0 and next_col >= 0 and next_row < rows and next_col < cols: 
                        if not visited[next_row][next_col] and grid[row][col] != 2:
                            queue.append([next_row, next_col])
                            visited[next_row][next_col] = True
                        
            steps += 1
            
        #print(houses_reached)
        if houses_reached != num_houses:
            for i in range(rows):
                for j in range(cols):
                    if grid[row][col] == 0 and visited[row][col] == True:
                        grid[row][col] = 2
                
            return math.inf
            
        return ditance_sum
                        
    '''
        
        
        
        
        
        
        
        
        
        