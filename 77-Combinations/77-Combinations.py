# Last updated: 7/9/2026, 10:09:46 AM
class Solution(object):
    def combine(self, n, k):
        res = []
        
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(list(comb))
                return
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack(1, [])
        return res
