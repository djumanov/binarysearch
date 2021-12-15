class Solution:
    def solve(self, sentence):
        sentence = sentence.split(sep=" ")
        sentence.reverse()
        return " ".join(sentence)