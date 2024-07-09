class Solution:
    def scoreOfString(self, s: str) -> int:
        total_score = 0
        for index in range(len(s) - 1):
            diff = abs(ord(s[index]) - ord(s[index + 1]))
            total_score += diff
        return total_score