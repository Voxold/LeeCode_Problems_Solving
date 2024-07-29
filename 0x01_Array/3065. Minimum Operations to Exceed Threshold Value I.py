class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        count = [num for num in nums if num < k]
        return len(count)