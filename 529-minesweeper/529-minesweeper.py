class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        
        click_row, click_col = click[0], click[1]
        
        if board[click_row][click_col] == 'M':
            board[click_row][click_col] = 'X'
            return board
        
        
        def dfs(board, cur_row, cur_col):
            if board[cur_row][cur_col] != 'E':
                return
            
            directions = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
            
            num_mines = 0
            for dr in directions:
                new_row = cur_row + dr[0]
                new_col = cur_col + dr[1]
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                    if board[new_row][new_col] == 'M':
                        num_mines += 1
            
            print(num_mines)
            if num_mines:
                board[cur_row][cur_col] = str(num_mines)
                return
            else:
                board[cur_row][cur_col] = 'B'
                
            for dr in directions:
                new_row = cur_row + dr[0]
                new_col = cur_col + dr[1]
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                    dfs(board, new_row, new_col)
            
        dfs(board, click_row, click_col)
        return board
                
            
                