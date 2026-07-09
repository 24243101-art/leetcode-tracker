# Last updated: 7/9/2026, 10:09:42 AM
class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for num in nums:
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1
        return i
