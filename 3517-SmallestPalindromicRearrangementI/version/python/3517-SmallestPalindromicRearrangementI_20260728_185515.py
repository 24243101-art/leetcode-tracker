# Last updated: 7/28/2026, 6:55:15 PM
1class Solution:
2    def smallestPalindrome(self, s):
3        freq = {}
4
5        for ch in s:
6            freq[ch] = freq.get(ch, 0) + 1
7
8        left = []
9        mid = ""
10
11        for ch in sorted(freq.keys()):
12            left.append(ch * (freq[ch] // 2))
13            if freq[ch] % 2 == 1:
14                mid = ch
15
16        left = "".join(left)
17
18        return left + mid + left[::-1]