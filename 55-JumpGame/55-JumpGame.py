# Last updated: 7/9/2026, 10:10:47 AM
class Solution(object):
    def canJump(self, nums):
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return True
