class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()

        def backtrack(start, path, target):
            if target == 0:
                result.append(path)
                return
            for number in range(start, len(candidates)):
                if number > start and candidates[number] == candidates[number - 1]:
                    continue
                if candidates[number] > target:
                    break
                backtrack(number + 1, path + [candidates[number]], target - candidates[number])

        backtrack(0, [], target)
        return result