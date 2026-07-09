# Last updated: 7/9/2026, 10:07:15 AM
class Solution:
    def checkGoodInteger(self, n):
        digits = [int(d) for d in str(n)]
        digitSum = sum(digits)
        squareSum = sum(d * d for d in digits)
        return squareSum - digitSum >= 50
