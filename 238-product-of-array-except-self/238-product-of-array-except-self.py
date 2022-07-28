class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1]
        right_product = [0 for i in nums]
        right_product[-1] = 1
        
        for i in range(0, len(nums)-1):
            product = nums[i] * left_product[i]
            left_product.append(product)
        
        for i in range(len(nums)-1, 0, -1):
            product = nums[i] * right_product[i]
            right_product[i-1] = product
            
        products = []
        
        for i in range(len(nums)):
            products.append(left_product[i] * right_product[i])
        
        return products