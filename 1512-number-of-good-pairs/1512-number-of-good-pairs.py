class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_dict = {}
        output = 0
        for num in nums:
            if num in nums_dict:
                output += nums_dict[num]
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        return output
        