class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        not_found_substr = False
        
        def form_str(source, cur_target):
            if not cur_target:
                return 0
            
            
            i, j = 0, 0          
            found_substr = False
            while i < len(source) and j < len(cur_target):
                if source[i] == cur_target[j]:
                    found_substr = True
                    j += 1
                
                i += 1
               
                
            if found_substr:
                num_sub = form_str(source, cur_target[j:])
                if num_sub == -1:
                    return -1
                else:
                    return 1 + num_sub  
            else:
                not_found_substr = True
                return -1
        
        return form_str(source, target)

                    
                    
            