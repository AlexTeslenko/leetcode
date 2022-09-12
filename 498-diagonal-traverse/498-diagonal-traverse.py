class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        rows, cols = len(mat), len(mat[0])
        up = True
        for col in range(cols):
            j = col
            row = 0
            cur_diag = []
            while j >= 0 and row < rows:
                cur_diag.append(mat[row][j])
                j -= 1
                row += 1
            
            if up:
                cur_diag.reverse()
            up = not up
            output += cur_diag
        
        for row in range(1, rows):
            j = row
            col = cols - 1
            cur_diag = []
            
            while j < rows and col >= 0:
                cur_diag.append(mat[j][col])
                j += 1
                col -= 1
            
            if up:
                cur_diag.reverse()
            up = not up
            output += cur_diag
                
        return output
            
            
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    ''' 
        
        output = []
        rows, cols = len(mat), len(mat[0])
        i, j = 0, 0
        down = False
        while len(output) < rows * cols:
            output.append(mat[i][j])
            print(mat[i][j])
            if down:
                i += 1
                j -= 1
                
                if i >= rows or j < 0:
                    if i >= rows:
                        i -= 1
                        j += 2
                    if j < 0:
                        j += 1
                    down = False
            else:
                i -= 1
                j += 1
                if i < 0 or j >= cols:
                    if i < 0 and j >= cols:
                        i += 2
                        j -= 1
                    elif i < 0:
                        i += 1
                    elif j >= cols:
                        j -= 1
                    down = True
        
            print(i, j)
        return output
    '''
                        
                
                