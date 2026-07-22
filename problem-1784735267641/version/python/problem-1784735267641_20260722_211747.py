# Last updated: 7/22/2026, 9:17:47 PM
1class Solution:
2    def titleToNumber(self, columnTitle):
3        result = 0
4
5        for ch in columnTitle:
6            result = result * 26 + (ord(ch) - ord('A') + 1)
7
8        return result