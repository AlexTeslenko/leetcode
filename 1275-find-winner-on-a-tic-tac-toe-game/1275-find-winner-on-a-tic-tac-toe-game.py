class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        field = [[0 for i in range(3)] for j in range(3)]
        for i in range(len(moves)):
            move = moves[i]
            if i % 2 == 0:
                field[move[0]][move[1]] = 1
            else:
                field[move[0]][move[1]] = -1
        
        sm = 0
        for row in field:
            if sum(row) == 3:
                return 'A'
            elif sum(row) == -3:
                return 'B'
        
        for i in range(3):
            col_sum = sum([row[i] for row in field])
            if col_sum == 3:
                return 'A'
            elif col_sum == -3:
                return 'B'
        
        diag_1_sm = sum([row[i] for i, row in enumerate(field)])
        diag_2_sm = sum([row[len(field[0]) - i - 1] for i, row in enumerate(field)])
        
        if diag_1_sm == 3 or diag_2_sm == 3:
            return 'A'
        
        if diag_1_sm == -3 or diag_2_sm == -3:
            return 'B'
        
        for row in field:
            if 0 in row:
                return 'Pending'
        
        return 'Draw'
            
        