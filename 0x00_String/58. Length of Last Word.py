class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        nl = s.split()
        return len(nl[-1])