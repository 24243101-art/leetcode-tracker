# Last updated: 7/9/2026, 10:11:06 AM
class Solution(object):
    def jump(self, nums):
        jumps = 0
        cur_end = 0
        cur_farthest = 0

        for i in range(len(nums) - 1): 
            cur_farthest = max(cur_farthest, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = cur_farthest

        return jumps
