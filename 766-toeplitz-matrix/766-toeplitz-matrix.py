class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix[0])):
            first_el = matrix[0][i]
            k = i
            j = 0
            
            while k < len(matrix[0])-1 and j < len(matrix)-1:
                k += 1
                j += 1
                if matrix[j][k] != first_el:
                    return False
        
        for i in range(len(matrix)):
            first_el = matrix[i][0]
            k = 0
            j = i
        
            while k < len(matrix[0])-1 and j < len(matrix)-1:
                k += 1
                j += 1
                if matrix[j][k] != first_el:
                    return False
        
        return True
        