# Last updated: 7/30/2026, 8:31:48 PM
1class Solution:
2    def minimumPushes(self, word):
3        n = len(word)
4        pushes = 0
5
6        for i in range(n):
7            pushes += (i // 8) + 1
8
9        return pushes