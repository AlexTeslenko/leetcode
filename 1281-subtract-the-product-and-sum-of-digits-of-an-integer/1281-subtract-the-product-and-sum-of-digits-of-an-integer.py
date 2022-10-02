class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_of_dg = 1
        sum_of_dg = 0
        
        while n:
            dg = n % 10
            product_of_dg *= dg
            sum_of_dg += dg
            n //= 10
        
        return product_of_dg - sum_of_dg
        