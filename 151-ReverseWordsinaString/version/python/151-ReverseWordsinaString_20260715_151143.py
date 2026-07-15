# Last updated: 7/15/2026, 3:11:43 PM
1class Solution:
2    def reverseWords(self, s):
3        words = s.split()
4        words.reverse()
5        return " ".join(words)