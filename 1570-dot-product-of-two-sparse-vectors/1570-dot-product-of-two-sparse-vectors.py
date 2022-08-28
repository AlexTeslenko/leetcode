class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx_num = {i: num for i, num in enumerate(nums) if num}
        
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_prod = 0
        for i in self.idx_num:
            if i in vec.idx_num:
                dot_prod += vec.idx_num[i] * self.idx_num[i]
        
        return dot_prod
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)