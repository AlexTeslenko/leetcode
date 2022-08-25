from collections import defaultdict
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        mat1_map, mat2_map = {}, {}
        output = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(k):
                if mat1[i][j]:
                    if  i not in mat1_map:
                        mat1_map[i] = []
                    mat1_map[i].append(j)
        
        for i in range(k):
            for j in range(n):
                if mat2[i][j]:
                    if  i not in mat2_map:
                        mat2_map[i] = []
                    mat2_map[i].append(j)
        
        for i in mat1_map:
            for k in mat1_map[i]:
                if k in mat2_map:
                    for l in mat2_map[k]:
                        print(i, k , l)
                        output[i][l] += mat1[i][k] * mat2[k][l]
                        
            
        
        print(mat1_map)
        print(mat2_map)
        
        return output
                    
        #m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        #output = [[0 for i in range(n)] for j in range(m)]
        #for i in range(m):
        #    for j in range(n):
        #        s = 0
        #        for l in range(k):
        #            s += mat1[i][l] * mat2[l][j]
                
        #        output[i][j] = s
        
        #return output
                
                
        