# Last updated: 7/9/2026, 10:11:15 AM
class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def backtrack(start, path, total):
            if total == target:
                res.append(list(path))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i+1, path, total + candidates[i])  
                path.pop()

        backtrack(0, [], 0)
        return res
