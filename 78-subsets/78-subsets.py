class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            cur_len = len(output)
            for i in range(cur_len):
                lst = output[i]
                new_lst = lst + [num]
                output.append(new_lst)
        
        return output
        