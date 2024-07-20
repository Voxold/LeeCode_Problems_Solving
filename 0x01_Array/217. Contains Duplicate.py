class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        st = set(nums)
        return len(nums) != len(st)
    