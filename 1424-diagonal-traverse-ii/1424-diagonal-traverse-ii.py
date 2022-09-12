class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:   
        output = []
        
        diags = {}
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                if row + col not in diags:
                    diags[row + col] = []
                diags[row + col].append(nums[row][col])
        
        for item in diags.values():
            output += reversed(item)
                      
        return output
                
        