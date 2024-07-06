class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)   
        for dig in range(n - 1, -1, -1):
            if digits[dig] < 9:
                digits[dig] += 1
                return digits
            digits[dig] = 0
        return [1] + [0] * n