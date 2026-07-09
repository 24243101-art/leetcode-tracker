# Last updated: 7/9/2026, 10:08:00 AM
class Solution:
    def singleNumber(self, nums):
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
