class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        output_sentence = ''
        for i, word in enumerate(words):
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += 'a' + 'a' * i
            output_sentence += word + " "
        
        return output_sentence.strip()