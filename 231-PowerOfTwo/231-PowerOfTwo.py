# Last updated: 7/9/2026, 10:07:31 AM
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        return (n & (n - 1)) == 0  
        