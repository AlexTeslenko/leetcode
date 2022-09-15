class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0 for i in range(n)] for _ in range(n)]
        self.cols = {i:0 for i in range(n)}
        self.rows = {i:0 for i in range(n)}
        self.diags = {0: 0, 1: 0}
        

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.board[row][col] = 1
        else:
            self.board[row][col] = -1
            
        self.cols[col] += self.board[row][col]
        self.rows[row] += self.board[row][col]
            
        if col + row == self.n - 1:
            self.diags[1] += self.board[row][col]
        if row == col:
            self.diags[0] += self.board[row][col]
        
        for col in self.cols:
            if self.cols[col] == self.n:
                return 1
            elif self.cols[col] == -self.n:
                return 2
        
        for row in self.rows:
            if self.rows[row] == self.n:
                return 1
            elif self.rows[row] == -self.n:
                return 2
        
        for diag in self.diags:
            if self.diags[diag] == self.n:
                return 1
            elif self.diags[diag] == -self.n:
                return 2
        return 0
        
            
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)