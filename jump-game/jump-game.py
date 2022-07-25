class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i
        
        return last_position == 0
        
        
        """
        ch = [-1 for i in nums]
        ch[len(nums)-1] = True
        return self.jump(0, nums, len(nums)-1, ch)
        
    
    def jump(self, cur_idx: int, nums: List[int], nums_len: int, ch: List[int]) -> bool:
        if cur_idx == nums_len:
            return True
        
        if cur_idx > nums_len: 
            return False
        
        if ch[cur_idx] != -1:
            return ch[cur_idx]
        
        cur_num = nums[cur_idx]
        
        if cur_num == 0:
             return False

        for num in range(1, cur_num+1):
            if self.jump(cur_idx+num, nums, nums_len, ch):
                ch[cur_idx] = True
                return ch[cur_idx]
        
        ch[cur_idx] = False
        
        return ch[cur_idx]
        """