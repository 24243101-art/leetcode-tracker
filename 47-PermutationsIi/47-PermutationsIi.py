# Last updated: 7/9/2026, 10:11:03 AM
class Solution(object):
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack([])
        return res
