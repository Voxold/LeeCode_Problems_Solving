class Solution:
    def findWordsContaining(self, words, x):
        lst = []
        for index, word in enumerate(words):
            if x in word:
                lst.append(index)
        return lst