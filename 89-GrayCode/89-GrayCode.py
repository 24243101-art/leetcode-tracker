# Last updated: 7/9/2026, 10:09:22 AM
class Solution:
    def grayCode(self, n):
        return [i ^ (i >> 1) for i in range(1 << n)]
