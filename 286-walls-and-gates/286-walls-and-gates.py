from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        def find_gate(rooms):
            dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            queue = deque()
            
            for row in range(len(rooms)):
                for col in range(len(rooms[0])):
                    if rooms[row][col] == 0:
                        queue.append((row, col))
            
            while queue:
                row, col = queue.popleft()
                for dr in dirs:
                    new_row, new_col = row + dr[0], col + dr[1]
                    if 0 <= new_row < len(rooms) and 0 <= new_col < len(rooms[0]) and rooms[new_row][new_col] != -1:
                        if rooms[new_row][new_col] ==  2147483647:
                            rooms[new_row][new_col] = rooms[row][col] + 1
                            queue.append((new_row, new_col))
                                
        find_gate(rooms)
        

                
                            
                
                
            
            
        