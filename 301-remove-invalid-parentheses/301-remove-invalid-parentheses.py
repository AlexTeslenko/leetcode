class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        min_removed = len([i for i in s if i in ['(', ')']])
        output = []
        
        
        def backtracking(s, cur_i, cur_s, left_prs, right_prs, removed_prs):
            if right_prs > left_prs:
                    return
                
            if cur_i >= len(s):
                if left_prs == right_prs and removed_prs <= min_removed:
                    output.append(cur_s)
                return
                    

            if s[cur_i] not in ['(', ')']:
                new_cur_s = cur_s+s[cur_i]
                backtracking(s, cur_i+1, new_cur_s, left_prs, right_prs, removed_prs)
            else:
                backtracking(s, cur_i+1, cur_s, left_prs, right_prs, removed_prs+1)
                
                if  s[cur_i] == '(':
                    new_cur_s = cur_s+s[cur_i]
                    backtracking(s, cur_i+1, new_cur_s, left_prs+1, right_prs, removed_prs)
                    
                else:
                    new_cur_s = cur_s+s[cur_i]
                    backtracking(s, cur_i+1, new_cur_s, left_prs, right_prs+1, removed_prs)
                    
        cur_s = ''
        backtracking(s, 0, cur_s, 0, 0, 0)
        max_str_ln = max([len(s) for s in output])
        
        return set([s for s in output if len(s)==max_str_ln])
        