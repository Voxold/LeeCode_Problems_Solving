class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        word1 = list(''.join(word1))
        word2 = list(''.join(word2))
        return word1 == word2