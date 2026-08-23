# Last updated: 8/23/2026, 5:42:51 PM
1class Solution:
2    def isAnagram(self, s, t):
3        if len(s) != len(t):
4            return False
5
6        count = [0] * 26
7
8        for i in range(len(s)):
9            count[ord(s[i]) - ord('a')] += 1
10            count[ord(t[i]) - ord('a')] -= 1
11
12        return all(x == 0 for x in count)          