class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        return s
    
one = Solution()

input_1 = one.reverseString(["h","e","l","l","o"])
print(input_1) # ['o', 'l', 'l', 'e', 'h']

input_2 = one.reverseString(["H","a","n","n","a","h"])
print(input_2) # ['h', 'a', 'n', 'n', 'a', 'H']

