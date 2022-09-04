class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        def check_feasible(ribbons, length):
            num_ribbons = 0
            for i in range(len(ribbons)):
                cur_ribbon = ribbons[i]
                num_ribbons += cur_ribbon // length
            
            return num_ribbons
        
        if sum(ribbons) < k :
            return 0
        
        low, high = 1, max(ribbons)
        max_lenght = 0 
        while low <= high:
            middle = low + (high - low) // 2
            cur_num_ribbons = check_feasible(ribbons, middle)
            if cur_num_ribbons < k:
                high = middle - 1 
            else:
                max_lenght = middle
                low = middle + 1
        
        return high
            
        
                    
        