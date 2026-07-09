# Last updated: 7/9/2026, 10:08:02 AM
class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num   
        return result
