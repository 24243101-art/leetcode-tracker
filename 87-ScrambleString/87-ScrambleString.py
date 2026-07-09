# Last updated: 7/9/2026, 10:09:25 AM
class Solution:
    def isScramble(self, s1, s2):
        memo = {}

        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False

            n = len(a)
            for i in range(1, n):
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dfs(s1, s2)
