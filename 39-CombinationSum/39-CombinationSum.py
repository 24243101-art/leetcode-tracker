# Last updated: 7/9/2026, 10:11:17 AM
class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(list(path))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i]) 
                path.pop()

        backtrack(0, [], 0)
        return res
