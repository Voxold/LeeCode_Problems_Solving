class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        subarray_sums = []
        for num in range(n):
            current_sum = 0
            for j in range(num, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
        subarray_sums.sort()
        result = sum(subarray_sums[left-1:right]) % MOD
        return result