class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
    
        def check_feaibility(weights, capasity, days):
            
            cur_weights = 0
            for w in weights:
                cur_weights += w
                if cur_weights > capasity:
                    days -= 1
                    cur_weights = w
            
            if days <= 0:
                return False
            
            return True
        
        min_cap, max_cap = max(weights), sum(weights)
        
        while min_cap < max_cap:
            middle_cap = min_cap + (max_cap - min_cap) // 2
            feacibility = check_feaibility(weights, middle_cap, days)
            if feacibility:
                max_cap = middle_cap
            else:
                min_cap = middle_cap + 1
        
        return max_cap
                
                
            