class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
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
                        
                
                