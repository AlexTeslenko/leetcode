class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        visited_cells = [[0 for i in range(cols)] for j in range(rows)]
        
        max_path = 0
        for i in range(rows):
            for j in range(cols):
                max_path = max(max_path, self.calculate_path([i,j], matrix, visited_cells))
        
        return max_path
        
    
    def calculate_path(self, cur_cell, matrix, visited):
        rows = len(visited)
        cols = len(visited[0])
        
        first_path, second_path,third_path, fourth_path = 0, 0, 0, 0
        
        if visited[cur_cell[0]][cur_cell[1]]:
            return visited[cur_cell[0]][cur_cell[1]]
        
        if cur_cell[0] > 0:
            if matrix[cur_cell[0]-1][cur_cell[1]] > matrix[cur_cell[0]][cur_cell[1]]:
                first_path = self.calculate_path([cur_cell[0]-1, cur_cell[1]], matrix, visited)
        
        if cur_cell[1] > 0:
            if matrix[cur_cell[0]][cur_cell[1]-1] > matrix[cur_cell[0]][cur_cell[1]]:
                second_path = self.calculate_path([cur_cell[0], cur_cell[1]-1], matrix, visited)
                
        if cur_cell[0] < rows-1:
            if matrix[cur_cell[0]+1][cur_cell[1]] > matrix[cur_cell[0]][cur_cell[1]]:
                third_path = self.calculate_path([cur_cell[0]+1, cur_cell[1]], matrix, visited)
        
        if cur_cell[1] < cols-1:
            if matrix[cur_cell[0]][cur_cell[1]+1] > matrix[cur_cell[0]][cur_cell[1]]:
                fourth_path = self.calculate_path([cur_cell[0], cur_cell[1]+1], matrix, visited)
                
        visited[cur_cell[0]][cur_cell[1]] = max(first_path, second_path,third_path, fourth_path) + 1
        
        return  visited[cur_cell[0]][cur_cell[1]]
        
        
            
            
        