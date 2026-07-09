# Last updated: 7/9/2026, 10:10:37 AM
class Solution(object):
    def getPermutation(self, n, k):
        from math import factorial

        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  
        res = []

        for i in range(n, 0, -1):
            f = factorial(i - 1)
            index = k // f
            res.append(nums[index])
            nums.pop(index)
            k %= f

        return ''.join(res)
