class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        num_prs = n
        output = []
        def generate_prs(cur_str, num_open, num_closed):
            if num_open > num_prs:
                return
            
            if num_open == num_closed and  num_open == num_prs:
                output.append(cur_str[:])
                return
            
            if num_open == num_closed:
                new_str = cur_str[:] 
                new_str += "("
                generate_prs(new_str, num_open+1, num_closed)
            elif num_open > num_closed:
                new_str_1 = cur_str[:] 
                new_str_1 += "("
                generate_prs(new_str_1, num_open+1, num_closed)
                new_str_2 = cur_str[:] 
                new_str_2 += ")"
                generate_prs(new_str_2, num_open, num_closed+1)
                
        generate_prs('', 0, 0)
        
        return output
                
                
                
                
            
            
        