class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def recursive_find(candidates, cur_idx, cur_target, cur_comb):
            if cur_target < 0 or cur_idx >= len(candidates):
                return
            
            if cur_target == 0:
                if cur_comb not in output:
                    output.append(cur_comb[:])
                
            new_comb = cur_comb[:]
            new_comb.append(candidates[cur_idx])
            
            recursive_find(candidates, cur_idx+1, cur_target-candidates[cur_idx], new_comb)
            recursive_find(candidates, cur_idx, cur_target-candidates[cur_idx], new_comb)
            recursive_find(candidates, cur_idx+1, cur_target, cur_comb[:])
            #recursive_find(candidates, cur_idx, cur_target, cur_comb[:])
            
        
        recursive_find(candidates, 0, target, [])
        
        return output
        