# Last updated: 7/22/2026, 9:15:26 PM
1class Solution:
2    def convertToTitle(self, columnNumber):
3        result = ""
4
5        while columnNumber > 0:
6            columnNumber -= 1
7            result = chr(columnNumber % 26 + ord('A')) + result
8            columnNumber //= 26
9
10        return result