class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = [(i, num) for i, num in enumerate(nums) if num]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        vec1_ptr, vec2_ptr = 0, 0
        dot_product = 0
        while vec1_ptr < len(self.nums) and vec2_ptr < len(vec.nums):
            if self.nums[vec1_ptr][0] == vec.nums[vec2_ptr][0]:
                dot_product += self.nums[vec1_ptr][1] * vec.nums[vec2_ptr][1]
                vec1_ptr += 1
                vec2_ptr += 1
            elif self.nums[vec1_ptr][0] < vec.nums[vec2_ptr][0]:
                vec1_ptr += 1
            else:
                vec2_ptr += 1
        
        return dot_product
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)