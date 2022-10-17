class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i+1 for i in range(n)]
        
        def find_winner(friends, i, k):
            if not friends:
                return
            
            if len(friends) == 1:
                return friends[0]
            
            
            next_i = (i+k-1) % len(friends)
            friends.pop(next_i)
          
            winner = find_winner(friends, next_i, k)
            
            return winner
        
        winner = find_winner(friends, 0, k)
        
        return winner
            