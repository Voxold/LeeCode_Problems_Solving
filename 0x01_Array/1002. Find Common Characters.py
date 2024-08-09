from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_freq = Counter(words[0])
    
        for word in words[1:]:
            word_freq = Counter(word)
            for char in common_freq:
                common_freq[char] = min(common_freq[char], word_freq[char])

        result = []
        for char, freq in common_freq.items():
            result.extend([char] * freq)

        return result
