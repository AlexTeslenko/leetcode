class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start_prt = 0
        max_num_fruits = 0
        cur_num_fruits = 0
        cur_fruits = {}
        
        for end_ptr in range(len(fruits)):
            if fruits[end_ptr] not in cur_fruits:
                cur_fruits[fruits[end_ptr]] = 0
            
            cur_fruits[fruits[end_ptr]] += 1
            cur_num_fruits += 1
                  
            while len(cur_fruits) > 2:
                cur_fruits[fruits[start_prt]] -= 1
                if cur_fruits[fruits[start_prt]] == 0:
                    del cur_fruits[fruits[start_prt]]
                    
                start_prt += 1
                cur_num_fruits -= 1
                       
            max_num_fruits = max(max_num_fruits, cur_num_fruits)
            
        return max_num_fruits
            
            
        
        