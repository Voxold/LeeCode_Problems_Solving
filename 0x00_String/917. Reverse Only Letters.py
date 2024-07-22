class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [char for char in s if char.isalpha()]
        reverse = letters[::-1]
        result = []
        ittering = iter(reverse)
        for char in s :
            if char.isalpha():
                result.append(next(ittering))
            else:
                result.append(char)
        return ''.join(result)

one = Solution()
print(one.reverseOnlyLetters("ab-cd"))
print(one.reverseOnlyLetters("a-bC-dEf-ghIj"))