class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left_ptr, right_ptr = 0, 0
        cur_k = k
        max_seq = 0
        for right_ptr in range(len(answerKey)):
            if answerKey[right_ptr] == 'F':
                cur_k -= 1
            
            while left_ptr < len(answerKey) and cur_k < 0:
                if answerKey[left_ptr] == 'F':
                    cur_k += 1
                left_ptr += 1
            
            max_seq = max(max_seq, right_ptr - left_ptr + 1)
        
        left_ptr, right_ptr = 0, 0
        cur_k = k
        for right_ptr in range(len(answerKey)):
            if answerKey[right_ptr] == 'T':
                cur_k -= 1
            
            while left_ptr < len(answerKey) and cur_k < 0:
                if answerKey[left_ptr] == 'T':
                    cur_k += 1
                left_ptr += 1
            
            max_seq = max(max_seq, right_ptr - left_ptr + 1)
        
        return max_seq
        