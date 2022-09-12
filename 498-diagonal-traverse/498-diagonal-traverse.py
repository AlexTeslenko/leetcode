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
        up = True
        for i in range(len(mat[0])):
            intermediate_result = []
            k = i
            j = 0
            while k >= 0 and j < len(mat):
                intermediate_result.append(mat[j][k])
                k -= 1
                j += 1
            
            if up:
                intermediate_result.reverse()
            
            up = not up
            
            output += intermediate_result
        
        for i in range(1, len(mat)):
            intermediate_result = []
            j = i
            k = len(mat[0]) - 1
            
            while j < len(mat) and k >= 0:
                intermediate_result.append(mat[j][k])
                j += 1
                k -= 1
            
            if up:
                intermediate_result.reverse()
            up = not up
            
            output += intermediate_result
                
        
        return output
    '''
                        
                
                