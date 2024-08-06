from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freqs = Counter(word).values()
        sorted_freqs = sorted(freqs, reverse=True)
        weighted_sum = sum(freq * (i // 8 + 1) for i, freq in enumerate(sorted_freqs))

        return weighted_sum
