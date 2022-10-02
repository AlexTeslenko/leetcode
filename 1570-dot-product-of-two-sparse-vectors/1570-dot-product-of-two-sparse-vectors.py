class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx_to_num = {i: num for i, num in enumerate(nums) if num}
        
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_prod = 0
        for idx in vec.idx_to_num:
            if idx in self.idx_to_num:
                dot_prod += self.idx_to_num[idx] * vec.idx_to_num[idx]
        
        return dot_prod

    
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)