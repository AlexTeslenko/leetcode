class Solution:
    def countSubstrings(self, s: str) -> int:
        num_paindrs = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    #print(s[i:j])
                    num_paindrs += 1
        return num_paindrs