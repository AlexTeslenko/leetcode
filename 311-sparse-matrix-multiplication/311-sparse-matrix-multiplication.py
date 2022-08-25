class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        output = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                s = 0
                for l in range(k):
                    s += mat1[i][l] * mat2[l][j]
                
                output[i][j] = s
        
        return output
                
                
        