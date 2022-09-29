from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        turt, hair = nums[0], nums[0]
        while True:
            turt = nums[turt]
            hair = nums[nums[hair]]
            if turt == hair:
                break
        
        hair = nums[0]
        while hair != turt:
            turt = nums[turt]
            hair = nums[hair]
        return turt