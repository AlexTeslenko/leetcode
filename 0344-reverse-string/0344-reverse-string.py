class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_ptr, right_ptr = 0, len(s)-1
        while left_ptr < right_ptr:
            s[left_ptr], s[right_ptr] = s[right_ptr], s[left_ptr]
            left_ptr += 1
            right_ptr -= 1
        