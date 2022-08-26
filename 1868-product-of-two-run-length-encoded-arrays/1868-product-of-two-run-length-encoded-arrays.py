class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        result = []
        encoded1_ptr, encoded2_ptr = 0, 0
        while encoded1_ptr < len(encoded1) and encoded2_ptr < len(encoded2):
            cur_encoded_num1 = encoded1[encoded1_ptr]
            cur_encoded_num2 = encoded2[encoded2_ptr]
            
            product = cur_encoded_num1[0] * cur_encoded_num2[0]
            freq = min(cur_encoded_num1[1], cur_encoded_num2[1])
            
            encoded1[encoded1_ptr][1] -= freq
            encoded2[encoded2_ptr][1] -= freq
            
            if encoded1[encoded1_ptr][1] == 0:
                encoded1_ptr += 1
            
            if encoded2[encoded2_ptr][1] == 0:
                encoded2_ptr += 1
                
            
            if not result or result[-1][0] != product:
                result.append([product, freq])
            else:
                result[-1][1] += freq
        
        return result