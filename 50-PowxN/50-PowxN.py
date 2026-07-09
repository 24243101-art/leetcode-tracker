# Last updated: 7/9/2026, 10:10:57 AM
class Solution(object):
    def myPow(self, x, n):
        def fastPow(x, n):
            if n == 0:
                return 1.0
            half = fastPow(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            return 1 / fastPow(x, -n)
        else:
            return fastPow(x, n)
