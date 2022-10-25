class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        num_to_power = {}
        powers = []
        for num in range(lo, hi+1):
            total_power = 0
            cur_num = num
            while cur_num != 1:
                if cur_num in num_to_power:
                    total_power +=  num_to_power[cur_num]
                    cur_num = 1
                elif cur_num % 2 == 0:
                    cur_num /= 2
                    total_power += 1
                elif cur_num % 2 != 0:
                    cur_num = 3 * cur_num + 1
                    total_power += 1
                    
            
            num_to_power[num] = total_power
            powers.append((total_power, num))
            
        powers.sort(key=lambda x: x[0])
        
        return powers[k-1][1]
            
        