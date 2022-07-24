class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {0: 0}
        min_num_coins = self.calcChange(coins, amount, cache)
        
        if min_num_coins == math.inf:
            return -1 
        return min_num_coins
        
    def calcChange(self, coins: List[int], amount: int, cache: dict):
        if amount in cache:
            return cache[amount]
        
        num_coins = [math.inf]
        for coin in coins:
            new_amount = amount - coin
            if new_amount >= 0:
                num_coins.append(self.calcChange(coins, new_amount, cache))
            
        
        min_num_coins = min(num_coins) + 1
        
        cache[amount] = min_num_coins
        
        return cache[amount]
        