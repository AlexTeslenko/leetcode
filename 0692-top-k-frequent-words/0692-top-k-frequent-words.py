from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_num = Counter(words)
        nums_word = {}
        for word, num in words_num.items():
            if num not in nums_word:
                nums_word[num] = []
            nums_word[num].append(word)
        
        for num in nums_word:
            nums_word[num].sort()
        
        nums_sorted = list(nums_word.items())
        nums_sorted.sort(key=lambda x: x[0], reverse=True)
        
        output = []
        i = 0
        while i < k:
            for item in nums_sorted:
                for word in item[1]:
                    i += 1
                    output.append(word)
                    if i == k:
                        return output
            
        
        return output
        