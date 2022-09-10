# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        first_one_col = 10000
        col_start_postion = cols - 1
        cur_row_is_zero = False
        for row in range(rows):
            if binaryMatrix.get(row, col_start_postion) != 0:
                low, high = 0, col_start_postion
                while low < high:
                    middle = low + (high - low) // 2
                    if binaryMatrix.get(row, middle) == 1:
                        high = middle
                    else:
                        low = middle + 1
                if binaryMatrix.get(row, high) == 1:
                    first_one_col = min(first_one_col, high)
                    col_start_postion = high
                             
        
        return first_one_col if first_one_col < 10000 else -1
    
    
    '''
        rows, cols = binaryMatrix.dimensions()
        first_one_col = 10000
        col_start_postion = cols - 1
        cur_row_is_zero = False
        for row in range(rows):
            if binaryMatrix.get(row, col_start_postion) != 0:
                col = col_start_postion
                cur_row_is_zero = False
                while col >= 0 and not cur_row_is_zero:
                    if binaryMatrix.get(row, col) == 1:
                        if col < first_one_col:
                            first_one_col = col
                    else:
                        cur_row_is_zero = True
                    
                    col -= 1
                
                col_start_postion = col+1               
        
        return first_one_col if first_one_col < 10000 else -1
    '''