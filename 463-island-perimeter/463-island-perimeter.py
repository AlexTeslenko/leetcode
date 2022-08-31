class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        pr = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    cur_pr = 4
                    if row > 0:
                        if grid[row-1][col] == 1:
                            cur_pr -= 1
                    if row < len(grid) - 1:
                        if grid[row+1][col] == 1:
                            cur_pr -= 1
                    if col > 0:
                        if grid[row][col-1] == 1:
                            cur_pr -= 1
                    if col < len(grid[0]) - 1:
                        if grid[row][col+1] == 1:
                            cur_pr -= 1

                    pr += cur_pr
        
        return pr
                        
        