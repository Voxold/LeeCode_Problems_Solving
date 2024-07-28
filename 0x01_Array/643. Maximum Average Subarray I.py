class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        summ = sum(nums[:k])
        max_sum = summ

        for i in range(k, len(nums)):
            summ += nums[i] - nums[i - k]
            max_sum = max(max_sum, summ)
            
        return max_sum / k