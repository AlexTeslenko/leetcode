class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        correct_oreder_words = ['' for word in words]
        
        for word in words:
            idx = int(word[-1]) - 1
            correct_oreder_words[idx] = word[:-1]
        
        return ' '.join(correct_oreder_words)
        